---
title: "An integrated transcriptomic cell atlas of human neural organoids"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf
article_url: https://www.nature.com/articles/s41586-024-08172-8
published_date: 2024-11-20
organ: brain
protocol_focus: integrated cross-protocol neural organoid cell atlas
deep_ingested: 2026-04-09
---

# An integrated transcriptomic cell atlas of human neural organoids

## Source

- PDF: [raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf](../../raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf)
- Article: [Nature](https://www.nature.com/articles/s41586-024-08172-8)
- Labs: Barbara Treutlein, J. Gray Camp, Fabian Theis — ETH Zürich / Roche / Helmholtz Munich (joint senior authors)
- Status: deep ingested 2026-04-09

## Study design

- Integrated 36 scRNA-seq datasets spanning 26 distinct neural organoid protocols
- Total cells: >1.7 million
- Reference mapping: against developing human brain cell atlases (4 primary brain references)
- Scope: unguided and guided protocols, various brain regions
- Deliverables: (1) integrated UMAP atlas, (2) programmatic interface to browse/query, (3) quantitative fidelity scores per protocol per region, (4) diseased organoid annotation framework

## Key findings

- **Atlas identifies which parts of the human developing brain ARE covered by existing protocols — and which remain uncovered**.
- Quantifies transcriptomic similarity between primary and organoid cells across all protocols on a common scale.
- Identifies **primary cell populations that are under-represented** in neural organoid models (important gap analysis).
- Atlas enables **automatic annotation of new organoid datasets** and side-by-side comparison of new vs. published protocols.
- Disease organoid analysis framework: uses healthy organoid atlas as "control cohort" to find disease-specific deviations.

## Distinctive contribution in this corpus

- **The single most comprehensive cross-protocol benchmarking resource in the corpus.**
- Builds directly on Velasco 2019, Bhaduri 2020, Kanton 2019, and many others — provides the meta-analysis they could not do alone.
- Answers the "which parts of the brain are we actually modeling" question that no individual protocol paper can answer.
- Includes assembloid (cf. Sloan 2018, Meng 2025) and transplantation (cf. Kelley 2024) data where available.

## Limitations and caveats

- Transcriptomics only — does not integrate electrophysiology, imaging, or morphology across protocols.
- Reference primary brain data sets have their own technical artifacts.
- "Under-represented" populations may reflect dissociation artifacts rather than absence.
- Cross-protocol comparison relies on harmonized annotation, which may mask protocol-specific biology.

## Relevance to brain synchronization query

- **The closest thing we have to a definitive cross-protocol mapping** of brain region coverage and fidelity.
- For any brain region question, this is the first place to check which protocol is best suited.
- Developmental stage mapping across protocols provides the maturation-axis quantification that was missing in Round 1.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — within-protocol reproducibility that this atlas contextualizes at cross-protocol scale.
- [Bhaduri 2020](bhaduri_2020_cell_stress_in_cortical.md) — primary cortex reference data used in the atlas.
- [Kanton 2019](kanton_2019_organoid_single-cell_genomic_atlas.md) — one of the foundational datasets integrated into this atlas.
- [Meng 2025](meng_2025_crispr_screens_in_human_neural.md) — perturbation data that can be compared against this atlas as control.

## Open questions

- Which brain regions remain most under-represented in existing protocols, and can the atlas guide targeted protocol development?
- How does the atlas handle recently published (post-2024) protocols?
- Can the disease-organoid framework generalize to non-brain organoid disease models?
