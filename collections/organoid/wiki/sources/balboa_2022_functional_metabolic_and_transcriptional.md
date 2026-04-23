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

## Related entities

- [Stem-cell-derived islets (SC-islets)](../entities/stem-cell-derived-islets-sc-islets.md)

## Related sources

- [Hogrebe 2021](hogrebe_2021_generation_of_insulin-producing_pancreatic.md) — complementary production-focused protocol (planar).
- [Koike 2021](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) — multi-organ model that includes pancreas lineage.
- [Bhaduri 2020](bhaduri_2020_cell_stress_in_cortical.md) — analogous "fidelity check vs primary" for brain.

## Open questions

- Why do glycolytic and mitochondrial metabolism remain different even after functional maturation?
- Can the ZM / NAC / T3 cocktail be transferred to other endocrine differentiation systems?
- What is the cytoarchitectural reorganization mechanism (mechanical? paracrine?)?
- How do Hogrebe 2021's planar SC-β cells compare on these maturation benchmarks?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:39:52+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/balboa_2022_functional_metabolic_and_transcriptional.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional -f json,markdown`
- Manifest: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/opendataloader-run.json](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/opendataloader-run.json)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional.json](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional.json)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional.md](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional.md)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile1.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile1.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile10.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile10.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile11.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile11.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile12.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile12.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile13.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile13.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile14.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile14.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile15.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile15.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile16.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile16.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile17.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile17.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile18.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile18.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile19.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile19.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile2.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile2.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile20.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile20.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile21.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile21.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile22.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile22.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile23.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile23.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile24.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile24.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile25.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile25.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile26.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile26.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile27.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile27.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile28.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile28.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile29.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile29.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile3.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile3.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile30.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile30.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile31.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile31.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile32.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile32.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile33.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile33.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile34.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile34.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile35.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile35.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile36.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile36.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile37.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile37.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile38.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile38.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile39.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile39.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile4.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile4.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile40.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile40.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile41.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile41.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile42.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile42.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile43.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile43.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile44.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile44.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile45.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile45.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile46.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile46.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile47.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile47.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile48.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile48.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile49.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile49.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile5.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile5.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile50.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile50.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile51.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile51.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile52.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile52.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile53.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile53.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile54.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile54.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile55.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile55.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile56.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile56.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile57.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile57.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile58.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile58.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile59.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile59.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile6.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile6.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile60.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile60.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile61.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile61.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile62.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile62.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile63.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile63.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile64.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile64.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile65.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile65.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile66.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile66.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile67.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile67.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile68.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile68.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile69.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile69.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile7.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile7.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile8.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile8.png)
- Output: [raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile9.png](../../raw/derived/opendataloader/balboa_2022_functional_metabolic_and_transcriptional/balboa_2022_functional_metabolic_and_transcriptional_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
