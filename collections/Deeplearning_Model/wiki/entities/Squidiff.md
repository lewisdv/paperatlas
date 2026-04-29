# Squidiff

## Type

- Named system / model

## Definition

- Squidiff is a conditional diffusion-model framework for predicting transcriptomic changes under development, perturbation, drug treatment, and environmental stress.
- The source frames it as a general stimulus-response generator that can recover transient intermediate states and support in silico screening.

## Core Architecture

- Combines a semantic encoder that maps cells into a latent semantic space with a conditional DDIM that reconstructs transcriptomes from semantic context plus Gaussian noise.
- Uses latent interpolation for developmental transitions and latent vector addition for perturbation or stimulus effects.
- Extends to unseen drugs through an adaptor using rescaled functional class fingerprints (`rFCFP`).

## Reported Uses

- Predicting iPSC differentiation trajectories and intermediate states.
- Modeling nonadditive gene perturbations and multi-drug responses.
- Generalizing drug-response prediction across cell types and partially unseen treatment regimes.
- Reconstructing blood vessel organoid development, neutron-irradiation responses, and G-CSF-mediated protective programs.

## Caveats

- Training is computationally expensive and slower than lighter generative baselines.
- The latent-direction arithmetic is only approximately linear and may fail in highly complex settings.
- Completely unseen drugs remain difficult without extra molecular-feature adaptors.

## Related

- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [AIVC](../entities/AIVC.md)
- [Source: Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md)
