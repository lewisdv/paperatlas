# GPerturb

## Type

- Named system / model

## Definition

- GPerturb is a sparse additive perturbation-regression model that uses hierarchical Bayesian modeling and Gaussian processes to estimate gene-level perturbation effects from single-cell perturbation data.
- The source emphasizes that it supports both continuous transformed inputs and count-based inputs while exposing uncertainty estimates and interpretable sparse effects.

## Core Architecture

- Decomposes observed expression into a basal cell-state component and an additive perturbation-effect component.
- Models both components with feature-specific Gaussian processes rather than neural latent embeddings.
- Uses sparsity switches to determine which perturbations affect which genes.
- Supports both Gaussian and zero-inflated Poisson observation models and can analyze dosage-response derivatives.

## Reported Uses

- Predicting single-gene and multigene perturbation outcomes from Perturb-seq-style data.
- Modeling dosage-sensitive perturbation responses, including non-monotonic dose-response curves.
- Serving as a non-deep-learning benchmark for comparison against CPA, GEARS, SAMS-VAE, and foundation-model-based perturbation methods.
- Identifying interpretable gene-perturbation dependencies at the gene level rather than only in a latent embedding space.

## Caveats

- Inferred perturbation effects can shift materially depending on preprocessing and on whether Gaussian or ZIP observation models are used.
- The model is competitive on perturbation prediction, but it is not framed here as a general-purpose foundation representation for many downstream tasks.
- Direct comparisons against other methods can be awkward because competing tools often assume different data formats, perturbation encodings, or internal normalizations.

## Related

- [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [GEARS](../entities/GEARS.md)
- [CellOT](../entities/CellOT.md)
- [Source: GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md)
