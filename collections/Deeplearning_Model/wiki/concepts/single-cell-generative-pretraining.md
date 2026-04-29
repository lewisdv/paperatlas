# Single-Cell Generative Pretraining

## Definition

- Single-cell generative pretraining is the strategy of training a large generative model on broad cell-atlas data first, then adapting the pretrained representation to many downstream single-cell tasks.
- In this collection, scGPT makes this pattern explicit for transformer models on atlas-scale scRNA-seq data, and C2S-Scale extends a related idea into multimodal LLM training over transcriptomic and textual corpora.

## In scGPT

- The model is pretrained on over `33` million normal human cells before task-specific fine-tuning.
- Pretraining is designed to jointly learn cell and gene representations that can later support annotation, integration, perturbation modeling, and gene-network analysis.
- The paper explicitly argues for a `pretraining universally, fine-tuning on demand` workflow.

## In C2S-Scale

- The same broad pattern reappears in an LLM setting: a large base model is pretrained on over `50` million transcriptomes plus associated text, then adapted to interpretation and perturbation tasks.
- Compared with scGPT, the representation is more language-native because transcriptomes are serialized into cell sentences.

## Claimed Benefits

- Reuses one pretrained model across many downstream tasks instead of building separate models from scratch.
- Improves as atlas size and corpus scale increase.
- Encourages representations that may transfer to unseen datasets, perturbations, and modalities better than task-isolated training.

## Caveats

- Downstream success still depends heavily on the fine-tuning objective and evaluation setup.
- Input tokenization and masking strategies are engineered abstractions over biology rather than direct mechanistic models.
- Comparing different pretrained model families can be difficult because they may differ in corpus, architecture, task mix, and downstream supervision all at once.

## Sources

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
