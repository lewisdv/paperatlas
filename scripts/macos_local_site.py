#!/usr/bin/env python3

import argparse
import http.client
import os
import plistlib
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from workspace import PROJECT_ROOT

DEFAULT_HOST_ALIAS = "paperatlas.local"
DEFAULT_BIND_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
DEFAULT_INTERVAL = 2.0
DEFAULT_SETTLE_SECONDS = 1.0

SUPPORT_DIR = PROJECT_ROOT / ".macos"
GENERATED_DIR = SUPPORT_DIR / "LaunchAgents"
USER_LAUNCH_AGENTS = Path.home() / "Library" / "LaunchAgents"

SERVER_LABEL = "local.papercollect.paperatlas.server"
WATCHER_LABEL = "local.papercollect.paperatlas.watcher"


@dataclass
class AgentSpec:
    label: str
    plist_path: Path
    installed_path: Path


def server_url(host_alias: str, port: int) -> str:
    return f"http://{host_alias}:{port}/index.html"


def launchctl_domain() -> str:
    return f"gui/{os.getuid()}"


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def server_responding(bind_host: str, port: int) -> bool:
    connection = http.client.HTTPConnection(bind_host, port, timeout=1.5)
    try:
        connection.request("GET", "/__paper_collect_ping__")
        response = connection.getresponse()
        response.read()
        return response.status == 204
    except OSError:
        return False
    finally:
        connection.close()


def plist_payload(label: str, program_arguments: list[str], stdout_path: Path, stderr_path: Path) -> dict:
    return {
        "Label": label,
        "ProgramArguments": program_arguments,
        "WorkingDirectory": str(PROJECT_ROOT),
        "RunAtLoad": True,
        "KeepAlive": True,
        "StandardOutPath": str(stdout_path),
        "StandardErrorPath": str(stderr_path),
        "EnvironmentVariables": {
            "PYTHONUNBUFFERED": "1",
        },
        "ProcessType": "Background",
    }


def agent_specs() -> list[AgentSpec]:
    return [
        AgentSpec(
            label=SERVER_LABEL,
            plist_path=GENERATED_DIR / f"{SERVER_LABEL}.plist",
            installed_path=USER_LAUNCH_AGENTS / f"{SERVER_LABEL}.plist",
        ),
        AgentSpec(
            label=WATCHER_LABEL,
            plist_path=GENERATED_DIR / f"{WATCHER_LABEL}.plist",
            installed_path=USER_LAUNCH_AGENTS / f"{WATCHER_LABEL}.plist",
        ),
    ]


def write_generated_plists(bind_host: str, port: int, interval: float, settle_seconds: float) -> list[AgentSpec]:
    python_executable = Path(sys.executable).resolve()
    SUPPORT_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    server_stdout = PROJECT_ROOT / ".launchagent_server.out.log"
    server_stderr = PROJECT_ROOT / ".launchagent_server.err.log"
    watcher_stdout = PROJECT_ROOT / ".launchagent_watcher.out.log"
    watcher_stderr = PROJECT_ROOT / ".launchagent_watcher.err.log"

    payloads = {
        SERVER_LABEL: plist_payload(
            SERVER_LABEL,
            [
                str(python_executable),
                str((PROJECT_ROOT / "scripts" / "serve_wiki_html.py").resolve()),
                "--host",
                bind_host,
                "--port",
                str(port),
                "serve",
            ],
            server_stdout,
            server_stderr,
        ),
        WATCHER_LABEL: plist_payload(
            WATCHER_LABEL,
            [
                str(python_executable),
                str((PROJECT_ROOT / "scripts" / "watch_wiki_html.py").resolve()),
                "--workspace",
                str(PROJECT_ROOT.resolve()),
                "watch",
                "--git-auto-sync",
                "--interval",
                str(interval),
                "--settle-seconds",
                str(settle_seconds),
            ],
            watcher_stdout,
            watcher_stderr,
        ),
    }

    specs = agent_specs()
    for spec in specs:
        with spec.plist_path.open("wb") as handle:
            plistlib.dump(payloads[spec.label], handle, sort_keys=False)
    return specs


def install_plists(specs: Iterable[AgentSpec]) -> None:
    USER_LAUNCH_AGENTS.mkdir(parents=True, exist_ok=True)
    for spec in specs:
        shutil.copy2(spec.plist_path, spec.installed_path)


def unload_agent(spec: AgentSpec) -> None:
    run(["launchctl", "bootout", launchctl_domain(), str(spec.installed_path)], check=False)


def load_agent(spec: AgentSpec) -> None:
    run(["launchctl", "bootstrap", launchctl_domain(), str(spec.installed_path)])
    run(["launchctl", "enable", f"{launchctl_domain()}/{spec.label}"], check=False)
    run(["launchctl", "kickstart", "-k", f"{launchctl_domain()}/{spec.label}"], check=False)


def ensure_hosts_entry(host_alias: str, bind_host: str) -> str:
    hosts_path = Path("/etc/hosts")
    original = hosts_path.read_text(encoding="utf-8")
    lines = original.splitlines()

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        tokens = stripped.split()
        if host_alias in tokens[1:]:
            if tokens[0] == bind_host:
                return "present"
            raise RuntimeError(f"{host_alias} already exists in /etc/hosts with {tokens[0]}")

    updated = original
    if updated and not updated.endswith("\n"):
        updated += "\n"
    updated += f"{bind_host}\t{host_alias}\n"
    hosts_path.write_text(updated, encoding="utf-8")
    return "added"


def remove_hosts_entry(host_alias: str) -> str:
    hosts_path = Path("/etc/hosts")
    original = hosts_path.read_text(encoding="utf-8")
    lines = original.splitlines()
    kept_lines = []
    removed = False

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            kept_lines.append(line)
            continue
        tokens = stripped.split()
        if host_alias in tokens[1:]:
            remaining_aliases = [token for token in tokens[1:] if token != host_alias]
            if remaining_aliases:
                kept_lines.append("\t".join([tokens[0], *remaining_aliases]))
            removed = True
            continue
        kept_lines.append(line)

    if not removed:
        return "absent"

    updated = "\n".join(kept_lines)
    if updated and not updated.endswith("\n"):
        updated += "\n"
    hosts_path.write_text(updated, encoding="utf-8")
    return "removed"


def install(host_alias: str, bind_host: str, port: int, interval: float, settle_seconds: float) -> int:
    specs = write_generated_plists(bind_host, port, interval, settle_seconds)
    install_plists(specs)

    for spec in specs:
        unload_agent(spec)
        load_agent(spec)

    hosts_result = ensure_hosts_entry(host_alias, bind_host)
    if server_responding(bind_host, port):
        print(f"Local site is responding at {server_url(host_alias, port)}")
    else:
        print(f"LaunchAgents installed. Check the server log if {server_url(host_alias, port)} does not respond yet.")
    print(f"Hosts entry: {hosts_result}")
    for spec in specs:
        print(f"LaunchAgent: {spec.installed_path}")
    return 0


def uninstall(host_alias: str) -> int:
    specs = agent_specs()
    for spec in specs:
        unload_agent(spec)
        spec.installed_path.unlink(missing_ok=True)
    hosts_result = remove_hosts_entry(host_alias)
    print(f"Removed hosts entry: {hosts_result}")
    for spec in specs:
        print(f"Removed LaunchAgent: {spec.installed_path}")
    return 0


def add_hosts(host_alias: str, bind_host: str, port: int) -> int:
    result = ensure_hosts_entry(host_alias, bind_host)
    print(f"Hosts entry: {result}")
    print(server_url(host_alias, port))
    return 0


def remove_hosts(host_alias: str) -> int:
    result = remove_hosts_entry(host_alias)
    print(f"Hosts entry: {result}")
    return 0


def status(host_alias: str, bind_host: str, port: int) -> int:
    print(f"Project root: {PROJECT_ROOT}")
    print(f"URL: {server_url(host_alias, port)}")
    print(f"Server responding on localhost: {'yes' if server_responding(bind_host, port) else 'no'}")
    for spec in agent_specs():
        print(f"{spec.label}: {'installed' if spec.installed_path.exists() else 'missing'}")
    return 0


def print_paths() -> int:
    for spec in agent_specs():
        print(spec.plist_path)
        print(spec.installed_path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install macOS LaunchAgents and a local hostname for the paper_collect site."
    )
    parser.add_argument("--hostname", default=DEFAULT_HOST_ALIAS, help=f"Local hostname to map (default: {DEFAULT_HOST_ALIAS})")
    parser.add_argument("--bind-host", default=DEFAULT_BIND_HOST, help=f"Bind host for the HTTP server (default: {DEFAULT_BIND_HOST})")
    parser.add_argument("--port", default=DEFAULT_PORT, type=int, help=f"HTTP port (default: {DEFAULT_PORT})")
    parser.add_argument("--interval", default=DEFAULT_INTERVAL, type=float, help=f"Watcher polling interval in seconds (default: {DEFAULT_INTERVAL})")
    parser.add_argument(
        "--settle-seconds",
        default=DEFAULT_SETTLE_SECONDS,
        type=float,
        help=f"Watcher settle delay in seconds (default: {DEFAULT_SETTLE_SECONDS})",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("write", help="Write generated LaunchAgent plists inside the project.")
    subparsers.add_parser("install", help="Install and load LaunchAgents, then add the hostname to /etc/hosts.")
    subparsers.add_parser("uninstall", help="Unload LaunchAgents and remove the hostname from /etc/hosts.")
    subparsers.add_parser("add-hosts", help="Add the hostname to /etc/hosts without touching LaunchAgents.")
    subparsers.add_parser("remove-hosts", help="Remove the hostname from /etc/hosts without touching LaunchAgents.")
    subparsers.add_parser("status", help="Show install status for the local site.")
    subparsers.add_parser("paths", help="Print generated and installed plist paths.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "write":
        specs = write_generated_plists(args.bind_host, args.port, args.interval, args.settle_seconds)
        for spec in specs:
            print(spec.plist_path)
        return 0
    if args.command == "install":
        return install(args.hostname, args.bind_host, args.port, args.interval, args.settle_seconds)
    if args.command == "uninstall":
        return uninstall(args.hostname)
    if args.command == "add-hosts":
        return add_hosts(args.hostname, args.bind_host, args.port)
    if args.command == "remove-hosts":
        return remove_hosts(args.hostname)
    if args.command == "status":
        return status(args.hostname, args.bind_host, args.port)
    if args.command == "paths":
        return print_paths()
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
