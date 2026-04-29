# scGPT

## Type

- Named system / model

## Definition

- scGPT is a generative pretrained transformer foundation model for single-cell omics.
- The source presents it as a reusable pretrained model that learns cell and gene representations from atlas-scale scRNA-seq data and is then fine-tuned for downstream tasks.

## Core Architecture

- Inputs combine gene tokens, expression values, and condition tokens such as batch, modality, or perturbation context.
- A specialized attention mask adapts generative transformer training to non-sequential gene-expression inputs.
- The whole-human pretrained model uses `12` transformer blocks, `8` attention heads, and embedding size `512`.
- The workflow follows atlas-scale generative pretraining first, then task-specific fine-tuning for downstream analyses.

## Reported Uses

- Cell type annotation and reference mapping.
- Multi-batch scRNA-seq integration with batch correction.
- Paired and mosaic multi-omic integration across RNA, ATAC, and protein inputs.
- Prediction of unseen perturbation responses and reverse perturbation retrieval.
- Gene program discovery and attention-based gene regulatory interaction analysis.

## Caveats

- The pretraining corpus is centered on normal human scRNA-seq data rather than every disease or perturbation context.
- Strong downstream performance often depends on additional task-specific fine-tuning objectives.
- The language-model framing requires engineered masking and tokenization because gene-expression inputs are not naturally sequential.

## Related

- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Source: scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
