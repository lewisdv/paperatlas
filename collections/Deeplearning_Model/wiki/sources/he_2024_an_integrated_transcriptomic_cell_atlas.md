---
title: An integrated transcriptomic cell atlas of human neural organoids
kind: paper
status: ingested
added: 2026-04-29T22:21:17+09:00
raw_source: raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf
---

# An integrated transcriptomic cell atlas of human neural organoids

## Source

- File: [raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf](../../raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf)
- Added: 2026-04-29T22:21:17+09:00
- Venue/status: Nature article; published online 20 November 2024
- Authors: Zhisong He, Leander Dony, Jonas Simon Fleck, Artur Szalata, Katelyn X. Li, Irena Sliskovic, Hsiu-Chuan Lin, Malgorzata Santel, Alexander Atamian, Giorgia Quadrato, Jieran Sun, Sergiu P. Pasca, Human Cell Atlas Organoid Biological Network, J. Gray Camp, Fabian J. Theis, and Barbara Treutlein
- DOI: `10.1038/s41586-024-08172-8`

## Summary

This paper builds an integrated human neural organoid cell atlas by harmonizing dozens of scRNA-seq studies into one reference resource for cell-type annotation, protocol comparison, and disease-model analysis. The atlas is not itself a deep model, but it provides a queryable reference system and benchmarking substrate for evaluating organoid fidelity against primary human brain development. In this collection, the paper matters because it adds a large atlas-and-query infrastructure layer that can support data projection, protocol evaluation, and disease-state comparison.

## Methods

- The study integrates `36` single-cell transcriptomic datasets spanning `26` neural organoid protocols into one atlas containing about `1.77` million cells after preprocessing and quality control.
- Batch correction and label harmonization use a three-step pipeline: reference similarity spectrum (RSS) projection to a developing human brain atlas, preliminary marker-based hierarchical annotation with `snapseed`, and label-aware integration with `scPoli`.
- The integrated atlas is mapped to primary developing human brain references to transfer cell class, regional, and neurotransmitter labels and to assess which in vivo states are represented or under-represented in organoids.
- The authors reconstruct developmental trajectories and pseudotime using neural optimal transport with `moscot`.
- The resource is also used for morphogen-screen analysis, protocol comparison, disease-model annotation, differential expression, and projection of new datasets into the atlas.

## Key Claims

- A unified transcriptomic atlas can quantitatively assess which neural states current organoid protocols capture and where they remain incomplete relative to human brain development.
- Atlas projection provides a practical way to annotate new organoid datasets, compare protocols, and evaluate neural disease models against a diverse control cohort.
- Universal cell-stress signatures, especially linked to glycolytic metabolism, explain part of the gap between organoid neurons and primary neurons without erasing core cell identities.
- Queryable atlas infrastructure is itself a valuable modeling substrate, even when the main contribution is not a new end-to-end foundation model.

## Evidence

- The atlas integrates `36` datasets from `34` published and `2` unpublished sources, covering `26` organoid protocols across ages from `7` to `450` days.
- The paper explicitly states that the atlas totals more than `1.7` million cells and provides a programmatic interface for browsing the atlas and querying new datasets.
- `scPoli` is reported as the best-performing integration method among those tested in their benchmarking pipeline.
- Mapping to primary references identifies under-represented neural states and shows increasing similarity of older organoids to second-trimester states, but not substantial matching to later developmental stages.
- Disease-model and morphogen-screen projections are used as demonstrations that the atlas can act as a control cohort and a protocol-evaluation framework rather than just a static compendium.

## Limitations

- This source is primarily an atlas resource and integration pipeline, not a new reusable deep foundation model trained for broad task transfer.
- Its conclusions depend on the quality and compatibility of the underlying public organoid studies, protocols, and annotation references.
- The fidelity analyses are transcriptomic and do not by themselves resolve functional equivalence across all biological axes.
- In this collection, the paper is somewhat peripheral to the single-cell foundation-model thread, so its main value is infrastructural and benchmarking-oriented.

## Related Pages

- [HNOCA](../entities/HNOCA.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)

## Open Questions

- How much of organoid benchmarking should be treated as a pretraining substrate for future models rather than only as an evaluation resource?
- If similar atlases are added for other systems, does this collection need a broader page on queryable biological reference atlases?
- Could the fidelity metrics used here become a standard benchmark for models that generate or retrieve neural organoid states?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:20:28+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/he_2024_an_integrated_transcriptomic_cell_atlas.pdf -o /tmp/odl-check-neural-organoid -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/he_2024_an_integrated_transcriptomic_cell_atlas/opendataloader-run.json](../../raw/derived/opendataloader/he_2024_an_integrated_transcriptomic_cell_atlas/opendataloader-run.json)
- Output: [raw/derived/opendataloader/he_2024_an_integrated_transcriptomic_cell_atlas/he_2024_an_integrated_transcriptomic_cell_atlas.md](../../raw/derived/opendataloader/he_2024_an_integrated_transcriptomic_cell_atlas/he_2024_an_integrated_transcriptomic_cell_atlas.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
