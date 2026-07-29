# Sequence-to-Single-Cell Profile Modeling

## Definition

- Sequence-to-single-cell profile models predict molecular readouts from genomic DNA while conditioning on an individual cell or cell state.
- The goal is to connect sequence determinants with cell-specific expression, chromatin accessibility, and variant effects.

## In scooby

- A Borzoi sequence encoder supplies long-context genomic representations.
- LoRA adapts those representations to single-cell RNA and ATAC assays.
- A continuous multiomic cell embedding parameterizes the decoder rather than assigning one output head per cell.
- This design supports predictions for related cells not seen during model training.

## Caveats

- Cell embeddings carry learned biological and technical structure from a separate model.
- Long-range enhancer effects, unseen tissues, and isoform choices remain difficult.
- Motif deletions and variant-effect predictions are hypotheses until experimentally tested.

## Sources

- [scooby: Modeling multi-modal genomic profiles from DNA sequence at single-cell resolution](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
