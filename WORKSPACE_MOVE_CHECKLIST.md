# Workspace Move Checklist

Use this checklist when moving `paper_collect` to a new local path such as Dropbox.

## What Is Already Safe

- Most core scripts resolve the workspace root dynamically from their own file location.
- The main wiki workflows should continue to work after a move:
  - `scripts/wiki.py`
  - `scripts/render_wiki_html.py`
  - `scripts/serve_wiki_html.py`
  - `scripts/watch_wiki_html.py`
  - `scripts/site_runtime.py`
- The brain organoid deck builder now resolves its own local `outputs/`, `references/`, and font patcher paths without hardcoded absolute paths.

## Before Moving

1. Stop local services if they are running.
   - `python3 scripts/serve_wiki_html.py stop`
   - `python3 scripts/watch_wiki_html.py status`
2. If macOS LaunchAgents are installed for the local site, note that they will need to be reinstalled after the move.
3. Commit or back up any uncommitted changes you care about.

## Move

1. Move the entire `paper_collect` directory to the new path.
2. Reopen the workspace from the new location before running any scripts.

## After Moving

1. Recreate or repair the OpenDataLoader virtual environment.
   - The `.venv-opendataloader` interpreter path is location-sensitive.
   - Safest option:
     - remove `.venv-opendataloader`
     - run `./scripts/setup_opendataloader_pdf.sh`
2. Restart local HTML services from the new path if needed.
   - `python3 scripts/serve_wiki_html.py start`
   - `python3 scripts/watch_wiki_html.py start`
3. If you use the macOS local hostname setup, reinstall it from the new path.
   - `python3 scripts/macos_local_site.py uninstall`
   - `python3 scripts/macos_local_site.py install`

## Known Residual Items

- Existing source pages may still show historical absolute paths inside `Parsed Artifacts` command lines.
  - These are informational and do not affect the relative Markdown links to parsed outputs.
- Existing temporary render/verification logs may still contain old absolute paths.
  - These can be deleted safely if you do not need them.

## Recommended Validation

Run these from the new path:

```bash
python3 scripts/wiki.py --collection Organoid status
python3 scripts/render_wiki_html.py --collection Organoid
python3 scripts/serve_wiki_html.py start
python3 scripts/wiki.py --collection Organoid parse-all-sources --only-missing
```

If the first three succeed and OpenDataLoader parsing works again after the virtual environment rebuild, the move is functionally complete.
