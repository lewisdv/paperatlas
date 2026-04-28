#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from workspace import resolve_workspace


SCRIPT_DIR = Path(__file__).resolve().parent
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
)
EUROPEPMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
SEOUL = ZoneInfo("Asia/Seoul")
DEFAULT_PAGE_SIZE = 100
DEFAULT_MAX_PAGES = 2
SOURCE_METADATA_DIRNAME = "source_metadata"
PRUNED_STATUS = "pruned"

SEARCH_TERMS = [
    "organoid protocol",
    "assembloid protocol",
    "brain organoid protocol",
    "cortical organoid protocol",
    "forebrain organoid protocol",
    "retinal organoid protocol",
    "vascular organoid protocol",
    "intestinal organoid protocol",
    "colonic organoid protocol",
    "gastric organoid protocol",
    "liver organoid protocol",
    "cholangiocyte organoid protocol",
    "pancreatic organoid protocol",
    "lung organoid protocol",
    "airway organoid protocol",
    "kidney organoid protocol",
    "heart organoid protocol",
    "placenta organoid protocol",
    "endometrium organoid protocol",
    "mammary organoid protocol",
    "prostate organoid protocol",
    "esophageal organoid protocol",
    "cervical organoid protocol",
    "transplantation organoid protocol",
    "organoid engineering protocol",
    "organoid",
    "assembloid",
    "brain organoid",
    "cerebral organoid",
    "retinal organoid",
    "patient-derived organoid",
    "tumor organoid",
    "cancer organoid",
    "kidney organoid",
    "liver organoid",
    "intestinal organoid",
    "gastric organoid",
    "pancreatic organoid",
    "lung organoid",
    "placenta organoid",
    "trophoblast organoid",
    "endometrial organoid",
    "cholangiocyte organoid",
    "cervical organoid",
    "breast organoid",
    "prostate organoid",
    "xenograft organoid",
    "organoid biobank",
]

METHOD_KEYWORDS = [
    "protocol",
    "generation",
    "generating",
    "establishment",
    "engineering",
    "culture",
    "derived",
    "derive",
    "differentiation",
    "transplantation",
    "injection",
    "electroporation",
    "profiling",
    "incorporation",
    "shipping",
    "repair",
    "model",
]

EXCLUDED_TITLE_KEYWORDS = [
    "review",
    "guideline",
    "guidelines",
    "current and future",
    "current applications",
    "future applications",
    "systematic review",
    "comprehensive guide",
    "ethics",
    "medicine",
    "technology for",
    "perspective",
    "commentary",
    "current progress and challenges",
    "recent advances",
    "promising solution",
    "blood vessels in a dish",
    "ameliorating and refining",
    "technological innovations",
    "innovation and translation",
    "organoids and organs-on-chips",
    "from organoid culture to manufacturing",
    "poster session",
    "poster of distinction",
    "preliminary and ongoing",
    "bibliometric",
    "global trend",
    "applications and research advances",
    "current organoid models",
    "current models",
    "temporal evolution",
]


@dataclass
class Candidate:
    title: str
    article_url: str
    pdf_url: str
    pmcid: str
    doi: str
    author_string: str
    first_author: str
    journal: str
    year: str
    published_date: str
    abstract: str
    organ_guess: str
    focus_guess: str
    score: int
    query: str

    @property
    def slug(self) -> str:
        author = slugify(self.first_author or "paper")
        year = slugify(self.year or "undated")
        title = slugify(self.title)[:90].strip("-")
        return f"{author}_{year}_{title}".strip("_")


def slugify(text: str) -> str:
    lowered = normalize_dashes(text.lower()).strip()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "item"


def normalize_title(text: str) -> str:
    lowered = re.sub(r"\s+", " ", normalize_dashes(text.lower())).strip()
    return re.sub(r"[^a-z0-9]+", "", lowered)


def normalize_dashes(text: str) -> str:
    return (
        text.replace("\u2010", "-")
        .replace("\u2011", "-")
        .replace("\u2012", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2212", "-")
    )


def http_get(url: str, *, accept: str = "*/*", cookie: str = "") -> bytes:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": accept,
            **({"Cookie": cookie} if cookie else {}),
        },
    )
    with urlopen(request, timeout=120) as response:
        return response.read()


def europepmc_query(
    term: str,
    page_size: int = DEFAULT_PAGE_SIZE,
    max_pages: int = DEFAULT_MAX_PAGES,
) -> list[dict]:
    query = quote(
        f'({term}) AND PUB_TYPE:"research-article" '
        'AND OPEN_ACCESS:y AND HAS_PDF:y '
        'AND NOT JOURNAL:"bioRxiv" AND NOT JOURNAL:"medRxiv"'
    )
    rows: list[dict] = []
    seen_ids: set[str] = set()
    cursor_mark = "*"

    for _page in range(1, max_pages + 1):
        url = (
            f"{EUROPEPMC_URL}?query={query}&format=json&pageSize={page_size}"
            f"&cursorMark={quote(cursor_mark)}&resultType=core&sort_date:y"
        )
        payload = json.loads(http_get(url, accept="application/json").decode("utf-8"))
        result_rows = payload.get("resultList", {}).get("result", [])
        if not result_rows:
            break
        for row in result_rows:
            key = row.get("pmcid") or row.get("id") or json.dumps(row, sort_keys=True)
            if key in seen_ids:
                continue
            rows.append(row)
            seen_ids.add(key)
        next_cursor = payload.get("nextCursorMark")
        if len(result_rows) < page_size or not next_cursor or next_cursor == cursor_mark:
            break
        cursor_mark = next_cursor
    return rows


def infer_first_author(author_string: str, title: str) -> str:
    if author_string:
        primary = re.split(r",|;| and ", author_string)[0].strip()
        parts = primary.split()
        if parts:
            return parts[-1].strip(".")
    return title.split()[0]


def choose_organ(title: str, abstract: str) -> str:
    text = f"{title} {abstract}".lower()
    mapping = [
        ("blood-brain barrier", "blood-brain-barrier"),
        ("brainstem", "brainstem"),
        ("hippocamp", "hippocampus"),
        ("midbrain", "midbrain"),
        ("hindbrain", "hindbrain"),
        ("cerebell", "cerebellum"),
        ("forebrain", "brain"),
        ("cortical", "brain"),
        ("brain", "brain"),
        ("neural", "brain"),
        ("assembloid", "brain assembloid"),
        ("retina", "retina"),
        ("optic", "retina"),
        ("eye", "forebrain + eye"),
        ("vascular", "vascular"),
        ("blood vessel", "vascular"),
        ("intestinal", "colon-intestine"),
        ("colonic", "colon-intestine"),
        ("colon", "colon-intestine"),
        ("gastric", "gastric"),
        ("stomach", "gastric"),
        ("cholangiocyte", "biliary"),
        ("biliary", "biliary"),
        ("liver", "liver"),
        ("hepatic", "liver"),
        ("hepato", "liver"),
        ("pancrea", "pancreas"),
        ("islet", "pancreas"),
        ("lung", "lung"),
        ("airway", "lung"),
        ("alveolar", "lung"),
        ("kidney", "kidney"),
        ("renal", "kidney"),
        ("heart", "heart"),
        ("cardiac", "heart"),
        ("trophoblast", "placenta"),
        ("placenta", "placenta"),
        ("endometr", "endometrium"),
        ("mammary", "mammary"),
        ("breast", "breast"),
        ("prostate", "prostate"),
        ("esoph", "esophagus"),
        ("cerv", "cervix"),
        ("bone marrow", "bone-marrow"),
        ("tooth", "tooth"),
        ("tumor", "tumor"),
        ("cancer", "cancer"),
    ]
    for needle, label in mapping:
        if needle in text:
            return label
    return "organoid-system"


def normalize_focus(title: str) -> str:
    value = re.sub(r"^(A|An|The)\s+", "", title.strip(), flags=re.I)
    value = re.sub(
        r"^(Protocol for|Protocol to|Generating|Generation of|Establishment of|Engineering|Profiling|Injection and electroporation of|Development of)\s+",
        "",
        value,
        flags=re.I,
    )
    value = value.strip(" .")
    return value[:1].lower() + value[1:] if value else "organoid workflow"


def score_result(result: dict) -> int:
    title = sanitize_title(result.get("title", ""))
    journal = normalize_dashes((result.get("journalTitle") or "").lower())
    abstract = result.get("abstractText", "") or ""
    normalized = normalize_dashes(title.lower())
    if "organoid" not in normalized and "assembloid" not in normalized:
        return -999
    if re.match(
        r"^(?:#\d+[:.\s]|[A-Z]{1,10}-\d+(?:\.[A-Z0-9]+)?[.\s]|[A-Z]{1,10}\d{2,}(?:[-.][A-Z0-9]+)?(?:\s|\||:)|[A-Z]{2,}\d{2}-\d{2}\b|[A-Z]\d+[.\s]|\d{2,}\s)",
        normalize_dashes(title),
    ):
        return -999
    if any(word in normalized for word in EXCLUDED_TITLE_KEYWORDS):
        return -999
    if "(adv. sci." in normalized:
        return -999
    if any(word in journal for word in ["conference", "proceedings", "meeting abstracts"]):
        return -999

    score = 0
    if "protocol" in normalized:
        score += 8
    for keyword in METHOD_KEYWORDS:
        if keyword in normalized:
            score += 2
    if re.search(r"\bhere,?\s+(we\s+)?(describe|report|present|outline)\b", abstract, re.I):
        score += 3
    if result.get("pmcid"):
        score += 2
    year = result.get("pubYear") or ""
    if year.isdigit():
        score += max(0, int(year) - 2014)
    return score


def sanitize_title(title: str) -> str:
    cleaned = re.sub(r"\s+", " ", normalize_dashes(title)).strip()
    cleaned = re.sub(r"†.*$", "", cleaned).strip()
    cleaned = re.sub(r"\s*See DOI:.*$", "", cleaned, flags=re.I).strip()
    return cleaned


def candidate_from_result(result: dict, query: str) -> Optional[Candidate]:
    score = score_result(result)
    if score < 0:
        return None

    pmcid = result.get("pmcid") or ""
    article_url, pdf_url = europepmc_fulltext_urls(result, pmcid)
    if not pdf_url:
        return None

    title = sanitize_title((result.get("title") or "").strip())
    author_string = (result.get("authorString") or "").strip()
    first_author = infer_first_author(author_string, title)
    year = str(result.get("pubYear") or "")
    published_date = (
        result.get("firstPublicationDate")
        or result.get("electronicPublicationDate")
        or (f"{year}-01-01" if year else "")
    )
    abstract = (result.get("abstractText") or "").strip()
    organ_guess = choose_organ(title, abstract)
    focus_guess = normalize_focus(title)

    return Candidate(
        title=title,
        article_url=article_url,
        pdf_url=pdf_url,
        pmcid=pmcid,
        doi=(result.get("doi") or "").strip(),
        author_string=author_string,
        first_author=first_author,
        journal=(result.get("journalTitle") or "").strip(),
        year=year,
        published_date=published_date,
        abstract=abstract,
        organ_guess=organ_guess,
        focus_guess=focus_guess,
        score=score,
        query=query,
    )


def europepmc_fulltext_urls(result: dict, pmcid: str) -> tuple[str, str]:
    if pmcid.startswith("PMC"):
        article_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
        return article_url, f"{article_url}pdf/"

    html_urls: list[str] = []
    pdf_urls: list[str] = []
    for entry in result.get("fullTextUrlList", {}).get("fullTextUrl", []):
        if (entry.get("availabilityCode") or "").upper() != "OA":
            continue
        url = (entry.get("url") or "").strip()
        style = (entry.get("documentStyle") or "").lower()
        if not url:
            continue
        if style == "pdf":
            pdf_urls.append(url)
        elif style in {"html", "fulltext"}:
            html_urls.append(url)

    article_url = html_urls[0] if html_urls else ""
    if not article_url and result.get("doi"):
        article_url = f"https://doi.org/{result['doi']}"
    pdf_url = pdf_urls[0] if pdf_urls else ""
    if not article_url:
        article_url = pdf_url
    return article_url, pdf_url


def pmc_cookie_from_challenge(html: str) -> str:
    challenge = re.search(r'POW_CHALLENGE = "([^"]+)"', html)
    difficulty = re.search(r'POW_DIFFICULTY = "([^"]+)"', html)
    cookie_name = re.search(r'POW_COOKIE_NAME = "([^"]+)"', html)
    if not (challenge and difficulty and cookie_name):
        raise RuntimeError("PMC response was neither a PDF nor a recognized proof-of-work challenge")

    challenge_value = challenge.group(1)
    difficulty_value = int(difficulty.group(1))
    prefix = "0" * difficulty_value
    nonce = 0
    while True:
        digest = hashlib.sha256(f"{challenge_value}{nonce}".encode("utf-8")).hexdigest()
        if digest.startswith(prefix):
            return f"{cookie_name.group(1)}={challenge_value},{nonce}"
        nonce += 1


def download_pdf(url: str, output_path: Path) -> None:
    raw = http_get(url, accept="application/pdf,*/*")
    if raw.startswith(b"%PDF"):
        output_path.write_bytes(raw)
        return

    html = raw.decode("utf-8", errors="ignore")
    cookie = pmc_cookie_from_challenge(html)
    second = http_get(url, accept="application/pdf,*/*", cookie=cookie)
    if not second.startswith(b"%PDF"):
        raise RuntimeError("Downloaded payload was not a PDF after solving the PMC challenge")
    output_path.write_bytes(second)


def existing_source_state(root: Path) -> tuple[set[str], set[str], int]:
    sources_dir = root / "wiki" / "sources"
    raw_dir = root / "raw" / "sources"
    titles = set()
    stems = set()
    for path in sources_dir.glob("*.md"):
        stems.add(path.stem)
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^title:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if match:
            titles.add(normalize_title(match.group(1)))
    raw_only = []
    for pdf in raw_dir.glob("*.pdf"):
        stems.add(pdf.stem)
        if not (sources_dir / f"{pdf.stem}.md").exists():
            raw_only.append(pdf.stem)
    return titles, stems, len(raw_only)


def write_metadata(metadata_dir: Path, candidate: Candidate, pdf_path: Path) -> None:
    metadata_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "title": candidate.title,
        "article_url": candidate.article_url,
        "pdf_url": candidate.pdf_url,
        "pmcid": candidate.pmcid,
        "doi": candidate.doi,
        "author_string": candidate.author_string,
        "first_author": candidate.first_author,
        "journal": candidate.journal,
        "year": candidate.year,
        "published_date": candidate.published_date,
        "abstract": candidate.abstract,
        "organ_guess": candidate.organ_guess,
        "focus_guess": candidate.focus_guess,
        "query": candidate.query,
        "downloaded_at": datetime.now(SEOUL).isoformat(timespec="seconds"),
        "local_path": f"raw/sources/{pdf_path.name}",
    }
    (metadata_dir / f"{pdf_path.stem}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def run_local_command(args: list[str], cwd: Path) -> None:
    print("$ " + " ".join(args), flush=True)
    subprocess.run(args, cwd=str(cwd), check=True)


def discover_candidates(
    root: Path,
    needed: int,
    *,
    page_size: int = DEFAULT_PAGE_SIZE,
    max_pages: int = DEFAULT_MAX_PAGES,
    search_terms: Optional[list[str]] = None,
) -> list[Candidate]:
    existing_titles, existing_stems, _ = existing_source_state(root)
    pool: dict[str, Candidate] = {}

    for query in search_terms or SEARCH_TERMS:
        try:
            results = europepmc_query(query, page_size=page_size, max_pages=max_pages)
        except (HTTPError, URLError, json.JSONDecodeError) as exc:
            print(f"warning: discovery query failed for {query!r}: {exc}", file=sys.stderr)
            continue
        for result in results:
            candidate = candidate_from_result(result, query)
            if candidate is None:
                continue
            normalized_title = normalize_title(candidate.title)
            if normalized_title in existing_titles or candidate.slug in existing_stems:
                continue
            previous = pool.get(candidate.pmcid)
            if previous is None or candidate.score > previous.score:
                pool[candidate.pmcid] = candidate
        time.sleep(0.2)

    ranked = sorted(
        pool.values(),
        key=lambda cand: (-cand.score, cand.published_date or "9999-99-99", cand.title.lower()),
    )
    buffer = max(needed * 20, 240)
    return ranked[:buffer]


def current_counts(root: Path) -> tuple[int, int]:
    source_pages = 0
    for path in (root / "wiki" / "sources").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if re.search(r"^status:\s*%s\s*$" % PRUNED_STATUS, text, flags=re.MULTILINE):
            continue
        source_pages += 1
    raw_sources = len(list((root / "raw" / "sources").glob("*.pdf")))
    return source_pages, raw_sources


def main() -> None:
    parser = argparse.ArgumentParser(description="Expand the organoid collection to 100 papers and ingest them.")
    parser.add_argument("--collection", default="Organoid")
    parser.add_argument("--workspace")
    parser.add_argument("--target", type=int, default=100)
    parser.add_argument("--page-size", type=int, default=DEFAULT_PAGE_SIZE)
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    parser.add_argument(
        "--search-term",
        action="append",
        default=[],
        help="Optional repeated Europe PMC search terms to use instead of the built-in defaults.",
    )
    parser.add_argument("--skip-parse", action="store_true")
    parser.add_argument("--skip-ingest", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
    args = parser.parse_args()

    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="Organoid",
    )
    root = workspace.root
    metadata_dir = root / "raw" / "derived" / SOURCE_METADATA_DIRNAME
    raw_dir = root / "raw" / "sources"

    source_pages, raw_sources = current_counts(root)
    _, _, raw_without_pages = existing_source_state(root)
    downloads_needed = max(0, args.target - source_pages - raw_without_pages)

    print(f"Current organoid source pages: {source_pages}")
    print(f"Current organoid raw PDFs: {raw_sources}")
    print(f"Existing raw PDFs without source pages: {raw_without_pages}")
    print(f"New downloads needed to reach {args.target} ingested source pages: {downloads_needed}")

    downloaded = 0
    failures: list[str] = []

    if downloads_needed > 0:
        selected_terms = args.search_term or None
        candidates = discover_candidates(
            root,
            downloads_needed,
            page_size=args.page_size,
            max_pages=args.max_pages,
            search_terms=selected_terms,
        )
        if not candidates:
            raise RuntimeError("No new open-access organoid candidates were discovered from Europe PMC")

        existing_titles, existing_stems, _ = existing_source_state(root)
        for candidate in candidates:
            if downloaded >= downloads_needed:
                break
            if normalize_title(candidate.title) in existing_titles or candidate.slug in existing_stems:
                continue
            output_path = raw_dir / f"{candidate.slug}.pdf"
            try:
                print(f"Downloading [{downloaded + 1}/{downloads_needed}] {candidate.title}", flush=True)
                download_pdf(candidate.pdf_url, output_path)
                if output_path.stat().st_size < 50_000:
                    raise RuntimeError(f"downloaded PDF was suspiciously small: {output_path.stat().st_size} bytes")
                write_metadata(metadata_dir, candidate, output_path)
                run_local_command(
                    [
                        sys.executable,
                        str(SCRIPT_DIR / "wiki.py"),
                        "--collection",
                        workspace.key,
                        "register-source",
                        str(output_path),
                        "--title",
                        candidate.title,
                        "--kind",
                        "paper",
                    ],
                    SCRIPT_DIR.parent,
                )
                existing_titles.add(normalize_title(candidate.title))
                existing_stems.add(candidate.slug)
                downloaded += 1
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{candidate.title} ({exc})")
                if output_path.exists():
                    output_path.unlink()
            time.sleep(0.2)

        if downloaded < downloads_needed:
            print(
                f"warning: only downloaded {downloaded} new papers out of the required {downloads_needed}. "
                f"Recent failures: {failures[:5]}",
                file=sys.stderr,
            )

    if not args.skip_parse:
        run_local_command(
            [
                sys.executable,
                str(SCRIPT_DIR / "wiki.py"),
                "--collection",
                workspace.key,
                "parse-all-sources",
                "--only-missing",
            ],
            SCRIPT_DIR.parent,
        )

    if not args.skip_ingest:
        run_local_command(
            [
                sys.executable,
                str(SCRIPT_DIR / "generic_ingest_organoid_sources.py"),
                "--collection",
                workspace.key,
            ],
            SCRIPT_DIR.parent,
        )

    if not args.skip_manifest:
        run_local_command(
            [
                sys.executable,
                str(SCRIPT_DIR / "rebuild_organoid_manifest.py"),
                "--collection",
                workspace.key,
            ],
            SCRIPT_DIR.parent,
        )

    final_source_pages, final_raw_sources = current_counts(root)
    print("")
    print("Expansion complete")
    print(f"- final raw PDFs: {final_raw_sources}")
    print(f"- final source pages: {final_source_pages}")
    if failures:
        print(f"- download failures encountered and skipped before success: {len(failures)}")


if __name__ == "__main__":
    main()
