# Single-Cell Multimodal Integration Regimes

## Definition

- Single-cell multimodal integration methods differ fundamentally in what correspondence exists across datasets.
- `Vertical` integration observes several modalities in the same cells.
- `Horizontal` integration aligns the same modality across sample groups, batches, platforms, or biological contexts.
- `Diagonal` integration has unpaired cells and distinct feature spaces.
- `Mosaic` integration contains a mixture of paired, partially paired, and single-modality blocks.
- Horizontal integration is included for terminological completeness, even though it is usually a batch- or context-alignment problem rather than a cross-modality problem.

## Methods In This Collection

- [MultiVI](../entities/MultiVI.md) learns from paired cells and extends their shared latent space to single-modality cells; it also supports complex mosaic combinations.
- [MIDAS](../entities/MIDAS.md) targets flexible RNA/ATAC/ADT mosaic blocks and explicitly separates biological state from technical noise.
- [scVAEIT](../entities/scVAEIT.md) targets mosaic feature panels and modality blocks by conditioning a VAE on authentic and randomly generated missingness masks.
- [GLUE](../entities/GLUE.md) handles fully unpaired, distinct feature spaces through a regulatory guidance graph.
- [scMODAL](../entities/scMODAL.md) handles unpaired modalities using weakly linked feature pairs to construct cross-modal cell anchors.
- Batch-correction components in MultiVI and MIDAS also address horizontal differences when the same modality is distributed across studies or batches.
- [scMultiMap](../entities/scMultiMap.md) is not an alignment model: it requires paired RNA/ATAC cells to test feature-feature associations.
- [scooby](../entities/scooby.md) is also not primarily an integration model: it consumes a multiomic cell embedding to condition DNA-sequence-to-profile prediction.

## Main Tradeoffs

- More pairing gives stronger supervision but costs more experimentally.
- Prior feature links can orient unpaired spaces, but wrong or missing links introduce dependency on external knowledge.
- Flexible mosaic models can impute missing blocks, but generated modalities are less certain than observations.
- Good batch mixing is insufficient: methods must also preserve cell populations and avoid false cross-modal correspondences.
- Integration geometry specifies the supervision available; it does not specify whether the method should use factorization, probabilistic inference, graphs, kernels, or deep generative learning. See [Multi-Omics Integration Method Taxonomy](multi-omics-integration-method-taxonomy.md).

## Sources

- [MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- [GLUE](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- [MultiVI](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
- [scMODAL](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
- [scMultiMap](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- [scooby](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
- [A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches](../sources/baiao_2025_technical_review_multi-omics_integration_methods.md)
- [scVAEIT](../sources/du_2022_scvaeit_mosaic_integration_imputation.md)
