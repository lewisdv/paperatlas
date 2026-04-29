---
title: Large-scale foundation model on single-cell transcriptomics
kind: paper
status: ingested
added: 2026-04-29T11:24:40+09:00
raw_source: raw/sources/hao_2024_large-scale_foundation_model_on_single-cell.pdf
---

# Large-scale foundation model on single-cell transcriptomics

## Source

- File: [raw/sources/hao_2024_large-scale_foundation_model_on_single-cell.pdf](../../raw/sources/hao_2024_large-scale_foundation_model_on_single-cell.pdf)
- Added: 2026-04-29T11:24:40+09:00
- Venue/status: Nature Methods article; published online 6 June 2024
- Authors: Minsheng Hao, Jing Gong, Xin Zeng, Chiming Liu, Yucheng Guo, Xingyi Cheng, Taifeng Wang, Jianzhu Ma, Xuegong Zhang, Le Song
- DOI: `10.1038/s41592-024-02305-7`
- Code: [biomap-research/scFoundation](https://github.com/biomap-research/scFoundation)

## Summary

This paper introduces scFoundation, also named xTrimoScFoundation alpha, as a large single-cell transcriptomic foundation model built around scale, gene coverage, and read-depth-aware pretraining. The model uses an asymmetric transformer-like encoder-decoder architecture over about twenty thousand genes and is pretrained on more than fifty million human scRNA-seq profiles. The paper emphasizes that scFoundation often works through non-fine-tuned or light-fine-tuned embeddings rather than heavy end-to-end downstream retraining, and positions it as a general foundation layer for clustering, drug response prediction, perturbation modeling, annotation, and gene module inference.

## Methods

- scFoundation models `19,264` genes with an asymmetric encoder-decoder architecture designed for sparse, long single-cell expression vectors.
- The core pretraining task is read-depth-aware (RDA) modeling, which extends masked language modeling by predicting masked gene values from either an unchanged or downsampled version of the same cell while conditioning on source and target total-count indicators `S` and `T`.
- Pretraining uses over `50` million human scRNA-seq profiles collected from public resources such as GEO, HCA, hECA, DISCO, and EMBL-EBI, spanning more than `100` tissue types across normal, disease, and tumor contexts.
- The main released model has about `100` million parameters, and the paper explicitly studies scaling behavior across `3M`, `10M`, and `100M` parameter variants.
- Downstream tasks often consume pooled encoder cell embeddings or decoder gene-context embeddings as features for task-specific heads or cooperating models such as DeepCDR, SCAD, GEARS, BBKNN, or SCENIC.

## Key Claims

- Large-scale pretraining with read-depth-aware objectives can produce a general single-cell foundation model that transfers across diverse downstream tasks.
- Modeling read-depth explicitly helps the pretrained model harmonize cells with different sequencing depth and even enhance low-depth profiles without dataset-specific fine-tuning.
- Scaling model size and data volume improves validation loss and downstream performance in a manner analogous to LLM scaling laws.

## Evidence

- Pretraining scale: the paper reports a `100M`-parameter model over `19,264` genes trained on more than `50` million human scRNA-seq profiles from over `100` tissue types.
- Scaling law evidence: validation loss follows a power-law decline across `3M`, `10M`, and `100M` parameter variants, and the `100M` scFoundation model is reported to surpass smaller or earlier transformer-scale baselines.
- Read-depth enhancement: on held-out cells downsampled to `1%`, `5%`, `10%`, and `20%` of original counts, scFoundation reportedly cuts MAE and MRE by about half even when the downsampling rate is below `10%`.
- Clustering without fine-tuning: in the pancreatic-islet downsampling benchmark, scFoundation is described as the only method whose cluster assignments align consistently with the reference clustering after enhancement; on Zheng68K it matches scVI on NMI and ARI while improving silhouette score.
- Perturbation prediction: using scFoundation embeddings inside GEARS, the source reports lower MSE than the original GEARS baseline; for two-gene perturbations it achieves the lowest average MSE in the `0/2 unseen` setting and outperforms GEARS and CPA across all unseen-gene cases.
- Annotation benchmarking: the paper reports the highest macro F1 on both tested annotation datasets when compared with CellTypist, scBERT, scANVI, ACTINN, Scanpy, and SingleCellNet.
- Gene-network evidence: the model identifies cell-type-specific regulators such as `KLF6`, `SPIB`, and `MXD4`, each stated to match prior monocyte, B-cell, or CD8 T-cell regulatory knowledge.

## Limitations

- The source explicitly notes that the current model is transcriptomics-only and does not yet include genomic or epigenomic inputs.
- Pretraining requires substantial computational resources, and the paper calls for further efficiency optimization.
- The authors also note that unsupervised pretraining ignores rich metadata that could link molecular features to phenotype.
- scFoundation treats read depth as a major technical confounder, but the paper itself notes that equalizing read depth does not remove all batch effects or modality differences.

## Related Pages

- [scFoundation](../entities/scFoundation.md)
- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)

## Open Questions

- How much of scFoundation's advantage comes from the RDA objective itself versus sheer scale in data and parameters?
- In this collection, when should a workflow prefer scFoundation-style read-depth-aware embeddings over scGPT-style fine-tuned generative transfer or SCimilarity-style retrieval?
- How would the same architecture behave once multimodal or metadata-aware pretraining is added, given that the authors explicitly identify those as next steps?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T11:24:54+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/hao_2024_large-scale_foundation_model_on_single-cell.pdf -o /tmp/odl-check-hao -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/hao_2024_large-scale_foundation_model_on_single-cell/opendataloader-run.json](../../raw/derived/opendataloader/hao_2024_large-scale_foundation_model_on_single-cell/opendataloader-run.json)
- Output: [raw/derived/opendataloader/hao_2024_large-scale_foundation_model_on_single-cell/hao_2024_large-scale_foundation_model_on_single-cell.md](../../raw/derived/opendataloader/hao_2024_large-scale_foundation_model_on_single-cell/hao_2024_large-scale_foundation_model_on_single-cell.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
