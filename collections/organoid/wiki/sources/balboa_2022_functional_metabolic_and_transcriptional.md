---
title: "Functional, metabolic and transcriptional maturation of human pancreatic islets derived from stem cells"
kind: paper
status: ingested
added: 2026-04-09T17:00:00+09:00
raw_source: raw/sources/balboa_2022_functional_metabolic_and_transcriptional.pdf
article_url: https://www.nature.com/articles/s41587-022-01219-z
published_date: 2022-02-10
organ: pancreas
protocol_focus: SC-islet functional maturation benchmarked against primary adult islets
deep_ingested: 2026-04-09
---

# Functional, metabolic and transcriptional maturation of human pancreatic islets derived from stem cells

## Source

- PDF: [raw/sources/balboa_2022_functional_metabolic_and_transcriptional.pdf](../../raw/sources/balboa_2022_functional_metabolic_and_transcriptional.pdf)
- Article: [Nature Biotechnology](https://www.nature.com/articles/s41587-022-01219-z)
- Labs: Timo Otonkoski + Diego Balboa (University of Helsinki; also CRG Barcelona)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: hPSCs (3 iPSC lines for robustness testing)
- Protocol innovations over baseline SC-islet methods:
  - Adherent differentiation until pancreatic progenitor stage (S4)
  - Optimized S4: nicotinamide + EGF + Activin A + ROCK inhibitor
  - **Microwell aggregation step** → ~80% PDX1+/NKX6-1+ pancreatic progenitor clusters
  - Improved final maturation stage (S7) in suspension culture
  - S7 omits ALK5 inhibitor and adds **aurora kinase inhibitor ZM447439** (anti-proliferative) + T3 + N-acetyl cysteine (NAC)
- Timepoints: S7w0 (start of final maturation) → S7w6 (6 weeks of maturation)
- Comparison: primary adult human islets
- Readouts: morphometry, GSIS (glucose-stimulated insulin secretion), metabolomics, electrophysiology, exocytosis, single-cell transcriptomics (in vitro + 6 months post-engraftment in mice)

## Key findings

- **Biphasic GSIS develops during in vitro S7 maturation** — by S7w2 onwards, SC-islets show biphasic responses similar to primary islets.
- **4-fold increase in insulin content** during first 3 weeks of S7.
- SC-β cells acquire **dense-core insulin granules resembling those of primary β cells** (ultrastructural).
- **Cytoarchitecture reorganizes**: from periphery-localized INS+ cells at S7w0 → polarized GCG+/INS+ clusters at S7w3 → intermingled mature cytoarchitecture at S7w6 (mirrors fetal islet development).
- **Ki-67+ proliferation reduces by 80%** during S7 — maturation linked to cell cycle exit.
- ZM / NAC / T3 all required for the maturation effect.
- SC-EC (enterochromaffin-like) byproduct cells reduce from ~13% → ~6.5% during S7 — another ZM-dependent outcome.
- Electrophysiology, signaling, and exocytosis approach primary islet levels.
- **Glycolytic and mitochondrial glucose metabolism still differ** from primary islets — maturation is not complete.
- scRNA-seq over 6 months of in vivo engraftment shows continued maturation trajectory converging toward primary islet transcriptome.

## Distinctive contribution in this corpus

- **Most comprehensive maturation benchmark** of SC-islets vs primary in the corpus.
- Establishes the "how mature are the cells really" framework for stem-cell-derived β cells.
- Identifies specific molecular maturation axes (cytoarchitecture, granule morphology, GSIS biphasicity, proliferation) and their dependencies.
- Complements Hogrebe 2021 (which is primarily about production protocol).

## Limitations and caveats

- Metabolic differences (glycolysis, mitochondrial metabolism) persist even after 6 weeks of S7.
- Maturation is assessed in vitro; full equivalence with adult β cells may require in vivo maturation.
- Primary islet comparison used donors at the lower end of functional responses — caveat for generalization.

## Relevance to corpus

- Together with Hogrebe 2021, establishes the current best-practice pair for pancreatic β cell generation (production + maturation).
- Represents the "functional fidelity" axis for pancreatic organoids — parallel to what Bhaduri 2020 did for brain organoids.

## Related concepts

- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Hogrebe 2021](hogrebe_2021_generation_of_insulin-producing_pancreatic.md) — complementary production-focused protocol (planar).
- [Koike 2021](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) — multi-organ model that includes pancreas lineage.
- [Bhaduri 2020](bhaduri_2020_cell_stress_in_cortical.md) — analogous "fidelity check vs primary" for brain.

## Open questions

- Why do glycolytic and mitochondrial metabolism remain different even after functional maturation?
- Can the ZM / NAC / T3 cocktail be transferred to other endocrine differentiation systems?
- What is the cytoarchitectural reorganization mechanism (mechanical? paracrine?)?
- How do Hogrebe 2021's planar SC-β cells compare on these maturation benchmarks?
