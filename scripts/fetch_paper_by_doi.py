#!/usr/bin/env python3
"""Resolve a DOI (or arXiv / bioRxiv id) to an open-access PDF and download it.

Stdlib only. Strategy (in order):
  1. arXiv shortcuts: doi like 10.48550/arXiv.XXXX -> arxiv.org PDF
  2. bioRxiv / medRxiv shortcuts: doi like 10.1101/XXXX -> biorxiv.org or medrxiv.org PDF
  3. Unpaywall (https://api.unpaywall.org) -> best_oa_location.url_for_pdf
  4. Crossref (https://api.crossref.org/works/<doi>) -> message.link[].URL where content-type=='application/pdf'

If a candidate URL responds with 200 and content-type contains 'pdf', the bytes
are written to --out. Any redirect to a landing page (HTML) is rejected.

Returns JSON on stdout describing the outcome:
  {"status": "ok", "source": "unpaywall", "url": "...", "out": "..."}
  {"status": "not_found", "doi": "...", "tried": ["arxiv", "unpaywall", ...]}
  {"status": "error", "message": "..."}
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple


USER_AGENT = "paper_collect/0.1 (mailto:%s)"
TIMEOUT = 30


def http_json(url: str, email: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT % email, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def try_download_pdf(url: str, out: Path, email: str) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT % email, "Accept": "application/pdf,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            ctype = (resp.headers.get("Content-Type") or "").lower()
            data = resp.read()
        if "pdf" not in ctype and not data[:4] == b"%PDF":
            return False
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ConnectionError):
        return False


def arxiv_id_from_doi(doi: str) -> Optional[str]:
    m = re.match(r"10\.48550/arxiv\.(.+)$", doi.lower())
    if m:
        return m.group(1)
    m = re.match(r"arxiv:(.+)$", doi.lower())
    if m:
        return m.group(1)
    return None


def biorxiv_id_from_doi(doi: str) -> Optional[Tuple[str, str]]:
    """Return (server, full_doi) for biorxiv/medrxiv."""
    if doi.lower().startswith("10.1101/"):
        return ("biorxiv", doi)
    return None


def fetch_from_arxiv(arxiv_id: str, out: Path, email: str) -> Optional[str]:
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return url if try_download_pdf(url, out, email) else None


def fetch_from_biorxiv(doi: str, out: Path, email: str) -> Optional[str]:
    for server in ("biorxiv", "medrxiv"):
        api = f"https://api.biorxiv.org/details/{server}/{doi}/na/json"
        try:
            data = http_json(api, email)
        except Exception:
            continue
        coll = data.get("collection") or []
        for entry in coll:
            version_doi = entry.get("doi") or doi
            version = entry.get("version") or "1"
            url = f"https://www.{server}.org/content/{version_doi}v{version}.full.pdf"
            if try_download_pdf(url, out, email):
                return url
    return None


def fetch_from_unpaywall(doi: str, out: Path, email: str) -> Optional[str]:
    api = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={urllib.parse.quote(email)}"
    try:
        data = http_json(api, email)
    except Exception:
        return None
    candidates: List[str] = []
    locs = []
    best = data.get("best_oa_location") or {}
    if best:
        locs.append(best)
    locs.extend(data.get("oa_locations") or [])
    for loc in locs:
        if loc.get("url_for_pdf") and loc["url_for_pdf"] not in candidates:
            candidates.append(loc["url_for_pdf"])
        # PMC landing page → derive PDF URL. Prefer Europe PMC (no PoW challenge).
        landing = loc.get("url_for_landing_page") or loc.get("url") or ""
        m = re.search(r"/articles/(PMC\d+)/?", landing)
        if m:
            europe_pmc = f"https://europepmc.org/articles/{m.group(1)}?pdf=render"
            if europe_pmc not in candidates:
                candidates.append(europe_pmc)
            pmc_pdf = f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(1)}/pdf/"
            if pmc_pdf not in candidates:
                candidates.append(pmc_pdf)
    for url in candidates:
        if try_download_pdf(url, out, email):
            return url
    return None


def fetch_from_crossref(doi: str, out: Path, email: str) -> Optional[str]:
    api = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        data = http_json(api, email)
    except Exception:
        return None
    links = (data.get("message") or {}).get("link") or []
    for link in links:
        if "pdf" in (link.get("content-type") or "").lower() and link.get("URL"):
            if try_download_pdf(link["URL"], out, email):
                return link["URL"]
    return None


def fetch(doi: str, out: Path, email: str) -> dict:
    doi = doi.strip()
    tried: List[str] = []

    arxiv = arxiv_id_from_doi(doi)
    if arxiv:
        tried.append("arxiv")
        url = fetch_from_arxiv(arxiv, out, email)
        if url:
            return {"status": "ok", "source": "arxiv", "url": url, "out": str(out)}

    bio = biorxiv_id_from_doi(doi)
    if bio:
        tried.append("biorxiv/medrxiv")
        url = fetch_from_biorxiv(doi, out, email)
        if url:
            return {"status": "ok", "source": "biorxiv", "url": url, "out": str(out)}

    tried.append("unpaywall")
    url = fetch_from_unpaywall(doi, out, email)
    if url:
        return {"status": "ok", "source": "unpaywall", "url": url, "out": str(out)}

    tried.append("crossref")
    url = fetch_from_crossref(doi, out, email)
    if url:
        return {"status": "ok", "source": "crossref", "url": url, "out": str(out)}

    return {"status": "not_found", "doi": doi, "tried": tried}


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve a DOI to an OA PDF and download it.")
    parser.add_argument("--doi", required=True, help="DOI (e.g. 10.1101/2024.01.02.123456) or 'arXiv:...'")
    parser.add_argument("--out", required=True, help="Output PDF path.")
    parser.add_argument("--email", required=True, help="Contact email for Unpaywall + UA header.")
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    result = fetch(args.doi, out, args.email)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("status") == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
