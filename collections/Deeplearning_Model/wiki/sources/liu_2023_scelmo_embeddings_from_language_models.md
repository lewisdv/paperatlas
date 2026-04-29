---
title: scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis
kind: paper
status: ingested
added: 2026-04-29T21:44:46+09:00
raw_source: raw/sources/liu_2023_scelmo_embeddings_from_language_models.pdf
---

# scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis

## Source

- File: [raw/sources/liu_2023_scelmo_embeddings_from_language_models.pdf](../../raw/sources/liu_2023_scelmo_embeddings_from_language_models.pdf)
- Added: 2026-04-29T21:44:46+09:00
- Venue/status: Manuscript-style source; no journal or DOI identified in the extracted text
- Authors: Tianyu Liu, Tianqi Chen, Wangjie Zheng, Xiao Luo, and Hongyu Zhao

## Summary

This paper presents scELMo, a lightweight pipeline that uses large language models to generate text descriptions and embeddings for genes, proteins, or cell metadata, then reuses those embeddings for single-cell analysis under zero-shot or adaptor-based fine-tuning settings. Rather than pretraining a new biological foundation model from scratch, scELMo tries to import biological prior knowledge through GPT-generated metadata embeddings and combine them with sequencing data. In this collection, the paper matters because it offers an alternate route to FM-like behavior: reuse an external LLM's semantic space instead of training a large domain model end to end.

## Methods

- scELMo asks an LLM, mainly GPT 3.5, to summarize feature-level or cell-level metadata, then uses the same model's embedding space to obtain vectors for those descriptions.
- Cell embeddings are formed by aggregating these feature embeddings with observed expression values; the paper contrasts naive arithmetic averaging (`aa`) with expression-weighted averaging (`wa`) and finds `wa` more useful in several zero-shot tasks.
- The zero-shot branch applies these embeddings directly to clustering, batch-effect correction, and simple annotation settings.
- The fine-tuning branch adds a lightweight adaptor network with classification and contrastive-learning objectives so the same embeddings can support harder tasks such as cell-type annotation, in-silico treatment analysis, and perturbation-related prediction.
- The paper also tests scELMo embeddings as additional inputs to other models such as CINEMA-OT, CPA, and GEARS.

## Key Claims

- LLM-derived metadata embeddings can carry biologically useful structure even without pretraining a new domain-specific foundation model.
- Weighted aggregation of feature embeddings can outperform simpler averaging and improve clustering and some batch-correction settings.
- A small fine-tuned adaptor on top of these embeddings can reach performance comparable to heavier pretrained models on some annotation tasks.
- The pipeline is resource-light relative to training large single-cell foundation models from scratch, while still helping on selected perturbation and treatment-analysis tasks.

## Evidence

- The paper compares multiple LLMs for description generation and reports that GPT 3.5 and GPT 4 are the most accurate, with GPT 3.5 selected because it balances accuracy and query time better.
- For repeated prompts on the same gene, the reported embedding correlation is greater than `0.9`, supporting stability of the GPT 3.5-derived embeddings.
- In clustering and proteomic batch-correction tasks, the paper reports that weighted averaging (`wa`) is consistently better than arithmetic averaging (`aa`) and that scELMo embeddings improve over GenePT in the tested clustering settings.
- In cell-type annotation, fine-tuned scELMo with GPT 3.5 embeddings is reported as comparable to models such as scGPT on the tested datasets while clearly outperforming zero-shot scELMo on harder batch-mixed cases like PBMC.
- For perturbation-related downstream tasks, the evidence is mixed but still useful: scELMo embeddings help CPA on some datasets, help GEARS on the Dixit dataset, and can improve CINEMA-OT when combined with cell-type information.

## Limitations

- The pipeline depends on external LLM behavior, and the paper explicitly notes that rapid LLM changes make the long-term contribution of GPT 3.5-specific embeddings unstable.
- It cannot generate meaningful knowledge for genes that are absent or weakly represented in the underlying LLM's training data.
- Zero-shot scELMo is weak when batch effects are large and is explicitly reported as not capable of multi-omic integration under the tested zero-shot framework.
- Not every perturbation task improves uniformly: for GEARS, GPT 3.5 embeddings do not significantly help on the Adamson and Norman datasets, and database-based GenePT embeddings sometimes outperform GPT-derived ones.

## Related Pages

- [scELMo](../entities/scELMo.md)
- [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md)
- [C2S-Scale](../entities/C2S-Scale.md)
- [scGPT](../entities/scGPT.md)

## Open Questions

- When does lightweight LLM-embedding reuse outperform training a biology-specific model from scratch, and when does it saturate?
- Would newer language models change scELMo mostly by improving knowledge coverage, or would the whole aggregation strategy need to change too?
- As this collection grows, should scELMo be treated as a true foundation-model approach or as a metadata-enrichment pipeline that borrows LLM semantics?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:43:47+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/liu_2023_scelmo_embeddings_from_language_models.pdf -o /tmp/odl-check-scelmo -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/liu_2023_scelmo_embeddings_from_language_models/opendataloader-run.json](../../raw/derived/opendataloader/liu_2023_scelmo_embeddings_from_language_models/opendataloader-run.json)
- Output: [raw/derived/opendataloader/liu_2023_scelmo_embeddings_from_language_models/liu_2023_scelmo_embeddings_from_language_models.md](../../raw/derived/opendataloader/liu_2023_scelmo_embeddings_from_language_models/liu_2023_scelmo_embeddings_from_language_models.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->

## Open Questions

- Pending ingest.
