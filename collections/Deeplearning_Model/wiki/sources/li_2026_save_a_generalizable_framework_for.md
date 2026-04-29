---
title: SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention
kind: paper
status: ingested
added: 2026-04-29T10:07:55+09:00
raw_source: raw/sources/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.pdf
---

# SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention

## Source

- File: [raw/sources/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.pdf](../../raw/sources/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.pdf)
- Added: 2026-04-29T10:07:55+09:00
- Venue/status: ICLR 2026 conference paper; arXiv:2604.16776v1
- Authors: Jiahao Li, Jiayi Dong, Peng Ye, Xiaochi Zhou, Haohai Lu, Fei Wang
- Code: [fdu-wangfeilab/sc-save](https://github.com/fdu-wangfeilab/sc-save)

## Summary

SAVE is a conditional generative framework for scRNA-seq data that combines semantically constructed gene blocks, a VAE-style latent compression module, and conditional flow matching. The paper positions the method as a response to flat gene-token modeling: instead of attending over individual genes, SAVE groups genes into balanced semantically similar blocks, applies attention over those blocks, and injects condition information through Adaptive Layer Normalization. Across the paper's reported benchmarks, SAVE is presented as a strong model for multi-condition generation, batch correction, and perturbation prediction.

## Methods

- Gene block construction: the model cleans NCBI Gene summary text, embeds each gene description with `text-embedding-ada-002`, and clusters the embeddings into equal-sized, non-overlapping blocks via an iterative optimal transport procedure.
- Gene Block Attention VAE: the reshaped expression tensor is encoded and reconstructed with Transformer blocks operating at the gene-block level rather than the single-gene token level.
- Conditional flow matching: the latent representation is generated from noise with a conditional flow matching network that uses Adaptive Layer Normalization to inject covariates such as batch, cell type, disease state, or perturbation context.
- Condition masking: training randomly masks condition values with a dedicated `[MASK]` token so the model can better generalize to missing or unseen condition combinations.

## Key Claims

- SAVE argues that gene-block-level attention captures higher-order biological relationships more effectively than flat gene-token modeling.
- The model claims strong extrapolation to unseen condition combinations by combining condition masking with conditional flow matching.
- The paper reports that SAVE outperforms several baselines on generation fidelity, batch correction, and perturbation prediction benchmarks.

## Evidence

- Single-condition generation: on Dentate gyrus and Tabula Muris, the paper reports substantially lower MMD than baseline models, with especially large gains on Dentate gyrus.
- Dual-condition generation: on Heart, PBMC, and Lung Atlas, SAVE is reported as the best method in Table 2, with WD/MMD values of `8.30/0.63`, `5.37/0.29`, and `4.37/1.14`, respectively.
- Unseen multi-condition generation: on the Lung Cancer benchmark, SAVE is reported to have the best unseen-condition WD (`4.63 +/- 0.95`) while scDiffusion has a slightly lower unseen MMD.
- Batch correction: Table 4 reports the top scIB score on Lung Atlas (`0.81`) and PBMC (`0.83`), and competitive performance on Heart (`0.80`).
- Perturbation prediction: on PBMC-IFN, SAVE reports average PCC `0.96` and average `R2` `0.86`, exceeding the paper's baseline averages.

## Limitations

- The source explicitly notes that gene-block construction depends on the coverage and quality of existing literature and database annotations.
- The source also notes that text-driven grouping can inherit historical literature bias and may be less reliable for poorly characterized or newly discovered genes.

## Related Pages

- [SAVE](../entities/SAVE.md)
- [Gene Block Attention](../concepts/gene-block-attention.md)

## Open Questions

- How sensitive are the reported gains to the choice of text embedding model used for gene summaries?
- How much of the improvement comes from gene block construction versus the latent flow matching backbone?
- After more sources are ingested into this collection, how will SAVE compare to other single-cell foundation or perturbation models already present in `raw/sources/`?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T10:12:03+09:00
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.pdf -o raw/derived/opendataloader/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention -f markdown --image-output off -q`
- Manifest: [raw/derived/opendataloader/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention/opendataloader-run.json](../../raw/derived/opendataloader/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention/opendataloader-run.json)
- Output: [raw/derived/opendataloader/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.md](../../raw/derived/opendataloader/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention/SAVE A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
