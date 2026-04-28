#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from workspace import resolve_workspace

import generic_ingest_organoid_sources as ingest
import wiki as wiki_cli


SEOUL = ZoneInfo("Asia/Seoul")
TOP_SCAN_CHARS = 6000
PRUNED_STATUS = "pruned"

MARKER_RULES = [
    (
        "conference abstract supplement",
        [
            r"abstract citation id",
            r"^abstracts\s*$",
            r"abstracts\s*/",
            r"agaabstracts",
            r"poster presentation",
            r"podium presentation",
            r"not published at author(?:'|’)?s request",
            r"^#\d+:",
            r"^[A-Z]{2,}\d{2}-\d{2}\b",
            r"^[A-Z]{2,4}\d{2,}(?:\s+\|\s+[A-Z]{2,8}\d{2,})?\s+[A-Z]",
        ],
    ),
    (
        "secondary review article",
        [
            r"minireviews?",
            r"^review\s*$",
            r"\breview article\b",
            r"\bin this review\b",
        ],
    ),
    (
        "cover or promotional blurb",
        [
            r"cover depicts",
            r"front cover",
            r"inside cover",
            r"back cover",
        ],
    ),
]


@dataclass
class Candidate:
    stem: str
    title: str
    page_path: Path
    reasons: list[str]
    evidence: list[str]


def now() -> datetime:
    return datetime.now(SEOUL)


def parsed_markdown_path(root: Path, stem: str) -> Path:
    return root / "raw" / "derived" / "opendataloader" / stem / f"{stem}.md"


def read_top(path: Path, limit: int = TOP_SCAN_CHARS) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")[:limit]


def normalized_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def candidate_for_page(root: Path, page_path: Path) -> Candidate | None:
    text = page_path.read_text(encoding="utf-8")
    frontmatter = ingest.parse_frontmatter(text)
    if frontmatter.get("status") == PRUNED_STATUS:
        return None

    stem = page_path.stem
    parsed_md = read_top(parsed_markdown_path(root, stem))
    title = frontmatter.get("title") or stem.replace("_", " ")

    reasons: list[str] = []
    evidence: list[str] = []
    for reason, patterns in MARKER_RULES:
        matched = []
        for pattern in patterns:
            if re.search(pattern, parsed_md, re.I | re.M):
                matched.append(pattern)
        if matched:
            reasons.append(reason)
            evidence.extend(matched)

    lowered = parsed_md.lower()
    if (
        "www.advancedscience.com" in lowered
        and "vol." in lowered
        and title.lower() not in lowered
        and "abstract" not in lowered
        and "introduction" not in lowered
    ):
        reasons.append("cover or promotional blurb")
        evidence.extend(["www.advancedscience.com", "vol. issue cover without article body"])

    if not reasons:
        return None
    return Candidate(
        stem=stem,
        title=title,
        page_path=page_path,
        reasons=dedupe(reasons),
        evidence=dedupe(evidence),
    )


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        ordered.append(item)
        seen.add(item)
    return ordered


def update_frontmatter(text: str, reason_text: str, stamp: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return text

    lines = parts[1].splitlines()
    updated: list[str] = []
    status_seen = False
    prune_reason_seen = False
    pruned_seen = False
    for line in lines:
        if line.startswith("status:"):
            updated.append(f"status: {PRUNED_STATUS}")
            status_seen = True
            continue
        if line.startswith("prune_reason:"):
            updated.append(f"prune_reason: {reason_text}")
            prune_reason_seen = True
            continue
        if line.startswith("pruned:"):
            updated.append(f"pruned: {stamp}")
            pruned_seen = True
            continue
        updated.append(line)
    if not status_seen:
        updated.append(f"status: {PRUNED_STATUS}")
    if not prune_reason_seen:
        updated.append(f"prune_reason: {reason_text}")
    if not pruned_seen:
        updated.append(f"pruned: {stamp}")
    return "---\n" + "\n".join(updated) + "\n---\n" + parts[2]


def upsert_corpus_status_section(text: str, reason_text: str, evidence: list[str], stamp: str) -> str:
    evidence_text = ", ".join(f"`{item}`" for item in evidence[:6]) or "`manual review`"
    block = (
        "## Corpus status\n\n"
        f"- Active corpus status: pruned on {stamp}\n"
        f"- Reason: {reason_text}\n"
        f"- Basis from parsed PDF: {evidence_text}\n"
        "- Note: the raw PDF is retained for traceability, but this source is excluded from the active organoid corpus, source index, and rebuilt manifest.\n"
    )
    pattern = re.compile(r"(## Corpus status\n\n.*?)(?=\n## |\Z)", re.S)
    if pattern.search(text):
        return pattern.sub(block + "\n", text, count=1)
    heading = re.search(r"^# .+?$", text, re.M)
    if not heading:
        return text.rstrip() + "\n\n" + block + "\n"
    insert_at = heading.end()
    return text[:insert_at] + "\n\n" + block + "\n" + text[insert_at:].lstrip("\n")


def replace_status_bullet(text: str, stamp: str) -> str:
    return re.sub(
        r"^- Status:.*$",
        f"- Status: pruned from active corpus on {stamp}",
        text,
        count=1,
        flags=re.M,
    )


def prune_page(candidate: Candidate, stamp: str) -> None:
    text = candidate.page_path.read_text(encoding="utf-8")
    reason_text = "; ".join(candidate.reasons)
    text = update_frontmatter(text, reason_text, stamp)
    text = replace_status_bullet(text, stamp)
    text = upsert_corpus_status_section(text, reason_text, candidate.evidence, stamp)
    candidate.page_path.write_text(text, encoding="utf-8")


def report_filename() -> str:
    return now().strftime("%Y%m%d_%H%M%S_organoid-corpus-lint-prune-pass.md")


def render_report(root: Path, candidates: list[Candidate], stamp: str) -> str:
    total_sources = sum(
        1
        for path in (root / "wiki" / "sources").glob("*.md")
        if ingest.parse_frontmatter(path.read_text(encoding="utf-8")).get("status") != PRUNED_STATUS
    )
    lines = [
        "---",
        'title: "Organoid corpus lint and prune pass"',
        "status: active",
        f"created: {now().isoformat(timespec='seconds')}",
        "---",
        "",
        "# 100편 organoid corpus lint/prune pass",
        "",
        "## Scope",
        "",
        "- Goal: remove low-signal additions from the active organoid corpus without deleting raw PDFs.",
        "- Rule: keep raw sources for traceability, but mark non-primary or non-article items as `status: pruned` so they drop out of the active source list and manifest.",
        f"- Run date: {stamp}",
        "",
        "## Result",
        "",
        f"- Pruned in this pass: {len(candidates)}",
        f"- Active source pages remaining: {total_sources}",
        "- Raw PDFs retained: yes",
        "",
        "## Pruned sources",
        "",
    ]

    for candidate in candidates:
        reason_text = "; ".join(candidate.reasons)
        evidence_text = ", ".join(f"`{item}`" for item in candidate.evidence[:6])
        lines.append(
            f"- [{candidate.title}](../sources/{candidate.page_path.name})"
            f" - {reason_text}; evidence: {evidence_text}"
        )

    lines.extend(
        [
            "",
            "## Decision rule used in this pass",
            "",
            "- Prune conference-supplement abstracts, poster/podium abstracts, and non-archival abstract pages.",
            "- Prune review/minireview pages that do not function as primary evidence in this protocol-heavy corpus.",
            "- Prune cover or promotional blurbs that are not the actual article text.",
            "",
            "## What remains to watch",
            "",
            "- Some retained papers may still be weak fits for a protocol-focused corpus even if they are full articles.",
            "- Query and concept pages may still cite pruned source pages; the pages remain on disk so those links do not break, but they should not be used as first-choice evidence.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def rebuild_artifacts(root: Path) -> None:
    ingest.update_index(root / "wiki" / "index.md", root / "wiki" / "sources")
    ingest.update_overview(root / "wiki" / "overview.md", root / "wiki" / "sources")
    subprocess.run(
        [sys.executable, str(Path(__file__).resolve().parent / "rebuild_organoid_manifest.py"), "--collection", root.name],
        cwd=str(Path(__file__).resolve().parent.parent),
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint and prune low-signal organoid corpus additions.")
    parser.add_argument("--collection", default="Organoid")
    parser.add_argument("--workspace")
    parser.add_argument("--apply", action="store_true", help="Apply pruning decisions to source pages and collection metadata.")
    args = parser.parse_args()

    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="Organoid",
    )
    root = workspace.root
    wiki_cli.configure_workspace(root)
    wiki_cli.ensure_layout()

    candidates = []
    for page_path in sorted((root / "wiki" / "sources").glob("*.md")):
        candidate = candidate_for_page(root, page_path)
        if candidate is not None:
            candidates.append(candidate)

    print(f"Lint found {len(candidates)} prune candidates")
    for candidate in candidates:
        reason_text = "; ".join(candidate.reasons)
        print(f"- {candidate.page_path.name}: {reason_text}")

    if not args.apply:
        return

    stamp = now().date().isoformat()
    for candidate in candidates:
        prune_page(candidate, stamp)

    report_path = root / "wiki" / "queries" / report_filename()
    report_path.write_text(render_report(root, candidates, stamp), encoding="utf-8")
    wiki_cli.insert_index_entry(
        "Queries",
        f"- [Organoid corpus lint/prune pass](queries/{report_path.name}) - low-signal source cleanup for the 100-paper expansion.",
    )
    rebuild_artifacts(root)
    wiki_cli.append_log(
        "lint prune",
        "Organoid 100-paper corpus",
        [
            f"Marked {len(candidates)} source pages as pruned from the active corpus.",
            f"Saved lint/prune report {wiki_cli.repo_rel(report_path)}.",
            "Rebuilt wiki/index.md, wiki/overview.md, and organoid_protocols_manifest.tsv after pruning.",
            "Retained raw PDFs for traceability while excluding pruned pages from the active source list.",
        ],
    )


if __name__ == "__main__":
    main()
