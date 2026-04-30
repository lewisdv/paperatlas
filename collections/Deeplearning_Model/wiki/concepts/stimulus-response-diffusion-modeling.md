# Stimulus-Response Diffusion Modeling

## Definition

- Stimulus-response diffusion modeling uses conditional diffusion processes to generate transcriptomic states under development, perturbation, drug treatment, or environmental change.
- In this collection, the point is not just denoising for reconstruction but using diffusion to traverse smooth latent transitions between biological conditions.

## In This Collection

- [Squidiff](../entities/Squidiff.md) is the main example, combining semantic latent variables with conditional DDIM generation to predict future, past, and perturbed cell states.
- Compared with [CellOT](../entities/CellOT.md), which models perturbation as transport between distributions, Squidiff emphasizes iterative denoising and latent semantic manipulation.
- The paper also connects naturally to [AIVC](../entities/AIVC.md), because it treats in silico generation of dynamic cell states as a practical ingredient for broader virtual-cell-style experimentation.
- Compared with [RNA Velocity Modules](rna-velocity-modules.md), the transition signal here comes from a generative latent process rather than spliced and unspliced kinetic inference.
- Compared with [Combinatorial Perturbation Generalization](combinatorial-perturbation-generalization.md), Squidiff aims to model smooth paths and intermediate states, not only the final endpoint of unseen perturbation combinations.

## Claimed Benefits

- Better support for smooth transient-state interpolation than many task-specific perturbation models.
- One framework can be reused across differentiation, gene perturbation, drug response, and injury-response settings.
- Can reconstruct missing intermediate states and enable in silico screening from limited measured conditions.

## Caveats

- Diffusion models are computationally expensive and slower to train than lighter generative alternatives.
- Their latent arithmetic may only approximately reflect true biological compositionality.
- Transfer to completely unseen perturbagens can still require extra molecular-feature adaptors.

## Sources

- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md)
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
