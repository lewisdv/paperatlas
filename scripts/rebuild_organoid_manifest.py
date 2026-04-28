#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from workspace import resolve_workspace


SOURCE_METADATA_DIRNAME = "source_metadata"
FIELDNAMES = [
    "published_date",
    "year",
    "first_author",
    "organ",
    "title",
    "article_url",
    "pdf_url",
    "filename",
    "local_path",
    "source_page",
    "focus",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    frontmatter = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def load_json_rows(metadata_dir: Path) -> dict[str, dict]:
    rows = {}
    if not metadata_dir.exists():
        return rows
    for path in metadata_dir.glob("*.json"):
        try:
            rows[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
    return rows


def load_existing_manifest(manifest_path: Path) -> dict[str, dict]:
    if not manifest_path.exists():
        return {}
    rows = {}
    with manifest_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            stem = Path(row.get("filename") or row.get("source_page") or "").stem
            if stem:
                rows[stem] = row
    return rows


def infer_pdf_url(article_url: str, existing: str = "") -> str:
    if existing:
        return existing
    if not article_url:
        return ""
    if "pmc.ncbi.nlm.nih.gov/articles/PMC" in article_url:
        return article_url.rstrip("/") + "/pdf/"
    if "nature.com/articles/" in article_url and not article_url.endswith(".pdf"):
        return article_url + ".pdf"
    return ""


def infer_first_author(stem: str, existing: str = "") -> str:
    if existing:
        return existing
    token = stem.split("_", 1)[0]
    return token.replace("-", " ").title()


def build_row(
    source_page: Path,
    root: Path,
    metadata_rows: dict[str, dict],
    existing_rows: dict[str, dict],
) -> dict | None:
    stem = source_page.stem
    text = source_page.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    if frontmatter.get("status") == "pruned":
        return None
    metadata = dict(existing_rows.get(stem, {}))
    metadata.update(metadata_rows.get(stem, {}))

    local_path = frontmatter.get("raw_source") or metadata.get("local_path") or f"raw/sources/{stem}.pdf"
    filename = Path(local_path).name
    published_date = (
        frontmatter.get("published_date")
        or metadata.get("published_date")
        or metadata.get("firstPublicationDate")
        or existing_rows.get(stem, {}).get("published_date", "")
    )
    year = (
        metadata.get("year")
        or existing_rows.get(stem, {}).get("year")
        or (published_date[:4] if published_date else "")
    )
    article_url = frontmatter.get("article_url") or metadata.get("article_url") or existing_rows.get(stem, {}).get("article_url", "")
    pdf_url = infer_pdf_url(article_url, metadata.get("pdf_url") or existing_rows.get(stem, {}).get("pdf_url", ""))

    return {
        "published_date": published_date,
        "year": year,
        "first_author": metadata.get("first_author") or infer_first_author(stem, existing_rows.get(stem, {}).get("first_author", "")),
        "organ": frontmatter.get("organ") or metadata.get("organ_guess") or existing_rows.get(stem, {}).get("organ", ""),
        "title": frontmatter.get("title") or metadata.get("title") or stem.replace("_", " "),
        "article_url": article_url,
        "pdf_url": pdf_url,
        "filename": filename,
        "local_path": local_path,
        "source_page": str(source_page.relative_to(root)).replace("\\", "/"),
        "focus": frontmatter.get("protocol_focus") or metadata.get("focus_guess") or existing_rows.get(stem, {}).get("focus", ""),
    }


def sort_key(row: dict) -> tuple[str, str]:
    return (row.get("published_date") or "9999-99-99", row.get("title", "").lower())


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild the organoid manifest from current source pages.")
    parser.add_argument("--collection", default="Organoid")
    parser.add_argument("--workspace")
    args = parser.parse_args()

    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="Organoid",
    )
    root = workspace.root
    manifest_path = root / "organoid_protocols_manifest.tsv"
    existing_rows = load_existing_manifest(manifest_path)
    metadata_rows = load_json_rows(root / "raw" / "derived" / SOURCE_METADATA_DIRNAME)

    rows = []
    for path in sorted((root / "wiki" / "sources").glob("*.md")):
        row = build_row(path, root, metadata_rows, existing_rows)
        if row is not None:
            rows.append(row)
    rows.sort(key=sort_key)

    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Rebuilt organoid manifest with {len(rows)} rows")


if __name__ == "__main__":
    main()
