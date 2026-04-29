# Cell Sentences

## Definition

- Cell sentences are textualized representations of transcriptomes in which genes are ordered by expression rank and emitted as a sequence of gene-name tokens.
- In this collection, the C2S-Scale paper uses them as the bridge that lets general-purpose LLMs operate directly on single-cell data without a custom tokenizer or architecture.

## In C2S-Scale

- For each cell, the top expressed genes are rank-ordered and serialized into a token sequence.
- Metadata, papers, and other biological text can then be mixed with these sequences in the same prompt or training corpus.
- The paper reports that the relationship between expression rank and original normalized expression remains strong enough that a fitted linear model can recover expression with `R2 = 0.85`.

## Claimed Benefits

- Reuses mainstream LLM infrastructure and scaling behavior for transcriptomic modeling.
- Lets the model connect gene-level patterns with natural-language biological knowledge already present in pretrained LLMs.
- Supports one shared framework for annotation, generation, interpretation, and multi-cell reasoning.

## Caveats

- The ordering is engineered rather than biologically intrinsic, so causal attention may emphasize high-to-low expression dependencies in ways that do not match real mechanisms.
- Better safeguards are still needed when cell-sentence models are asked to produce open-ended biological prose.

## Sources

- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
