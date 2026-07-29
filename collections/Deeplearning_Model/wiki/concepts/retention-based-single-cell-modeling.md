# Retention-Based Single-Cell Modeling

## Definition

- Retention-based single-cell modeling replaces conventional quadratic self-attention with a retention mechanism designed for parallel training and efficient recurrent or chunkwise inference.
- In this collection, CellFM implements this idea through ERetNet.

## ERetNet In CellFM

- ERetNet processes projected expression and gene-ID embeddings.
- It computes key-value structure before applying queries, giving the paper's claimed linear complexity in the number of gene tokens.
- CellFM replaces RetNet's feed-forward layer with SGLU and its pre-layer normalization with DeepNorm.
- The flagship network stacks `40` ERetNet blocks with `48` heads per block.

## Why It Matters

- Single-cell models often process thousands of genes per cell, making dense attention expensive.
- A more efficient backbone lets the authors scale CellFM to `800M` parameters and `102.3M` training cells.
- This makes architecture efficiency part of the biological-model scaling argument rather than only an implementation detail.

## Caveats

- The CellFM paper changes backbone, corpus size, parameter count, and representation together, so it does not isolate the causal contribution of retention.
- Linear-complexity claims concern the sequence operation, not the total end-to-end cost of data curation, projection, pretraining, or fine-tuning.
- Retention scores are learned model interactions and should not be read automatically as biological regulation.

## Sources

- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
