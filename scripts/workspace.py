#!/usr/bin/env python3

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS_DIR = PROJECT_ROOT / "collections"
COLLECTION_META_NAME = "collection.json"

TOKEN_OVERRIDES = {
    "ai": "AI",
    "hifi": "HiFi",
    "longread": "LongRead",
    "ont": "ONT",
    "wgs": "WGS",
}


def slugify_collection(value: str) -> str:
    lowered = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", lowered)
    normalized = normalized.strip("-")
    return normalized or "collection"


def humanize_collection_name(slug: str) -> str:
    parts = [part for part in slug.replace("_", "-").split("-") if part]
    rendered = []
    for part in parts:
        rendered.append(TOKEN_OVERRIDES.get(part, part.title()))
    return " ".join(rendered) or "Research Collection"


@dataclass
class Workspace:
    root: Path
    key: str
    title: str
    description: str

    @property
    def raw_dir(self) -> Path:
        return self.root / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.root / "wiki"

    @property
    def wiki_html_dir(self) -> Path:
        return self.root / "wiki_html"


def read_collection_metadata(root: Path) -> dict:
    meta_path = root / COLLECTION_META_NAME
    if not meta_path.exists():
        return {}
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def build_workspace(root: Path) -> Workspace:
    meta = read_collection_metadata(root)
    key = root.name
    title = meta.get("title") or humanize_collection_name(key)
    description = meta.get("description") or f"{title} research workspace."
    return Workspace(root=root, key=key, title=title, description=description)


def list_collection_workspaces() -> List[Workspace]:
    workspaces: List[Workspace] = []
    if not COLLECTIONS_DIR.exists():
        return workspaces

    for path in sorted(COLLECTIONS_DIR.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_dir() or path.name.startswith("."):
            continue
        if not ((path / "wiki").exists() or (path / COLLECTION_META_NAME).exists()):
            continue
        workspaces.append(build_workspace(path.resolve()))
    return workspaces


def resolve_workspace(
    *,
    collection: Optional[str] = None,
    workspace: Optional[str] = None,
    default_collection: Optional[str] = None,
) -> Workspace:
    if collection and workspace:
        raise ValueError("Use either --collection or --workspace, not both.")

    if workspace:
        root = Path(workspace).expanduser().resolve()
        return build_workspace(root)

    if collection:
        root = (COLLECTIONS_DIR / slugify_collection(collection)).resolve()
        return build_workspace(root)

    if (PROJECT_ROOT / "raw").exists() and (PROJECT_ROOT / "wiki").exists():
        return build_workspace(PROJECT_ROOT)

    if default_collection:
        root = (COLLECTIONS_DIR / slugify_collection(default_collection)).resolve()
        return build_workspace(root)

    raise ValueError(
        "No default workspace found. Pass --collection <name> or --workspace <path>."
    )
