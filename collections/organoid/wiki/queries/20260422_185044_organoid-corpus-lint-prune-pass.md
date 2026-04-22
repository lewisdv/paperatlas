---
title: "Organoid corpus lint and prune pass"
status: active
created: 2026-04-22T18:50:44+09:00
---

# Remaining standard-page lint/prune pass

## Scope

- Goal: finish cleanup of the last `standard` source pages in the active organoid corpus.
- Rule: keep raw PDFs for traceability, prune commentary or supplement-style leftovers from the active corpus, and retain only pages that still add distinct primary evidence.
- Run date: 2026-04-22

## Result

- Pruned in this pass: 4
- Retained and manually deep-ingested in this pass: 1
- Active source pages remaining: 96
- Active deep-ingested source pages: 96
- Active standard-ingested source pages: 0
- Raw PDFs retained: yes

## Pruned sources

- [Beyond the Single Biopsy: Unveiling the Spatial Complexity of Gastric Cancer through Multi-Regional Organoids](../sources/d_2026_beyond-the-single-biopsy-unveiling-the-spatial-complexity-of-gastric-cancer-through-multi.md) - commentary or perspective article; evidence: `See "Patient-Derived Organoids from Multiple Sites of a Single Tumor..."`, `Corresponding Author`
- [Novel Pituitary Organoid Model as Powerful Tool to Unravel Pituitary Stem Cell Biology Across Ages and Disease](../sources/h_2021_novel-pituitary-organoid-model-as-powerful-tool-to-unravel-pituitary-stem-cell-biology-acr.md) - conference abstract supplement; evidence: `A652 | Journal of the Endocrine Society`, `Issue Supplement_1`
- [Canine Pituitary Organoids as 3D In Vitro Model for Cushing Disease](../sources/k_2021_canine-pituitary-organoids-as-3d-in-vitro-model-for-cushing-disease.md) - conference abstract supplement; evidence: `Journal of the Endocrine Society | A533`, `NEUROENDOCRINOLOGY AND PITUITARY BASIC RESEARCH ADVANCES`
- [In vitro and in silico approaches to engineering three-dimensional biological tissues and organoids](../sources/h_2022_in-vitro-and-in-silico-approaches-to-engineering-three-dimensional-biological-tissues-and.md) - secondary review article; evidence: `One contribution of 6 to a theme issue`, `This special edition showcases`

## Retained source

- [Modeling Atrial Fibrillation in a Human Heart Macrophage Assembloid](../sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.md) - retained and promoted to `deep_ingested` because it still provides distinct primary disease-assay value: an immune-bearing cardiac assembloid with `LPS`, `IFN-g`, and `IL-1B` triggering, `RT-qPCR` and confocal inflammasome readouts, plus `FluoVolt` rhythm phenotyping.

## Decision rule used in this pass

- Prune commentary or perspective pages that mainly point to another primary PDO study rather than supplying protocol details themselves.
- Prune supplement abstracts even when they contain interesting results, because the active corpus is being kept protocol-heavy and full-text-first.
- Prune theme-issue reviews when they summarize featured papers rather than acting as primary evidence.
- Retain short-form primary reports only when they still add a distinct organ-system or assay axis that is otherwise thin in the corpus.

## What changed in the corpus

- The active organoid corpus dropped from `100` to `96`, but every remaining active source page is now `deep-ingested`.
- The cardiac branch now includes an immune-enabled atrial-fibrillation assembloid note instead of a generic `standard` placeholder.
- The main backlog is no longer source-page cleanup; it is concept consolidation, entity creation, and higher-level synthesis.
