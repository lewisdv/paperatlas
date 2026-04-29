---
title: Towards multimodal foundation models in molecular cell biology
kind: paper
status: ingested
added: 2026-04-29T16:08:23+09:00
raw_source: raw/sources/cui_2025_towards_multimodal_foundation_models_in.pdf
---

# Towards multimodal foundation models in molecular cell biology

## Source

- File: [raw/sources/cui_2025_towards_multimodal_foundation_models_in.pdf](../../raw/sources/cui_2025_towards_multimodal_foundation_models_in.pdf)
- Added: 2026-04-29T16:08:23+09:00
- Venue/status: Perspective-style article; received 17 October 2023, accepted 29 January 2025, published online 16 April 2025
- Authors: Haotian Cui, Alejandro Tejada-Lapuerta, Maria Brbic, Julio Saez-Rodriguez, Simona Cristea, Hani Goodarzi, Mohammad Lotfollahi, Fabian J. Theis, and Bo Wang
- DOI: `10.1038/s41586-025-08710-y`

## Summary

This perspective argues that molecular cell biology is approaching a point where large multimodal foundation models (MFMs) could become a practical organizing layer for genomics, transcriptomics, epigenomics, proteomics, metabolomics, and spatial data. Rather than reporting one new trained model, the paper lays out why data-centric pretraining across modalities might outperform narrower specialist pipelines, which computational components such systems may need, which scientific tasks they could unlock, and which technical and governance bottlenecks still make the vision incomplete. In this collection, the paper matters because it turns several already ingested model threads into one explicit umbrella paradigm.

## Methods

- The paper proposes pretraining one multimodal model across large aggregated omics corpora with self-supervised learning, then adapting it to many downstream tasks through fine-tuning or in-context learning.
- It argues for unified tokenization across biological resolutions and modalities, from nucleotide-level inputs up to genes and proteins, so heterogeneous assays can enter one shared model space.
- A hybrid transformer design is proposed with intramodal attention for within-modality structure and intermodal attention for cross-modality relations.
- Training is framed as a promptable token-generation system that can support masked reconstruction, cross-modal prediction, temporal forecasting, and conditional perturbation-response generation within one model family.
- The workflow is explicitly data-centric and lab-in-the-loop: experimental rounds should refine the model, and the model should in turn prioritize informative next experiments.

## Key Claims

- Multimodal foundation models could serve as a unifying representation layer for molecular cell biology by learning across many contexts instead of treating each tissue, modality, or task as isolated.
- The strongest downstream opportunities are not limited to classification; they include continuous cell-state contextualization, gene-function and regulatory-network inference, missing-modality completion, and in silico perturbation.
- Shared large-scale pretraining is presented as a route to broader generalization and lower overfitting than traditional specialist models trained only on small labeled datasets.
- Progress will require not only bigger models but also better paired multimodal data, rigorous community benchmarks, uncertainty-aware outputs, and open infrastructure.

## Evidence

- The source contrasts the proposed MFM paradigm with earlier whole-cell and virtual-cell approaches based on rule-based modules or ODE systems, arguing that these approaches struggle with large nonlinear interactions across diverse tissues and cell states.
- It grounds the proposal in current data trends, highlighting atlas-scale resources such as HCA, HuBMAP, and HTAN plus rapidly growing paired multi-omics assays.
- Figure 3 specifies desired computational components including unified tokenization, hybrid multilevel attention, intramodal and cross-modal tasks, and prompt-guided generation.
- The paper names concrete opportunity areas: tissue heterogeneity characterization, context-specific gene-regulatory-network inference, cross-modal completion of cellular state, temporal trajectory reasoning, and perturbation-response prediction.
- It also explicitly cites already emerging ingredients relevant to this collection, including scGPT, Geneformer, scBERT, CellOT, CPA, and GEARS, as early evidence that parts of the MFM agenda are becoming technically plausible.

## Limitations

- This is a perspective and design blueprint, not a released end-to-end MFM benchmark, so it does not provide one integrated model with empirical head-to-head results.
- The paper repeatedly notes that paired multimodal data remain limited, especially outside transcriptomics, and that large-scale curation, harmonization, and global coordination are still major bottlenecks.
- Evaluation is itself an open problem because human-labeled annotations can penalize models that discover novel cell states or regulatory structure.
- Interpretability, hallucination risk, uncertainty reporting, compute access, privacy, and equitable data representation are all identified as unresolved constraints rather than solved engineering details.

## Related Pages

- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [AIVC](../entities/AIVC.md)
- [scGPT](../entities/scGPT.md)
- [scFoundation](../entities/scFoundation.md)
- [CellOT](../entities/CellOT.md)

## Open Questions

- Which already ingested systems in this collection look most like partial MFM implementations, and which still remain single-task tools under a broader MFM narrative?
- Does this collection need a later synthesis that separates perspective-style MFM roadmaps from papers that actually train and benchmark unified multimodal models?
- How much of the proposed MFM stack depends on true paired multimodal data versus architectures that can exploit fragmented and partially aligned datasets?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T16:08:27+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/cui_2025_towards_multimodal_foundation_models_in.pdf -o /tmp/odl-check-mmfm -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/cui_2025_towards_multimodal_foundation_models_in/opendataloader-run.json](../../raw/derived/opendataloader/cui_2025_towards_multimodal_foundation_models_in/opendataloader-run.json)
- Output: [raw/derived/opendataloader/cui_2025_towards_multimodal_foundation_models_in/cui_2025_towards_multimodal_foundation_models_in.md](../../raw/derived/opendataloader/cui_2025_towards_multimodal_foundation_models_in/cui_2025_towards_multimodal_foundation_models_in.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
