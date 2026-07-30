# Post-Imputation Inference

## Definition

- Post-imputation inference asks whether regression coefficients, uncertainty estimates, p-values, and discoveries remain valid after missing values have been predicted.
- It is distinct from imputation accuracy: a model can reconstruct entries well on average while inducing bias or false discoveries in a downstream analysis.

## Failure Of Naive Plugin Analysis

- A Plugin analysis replaces missing or denoised values and then treats the completed matrix as fully observed.
- High-dimensional correlated features can leak true signal into null features during imputation.
- Ignoring imputation error understates uncertainty and can inflate false-discovery rates.
- Optimizing entrywise reconstruction is not always equivalent to estimating the conditional mean needed for a downstream regression.

## Main Responses

- `Complete`: analyze only observed outcomes. This can be valid under suitable missingness assumptions but loses information and power.
- `Multiple imputation`: analyze several plausible completed datasets and combine within- and between-imputation variance, at additional computational and modeling cost.
- `Posterior integration`: test over a model's posterior distribution rather than treating one denoised matrix as fully observed. [totalVI](../entities/totalVI.md) uses posterior log-fold-change distributions and Bayes factors for its differential-expression workflow.
- `Doubly robust correction`: combine an outcome model with an observation-propensity model and add an inverse-propensity-weighted residual correction.

## Augmented Doubly Robust Strategy

- Low-dimensional covariates model the probability that a peptide is observed.
- A flexible model uses those covariates plus the remaining peptide panel to estimate the conditional mean of a missing peptide.
- The corrected pseudo-outcome is consistent when at least one nuisance model is consistent, subject to regularity and overlap assumptions.
- High-dimensional augmentation can improve efficiency when correlated auxiliary peptides reduce residual variance.

## Evaluation

- Calibration: bias, confidence-interval coverage, type-I error, or FDR.
- Efficiency: variance, power, or true-positive rate at controlled error.
- Robustness: sensitivity to missingness mechanism, propensity misspecification, outcome-model quality, and sample splitting.
- Biological plausibility is supporting evidence, not a substitute for calibration.

## Connection To Multimodal Generation

- [scMVP](../entities/scMVP.md), [totalVI](../entities/totalVI.md), [scVAEIT](../entities/scVAEIT.md), [MIDAS](../entities/MIDAS.md), [MultiVI](../entities/MultiVI.md), and [StabMap](../entities/StabMap.md) generate, denoise, or transfer unmeasured molecular features.
- Their imputed outputs should not automatically inherit the inferential status of observed measurements.
- Valid downstream testing may require posterior integration, multiple imputation, doubly robust correction, sample splitting, or task-specific calibration.
- totalVI's posterior testing is more uncertainty-aware than a plug-in matrix, while scMVP's imputation-based differential and CRE analyses illustrate why reconstruction utility and general error calibration remain distinct.

## Sources

- [Augmented Doubly Robust Post-Imputation Inference for Proteomic Data](../sources/moon_2025_augmented_doubly_robust_post-imputation_proteomics.md)
- [Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
- [Joint probabilistic modeling of single-cell multi-omic data with totalVI](../sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
- [A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data](../sources/li_2022_scmvp_multi-view_rna_atac.md)
- [Stabilized mosaic single-cell data integration using unshared features](../sources/ghazanfar_2024_stabmap_mosaic_unshared_features.md)
