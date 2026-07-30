# Masked Conditional Multimodal Imputation

## Definition

- Masked conditional multimodal imputation trains a model to predict selected features or modalities from the complementary observed measurements.
- The missingness mask is part of the model input, so structural absence is distinguished from a measured biological zero.

## In scVAEIT

- Each cell has an `authentic mask` describing the measurements actually absent from its source dataset.
- Additional random masks are generated during every optimization step.
- The encoder estimates a latent posterior from the unmasked data and mask embedding.
- The decoder predicts the masked values under modality-matched likelihoods.
- Random masking supplies supervised conditional-prediction targets and regularizes the model against memorizing only easy features.

## Why It Matters

- Mosaic datasets may omit complete modalities, partial feature panels, or different feature subsets in different studies.
- Zero-filling without explicit masking can confuse structural absence with real zero abundance.
- A mask-conditioned model can reuse one trained reference across several incomplete query designs.

## Contrast With Other Missing-Panel Strategies

- [totalVI](../entities/totalVI.md) substitutes zeros for absent protein inputs, omits their likelihood terms during training, and predicts them through a batch-integrated latent space.
- [scVAEIT](../entities/scVAEIT.md) instead encodes the missingness pattern itself and adds random training masks.
- These strategies are not interchangeable: omission prevents an absent target from contributing to the likelihood, whereas explicit mask conditioning also tells the model which measurements are structurally absent.

## Design Choices

- Mask distribution: independent feature dropout, complete modality dropout, authentic structural masks, or prior-informed masks.
- Observation model: count-aware RNA or protein likelihoods and binary accessibility likelihoods.
- Objective balance: missing-feature prediction versus reconstruction or denoising of observed values.
- Transfer scope: unseen cells from the same population versus shifted tissues, protocols, or feature panels.

## Evidence Boundaries

- Artificial masking provides known ground truth but may not reproduce real missingness mechanisms.
- Reconstruction and correlation metrics do not prove valid downstream coefficients, p-values, or biological mechanisms.
- More aggressive masking can improve robustness but remove too much conditioning information.
- See [Post-Imputation Inference](post-imputation-inference.md) for the distinction between producing an estimate and performing valid inference with it.

## Sources

- [Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
- [Joint probabilistic modeling of single-cell multi-omic data with totalVI](../sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
