#!/usr/bin/env python3

import argparse
import atexit
import http.client
import os
import signal
import subprocess
import sys
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional, Tuple

from workspace import PROJECT_ROOT

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
PID_FILE = PROJECT_ROOT / ".wiki_html_server.pid"
LOG_FILE = PROJECT_ROOT / ".wiki_html_server.log"


class WikiHtmlRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/__paper_collect_ping__":
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format: str, *args: object) -> None:
        sys.stdout.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))
        sys.stdout.flush()


def server_url(host: str, port: int) -> str:
    return f"http://{host}:{port}/index.html"


def server_responding(host: str, port: int) -> bool:
    connection = http.client.HTTPConnection(host, port, timeout=1.5)
    try:
        connection.request("GET", "/__paper_collect_ping__")
        response = connection.getresponse()
        response.read()
        return response.status == HTTPStatus.NO_CONTENT
    except OSError:
        return False
    finally:
        connection.close()


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
        cwd=PROJECT_ROOT,
    )
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def server_process_matches(pid: int) -> bool:
    command = command_for_pid(pid)
    return "serve_wiki_html.py" in command and " serve" in command


def server_running(host: str, port: int) -> Tuple[bool, Optional[int], str]:
    pid = read_pid()
    if pid is None:
        if server_responding(host, port):
            return True, None, ""
        return False, None, ""
    try:
        os.kill(pid, 0)
    except OSError:
        cleanup_pid_file(pid)
        if server_responding(host, port):
            return True, None, ""
        return False, None, ""
    command = command_for_pid(pid)
    if not command:
        return True, pid, ""
    if not server_process_matches(pid):
        return False, pid, command
    return True, pid, command


def serve_foreground(host: str, port: int) -> int:
    handler = partial(WikiHtmlRequestHandler, directory=str(PROJECT_ROOT))
    httpd = ThreadingHTTPServer((host, port), handler)
    write_pid_file(os.getpid())
    atexit.register(cleanup_pid_file, os.getpid())

    def request_stop(_signum: int, _frame: object) -> None:
        httpd.shutdown()

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)

    print(f"Serving paper_collect at {server_url(host, port)}", flush=True)
    try:
        httpd.serve_forever()
    finally:
        cleanup_pid_file(os.getpid())
        httpd.server_close()
    return 0


def start_server(host: str, port: int) -> int:
    running, pid, _command = server_running(host, port)
    if running:
        if pid is None:
            print(f"wiki_html server is already responding at {server_url(host, port)}")
        else:
            print(f"wiki_html server is already running (pid {pid}) at {server_url(host, port)}")
        return 0

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    log_handle = LOG_FILE.open("a", encoding="utf-8")
    process = subprocess.Popen(
        [sys.executable, str(Path(__file__).resolve()), "--host", host, "--port", str(port), "serve"],
        cwd=PROJECT_ROOT,
        stdout=log_handle,
        stderr=subprocess.STDOUT,
        start_new_session=True,
        close_fds=True,
    )
    write_pid_file(process.pid)
    print(f"Started wiki_html server (pid {process.pid}) at {server_url(host, port)}")
    print(f"Log: {LOG_FILE}")
    return 0


def stop_server() -> int:
    running, pid, command = server_running(DEFAULT_HOST, DEFAULT_PORT)
    if not running:
        if pid is not None and command:
            print(f"PID file points to a different process ({pid}): {command}")
        else:
            print("wiki_html server is not running.")
        cleanup_pid_file(pid)
        return 0

    if pid is None:
        print("wiki_html server is responding, but it is not managed by the current PID file.")
        print("Stop that existing server separately, or restart it with scripts/site_runtime.py.")
        return 1

    assert pid is not None
    os.kill(pid, signal.SIGTERM)
    print(f"Stopped wiki_html server (pid {pid}).")
    cleanup_pid_file(pid)
    return 0


def status_server(host: str, port: int) -> int:
    running, pid, command = server_running(host, port)
    if not running:
        if pid is not None and command:
            print(f"wiki_html server pid file exists but process does not match: {pid}")
            print(command)
        else:
            print("wiki_html server is not running.")
        return 1

    if pid is None:
        print("wiki_html server is running (pid unavailable; existing localhost server detected)")
    else:
        print(f"wiki_html server is running (pid {pid})")
    print(f"URL: {server_url(host, port)}")
    if command:
        print(command)
    else:
        print("Command unavailable in this environment; PID check passed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Serve the paper_collect HTML site over localhost.")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Bind host (default: {DEFAULT_HOST})")
    parser.add_argument("--port", default=DEFAULT_PORT, type=int, help=f"Bind port (default: {DEFAULT_PORT})")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("serve", help="Run the server in the foreground.")
    subparsers.add_parser("start", help="Start the server in the background.")
    subparsers.add_parser("stop", help="Stop the background server.")
    subparsers.add_parser("status", help="Show server status.")
    subparsers.add_parser("url", help="Print the local viewer URL.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "serve":
        return serve_foreground(args.host, args.port)
    if args.command == "start":
        return start_server(args.host, args.port)
    if args.command == "stop":
        return stop_server()
    if args.command == "status":
        return status_server(args.host, args.port)
    if args.command == "url":
        print(server_url(args.host, args.port))
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
