---
title: Augmented Doubly Robust Post-Imputation Inference for Proteomic Data
kind: paper
status: ingested
added: 2026-07-30T13:39:34+09:00
raw_source: raw/sources/moon_2025_augmented_doubly_robust_post-imputation_proteomics.pdf
---

# Augmented Doubly Robust Post-Imputation Inference for Proteomic Data

## Source

- File: [raw/sources/moon_2025_augmented_doubly_robust_post-imputation_proteomics.pdf](../../raw/sources/moon_2025_augmented_doubly_robust_post-imputation_proteomics.pdf)
- Added: 2026-07-30T13:39:34+09:00
- Authors: Haeun Moon, Jin-Hong Du, Jing Lei, and Kathryn Roeder
- Version: arXiv:2403.15802v2, 21 January 2025
- Type: Statistical-methodology preprint
- Keywords stated in source: proteomic data, post-imputation inference, double robustness, variational autoencoder

## Summary

- Missing peptide abundances are often imputed and then analyzed as though they were observed. This `Plugin` workflow can transfer imputation error and cross-peptide confounding into regression coefficients and false discoveries.
- The paper proposes an augmented doubly robust estimator, denoted `DR_UW`, for downstream linear-regression inference.
- A low-dimensional covariate model estimates each peptide's observation propensity, while a flexible outcome model predicts peptide abundance from both low-dimensional covariates and the remaining high-dimensional peptide panel.
- A doubly robust pseudo-outcome corrects the imputed conditional mean with inverse-propensity-weighted observed residuals. The pseudo-outcome is then regressed on the covariates of scientific interest.
- The central target is valid and efficient inference after imputation, not the most accurate reconstruction of every missing entry.

## Statistical Setup

- For peptide outcome `Y`, observation indicator `C`, low-dimensional covariates `W`, and high-dimensional auxiliary peptide data `U`, the method estimates:
  - the observation propensity `δ(W) = P(C = 1 | W)` with a parametric logistic model
  - the augmented outcome regression `ν(W,U) = E[Y | W,U]` with a masking-based VAEIT model
- The pseudo-outcome has the form `ν̂(W,U) + C/δ̂(W) × (Y - ν̂(W,U))`.
- Regressing this pseudo-outcome on `W` transfers the doubly robust correction to the regression coefficients used for peptide-level hypothesis tests.
- Peptide-wise p-values are converted to Benjamini-Hochberg q-values for multiple testing.

## Theoretical Claims

- Theorem 2.2 establishes consistency when either the outcome regression or the propensity model is consistent, subject to the paper's assumptions.
- Theorem 2.3 establishes asymptotic normality when the product of the two nuisance-estimation errors is `oP(n^-1/2)`.
- Under consistent nuisance estimation, the estimator reaches the oracle asymptotic variance even though the outcome model itself need not converge at a parametric rate.
- Theorem 2.4 states that augmenting the outcome model with the high-dimensional peptide panel has asymptotic variance no larger than a doubly robust model using only low-dimensional covariates.
- `Double robustness` does not mean both nuisance models may be wrong. If both are inconsistent or the imputation is extremely poor, the guarantees and efficiency gains can fail.

## Evidence

### Generic Simulations

- Eight procedures are compared: unavailable complete-data `Full`, observed-only `Complete`, MICE, SVD, MissForest, low-dimensional `DR_W`, proposed `DR_UW`, and VAE `Plugin`.
- Simulations use `p = 1,000` peptides, `n = 200` or `500`, 10% signal peptides, MCAR or MAR missingness, Gaussian or skewed outcomes, a realistic peptide covariance matrix, and 200 repetitions.
- Full, Complete, MICE, DR_W, and DR_UW control FDR in the reported settings; the Plugin method inflates FDR because signal-peptide differences bleed into correlated null peptides during imputation.
- DR_UW has the second-highest reported true-positive rate after the unavailable Full method and approaches Full when `n = 500`.
- SVD and MissForest plugin-missing variants can control FDR in some settings but have lower power than Complete and can inflate FDR under stronger signals.

### Single-Cell Proteomics

- The Leduc et al. mass-spectrometry dataset is highly incomplete: 85.6% of peptides have observation rates below 0.5. The main analysis therefore reports sensitivity across observation-rate thresholds.
- At an observation threshold of 0.7, 753 peptides remain for analysis. Realistic simulations on this dataset show that Complete, DR_W, and DR_UW control FDR, while DR_UW improves true-positive rate at stringent cutoffs and Plugin severely inflates FDR.
- For the cell-size association analysis at observation threshold 0.7 and q-value 0.05, DR_UW selects 149 peptides with a mirror rate of 0.13; Complete selects 111 with 0.20, DR_W selects 106 with 0.22, and Plugin selects 303 with 0.26.
- At q-value 0.01, 90% of DR_UW's additional protein-level discoveries overlap proteins found by the more conservative Complete analysis.

### Alzheimer Disease Proteomics

- The bulk analysis contains 220 samples, including 139 dementia cases and 81 controls, and 488 peptides observed in all four studied brain regions at rates between 0.5 and 1.
- At q-value 0.05, Complete selects 55 peptides, DR_W 50, DR_UW 58, and Plugin 79.
- DR_UW identifies seven peptides not selected by Complete; six are connected by the authors to prior Alzheimer-disease or related literature.
- Those literature links support plausibility, not new causal or experimental validation.

## Interpretation

- Reconstruction accuracy and inferential validity are distinct targets. A denoised matrix can look better and still produce biased coefficients or inflated FDR.
- Correlated high-dimensional features can improve an outcome model, but they can also leak signal into null features when imputed values are treated as observations without correction.
- The residual correction uses observed outcomes to remove first-order outcome-model error and gives more weight to residuals from regions with low observation probability.
- An observed-only analysis can be safer but lose substantial power. DR_UW aims to recover information from incomplete samples without accepting the Plugin method's inferential bias.
- This paper supplies a downstream-inference boundary for [Cross-modality Generation](../concepts/cross-modality-generation.md) and [scVAEIT](../entities/scVAEIT.md): generated values are inputs to an analysis, not automatically valid observations.

## Limitations

- The source is a 2025 preprint rather than a final journal article.
- The main missingness arguments rely on MCAR or MAR structures, a correctly estimated propensity or outcome nuisance model, and adequate overlap or positivity.
- For concise theory, nuisance estimates are initially treated as independent of the inference sample. The authors discuss cross-fitting, but their numerical analyses reuse the same data and appeal to regularity rather than implementing the formal split.
- Efficiency depends on informative peptide correlations and a usable imputation model. With completely noisy imputation, DR_UW can make fewer discoveries than Complete.
- Real datasets do not provide ground-truth missing peptide values or true discovery labels; mirror rates, overlap, simulation, and literature support are indirect checks.
- The high-dimensional outcome model is tailored to Gaussian-like peptide abundances and may require modification for other data distributions.

## Related Pages

- [Post-Imputation Inference](../concepts/post-imputation-inference.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Multi-Omics Integration Method Taxonomy](../concepts/multi-omics-integration-method-taxonomy.md)
- [scVAEIT](../entities/scVAEIT.md)

## Open Questions

- How should nuisance-model error be diagnosed when no complete proteomic ground truth exists?
- Does cross-fitting materially change calibration and power in the two real datasets?
- How robust is DR_UW when missingness is genuinely not at random?
- Can downstream targets beyond linear coefficients and peptide-wise multiple testing receive equally practical doubly robust corrections?
- How should uncertainty from a multimodal missing-modality model propagate into cell-type-specific or regulatory analyses?

## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Markdown: [raw/derived/opendataloader/moon_2025_augmented_doubly_robust_post-imputation_proteomics/moon_2025_augmented_doubly_robust_post-imputation_proteomics.md](../../raw/derived/opendataloader/moon_2025_augmented_doubly_robust_post-imputation_proteomics/moon_2025_augmented_doubly_robust_post-imputation_proteomics.md)
- Manifest: [raw/derived/opendataloader/moon_2025_augmented_doubly_robust_post-imputation_proteomics/opendataloader-run.json](../../raw/derived/opendataloader/moon_2025_augmented_doubly_robust_post-imputation_proteomics/opendataloader-run.json)
- Poppler layout text: [raw/derived/pdftext/Moon_2025_ADRPI/Moon_2025_ADRPI.txt](../../raw/derived/pdftext/Moon_2025_ADRPI/Moon_2025_ADRPI.txt)
- These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
