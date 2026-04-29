# LLM-Derived Feature Embeddings

## Definition

- LLM-derived feature embeddings are vectors obtained by asking a language model to summarize biological entities such as genes or proteins and then embedding those generated descriptions.
- In this collection, the idea is to import semantic biological priors from a general LLM into single-cell analysis without training a new large biological model from scratch.

## In This Collection

- [scELMo](../entities/scELMo.md) is the main example, using GPT 3.5 to generate descriptions and embeddings for genes, proteins, and cell-related metadata.
- Compared with [C2S-Scale](../entities/C2S-Scale.md), which serializes cells into gene-token sentences and trains a large biological LLM directly, scELMo keeps the LLM mostly external and lightweight.
- The paper also contrasts this strategy with GenePT-style embeddings derived from curated text sources such as NCBI.

## Claimed Benefits

- Reuses the semantic knowledge already present in strong language models.
- Avoids the cost of end-to-end pretraining for some downstream tasks.
- Can be plugged into zero-shot pipelines or lightweight task adaptors.

## Caveats

- Embedding quality depends on prompt quality, LLM knowledge coverage, and vendor-specific model behavior.
- The method can degrade when batch structure is complex or when the downstream task needs more than semantic priors alone.
- General LLM embeddings may help some tasks while underperforming curated database embeddings on others.

## Sources

- [scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis](../sources/liu_2023_scelmo_embeddings_from_language_models.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
