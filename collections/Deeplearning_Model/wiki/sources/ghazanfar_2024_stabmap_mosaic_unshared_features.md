---
title: Stabilized mosaic single-cell data integration using unshared features
kind: paper
status: ingested
added: 2026-07-30T16:44:24+09:00
raw_source: raw/sources/ghazanfar_2024_stabmap_mosaic_unshared_features.pdf
---

# Stabilized mosaic single-cell data integration using unshared features

## Source

- File: [raw/sources/ghazanfar_2024_stabmap_mosaic_unshared_features.pdf](../../raw/sources/ghazanfar_2024_stabmap_mosaic_unshared_features.pdf)
- Added: 2026-07-30T16:44:24+09:00
- Authors: Shila Ghazanfar, Carolina Guibentif, and John C. Marioni
- Venue: *Nature Biotechnology* 42, 284-292 (2024)
- DOI: [10.1038/s41587-023-01766-z](https://doi.org/10.1038/s41587-023-01766-z)
- Published online: 25 May 2023
- License stated in source: The Author(s) 2023

## Summary

- `StabMap` is a reference-projection method for integrating mosaic single-cell datasets whose feature sets overlap only pairwise.
- It builds a `mosaic data topology` (MDT), a connected graph whose nodes are datasets and whose edges encode the number of shared features.
- Cells are projected into supervised or unsupervised reference coordinates by fitting linear maps along shortest paths through the graph.
- Because no feature must be present in every dataset, StabMap supports `multi-hop` integration in which some dataset pairs share no features at all.
- The method is modality-agnostic and is demonstrated across RNA, ATAC, protein, imaging, in situ transcriptomics, and spatial-neighborhood features.

## Algorithm

- Inputs are appropriately normalized cell-by-feature matrices, optional cell labels, and one or more reference datasets.
- The MDT contains an edge whenever two datasets share at least one feature; edge weights are the absolute number of shared features.
- The MDT must be connected, but a global intersection of features is not required.
- Each reference space is defined by PCA, linear discriminant analysis when labels are supplied, or a user-provided lower-dimensional embedding.
- If a query shares the reference features, it is projected directly with the reference loadings.
- If only a subset overlaps, multivariable linear regression predicts reference coordinates from the shared features.
- If no direct overlap exists, the regression-and-projection step is repeated along the weighted shortest path through intermediate datasets.
- When multiple references are used, their score matrices are reweighted and concatenated.
- Residual batch effects are handled after StabMap with a horizontal integration method such as fastMNN.

## Evidence

### Simulated Mosaic Integration

- A paired 10x PBMC Multiome dataset of about 36,000 cells is split into RNA-only and ATAC-only views with 318 matched promoter-gene features.
- Compared with naive PCA, UINMF, and MultiMAP, StabMap better preserves reported cell-type classification and local cell-neighborhood structure.
- Mouse-gastrulation query datasets are restricted to 50-5,000 randomly selected genes and evaluated across 12 train-query combinations.
- StabMap retains higher cell-type classification accuracy than the comparison methods, particularly when very few query features are available.

### Multi-Hop Integration

- PBMC RNA-only, ATAC-only, and Multiome blocks are constructed so RNA and ATAC have no direct feature overlap.
- StabMap is compared with Cobolt and MultiVI while the size of the bridging Multiome dataset is varied.
- Performance deteriorates when the bridge contains fewer than about 1,000 cells and becomes stable above that scale in the reported experiment.
- A chain of eight mouse-gastrulation datasets shows better preservation with more informative features and, to a smaller degree, more cells per bridge dataset.
- Real demonstrations connect CyTOF, ECCITE-seq, and 10x Multiome PBMC data through seven shared proteins, and connect IMC, CITE-seq, and Xenium breast-tumor data through 19 shared IMC-CITE protein features.

### Spatial Mapping

- In breast cancer data, StabMap transfers epithelial and broad cell-type annotations from IMC to Xenium, imputes IMC protein signal on Xenium-resolved tissue, and supports local cell-contact maps.
- A mouse-embryo analysis integrates scRNA-seq from wild-type and Brachyury-knockout chimeras with 351-gene seqFISH data and spatial-neighborhood features.
- The local model identifies 16,677 of 57,536 seqFISH cells with significant enrichment or depletion of knockout neighbors at FDR-adjusted P below 0.05.
- The mapped pattern suggests anterior-posterior differences in splanchnic mesoderm, with Tbx1 and Fgf8 associated with the anterior enriched domain and Foxf1, Wnt2, Hoxb2, and Hoxb4 with posterior depleted regions.
- This is computational transfer onto a spatial reference, not a new spatial perturbation experiment.

### Computation

- The paper reports seconds to under a minute for tens of thousands of cells on a standard MacBook and 5-10 minutes for 300,000 cells in the breast-cancer analysis.
- Sparse matrices are used where possible, but the feature-imputation helper converts to dense arrays and is identified as a memory limitation.

## Interpretation

- StabMap separates two requirements that are often conflated: every dataset must be connected to the collection, but every dataset need not share one universal feature set.
- Unshared features influence the reference coordinates before the shared features are used to predict those coordinates in another dataset.
- The bridge datasets are statistical transport infrastructure; their size, feature informativeness, and biological coverage determine how much information survives repeated projections.
- StabMap is not a generative latent-variable model. Its strength is a fast, inspectable sequence of reference projections that can wrap around other vertical or horizontal integration methods.
- The output coordinate system is partly a scientific choice because reference selection determines which biological variation defines the map.

## Limitations

- A connected MDT is mandatory. A disconnected dataset cannot be mapped without an additional bridge or prior feature relation.
- Multi-hop errors can accumulate, and the PBMC experiment shows failure when the bridging dataset is too small.
- The core mappings are linear; nonlinear alternatives are proposed as future work.
- All features from a multiomic experiment are concatenated in the demonstrated workflow, which is a naive form of vertical integration.
- Batch correction is not intrinsic and may still be required downstream.
- Reference choice, preprocessing, and feature scaling can change the recovered space.
- Mapping, annotation transfer, and feature imputation do not automatically provide calibrated uncertainty for each prediction.

## Related Pages

- [StabMap](../entities/StabMap.md)
- [Multi-Hop Mosaic Integration](../concepts/multi-hop-mosaic-integration.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Multi-Omics Integration Method Taxonomy](../concepts/multi-omics-integration-method-taxonomy.md)
- [MIDAS](../entities/MIDAS.md)
- [MultiVI](../entities/MultiVI.md)

## Open Questions

- How should uncertainty compound across successive regression paths?
- Can graph-path selection use feature quality and biological coverage instead of only overlap counts?
- When should one choose a single reference versus several reweighted references?
- Would nonlinear mappings improve transfer without sacrificing speed and inspectability?
- How should bridge adequacy be diagnosed before downstream spatial or differential analysis?

## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Markdown: [raw/derived/opendataloader/ghazanfar_2024_stabmap_mosaic_unshared_features/ghazanfar_2024_stabmap_mosaic_unshared_features.md](../../raw/derived/opendataloader/ghazanfar_2024_stabmap_mosaic_unshared_features/ghazanfar_2024_stabmap_mosaic_unshared_features.md)
- Manifest: [raw/derived/opendataloader/ghazanfar_2024_stabmap_mosaic_unshared_features/opendataloader-run.json](../../raw/derived/opendataloader/ghazanfar_2024_stabmap_mosaic_unshared_features/opendataloader-run.json)
- Poppler layout text: [raw/derived/pdftext/Ghazanfar_2024_StabMap/Ghazanfar_2024_StabMap.txt](../../raw/derived/pdftext/Ghazanfar_2024_StabMap/Ghazanfar_2024_StabMap.txt)
- These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
