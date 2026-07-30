# MIDAS

## Type

- Deep generative mosaic-integration and knowledge-transfer framework

## Definition

- MIDAS integrates single-cell datasets with heterogeneous subsets of RNA, ATAC, and ADT measurements.
- It separates biological state from technical noise while performing batch correction, missing-modality imputation, and modality alignment.

## Core Architecture

- Modality-specific VAE encoders and decoders with a product-of-experts posterior.
- Self-supervised joint-posterior regularization for modality alignment.
- Information-bottleneck objectives for biological/technical latent disentanglement.
- Atlas-to-query model transfer and reciprocal label mapping.

## Reported Uses

- Rectangular and mosaic trimodal integration.
- Multimodal PBMC atlas construction.
- Missing-modality imputation, cell typing, and pseudotime analysis.
- Cross-tissue and reference-to-query knowledge transfer.

## Caveats

- The implementation supports three modalities.
- Fully diagonal integration remains difficult without reference transfer.
- Imputed features and computationally discovered populations require external validation.

## Related

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [MultiVI](MultiVI.md)
- [scVAEIT](scVAEIT.md)
- [StabMap](StabMap.md)
- [Source: Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
