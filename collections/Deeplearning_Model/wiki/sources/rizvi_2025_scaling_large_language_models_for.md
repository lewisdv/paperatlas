---
title: Scaling Large Language Models for Next-Generation Single-Cell Analysis
kind: paper
status: ingested
added: 2026-04-29T11:03:29+09:00
raw_source: raw/sources/rizvi_2025_scaling_large_language_models_for.pdf
---

# Scaling Large Language Models for Next-Generation Single-Cell Analysis

## Source

- File: [raw/sources/rizvi_2025_scaling_large_language_models_for.pdf](../../raw/sources/rizvi_2025_scaling_large_language_models_for.pdf)
- Added: 2026-04-29T11:03:29+09:00
- Venue/status: 2025 preprint dated 25 October 2025
- Authors: Syed Asad Rizvi, Daniel Levine, Aakash Patel, Shiyang Zhang, Eric Wang, Curtis Jamison Perry, Nicole Mayerli Constante, Sizhuang He, David Zhang, Cerise Tang, Zhuoyang Lyu, Rayyan Darji, Chang Li, Emily Sun, David Jeong, Lawrence Zhao, Jennifer Kwan, David Braun, Brian Hafler, Hattie Chung, Rahul M. Dhodapkar, Paul Jaeger, Bryan Perozzi, Jeffrey Ishizuka, David van Dijk, Shekoofeh Azizi

## Summary

This paper introduces C2S-Scale, a family of large language models for single-cell analysis built on the Cell2Sentence idea of converting transcriptomes into natural-language-like gene sequences. The central argument is that off-the-shelf LLM scaling can be reused for biology if scRNA-seq profiles, metadata, and biological text are all placed into one multimodal token space. Across the source's reported results, larger models, multi-task training, and reinforcement-learning-based refinement support a broad task surface that spans annotation, dataset interpretation, spatial reasoning, perturbation prediction, and experimentally validated virtual screening.

## Methods

- Each cell is transformed into a `cell sentence` by rank-ordering genes by expression and serializing the top genes as a sequence of gene-name tokens.
- C2S-Scale pretrains general-purpose Transformer LLMs on a multimodal corpus of over `50` million human and mouse transcriptomes plus associated metadata, papers, and text, totaling over `1` billion tokens.
- The paper studies scaling from `410` million to `27` billion parameters and trains the models on a mixture of predictive, generative, single-cell, and multi-cell tasks rather than a single downstream objective.
- Downstream fine-tuning covers cell type annotation, dataset interpretation, spatial neighborhood reasoning, and perturbation response prediction; reinforcement learning with GRPO is then used to align outputs to biological objectives such as BioBERTScore or targeted gene programs.
- For generation quality, the paper introduces single-cell Frechet Inception Distance (`scFID`), which scores generated profiles in a foundation-model embedding space rather than only at the individual-gene level.

## Key Claims

- LLM scaling laws transfer to transcriptomic modeling: increasing both model size and dataset size leads to consistent gains across diverse biological tasks.
- Representing transcriptomes as language-like token sequences allows one model family to unify predictive, generative, and natural-language reasoning tasks that are usually split across separate systems.
- Reinforcement-learning-based alignment can make LLM outputs more biologically useful for perturbation prediction and even support experimentally testable discovery workflows.

## Evidence

- Corpus scale: the pretraining corpus contains over `50` million human and mouse transcriptomes and more than `1` billion tokens drawn from transcriptomic data, metadata, and biological text.
- Scaling evidence: the source reports consistent improvements as model size increases from `410M` to `27B` parameters across cell type annotation, dataset interpretation, and conditional generation tasks.
- Cell type annotation: on a diverse immune dataset, C2S-Scale reports `95.43%` accuracy, compared with `93.1%` for scGPT and `94.0%` for Geneformer.
- Natural-language reasoning: on single-cell question answering, the paper reports that C2S-Scale outperforms GPT-4o by `3%` in BERTScore after domain-specific training.
- Perturbation modeling: on the Dong et al. cytokine benchmark, the source reports the best MMD, Wasserstein, and scFID scores among the compared methods and states that C2S-Scale performs best on fully unseen combinatorial perturbations.
- RL gains: GRPO is reported to reduce interferon-related scFID by `16%`; on L1000 apoptosis tasks, it improves Kendall's tau by `9.2%` for the `410M` model and `4.9%` for the `1B` model, while Pearson's `r` improves by `6.6%` and `3.6%`, respectively.
- Experimental validation: the model's virtual screen identified silmitasertib as an interferon-conditional amplifier of antigen presentation, and the paper reports increased MHC-I mean fluorescence intensity in unseen human cell models, including `13.6%` and `34.9%` gains with low-dose IFN-beta in one model and `17.1%` and `28.1%` gains in a second model.

## Limitations

- The supplementary section explicitly notes that autoregressive causal attention imposes a directional ordering over genes that may not reflect true biological dependencies, even if the framework works well empirically.
- The source also states that open-ended natural-language outputs such as abstract generation or cluster captioning remain vulnerable to LLM hallucinations and need stronger biological safeguards.
- The current framework is still centered on transcriptomic plus text-style inputs; the paper presents integration of epigenomic, proteomic, and clinical data as future work rather than a solved capability.
- Some validation successes occur despite sparse training coverage for certain contexts, such as neuroendocrine cells, which suggests generalization but also indicates uneven representation in the corpus.

## Related Pages

- [C2S-Scale](../entities/C2S-Scale.md)
- [Cell Sentences](../concepts/cell-sentences.md)

## Open Questions

- How much of C2S-Scale's advantage comes from converting data into language space versus simply scaling the underlying model size and corpus?
- How robust are open-ended interpretation outputs once the tasks move beyond benchmark settings with strong textual supervision?
- After more perturbation and foundation-model papers are ingested into this collection, where does C2S-Scale sit relative to specialized single-cell generators such as SAVE or retrieval-focused systems such as SCimilarity?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T10:52:58+0900
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/rizvi_2025_scaling_large_language_models_for.pdf -o /tmp/odl-check-rizvi -f markdown --image-output off -q`
- Manifest: [raw/derived/opendataloader/rizvi_2025_scaling_large_language_models_for/opendataloader-run.json](../../raw/derived/opendataloader/rizvi_2025_scaling_large_language_models_for/opendataloader-run.json)
- Output: [raw/derived/opendataloader/rizvi_2025_scaling_large_language_models_for/rizvi_2025_scaling_large_language_models_for.md](../../raw/derived/opendataloader/rizvi_2025_scaling_large_language_models_for/rizvi_2025_scaling_large_language_models_for.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
