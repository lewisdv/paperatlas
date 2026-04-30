# Transcriptomic Fidelity Benchmarking

## Definition

- Transcriptomic fidelity benchmarking is the evaluation of how closely an in vitro or generated cellular system matches a primary reference state using transcriptomic similarity, coverage, and differential-expression analyses.
- In this collection, the concept is tied to atlas-based comparison of organoid cells against primary developing human brain references.

## In This Collection

- [HNOCA](../entities/HNOCA.md) provides a concrete benchmarking framework by integrating neural organoid datasets and mapping them to primary brain references.
- The source uses fidelity metrics to compare protocols, identify under-represented states, and separate core identity from common stress-related divergence.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md) and [Hierarchical Partial Rejection](hierarchical-partial-rejection.md), the emphasis here is not a per-cell confidence threshold but diagnosis of where an entire in vitro system falls outside strong primary-reference coverage.
- Compared with [Region-Specific Developmental Trajectories](region-specific-developmental-trajectories.md), fidelity benchmarking is the system-level question of whether those trajectories and regional states are actually covered or developmentally matched.
- Compared with [Sex-Stratified Transcriptomic Burden](sex-stratified-transcriptomic-burden.md), this concept tracks reference mismatch and missing-state coverage rather than subgroup-specific disease asymmetry.

## Claimed Benefits

- Turns heterogeneous atlas data into a quantitative protocol-evaluation resource.
- Helps distinguish whether poor performance reflects missing cell states, immature developmental timing, or universal in vitro stress.
- Provides a reusable substrate for projecting and comparing new datasets.

## Caveats

- Transcriptomic similarity is only one axis of fidelity and may miss functional differences.
- The benchmark depends on the choice and quality of primary references and integration pipeline.
- In this collection, the concept is demonstrated mainly for neural organoids, not yet across many biological systems.

## Sources

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
