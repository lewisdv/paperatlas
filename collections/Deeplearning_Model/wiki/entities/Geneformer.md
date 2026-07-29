# Geneformer

## Type

- Named system / single-cell foundation model

## Definition

- Geneformer is a context-aware Transformer pretrained on rank-encoded human single-cell transcriptomes.
- Its primary goal is transfer into network-biology and disease tasks when labelled, task-specific data are scarce.

## Corpus And Representation

- Pretrained on Genecorpus-30M, containing `29.9M` human cells from `561` public datasets.
- Each cell becomes a [Rank-Value Encoding](../concepts/rank-value-encoding.md): genes are ordered by expression normalized to the gene's non-zero median across the pretraining corpus.
- The representation emphasizes genes that distinguish cell state and deemphasizes ubiquitous housekeeping genes.

## Core Architecture

- Six Transformer encoder layers.
- Input length `2,048`, hidden size `256`, four dense attention heads per layer, and feed-forward size `512`.
- Self-supervised pretraining masks `15%` of gene positions and predicts the missing genes from cell context.

## Main Outputs

- Contextual gene embeddings.
- Cell embeddings formed by averaging contextual gene embeddings.
- Contextual attention weights.
- Gene- and cell-classification outputs after task-specific fine-tuning.
- [Embedding-Space In Silico Perturbation](../concepts/embedding-space-in-silico-perturbation.md) by deleting or repositioning genes in the ranked input.

## Reported Uses

- Cell-type annotation.
- Context-dependent dosage-sensitivity prediction.
- Bivalent chromatin-state prediction.
- Identification of central versus peripheral network nodes.
- Cardiomyopathy-state classification and therapeutic-target prioritization.

## Caveats

- Rank encoding trades away quantitative count magnitude.
- Input perturbations are model-space proxies rather than explicit molecular simulations.
- The original paper's strongest mechanistic examples are concentrated in cardiovascular biology.
- Attention enrichment is useful for hypothesis generation but does not by itself establish causal network edges.

## Related

- [Source: Transfer learning enables predictions in network biology](../sources/theodoris_2023_transfer_learning_network_biology_Geneformer.md)
- [Rank-Value Encoding](../concepts/rank-value-encoding.md)
- [Embedding-Space In Silico Perturbation](../concepts/embedding-space-in-silico-perturbation.md)
- [Study Guide: scGPT, scFoundation, Geneformer, and CellFM](../syntheses/scgpt-scfoundation-geneformer-cellfm-study-guide.md)
