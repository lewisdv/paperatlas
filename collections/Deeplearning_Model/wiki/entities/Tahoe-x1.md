# Tahoe-x1

## Type

- Named system / model family

## Definition

- Tahoe-x1, or Tx1, is a family of perturbation-trained single-cell foundation models scaling up to `3` billion parameters and designed for cancer-focused functional genomics.
- The source frames it as a model family that jointly learns gene, cell, and compound representations from very large perturbative transcriptomic corpora.

## Core Architecture

- Derived from a scGPT-style transformer encoder over gene-token sequences.
- Uses discretized expression bins, masking indicators, a global `<cls>` token, and an optional `<drug>` token to inject chemical context.
- Combines a gene-aware decoder and a cell-aware decoder under a masked-expression generative training objective.
- Includes model scales around `70M`, `1B`, and `3B` parameters, with the largest model using `32` transformer layers.

## Data And Training

- Pretrained on up to `266` million single-cell profiles from Tahoe-100M, Arc scBaseCount, and CZ CELLxGENE.
- Tahoe-100M is especially central because it contributes explicit context-perturbation pairs across many cancer cell lines and compounds.
- The paper emphasizes engineering optimizations such as FlashAttention-compatible kernels, mixed precision, efficient data loading, and FSDP for practical scaling.

## Reported Uses

- Predicting broad and context-specific gene essentiality in DepMap-style settings.
- Recovering cancer hallmark pathway structure from learned gene embeddings.
- Supporting cell-type classification from frozen cell embeddings.
- Serving as a latent space for few-shot and zero-shot perturbation-response prediction when paired with the State Transition module.

## Caveats

- The strongest claims are reported in a developer-authored preprint and depend heavily on the Tahoe-100M ecosystem.
- The training corpus is perturbation rich but still concentrated in cancer cell-line experiments rather than full patient biology.
- The current system does not yet integrate broader modalities such as protein or spatial measurements.

## Related

- [Perturbation-Trained Foundation Models](../concepts/perturbation-trained-foundation-models.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Source: Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters](../sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md)
