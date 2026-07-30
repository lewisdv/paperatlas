# Multi-Hop Mosaic Integration

## Definition

- Multi-hop mosaic integration connects datasets through a chain of pairwise feature overlaps even when some dataset pairs share no features.
- It replaces the requirement for one global feature intersection with the weaker requirement that the dataset graph remain connected.

## StabMap Strategy

- Build a mosaic data topology whose nodes are datasets and whose weighted edges represent pairwise feature overlap.
- Choose one or more reference coordinate systems.
- Predict those coordinates directly for adjacent datasets or iteratively along weighted shortest paths for non-adjacent datasets.
- Reweight and concatenate several reference projections when multiple references are selected.

## Bridge Datasets

- A bridge measures enough features or modalities to connect otherwise disjoint blocks.
- Bridge size, biological coverage, and feature informativeness determine whether repeated mappings preserve cell identity.
- In the StabMap PBMC simulation, performance is compromised below roughly 1,000 bridge cells and stabilizes above that size.
- Connectivity alone therefore does not guarantee identifiability or accurate transfer.

## Relation To Other Mosaic Methods

- [MultiVI](../entities/MultiVI.md) and [MIDAS](../entities/MIDAS.md) learn probabilistic latent spaces from paired or mosaic blocks.
- [scVAEIT](../entities/scVAEIT.md) learns conditional completion from authentic and random masks.
- [StabMap](../entities/StabMap.md) instead projects reference coordinates through pairwise overlaps and can wrap around an existing vertical or horizontal integration method.

## Evidence Boundaries

- Projection error can accumulate with path length.
- A reference emphasizes the biological variation present in that reference.
- Residual batch effects and nonlinear differences may remain.
- Transferred annotations or imputed features are predictions, not new observations.

## Sources

- [Stabilized mosaic single-cell data integration using unshared features](../sources/ghazanfar_2024_stabmap_mosaic_unshared_features.md)
