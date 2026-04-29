---
title: Multimodal foundation transformer models for multiscale genomics
kind: paper
status: ingested
added: 2026-04-29T21:53:40+09:00
raw_source: raw/sources/khan_2025_multimodal_foundation_transformer_models_for.pdf
---

# Multimodal foundation transformer models for multiscale genomics

## Source

- File: [raw/sources/khan_2025_multimodal_foundation_transformer_models_for.pdf](../../raw/sources/khan_2025_multimodal_foundation_transformer_models_for.pdf)
- Added: 2026-04-29T21:53:40+09:00
- Venue/status: Nature Methods perspective; accepted 17 October 2025, with the extracted PDF still showing an unresolved published-online placeholder
- Authors: Sumeer Ahmad Khan, Xabier Martinez-de-Morentin, Abdel Rahman Alsabbagh, Alberto Maillo, Vincenzo Lagani, David Gomez-Cabrero, Robert Lehmann, and Jesper Tegner
- DOI: `10.1038/s41592-025-02918-6`

## Summary

This perspective surveys the emerging transformer landscape across genomics and argues that the field is moving from unimodal domain models toward multimodal foundation transformer systems that operate across DNA, single-cell, spatial, proteomic, image, and text modalities. Its most distinctive contribution is a three-tier taxonomy plus a forward-looking `Super Transformer` blueprint with modality-specific encoders, shared embeddings, and cross-attention for multiscale integration. In this collection, the paper matters because it places single-cell-focused systems such as scGPT, scFoundation, and C2S-Scale inside a broader multiscale transformer roadmap.

## Methods

- The paper organizes current genomics transformers into three groups: augmented unimodal models that predict outside their training modality, multi-omics multimodal transformers, and broader multimodal systems that also incorporate images or text.
- It reviews example architectures across genomic sequence modeling, single-cell omics, spatial transcriptomics, and LLM-linked molecular analysis, and pairs the review with code-based primers for practical adoption.
- It reports a landscape analysis of `91` transformer models (`41` unimodal and `50` multimodal) using GPT-4o embeddings to visualize clustering and the recent rise of LLM-linked multimodal approaches.
- It proposes a `Super Transformer` design in which each modality is tokenized by a dedicated encoder, projected into a shared embedding space, fused by cross-attention or contrastive objectives, refined by hierarchical transformer blocks, and decoded through multitask heads.
- The blueprint also recommends efficiency and scaling strategies such as sparse or low-rank attention, pretrained module reuse, distributed training, and optional injection of structured priors such as ontology tokens.

## Key Claims

- Transformers are emerging as a natural backbone for multiscale genomics because biological data can be reframed as structured token sequences across many assay types.
- The field is progressing through a recognizable three-tier path from unimodal models to multi-omics systems to genuinely multimodal transformer ecosystems.
- Future high-value systems should combine heterogeneous modalities through modular shared-representation architectures rather than relying on isolated specialist models per assay.
- LLMs can support multimodal alignment and interpretation, but their outputs should be treated as hypothesis-generating aids rather than definitive biological ground truth.

## Evidence

- The perspective ties the need for more general transformer systems to atlas scale, citing more than `60` million cells in the Human Cell Atlas portal and more than `100` million cells in CZ CELLxGENE.
- It uses the three-tier taxonomy to place concrete models on a progression path, citing cross-modal or multimodal examples such as Enformer, scGPT, MarsGT, scCLIP, scMVP, Nicheformer, ChatNT, and CellWhisperer.
- The reported GPT-4o embedding analysis over `91` models is presented as evidence that transformer development is clustering into unimodal versus multimodal families, with a visible recent rise in LLM-linked models.
- The proposed `Super Transformer` is technically specified rather than left abstract: the paper calls for modality-specific tokenizers, shared-dimensional embeddings, cross-attention or contrastive fusion, hierarchical refinement blocks, and multitask heads for downstream prediction.
- The source also spells out operational prerequisites such as matched multimodal data, metadata standards, mixed-precision or distributed training, parameter-efficient fine-tuning, community benchmarks, and partial lab validation.

## Limitations

- This is a perspective and technical roadmap, not a new end-to-end benchmark paper, so it does not validate one unified `Super Transformer` against competing systems.
- The extracted PDF still carries an unresolved published-online placeholder, so the precise final online-publication date is not available from the current collection source.
- The paper explicitly treats compute cost, paired-data scarcity, metadata harmonization, and evaluation design as open bottlenecks rather than solved engineering details.
- Interpretability and modality alignment remain unsettled, and the paper notes that LLM-linked biological text integration can propagate weak or incomplete prior knowledge.

## Related Pages

- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [Super Transformer Architecture](../concepts/super-transformer-architecture.md)
- [scGPT](../entities/scGPT.md)
- [scFoundation](../entities/scFoundation.md)
- [C2S-Scale](../entities/C2S-Scale.md)
- [AIVC](../entities/AIVC.md)

## Open Questions

- Which already ingested systems in this collection look like partial `Super Transformer` components, and which remain fundamentally unimodal despite transfer-learning claims?
- How much biological performance gain comes from true multimodal fusion versus simply scaling stronger unimodal encoders and aligning them late?
- If this collection later includes more spatial and imaging sources, does the current single-cell-heavy picture understate the difficulty of multiscale transformer integration?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:53:03+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/khan_2025_multimodal_foundation_transformer_models_for.pdf -o /tmp/odl-check-khan -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/khan_2025_multimodal_foundation_transformer_models_for/opendataloader-run.json](../../raw/derived/opendataloader/khan_2025_multimodal_foundation_transformer_models_for/opendataloader-run.json)
- Output: [raw/derived/opendataloader/khan_2025_multimodal_foundation_transformer_models_for/khan_2025_multimodal_foundation_transformer_models_for.md](../../raw/derived/opendataloader/khan_2025_multimodal_foundation_transformer_models_for/khan_2025_multimodal_foundation_transformer_models_for.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
