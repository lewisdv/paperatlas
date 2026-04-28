#!/usr/bin/env python3

import argparse
import atexit
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from workspace import PROJECT_ROOT, list_collection_workspaces, resolve_workspace

ROOT = PROJECT_ROOT
WIKI_DIR = ROOT / "wiki"
RENDER_SCRIPT = ROOT / "scripts" / "render_wiki_html.py"
PID_FILE = ROOT / ".wiki_html_watcher.pid"
LOG_FILE = ROOT / ".render_watcher.log"
PROJECT_MODE = False

_STOP_REQUESTED = False


def run_git_command(args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )


def log_subprocess_output(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout.strip():
        print(result.stdout.strip(), flush=True)
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr, flush=True)


def unique_preserving_order(items: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    ordered: List[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def project_sync_pathspecs(paths: List[str], *, include_all_collections: bool = False) -> List[str]:
    if include_all_collections:
        collection_specs = [
            f"collections/{workspace.key}" for workspace in list_collection_workspaces()
        ]
    else:
        collection_specs = [f"collections/{key}" for key in sorted(changed_collections(paths))]

    return unique_preserving_order(collection_specs)


def workspace_sync_pathspecs() -> List[str]:
    try:
        relative_root = ROOT.resolve().relative_to(PROJECT_ROOT.resolve())
    except ValueError:
        return []
    if str(relative_root) == ".":
        return []
    return [relative_root.as_posix()]


def git_current_branch() -> str:
    result = run_git_command(["branch", "--show-current"])
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


STOPWORDS = {
    "a",
    "an",
    "and",
    "comparison",
    "concept",
    "concepts",
    "corpus",
    "generation",
    "log",
    "note",
    "notes",
    "of",
    "organoid",
    "organoids",
    "overview",
    "page",
    "pages",
    "paper",
    "protocol",
    "protocols",
    "query",
    "sources",
    "study",
    "summary",
    "synthesis",
    "the",
    "update",
    "wiki",
}


def collection_key_from_path(path: str) -> str:
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "collections":
        return parts[1]
    return ""


def section_from_path(path: str) -> str:
    parts = Path(path).parts
    if "wiki" in parts:
        wiki_index = parts.index("wiki")
        if len(parts) > wiki_index + 1:
            return parts[wiki_index + 1]
    return ""


def slug_to_words(value: str) -> List[str]:
    return [part for part in re.split(r"[^a-z0-9]+", value.lower()) if part]


def clean_topic_words(words: Iterable[str]) -> List[str]:
    cleaned: List[str] = []
    for word in words:
        if word.isdigit():
            continue
        if re.fullmatch(r"(19|20)\d{2}", word):
            continue
        if word in STOPWORDS:
            continue
        if len(word) <= 2:
            continue
        cleaned.append(word)
    return cleaned


def title_from_markdown(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return path.stem.replace("-", " ").replace("_", " ")

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("title:"):
            return stripped.split(":", 1)[1].strip().strip('"').strip("'")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ")


def summarize_topic_from_files(files: List[str]) -> str:
    if not files:
        return ""

    markdown_files = [Path(file) for file in files if file.endswith(".md")]
    if len(markdown_files) == 1:
        title = title_from_markdown(PROJECT_ROOT / markdown_files[0]).strip()
        title = re.sub(r"\s+", " ", title)
        if title:
            return title[:72]

    word_counts: Dict[str, int] = {}
    for file in files:
        words = clean_topic_words(slug_to_words(Path(file).stem))
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    if not word_counts:
        return ""

    ranked_words = [
        word
        for word, _count in sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    ][:4]
    if not ranked_words:
        return ""
    return " ".join(ranked_words)


def describe_collection_change(collection_key: str, files: List[str]) -> str:
    if not files:
        return f"{collection_key}: sync updates"

    sections = {section_from_path(file) for file in files if section_from_path(file)}
    topic = summarize_topic_from_files(files)
    if topic:
        return f"{collection_key}: update {topic}"
    if len(sections) == 1:
        only_section = next(iter(sections))
        if only_section == "queries":
            return f"{collection_key}: update query notes"
        if only_section == "syntheses":
            return f"{collection_key}: update synthesis notes"
        if only_section == "concepts":
            return f"{collection_key}: update concept pages"
        if only_section == "sources":
            return f"{collection_key}: update source pages"
    return f"{collection_key}: sync wiki updates"


def build_git_commit_message(staged_files: List[str], pathspecs: List[str]) -> str:
    collection_keys: List[str] = []
    for pathspec in pathspecs:
        key = collection_key_from_path(pathspec)
        if key:
            collection_keys.append(key)

    collection_keys = unique_preserving_order(collection_keys)
    if not collection_keys:
        return "Auto-sync wiki updates"

    staged_by_collection: Dict[str, List[str]] = {}
    for file in staged_files:
        key = collection_key_from_path(file)
        if not key:
            continue
        staged_by_collection.setdefault(key, []).append(file)

    if len(collection_keys) == 1:
        key = collection_keys[0]
        return describe_collection_change(key, staged_by_collection.get(key, []))

    if len(collection_keys) <= 3:
        summaries = [describe_collection_change(key, staged_by_collection.get(key, [])) for key in collection_keys]
        return " | ".join(summaries)
    return f"collections: sync {', '.join(collection_keys[:3])} +{len(collection_keys) - 3} more"


def git_auto_sync(pathspecs: List[str]) -> int:
    pathspecs = unique_preserving_order(pathspecs)
    if not pathspecs:
        log("Git auto-sync skipped: no collection paths were eligible.")
        return 0

    repo_check = run_git_command(["rev-parse", "--is-inside-work-tree"])
    if repo_check.returncode != 0 or repo_check.stdout.strip() != "true":
        log("Git auto-sync skipped: project root is not a git repository.")
        return 0

    remote_check = run_git_command(["remote", "get-url", "origin"])
    if remote_check.returncode != 0 or not remote_check.stdout.strip():
        log("Git auto-sync skipped: origin remote is not configured.")
        return 0

    branch = git_current_branch()
    if not branch:
        log("Git auto-sync skipped: could not determine the current branch.")
        return 0

    status_before = run_git_command(["status", "--porcelain", "--untracked-files=all", "--", *pathspecs])
    if status_before.returncode != 0:
        log("Git auto-sync failed while checking repository status.")
        log_subprocess_output(status_before)
        return 1
    if not status_before.stdout.strip():
        log("Git auto-sync skipped: no Git changes were found in the updated collection paths.")
        return 0

    add_result = run_git_command(["add", "-A", "--", *pathspecs])
    if add_result.returncode != 0:
        log("Git auto-sync failed while staging collection changes.")
        log_subprocess_output(add_result)
        return 1

    staged_result = run_git_command(["diff", "--cached", "--name-only", "--", *pathspecs])
    if staged_result.returncode != 0:
        log("Git auto-sync failed while checking staged collection changes.")
        log_subprocess_output(staged_result)
        return 1
    staged_files = [line.strip() for line in staged_result.stdout.splitlines() if line.strip()]
    if not staged_files:
        log("Git auto-sync skipped: nothing remained staged after filtering to collection paths.")
        return 0

    commit_message = build_git_commit_message(staged_files, pathspecs)
    log(
        "Git auto-sync committing %d file(s) from %d path scope(s): %s"
        % (len(staged_files), len(pathspecs), commit_message)
    )
    commit_result = run_git_command(["commit", "-m", commit_message, "--", *pathspecs])
    if commit_result.returncode != 0:
        log("Git auto-sync failed while creating the commit.")
        log_subprocess_output(commit_result)
        return 1
    log_subprocess_output(commit_result)

    push_result = run_git_command(["push", "origin", branch])
    if push_result.returncode != 0:
        log("Git auto-sync created the commit but failed to push it.")
        log_subprocess_output(push_result)
        return 1
    log_subprocess_output(push_result)
    log(f"Git auto-sync pushed the latest wiki commit to origin/{branch}.")
    return 0


def configure_workspace(root: Path) -> None:
    global ROOT, WIKI_DIR, PID_FILE, LOG_FILE, PROJECT_MODE
    ROOT = root
    WIKI_DIR = ROOT / "wiki"
    PID_FILE = ROOT / ".wiki_html_watcher.pid"
    PROJECT_MODE = root == PROJECT_ROOT and (root / "collections").exists() and not WIKI_DIR.exists()
    if PROJECT_MODE:
        LOG_FILE = ROOT / ".render_watcher.log"
    else:
        LOG_FILE = ROOT / "wiki_html" / "render_watcher.log"


def watched_files() -> Iterable[Path]:
    yield RENDER_SCRIPT
    yield ROOT / "scripts" / "workspace.py"
    if PROJECT_MODE:
        collections_dir = ROOT / "collections"
        if not collections_dir.exists():
            return
        for path in sorted(collections_dir.rglob("*")):
            if not path.is_file():
                continue
            rel_parts = path.relative_to(ROOT).parts
            if any(part.startswith(".") for part in rel_parts):
                continue
            if "wiki_html" in rel_parts:
                continue
            yield path
        return

    for path in sorted(WIKI_DIR.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            yield path


def build_snapshot() -> Dict[str, Tuple[int, int]]:
    snapshot: Dict[str, Tuple[int, int]] = {}
    for path in watched_files():
        try:
            stat_result = path.stat()
        except FileNotFoundError:
            continue
        snapshot[str(path.relative_to(ROOT))] = (stat_result.st_mtime_ns, stat_result.st_size)
    return snapshot


def summarize_changes(before: Dict[str, Tuple[int, int]], after: Dict[str, Tuple[int, int]]) -> str:
    created = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(path for path in set(before) & set(after) if before[path] != after[path])
    samples = (created + changed + removed)[:5]
    parts = []
    if created:
        parts.append(f"{len(created)} added")
    if changed:
        parts.append(f"{len(changed)} updated")
    if removed:
        parts.append(f"{len(removed)} removed")
    if not parts:
        return "change detected"
    sample_text = ", ".join(samples)
    return f"{', '.join(parts)} ({sample_text})"


def log(message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def run_render_command(root: Path) -> int:
    command = [sys.executable, str(RENDER_SCRIPT), "--workspace", str(root)]
    result = subprocess.run(command, cwd=PROJECT_ROOT, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip(), flush=True)
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr, flush=True)
    return result.returncode


def render_root_hub() -> int:
    log("Rendering top-level collection hub.")
    result = run_render_command(PROJECT_ROOT)
    if result == 0:
        log("Top-level collection hub rendered successfully.")
    else:
        log(f"Top-level collection hub render failed with exit code {result}.")
    return result


def render_collection_workspace(workspace_root: Path) -> int:
    log(f"Rendering collection HTML for {workspace_root.name}.")
    result = run_render_command(workspace_root)
    if result == 0:
        log(f"Collection render finished successfully for {workspace_root.name}.")
    else:
        log(f"Collection render failed for {workspace_root.name} with exit code {result}.")
    return result


def render_project_site() -> int:
    collection_failures = 0
    for workspace in list_collection_workspaces():
        collection_failures += int(render_collection_workspace(workspace.root) != 0)
    hub_result = render_root_hub()
    if collection_failures or hub_result != 0:
        return 1
    return 0


def render_once() -> int:
    if PROJECT_MODE:
        log("Running project-wide wiki HTML render.")
        result = render_project_site()
        if result == 0:
            log("Project-wide render finished successfully.")
        else:
            log("Project-wide render finished with failures.")
        return result

    log("Running wiki HTML render.")
    result = render_collection_workspace(ROOT)
    if result == 0:
        log("Render finished successfully.")
    else:
        log(f"Render failed with exit code {result}.")
    return result


def write_pid_file(pid: int) -> None:
    PID_FILE.write_text(f"{pid}\n", encoding="utf-8")


def cleanup_pid_file(expected_pid: Optional[int] = None) -> None:
    if not PID_FILE.exists():
        return
    try:
        current = int(PID_FILE.read_text(encoding="utf-8").strip())
    except ValueError:
        PID_FILE.unlink(missing_ok=True)
        return
    if expected_pid is None or current == expected_pid:
        PID_FILE.unlink(missing_ok=True)


def read_pid() -> Optional[int]:
    if not PID_FILE.exists():
        return None
    try:
        return int(PID_FILE.read_text(encoding="utf-8").strip())
    except ValueError:
        return None


def command_for_pid(pid: int) -> str:
    result = subprocess.run(
        ["ps", "-p", str(pid), "-o", "command="],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def watcher_process_matches(pid: int) -> bool:
    command = command_for_pid(pid)
    return "watch_wiki_html.py" in command and " watch" in command


def watcher_running() -> Tuple[bool, Optional[int], str]:
    pid = read_pid()
    if pid is None:
        return False, None, ""
    try:
        os.kill(pid, 0)
    except OSError:
        cleanup_pid_file(pid)
        return False, None, ""
    command = command_for_pid(pid)
    if not command:
        return True, pid, ""
    if not watcher_process_matches(pid):
        return False, pid, command
    return True, pid, command


def changed_paths(before: Dict[str, Tuple[int, int]], after: Dict[str, Tuple[int, int]]) -> List[str]:
    created = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(path for path in set(before) & set(after) if before[path] != after[path])
    return created + changed + removed


def changed_collections(paths: List[str]) -> Set[str]:
    collections: Set[str] = set()
    for path in paths:
        parts = Path(path).parts
        if len(parts) >= 2 and parts[0] == "collections":
            collections.add(parts[1])
    return collections


def needs_full_project_render(paths: List[str]) -> bool:
    full_render_triggers = {
        "scripts/render_wiki_html.py",
        "scripts/workspace.py",
    }
    return any(path in full_render_triggers for path in paths)


def wait_for_stable_snapshot(previous: Dict[str, Tuple[int, int]], interval: float, settle_seconds: float) -> Dict[str, Tuple[int, int]]:
    candidate = previous
    deadline = time.monotonic() + settle_seconds
    while time.monotonic() < deadline and not _STOP_REQUESTED:
        time.sleep(interval)
        current = build_snapshot()
        if current != candidate:
            candidate = current
            deadline = time.monotonic() + settle_seconds
    return candidate


def request_stop(_signum: int, _frame: object) -> None:
    global _STOP_REQUESTED
    _STOP_REQUESTED = True


def watch_loop(interval: float, settle_seconds: float, git_auto_sync_enabled: bool) -> int:
    global _STOP_REQUESTED
    _STOP_REQUESTED = False
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    write_pid_file(os.getpid())
    atexit.register(cleanup_pid_file, os.getpid())
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)

    if PROJECT_MODE:
        log(
            f"Watching all collections under {ROOT / 'collections'} every {interval:.1f}s "
            f"with {settle_seconds:.1f}s settle time."
        )
    else:
        log(f"Watching {WIKI_DIR} every {interval:.1f}s with {settle_seconds:.1f}s settle time.")
    if git_auto_sync_enabled:
        log("Git auto-sync is enabled for collection changes.")
    baseline = build_snapshot()
    render_once()

    while not _STOP_REQUESTED:
        time.sleep(interval)
        current = build_snapshot()
        if current == baseline:
            continue
        log(f"Change detected: {summarize_changes(baseline, current)}")
        stabilized = wait_for_stable_snapshot(current, min(interval, 0.5), settle_seconds)
        paths = changed_paths(baseline, stabilized)
        baseline = stabilized
        if PROJECT_MODE:
            if needs_full_project_render(paths):
                sync_pathspecs = project_sync_pathspecs(paths, include_all_collections=True)
                render_result = render_project_site()
                if git_auto_sync_enabled and render_result == 0:
                    git_auto_sync(sync_pathspecs)
                continue

            sync_pathspecs = project_sync_pathspecs(paths)
            touched_collections = changed_collections(paths)
            existing_workspaces = {workspace.key: workspace for workspace in list_collection_workspaces()}
            collection_failures = 0
            for key in sorted(touched_collections):
                workspace = existing_workspaces.get(key)
                if workspace is None:
                    continue
                collection_failures += int(render_collection_workspace(workspace.root) != 0)
            hub_result = render_root_hub()
            if git_auto_sync_enabled and collection_failures == 0 and hub_result == 0:
                git_auto_sync(sync_pathspecs)
            continue

        render_result = render_once()
        if git_auto_sync_enabled and render_result == 0:
            git_auto_sync(workspace_sync_pathspecs())

    log("Watcher stopped.")
    return 0


def start_watcher(interval: float, settle_seconds: float, git_auto_sync_enabled: bool) -> int:
    running, pid, command = watcher_running()
    if running and pid is not None:
        print(f"Watcher already running with pid {pid}.")
        print(f"Log: {LOG_FILE}")
        return 0
    if pid is not None and command:
        print(f"Refusing to reuse pid file because pid {pid} is not the wiki watcher.")
        print(f"Current command: {command}")
        return 1

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    script_path = Path(__file__).resolve()
    with LOG_FILE.open("a", encoding="utf-8") as log_handle:
        process = subprocess.Popen(
            [
                sys.executable,
                str(script_path),
                "--workspace",
                str(ROOT),
                "watch",
                *(["--git-auto-sync"] if git_auto_sync_enabled else []),
                "--interval",
                str(interval),
                "--settle-seconds",
                str(settle_seconds),
            ],
            cwd=PROJECT_ROOT,
            stdin=subprocess.DEVNULL,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    print(f"Started wiki HTML watcher with pid {process.pid}.")
    print(f"Log: {LOG_FILE}")
    return 0


def stop_watcher() -> int:
    running, pid, command = watcher_running()
    if not running or pid is None:
        if pid is not None and command:
            print(f"Watcher pid file points to another process ({pid}).")
            print(f"Current command: {command}")
            return 1
        print("Watcher is not running.")
        cleanup_pid_file()
        return 0

    os.kill(pid, signal.SIGTERM)
    for _ in range(20):
        time.sleep(0.25)
        still_running, _, _ = watcher_running()
        if not still_running:
            cleanup_pid_file(pid)
            print(f"Stopped wiki HTML watcher (pid {pid}).")
            return 0
    print(f"Sent SIGTERM to pid {pid}, but it is still running.")
    return 1


def status_watcher() -> int:
    running, pid, command = watcher_running()
    if running and pid is not None:
        print(f"Watcher is running with pid {pid}.")
        print(f"Log: {LOG_FILE}")
        if command:
            print(f"Command: {command}")
        else:
            print("Command unavailable in this environment; PID check passed.")
        return 0
    if pid is not None and command:
        print(f"Pid file exists but pid {pid} is not the wiki watcher.")
        print(f"Current command: {command}")
        return 1
    print("Watcher is not running.")
    print(f"Log: {LOG_FILE}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Auto-render wiki_html whenever Markdown wiki files change."
    )
    parser.add_argument(
        "--collection",
        help="Collection name under collections/, for example Multi_Omics or Organoid.",
    )
    parser.add_argument(
        "--workspace",
        help="Explicit workspace path. Overrides --collection.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in ("watch", "start"):
        subparser = subparsers.add_parser(name)
        subparser.add_argument("--interval", type=float, default=2.0, help="Polling interval in seconds.")
        subparser.add_argument(
            "--settle-seconds",
            type=float,
            default=1.0,
            help="How long a change burst must stay quiet before rebuilding.",
        )
        subparser.add_argument(
            "--git-auto-sync",
            action="store_true",
            help="After a successful render, automatically git add/commit/push changed collection files.",
        )

    subparsers.add_parser("stop")
    subparsers.add_parser("status")
    subparsers.add_parser("render")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.collection or args.workspace:
        workspace = resolve_workspace(
            collection=args.collection,
            workspace=args.workspace,
            default_collection="Multi_Omics",
        )
        configure_workspace(workspace.root)
    else:
        configure_workspace(PROJECT_ROOT)
    if args.command == "watch":
        return watch_loop(args.interval, args.settle_seconds, args.git_auto_sync)
    if args.command == "start":
        return start_watcher(args.interval, args.settle_seconds, args.git_auto_sync)
    if args.command == "stop":
        return stop_watcher()
    if args.command == "status":
        return status_watcher()
    if args.command == "render":
        return render_once()
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
