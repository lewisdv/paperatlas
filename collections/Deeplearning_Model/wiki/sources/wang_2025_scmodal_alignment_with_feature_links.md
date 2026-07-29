---
title: scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links
kind: paper
status: ingested
added: 2026-07-29T17:52:24+09:00
raw_source: raw/sources/wang_2025_scmodal_alignment_with_feature_links.pdf
---

# scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links

## Source

- File: [raw/sources/wang_2025_scmodal_alignment_with_feature_links.pdf](../../raw/sources/wang_2025_scmodal_alignment_with_feature_links.pdf)
- Added: 2026-07-29T17:52:24+09:00
- Venue/status: Nature Communications (2025)
- Authors: Gefei Wang, Jia Zhao, Yingxin Lin, Tianyu Liu, Yize Zhao, and Hongyu Zhao
- DOI: `10.1038/s41467-025-60333-z`
- SHA-256: `32b992f141acb4f2da3b3df25c6933ffb4eb8afeb4aa51249b98caee835edf76`

## Summary

scMODAL aligns unpaired single-cell modalities even when only a small set of weakly correlated feature pairs is known, as in RNA-to-protein integration. Nonlinear encoders map full modality-specific feature matrices into a shared latent space; a GAN mixes their distributions; mutual-nearest-neighbor anchors derived from linked features guide correct population matching; and geometry regularization preserves within-modality structure. The trained encoder-decoder compositions also support cross-modal imputation and feature-relationship inference.

## Methods

- Known positive feature pairs, such as a surface protein and its coding gene or an RNA gene and its ATAC gene-activity score, define the linked-feature views.
- Separate nonlinear encoder/decoder networks use all features rather than discarding modality-unique information.
- A discriminator aligns latent distributions adversarially.
- Mutual nearest neighbors computed in linked-feature space become anchor pairs constrained to stay close in the latent space.
- Autoencoding and Gaussian-kernel geometry penalties preserve information and local structure.
- Chaining an encoder from one modality with the other modality's decoder performs cross-modal feature imputation.

## Key Claims

- Weak, sparse feature links can guide unpaired nonlinear alignment when combined with adversarial distribution matching.
- Anchor, reconstruction, and geometry penalties prevent the population mismatches that occur with unconstrained GAN alignment.
- One integrated representation can support label transfer, imputation, relationship inference, and spatial cell-cell communication analysis.

## Evidence

- In RNA/ADT PBMC integration, label-transfer accuracy is approximately `98%` for broad and `86%` for fine annotations, the highest among the compared methods.
- Protein imputation has mean correlation `0.53`, versus `0.42` for MaxFuse and `0.40` for bindSC, relative improvements of `29%` and `34%`.
- The method remains strong when the linked protein panel is reduced to `30` features.
- Across RNA, protein, ATAC, and CODEX examples, the paper reports preservation of fine populations that competing methods merge.
- The implementation handles `322,318` RNA and ADT cells in the scaling analysis.
- Ablation is unusually informative: removing MNN-anchor regularization drives label-transfer accuracy close to zero, showing that adversarial mixing alone does not establish biological correspondence.

## Limitations

- scMODAL still requires known positively correlated feature links; absent or badly characterized links restrict applicability.
- The strong anchor-ablation failure demonstrates both the value of the prior and the model's dependence on it.
- Cross-modal imputation and inferred feature networks are predictions from the aligned model, not direct evidence of regulation.
- GAN optimization adds instability and additional design choices relative to probabilistic VAE integration.
- Most benchmarks use known annotations or paired assays as ground truth even though deployment targets unpaired data.

## Related Pages

- [scMODAL](../entities/scMODAL.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [GLUE](../entities/GLUE.md)
- [MultiVI](../entities/MultiVI.md)

## Open Questions

- How should negatively correlated, context-specific, or uncertain feature links be represented?
- Does anchor discovery remain reliable when one modality omits an entire cell population?
- How well calibrated are imputed features outside the cell states covered by the linked-feature anchors?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T18:04:58+0900
- Manifest: [raw/derived/opendataloader/wang_2025_scmodal_alignment_with_feature_links/opendataloader-run.json](../../raw/derived/opendataloader/wang_2025_scmodal_alignment_with_feature_links/opendataloader-run.json)
- Output: [raw/derived/opendataloader/wang_2025_scmodal_alignment_with_feature_links/wang_2025_scmodal_alignment_with_feature_links.md](../../raw/derived/opendataloader/wang_2025_scmodal_alignment_with_feature_links/wang_2025_scmodal_alignment_with_feature_links.md)
- Layout text: [raw/derived/pdftext/Wang_2025_scMODAL/Wang_2025_scMODAL.txt](../../raw/derived/pdftext/Wang_2025_scMODAL/Wang_2025_scMODAL.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
