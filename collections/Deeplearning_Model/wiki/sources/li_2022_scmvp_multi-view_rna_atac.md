---
title: A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data
kind: paper
status: ingested
added: 2026-07-30T16:44:15+09:00
raw_source: raw/sources/li_2022_scmvp_multi-view_rna_atac.pdf
---

# A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data

## Source

- File: [raw/sources/li_2022_scmvp_multi-view_rna_atac.pdf](../../raw/sources/li_2022_scmvp_multi-view_rna_atac.pdf)
- Added: 2026-07-30T16:44:15+09:00
- Authors: Gaoyang Li, Shaliu Fu, Shuguang Wang, Chenyu Zhu, Bin Duan, Chen Tang, Xiaohan Chen, Guohui Chuai, Ping Wang, and Qi Liu
- Venue: *Genome Biology* 23, 20 (2022)
- DOI: [10.1186/s13059-021-02595-6](https://doi.org/10.1186/s13059-021-02595-6)
- License stated in source: Creative Commons Attribution 4.0

## Summary

- `scMVP`, or Single-Cell Multi-View Profiler, is a non-symmetric multimodal variational autoencoder for same-cell RNA and chromatin-accessibility measurements.
- It learns one joint cell representation while retaining separate RNA and ATAC generation channels for denoising and imputation.
- The model combines a Gaussian-mixture latent prior, modality-specific count likelihoods, attention modules, and a cycle-consistency-style loss intended to preserve cluster semantics between raw and imputed profiles.
- Its reported tasks include cell clustering, visualization, differential analysis, cis-regulatory-element prioritization, and developmental trajectory inference across SNARE-seq, sci-CAR, Paired-seq, SHARE-seq, and 10x Multiome datasets.

## Data Regime And Architecture

- scMVP targets `vertical` integration: RNA and ATAC are measured in the same cell.
- Inputs are raw scRNA-seq counts and TF-IDF-transformed scATAC-seq peak values.
- A Gaussian-mixture model prior represents cell clusters in the common latent variable.
- RNA is modeled with a negative-binomial observation model; the paper models ATAC values with a zero-inflated Poisson distribution.
- The RNA branch uses mask attention, whereas the high-dimensional sparse ATAC branch uses multi-head self-attention derived from Transformer architectures.
- Separate decoders generate RNA and ATAC profiles from the joint latent code.
- Single-channel encoders re-embed each imputed modality, and a cycle-GAN-like consistency penalty reduces divergence between the joint latent representation and modality-specific imputed representations.
- The paper selects a 10-dimensional latent space in its initial cell-line experiments.

## Evidence

### Scalability And Imputation

- Runtime and memory were evaluated by subsampling 1,000 to 100,000 cells from a 67,418-cell SHARE-seq GM12878 dataset with 8,000 genes and 23,000 peaks.
- scMVP used 752 MB for 1,000 cells and 8.5 GB for 100,000 cells; training on 100,000 cells took under one hour on the reported GPU server.
- In sci-CAR, Paired-seq, and SNARE-seq cell-line data, scMVP-imputed RNA had higher correlation with corresponding bulk RNA measurements than raw counts and was generally similar to or better than scVI.
- For BJ, H1, K562, and GM12878 cells, median per-cell imputed ATAC peak counts were 4,114, 3,778, 1,017, and 1,251, compared with 918, 922, 404, and 442 raw peaks.
- The additional imputed peaks retained similar or higher overlap rates with bulk DNase-seq or ATAC-seq references in the reported cell lines.

### Cell Clustering

- Benchmarks include single-view methods, Seurat WNN, MultiVI, Cobolt, MOFA+, scAI, and other integration approaches.
- In the sci-CAR cell-line experiment, scMVP and several RNA-dominant baselines reach ARI values from 0.92 to 1, while WNN, cisTopic, and the tested universal integration tools score from 0.36 to 0.42.
- In Paired-seq, the universal methods score only 0.01 to 0.11, whereas scMVP remains competitive with the stronger single-view or paired-data methods.
- In a SNARE-seq P0 cortex dataset, the joint scMVP embedding reaches ARI 0.41, compared with 0.37 for its RNA-only mode, 0.30 for its ATAC-only mode, and 0.44 for WNN.
- In SHARE-seq mouse skin, joint scMVP reaches ARI 0.50, compared with 0.45 for its RNA-only mode, 0.34 for its ATAC-only mode, and 0.44 for WNN.

### Downstream Biological Analyses

- The realistic-data experiments include 5,081 SNARE-seq P0 cortex cells, 7,039 lymph-node T cells, 11,909 10x PBMC cells, and 34,773 SHARE-seq mouse-skin cells.
- In the P0 cortex analysis, candidate regulatory peaks derived from scMVP-imputed inputs show higher H3K4me3 enrichment near transcription start sites and higher H3K27ac or H3K4me1 enrichment at distal sites than peaks derived from raw counts.
- Diffusion-map trajectories built from the joint latent space recover reported progenitor-to-neuron and hair-follicle bulge-cell orderings.
- These trajectory and chromatin-enrichment results support downstream utility, but they do not directly validate every imputed molecular value.

## Interpretation

- scMVP is specialized for paired RNA+ATAC data and uses that same-cell correspondence more directly than methods designed for partially paired or fully unpaired regimes.
- Its non-symmetric branches encode an important principle: modalities can share cell state without sharing observation noise, dimensionality, or a suitable likelihood.
- The clustering-consistency objective tries to prevent strong denoising from erasing modality-specific biological structure.
- `Joint embedding quality`, `entrywise imputation`, and `regulatory inference` remain separate evaluation targets even though the paper places them in one pipeline.
- scMVP should not be confused with Cobolt; Cobolt is one of the comparison methods in this source.

## Limitations

- The method assumes same-cell RNA and ATAC pairing and does not directly solve diagonal or arbitrary mosaic integration.
- The Gaussian-mixture prior and predefined number of mixture components may influence the recovered cluster geometry.
- Several comparisons include methods designed for different data regimes, so a ranking does not isolate architecture alone.
- Bulk correlation, peak overlap, clustering ARI, and histone-mark enrichment are indirect validation of imputation rather than single-cell molecular ground truth.
- Differential and CRE analyses use imputed outputs without a general demonstration of post-imputation calibration or false-discovery control.
- The supplied PDF points to supplementary material that is not separately stored in this collection.

## Related Pages

- [scMVP](../entities/scMVP.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Multi-Omics Integration Method Taxonomy](../concepts/multi-omics-integration-method-taxonomy.md)
- [Post-Imputation Inference](../concepts/post-imputation-inference.md)
- [MultiVI](../entities/MultiVI.md)

## Open Questions

- How sensitive are cluster assignments and trajectories to the chosen Gaussian-mixture component count?
- Does explicit uncertainty propagation change the reported differential or CRE results?
- How would scMVP compare with newer paired-data models under harmonized preprocessing and held-out-cell evaluation?
- Can its asymmetric attention branches be retained while extending the model to missing modalities or unpaired cells?

## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Markdown: [raw/derived/opendataloader/li_2022_scmvp_multi-view_rna_atac/li_2022_scmvp_multi-view_rna_atac.md](../../raw/derived/opendataloader/li_2022_scmvp_multi-view_rna_atac/li_2022_scmvp_multi-view_rna_atac.md)
- Manifest: [raw/derived/opendataloader/li_2022_scmvp_multi-view_rna_atac/opendataloader-run.json](../../raw/derived/opendataloader/li_2022_scmvp_multi-view_rna_atac/opendataloader-run.json)
- Poppler layout text: [raw/derived/pdftext/Li_2022_scMVP/Li_2022_scMVP.txt](../../raw/derived/pdftext/Li_2022_scMVP/Li_2022_scMVP.txt)
- These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
