# Combinatorial Perturbation Generalization

## Definition

- Combinatorial perturbation generalization is the ability to predict the effect of multigene or multi-intervention combinations that were not directly observed during training.
- In this collection, the hardest case is not only unseen combinations of seen perturbations, but combinations containing genes that were never individually perturbed before.

## In This Collection

- [GEARS](../entities/GEARS.md) is the clearest example: it uses knowledge-graph priors to extrapolate to unseen multigene combinations.
- [Squidiff](../entities/Squidiff.md) tackles a related compositional question through latent-vector arithmetic for gene and drug perturbations.
- [Tahoe-x1](../entities/Tahoe-x1.md) approaches generalization differently, by scaling perturbation-rich pretraining rather than using explicit knowledge-graph structure.
- [CellFM](../entities/CellFM.md) contributes pretrained gene embeddings to GEARS and uses a `20`-gene reverse-perturbation benchmark to rank which one- or two-gene intervention could have produced an observed state.
- Compared with [Neural Optimal Transport](neural-optimal-transport.md), the emphasis here is unseen intervention composition, not learning a minimal-effort map between observed control and treated populations.
- Compared with [Stimulus-Response Diffusion Modeling](stimulus-response-diffusion-modeling.md), the main target is the final transcriptional outcome of new perturbation combinations rather than a smooth generative path through intermediate states.

## Claimed Benefits

- Reduces the experimental burden created by the combinatorial explosion of possible interventions.
- Helps surface synergistic, redundant, epistatic, or otherwise non-additive interactions.
- Supports better prioritization of high-value perturbation screens.

## Caveats

- Generalization quality depends heavily on the structure and completeness of the inductive bias, whether that bias is a knowledge graph, latent arithmetic, or a perturbation-rich corpus.
- Strong predictions for combinations do not remove the need for experimental validation.
- Reverse retrieval and forward response prediction should be separated: identifying a likely intervention is not the same task as reconstructing its full expression response.

## Sources

- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md)
- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
