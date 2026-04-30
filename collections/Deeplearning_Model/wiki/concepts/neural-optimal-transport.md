# Neural Optimal Transport

## Definition

- In this collection, neural optimal transport refers to learning a perturbation map between unpaired cell-state distributions by parameterizing optimal-transport objectives with neural networks.
- Instead of directly pairing cells across conditions, the method infers how mass should move from a control population to a perturbed population under a minimal-effort principle.

## In CellOT

- CellOT learns a perturbation-specific map `T_k` from `rho_c` to `rho_k`.
- It parameterizes dual potentials `f` and `g` with input convex neural networks.
- The transport map is recovered as `nabla g_k` and then applied to previously unseen control cells.
- For scRNA-seq, the published workflow applies the transport map in an autoencoder latent space.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md), the main question is not whether two profiles are nearest neighbors but whether one population can be plausibly transported into another while preserving heterogeneous response structure.
- Compared with [Cross-modality Generation](cross-modality-generation.md), the model aligns source and target conditions through transport geometry rather than by making multiple modalities interchangeable inside one shared latent representation.

## Claimed Benefits

- Works with unpaired single-cell measurements rather than requiring paired before-and-after observations.
- Preserves heterogeneous response structure better than baselines that mainly capture average shifts.
- Supports out-of-sample and some out-of-distribution perturbation prediction when similar structure exists in the training set.

## Caveats

- The approach depends on the optimal-transport minimal-effort hypothesis and on source-target geometry being similar enough for alignment to remain meaningful.
- Performance drops for strong perturbations, coarse developmental gaps, or settings with unique and sparsely represented responses.
- High-dimensional transcriptomic applications may still rely on auxiliary latent representations for stable modeling.

## Sources

- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
