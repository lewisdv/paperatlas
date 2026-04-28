#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

from workspace import resolve_workspace

SCRIPT_DIR = Path(__file__).resolve().parent

import deep_ingest_organoid_protocols as base
import wiki as wiki_cli


TODAY = datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat()
SOURCE_METADATA_DIRNAME = "source_metadata"
CURRENT_SOURCE_MARKER_BEGIN = "<!-- opendataloader:begin -->"
CURRENT_SOURCE_MARKER_END = "<!-- opendataloader:end -->"
PRUNED_STATUS = "pruned"

ORGAN_KEYWORDS = [
    ("blood-brain barrier", "blood-brain-barrier"),
    ("brainstem", "brainstem"),
    ("hippocamp", "hippocampus"),
    ("midbrain", "midbrain"),
    ("hindbrain", "hindbrain"),
    ("cerebell", "cerebellum"),
    ("telenceph", "brain"),
    ("forebrain", "brain"),
    ("cortical", "brain"),
    ("brain", "brain"),
    ("neural", "brain"),
    ("assembloid", "brain assembloid"),
    ("retina", "retina"),
    ("optic", "retina"),
    ("eye", "forebrain + eye"),
    ("inner ear", "inner-ear"),
    ("vestibular", "inner-ear"),
    ("tooth", "tooth"),
    ("intestinal", "colon-intestine"),
    ("colonic", "colon-intestine"),
    ("colon", "colon-intestine"),
    ("gastric", "gastric"),
    ("stomach", "gastric"),
    ("cholangiocyte", "biliary"),
    ("biliary", "biliary"),
    ("bile duct", "biliary"),
    ("hepato", "liver"),
    ("hepatic", "liver"),
    ("liver", "liver"),
    ("pancrea", "pancreas"),
    ("islet", "pancreas"),
    ("lung", "lung"),
    ("airway", "lung"),
    ("alveolar", "lung"),
    ("kidney", "kidney"),
    ("renal", "kidney"),
    ("nephron", "kidney"),
    ("heart", "heart"),
    ("cardiac", "heart"),
    ("blood vessel", "vascular"),
    ("vascular", "vascular"),
    ("bone marrow", "bone-marrow"),
    ("hematopo", "bone-marrow"),
    ("trophoblast", "placenta"),
    ("placenta", "placenta"),
    ("endometr", "endometrium"),
    ("uter", "endometrium"),
    ("mammary", "mammary"),
    ("breast", "breast"),
    ("prostate", "prostate"),
    ("esoph", "esophagus"),
    ("cerv", "cervix"),
    ("ductal", "ductal epithelial"),
    ("tumor", "tumor"),
    ("cancer", "cancer"),
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    frontmatter = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def active_source_pages(sources_dir: Path) -> list[Path]:
    pages: list[Path] = []
    for path in sorted(sources_dir.glob("*.md")):
        frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
        if frontmatter.get("status") == PRUNED_STATUS:
            continue
        pages.append(path)
    return pages


def pruned_source_count(sources_dir: Path) -> int:
    count = 0
    for path in sources_dir.glob("*.md"):
        frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
        if frontmatter.get("status") == PRUNED_STATUS:
            count += 1
    return count


def humanized_stem_title(stem: str) -> str:
    return stem.replace("_", " ")


def load_manifest_rows(manifest_path: Path) -> dict[str, dict]:
    if not manifest_path.exists():
        return {}
    rows = {}
    with manifest_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            stem = Path(row["filename"]).stem if row.get("filename") else Path(row["source_page"]).stem
            rows[stem] = row
    return rows


def load_source_metadata(metadata_dir: Path) -> dict[str, dict]:
    rows = {}
    if not metadata_dir.exists():
        return rows
    for path in sorted(metadata_dir.glob("*.json")):
        try:
            rows[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
    return rows


def choose_organ(title: str, abstract: str, fallback: str = "") -> str:
    text = f"{title} {abstract}".lower()
    for needle, organ in ORGAN_KEYWORDS:
        if needle in text:
            return organ
    return fallback or "organoid-system"


def readable_organ(organ: str) -> str:
    return organ.replace("-", " ")


def normalize_focus(text: str) -> str:
    lowered = text.strip()
    lowered = re.sub(r"^(A|An|The)\s+", "", lowered, flags=re.I)
    lowered = re.sub(r"^(Protocol for|Protocol to|Generating|Generation of|Establishment of|Engineering|Profiling|Injection and electroporation of|Development of)\s+", "", lowered, flags=re.I)
    lowered = lowered.strip(" .")
    return lowered[:1].lower() + lowered[1:] if lowered else "organoid workflow"


def guess_focus(title: str, organ: str, abstract: str = "") -> str:
    if title:
        return normalize_focus(title)
    if abstract:
        return f"{readable_organ(organ)} organoid workflow"
    return "organoid workflow"


def guess_bucket(title: str, focus: str, organ: str, abstract: str) -> str:
    text = f"{title} {focus} {organ} {abstract}".lower()
    if any(word in text for word in ["transplant", "engraft", "graft", "host circuit", "host integration", "repair"]):
        return "transplantation"
    if any(word in text for word in ["crispr", "screen", "imaging", "profiling", "electroporation", "microfluid", "chip", "mass spectrometry", "single-cell transcriptomics", "sequencing", "reporter", "shipping"]):
        return "engineering"
    if any(word in text for word in ["coculture", "co-culture", "microbe", "permeability", "infection", "assay", "injury model"]):
        return "functional"
    if any(word in text for word in ["patient-derived", "tumor", "cancer", "adult", "fetal", "clinical sample", "primary human", "cholangiocarcinoma", "prostate", "breast", "placenta", "endo-ectocervical"]):
        return "adult"
    if any(word in text for word in ["assembloid", "multi", "vascularized", "bilateral eye", "innervated", "bone marrow", "organoid-on-a-chip", "perfusable vasculature", "complex", "boundary"]):
        return "multi"
    return "foundation"


def guess_concepts(title: str, organ: str, bucket: str, focus: str) -> list[str]:
    text = f"{title} {focus} {organ}".lower()
    concepts: list[str] = []

    if bucket == "foundation":
        concepts.append("self-organization-and-directed-patterning")
    if bucket == "adult":
        concepts.append("adult-stem-cell-and-patient-derived-organoid-platforms")
    if bucket == "functional" or bucket == "transplantation":
        concepts.append("organoid-functional-assays-transplantation-and-coculture")
    if bucket == "engineering":
        concepts.append("organoid-engineering-imaging-and-screening")
    if bucket == "multi":
        concepts.append("multi-lineage-and-tissue-complexity")

    if any(word in text for word in ["brain", "cortical", "forebrain", "midbrain", "hindbrain", "brainstem", "hippocamp", "cerebell", "telenceph", "neural", "assembloid"]):
        concepts.append("brain-organoid-patterning-and-assembloids")
    if any(word in text for word in ["midbrain", "hindbrain", "brainstem", "hippocamp", "cerebell", "telenceph"]):
        concepts.append("brain-subregion-specific-organoid-protocols")
    if any(word in text for word in ["reproduc", "fidelity", "atlas", "single-cell", "transcriptom"]):
        concepts.append("brain-organoid-fidelity-reproducibility-and-atlases")
    if any(word in text for word in ["intestinal", "colonic", "colon", "gastric", "stomach", "hepatic", "hepato", "liver", "pancrea", "biliary", "cholangiocyte", "endometrium", "placenta"]):
        concepts.append("gastrointestinal-and-endodermal-organoid-systems")
    if any(word in text for word in ["kidney", "renal", "nephron"]):
        concepts.append("kidney-organoid-differentiation-routes")
    if any(word in text for word in ["heart", "cardiac", "hematopo", "blood-generating"]):
        concepts.append("cardiac-and-hematoendothelial-organoids")
    if any(word in text for word in ["vascular", "blood vessel", "perfusion", "permeability", "blood-brain barrier", "vasculature"]):
        concepts.append("organoid-vascularization-and-perfusion-strategies")
    if any(word in text for word in ["bone marrow", "innervated", "bilateral eye", "complex", "boundary", "vascularized"]):
        concepts.append("multi-lineage-and-tissue-complexity")

    unique = []
    for slug in concepts:
        if slug in base.CONCEPT_PAGES and slug not in unique:
            unique.append(slug)

    if not unique:
        unique.append("self-organization-and-directed-patterning")
    return unique[:4]


def guess_contribution(title: str, focus: str, abstract: str) -> str:
    abstract_line = first_sentence(abstract)
    if abstract_line:
        lowered = abstract_line[:1].lower() + abstract_line[1:]
        lowered = re.sub(r"^here,?\s+(we\s+)?(describe|report|present|outline)\s+", "", lowered, flags=re.I)
        lowered = lowered.rstrip(".")
        return lowered
    return f"establishes a workflow for {focus}"


def guess_relevance(organ: str, bucket: str, focus: str) -> str:
    branch = {
        "foundation": "baseline derivation coverage",
        "adult": "adult or patient-derived organoid coverage",
        "functional": "assay-layer coverage",
        "engineering": "engineering and platform-readout coverage",
        "multi": "multi-lineage organoid coverage",
        "transplantation": "host-context validation coverage",
    }[bucket]
    return f"extends the corpus with {readable_organ(organ)} work and strengthens the {branch} around {focus}"


def first_sentence(text: str) -> str:
    if not text:
        return ""
    collapsed = re.sub(r"\s+", " ", text).strip()
    match = re.search(r"(.+?[.!?])(\s|$)", collapsed)
    if match:
        return match.group(1).strip()
    return collapsed[:400].strip()


def extract_title_from_parsed_markdown(root: Path, stem: str) -> str:
    md_path = root / "raw" / "derived" / "opendataloader" / stem / f"{stem}.md"
    if not md_path.exists():
        return ""
    try:
        for line in md_path.read_text(encoding="utf-8").splitlines():
            cleaned = line.strip().lstrip("#").strip()
            if len(cleaned.split()) >= 4:
                return cleaned
    except OSError:
        return ""
    return ""


def extract_doi_url_from_parsed_markdown(root: Path, stem: str) -> str:
    md_path = root / "raw" / "derived" / "opendataloader" / stem / f"{stem}.md"
    if not md_path.exists():
        return ""
    try:
        for line in md_path.read_text(encoding="utf-8").splitlines()[:20]:
            cleaned = line.strip()
            if cleaned.startswith("https://doi.org/"):
                return cleaned
    except OSError:
        return ""
    return ""


def extract_parsed_artifacts_block(text: str) -> str:
    begin = text.find(CURRENT_SOURCE_MARKER_BEGIN)
    end = text.find(CURRENT_SOURCE_MARKER_END)
    if begin == -1 or end == -1 or end < begin:
        return ""
    return text[begin : end + len(CURRENT_SOURCE_MARKER_END)]


def patch_generated_page(page: str, ingested_date: str) -> str:
    page = page.replace(
        f"deep_ingested: {base.TODAY}\n",
        f"ingest_method: generic-auto\ningested: {ingested_date}\n",
    )
    page = page.replace(
        f"- Status: deep ingested on {base.TODAY}\n",
        f"- Status: ingested on {ingested_date}\n- Ingest method: generic auto-ingest from metadata, abstract text, and raw-PDF scope extraction\n",
    )
    page = page.replace(
        "## Limitations and caveats\n\n",
        "## Limitations and caveats\n\n"
        "- This page was generated from article metadata, abstract text, and raw-PDF scope extraction; it has not yet had a manual deep-ingest pass.\n",
        1,
    )
    page = page.replace("- Article: []()\n", "- Article: not recorded in local metadata\n")
    return page


def build_source_line(frontmatter: dict[str, str], filename: str) -> str:
    title = frontmatter.get("title") or filename
    if frontmatter.get("deep_ingested"):
        desc = "deeply ingested protocol source."
    elif frontmatter.get("status") == "ingested":
        focus = frontmatter.get("protocol_focus")
        desc = f"{focus}, ingested source page." if focus else "ingested source page."
    else:
        desc = f"{frontmatter.get('kind', 'paper')} source queued for ingest."
    return f"- [{title}](sources/{filename}) - {desc}"


def replace_section(text: str, heading: str, replacement_body: str) -> str:
    pattern = re.compile(rf"({re.escape(heading)}\n\n)(.*?)(?=\n## |\Z)", re.S)
    if not pattern.search(text):
        suffix = "" if text.endswith("\n") else "\n"
        return text + suffix + f"\n{heading}\n\n{replacement_body}\n"
    return pattern.sub(rf"\1{replacement_body}\n", text, count=1)


def source_sort_key(path: Path) -> tuple[str, str]:
    frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
    return (
        frontmatter.get("published_date", "9999-99-99"),
        frontmatter.get("title", path.name).lower(),
    )


def update_index(index_path: Path, sources_dir: Path) -> None:
    current = index_path.read_text(encoding="utf-8")
    source_pages = sorted(active_source_pages(sources_dir), key=source_sort_key)
    source_lines = "\n".join(
        build_source_line(parse_frontmatter(path.read_text(encoding="utf-8")), path.name)
        for path in source_pages
    )
    index_path.write_text(replace_section(current, "## Sources", source_lines), encoding="utf-8")


def update_overview(overview_path: Path, sources_dir: Path) -> None:
    source_pages = active_source_pages(sources_dir)
    frontmatters = [parse_frontmatter(path.read_text(encoding="utf-8")) for path in source_pages]
    total = len(frontmatters)
    deep = sum(1 for fm in frontmatters if fm.get("deep_ingested"))
    ingested = sum(1 for fm in frontmatters if fm.get("status") == "ingested" and not fm.get("deep_ingested"))
    queued = sum(1 for fm in frontmatters if fm.get("status") == "queued")
    pruned = pruned_source_count(sources_dir)

    organ_counts: dict[str, int] = {}
    for fm in frontmatters:
        organ = fm.get("organ")
        if not organ:
            continue
        organ_counts[organ] = organ_counts.get(organ, 0) + 1
    top_organs = sorted(organ_counts.items(), key=lambda item: (-item[1], item[0]))[:10]

    organ_lines = "\n".join(f"- {readable_organ(organ)}: {count}" for organ, count in top_organs)
    text = (
        "# Overview\n\n"
        f"This collection currently contains {total} active organoid-related source pages. "
        f"{deep} are deep-ingested protocol pages, {ingested} are standard ingested pages, {queued} remain queued, and {pruned} are pruned from the active corpus.\n\n"
        "## What this collection is good for\n\n"
        "- expanding organoid protocol coverage across developmental, patient-derived, assay-layer, transplantation, and engineering workflows\n"
        "- comparing self-organization, directed patterning, and multi-lineage assembly strategies across organ systems\n"
        "- identifying which papers are already deeply curated versus which newer additions still need a later deep-ingest pass\n"
        "- keeping low-signal conference abstracts, cover pages, and review-only additions out of the active protocol corpus while retaining them for traceability\n"
        "- using the organoid collection as a practical protocol and assay-planning map rather than only a static bibliography\n\n"
        "## Current source-page status\n\n"
        f"- Deep ingested: {deep}\n"
        f"- Standard ingested: {ingested}\n"
        f"- Queued: {queued}\n\n"
        "## Pruned source-page status\n\n"
        f"- Pruned from active corpus: {pruned}\n\n"
        "## Largest organ/system clusters\n\n"
        f"{organ_lines if organ_lines else '- Organ labels are still sparse for some sources.'}\n\n"
        "## Working note\n\n"
        "- New standard ingests are grounded in article metadata, abstract text, and raw-PDF scope extraction.\n"
        "- Use the deep-ingested pages first when you need the most curated cross-paper framing.\n"
        "- Pruned source pages remain in `wiki/sources/` with `status: pruned` so older cross-links do not break.\n"
        "- Use `python3 scripts/wiki.py --collection Organoid resume` to see the current backlog and latest query work.\n"
    )
    overview_path.write_text(text, encoding="utf-8")


def append_log(log_path: Path, created_or_updated: list[str]) -> None:
    if not created_or_updated:
        return
    existing = log_path.read_text(encoding="utf-8").rstrip()
    stamp = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M KST")
    preview = ", ".join(created_or_updated[:8])
    if len(created_or_updated) > 8:
        preview += ", ..."
    block = (
        f"\n\n## [{stamp}] generic ingest | Organoid batch update\n\n"
        f"- Generic-ingested {len(created_or_updated)} source pages using metadata, abstract text, and raw-PDF scope extraction.\n"
        "- Updated wiki/index.md and wiki/overview.md to reflect the expanded corpus.\n"
        f"- Representative source pages in this pass: {preview}\n"
    )
    log_path.write_text(existing + block + "\n", encoding="utf-8")


def metadata_for_stem(stem: str, manifest_rows: dict[str, dict], source_metadata: dict[str, dict]) -> dict:
    merged = {}
    manifest_row = manifest_rows.get(stem, {})
    merged.update(manifest_row)
    merged.update(source_metadata.get(stem, {}))
    return merged


def ensure_source_page(
    raw_pdf: Path,
    source_page: Path,
    title: str,
    root: Path,
) -> None:
    if source_page.exists():
        return
    wiki_cli.configure_workspace(root)
    wiki_cli.ensure_layout()
    source_page.write_text(
        wiki_cli.build_source_page(title, "paper", raw_pdf, source_page),
        encoding="utf-8",
    )


def discover_source_page_path(root: Path, stem: str) -> Path:
    return root / "wiki" / "sources" / f"{stem}.md"


def build_row(
    raw_pdf: Path,
    source_page: Path,
    frontmatter: dict[str, str],
    metadata: dict,
    root: Path,
) -> dict:
    parsed_title = extract_title_from_parsed_markdown(root, raw_pdf.stem)
    frontmatter_title = frontmatter.get("title", "")
    metadata_title = metadata.get("title", "")
    humanized_title = humanized_stem_title(raw_pdf.stem)
    if metadata_title and metadata_title != humanized_title:
        preferred_metadata_title = metadata_title
    else:
        preferred_metadata_title = ""
    if frontmatter_title and frontmatter_title != humanized_stem_title(raw_pdf.stem):
        preferred_frontmatter_title = frontmatter_title
    else:
        preferred_frontmatter_title = ""
    title = (
        preferred_metadata_title
        or preferred_frontmatter_title
        or parsed_title
        or frontmatter_title
        or humanized_title
    )
    abstract = metadata.get("abstract") or metadata.get("abstractText") or ""
    organ = (
        frontmatter.get("organ")
        or metadata.get("organ")
        or metadata.get("organ_guess")
        or choose_organ(title, abstract)
    )
    focus_candidates = [
        frontmatter.get("protocol_focus", ""),
        metadata.get("protocol_focus", ""),
        metadata.get("focus", ""),
        metadata.get("focus_guess", ""),
    ]
    preferred_focus = ""
    for candidate in focus_candidates:
        if candidate and candidate != humanized_title:
            preferred_focus = candidate
            break
    focus = preferred_focus or guess_focus(title, organ, abstract)
    article_url = (
        metadata.get("article_url")
        or frontmatter.get("article_url")
        or extract_doi_url_from_parsed_markdown(root, raw_pdf.stem)
        or ""
    )
    published_date = metadata.get("published_date") or frontmatter.get("published_date") or metadata.get("firstPublicationDate") or ""
    first_author = metadata.get("first_author") or frontmatter.get("first_author") or raw_pdf.stem.split("_", 1)[0].title()
    year = metadata.get("year") or frontmatter.get("year") or (published_date[:4] if published_date else "")
    added = frontmatter.get("added") or metadata.get("added") or datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    return {
        "title": title,
        "kind": frontmatter.get("kind", "paper"),
        "added": added,
        "local_path": str(raw_pdf.relative_to(root)).replace("\\", "/"),
        "source_page": str(source_page.relative_to(root)).replace("\\", "/"),
        "article_url": article_url,
        "published_date": published_date,
        "organ": organ,
        "focus": focus,
        "first_author": first_author,
        "year": str(year or ""),
    }


def ingest_source_page(
    root: Path,
    raw_pdf: Path,
    source_page: Path,
    manifest_rows: dict[str, dict],
    source_metadata: dict[str, dict],
) -> Optional[str]:
    current_text = source_page.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(current_text)
    if frontmatter.get("deep_ingested"):
        return None
    if frontmatter.get("status") == PRUNED_STATUS:
        return None
    if frontmatter.get("status") == "ingested" and frontmatter.get("ingest_method") != "generic-auto":
        return None

    stem = raw_pdf.stem
    metadata = metadata_for_stem(stem, manifest_rows, source_metadata)
    row = build_row(raw_pdf, source_page, frontmatter, metadata, root)
    abstract = metadata.get("abstract") or metadata.get("abstractText") or ""
    scope = first_sentence(abstract) or base.extract_scope(raw_pdf)
    bucket = guess_bucket(row["title"], row["focus"], row["organ"], abstract)
    note = {
        "bucket": bucket,
        "contribution": guess_contribution(row["title"], row["focus"], abstract),
        "relevance": guess_relevance(row["organ"], bucket, row["focus"]),
        "concepts": guess_concepts(row["title"], row["organ"], bucket, row["focus"]),
    }
    page = base.source_page_text(row, note, scope)
    page = patch_generated_page(page, TODAY)
    artifacts = extract_parsed_artifacts_block(current_text)
    if artifacts:
        page = page.rstrip() + "\n\n" + artifacts.rstrip() + "\n"
    source_page.write_text(page, encoding="utf-8")
    return Path(row["source_page"]).name


def main() -> None:
    parser = argparse.ArgumentParser(description="Generically ingest queued organoid sources.")
    parser.add_argument("--collection", default="Organoid")
    parser.add_argument("--workspace")
    args = parser.parse_args()

    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="Organoid",
    )
    root = workspace.root
    manifest_rows = load_manifest_rows(root / "organoid_protocols_manifest.tsv")
    source_metadata = load_source_metadata(root / "raw" / "derived" / SOURCE_METADATA_DIRNAME)

    created_or_updated: list[str] = []
    raw_sources = sorted((root / "raw" / "sources").glob("*.pdf"))

    for raw_pdf in raw_sources:
        source_page = discover_source_page_path(root, raw_pdf.stem)
        metadata = metadata_for_stem(raw_pdf.stem, manifest_rows, source_metadata)
        title = metadata.get("title") or raw_pdf.stem.replace("_", " ")
        ensure_source_page(raw_pdf, source_page, title, root)
        updated = ingest_source_page(root, raw_pdf, source_page, manifest_rows, source_metadata)
        if updated:
            created_or_updated.append(updated)

    update_index(root / "wiki" / "index.md", root / "wiki" / "sources")
    update_overview(root / "wiki" / "overview.md", root / "wiki" / "sources")
    append_log(root / "wiki" / "log.md", created_or_updated)

    print(f"Generic ingest completed for {len(created_or_updated)} organoid source pages")
    if created_or_updated:
        for name in created_or_updated[:20]:
            print(f"- {name}")
        if len(created_or_updated) > 20:
            print(f"- ... {len(created_or_updated) - 20} more")


if __name__ == "__main__":
    main()
