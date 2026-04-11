#!/usr/bin/env python3
"""Deep ingest for Round 2/3/4 new organoid papers using opendataloader-pdf.

Extracts structured markdown from each PDF and writes it to a per-paper
cache directory, so we can read the real protocol content and enrich
the wiki source pages rather than relying on stub summaries.
"""

from __future__ import annotations

import os
import sys
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

ROOT = Path("/Users/davin/paper_collect/collections/organoid")
RAW_DIR = ROOT / "raw" / "sources"
CACHE_DIR = ROOT / "raw" / "ingest_cache_round234"
CACHE_DIR.mkdir(exist_ok=True)

# Papers added in rounds 2/3/4 — deep ingest targets
PAPERS = [
    # Round 2
    "pereira_2021_human_sensorimotor_organoids_derived",
    "wimmer_2019_generation_of_blood_vessel_organoids",
    "hogrebe_2021_generation_of_insulin-producing_pancreatic",
    "koehler_2017_generation_of_inner_ear_organoids",
    "vandervalk_2025_generation_and_characterization_of_vestibular",
    "velasco_2019_individual_brain_organoids_reproducibly",
    "he_2024_an_integrated_transcriptomic_cell_atlas",
    "kanton_2019_organoid_single-cell_genomic_atlas",
    # Round 3
    "yoon_2019_reliability_of_human_cortical",
    "bhaduri_2020_cell_stress_in_cortical",
    "kuwahara_2015_generation_of_a_ciliary",
    # Round 4
    "cakir_2019_engineering_of_human_brain",
    "homan_2019_flow-enhanced_vascularization_and_maturation",
    "worsdorfer_2019_generation_of_complex_human_organoid",
    "balboa_2022_functional_metabolic_and_transcriptional",
]


def extract_markdown(pdf_path: Path, out_dir: Path) -> Optional[Path]:
    """Run opendataloader-pdf convert → markdown. Return path to the .md file."""
    try:
        from opendataloader_pdf import convert
    except ImportError:
        print("ERROR: opendataloader-pdf not installed in this Python", file=sys.stderr)
        return None

    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        convert(
            str(pdf_path),
            output_dir=str(out_dir),
            format="markdown",
            quiet=True,
            table_method="cluster",
            reading_order="xycut",
        )
    except Exception as e:
        print(f"  EXTRACTION FAILED for {pdf_path.name}: {e}", file=sys.stderr)
        return None

    md_files = [f for f in out_dir.iterdir() if f.suffix == ".md"]
    if not md_files:
        return None
    return md_files[0]


def main() -> int:
    os.environ.setdefault("JAVA_HOME", "/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home")
    os.environ["PATH"] = "/usr/local/opt/openjdk@21/bin:" + os.environ.get("PATH", "")

    total = len(PAPERS)
    ok = 0
    failed: list[str] = []

    for idx, slug in enumerate(PAPERS, 1):
        pdf = RAW_DIR / f"{slug}.pdf"
        if not pdf.exists():
            print(f"[{idx}/{total}] MISSING PDF: {slug}")
            failed.append(slug)
            continue

        paper_cache = CACHE_DIR / slug
        md_file = paper_cache / f"{slug}.md"
        if md_file.exists() and md_file.stat().st_size > 10_000:
            print(f"[{idx}/{total}] SKIP (cached): {slug} ({md_file.stat().st_size // 1024} KB)")
            ok += 1
            continue

        print(f"[{idx}/{total}] Extracting: {slug}")
        result = extract_markdown(pdf, paper_cache)
        if result and result.stat().st_size > 1000:
            print(f"  ✅ {result.name} ({result.stat().st_size // 1024} KB)")
            ok += 1
        else:
            print(f"  ❌ extraction failed or too small")
            failed.append(slug)

    print(f"\n=== Summary: {ok}/{total} succeeded ===")
    if failed:
        print("Failed:")
        for f in failed:
            print(f"  - {f}")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
