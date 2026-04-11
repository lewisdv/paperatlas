#!/usr/bin/env python3

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

from workspace import PROJECT_ROOT, resolve_workspace


ROOT = PROJECT_ROOT
RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
SOURCE_DIR = RAW_DIR / "sources"
ASSET_DIR = RAW_DIR / "assets"
SOURCE_PAGES_DIR = WIKI_DIR / "sources"
ENTITY_DIR = WIKI_DIR / "entities"
CONCEPT_DIR = WIKI_DIR / "concepts"
QUERY_DIR = WIKI_DIR / "queries"
SYNTHESIS_DIR = WIKI_DIR / "syntheses"
INDEX_PATH = WIKI_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"
OVERVIEW_PATH = WIKI_DIR / "overview.md"

REQUIRED_DIRS = [
    SOURCE_DIR,
    ASSET_DIR,
    SOURCE_PAGES_DIR,
    ENTITY_DIR,
    CONCEPT_DIR,
    QUERY_DIR,
    SYNTHESIS_DIR,
]


def configure_workspace(root: Path):
    global ROOT, RAW_DIR, WIKI_DIR, SOURCE_DIR, ASSET_DIR
    global SOURCE_PAGES_DIR, ENTITY_DIR, CONCEPT_DIR, QUERY_DIR, SYNTHESIS_DIR
    global INDEX_PATH, LOG_PATH, OVERVIEW_PATH, REQUIRED_DIRS

    ROOT = root
    RAW_DIR = ROOT / "raw"
    WIKI_DIR = ROOT / "wiki"
    SOURCE_DIR = RAW_DIR / "sources"
    ASSET_DIR = RAW_DIR / "assets"
    SOURCE_PAGES_DIR = WIKI_DIR / "sources"
    ENTITY_DIR = WIKI_DIR / "entities"
    CONCEPT_DIR = WIKI_DIR / "concepts"
    QUERY_DIR = WIKI_DIR / "queries"
    SYNTHESIS_DIR = WIKI_DIR / "syntheses"
    INDEX_PATH = WIKI_DIR / "index.md"
    LOG_PATH = WIKI_DIR / "log.md"
    OVERVIEW_PATH = WIKI_DIR / "overview.md"
    REQUIRED_DIRS = [
        SOURCE_DIR,
        ASSET_DIR,
        SOURCE_PAGES_DIR,
        ENTITY_DIR,
        CONCEPT_DIR,
        QUERY_DIR,
        SYNTHESIS_DIR,
    ]


def now():
    return datetime.now().astimezone()


def repo_rel(path):
    return path.resolve().relative_to(ROOT)


def slugify(text):
    lowered = text.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", lowered)
    normalized = normalized.strip("-")
    return normalized or "item"


def ensure_layout():
    for directory in REQUIRED_DIRS:
        directory.mkdir(parents=True, exist_ok=True)

    if not INDEX_PATH.exists():
        INDEX_PATH.write_text(
            "# Index\n\n"
            "## Overview\n\n"
            "- [Overview](overview.md) - top-level summary of the current collection.\n\n"
            "## Sources\n\n"
            "## Entities\n\n"
            "## Concepts\n\n"
            "## Queries\n\n"
            "## Syntheses\n",
            encoding="utf-8",
        )

    if not LOG_PATH.exists():
        LOG_PATH.write_text("# Log\n", encoding="utf-8")

    if not OVERVIEW_PATH.exists():
        OVERVIEW_PATH.write_text(
            "# Overview\n\nThis wiki is ready for ingestion.\n",
            encoding="utf-8",
        )


def insert_index_entry(section_name, entry_line):
    text = INDEX_PATH.read_text(encoding="utf-8")
    if entry_line in text:
        return

    lines = text.splitlines()
    header = "## %s" % section_name
    section_start = None
    section_end = len(lines)

    for i, line in enumerate(lines):
        if line.strip() == header:
            section_start = i
            break

    if section_start is None:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n%s\n\n%s\n" % (header, entry_line)
        INDEX_PATH.write_text(text, encoding="utf-8")
        return

    for i in range(section_start + 1, len(lines)):
        if lines[i].startswith("## "):
            section_end = i
            break

    insertion = [entry_line]
    if section_end == section_start + 1:
        insertion.append("")

    updated = lines[:section_end] + insertion + lines[section_end:]
    INDEX_PATH.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")


def append_log(kind, title, bullets):
    timestamp = now().strftime("%Y-%m-%d %H:%M %Z")
    entry_lines = ["", "## [%s] %s | %s" % (timestamp, kind, title), ""]
    entry_lines.extend("- %s" % bullet for bullet in bullets)
    LOG_PATH.write_text(
        LOG_PATH.read_text(encoding="utf-8").rstrip() + "\n" + "\n".join(entry_lines) + "\n",
        encoding="utf-8",
    )


def count_files(directory, pattern="*"):
    return sum(1 for path in directory.rglob(pattern) if path.is_file())


def unique_path(path):
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 2
    while True:
        candidate = parent / ("%s-%d%s" % (stem, counter, suffix))
        if not candidate.exists():
            return candidate
        counter += 1


def build_source_page(title, kind, copied_source, source_page):
    link_to_raw = Path("../../") / repo_rel(copied_source)
    created = now().isoformat(timespec="seconds")
    return (
        "---\n"
        "title: %s\n"
        "kind: %s\n"
        "status: queued\n"
        "added: %s\n"
        "raw_source: %s\n"
        "---\n\n"
        "# %s\n\n"
        "## Source\n\n"
        "- File: [%s](%s)\n"
        "- Added: %s\n\n"
        "## Summary\n\n"
        "Pending ingest.\n\n"
        "## Key Claims\n\n"
        "- Pending ingest.\n\n"
        "## Open Questions\n\n"
        "- Pending ingest.\n"
    ) % (
        title,
        kind,
        created,
        repo_rel(copied_source),
        title,
        repo_rel(copied_source),
        link_to_raw.as_posix(),
        created,
    )


def create_source_page_for_file(source_file, title, kind):
    page_name = source_file.stem + ".md"
    source_page = unique_path(SOURCE_PAGES_DIR / page_name)
    source_page.write_text(
        build_source_page(title, kind, source_file, source_page),
        encoding="utf-8",
    )

    insert_index_entry(
        "Sources",
        "- [%s](sources/%s) - %s source queued for ingest."
        % (title, source_page.name, kind),
    )
    append_log(
        "ingest queued",
        title,
        [
            "Registered raw source %s." % repo_rel(source_file),
            "Created source page %s." % repo_rel(source_page),
        ],
    )
    return source_page


def command_init(_args):
    ensure_layout()
    print("Workspace initialized at %s" % ROOT)
    print("Raw sources: %s" % repo_rel(SOURCE_DIR))
    print("Wiki root: %s" % repo_rel(WIKI_DIR))
    return 0


def command_status(_args):
    ensure_layout()

    raw_count = count_files(SOURCE_DIR)
    source_page_count = count_files(SOURCE_PAGES_DIR, "*.md")
    entity_count = count_files(ENTITY_DIR, "*.md")
    concept_count = count_files(CONCEPT_DIR, "*.md")
    query_count = count_files(QUERY_DIR, "*.md")
    synthesis_count = count_files(SYNTHESIS_DIR, "*.md")

    log_lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
    recent = [line for line in log_lines if line.startswith("## [")][-5:]

    print("paper_collect status")
    print("")
    print("root: %s" % ROOT)
    print("raw sources: %d" % raw_count)
    print("source pages: %d" % source_page_count)
    print("entity pages: %d" % entity_count)
    print("concept pages: %d" % concept_count)
    print("query pages: %d" % query_count)
    print("synthesis pages: %d" % synthesis_count)
    print("")
    print("key files:")
    print("- %s" % repo_rel(INDEX_PATH))
    print("- %s" % repo_rel(LOG_PATH))
    print("- %s" % repo_rel(OVERVIEW_PATH))

    if recent:
        print("")
        print("recent log entries:")
        for line in recent:
            print("- %s" % line[3:])

    return 0


def command_add_source(args):
    ensure_layout()

    source_path = Path(args.path).expanduser().resolve()
    if not source_path.exists() or not source_path.is_file():
        print("Source file not found: %s" % source_path, file=sys.stderr)
        return 1

    title = args.title or source_path.stem.replace("_", " ").replace("-", " ").strip()
    source_slug = slugify(title)
    timestamp = now().strftime("%Y%m%d_%H%M%S")
    copied_source = unique_path(SOURCE_DIR / ("%s_%s%s" % (timestamp, source_slug, source_path.suffix)))
    shutil.copy2(source_path, copied_source)

    source_page = create_source_page_for_file(copied_source, title, args.kind)

    print("Queued source: %s" % title)
    print("raw file: %s" % repo_rel(copied_source))
    print("wiki page: %s" % repo_rel(source_page))
    print("")
    print("Next step:")
    print(
        "Ask Codex to ingest %s and update the wiki according to AGENTS.md."
        % repo_rel(copied_source)
    )
    return 0


def command_register_source(args):
    ensure_layout()

    source_path = Path(args.path).expanduser().resolve()
    if not source_path.exists() or not source_path.is_file():
        print("Source file not found: %s" % source_path, file=sys.stderr)
        return 1

    try:
        source_path.relative_to(SOURCE_DIR.resolve())
    except ValueError:
        print(
            "Source file must already be inside %s" % SOURCE_DIR.resolve(),
            file=sys.stderr,
        )
        return 1

    title = args.title or source_path.stem.replace("_", " ").replace("-", " ").strip()
    source_page = create_source_page_for_file(source_path, title, args.kind)

    print("Registered source: %s" % title)
    print("raw file: %s" % repo_rel(source_path))
    print("wiki page: %s" % repo_rel(source_page))
    return 0


def command_new_query(args):
    ensure_layout()

    title = args.title.strip()
    slug = slugify(title)
    timestamp = now().strftime("%Y%m%d_%H%M%S")
    query_path = unique_path(QUERY_DIR / ("%s_%s.md" % (timestamp, slug)))
    created = now().isoformat(timespec="seconds")
    question = args.question or title

    query_path.write_text(
        "---\n"
        "title: %s\n"
        "status: open\n"
        "created: %s\n"
        "---\n\n"
        "# %s\n\n"
        "## Question\n\n"
        "%s\n\n"
        "## Working Answer\n\n"
        "Pending analysis.\n\n"
        "## Pages Consulted\n\n"
        "- Pending.\n\n"
        "## Follow-up\n\n"
        "- Pending.\n"
        % (title, created, title, question),
        encoding="utf-8",
    )

    insert_index_entry(
        "Queries",
        "- [%s](queries/%s) - saved research question."
        % (title, query_path.name),
    )
    append_log(
        "query created",
        title,
        ["Created query page %s." % repo_rel(query_path)],
    )

    print("Created query page: %s" % repo_rel(query_path))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description="Manage the paper_collect wiki workspace.")
    parser.add_argument(
        "--collection",
        help="Collection name under collections/, for example longread-sequencing or organoid.",
    )
    parser.add_argument(
        "--workspace",
        help="Explicit workspace path. Overrides --collection.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create the base workspace layout.")
    init_parser.set_defaults(func=command_init)

    status_parser = subparsers.add_parser("status", help="Show workspace status.")
    status_parser.set_defaults(func=command_status)

    add_source_parser = subparsers.add_parser("add-source", help="Copy a source into raw/sources and create a stub source page.")
    add_source_parser.add_argument("path", help="Path to a local file.")
    add_source_parser.add_argument("--title", help="Optional human-readable title.")
    add_source_parser.add_argument(
        "--kind",
        default="paper",
        choices=["paper", "article", "book", "note", "dataset", "other"],
        help="Source type label for the wiki page.",
    )
    add_source_parser.set_defaults(func=command_add_source)

    register_source_parser = subparsers.add_parser(
        "register-source",
        help="Create a source page for a file that already exists in raw/sources.",
    )
    register_source_parser.add_argument("path", help="Path to a local file inside raw/sources.")
    register_source_parser.add_argument("--title", help="Optional human-readable title.")
    register_source_parser.add_argument(
        "--kind",
        default="paper",
        choices=["paper", "article", "book", "note", "dataset", "other"],
        help="Source type label for the wiki page.",
    )
    register_source_parser.set_defaults(func=command_register_source)

    new_query_parser = subparsers.add_parser("new-query", help="Create a saved query page.")
    new_query_parser.add_argument("title", help="Short title for the query.")
    new_query_parser.add_argument("--question", help="Optional full question text.")
    new_query_parser.set_defaults(func=command_new_query)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="longread-sequencing",
    )
    configure_workspace(workspace.root)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
