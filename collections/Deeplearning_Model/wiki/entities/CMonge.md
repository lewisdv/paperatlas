# CMonge

## Type

- Conditional neural optimal-transport model for single-cell perturbation response prediction

## Definition

- CMonge means Conditional Monge Gap.
- It learns a condition-parameterized map from a source-cell distribution to a treated-cell distribution using unpaired observations, with drug, dose, and optionally drug-combination context as inputs.

## Core Components

- Source-cell and condition encoders feed an MLP that predicts a target-cell shift.
- Drug context can use RDKit features from SMILES strings or a mechanism-of-action representation; dose is encoded separately.
- A DeepSets-style pooling operation represents multi-drug contexts.
- Sinkhorn divergence matches the predicted and observed target distributions, while a Monge-Gap term promotes cost-optimal transport.

## Reported Uses

- In-sample and held-out drug/dose response prediction in the multi-cell-line sci-Plex screen.
- Multi-drug condition modeling.
- Generalization experiments on single-cell transcriptomic and multiplexed `4i` protein-imaging perturbation data.

## Caveats

- A global conditional map trades condition-specific flexibility for reuse across contexts; its transfer quality depends on context representation and training coverage.
- Distribution-level target matching does not create a ground-truth paired target for each individual source cell.
- The paper's drug-screen evaluations do not establish equivalent generalization to multigene perturbations, novel cell types, or arbitrary mechanisms.

## Related

- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [CellOT](CellOT.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [Source: Conditional Monge Gap enables generalizable single-cell perturbation modelling](../sources/driessen_2026_cmonge_generalizable_perturbation.md)
