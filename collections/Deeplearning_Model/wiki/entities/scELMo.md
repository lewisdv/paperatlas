# scELMo

## Type

- Named system / pipeline

## Definition

- scELMo is a single-cell analysis pipeline that uses LLM-generated metadata descriptions and embeddings as reusable biological features.
- Instead of pretraining a large biological model from scratch, it reuses GPT-derived semantic embeddings and optionally fine-tunes a lightweight adaptor.

## Core Architecture

- Generates text descriptions for genes, proteins, or cell metadata with GPT 3.5.
- Extracts embeddings for those descriptions and aggregates them into cell-level representations.
- Supports direct zero-shot usage and a fine-tuning mode with a small adaptor network plus contrastive objectives.
- Can also inject these embeddings into other downstream models such as CINEMA-OT, CPA, and GEARS.

## Reported Uses

- Cell clustering and some batch-effect correction settings.
- Cell-type annotation with either zero-shot kNN or fine-tuned adaptors.
- In-silico treatment analysis through deletion-style embedding shifts.
- Perturbation-analysis enhancement when used as an auxiliary embedding source.

## Caveats

- The method depends on external LLM availability, knowledge coverage, and prompt behavior.
- Zero-shot behavior degrades in strong batch or multi-resource settings.
- Improvements on perturbation tasks are inconsistent across datasets and models.

## Related

- [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md)
- [C2S-Scale](../entities/C2S-Scale.md)
- [Source: scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis](../sources/liu_2023_scelmo_embeddings_from_language_models.md)
