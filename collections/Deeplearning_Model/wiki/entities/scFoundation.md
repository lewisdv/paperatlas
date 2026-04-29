# scFoundation

## Type

- Named system / model

## Definition

- scFoundation, also called xTrimoScFoundation alpha, is a large pretrained foundation model for single-cell transcriptomics.
- The source presents it as a scale-focused, read-depth-aware foundation layer whose embeddings can be reused across many downstream tasks with little or no full-model fine-tuning.

## Core Architecture

- The model uses an asymmetric encoder-decoder transformer-like architecture over `19,264` genes.
- Pretraining relies on read-depth-aware modeling with source and target count indicators `S` and `T`.
- The main published model has about `100` million parameters and is pretrained on over `50` million human scRNA-seq profiles.
- Downstream tasks consume either pooled cell embeddings or gene-context embeddings from the pretrained model.

## Reported Uses

- Read-depth enhancement and clustering.
- Bulk and single-cell drug response prediction.
- Single-cell perturbation response modeling.
- Cell type annotation.
- Gene module and gene regulatory network inference.

## Caveats

- The current paper is transcriptomics-only rather than fully multimodal.
- Computational cost is explicitly identified by the authors as a limitation.
- Read-depth-aware pretraining helps with one important technical confounder but does not solve every batch or modality effect.

## Related

- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)
- [Source: Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
