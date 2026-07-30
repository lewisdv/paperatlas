# MultiVI

## Type

- Probabilistic multimodal and mosaic-integration model

## Definition

- MultiVI combines paired multiome and single-modality cells in one latent representation.
- It generates normalized or imputed RNA, ATAC, and protein features with uncertainty estimates.

## Core Architecture

- Modality-specific encoders and likelihood-matched decoders inherited from scVI, PeakVI, and [totalVI](totalVI.md).
- Symmetric-KL alignment and averaging of paired-cell latent distributions.
- Adversarial domain adaptation for batch correction.
- Posterior sampling for imputation uncertainty and Bayesian differential analysis.

## Reported Uses

- RNA/ATAC and RNA/ATAC/protein integration.
- Missing-modality imputation.
- Cross-modal differential expression and accessibility.
- Reanalysis of single-modality datasets using a paired multiome anchor.

## Caveats

- Many tests artificially unpair originally paired observations.
- Small datasets may not support stable modality-specific embeddings.
- Imputed molecular values remain model estimates rather than measurements.

## Related

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [MIDAS](MIDAS.md)
- [scVAEIT](scVAEIT.md)
- [scMVP](scMVP.md)
- [StabMap](StabMap.md)
- [totalVI](totalVI.md)
- [Source: MultiVI: deep generative model for the integration of multimodal data](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
