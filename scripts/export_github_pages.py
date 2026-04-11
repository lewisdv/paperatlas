#!/usr/bin/env python3

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from workspace import PROJECT_ROOT, list_collection_workspaces

RENDER_SCRIPT = PROJECT_ROOT / "scripts" / "render_wiki_html.py"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "site"

DATA_HREF_RE = re.compile(r'\sdata-(?:file|http)-href="[^"]*"')
LOCAL_VIEWER_LINK_RE = re.compile(
    r'<a[^>]*data-i18n-key="open_local_viewer"[^>]*>.*?</a>',
    re.DOTALL,
)
ROOT_LOCAL_VIEWER_RE = re.compile(
    r'<div class="hero-actions">\s*<a class="hero-button" href="http://127\.0\.0\.1:8765/index\.html">Open Local Viewer</a>\s*</div>',
    re.DOTALL,
)
WIKI_DATA_RE = re.compile(
    r'(<script id="wiki-data" type="application/json">)(.*?)(</script>)',
    re.DOTALL,
)


def run_render(command: list[str]) -> None:
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
    )
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip(), file=sys.stderr)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def render_all() -> None:
    for workspace in list_collection_workspaces():
        run_render([sys.executable, str(RENDER_SCRIPT), "--collection", workspace.key])
    run_render([sys.executable, str(RENDER_SCRIPT), "--workspace", str(PROJECT_ROOT)])


def sanitize_dashboard_data(html_text: str, include_pdfs: bool) -> str:
    match = WIKI_DATA_RE.search(html_text)
    if not match:
        return html_text

    data = json.loads(match.group(2))
    for page in data.get("pages", []):
        page["file_href"] = ""
        page["http_href"] = ""
        page["pdf_file_href"] = ""
        page["pdf_http_href"] = ""
        if not include_pdfs:
            page["pdf_href"] = ""

    replacement = (
        f"{match.group(1)}"
        f"{json.dumps(data, ensure_ascii=False)}"
        f"{match.group(3)}"
    )
    return html_text[: match.start()] + replacement + html_text[match.end() :]


def sanitize_html_file(path: Path, include_pdfs: bool) -> None:
    html_text = path.read_text(encoding="utf-8")
    html_text = DATA_HREF_RE.sub("", html_text)
    html_text = LOCAL_VIEWER_LINK_RE.sub("", html_text)
    html_text = ROOT_LOCAL_VIEWER_RE.sub('<div class="hero-actions"></div>', html_text)
    html_text = sanitize_dashboard_data(html_text, include_pdfs)
    path.write_text(html_text, encoding="utf-8")


def copy_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def export_site(output_dir: Path, include_pdfs: bool) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(PROJECT_ROOT / "index.html", output_dir / "index.html")
    copy_tree(PROJECT_ROOT / "assets", output_dir / "assets")

    for workspace in list_collection_workspaces():
        if workspace.wiki_html_dir.exists():
            copy_tree(
                workspace.wiki_html_dir,
                output_dir / "collections" / workspace.key / "wiki_html",
            )
        if include_pdfs and (workspace.raw_dir / "sources").exists():
            copy_tree(
                workspace.raw_dir / "sources",
                output_dir / "collections" / workspace.key / "raw" / "sources",
            )

    for html_path in output_dir.rglob("*.html"):
        sanitize_html_file(html_path, include_pdfs)

    (output_dir / ".nojekyll").write_text("", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Export a GitHub Pages-friendly static site from the paper_atlas workspace."
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help=f"Export directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--skip-render",
        action="store_true",
        help="Do not rerender wiki_html before exporting.",
    )
    parser.add_argument(
        "--include-pdfs",
        action="store_true",
        help="Include collections/*/raw/sources PDFs in the exported site.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not args.skip_render:
        render_all()
    export_site(output_dir, include_pdfs=args.include_pdfs)

    print(f"Exported GitHub Pages site to {output_dir}")
    if args.include_pdfs:
        print("Public PDFs: included")
    else:
        print("Public PDFs: excluded (recommended unless you know redistribution is allowed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
