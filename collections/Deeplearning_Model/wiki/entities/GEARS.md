# GEARS

## Type

- Named system / model

## Definition

- GEARS, or graph-enhanced gene activation and repression simulator, is a deep-learning model for predicting transcriptional outcomes of single-gene and multigene perturbations.
- The source emphasizes its ability to generalize to combinations containing genes that were never experimentally perturbed during training.

## Core Architecture

- Uses separate embeddings for each gene and for the perturbation of that gene.
- Learns these embeddings through a gene coexpression graph and a Gene Ontology-derived perturbation graph.
- Applies GNN message passing, a cross-gene layer, and gene-specific MLPs to predict post-perturbation expression.
- Outputs an uncertainty score to flag low-confidence predictions when graph support is weak.

## Reported Uses

- Predicting held-out single-gene perturbation outcomes in large Perturb-seq screens.
- Predicting non-additive two-gene interactions such as synergy, redundancy, and epistasis.
- Ranking candidate multigene perturbations for experimental follow-up.
- Generalizing to perturbation sets with one or both genes unseen during training.

## Caveats

- Performance depends on graph connectivity and knowledge quality for the perturbed genes.
- The model is specialized for perturbational transcriptomics rather than broad cross-task biological reasoning.
- It is strong on prioritization and prediction, but not a foundation-model-style reusable representation layer.

## Related

- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [CellOT](../entities/CellOT.md)
- [Source: Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
