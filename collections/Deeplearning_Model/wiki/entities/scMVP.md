# scMVP

## Type

- Non-symmetric multimodal variational autoencoder for paired single-cell RNA and ATAC data

## Definition

- `scMVP` stands for Single-Cell Multi-View Profiler.
- It jointly embeds same-cell RNA and chromatin-accessibility measurements and separately imputes each modality.

## Core Architecture

- Gaussian-mixture prior over a joint cell-state latent variable.
- Negative-binomial RNA and zero-inflated Poisson ATAC observation models.
- Mask-attention RNA branch and Transformer-derived self-attention ATAC branch.
- Separate modality decoders plus a cycle-consistency-style latent alignment loss.

## Reported Uses

- Denoising and imputation.
- Cell clustering and visualization.
- Differential-expression and cis-regulatory-element prioritization.
- Joint RNA-ATAC developmental trajectory inference.

## Caveats

- Requires paired RNA and ATAC in the same cells.
- Cluster geometry depends partly on the Gaussian-mixture specification.
- Downstream analyses of imputed values require separate inferential calibration.

## Related

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [MultiVI](MultiVI.md)
- [Source: A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data](../sources/li_2022_scmvp_multi-view_rna_atac.md)
