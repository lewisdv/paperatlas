# SAVE

## Type

- Named system / model

## Definition

- SAVE expands to "Single-cell Gene Block Attention-based Variational gEnerative framework."
- The source presents SAVE as a unified framework for conditional scRNA-seq generation and integration.

## Core Architecture

- Gene block construction from NCBI Gene summaries using `text-embedding-ada-002` and balanced optimal transport clustering.
- A VAE-like encoder/decoder with Gene Block Attention operating on reshaped gene-block tensors.
- A conditional flow matching network that injects covariates through Adaptive Layer Normalization.
- A condition-masking training strategy intended to improve robustness to unseen condition combinations.

## Reported Performance

- The source reports strong results on conditional generation across single-condition, dual-condition, and more complex multi-condition settings.
- The source also reports competitive or leading performance on batch correction and perturbation prediction benchmarks.

## Limitations

- The system depends on text-derived gene semantics, so its block construction quality is bounded by annotation coverage and literature bias.

## Related

- [Gene Block Attention](../concepts/gene-block-attention.md)
- [Source: SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](../sources/li_2026_save_a_generalizable_framework_for.md)
