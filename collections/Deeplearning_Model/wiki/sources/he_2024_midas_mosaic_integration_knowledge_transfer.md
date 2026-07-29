---
title: Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS
kind: paper
status: ingested
added: 2026-07-29T17:52:23+09:00
raw_source: raw/sources/he_2024_midas_mosaic_integration_knowledge_transfer.pdf
---

# Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS

## Source

- File: [raw/sources/he_2024_midas_mosaic_integration_knowledge_transfer.pdf](../../raw/sources/he_2024_midas_mosaic_integration_knowledge_transfer.pdf)
- Added: 2026-07-29T17:52:23+09:00
- Venue/status: Nature Biotechnology 42, 1594-1605 (2024); published online 23 January 2024
- Authors: Zhen He, Shuofeng Hu, Yaowen Chen, Sijing An, Jiahao Zhou, Runyan Liu, Junfeng Shi, Jing Wang, Guohua Dong, Jinhui Shi, Jiaxin Zhao, Le Ou-Yang, Yuan Zhu, Xiaochen Bo, and Xiaomin Ying
- DOI: `10.1038/s41587-023-02040-y`
- SHA-256: `2eb26d29bd7e01dc1a0766a50ffbe31ddc1bc08ea84f90774326dccb46462c84`

## Summary

MIDAS is a variational deep generative framework for `mosaic` single-cell multi-omics integration, where datasets overlap in only some of RNA, ATAC, and ADT measurements. It jointly performs dimensionality reduction, modality alignment, missing-modality imputation, and batch correction. The central design separates a modality-agnostic biological-state latent variable from a technical-noise latent variable, then adds reference-to-query model transfer and reciprocal label mapping. The paper benchmarks MIDAS against 19 alternatives and builds a 185,518-cell trimodal PBMC atlas.

## Methods

- Modality-specific encoders and decoders are organized as a VAE over incomplete RNA, ATAC, and ADT count blocks.
- A product-of-experts posterior combines whatever modalities are observed for a cell.
- Joint-posterior regularization supplies self-supervised modality alignment.
- Information-bottleneck penalties disentangle biological state from batch-associated technical noise.
- Model transfer fine-tunes an atlas-pretrained MIDAS on query data; reciprocal reference mapping transfers labels while retaining the ability to flag query populations absent from the reference.
- The authors introduce `scMIB`, extending scIB with modality-alignment and feature-space metrics for mosaic integration.

## Key Claims

- One model can integrate flexible combinations of three modalities while simultaneously correcting batches and imputing missing blocks.
- Explicit biological/technical disentanglement makes the latent representation useful for clustering, annotation, trajectory analysis, and atlas transfer.
- Reference transfer can rescue difficult diagonal-integration settings that lack cell-to-cell cross-modal correspondence.

## Evidence

- In complete trimodal DOGMA-seq and TEA-seq benchmarks, MIDAS has the highest reported scIB batch-correction, biological-conservation, and overall scores; raw versus corrected cell-type fold changes remain strongly correlated across modalities (`Pearson r > 0.8`).
- Across constructed mosaic tasks, MIDAS outperforms scVAEIT, scMoMaT, Multigrate, and StabMap in the paper's scIB/scMIB comparisons.
- Cell labels inferred from incomplete DOGMA tasks have micro-F1 above `0.885` relative to full-data labels, except in the fully diagonal case.
- The PBMC atlas integrates `185,518` cells from `27` batches, `10` platforms, and RNA/ATAC/ADT combinations.
- In cross-tissue transfer, model transfer takes `1.28 h` versus `2.61 h` for de novo integration while giving comparable performance; reciprocal mapping identifies a progenitor population absent from the PBMC reference.

## Limitations

- The implemented model is limited to three modalities; extension to four or more is proposed rather than demonstrated.
- Fully diagonal data without paired cross-modal anchors remain harder; the paper reports only moderate performance until atlas transfer is added.
- Imputed measurements are model-derived and should not automatically be treated as observed evidence, especially for regulatory-network inference.
- Several biological findings, including the proposed low-chromatin-accessibility T-cell state, are computational observations requiring independent validation.
- Benchmark datasets are largely public blood multi-omics collections, so performance may not transfer unchanged to other tissues or assay combinations.

## Related Pages

- [MIDAS](../entities/MIDAS.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [MultiVI](../entities/MultiVI.md)
- [GLUE](../entities/GLUE.md)

## Open Questions

- How reliable are imputed modalities for quantitative downstream tests rather than visualization or label transfer?
- How much paired data or reference overlap is needed before atlas transfer rescues a fully diagonal dataset?
- Can biological and technical latent factors remain identifiable when tissue, batch, and modality are strongly confounded?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T18:04:58+0900
- Manifest: [raw/derived/opendataloader/he_2024_midas_mosaic_integration_knowledge_transfer/opendataloader-run.json](../../raw/derived/opendataloader/he_2024_midas_mosaic_integration_knowledge_transfer/opendataloader-run.json)
- Output: [raw/derived/opendataloader/he_2024_midas_mosaic_integration_knowledge_transfer/he_2024_midas_mosaic_integration_knowledge_transfer.md](../../raw/derived/opendataloader/he_2024_midas_mosaic_integration_knowledge_transfer/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- Layout text: [raw/derived/pdftext/He_2024_MIDAS/He_2024_MIDAS.txt](../../raw/derived/pdftext/He_2024_MIDAS/He_2024_MIDAS.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
