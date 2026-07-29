# scMODAL

## Type

- Feature-link-guided adversarial alignment framework

## Definition

- scMODAL aligns unpaired single-cell modalities using a limited set of known positively correlated cross-modal feature pairs.
- It is designed for both strongly linked modalities such as RNA/ATAC and weakly linked modalities such as RNA/protein.

## Core Architecture

- Nonlinear modality-specific encoders and decoders.
- GAN-based latent-distribution alignment.
- Mutual-nearest-neighbor anchors constructed from linked features.
- Autoencoding, anchor-distance, and geometry-preservation regularizers.

## Reported Uses

- RNA/protein, RNA/ATAC, tri-modal, and CODEX integration.
- Cross-modal label transfer and feature imputation.
- Feature-relation and spatial cell-communication inference.

## Caveats

- Requires known positive feature links.
- Correct cell-state matching collapses when the anchor penalty is removed.
- Imputed features and inferred networks need external validation.

## Related

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [GLUE](GLUE.md)
- [Source: scMODAL](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
