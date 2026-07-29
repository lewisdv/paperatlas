---
title: Multi-omics single-cell data integration and regulatory inference with graph-linked embedding
kind: paper
status: ingested
added: 2026-07-29T17:52:23+09:00
raw_source: raw/sources/cao_2022_glue_multi-omics_integration_regulatory_inference.pdf
---

# Multi-omics single-cell data integration and regulatory inference with graph-linked embedding

## Source

- File: [raw/sources/cao_2022_glue_multi-omics_integration_regulatory_inference.pdf](../../raw/sources/cao_2022_glue_multi-omics_integration_regulatory_inference.pdf)
- Added: 2026-07-29T17:52:23+09:00
- Venue/status: Nature Biotechnology 40, 1458-1466 (2022); published online 2 May 2022
- Authors: Zhi-Jie Cao and Ge Gao
- DOI: `10.1038/s41587-022-01284-4`
- SHA-256: `f6d812d3ef55c65a2ec30661a05f3ecbc3981e14236a018731ec186a13e99537`

## Summary

GLUE (`graph-linked unified embedding`) integrates unpaired single-cell modalities that have different feature spaces. It assigns each modality its own VAE, embeds cells in a shared latent space, and links modality-specific features through a signed regulatory `guidance graph`. A graph VAE encodes that prior, while adversarial learning aligns cell embeddings. Because feature embeddings reconstruct both the prior graph and observed omics data, GLUE also derives updated peak-gene and transcription-factor regulatory scores. The paper covers RNA/ATAC benchmarks, RNA/ATAC/methylation integration, regulatory inference, and atlas-scale integration over millions of cells.

## Methods

- Omics-specific VAEs use likelihoods matched to each modality while sharing a common latent-cell dimension.
- A signed guidance graph connects features across modalities, such as ATAC peaks to nearby genes and methylation measurements negatively to genes.
- A graph VAE learns feature embeddings from the guidance graph; inner products between cell and feature embeddings reconstruct each omics matrix.
- An omics discriminator performs adversarial alignment of cells from different modalities.
- Regulatory scores are cosine similarities between learned feature embeddings and can be evaluated against shuffled-embedding null distributions.

## Key Claims

- Biological prior graphs can orient otherwise unpaired feature spaces without explicit lossy feature conversion.
- Jointly fitting the graph and observed data makes integration and regulatory inference two outputs of the same model.
- Minibatch neural training and a multistage atlas procedure make unpaired integration feasible at million-cell scale.

## Evidence

- GLUE ranks first on the reported overall integration score across SNARE-seq, SHARE-seq, 10X Multiome, Nephron, and mouse primary motor cortex benchmarks.
- Against the second-best method, single-cell FOSCTTM alignment error is lower by `3.6x`, `1.7x`, and `1.5x` on SNARE-seq, SHARE-seq, and 10X Multiome.
- Integration performance changes little even when up to `90%` of guidance edges are corrupted; GLUE remains top-ranked at `2,000` cells but degrades more sharply below `1,000`.
- In triple-omics mouse cortex integration, marker overlap is significant at `FDR < 5 x 10^-17` for `12/14` cell types.
- Peak-gene regulatory inference reaches pcHi-C AUROC `0.631`, versus approximately `0.55` for Cicero, Pearson/Spearman correlation, and LASSO baselines.
- The atlas case integrates fetal scRNA-seq and scATAC-seq collections containing millions of cells and uses cross-modal evidence to revise ambiguous neural annotations.

## Limitations

- Alignment is influenced by the chosen guidance graph, even though corruption experiments show robustness for the tested priors.
- Neural training is less reliable on small datasets, especially below about `1,000` cells.
- The current graph is multipartite and mostly contains cross-modality edges; within-modality, multi-relational, and higher-order regulatory structures are not modeled.
- Regulatory scores learned from whole-atlas data can average over tissue- or time-specific circuits and should not be read as cell-context-specific causal edges.
- The authors warn that chained cross-modal imputation may introduce artifacts and damage regulatory inference.

## Related Pages

- [GLUE](../entities/GLUE.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [scMODAL](../entities/scMODAL.md)
- [scMultiMap](../entities/scMultiMap.md)

## Open Questions

- How stable are inferred regulatory edges to alternative but biologically plausible guidance graphs?
- When should a global atlas model be replaced by tissue- or state-specific GLUE models?
- Can paired observations be incorporated without letting abundant paired cell types dominate the unpaired atlas?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T18:04:58+0900
- Manifest: [raw/derived/opendataloader/cao_2022_glue_multi-omics_integration_regulatory_inference/opendataloader-run.json](../../raw/derived/opendataloader/cao_2022_glue_multi-omics_integration_regulatory_inference/opendataloader-run.json)
- Output: [raw/derived/opendataloader/cao_2022_glue_multi-omics_integration_regulatory_inference/cao_2022_glue_multi-omics_integration_regulatory_inference.md](../../raw/derived/opendataloader/cao_2022_glue_multi-omics_integration_regulatory_inference/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- Layout text: [raw/derived/pdftext/Cao_2022_GLUE/Cao_2022_GLUE.txt](../../raw/derived/pdftext/Cao_2022_GLUE/Cao_2022_GLUE.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
