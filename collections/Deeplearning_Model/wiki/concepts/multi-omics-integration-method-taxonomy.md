# Multi-Omics Integration Method Taxonomy

## Definition

- Multi-omics integration methods should be classified along two orthogonal axes:
  - `data geometry`: which sample and modality correspondences are observed
  - `algorithm family`: which mathematical representation and assumptions are used
- Keeping these axes separate prevents labels such as `mosaic`, `VAE`, and `multimodal` from being treated as interchangeable.

## Data Geometry

- `Vertical`: several modalities measured in the same samples.
- `Horizontal`: one modality aligned across sample groups, batches, or platforms.
- `Diagonal`: distinct modalities measured in unpaired sample groups.
- `Mosaic`: partially overlapping modality blocks connect otherwise incomplete datasets.
- See [Single-Cell Multimodal Integration Regimes](single-cell-multimodal-integration-regimes.md) for method-level examples in this collection.

## Algorithm Families

| Family | Main representation | Typical strengths | Main pressure points |
|---|---|---|---|
| Correlation or covariance | Cross-dataset linear components | Interpretable associations and co-varying modules | Linearity, high dimensionality, matched samples |
| Matrix factorization | Shared and modality-specific low-rank factors | Efficient dimensionality reduction and inspectable factors | Linear assumptions and limited uncertainty modeling |
| Probabilistic or Bayesian | Distributions over shared latent factors | Uncertainty, flexible likelihoods, missing-data handling | Model assumptions, tuning, and computation |
| Multiple-kernel learning | Combined sample-similarity kernels | Nonlinear integration across heterogeneous feature spaces | Kernel and hyperparameter sensitivity |
| Network-based | Fused sample or feature graphs | Topological relations and robustness to some missingness | Similarity metric and graph-construction dependence |
| Deep generative | Nonlinear latent distributions and decoders | Joint embeddings, denoising, generation, and imputation | Data and compute demand, optimization, interpretability |

## VAE Design Levers

- `Observation model`: Gaussian or reconstruction losses are not universally appropriate; sparse single-cell counts often need count-aware likelihoods.
- `Latent fusion`: concatenation, mixture of experts, product of experts, or mixtures of products of experts impose different rules for combining modality evidence.
- `Distribution alignment`: KL divergence, maximum mean discrepancy, or adversarial discriminators can align posteriors, conditions, modalities, or batches.
- `Semantic supervision`: task losses, contrastive pairs, cycle consistency, and disentanglement terms shape what the latent space preserves.
- `Missingness`: masking, conditional inference, overlapping reference blocks, or omission of absent experts determine how a model handles missing features or modalities. [scVAEIT](../entities/scVAEIT.md) makes the authentic and randomly generated masks explicit model inputs.

## Method-Selection Questions

- Are samples paired, batch-matched, fully unpaired, or connected through overlapping modality blocks?
- Is the main output a joint embedding, batch correction, clustering, missing-modality imputation, outcome prediction, or regulatory inference?
- Must uncertainty be explicit?
- How much modality-specific variation must remain visible?
- Is the sample size sufficient for a nonlinear generative model?
- Is an interpretable factor or association more useful than a flexible decoder?
- Are comparisons being made under the same preprocessing, data split, and task-specific metric?

## Evidence Boundaries

- Latent-space mixing, reconstruction, downstream classification, and biological interpretation are different success criteria.
- Imputed features remain model estimates.
- Valid inference after imputation is a separate problem from integration or reconstruction; see [Post-Imputation Inference](post-imputation-inference.md).
- Regulatory links inferred from embeddings or cross-modal associations are not automatically causal.
- The review provides a technical taxonomy and qualitative inventory, not a unified head-to-head benchmark.

## Sources

- [A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches](../sources/baiao_2025_technical_review_multi-omics_integration_methods.md)
- [Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
