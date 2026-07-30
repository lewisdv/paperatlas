# scVAEIT

## Type

- Mask-conditioned variational autoencoder for single-cell multimodal mosaic integration and transfer

## Definition

- scVAEIT stands for `Single-Cell Variational AutoEncoder for Integration and Transfer learning`.
- It integrates datasets with partially overlapping RNA, protein, and chromatin-accessibility features or modalities and imputes the unobserved quantities.

## Core Architecture

- Mask encoder for authentic and randomly generated missingness patterns.
- Conditional variational encoder over observed values, mask embedding, and optional covariates.
- Joint latent representation with modality-specific negative-binomial or Bernoulli decoders.
- Combined masked-imputation ELBO and observed-feature reconstruction objective.
- Feature-blocked connections and mini-batch training for scalability.

## Reported Uses

- Bimodal and trimodal mosaic integration.
- Denoising and missing-feature or missing-modality imputation.
- Batch and experimental-condition adjustment.
- Transfer to unseen cell types, tissues, protocols, and partial feature panels.
- Reference-atlas training followed by low-cost query imputation.

## Evidence Boundary

- Held-out and external-dataset tests strengthen the transfer claim.
- Imputation metrics, joint-embedding quality, and downstream inferential validity are separate endpoints.
- Later MIDAS benchmarks report different method rankings under other mosaic configurations.

## Caveats

- Evidence is concentrated in blood-derived data.
- Robustness depends on training masks resembling meaningful missingness patterns.
- Imputed quantities require downstream uncertainty and false-discovery controls when used for biological testing.

## Related

- [Masked Conditional Multimodal Imputation](../concepts/masked-conditional-multimodal-imputation.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Post-Imputation Inference](../concepts/post-imputation-inference.md)
- [MIDAS](MIDAS.md)
- [MultiVI](MultiVI.md)
- [Source: Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
