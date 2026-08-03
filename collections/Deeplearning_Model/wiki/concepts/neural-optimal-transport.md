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
- Compared with [Fate Decision Intensity](fate-decision-intensity.md), this concept is about moving between observed source and target distributions rather than identifying early commitment hotspots inside one lineage landscape.
- Compared with [Combinatorial Perturbation Generalization](combinatorial-perturbation-generalization.md), the method is stronger on distributional source-target mapping than on extrapolating unseen multigene endpoints through graph priors.

## In CMonge

- [CMonge](../entities/CMonge.md) replaces one-map-per-condition training with a single condition-parameterized map: a source cell and drug/dose context produce a predicted target shift.
- Its objective combines Sinkhorn divergence with a Monge-Gap regularizer, and drug combinations are represented with a set-pooling operation.
- This makes reuse across measured and held-out drug or dose contexts a direct target, while making the quality of chemical or mechanistic context features part of the model assumption.

## Relation to Schrödinger Bridges

- [Schrödinger Bridge Generative Modeling](schrodinger-bridge-generative-modeling.md) is closely related through entropy-regularized transport, but it learns a stochastic path measure relative to a reference process.
- [ARTEMIS](../entities/ARTEMIS.md) uses that dynamic path formulation for time-series snapshots and population-mass change; CellOT and CMonge instead learn source-to-target perturbation transport rules.

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
- [Conditional Monge Gap enables generalizable single-cell perturbation modelling](../sources/driessen_2026_cmonge_generalizable_perturbation.md)
- [ARTEMIS integrates autoencoders and Schrödinger Bridges to predict continuous dynamics](../sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.md)
