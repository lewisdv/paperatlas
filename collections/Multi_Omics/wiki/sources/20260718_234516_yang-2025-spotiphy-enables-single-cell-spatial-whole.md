---
title: "Spotiphy enables single-cell spatial whole transcriptomics across an entire section"
kind: paper
status: ingested
added: 2026-07-18
deep_ingested: 2026-07-18
doi: 10.1038/s41592-025-02622-5
pmid: 40074951
pmcid: PMC11978521
authors: Yang J et al.
journal: Nature Methods (2025)
raw_source: raw/sources/20260718_234516_yang-2025-spotiphy-enables-single-cell-spatial-whole.pdf
pdf_status: downloaded
---

# Spotiphy enables single-cell spatial whole transcriptomics across an entire section

## Key findings

- Spotiphy combines spot-level sequencing spatial transcriptomics, scRNA-seq references, and histological nucleus segmentation in a probabilistic generative model.
- It estimates cell-type proportions, decomposes spots into inferred single-cell transcriptomes, and imputes cells in noncapture regions to create whole-section images.
- Against 13 deconvolution methods, matched/simulated benchmarks generally gave Spotiphy the strongest or near-strongest accuracy with lower computational time.
- Applications resolved astrocyte and disease-associated microglia regionalization in Alzheimer mouse brain and altered tumor–microenvironment interactions in human breast tissue.

## Limitations

- Output is model-inferred rather than directly measured single-cell whole-transcriptome data.
- Accuracy depends on reference completeness, segmentation, alignment, and assumptions used to fill noncapture space; rare-cell claims require orthogonal validation.

## Related

- [Spatial transcriptomics and multiomic integration](../concepts/spatial-transcriptomics-and-multiomic-integration.md)
- [Single-cell atlas integration and reference reuse](../concepts/single-cell-atlas-integration-and-reference-reuse.md)

