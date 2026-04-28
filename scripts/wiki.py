#!/usr/bin/env python3

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from workspace import PROJECT_ROOT, resolve_workspace


ROOT = PROJECT_ROOT
RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
SOURCE_DIR = RAW_DIR / "sources"
ASSET_DIR = RAW_DIR / "assets"
DERIVED_DIR = RAW_DIR / "derived"
OPENDATALOADER_DIR = DERIVED_DIR / "opendataloader"
SOURCE_PAGES_DIR = WIKI_DIR / "sources"
ENTITY_DIR = WIKI_DIR / "entities"
CONCEPT_DIR = WIKI_DIR / "concepts"
QUERY_DIR = WIKI_DIR / "queries"
SYNTHESIS_DIR = WIKI_DIR / "syntheses"
INDEX_PATH = WIKI_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"
OVERVIEW_PATH = WIKI_DIR / "overview.md"
PRUNED_STATUS = "pruned"

REQUIRED_DIRS = [
    SOURCE_DIR,
    ASSET_DIR,
    DERIVED_DIR,
    OPENDATALOADER_DIR,
    SOURCE_PAGES_DIR,
    ENTITY_DIR,
    CONCEPT_DIR,
    QUERY_DIR,
    SYNTHESIS_DIR,
]


def configure_workspace(root: Path):
    global ROOT, RAW_DIR, WIKI_DIR, SOURCE_DIR, ASSET_DIR
    global DERIVED_DIR, OPENDATALOADER_DIR
    global SOURCE_PAGES_DIR, ENTITY_DIR, CONCEPT_DIR, QUERY_DIR, SYNTHESIS_DIR
    global INDEX_PATH, LOG_PATH, OVERVIEW_PATH, REQUIRED_DIRS

    ROOT = root
    RAW_DIR = ROOT / "raw"
    WIKI_DIR = ROOT / "wiki"
    SOURCE_DIR = RAW_DIR / "sources"
    ASSET_DIR = RAW_DIR / "assets"
    DERIVED_DIR = RAW_DIR / "derived"
    OPENDATALOADER_DIR = DERIVED_DIR / "opendataloader"
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
        DERIVED_DIR,
        OPENDATALOADER_DIR,
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


def display_rel(path):
    resolved = Path(path).resolve()
    try:
        return repo_rel(resolved).as_posix()
    except ValueError:
        return str(path)


def slugify(text):
    lowered = text.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", lowered)
    normalized = normalized.strip("-")
    return normalized or "item"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    data = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


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


def recent_log_headers(limit=5):
    if limit <= 0:
        return []
    log_lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
    return [line for line in log_lines if line.startswith("## [")][-limit:]


def recent_markdown_pages(directory, limit=5):
    if limit <= 0:
        return []
    pages = [path for path in directory.glob("*.md") if path.is_file()]
    pages.sort(key=lambda path: (path.stat().st_mtime, path.name))
    return pages[-limit:]


def registered_source_markers():
    registered = set()
    for path in SOURCE_PAGES_DIR.glob("*.md"):
        if not path.is_file():
            continue
        registered.add(path.stem)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"^raw_source:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if not match:
            continue
        raw_name = Path(match.group(1).strip()).name
        if raw_name:
            registered.add(raw_name)
            registered.add(Path(raw_name).stem)
    return registered


def source_page_frontmatters():
    rows = []
    for path in sorted(SOURCE_PAGES_DIR.glob("*.md")):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rows.append((path, parse_frontmatter(text)))
    return rows


def active_and_pruned_source_counts():
    active = 0
    pruned = 0
    for _path, frontmatter in source_page_frontmatters():
        if frontmatter.get("status") == PRUNED_STATUS:
            pruned += 1
        else:
            active += 1
    return active, pruned


def missing_source_pages():
    registered = registered_source_markers()
    missing = []
    for path in sorted(SOURCE_DIR.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_file():
            continue
        if path.name not in registered and path.stem not in registered:
            missing.append(path)
    return missing


def missing_parsed_sources():
    parsed_stems = {path.name for path in OPENDATALOADER_DIR.iterdir() if path.is_dir()}
    missing = []
    for path in sorted(SOURCE_DIR.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_file():
            continue
        if path.suffix.lower() != ".pdf":
            continue
        if path.stem not in parsed_stems:
            missing.append(path)
    return missing


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


def opendataloader_bin_candidates():
    candidates = []
    env_bin = os.environ.get("OPENDATALOADER_PDF_BIN")
    if env_bin:
        candidates.append(Path(env_bin).expanduser())

    candidates.extend(
        [
            PROJECT_ROOT / ".venv-opendataloader" / "bin" / "opendataloader-pdf",
            ROOT / ".venv-opendataloader" / "bin" / "opendataloader-pdf",
        ]
    )
    return candidates


def find_opendataloader_executable():
    executable = shutil.which("opendataloader-pdf")
    if executable:
        return Path(executable)

    for candidate in opendataloader_bin_candidates():
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def build_opendataloader_env():
    env = os.environ.copy()
    path_parts = []
    java_homes = []

    for candidate in opendataloader_bin_candidates():
        if candidate.exists():
            path_parts.append(str(candidate.parent))

    java_roots = [
        Path("/usr/local/opt/openjdk@21"),
        Path("/usr/local/opt/openjdk"),
        Path("/opt/homebrew/opt/openjdk@21"),
        Path("/opt/homebrew/opt/openjdk"),
    ]
    for root in java_roots:
        bin_dir = root / "bin"
        java_home = root / "libexec" / "openjdk.jdk" / "Contents" / "Home"
        if bin_dir.exists():
            path_parts.append(str(bin_dir))
        if java_home.exists():
            java_homes.append(java_home)

    if path_parts:
        env["PATH"] = ":".join(path_parts + [env.get("PATH", "")]).strip(":")
    if "JAVA_HOME" not in env and java_homes:
        env["JAVA_HOME"] = str(java_homes[0])
    return env


def ensure_source_inside_workspace(source_path):
    try:
        source_path.relative_to(SOURCE_DIR.resolve())
    except ValueError:
        print(
            "Source file must already be inside %s" % SOURCE_DIR.resolve(),
            file=sys.stderr,
        )
        return False
    return True


def humanize_title_from_path(path):
    return path.stem.replace("_", " ").replace("-", " ").strip()


def source_page_marker_block(source_file, generated_files, manifest_path, command_text):
    lines = [
        "<!-- opendataloader:begin -->",
        "## Parsed Artifacts",
        "",
        "- Parser: OpenDataLoader PDF",
        "- Generated: %s" % now().isoformat(timespec="seconds"),
        "- Command: `%s`" % command_text,
        "- Manifest: [%s](%s)"
        % (
            repo_rel(manifest_path),
            (Path("../../") / repo_rel(manifest_path)).as_posix(),
        ),
    ]

    for generated_path in generated_files:
        lines.append(
            "- Output: [%s](%s)"
            % (
                repo_rel(generated_path),
                (Path("../../") / repo_rel(generated_path)).as_posix(),
            )
        )

    lines.extend(
        [
            "",
            "These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.",
            "<!-- opendataloader:end -->",
        ]
    )
    return "\n".join(lines)


def find_source_page_for_file(source_file):
    expected_rel = repo_rel(source_file).as_posix()
    direct_match = SOURCE_PAGES_DIR / ("%s.md" % source_file.stem)
    if direct_match.exists():
        text = direct_match.read_text(encoding="utf-8")
        if ("raw_source: %s" % expected_rel) in text:
            return direct_match

    for path in SOURCE_PAGES_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if ("raw_source: %s" % expected_rel) in text:
            return path
    return None


def update_source_page_parsed_artifacts(source_page, source_file, generated_files, manifest_path, command_text):
    block = source_page_marker_block(
        source_file=source_file,
        generated_files=generated_files,
        manifest_path=manifest_path,
        command_text=command_text,
    )
    text = source_page.read_text(encoding="utf-8")
    start_marker = "<!-- opendataloader:begin -->"
    end_marker = "<!-- opendataloader:end -->"

    if start_marker in text and end_marker in text:
        start_index = text.index(start_marker)
        end_index = text.index(end_marker) + len(end_marker)
        updated = (text[:start_index].rstrip() + "\n\n" + block + "\n").rstrip() + "\n"
    else:
        updated = text.rstrip() + "\n\n" + block + "\n"

    source_page.write_text(updated, encoding="utf-8")


def run_opendataloader_parse(source_path, format_value, use_struct_tree=False, hybrid_backend=None):
    executable = find_opendataloader_executable()
    if executable is None:
        print(
            "OpenDataLoader PDF CLI not found. Install with `./scripts/setup_opendataloader_pdf.sh` or `pip install -U opendataloader-pdf`.",
            file=sys.stderr,
        )
        return None

    output_dir = OPENDATALOADER_DIR / source_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    command = [
        str(executable),
        str(source_path),
        "-o",
        str(output_dir),
        "-f",
        format_value,
    ]
    if use_struct_tree:
        command.append("--use-struct-tree")
    if hybrid_backend:
        command.extend(["--hybrid", hybrid_backend])

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=build_opendataloader_env(),
    )
    if result.returncode != 0:
        print("OpenDataLoader parse failed for %s" % source_path, file=sys.stderr)
        if result.stderr.strip():
            print(result.stderr.strip(), file=sys.stderr)
        elif result.stdout.strip():
            print(result.stdout.strip(), file=sys.stderr)
        return None

    generated_files = sorted(
        path
        for path in output_dir.rglob("*")
        if path.is_file() and path.name != "opendataloader-run.json"
    )
    manifest_path = output_dir / "opendataloader-run.json"
    manifest = {
        "source": repo_rel(source_path).as_posix(),
        "generated_at": now().isoformat(timespec="seconds"),
        "parser": "opendataloader-pdf",
        "formats": [token.strip() for token in format_value.split(",") if token.strip()],
        "use_struct_tree": bool(use_struct_tree),
        "hybrid_backend": hybrid_backend or "",
        "command": command,
        "outputs": [repo_rel(path).as_posix() for path in generated_files],
        "stdout": result.stdout.strip(),
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    command_display = " ".join(
        [
            display_rel(executable),
            display_rel(source_path),
            "-o",
            display_rel(output_dir),
            "-f",
            format_value,
            *(
                ["--use-struct-tree"]
                if use_struct_tree
                else []
            ),
            *(
                ["--hybrid", hybrid_backend]
                if hybrid_backend
                else []
            ),
        ]
    )

    return {
        "output_dir": output_dir,
        "manifest_path": manifest_path,
        "generated_files": generated_files,
        "command_text": command_display,
    }


def parse_source_with_opendataloader(source_path, *, format_value, use_struct_tree=False, hybrid_backend=None):
    if not ensure_source_inside_workspace(source_path):
        return 1

    parse_result = run_opendataloader_parse(
        source_path=source_path,
        format_value=format_value,
        use_struct_tree=use_struct_tree,
        hybrid_backend=hybrid_backend,
    )
    if parse_result is None:
        return 1

    source_page = find_source_page_for_file(source_path)
    if source_page is not None:
        update_source_page_parsed_artifacts(
            source_page=source_page,
            source_file=source_path,
            generated_files=parse_result["generated_files"],
            manifest_path=parse_result["manifest_path"],
            command_text=parse_result["command_text"],
        )
        append_log(
            "source parsed",
            source_path.name,
            [
                "Parsed %s with OpenDataLoader PDF." % repo_rel(source_path),
                "Saved helper artifacts under %s." % repo_rel(parse_result["output_dir"]),
                "Updated source page %s." % repo_rel(source_page),
            ],
        )
    else:
        print(
            "No source page found for %s. Parsed artifacts were still generated."
            % repo_rel(source_path),
            file=sys.stderr,
        )

    print("Parsed source with OpenDataLoader: %s" % repo_rel(source_path))
    print("output dir: %s" % repo_rel(parse_result["output_dir"]))
    print("manifest: %s" % repo_rel(parse_result["manifest_path"]))
    if parse_result["generated_files"]:
        image_files = []
        primary_files = []
        for path in parse_result["generated_files"]:
            if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                image_files.append(path)
            else:
                primary_files.append(path)
        print("outputs:")
        for path in primary_files:
            print("- %s" % repo_rel(path))
        if image_files:
            print("- %d image files" % len(image_files))
    return 0


def command_parse_all_sources(args):
    ensure_layout()

    source_files = sorted(path for path in SOURCE_DIR.iterdir() if path.is_file())
    if args.limit:
        source_files = source_files[: args.limit]

    total = len(source_files)
    if total == 0:
        print("No source files found under %s" % repo_rel(SOURCE_DIR))
        return 0

    parsed = 0
    skipped = 0
    failed = 0

    for index, source_path in enumerate(source_files, 1):
        output_dir = OPENDATALOADER_DIR / source_path.stem
        manifest_path = output_dir / "opendataloader-run.json"
        if args.only_missing and manifest_path.exists() and not args.force:
            print("[%d/%d] Skip: %s (already parsed)" % (index, total, source_path.name))
            skipped += 1
            continue

        print("[%d/%d] Parsing: %s" % (index, total, source_path.name))
        exit_code = parse_source_with_opendataloader(
            source_path,
            format_value=args.parse_format,
            use_struct_tree=args.use_struct_tree,
            hybrid_backend=args.hybrid_backend,
        )
        if exit_code == 0:
            parsed += 1
        else:
            failed += 1

    print("")
    print("OpenDataLoader batch parse summary")
    print("- parsed: %d" % parsed)
    print("- skipped: %d" % skipped)
    print("- failed: %d" % failed)

    return 0 if failed == 0 else 1


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
    parsed_dir_count = sum(1 for path in OPENDATALOADER_DIR.glob("*") if path.is_dir())
    source_page_count, pruned_source_count = active_and_pruned_source_counts()
    entity_count = count_files(ENTITY_DIR, "*.md")
    concept_count = count_files(CONCEPT_DIR, "*.md")
    query_count = count_files(QUERY_DIR, "*.md")
    synthesis_count = count_files(SYNTHESIS_DIR, "*.md")

    recent = recent_log_headers(limit=5)

    print("paper_collect status")
    print("")
    print("root: %s" % ROOT)
    print("raw sources: %d" % raw_count)
    print("parsed sources (OpenDataLoader): %d" % parsed_dir_count)
    print("source pages: %d" % source_page_count)
    print("pruned source pages: %d" % pruned_source_count)
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


def command_resume(args):
    ensure_layout()

    limit = max(args.limit, 1)
    recent = recent_log_headers(limit=limit)
    recent_queries = recent_markdown_pages(QUERY_DIR, limit=limit)
    recent_syntheses = recent_markdown_pages(SYNTHESIS_DIR, limit=limit)
    pending_pages = missing_source_pages()
    pending_parsed = missing_parsed_sources()
    _active_source_count, pruned_source_count = active_and_pruned_source_counts()

    print("paper_collect resume")
    print("")
    print("root: %s" % ROOT)
    print("")
    print("start here:")
    print("- %s" % repo_rel(OVERVIEW_PATH))
    print("- %s" % repo_rel(INDEX_PATH))
    print("- %s" % repo_rel(LOG_PATH))

    if recent_queries:
        print("")
        print("recent query pages:")
        for path in recent_queries:
            print("- %s" % repo_rel(path))

    if recent_syntheses:
        print("")
        print("recent synthesis pages:")
        for path in recent_syntheses:
            print("- %s" % repo_rel(path))

    if recent:
        print("")
        print("recent log entries:")
        for line in recent:
            print("- %s" % line[3:])

    print("")
    print("open backlog:")
    print("- raw sources without wiki pages: %d" % len(pending_pages))
    if pending_pages:
        for path in pending_pages[:limit]:
            print("  - %s" % repo_rel(path))
        if len(pending_pages) > limit:
            print("  - ... %d more" % (len(pending_pages) - limit))
    print("- PDF sources without OpenDataLoader artifacts: %d" % len(pending_parsed))
    if pending_parsed:
        for path in pending_parsed[:limit]:
            print("  - %s" % repo_rel(path))
        if len(pending_parsed) > limit:
            print("  - ... %d more" % (len(pending_parsed) - limit))
    print("- pruned source pages excluded from the active corpus: %d" % pruned_source_count)

    print("")
    print("next moves:")
    if pending_pages:
        print("- Register and ingest the queued raw sources above before expanding concepts or new query layers.")
        print("- After each ingest, update wiki/index.md, wiki/overview.md, and wiki/log.md if the collection picture changed.")
    elif pending_parsed:
        print("- Run parse-source or parse-all-sources --only-missing for the PDFs above when layout-sensitive extraction would help.")
        print("- Then continue deepening concept/query pages from the refreshed source pages.")
    elif recent_queries:
        print("- Continue from the newest saved query pages above and fold stable decision rules back into concepts or a synthesis page.")
        print("- Keep answers knowledge-base-first: use only this collection's wiki and raw sources unless explicitly told otherwise.")
    else:
        print("- Add a new source with add-source or create a saved question with new-query, depending on whether you are expanding corpus or analysis.")

    return 0


def command_add_source(args):
    ensure_layout()

    source_path = Path(args.path).expanduser().resolve()
    if not source_path.exists() or not source_path.is_file():
        print("Source file not found: %s" % source_path, file=sys.stderr)
        return 1

    title = args.title or humanize_title_from_path(source_path)
    source_slug = slugify(title)
    timestamp = now().strftime("%Y%m%d_%H%M%S")
    copied_source = unique_path(SOURCE_DIR / ("%s_%s%s" % (timestamp, source_slug, source_path.suffix)))
    shutil.copy2(source_path, copied_source)

    source_page = create_source_page_for_file(copied_source, title, args.kind)

    parse_exit = 0
    if args.parse_with_opendataloader:
        parse_exit = parse_source_with_opendataloader(
            copied_source,
            format_value=args.parse_format,
            use_struct_tree=args.use_struct_tree,
            hybrid_backend=args.hybrid_backend,
        )

    print("Queued source: %s" % title)
    print("raw file: %s" % repo_rel(copied_source))
    print("wiki page: %s" % repo_rel(source_page))
    if args.parse_with_opendataloader and parse_exit == 0:
        print("parsed helper artifacts: %s" % repo_rel(OPENDATALOADER_DIR / copied_source.stem))
    print("")
    print("Next step:")
    print(
        "Ask Codex to ingest %s and update the wiki according to AGENTS.md."
        % repo_rel(copied_source)
    )
    return parse_exit


def command_register_source(args):
    ensure_layout()

    source_path = Path(args.path).expanduser().resolve()
    if not source_path.exists() or not source_path.is_file():
        print("Source file not found: %s" % source_path, file=sys.stderr)
        return 1

    if not ensure_source_inside_workspace(source_path):
        return 1

    title = args.title or humanize_title_from_path(source_path)
    source_page = create_source_page_for_file(source_path, title, args.kind)

    parse_exit = 0
    if args.parse_with_opendataloader:
        parse_exit = parse_source_with_opendataloader(
            source_path,
            format_value=args.parse_format,
            use_struct_tree=args.use_struct_tree,
            hybrid_backend=args.hybrid_backend,
        )

    print("Registered source: %s" % title)
    print("raw file: %s" % repo_rel(source_path))
    print("wiki page: %s" % repo_rel(source_page))
    if args.parse_with_opendataloader and parse_exit == 0:
        print("parsed helper artifacts: %s" % repo_rel(OPENDATALOADER_DIR / source_path.stem))
    return parse_exit


def command_parse_source(args):
    ensure_layout()

    source_path = Path(args.path).expanduser().resolve()
    if not source_path.exists() or not source_path.is_file():
        print("Source file not found: %s" % source_path, file=sys.stderr)
        return 1

    return parse_source_with_opendataloader(
        source_path,
        format_value=args.parse_format,
        use_struct_tree=args.use_struct_tree,
        hybrid_backend=args.hybrid_backend,
    )


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
        help="Collection name under collections/, for example Multi_Omics or Organoid.",
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

    resume_parser = subparsers.add_parser(
        "resume",
        help="Show the fastest way to recover context for the current workspace.",
    )
    resume_parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Maximum number of recent or pending items to show per section.",
    )
    resume_parser.set_defaults(func=command_resume)

    add_source_parser = subparsers.add_parser("add-source", help="Copy a source into raw/sources and create a stub source page.")
    add_source_parser.add_argument("path", help="Path to a local file.")
    add_source_parser.add_argument("--title", help="Optional human-readable title.")
    add_source_parser.add_argument(
        "--kind",
        default="paper",
        choices=["paper", "article", "book", "note", "dataset", "other"],
        help="Source type label for the wiki page.",
    )
    add_source_parser.add_argument(
        "--parse-with-opendataloader",
        action="store_true",
        help="Also parse the copied source with OpenDataLoader PDF and save helper artifacts under raw/derived/opendataloader/.",
    )
    add_source_parser.add_argument(
        "--parse-format",
        default="json,markdown",
        help="OpenDataLoader output formats, for example json,markdown or markdown.",
    )
    add_source_parser.add_argument(
        "--use-struct-tree",
        action="store_true",
        help="Prefer the PDF structure tree when the source is tagged.",
    )
    add_source_parser.add_argument(
        "--hybrid-backend",
        help="Optional OpenDataLoader hybrid backend name, for example docling-fast.",
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
    register_source_parser.add_argument(
        "--parse-with-opendataloader",
        action="store_true",
        help="Also parse the registered source with OpenDataLoader PDF and save helper artifacts under raw/derived/opendataloader/.",
    )
    register_source_parser.add_argument(
        "--parse-format",
        default="json,markdown",
        help="OpenDataLoader output formats, for example json,markdown or markdown.",
    )
    register_source_parser.add_argument(
        "--use-struct-tree",
        action="store_true",
        help="Prefer the PDF structure tree when the source is tagged.",
    )
    register_source_parser.add_argument(
        "--hybrid-backend",
        help="Optional OpenDataLoader hybrid backend name, for example docling-fast.",
    )
    register_source_parser.set_defaults(func=command_register_source)

    parse_source_parser = subparsers.add_parser(
        "parse-source",
        help="Parse an existing raw/sources PDF with OpenDataLoader PDF and save helper artifacts.",
    )
    parse_source_parser.add_argument("path", help="Path to a local file inside raw/sources.")
    parse_source_parser.add_argument(
        "--parse-format",
        default="json,markdown",
        help="OpenDataLoader output formats, for example json,markdown or markdown.",
    )
    parse_source_parser.add_argument(
        "--use-struct-tree",
        action="store_true",
        help="Prefer the PDF structure tree when the source is tagged.",
    )
    parse_source_parser.add_argument(
        "--hybrid-backend",
        help="Optional OpenDataLoader hybrid backend name, for example docling-fast.",
    )
    parse_source_parser.set_defaults(func=command_parse_source)

    parse_all_parser = subparsers.add_parser(
        "parse-all-sources",
        help="Parse collection raw/sources files with OpenDataLoader PDF and save helper artifacts.",
    )
    parse_all_parser.add_argument(
        "--parse-format",
        default="json,markdown",
        help="OpenDataLoader output formats, for example json,markdown or markdown.",
    )
    parse_all_parser.add_argument(
        "--use-struct-tree",
        action="store_true",
        help="Prefer the PDF structure tree when the source is tagged.",
    )
    parse_all_parser.add_argument(
        "--hybrid-backend",
        help="Optional OpenDataLoader hybrid backend name, for example docling-fast.",
    )
    parse_all_parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Skip files that already have an opendataloader-run.json manifest.",
    )
    parse_all_parser.add_argument(
        "--force",
        action="store_true",
        help="Reparse files even if helper artifacts already exist.",
    )
    parse_all_parser.add_argument(
        "--limit",
        type=int,
        help="Optional maximum number of source files to parse.",
    )
    parse_all_parser.set_defaults(func=command_parse_all_sources)

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
        default_collection="Multi_Omics",
    )
    configure_workspace(workspace.root)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
