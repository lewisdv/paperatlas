#!/usr/bin/env python3

from __future__ import annotations

import csv
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent / "collections" / "organoid"
MANIFEST = ROOT / "organoid_protocols_manifest.tsv"
LOG_PATH = ROOT / "wiki" / "log.md"
TODAY = "2026-04-10"

sys.path.insert(0, str(SCRIPT_DIR))
import deep_ingest_organoid_protocols as base


PENDING_NOTES = OrderedDict(
    [
        (
            "eura_2020_brainstem_organoids_from_human_pluripotent",
            {
                "bucket": "foundation",
                "contribution": "builds a brainstem organoid workflow that combines midbrain and hindbrain progenitors with dopaminergic, noradrenergic, cholinergic, and neural-crest-linked populations",
                "relevance": "extends the brain corpus beyond forebrain-heavy protocols into posterior brainstem territory",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                ],
                "scope": "Here, the authors describe a method for generating human brainstem organoids from hPSCs that contain midbrain and hindbrain progenitors, dopaminergic, noradrenergic, and cholinergic neurons, plus neural-crest-lineage cells.",
            },
        ),
        (
            "pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an",
            {
                "bucket": "foundation",
                "contribution": "creates free-floating hippocampal spheroids from human iPSCs that preserve hippocampal marker identity and support early Alzheimer-related phenotype readouts",
                "relevance": "adds a hippocampus-biased disease-modeling protocol that is more region-specific than generic cerebral organoids",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                ],
                "scope": "Here, the authors report a chemical strategy for rapidly generating free-floating hippocampal spheroids from human iPSCs, then use them to read out early Alzheimer-related phenotypes and NeuroD1-response programs.",
            },
        ),
        (
            "zagare_2021_a_robust_protocol_for_the",
            {
                "bucket": "foundation",
                "contribution": "derives midbrain organoids from patterned neuroepithelial stem cells with reproducible dopaminergic and glial composition",
                "relevance": "provides a robust midbrain baseline for Parkinson-oriented and ventral-midbrain studies",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                ],
                "scope": "Here, the authors describe a robust protocol for deriving human midbrain organoids from neuroepithelial stem cells, yielding dopaminergic neurons and glial cells suited to ventral-midbrain development and Parkinson disease modeling.",
            },
        ),
        (
            "valiulahi_2021_generation_of_caudal-type_serotonin_neurons",
            {
                "bucket": "foundation",
                "contribution": "patterns ventral hindbrain progenitors toward caudal serotonin neurons and adapts the system into hindbrain-like organoids",
                "relevance": "fills the hindbrain and serotonergic gap in a collection that previously leaned toward forebrain protocols",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                ],
                "scope": "Here, the authors describe a hindbrain differentiation strategy that uses ventralization and retinoic-acid caudalization to generate caudal serotonin neurons and serotonin-enriched hindbrain organoids from hPSCs.",
            },
        ),
        (
            "chen_2023_protocol_for_generating_reproducible_miniaturized",
            {
                "bucket": "foundation",
                "contribution": "miniaturizes midbrain organoids into controlled, necrosis-limited units that are compatible with higher-throughput screening",
                "relevance": "connects subregion-specific brain organoids to reproducible screening-scale workflows",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                    "organoid-engineering-imaging-and-screening",
                ],
                "scope": "Here, the authors present a protocol for generating miniaturized controlled midbrain organoids of reproducible size and composition without a necrotic center, enabling cost-effective screening-scale culture.",
            },
        ),
        (
            "atamian_2024_generation_and_long-term_culture_of",
            {
                "bucket": "foundation",
                "contribution": "uses dual-SMAD plus WNT and FGF8b patterning to generate cerebellar organoids with both rhombic-lip and ventricular-zone progenitors and support long-term Purkinje-cell maturation",
                "relevance": "adds a cerebellar long-term maturation route and expands coverage of caudal brain development",
                "concepts": [
                    "self-organization-and-directed-patterning",
                    "brain-organoid-patterning-and-assembloids",
                    "brain-subregion-specific-organoid-protocols",
                ],
                "scope": "Here, the authors describe a dual-SMAD plus WNT and FGF8b cerebellar organoid protocol that produces both rhombic-lip and ventricular-zone progenitors and supports long-term Purkinje-cell maturation.",
            },
        ),
    ]
)


NEW_CONCEPT = {
    "title": "Brain subregion-specific organoid protocols",
    "sources": [
        "lancaster_2014_generation_of_cerebral_organoids_from",
        "sloan_2018_generation_and_assembly_of_human",
        "giandomenico_2021_generation_and_long-term_culture_of",
        "fitzgerald_2024_generation_of_semi-guided_cortical_organoids",
        "ullah_2025_generating_and_characterizing_human_telencephalic",
        "eura_2020_brainstem_organoids_from_human_pluripotent",
        "pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an",
        "zagare_2021_a_robust_protocol_for_the",
        "valiulahi_2021_generation_of_caudal-type_serotonin_neurons",
        "chen_2023_protocol_for_generating_reproducible_miniaturized",
        "atamian_2024_generation_and_long-term_culture_of",
    ],
    "position": "This corpus now spans a continuum from broad cerebral organoids to explicitly patterned forebrain, brainstem, midbrain, hindbrain, hippocampal, and cerebellar protocols.",
    "synthesis": [
        "Lancaster and Giandomenico remain broad cerebral references, whereas Sloan and Ullah move toward cleaner forebrain or telencephalic control.",
        "Eura, Zagare, and Chen extend the corpus into brainstem and midbrain workflows, with Chen emphasizing miniaturization and screening-friendly control.",
        "Valiulahi, Pomeshchik, and Atamian fill caudal hindbrain, hippocampal, and cerebellar territory that would otherwise be missing from a forebrain-heavy brain collection.",
    ],
    "tension": [
        "region-specific fidelity versus broad developmental diversity",
        "screening-friendly control versus architectural richness and maturation",
    ],
    "questions": [
        "Which subregion protocol best matches the desired cell types, maturity window, and assay readout?",
        "Which protocol differences reflect true regional specification versus engineering for throughput or disease modeling?",
    ],
}


def read_rows() -> list[dict]:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t"))
    for row in rows:
        row["added"] = row.get("added") or datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    return rows


def extend_unique(values: list[str], additions: list[str]) -> None:
    for value in additions:
        if value not in values:
            values.append(value)


def patch_concepts() -> None:
    base.TODAY = TODAY

    additions = list(PENDING_NOTES.keys())
    extend_unique(base.CONCEPT_PAGES["self-organization-and-directed-patterning"]["sources"], additions)
    extend_unique(
        base.CONCEPT_PAGES["brain-organoid-patterning-and-assembloids"]["sources"],
        additions,
    )
    extend_unique(
        base.CONCEPT_PAGES["organoid-engineering-imaging-and-screening"]["sources"],
        ["chen_2023_protocol_for_generating_reproducible_miniaturized"],
    )

    brain = base.CONCEPT_PAGES["brain-organoid-patterning-and-assembloids"]
    brain["position"] = (
        "Brain-organoid protocols in this collection now split into broad cerebral self-organization, "
        "forebrain patterning, posterior brain subregion protocols, long-term maturation, transplantation, "
        "and perturbation-ready neural systems."
    )
    brain["synthesis"] = [
        "Lancaster remains the self-organizing cerebral reference point, whereas Sloan and Ullah move toward cleaner forebrain or telencephalic control.",
        "Eura, Zagare, Chen, Valiulahi, Pomeshchik, and Atamian extend the corpus into brainstem, midbrain, hindbrain, hippocampal, and cerebellar protocols rather than leaving it forebrain-dominant.",
        "Giandomenico and Fitzgerald emphasize later-stage maturation and functional readouts, while Kelley and Meng show how transplantation or pooled perturbation can become the next experimental layer.",
    ]
    brain["questions"] = [
        "Which brain questions require a specific subregion protocol rather than a broad cerebral organoid?",
        "What is the best tradeoff between regional control, long-term survival, functional readout, and experimental throughput?",
    ]

    if "brain-subregion-specific-organoid-protocols" not in base.CONCEPT_PAGES:
        updated = OrderedDict()
        for slug, data in base.CONCEPT_PAGES.items():
            updated[slug] = data
            if slug == "brain-organoid-patterning-and-assembloids":
                updated["brain-subregion-specific-organoid-protocols"] = NEW_CONCEPT
        base.CONCEPT_PAGES = updated
    else:
        base.CONCEPT_PAGES["brain-subregion-specific-organoid-protocols"] = NEW_CONCEPT


def write_sources(rows_by_stem: dict[str, dict]) -> None:
    for stem, note in PENDING_NOTES.items():
        row = dict(rows_by_stem[stem])
        row["scope"] = note["scope"]
        target = ROOT / row["source_page"]
        target.write_text(base.source_page_text(row, note, row["scope"]), encoding="utf-8")


def write_concepts(rows_by_stem: dict[str, dict]) -> None:
    touched = {
        "self-organization-and-directed-patterning",
        "brain-organoid-patterning-and-assembloids",
        "brain-subregion-specific-organoid-protocols",
        "organoid-engineering-imaging-and-screening",
    }
    concepts_dir = ROOT / "wiki" / "concepts"
    concepts_dir.mkdir(parents=True, exist_ok=True)
    for slug in touched:
        target = concepts_dir / f"{slug}.md"
        target.write_text(base.concept_page_text(slug, base.CONCEPT_PAGES[slug], rows_by_stem), encoding="utf-8")


def append_log() -> None:
    headline = "deep ingest | Brain subregion queued sources"
    current = LOG_PATH.read_text(encoding="utf-8")
    if headline in current:
        return
    stamp = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M KST")
    block = (
        f"\n## [{stamp}] {headline}\n\n"
        "- Deep-ingested six previously queued organoid sources covering brainstem, hippocampus, midbrain, hindbrain, and cerebellum.\n"
        "- Added concept page wiki/concepts/brain-subregion-specific-organoid-protocols.md.\n"
        "- Refreshed brain-focused concept pages so subregion-specific protocols show up in the organoid knowledge base.\n"
    )
    LOG_PATH.write_text(current.rstrip() + "\n" + block, encoding="utf-8")


def main() -> None:
    rows = read_rows()
    rows_by_stem = {base.protocol_stem(row): row for row in rows}
    missing = [stem for stem in PENDING_NOTES if stem not in rows_by_stem]
    if missing:
        raise KeyError(f"Missing manifest rows for: {', '.join(missing)}")

    patch_concepts()
    write_sources(rows_by_stem)
    write_concepts(rows_by_stem)
    append_log()

    print(f"Deep-ingested {len(PENDING_NOTES)} pending organoid sources")
    print("Updated concept pages: brain + subregion-specific coverage")


if __name__ == "__main__":
    main()
