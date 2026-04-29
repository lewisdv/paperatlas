# C2S-Scale

## Type

- Named system / model family

## Definition

- C2S-Scale is a family of large language models for single-cell analysis built on the Cell2Sentence framework.
- The source presents it as a general-purpose biological LLM that jointly models transcriptomic cell profiles, metadata, and natural-language biological context in one token space.

## Core Architecture

- Each cell is serialized as a `cell sentence`, a ranked sequence of gene-name tokens ordered by expression.
- The framework uses standard Transformer LLMs rather than a custom single-cell architecture, allowing it to inherit mainstream LLM scaling patterns.
- Pretraining is multi-task and multimodal, mixing transcriptomic data with annotations, papers, gene sets, and other biological text.
- Task-specific fine-tuning and GRPO-based reinforcement learning adapt the model for annotation, interpretation, perturbation prediction, and biological question answering.

## Reported Uses

- Cell type annotation and embedding of scRNA-seq profiles.
- Natural-language interpretation of cells, clusters, and whole datasets.
- Spatial neighborhood reasoning with multi-cell context and interaction prompts.
- Perturbation response prediction across cytokine, drug, and knockout settings.
- Virtual screening that proposes experimentally testable context-specific hypotheses.

## Caveats

- The source explicitly notes that causal attention over gene order is an imperfect proxy for biological dependency structure.
- Open-ended text outputs remain susceptible to hallucination and require stronger biological guardrails.
- The current paper frames broader epigenomic, proteomic, and clinical integration as future work rather than established capability.

## Related

- [Cell Sentences](../concepts/cell-sentences.md)
- [Source: Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
