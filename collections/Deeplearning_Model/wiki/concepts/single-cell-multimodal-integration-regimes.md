# Single-Cell Multimodal Integration Regimes

## Definition

- Single-cell multimodal integration methods differ fundamentally in what correspondence exists across datasets.
- `Vertical` integration observes several modalities in the same cells.
- `Diagonal` integration has unpaired cells and distinct feature spaces.
- `Mosaic` integration contains a mixture of paired, partially paired, and single-modality blocks.

## Methods In This Collection

- [MultiVI](../entities/MultiVI.md) learns from paired cells and extends their shared latent space to single-modality cells; it also supports complex mosaic combinations.
- [MIDAS](../entities/MIDAS.md) targets flexible RNA/ATAC/ADT mosaic blocks and explicitly separates biological state from technical noise.
- [GLUE](../entities/GLUE.md) handles fully unpaired, distinct feature spaces through a regulatory guidance graph.
- [scMODAL](../entities/scMODAL.md) handles unpaired modalities using weakly linked feature pairs to construct cross-modal cell anchors.
- [scMultiMap](../entities/scMultiMap.md) is not an alignment model: it requires paired RNA/ATAC cells to test feature-feature associations.
- [scooby](../entities/scooby.md) is also not primarily an integration model: it consumes a multiomic cell embedding to condition DNA-sequence-to-profile prediction.

## Main Tradeoffs

- More pairing gives stronger supervision but costs more experimentally.
- Prior feature links can orient unpaired spaces, but wrong or missing links introduce dependency on external knowledge.
- Flexible mosaic models can impute missing blocks, but generated modalities are less certain than observations.
- Good batch mixing is insufficient: methods must also preserve cell populations and avoid false cross-modal correspondences.

## Sources

- [MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- [GLUE](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- [MultiVI](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
- [scMODAL](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
- [scMultiMap](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- [scooby](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
