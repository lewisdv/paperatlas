#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path

from workspace import PROJECT_ROOT

SERVE_SCRIPT = PROJECT_ROOT / "scripts" / "serve_wiki_html.py"
WATCH_SCRIPT = PROJECT_ROOT / "scripts" / "watch_wiki_html.py"


def run_script(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )


def print_result(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)


def start_site() -> int:
    serve_result = run_script(SERVE_SCRIPT, "start")
    print_result(serve_result)

    watch_result = run_script(WATCH_SCRIPT, "start")
    print_result(watch_result)

    url_result = run_script(SERVE_SCRIPT, "url")
    url = url_result.stdout.strip() if url_result.returncode == 0 else ""
    if url:
        print(f"Top-level site: {url}")

    return 0 if serve_result.returncode == 0 and watch_result.returncode == 0 else 1


def stop_site() -> int:
    watch_result = run_script(WATCH_SCRIPT, "stop")
    print_result(watch_result)

    serve_result = run_script(SERVE_SCRIPT, "stop")
    print_result(serve_result)

    return 0 if serve_result.returncode == 0 and watch_result.returncode == 0 else 1


def status_site() -> int:
    serve_result = run_script(SERVE_SCRIPT, "status")
    print("Server")
    print_result(serve_result)
    print("")

    watch_result = run_script(WATCH_SCRIPT, "status")
    print("Watcher")
    print_result(watch_result)
    print("")

    url_result = run_script(SERVE_SCRIPT, "url")
    if url_result.returncode == 0 and url_result.stdout.strip():
        print(f"Top-level site: {url_result.stdout.strip()}")

    return 0 if serve_result.returncode == 0 and watch_result.returncode == 0 else 1


def url_site() -> int:
    result = run_script(SERVE_SCRIPT, "url")
    print_result(result)
    return result.returncode


def restart_site() -> int:
    stop_site()
    return start_site()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage the paper_collect local website and automatic HTML updates."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("start", help="Start the localhost site server and the root watcher.")
    subparsers.add_parser("stop", help="Stop the localhost site server and the root watcher.")
    subparsers.add_parser("restart", help="Restart the localhost site server and the root watcher.")
    subparsers.add_parser("status", help="Show the status of the site server and the root watcher.")
    subparsers.add_parser("url", help="Print the top-level site URL.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "start":
        return start_site()
    if args.command == "stop":
        return stop_site()
    if args.command == "restart":
        return restart_site()
    if args.command == "status":
        return status_site()
    if args.command == "url":
        return url_site()

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
