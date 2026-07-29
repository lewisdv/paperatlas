# scooby

## Type

- Cell-conditioned sequence-to-function model

## Definition

- scooby predicts scRNA-seq coverage and scATAC-seq insertion profiles from genomic sequence at single-cell resolution.
- It adapts Borzoi with LoRA and conditions a lightweight profile decoder on a continuous cell-state embedding.

## Core Architecture

- Pretrained Borzoi sequence encoder over approximately half a megabase.
- LoRA adaptation to the target single-cell assay.
- Poisson-MultiVI cell embeddings.
- Cell-conditioned convolutional decoder for RNA and ATAC profiles.

## Reported Uses

- Held-out gene, genomic-region, and cell-state prediction.
- In silico TF motif deletion and target-gene prioritization.
- Bulk eQTL effect prediction and single-cell decomposition.
- Connecting variant effects to accessibility, expression, and candidate TF motifs.

## Caveats

- Evidence comes from one hematopoietic dataset and a 2024 preprint.
- Training is computationally intensive.
- Distal regulation and isoform-specific prediction remain weak.
- Interpretations are in silico hypotheses.

## Related

- [Sequence-to-Single-Cell Profile Modeling](../concepts/sequence-to-single-cell-profile-modeling.md)
- [MultiVI](MultiVI.md)
- [scMultiMap](scMultiMap.md)
- [Source: scooby](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
