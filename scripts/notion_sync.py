#!/usr/bin/env python3
"""Notion 'reference paper hub' -> wiki ingestion CLI.

Designed to be driven by Claude (which reads Notion via MCP). This script handles
the local side: state tracking, PDF download via DOI, wiki file creation, log
appending. It does NOT itself call Notion — Claude passes structured paper info
via the `ingest` subcommand.

Subcommands:
  config                            Dump the resolved hub→collection mapping.
  is-ingested  --page-id <id>       Exit 0 if the Notion page has been ingested,
                                    1 otherwise. Useful for dedup checks.
  status                            Per-hub counts of ingested papers + last sync.
  ingest       --page-id ... \
               --collection ... \
               --title ... \
               --doi ... \
               --notion-url ... \
               [--one-line ...] \
               [--task-relevance ...] \
               [--key-results ...] \
               [--hub-label ...]    Run the full ingest: download PDF if possible,
                                    create wiki/sources/<slug>.md, update state.
  forget       --page-id <id>       Remove a page from state (re-ingestable).

State file: scripts/.notion_sync_state.json (gitignored).
Config:     scripts/notion_sync_config.json (committed).
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = SCRIPTS_DIR / "notion_sync_config.json"
STATE_PATH = SCRIPTS_DIR / ".notion_sync_state.json"
COLLECTIONS_DIR = ROOT / "collections"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"Missing config: {CONFIG_PATH}")
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"version": 1, "ingested_pages": {}, "last_sync": None}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def slugify_filename(text: str, max_len: int = 60) -> str:
    """Produce an ASCII-only filename stem. Drops non-ASCII (e.g. Korean) and caps length at a word boundary."""
    ascii_only = re.sub(r"[^A-Za-z0-9]+", "_", text.strip())
    ascii_only = re.sub(r"_+", "_", ascii_only).strip("_-")
    if not ascii_only:
        ascii_only = "paper"
    if len(ascii_only) <= max_len:
        return ascii_only
    truncated = ascii_only[:max_len]
    last_sep = truncated.rfind("_")
    if last_sep > max_len * 0.6:
        truncated = truncated[:last_sep]
    return truncated.rstrip("_-")


def insert_index_entry(collection_root: Path, section_name: str, entry_line: str) -> None:
    """Append entry_line under '## section_name' in <collection>/wiki/index.md.
    Mirrors scripts/wiki.py:insert_index_entry semantics."""
    index_path = collection_root / "wiki" / "index.md"
    if not index_path.exists():
        return
    text = index_path.read_text(encoding="utf-8")
    if entry_line in text:
        return
    lines = text.splitlines()
    header = f"## {section_name}"
    section_start = None
    for i, line in enumerate(lines):
        if line.strip() == header:
            section_start = i
            break
    if section_start is None:
        if not text.endswith("\n"):
            text += "\n"
        text += f"\n{header}\n\n{entry_line}\n"
        index_path.write_text(text, encoding="utf-8")
        return
    section_end = len(lines)
    for i in range(section_start + 1, len(lines)):
        if lines[i].startswith("## "):
            section_end = i
            break
    insertion = [entry_line]
    if section_end == section_start + 1:
        insertion.append("")
    updated = lines[:section_end] + insertion + lines[section_end:]
    index_path.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")


def collection_root(collection: str) -> Path:
    direct = COLLECTIONS_DIR / collection
    if direct.exists():
        return direct
    # Try case-insensitive match
    for path in COLLECTIONS_DIR.iterdir():
        if path.is_dir() and path.name.casefold() == collection.casefold():
            return path
    sys.exit(f"Collection '{collection}' not found under {COLLECTIONS_DIR}")


def cmd_config(args: argparse.Namespace) -> int:
    cfg = load_config()
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    cfg = load_config()
    state = load_state()
    ingested = state.get("ingested_pages", {})
    print(f"Last sync: {state.get('last_sync') or 'never'}")
    print(f"Total ingested: {len(ingested)}")
    print("")
    # Group ingested by hub label
    by_hub: Dict[str, int] = {}
    by_collection: Dict[str, int] = {}
    for entry in ingested.values():
        by_hub[entry.get("hub_label", "?")] = by_hub.get(entry.get("hub_label", "?"), 0) + 1
        by_collection[entry.get("collection", "?")] = by_collection.get(entry.get("collection", "?"), 0) + 1

    print("Configured hubs:")
    for hub in cfg.get("hubs", []):
        label = hub.get("label", hub.get("notion_page_id"))
        coll = hub.get("collection")
        n = by_hub.get(label, 0)
        print(f"  [{coll:>22s}] {n:4d} ingested  ←  {label}")

    print("")
    print("By collection:")
    for coll, n in sorted(by_collection.items()):
        print(f"  {coll:>22s}: {n}")
    return 0


def cmd_is_ingested(args: argparse.Namespace) -> int:
    state = load_state()
    return 0 if args.page_id in state.get("ingested_pages", {}) else 1


def cmd_forget(args: argparse.Namespace) -> int:
    state = load_state()
    if args.page_id in state.get("ingested_pages", {}):
        del state["ingested_pages"][args.page_id]
        save_state(state)
        print(f"Removed {args.page_id} from state.")
        return 0
    print(f"Page {args.page_id} not in state.", file=sys.stderr)
    return 1


def build_wiki_source_page(
    *,
    title: str,
    doi: Optional[str],
    notion_url: str,
    notion_title: Optional[str],
    hub_label: str,
    pmid: Optional[str],
    pmc: Optional[str],
    one_line: Optional[str],
    task_relevance: Optional[str],
    key_results: Optional[str],
    raw_source_rel: Optional[str],
    pdf_status: str,
) -> str:
    added = now_iso()
    parts: List[str] = []
    parts.append("---")
    parts.append(f"title: {title}")
    parts.append("kind: paper")
    parts.append(f"status: {'queued' if raw_source_rel else 'pending_pdf'}")
    parts.append(f"added: {added}")
    if raw_source_rel:
        parts.append(f"raw_source: {raw_source_rel}")
    if doi:
        parts.append(f"doi: {doi}")
    parts.append(f"notion_url: {notion_url}")
    parts.append(f"notion_hub: {hub_label}")
    if pmid:
        parts.append(f"pmid: {pmid}")
    if pmc:
        parts.append(f"pmc: {pmc}")
    parts.append(f"pdf_status: {pdf_status}")
    parts.append("---")
    parts.append("")
    parts.append(f"# {title}")
    parts.append("")
    parts.append("## Source")
    parts.append("")
    if raw_source_rel:
        link = "../../" + raw_source_rel
        parts.append(f"- File: [{raw_source_rel}]({link})")
    else:
        parts.append(f"- File: _PDF not yet downloaded ({pdf_status})_")
    if doi:
        parts.append(f"- DOI: [{doi}](https://doi.org/{doi})")
    if pmid:
        parts.append(f"- PubMed: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
    if pmc:
        parts.append(f"- PMC: [{pmc}](https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/)")
    notion_link_label = notion_title or hub_label
    parts.append(f"- Notion: [{notion_link_label}]({notion_url})")
    parts.append(f"- Hub: {hub_label}")
    parts.append(f"- Added: {added}")
    parts.append("")
    parts.append("## Notion Summary")
    parts.append("")
    if one_line:
        parts.append(f"**한 줄 요약:** {one_line}")
        parts.append("")
    if task_relevance:
        parts.append("**과제 관련성:**")
        parts.append("")
        parts.append(task_relevance)
        parts.append("")
    if key_results:
        parts.append("**주요 결과:**")
        parts.append("")
        parts.append(key_results)
        parts.append("")
    parts.append("## Summary")
    parts.append("")
    parts.append("Pending ingest.")
    parts.append("")
    parts.append("## Key Claims")
    parts.append("")
    parts.append("- Pending ingest.")
    parts.append("")
    parts.append("## Open Questions")
    parts.append("")
    parts.append("- Pending ingest.")
    parts.append("")
    return "\n".join(parts)


def run_git(args: List[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=60)


def git_sync_paths(paths: List[Path], commit_message: str) -> dict:
    """Stage, commit, and push the given paths. Returns a status dict.

    Returns:
      {"status": "ok"|"skipped"|"failed", "reason": "...", "branch": "...", "commit": "..."}
    """
    rel_paths: List[str] = []
    for p in paths:
        try:
            rel_paths.append(str(p.relative_to(ROOT).as_posix()))
        except ValueError:
            return {"status": "failed", "reason": f"path outside repo: {p}"}

    repo_check = run_git(["rev-parse", "--is-inside-work-tree"], ROOT)
    if repo_check.returncode != 0 or repo_check.stdout.strip() != "true":
        return {"status": "skipped", "reason": "not a git repository"}

    remote_check = run_git(["remote", "get-url", "origin"], ROOT)
    if remote_check.returncode != 0 or not remote_check.stdout.strip():
        return {"status": "skipped", "reason": "origin remote not configured"}

    branch_proc = run_git(["rev-parse", "--abbrev-ref", "HEAD"], ROOT)
    if branch_proc.returncode != 0:
        return {"status": "skipped", "reason": "could not determine current branch"}
    branch = branch_proc.stdout.strip()

    add = run_git(["add", "--", *rel_paths], ROOT)
    if add.returncode != 0:
        return {"status": "failed", "reason": f"git add failed: {add.stderr.strip()}"}

    staged = run_git(["diff", "--cached", "--name-only", "--", *rel_paths], ROOT)
    if staged.returncode != 0:
        return {"status": "failed", "reason": f"git diff failed: {staged.stderr.strip()}"}
    if not staged.stdout.strip():
        return {"status": "skipped", "reason": "nothing staged after filtering paths"}

    commit = run_git(["commit", "-m", commit_message, "--", *rel_paths], ROOT)
    if commit.returncode != 0:
        return {"status": "failed", "reason": f"git commit failed: {commit.stderr.strip() or commit.stdout.strip()}"}

    sha_proc = run_git(["rev-parse", "HEAD"], ROOT)
    sha = sha_proc.stdout.strip()[:7] if sha_proc.returncode == 0 else None

    push = run_git(["push", "origin", branch], ROOT)
    if push.returncode != 0:
        return {
            "status": "committed_not_pushed",
            "reason": f"push failed: {push.stderr.strip() or push.stdout.strip()}",
            "branch": branch,
            "commit": sha,
        }

    return {"status": "ok", "branch": branch, "commit": sha}


def cmd_ingest(args: argparse.Namespace) -> int:
    cfg = load_config()
    state = load_state()

    if args.page_id in state.get("ingested_pages", {}) and not args.force:
        print(f"Already ingested: {args.page_id}. Use --force to re-ingest.", file=sys.stderr)
        return 2

    coll_root = collection_root(args.collection)
    raw_sources = coll_root / "raw" / "sources"
    wiki_sources = coll_root / "wiki" / "sources"
    if not raw_sources.exists() or not wiki_sources.exists():
        sys.exit(f"Collection layout missing under {coll_root}. Run wiki.py init first.")

    slug = slugify_filename(args.title)
    # Disambiguate against existing source pages
    candidate = wiki_sources / f"{slug}.md"
    i = 2
    while candidate.exists():
        candidate = wiki_sources / f"{slug}-{i}.md"
        i += 1
    source_page = candidate

    pdf_status = "skipped"
    raw_source_rel: Optional[str] = None
    pdf_url: Optional[str] = None

    if args.doi and not args.no_download:
        email = cfg.get("unpaywall_email") or "anon@example.com"
        pdf_path = raw_sources / f"{slug}.pdf"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "fetch_paper_by_doi.py"),
                "--doi", args.doi,
                "--out", str(pdf_path),
                "--email", email,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0 and pdf_path.exists():
            pdf_status = "downloaded"
            raw_source_rel = pdf_path.relative_to(coll_root).as_posix()
            try:
                payload = json.loads(result.stdout.strip().splitlines()[-1])
                pdf_url = payload.get("url")
            except Exception:
                pdf_url = None
        else:
            pdf_status = "not_found"
    elif not args.doi:
        pdf_status = "no_doi"

    source_page.write_text(
        build_wiki_source_page(
            title=args.title,
            doi=args.doi,
            notion_url=args.notion_url,
            notion_title=args.notion_title,
            hub_label=args.hub_label or "",
            pmid=args.pmid,
            pmc=args.pmc,
            one_line=args.one_line,
            task_relevance=args.task_relevance,
            key_results=args.key_results,
            raw_source_rel=raw_source_rel,
            pdf_status=pdf_status,
        ),
        encoding="utf-8",
    )

    index_entry = f"- [{args.title}](sources/{source_page.name}) - paper source queued for ingest."
    insert_index_entry(coll_root, "Sources", index_entry)

    # Append to wiki/log.md
    log_path = coll_root / "wiki" / "log.md"
    log_entry = (
        f"\n## {now_iso()} – notion-sync ingest: {args.title}\n\n"
        f"- Hub: {args.hub_label}\n"
        f"- Notion: {args.notion_url}\n"
        f"- DOI: {args.doi or '(none)'}\n"
        f"- PDF: {pdf_status}{' (' + (pdf_url or '') + ')' if pdf_url else ''}\n"
        f"- Source page: wiki/sources/{source_page.name}\n"
    )
    with log_path.open("a", encoding="utf-8") as f:
        f.write(log_entry)

    # Update state
    state.setdefault("ingested_pages", {})[args.page_id] = {
        "collection": args.collection,
        "hub_label": args.hub_label,
        "title": args.title,
        "doi": args.doi,
        "pmid": args.pmid,
        "pmc": args.pmc,
        "pdf_status": pdf_status,
        "pdf_url": pdf_url,
        "source_page": str(source_page.relative_to(ROOT).as_posix()),
        "raw_source": raw_source_rel,
        "notion_url": args.notion_url,
        "ingested_at": now_iso(),
    }
    state["last_sync"] = now_iso()
    save_state(state)

    result: dict = {
        "status": "ok",
        "page_id": args.page_id,
        "collection": args.collection,
        "pdf_status": pdf_status,
        "pdf_url": pdf_url,
        "source_page": str(source_page.relative_to(ROOT).as_posix()),
        "raw_source": raw_source_rel,
    }

    if args.git_sync:
        msg = f"{args.collection}: ingest {args.title} from Notion"
        if len(msg) > 100:
            msg = msg[:97] + "..."
        git_paths = [source_page, log_path]
        result["git"] = git_sync_paths(git_paths, msg)

    print(json.dumps(result, ensure_ascii=False))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Notion → wiki sync helper.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("config", help="Dump config JSON.").set_defaults(func=cmd_config)
    sub.add_parser("status", help="Per-hub ingested counts.").set_defaults(func=cmd_status)

    p_is = sub.add_parser("is-ingested", help="Exit 0 if page ingested, 1 otherwise.")
    p_is.add_argument("--page-id", required=True)
    p_is.set_defaults(func=cmd_is_ingested)

    p_forget = sub.add_parser("forget", help="Remove a page from state.")
    p_forget.add_argument("--page-id", required=True)
    p_forget.set_defaults(func=cmd_forget)

    p_ingest = sub.add_parser("ingest", help="Ingest one Notion paper page.")
    p_ingest.add_argument("--page-id", required=True, help="Notion page UUID.")
    p_ingest.add_argument("--collection", required=True, help="Target wiki collection.")
    p_ingest.add_argument("--title", required=True, help="Paper title (used for filename).")
    p_ingest.add_argument("--doi", help="DOI (10.xxxx/...) or 'arXiv:YYYY.NNNNN'.")
    p_ingest.add_argument("--notion-url", required=True)
    p_ingest.add_argument("--notion-title", help="Notion page title (cleaned of emoji). Falls back to hub label.")
    p_ingest.add_argument("--hub-label", default="", help="Source hub label (for log).")
    p_ingest.add_argument("--pmid", help="PubMed ID (numeric).")
    p_ingest.add_argument("--pmc", help="PMC ID (e.g. PMC12345678).")
    p_ingest.add_argument("--one-line", help="한 줄 요약 from Notion.")
    p_ingest.add_argument("--task-relevance", help="과제 관련성 block from Notion.")
    p_ingest.add_argument("--key-results", help="주요 결과 block from Notion.")
    p_ingest.add_argument("--no-download", action="store_true", help="Skip PDF download.")
    p_ingest.add_argument("--force", action="store_true", help="Re-ingest even if already in state.")
    p_ingest.add_argument(
        "--git-sync",
        action="store_true",
        help="After ingest, git add+commit+push the new wiki source page and log.md to origin/<current-branch>.",
    )
    p_ingest.set_defaults(func=cmd_ingest)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
