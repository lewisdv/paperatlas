# Cell Sentences

## Definition

- Cell sentences are textualized representations of transcriptomes in which genes are ordered by expression rank and emitted as a sequence of gene-name tokens.
- The original [Cell2Sentence](../entities/Cell2Sentence.md) paper introduces this representation as a bridge that lets general-purpose causal LLMs operate on single-cell data without a custom model architecture.

## In Original Cell2Sentence

- Counts are normalized per cell, log-transformed, rank-ordered, and serialized as gene names.
- Exact expression values disappear from the sequence. A dataset-specific linear regression from log-rank to expression approximately maps the sentence back to expression space.
- On the immune-tissue reconstruction analysis, the paper reports `R² = 0.815`; broad UMAP structure is also preserved qualitatively.
- GPT-2 experiments truncate sentences to the top `100` genes, while Pythia-160M can process full sentences with a `9,200`-token maximum input.
- Natural-language prompts can be prepended or appended to support conditional generation, classification, and prose generation in one causal-language-model interface.

## In C2S-Scale

- For each cell, the top expressed genes are rank-ordered and serialized into a token sequence.
- Metadata, papers, and other biological text can then be mixed with these sequences in the same prompt or training corpus.
- The later C2S-Scale paper expands the idea to a much larger corpus and model family, while retaining the same language-native representation.
- The later paper reports `R² = 0.85` for its own rank-to-expression reconstruction setting; this should not be substituted for the original paper's `0.815` result.
- Compared with [Gene Block Attention](gene-block-attention.md), this keeps a flat token stream and borrows language-model ordering rather than grouping genes into semantically balanced modules.
- Compared with [Read-Depth-Aware Pretraining](read-depth-aware-pretraining.md), the emphasis is not on modeling technical count variation explicitly but on translating transcriptomes into a language-native representation.
- Compared with [LLM-Derived Feature Embeddings](llm-derived-feature-embeddings.md), the model trains directly on transcriptome-as-language sequences rather than importing an external semantic embedding space.
- Compared with [Evolutionary Contrastive RNA Pretraining](evolutionary-contrastive-rna-pretraining.md), the sequence here is not the molecular RNA transcript itself but an ordered rendering of whole-cell expression into a token list.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md), this concept opens the door to open-ended generation and natural-language reasoning rather than constraining outputs to atlas neighbors and confidence-aware retrieval.

## Claimed Benefits

- Reuses mainstream LLM infrastructure and scaling behavior for transcriptomic modeling.
- Lets the model connect gene-level patterns with natural-language biological knowledge already present in pretrained LLMs.
- Supports one shared framework for annotation, generation, interpretation, and multi-cell reasoning.

## Caveats

- The ordering is engineered rather than biologically intrinsic, so causal attention may emphasize high-to-low expression dependencies in ways that do not match real mechanisms.
- Rank order discards exact abundance and makes quantitative reconstruction dependent on a fitted dataset-level relationship.
- Generated sentences can contain invalid or duplicated gene names and require postprocessing.
- Better safeguards are still needed when cell-sentence models are asked to produce open-ended biological prose.

## Sources

- [Cell2Sentence: Teaching Large Language Models the Language of Biology](../sources/levine_2024_cell2sentence_teaching_llms_biology.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
