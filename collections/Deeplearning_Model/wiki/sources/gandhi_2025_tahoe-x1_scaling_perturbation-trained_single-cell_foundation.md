---
title: Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters
kind: paper
status: ingested
added: 2026-04-29T16:13:51+09:00
raw_source: raw/sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.pdf
---

# Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters

## Source

- File: [raw/sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.pdf](../../raw/sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.pdf)
- Added: 2026-04-29T16:13:51+09:00
- Venue/status: Preprint-style manuscript from Tahoe Therapeutics; no journal or DOI identified in the extracted text
- Authors: Shreshth Gandhi, Farnoosh Javadi, Valentine Svensson, Umair Khan, Matthew G. Jones, John Yu, Daniele Merico, Hani Goodarzi, and Nima Alidoust

## Summary

This paper presents Tahoe-x1 (Tx1), a family of perturbation-trained single-cell foundation models scaling to 3 billion parameters and aimed at cancer-relevant functional genomics. The central claim is that large-scale perturbation-rich pretraining, especially on the Tahoe-100M compendium, produces embeddings that are substantially better for context-dependent biology than observational atlas pretraining alone. In this collection, the paper is important because it makes perturbation-specific pretraining itself a first-class design choice rather than only a downstream fine-tuning task.

## Methods

- Tx1 is a scGPT-style transformer family in which each cell is represented as a gene-token sequence with discretized expression bins, masking indicators, a global `<cls>` token, and an optional `<drug>` token carrying chemical context.
- The pretraining objective is masked expression reconstruction with both gene-aware and cell-aware decoders, so the model jointly learns gene, cell, and compound representations.
- Pretraining uses up to `266` million single-cell profiles drawn from Tahoe-100M, Arc scBaseCount, and CZ CELLxGENE, with the largest Tx1-3B model using `32` transformer layers and training across `128` GPUs.
- Training follows a two-stage recipe, first with shorter `1,024`-gene contexts and then with longer `2,048`-gene contexts on a stricter quality-filtered subset.
- Evaluation spans four benchmark families: DepMap gene-essentiality prediction, MSigDB hallmark recovery from gene embeddings, Tabula Sapiens cell-type classification, and perturbation-response prediction in few-shot and zero-shot settings using Arc Institute's State Transition module on top of Tx1 embeddings.

## Key Claims

- Scaling perturbation-trained pretraining data improves context-generalizable functional genomics performance more than observational atlas pretraining alone.
- Tx1 achieves state-of-the-art or competitive-best results across gene essentiality, hallmark-pathway structure, cell-state classification, and held-out perturbation-response prediction.
- Compute-efficient implementation choices make multi-billion-parameter single-cell foundation models practical enough to train without proportionally exploding cost.
- Large perturbation compendia are framed not as optional extras but as essential ingredients for causal and translational utility in precision oncology.

## Evidence

- The paper reports that Tx1 achieves `3`- to `30`-fold higher compute efficiency than prior implementations of comparable cell-state models through FlashAttention-compatible design choices, mixed precision, and optimized distributed training.
- In DepMap-based essentiality prediction, the source states that Tx1 is the only model performing on the same level as or better than a linear baseline, while also achieving the strongest mean AUROC and AUPRC for broadly essential genes.
- For cancer hallmark recovery, Tx1-3B reaches a mean AUPRC of `0.31`, outperforming the compared protein- or transcriptome-embedding baselines in the MSigDB benchmark.
- On Tabula Sapiens classification, Tx1-3B is reported as competitive with or better than models trained on broader multi-species corpora despite being trained on human cells only.
- For held-out perturbation-response prediction, Tx1 embeddings combined with State Transition outperform SE-600M and simple baselines in both Tahoe-100M few-shot/zero-shot settings and donor-held-out Parse-PBMC transfer experiments.

## Limitations

- The source is a preprint-style manuscript from the model developers, so the strongest performance claims come from an author-controlled benchmark package rather than from an external independent comparison.
- The pretraining advantage is heavily tied to Tahoe-100M, which is unusually large and perturbation rich but still centered on in vitro cancer cell-line settings rather than primary tissues or in vivo tumor microenvironments.
- The current architecture remains transcriptomics-first: it models genes, cells, and drug context, but does not yet integrate protein abundance, spatial context, or other modalities that the paper itself identifies as important next steps.
- Some downstream perturbation claims depend on combining Tx1 embeddings with a separate State Transition module, so the perturbation-prediction stack is not purely a single-model end-to-end system.

## Related Pages

- [Tahoe-x1](../entities/Tahoe-x1.md)
- [Perturbation-Trained Foundation Models](../concepts/perturbation-trained-foundation-models.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [CellOT](../entities/CellOT.md)
- [scGPT](../entities/scGPT.md)
- [scFoundation](../entities/scFoundation.md)

## Open Questions

- How much of Tx1's reported gain comes from sheer dataset scale versus the fact that the pretraining corpus is explicitly perturbative?
- If more perturbation-heavy sources are ingested, does this collection need a sharper split between observational atlas foundation models and perturbation-trained foundation models?
- How well would the Tx1 recipe transfer beyond oncology cell lines into primary tissue, developmental, or multimodal settings?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T16:13:54+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.pdf -o /tmp/odl-check-tahoe -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation/opendataloader-run.json](../../raw/derived/opendataloader/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation/opendataloader-run.json)
- Output: [raw/derived/opendataloader/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md](../../raw/derived/opendataloader/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
