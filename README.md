# paper_collect

This workspace is a lightweight starter for the "LLM wiki" pattern described in the Karpathy gist:

- raw sources stay immutable
- the wiki is a maintained Markdown knowledge base
- `AGENTS.md` tells Codex how to behave in this repo
- `scripts/wiki.py` helps you add sources and track the workspace

The gist itself is not an installable app. This repo turns the idea into a local structure you can start using right away.

For the current Long Read WGS starter corpus, see `collections/Multi_Omics/long_read_wgs_manifest.tsv`, `collections/Multi_Omics/long_read_wgs_papers.xlsx`, and `scripts/download_long_read_wgs.sh`.

## Collections

You can keep separate research domains in separate collection workspaces under `collections/`.

```text
collections/
├── Deeplearning_Model/
├── Multi_Omics/
└── Organoid/
```

Each collection keeps its own `raw/`, `wiki/`, and `wiki_html/`, so unrelated topics do not mix.

## Layout

```text
paper_collect/
├── AGENTS.md
├── README.md
├── collections/
│   └── <collection>/
│       ├── raw/
│       │   ├── assets/
│       │   ├── derived/
│       │   └── sources/
│       ├── wiki/
│       │   ├── concepts/
│       │   ├── entities/
│       │   ├── queries/
│       │   ├── sources/
│       │   └── syntheses/
│       └── wiki_html/
└── scripts/
```

## Quick Start

Check the workspace status:

```bash
python3 scripts/wiki.py --collection Multi_Omics status
```

Add a source file into the immutable raw collection:

```bash
python3 scripts/wiki.py --collection Organoid add-source /absolute/path/to/paper.pdf --title "Paper Title" --kind paper
```

Add a source and immediately create OpenDataLoader helper artifacts:

```bash
python3 scripts/wiki.py --collection Organoid add-source /absolute/path/to/paper.pdf \
  --title "Paper Title" \
  --kind paper \
  --parse-with-opendataloader \
  --parse-format json,markdown
```

Parse an existing raw source later:

```bash
python3 scripts/wiki.py --collection Organoid parse-source \
  collections/Organoid/raw/sources/example.pdf \
  --parse-format json,markdown
```

Parse every source in a collection and skip ones that are already done:

```bash
python3 scripts/wiki.py --collection Organoid parse-all-sources --only-missing
```

Create a query page for a research question:

```bash
python3 scripts/wiki.py --collection Deeplearning_Model new-query "compare retrieval strategies" --question "How does persistent synthesis differ from plain RAG?"
```

Then ask Codex to do the knowledge work, for example:

```text
Read collections/<collection>/raw/sources/... and update the wiki according to AGENTS.md.
```

Re-download the curated Long Read WGS starter corpus:

```bash
./scripts/download_long_read_wgs.sh
```

Normalize the Long Read WGS corpus filenames and rebuild the spreadsheet:

```bash
python3 scripts/organize_long_read_wgs.py --collection Multi_Omics
```

Render the Markdown wiki as a static HTML site:

```bash
python3 scripts/render_wiki_html.py --collection Multi_Omics
```

This also refreshes the top-level `index.html` collection hub automatically.

Then open `collections/Multi_Omics/wiki_html/index.html`.

If your local HTML preview blocks navigation between pages, use the built-in localhost viewer instead:

```bash
python3 scripts/serve_wiki_html.py start
python3 scripts/serve_wiki_html.py status
python3 scripts/serve_wiki_html.py url
```

Then open `http://127.0.0.1:8765/index.html`. The generated HTML now prefers the localhost viewer automatically when it is running, and falls back to direct file links otherwise.

If you want the top-level site to stay available like a local website while your wiki keeps updating, use the combined site runtime helper:

```bash
python3 scripts/site_runtime.py start
python3 scripts/site_runtime.py status
python3 scripts/site_runtime.py url
python3 scripts/site_runtime.py stop
```

This starts both the localhost site server and the root watcher, so the top-level `index.html` stays available at the same URL while collections rerender in the background. The bundled watcher start also enables automatic git sync for changed collection files.

For a macOS login-time setup with a friendly local hostname such as `http://paperatlas.local:8765`, use:

```bash
python3 scripts/macos_local_site.py write
python3 scripts/macos_local_site.py install
python3 scripts/macos_local_site.py status
```

This generates LaunchAgent plists, installs them into `~/Library/LaunchAgents`, loads them with `launchctl`, and adds `paperatlas.local` to `/etc/hosts`. The watcher LaunchAgent also starts with git auto-sync enabled.

## GitHub Pages

This workspace can also be exported as a public static site for GitHub Pages.

Create a Pages-ready export locally:

```bash
python3 scripts/export_github_pages.py --output-dir site
```

If you explicitly want to publish the raw source PDFs too:

```bash
python3 scripts/export_github_pages.py --output-dir site --include-pdfs
```

By default, the export excludes PDFs. This is the safer default because many publisher PDFs should not be republished on a public website unless you know redistribution is allowed.

The repo also includes a GitHub Actions workflow at `.github/workflows/deploy-pages.yml`. After you put this workspace into a GitHub repository and push it, the workflow can build and deploy the exported static site to GitHub Pages automatically.

Recommended setup:

1. Create a GitHub repository such as `paperatlas` and push this workspace.
2. In the repository settings, use **Pages** with **GitHub Actions** as the source.
3. Push to `main` or `master`, or run the workflow manually.

For a user site, GitHub's quickstart currently uses a repository named `<username>.github.io`. For a project site, you can use a normal repository and publish it with the included workflow. See the official GitHub Pages quickstart: https://docs.github.com/ko/pages/quickstart

Example project-site URL:

- Repo: `https://github.com/<username>/paperatlas`
- Pages: `https://<username>.github.io/paperatlas/`

Keep every collection HTML site and the top-level hub updated automatically:

```bash
python3 scripts/watch_wiki_html.py start
python3 scripts/watch_wiki_html.py status
python3 scripts/watch_wiki_html.py stop
```

The root watcher polls `collections/` every 2 seconds, rerenders only the collection(s) that changed, and also regenerates the top-level `index.html`. It also catches newly added collections.

If you also want each successful wiki update to be committed and pushed to GitHub automatically, start the watcher with git auto-sync:

```bash
python3 scripts/watch_wiki_html.py start --git-auto-sync
```

This stages only the changed collection source files, creates an automatic commit, and pushes it to the current branch's `origin` remote after a successful rerender. The GitHub Pages workflow then rebuilds the public site from those pushed sources.

If you want a collection-scoped watcher instead:

```bash
python3 scripts/watch_wiki_html.py --collection Multi_Omics start
python3 scripts/watch_wiki_html.py --collection Multi_Omics status
python3 scripts/watch_wiki_html.py --collection Multi_Omics stop
```

The root watcher writes logs to `.render_watcher.log`. Collection-scoped watchers write logs to `collections/<collection>/wiki_html/render_watcher.log`.

The localhost viewer writes its PID and log to `.wiki_html_server.pid` and `.wiki_html_server.log`.

Create a new empty collection scaffold:

```bash
python3 scripts/wiki.py --collection Organoid init
python3 scripts/wiki.py --collection Multi_Omics init
python3 scripts/wiki.py --collection Deeplearning_Model init
```

## Suggested Workflow

1. Drop papers, articles, notes, or exports into `raw/sources/` with `add-source`.
2. If a PDF has difficult layout, run OpenDataLoader parsing to generate helper artifacts under `raw/derived/opendataloader/`.
3. Ask Codex to ingest one source at a time.
4. Let Codex update `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/index.md`, and `wiki/log.md`.
5. Ask questions against the wiki and save good answers in `wiki/queries/` or `wiki/syntheses/`.
6. Occasionally ask Codex to lint the wiki for stale claims, missing cross-links, and contradictions.

## Resuming After Context Loss

If a chat session loses context, use the collection-scoped resume view first:

```bash
python3 scripts/wiki.py --collection Organoid resume
python3 scripts/wiki.py --collection Multi_Omics resume
```

The `resume` command prints the key wiki entry points, recent log entries, latest query/synthesis pages, and any backlog where `raw/sources/` has not yet been turned into `wiki/sources/` or OpenDataLoader helper artifacts.

For a human-readable project handoff, also read `WORKFLOW_CHECKPOINT.md`.

## OpenDataLoader Integration

`opendataloader-pdf` is now treated as an optional preprocessing layer for layout-sensitive PDFs.

- It is useful when `pdftotext`-style extraction is too lossy.
- It does not replace the original source PDF.
- It does not replace the wiki workflow.

Generated files are written under:

```text
collections/<collection>/raw/derived/opendataloader/<source-stem>/
```

Typical contents include Markdown, JSON, and an `opendataloader-run.json` manifest. When a source page exists, `wiki/sources/*.md` gets a `Parsed Artifacts` section with links to those files.

Prerequisites for using the parser:

```bash
./scripts/setup_opendataloader_pdf.sh
```

For OCR or scanned-PDF workflows:

```bash
./scripts/setup_opendataloader_pdf.sh --with-hybrid
```

## Knowledge-Base-First Usage

For collection research, the safest pattern is to force Codex to stay inside the current collection knowledge base.

- Ask Codex to use only `collections/<collection>/wiki/` and `collections/<collection>/raw/`.
- If the answer is not supported there, Codex should say the information is not present instead of filling gaps from model memory.
- If the wiki is incomplete, ask Codex to open the relevant raw paper or source file, read it, and then repair the wiki before answering.
- After a useful answer, ask Codex to save it into `wiki/queries/` or `wiki/syntheses/` if you want that knowledge to persist.
- Periodically ask Codex to review the collection for duplicate or overlapping pages and suggest merges.

Helpful prompt patterns:

```text
Use only the knowledge in collections/<collection>/wiki and collections/<collection>/raw.
If the answer is not supported there, tell me that the knowledge base does not contain it.
```

```text
If the wiki does not contain enough detail, open the relevant raw source files,
read them, update the source pages, and then answer again.
```

```text
Save this answer as a query page in the wiki.
```

```text
Review this collection for duplicate or overlapping wiki pages and suggest what to merge.
```

## Notes

- The CLI uses only the Python standard library. No extra install step is required.
- If you want version history, run `git init` in this folder and commit the workspace.
