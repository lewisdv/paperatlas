#!/usr/bin/env python3
"""Bulk-call notion_sync.py ingest for a JSON list of paper specs.

Usage:
  python3 scripts/notion_batch_ingest.py path/to/specs.json

specs.json schema:
[
  {
    "page_id": "uuid",
    "collection": "Cancer_Multiomics",
    "title": "Title slug-friendly",
    "notion_title": "Full Notion page title (optional)",
    "doi": "10.xxxx/yyyy",
    "notion_url": "https://www.notion.so/<32hex>",
    "hub_label": "...",
    "pmid": "41454718",       // optional
    "pmc": "PMC12948274",     // optional
    "one_line": "...",        // optional
    "task_relevance": "...",  // optional
    "key_results": "..."      // optional
  },
  ...
]
"""
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
NOTION_SYNC = SCRIPTS / "notion_sync.py"

if len(sys.argv) != 2:
    sys.exit("usage: notion_batch_ingest.py <specs.json>")

specs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
results = []

for spec in specs:
    cmd = [
        sys.executable, str(NOTION_SYNC), "ingest",
        "--page-id", spec["page_id"],
        "--collection", spec["collection"],
        "--title", spec["title"],
        "--notion-url", spec["notion_url"],
        "--hub-label", spec.get("hub_label", ""),
    ]
    for opt, key in [
        ("--doi", "doi"),
        ("--notion-title", "notion_title"),
        ("--pmid", "pmid"),
        ("--pmc", "pmc"),
        ("--one-line", "one_line"),
        ("--task-relevance", "task_relevance"),
        ("--key-results", "key_results"),
    ]:
        if spec.get(key):
            cmd += [opt, spec[key]]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if proc.returncode == 2:
        results.append({"title": spec["title"][:55], "skipped": "already ingested"})
        continue
    if proc.returncode != 0:
        results.append({"title": spec["title"][:55], "error": proc.stderr.strip()[:200]})
        continue
    try:
        out = json.loads(proc.stdout.strip().splitlines()[-1])
        results.append({"title": spec["title"][:55], "pdf": out.get("pdf_status"), "page": Path(out.get("source_page", "")).name})
    except Exception:
        results.append({"title": spec["title"][:55], "raw": proc.stdout.strip()[:200]})

print(json.dumps(results, ensure_ascii=False, indent=2))
print(f"\nDone: {len(results)} papers, {sum(1 for r in results if r.get('pdf')=='downloaded')} PDFs downloaded, {sum(1 for r in results if r.get('skipped'))} skipped, {sum(1 for r in results if r.get('error'))} errors", file=sys.stderr)
