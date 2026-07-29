# Rank-Value Encoding

## Definition

- Rank-value encoding converts a cell's expressed genes into an ordered token sequence.
- In Geneformer, each gene's expression is divided by its non-zero median expression across Genecorpus-30M, and genes are ranked within the cell by that normalized value.

## Biological Prior

- Ubiquitously abundant housekeeping genes are pushed down because their expression is not unusual relative to the corpus.
- Lowly expressed transcription factors can move upward when their expression is unusually informative in a particular cell.
- The ordering therefore encodes `state distinctiveness` rather than raw abundance alone.

## Claimed Benefits

- Produces a non-parametric input representation.
- Can be more stable than absolute counts under technical variation that preserves within-cell order.
- Creates a gene-token sequence compatible with masked-token Transformer pretraining.
- Allows simple in silico deletion or activation by removing or repositioning gene tokens.

## Tradeoffs

- Exact expression magnitudes are discarded.
- The normalization factors depend on the composition and quality of the pretraining corpus.
- Relative order is a useful model input, but it is not a temporal or causal gene sequence.
- Moving a gene to the front of the sequence is only a proxy for activation.

## Comparison

- [Geneformer](../entities/Geneformer.md) is the clearest rank-value model in this collection.
- [scGPT](../entities/scGPT.md) retains gene tokens but adds expression-value and condition representations rather than relying only on rank.
- [CellFM](../entities/CellFM.md) and [scFoundation](../entities/scFoundation.md) stay closer to quantitative expression through value projection and reconstruction.
- [Cell Sentences](cell-sentences.md) also serialize transcriptomes, but their purpose is more language-native multimodal reasoning than Geneformer's corpus-normalized network transfer.

## Sources

- [Transfer learning enables predictions in network biology](../sources/theodoris_2023_transfer_learning_network_biology_Geneformer.md)
- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
