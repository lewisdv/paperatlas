---
title: scGPT: toward building a foundation model for single-cell multi-omics using generative AI
kind: paper
status: ingested
added: 2026-04-29T11:17:30+09:00
raw_source: raw/sources/cui_2024_scgpt_toward_building_a_foundation.pdf
---

# scGPT: toward building a foundation model for single-cell multi-omics using generative AI

## Source

- File: [raw/sources/cui_2024_scgpt_toward_building_a_foundation.pdf](../../raw/sources/cui_2024_scgpt_toward_building_a_foundation.pdf)
- Added: 2026-04-29T11:17:30+09:00
- Venue/status: Nature Methods article; published online 26 February 2024
- Authors: Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, Bo Wang
- DOI: `10.1038/s41592-024-02201-0`
- Code: [bowang-lab/scGPT](https://github.com/bowang-lab/scGPT)

## Summary

This paper presents scGPT, a generative pretrained transformer for single-cell biology that is trained on a very large atlas of normal human scRNA-seq data and then adapted to multiple downstream tasks. The model treats genes as transformer tokens, adds expression values and condition tokens, and uses a specialized attention mask to make autoregressive-style generative pretraining work on non-sequential omics data. The paper positions scGPT as a generalist foundation model whose pretrained cell and gene representations can support annotation, batch correction, multi-omic integration, perturbation prediction, and gene-regulatory analysis.

## Methods

- scGPT uses gene tokens, expression values, and condition tokens such as modality, batch, or perturbation context as its core input representation.
- The pretrained whole-human model uses `12` transformer blocks with `8` attention heads, embedding size `512`, and a specialized attention mask to adapt generative pretraining to non-sequential gene-expression inputs.
- Pretraining uses over `33` million normal human cells from CELLxGENE, spanning `51` organs or tissues and `441` studies.
- The workflow follows two stages: atlas-scale self-supervised generative pretraining, then task-specific fine-tuning for cell type annotation, perturbation prediction, scRNA-seq integration, scMultiomic integration, and gene regulatory network inference.
- For scRNA-seq integration, fine-tuning combines masked gene-expression recovery with objectives such as ECS, reverse-backpropagation domain adaptation, and domain-specific normalization to encourage biological conservation plus batch correction.

## Key Claims

- A single generatively pretrained transformer can serve as a reusable single-cell foundation model across many downstream tasks instead of requiring separate specialized architectures.
- Larger pretraining datasets improve the quality of pretrained embeddings and downstream fine-tuning performance, supporting a scaling-style foundation-model view of single-cell omics.
- Pretrained gene and cell representations can encode biologically meaningful structure beyond task labels, including batch-robust cell states, perturbation effects, and context-specific gene interactions.

## Evidence

- Pretraining scale: the whole-human model is trained on `33` million normal human cells from `51` tissues and `441` studies, and the paper shows coherent cell-type organization when visualizing embeddings from a `10%` sample.
- Cell type annotation: on pancreas, scGPT reports precision above `0.8` for most cell types; on the MS dataset it reports accuracy around `0.85`; across pancreas, MS, and tumor-infiltrating myeloid benchmarks it consistently outperforms TOSICA and scBERT on accuracy, precision, recall, and macro F1.
- Perturbation prediction: across Adamson, Replogle, and Norman Perturb-seq benchmarks, the source states that scGPT achieves the highest scores among the compared methods and outperforms GEARS and a linear baseline by roughly `5-20%`, especially on post-perturbation change metrics.
- Reverse perturbation retrieval: on a `20`-gene Norman subset with `210` possible one- or two-gene perturbation combinations, scGPT reports `91.4%` relevant top-1 retrievals and `65.7%` correct top-8 retrievals, far better than random trial-and-error over `105.5` expected attempts on average.
- Multi-batch integration: on PBMC 10k, scGPT reports `AvgBIO = 0.821`, described as `5-10%` higher than the compared methods while still separating all cell types.
- Multi-omic integration: on paired RNA-protein BMMC data with about `90,000` cells, `12` donors, and `48` cell types, the paper reports a `9%` AvgBIO improvement over Seurat; on the ASAP PBMC mosaic benchmark it reports stronger batch correction than scMoMat, including `AvgBATCH = 0.951` versus `0.916`.
- Gene-network evidence: for attention-based interaction analysis, the top `20` DDIT3-influenced genes all match ChIP-Atlas targets, and `19` of the top `20` BHLHE40-influenced genes also validate; scGPT also identifies `22` Reactome pathways not recovered by the coexpression baseline, `14` of them immune-related.

## Limitations

- The pretraining corpus is restricted to normal human scRNA-seq data, so disease, perturbation, or multimodal scenarios still rely on downstream fine-tuning rather than being fully solved in zero-shot form.
- The source has to introduce a specially designed attention mask because gene-expression profiles are not naturally sequential data, which means the language-model analogy remains engineered rather than native.
- Many of the strongest downstream claims depend on task-specific objectives and adapters, so the pretrained model alone is not the entire solution.
- The perturbation benchmarks focus on unseen genes or combinations inside curated experimental datasets; they do not establish universal generalization across all perturbation regimes.

## Related Pages

- [scGPT](../entities/scGPT.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)

## Open Questions

- How much of scGPT's practical advantage comes from large-scale atlas pretraining versus the task-specific fine-tuning objectives layered on top of it?
- As more single-cell foundation models are ingested in this collection, where does scGPT sit relative to retrieval-first models such as SCimilarity and language-native models such as C2S-Scale?
- How well would the core pretraining recipe transfer to disease-heavy, developmental, or multimodal corpora that differ substantially from the normal-human atlas used here?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T11:20:07+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/cui_2024_scgpt_toward_building_a_foundation.pdf -o /tmp/odl-check-scgpt -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/cui_2024_scgpt_toward_building_a_foundation/opendataloader-run.json](../../raw/derived/opendataloader/cui_2024_scgpt_toward_building_a_foundation/opendataloader-run.json)
- Output: [raw/derived/opendataloader/cui_2024_scgpt_toward_building_a_foundation/cui_2024_scgpt_toward_building_a_foundation.md](../../raw/derived/opendataloader/cui_2024_scgpt_toward_building_a_foundation/cui_2024_scgpt_toward_building_a_foundation.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
