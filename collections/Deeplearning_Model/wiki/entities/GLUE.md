# GLUE

## Type

- Graph-guided unpaired multi-omics integration framework

## Definition

- GLUE (`graph-linked unified embedding`) aligns cells from unpaired omics layers with distinct feature spaces.
- A regulatory guidance graph links modality-specific features and supports both integration and regulatory inference.

## Core Architecture

- One probabilistic VAE per modality.
- Graph VAE over signed cross-modality feature relations.
- Shared cell embeddings aligned with an omics discriminator.
- Cell-feature inner-product decoders and feature-similarity regulatory scores.

## Reported Uses

- Unpaired RNA/ATAC integration.
- RNA/ATAC/DNA-methylation triple-omics integration.
- Peak-gene and TF-target regulatory inference.
- Multi-omics atlas integration over millions of cells.

## Caveats

- Depends on a guidance graph and sufficient cell numbers.
- Whole-dataset regulatory scores may mix context-specific circuits.
- Cross-modal imputation can create artifacts and is not the paper's main validated output.

## Related

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [scMODAL](scMODAL.md)
- [Source: Multi-omics single-cell data integration and regulatory inference with graph-linked embedding](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
