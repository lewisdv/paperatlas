---
title: Continual integration of single-cell multimodal data with MIRACLE
kind: paper
status: ingested
added: 2026-08-03T12:54:08+09:00
raw_source: raw/sources/zhou_2026_miracle_continual_multimodal_integration.pdf
---

# Continual integration of single-cell multimodal data with MIRACLE

## Source

- File: [raw/sources/zhou_2026_miracle_continual_multimodal_integration.pdf](../../raw/sources/zhou_2026_miracle_continual_multimodal_integration.pdf)
- Added: 2026-08-03T12:54:08+09:00
- Authors: Jiahao Zhou, Jing Wang, Shuofeng Hu, Tongtong Kan, Chao Feng, Xiaohan Qiang, Guohua Dong, Jinhui Shi, Runyan Liu, Xiaochen Bo, Le Ou-Yang, Xiaomin Ying, and Zhen He
- Venue/status: *Nature Computational Science* article; accepted 30 June 2026. The supplied PDF shows `Published online: xx xx xxxx`, so a final online-publication date is not available in this source copy.
- DOI: [10.1038/s43588-026-01030-9](https://doi.org/10.1038/s43588-026-01030-9)
- SHA-256: `4203d9ff002a1aea69c816ed73410cd6aa39d82430e605933928d631c9ab3282`

## Summary

- `MIRACLE` (multimodal integration with continual learning) updates a single-cell atlas as new datasets arrive rather than reintegrating every past dataset at each update.
- It uses [MIDAS](../entities/MIDAS.md) as its multimodal mosaic VAE base, retaining MIDAS's RNA, ATAC, and ADT integration, batch-correction, and imputation functions.
- The continual-learning wrapper combines dynamic architecture adaptation for newly arriving modalities or features with rehearsal of a bounded memory of past cells.
- Its distribution-preserving reservoir sampling (`DPRS`) keeps past-batch proportions and uses ball-tree sampling (`BTS`) in embedding space to retain within-batch distributional coverage.
- The paper evaluates online integration across batches, modality combinations, tissues, and respiratory infections, framing the output as a continually refinable and shareable multimodal atlas.

## Method

- At an update step, MIRACLE trains the previous model on the new batch together with rehearsal memory, then recomputes integration outputs for all data observed so far.
- When new features or a modality appear, the architecture adds the corresponding parameters, initializes those additions, and combines them with the existing parameters before training.
- DPRS first applies batched reservoir sampling so the bounded memory preserves the original contribution of each incoming batch. It then uses BTS to partition the embedding space at equal-frequency resolutions and sample within those partitions.
- The base MIDAS model provides modality-specific encoder/decoder components, shared biological-state embeddings, batch-associated technical-noise handling, and imputed or batch-corrected modality outputs.
- The paper contrasts four update choices: repeated offline reintegration, fixed-model generalization, sequential fine-tuning without rehearsal, and its rehearsal-based continual-learning update.

## Reported Evidence

### Bounded-Memory Continual Integration

- On a 523,369-cell, 42-batch cardiomyopathy snRNA-seq dataset, reported integration quality rose with rehearsal capacity and saturated at 20,000 cells, or about one twenty-sixth of the full sample.
- On the 2.3-million-cell Human Lung Cell Atlas benchmark, the paper reports that MIRACLE had higher integration accuracy and ran more than an order of magnitude faster than repeated offline integration while retaining a low, constant memory footprint.
- In the eight-batch RNA+ADT WNN PBMC benchmark, MIRACLE was reported to remain close to its offline version across update steps, whereas the no-rehearsal transfer control degraded in batch mixing as old information was forgotten.

### Mosaic and Atlas-Level Evaluation

- The DOTEA test combines DOGMA-seq and TEA-seq PBMC batches into four RNA, ATAC, and ADT modality combinations. MIRACLE was reported to retain modality alignment, batch correction, and cell-type structure as incomplete blocks arrived.
- For the 34-batch PBMC reference atlas, the paper adds RNA-only tonsil and spleen data and ATAC+ADT bone-marrow data online. It reports that MIRACLE preserved prior structure and made newly represented tissue-specific cell types distinct, unlike the fixed generalization and no-rehearsal transfer baselines.
- The reported benchmarks use `scIB` for horizontal or rectangular settings and `scMIB` for mosaic settings, plus continual-learning average accuracy and backward transfer to quantify historical-task retention.

### Respiratory-Infection Atlas

- Starting from the 34-batch healthy PBMC trimodal atlas, the study sequentially adds COVID-19 (10 RNA+ADT batches), influenza A (7 RNA batches), and tuberculosis (20 RNA+ADT batches).
- The authors refine the atlas from 13 to 23 annotated cell types and report an expanded CD4+ cytotoxic T-cell population in COVID-19, a HERC1+ T-cell subset in influenza A, and reduced MAIT-cell fractions across all three infections.
- These are computational interpretations from the continually integrated datasets; the paper cites supporting analyses, but the inferred cell states and mechanisms are not independent experimental validation.

## Interpretation

- MIRACLE makes the *arrival pattern* of data a first-class design choice. `Mosaic` describes which modalities co-occur, while continual integration describes how the model should update when another mosaic block appears.
- Its main novelty is not a new static multi-omics likelihood. It is a continual-learning wrapper that turns MIDAS from a static mosaic integrator into a bounded-memory online atlas-updating procedure.
- The comparison makes a useful three-way tradeoff explicit: fixed reference mapping is efficient but may miss new variation; naïve fine-tuning adapts but forgets; rehearsal aims to preserve historical knowledge while keeping recomputation bounded.
- Because the learned representation and all prior outputs change after an update, model versioning and the composition of rehearsal memory become part of the scientific provenance of an atlas.

## Limitations

- The demonstrations inherit MIDAS's current RNA/ATAC/ADT scope. Additional modalities, methylomics, metabolomics, and spatial context are proposed future extensions rather than demonstrated core capabilities.
- The rehearsal memory is necessarily a lossy summary. Its adequacy depends on capacity, sampling, batch order, and whether rare or newly emerging states are represented in the stored cells.
- Online and offline quality is evaluated on curated sequential benchmarks. A strong result under one ordering or reference configuration does not establish order-robust behavior for arbitrary future data streams.
- Dynamic extension addresses added features and modalities, but changes in preprocessing, feature definitions, or confounded biological and technical variation can still destabilize comparability across updates.
- Label transfer, imputed modalities, and disease-associated cell-state interpretations remain model-assisted estimates; they should not be treated as observed measurements or causal mechanisms without external validation.

## Related Pages

- [MIRACLE](../entities/MIRACLE.md)
- [MIDAS](../entities/MIDAS.md)
- [Continual Single-Cell Atlas Integration](../concepts/continual-single-cell-atlas-integration.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Multi-Omics Integration Method Taxonomy](../concepts/multi-omics-integration-method-taxonomy.md)
- [StabMap](../entities/StabMap.md)
- [scVAEIT](../entities/scVAEIT.md)

## Open Questions

- How can an atlas automatically detect when its current rehearsal memory no longer represents newly introduced biology?
- Which update outputs should be frozen and versioned so that earlier analyses remain reproducible after later continual integration?
- Can continual learning retain reliable integration when a new modality has little or no overlap with prior RNA, ATAC, and ADT data?
- How should privacy, access control, and consent constraints affect sharing a model whose rehearsal memory contains raw past cells?
- Do reported online-integration gains persist when cell labels, protocols, and biological novelty are systematically more heterogeneous than the curated benchmarks?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-03T12:54:08+0900
- Manifest: [raw/derived/opendataloader/zhou_2026_miracle_continual_multimodal_integration/opendataloader-run.json](../../raw/derived/opendataloader/zhou_2026_miracle_continual_multimodal_integration/opendataloader-run.json)
- Output: [raw/derived/opendataloader/zhou_2026_miracle_continual_multimodal_integration/zhou_2026_miracle_continual_multimodal_integration.md](../../raw/derived/opendataloader/zhou_2026_miracle_continual_multimodal_integration/zhou_2026_miracle_continual_multimodal_integration.md)
- Layout text: [raw/derived/pdftext/Zhou_2026_MIRACLE/Zhou_2026_MIRACLE.txt](../../raw/derived/pdftext/Zhou_2026_MIRACLE/Zhou_2026_MIRACLE.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
