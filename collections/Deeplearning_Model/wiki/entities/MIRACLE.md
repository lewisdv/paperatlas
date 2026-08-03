# MIRACLE

## Type

- Continual-learning framework for multimodal mosaic single-cell atlas integration

## Definition

- MIRACLE means `multimodal integration with continual learning`.
- It wraps [MIDAS](MIDAS.md) so a multimodal atlas can be updated as new RNA, ATAC, and ADT datasets arrive without fully retraining on every earlier dataset.

## Core Components

- MIDAS's multimodal VAE provides the static mosaic-integration, batch-correction, and imputation substrate.
- Dynamic architecture adaptation adds parameters for newly encountered features or modalities and retains prior parameters as the starting point.
- Rehearsal training combines each new batch with a bounded sample of prior cells to mitigate catastrophic forgetting.
- Distribution-preserving reservoir sampling (`DPRS`) maintains past-batch proportions; ball-tree sampling (`BTS`) aims to preserve within-batch embedding distributions.

## Reported Uses

- Continual batch and cell-type integration of PBMC CITE-seq data.
- Incremental mosaic integration across RNA, ATAC, and ADT blocks.
- Cross-tissue trimodal atlas expansion and label transfer.
- Sequential integration of COVID-19, influenza A, and tuberculosis PBMC datasets.

## Caveats

- It inherits the modality scope and static-model assumptions of MIDAS.
- A fixed rehearsal memory trades computational bounds against coverage of rare states and historical variation.
- Update order, retained-cell sampling, model version, and preprocessing must be recorded to make an evolving atlas reproducible.
- Reported label refinements and disease-state findings are computational outputs that need independent validation.

## Related

- [Continual Single-Cell Atlas Integration](../concepts/continual-single-cell-atlas-integration.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [MIDAS](MIDAS.md)
- [StabMap](StabMap.md)
- [scVAEIT](scVAEIT.md)
- [Source: Continual integration of single-cell multimodal data with MIRACLE](../sources/zhou_2026_miracle_continual_multimodal_integration.md)
