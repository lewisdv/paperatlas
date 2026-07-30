# Cross-modality Generation

## Definition

- Cross-modality generation is the task of reconstructing unmeasured biological or phenotypic modalities from observed inputs by using a shared latent representation.
- In this collection, the task now spans broad human-health measurements and single-cell RNA, chromatin-accessibility, and protein observations.

## In AURORA

- Seven modalities are aligned into a common latent space across fragmented and partially paired datasets.
- Missing modalities are decoded from the shared embedding, allowing one measured modality to stand in for others.
- The generated outputs are then reused for downstream tasks such as aging clocks, disease prediction, and perturbation simulation.
- Compared with [Multimodal Foundation Models](multimodal-foundation-models.md), this is a narrower operational function inside a broader multimodal paradigm: the focus is specifically reconstructing missing modalities rather than defining the whole pretraining agenda.
- Compared with [Multi-Omic Developmental Atlases](multi-omic-developmental-atlases.md), the goal here is generation from partial observations, not building a reference substrate for developmental mapping and benchmarking.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md), similarity here means cross-modal equivalence in one latent space rather than nearest-neighbour retrieval over a reference atlas.
- Compared with [Neural Optimal Transport](neural-optimal-transport.md), the objective is modality completion from shared embeddings rather than learning a minimal-effort map between source and target state distributions.

## In Single-Cell Multi-Omics

- [MultiVI](../entities/MultiVI.md) uses paired multiome cells as the anchor for integrating single-modality cells, then samples its posterior to impute missing RNA, ATAC, or protein features and quantify uncertainty.
- [MIDAS](../entities/MIDAS.md) targets flexible mosaic datasets in which batches contain different subsets of RNA, ATAC, and ADT; missing-block generation is coupled to batch correction and biological/technical latent disentanglement.
- [scVAEIT](../entities/scVAEIT.md) encodes authentic missingness patterns and applies new random masks during training so it learns conditional distributions of absent features or modalities from complementary observed measurements.
- [scMODAL](../entities/scMODAL.md) addresses unpaired modalities by using known cross-modal feature links to construct cell anchors, then performs feature imputation through its aligned latent spaces and decoders.
- These methods therefore solve related but non-equivalent problems: paired-reference completion, mask-conditioned or disentangled mosaic completion, and feature-link-guided unpaired completion.
- See [Single-Cell Multimodal Integration Regimes](single-cell-multimodal-integration-regimes.md) for the supervision assumptions behind those differences.

## Claimed Benefits

- Reduces the impact of missing modalities and batch fragmentation.
- Expands effective training coverage for downstream predictors.
- Makes it possible to derive multimodal risk estimates from simpler inputs such as routine blood tests or facial imaging.

## Caveats

- The source explicitly says that flawless molecular reconstruction from limited unimodal inputs is still aspirational.
- AURORA and MultiVI depend strongly on paired multimodal ground truth; MIDAS can exploit partially paired mosaic blocks; scMODAL substitutes known feature links and inferred anchors for direct cell pairing.
- Generated modalities are posterior or decoder estimates, not replacement measurements. Their utility must be checked separately for reconstruction, downstream prediction, and biological interpretation.
- Alignment quality does not by itself prove that an individual imputed feature is correct.
- Good imputation metrics do not guarantee calibrated coefficients, p-values, or false-discovery rates. See [Post-Imputation Inference](post-imputation-inference.md).

## Sources

- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
- [MultiVI: deep generative model for the integration of multimodal data](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
- [Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- [scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
- [Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
- [Augmented Doubly Robust Post-Imputation Inference for Proteomic Data](../sources/moon_2025_augmented_doubly_robust_post-imputation_proteomics.md)
