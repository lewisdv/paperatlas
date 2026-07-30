# StabMap

## Type

- Reference-projection method for mosaic and multi-hop single-cell integration

## Definition

- StabMap integrates datasets with partially overlapping feature spaces by traversing a connected mosaic data topology.
- It does not require one feature to be shared across every dataset.

## Core Algorithm

- Dataset graph weighted by pairwise feature overlap.
- PCA, linear discriminant analysis, or supplied reference coordinates.
- Linear prediction of reference coordinates from shared features.
- Iterated projection along weighted shortest paths.
- Optional reweighting and concatenation of several reference spaces.

## Reported Uses

- RNA-ATAC and multi-platform mosaic integration.
- Multi-hop mapping through paired bridge datasets.
- Annotation and feature transfer across CyTOF, CITE-seq, IMC, Multiome, and Xenium.
- Mapping dissociated perturbation data onto spatial references.

## Caveats

- The dataset graph must be connected.
- Small or uninformative bridge datasets degrade mapping.
- The core projections are linear and residual batch correction is external.
- Reference selection defines which variation dominates the output space.

## Related

- [Multi-Hop Mosaic Integration](../concepts/multi-hop-mosaic-integration.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [MIDAS](MIDAS.md)
- [MultiVI](MultiVI.md)
- [Source: Stabilized mosaic single-cell data integration using unshared features](../sources/ghazanfar_2024_stabmap_mosaic_unshared_features.md)
