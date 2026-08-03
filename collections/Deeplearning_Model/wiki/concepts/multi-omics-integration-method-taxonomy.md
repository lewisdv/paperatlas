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

## Temporal Update Strategy

- `Offline reintegration` retrains on all data observed so far and serves as a retention upper benchmark, but cumulative cost rises with atlas size.
- `Fixed-model generalization` maps new data through an unchanged reference model, making updates cheap but limiting adaptation to unseen variation.
- `Sequential fine-tuning` adapts parameters on new data but can catastrophically forget earlier batches.
- `Rehearsal-based continual learning` retains a bounded, representative sample of historical data during updates to balance adaptation and retention; [MIRACLE](../entities/MIRACLE.md) is the example in this collection.
- This axis is independent of vertical, horizontal, diagonal, and mosaic geometry. See [Continual Single-Cell Atlas Integration](continual-single-cell-atlas-integration.md).

## Algorithm Families

| Family | Main representation | Typical strengths | Main pressure points |
|---|---|---|---|
| Correlation or covariance | Cross-dataset linear components | Interpretable associations and co-varying modules | Linearity, high dimensionality, matched samples |
| Matrix factorization | Shared and modality-specific low-rank factors | Efficient dimensionality reduction and inspectable factors | Linear assumptions and limited uncertainty modeling |
| Probabilistic or Bayesian | Distributions over shared latent factors | Uncertainty, flexible likelihoods, missing-data handling | Model assumptions, tuning, and computation |
| Multiple-kernel learning | Combined sample-similarity kernels | Nonlinear integration across heterogeneous feature spaces | Kernel and hyperparameter sensitivity |
| Network-based | Fused sample or feature graphs | Topological relations and robustness to some missingness | Similarity metric and graph-construction dependence |
| Reference projection | Low-dimensional reference coordinates predicted from shared features | Fast query mapping and pairwise-overlap chains | Reference dependence, linearity, and accumulated path error |
| Deep generative | Nonlinear latent distributions and decoders | Joint embeddings, denoising, generation, and imputation | Data and compute demand, optimization, interpretability |
| Continual-learning wrapper | An existing integration model plus sequential updating and rehearsal memory | Incremental atlas updates without full reintegration | Forgetting, memory representativeness, update order, and provenance |

## VAE Design Levers

- `Observation model`: Gaussian or reconstruction losses are not universally appropriate; sparse single-cell counts often need count-aware likelihoods. [scMVP](../entities/scMVP.md) uses separate RNA and ATAC likelihoods, while [totalVI](../entities/totalVI.md) adds a foreground/background mixture for protein counts.
- `Latent fusion`: concatenation, mixture of experts, product of experts, or mixtures of products of experts impose different rules for combining modality evidence.
- `Distribution alignment`: KL divergence, maximum mean discrepancy, or adversarial discriminators can align posteriors, conditions, modalities, or batches.
- `Semantic supervision`: task losses, contrastive pairs, cycle consistency, and disentanglement terms shape what the latent space preserves.
- `Missingness`: masking, conditional inference, overlapping reference blocks, omission of absent experts, or omission of unobserved likelihood terms determine how a model handles missing features or modalities. [scVAEIT](../entities/scVAEIT.md) makes masks explicit, whereas totalVI handles absent protein panels through its likelihood and integrated latent space.

## Method-Selection Questions

- Are samples paired, batch-matched, fully unpaired, or connected through overlapping modality blocks?
- Is there one global feature intersection, only a connected chain of pairwise overlaps, or no feature-level bridge at all?
- Is the main output a joint embedding, batch correction, clustering, missing-modality imputation, outcome prediction, or regulatory inference?
- Must uncertainty be explicit?
- Does an assay-specific nuisance process, such as antibody background, need its own probabilistic component?
- How much modality-specific variation must remain visible?
- Is the sample size sufficient for a nonlinear generative model?
- Is an interpretable factor or association more useful than a flexible decoder?
- Are comparisons being made under the same preprocessing, data split, and task-specific metric?
- Will new batches, tissues, features, or modalities arrive over time, and must the resulting atlas retain reproducible representations of its historical data?

## Evidence Boundaries

- Latent-space mixing, reconstruction, downstream classification, and biological interpretation are different success criteria.
- Imputed features remain model estimates.
- Valid inference after imputation is a separate problem from integration or reconstruction; see [Post-Imputation Inference](post-imputation-inference.md).
- Regulatory links inferred from embeddings or cross-modal associations are not automatically causal.
- The review provides a technical taxonomy and qualitative inventory, not a unified head-to-head benchmark.
- A connected dataset topology is not sufficient by itself: bridge size and feature informativeness determine whether multi-hop transfer remains reliable.
- A strong offline score does not establish continual-integration quality: historical retention, memory sampling, and update order must be evaluated separately.

## Sources

- [A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches](../sources/baiao_2025_technical_review_multi-omics_integration_methods.md)
- [Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
- [A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data](../sources/li_2022_scmvp_multi-view_rna_atac.md)
- [Joint probabilistic modeling of single-cell multi-omic data with totalVI](../sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
- [Stabilized mosaic single-cell data integration using unshared features](../sources/ghazanfar_2024_stabmap_mosaic_unshared_features.md)
- [Continual integration of single-cell multimodal data with MIRACLE](../sources/zhou_2026_miracle_continual_multimodal_integration.md)
