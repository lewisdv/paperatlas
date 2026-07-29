---
title: "CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells"
kind: paper
status: ingested
added: 2026-05-15T14:55:57+09:00
raw_source: raw/sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.pdf
doi: 10.1038/s41467-025-59926-5
notion_url: https://www.notion.so/351302d9c59881aebbfadca214e73fcf
notion_hub: VITAL 디지털세포
pdf_status: downloaded
---

# CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells

## Source

- File: [raw/sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.pdf](../../raw/sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.pdf)
- DOI: [10.1038/s41467-025-59926-5](https://doi.org/10.1038/s41467-025-59926-5)
- Venue/status: Nature Communications article; published online 20 May 2025
- Authors: Yuansong Zeng, Jiancong Xie, Ningyuan Shangguan, Zhuoyi Wei, Wenbing Li, Yun Su, Shuangyu Yang, Chengyang Zhang, Jinbo Zhang, Nan Fang, Hongyu Zhang, Yutong Lu, Huiying Zhao, Jue Fan, Weijiang Yu, Yuedong Yang
- Code: [biomed-AI/CellFM](https://github.com/biomed-AI/CellFM)
- Data: Zenodo records `10.5281/zenodo.15138665` and `10.5281/zenodo.15155900`
- Notion: [CellFM (Zeng et al., 2025) — 100M-cell RetNet 기반 scale baseline](https://www.notion.so/351302d9c59881aebbfadca214e73fcf)
- Hub: VITAL 디지털세포
- Added: 2026-05-15T14:55:57+09:00

## Summary

CellFM is an `800M`-parameter human single-cell foundation model pretrained on `102,304,686` cells from `19,914` samples. Its central design choice is continuous value projection: scalar expression values are mapped to dense vectors, combined with gene-ID embeddings, and reconstructed after masking rather than being reduced to gene ranks or discrete expression bins. To make this scale computationally tractable, CellFM replaces a conventional Transformer backbone with `ERetNet`, a linear-complexity retention architecture, and uses LoRA for parameter-efficient downstream adaptation.

## Corpus And Preprocessing

- The corpus aggregates `102,304,686` human cells from GEO, ENA, GSA, ImmPort, and other public repositories.
- It includes `19,914` samples. The source reports `46.3M` cells from normal donors, `7.1M` from viral-infection donors, `3.5M` from lung-cancer donors, and about `70M` cells with cell-type annotations.
- `66.7M` cells were generated with 10x Genomics technologies.
- A standardized workflow filters cells with fewer than `200` detected genes, normalizes gene symbols to HGNC-approved names, and stores the matrices in a unified sparse format.
- The final preprocessing vocabulary contains `24,078` protein-coding and common mitochondrial genes. Counts are normalized and log1p-transformed.

## Representation And Architecture

- Each cell is represented by at most `2,048` expressed genes. Cells above the limit are subsampled from highly expressed genes; shorter inputs are padded.
- A multilayer perceptron projects each scalar expression value into a `1,536`-dimensional vector, which is added to a learned gene-ID embedding. A `[CLS]`-like token aggregates cell-level information.
- During pretraining, `20%` of non-padding genes are masked. The model reconstructs masked expression representations with a masked MSE objective plus a second cell-token-to-gene-vocabulary loss.
- The `800M` model stacks `40` ERetNet blocks with `48` attention/retention heads per block and head dimension `32`.
- ERetNet modifies RetNet with gated multi-head retention, an SGLU feed-forward replacement, and DeepNorm for training stability. The claimed computational advantage is linear rather than quadratic complexity in the number of input genes.
- Pretraining used two epochs, Adam with initial learning rate `1e-7`, total batch size `128`, MindSpore data parallelism, and `32` Ascend 910 NPUs across four Huawei Atlas 800 servers.
- LoRA freezes the main pretrained weights and learns low-rank updates in the ERetNet encoder during task adaptation.

## Evaluations And Evidence

### Gene Function

- Zero-shot gene embeddings were evaluated on dosage sensitivity, bivalent versus unmethylated promoters, and bivalent versus H3K4-only promoters.
- CellFM's average accuracy was reported as `5.68%` above UCE and `5.86%` above scGPT across those three binary tasks.
- On Gene Ontology multilabel prediction restricted to the ten most frequent functions in each ontology branch, CellFM exceeded GeneCompass and UCE by `1.6%` and `1.94%` in average AUPR.

### Perturbation

- For Adamson and Norman Perturb-seq benchmarks, CellFM gene embeddings replaced the original gene embeddings inside GEARS.
- The resulting model improved average PCC by `1%` and MSE by `1.45%` over the second-ranked scFoundation configuration, and improved PCC and MSE by `4.75%` and `7%` over unmodified GEARS.
- In a 20-gene reverse-perturbation benchmark with `210` possible one- or two-gene combinations, CellFM recovered the correct perturbation within the top ten for `81.8%` of test cases, `18.1` percentage points above the authors' scGPT re-evaluation.
- When CellFM cell embeddings replaced CellOT's input representation for four drug-perturbation datasets, the source reports average improvements of `66.6%` in L2 and `2.2%` in PCC over CellOT.

### Cell Annotation

- The frozen-embedding annotation benchmark used the smaller `80M` CellFM rather than the flagship `800M` model.
- Across eight within-dataset benchmarks, CellFM-80M averaged `92.91%` accuracy, `2.02` percentage points above scFoundation.
- Across seven cross-batch datasets, it was `2.3` percentage points above scFoundation on average.
- The `800M` model was weaker in the paper's frozen-embedding setting but, after fine-tuning, averaged `12.8%` and `15.92%` higher accuracy than scGPT and Geneformer across the inter-dataset benchmarks.

### Gene Relationships

- The paper uses zero-shot gene-embedding similarity, attention maps, and immune-cell fine-tuning to recover gene programs and context-sensitive immune relationships.
- Across nine perturbed genes, an average of `18` of the top `20` attention-ranked influenced genes were found in ChIP-Atlas.
- The authors nevertheless state that CellFM attention is limited for static or global biological knowledge.

## Key Claims

- Continuous expression-value projection can preserve quantitative signal that rank-based and binned representations discard.
- A retention-based architecture can scale human single-cell pretraining to both a `100M`-cell corpus and an `800M`-parameter model.
- Large pretrained gene and cell representations can improve multiple task-specific systems, including classifiers, GEARS, and CellOT.

## Interpretation

- CellFM is best read as a scale-and-representation paper, not simply as a universal end-to-end solver.
- Several strongest results come from inserting CellFM embeddings into another method or training a classifier on frozen embeddings.
- The paper's own taxonomy places Geneformer in the ordering family, scGPT in value categorization, and CellFM plus scFoundation in value projection. This is a useful comparison axis, but individual implementations differ in more than representation alone.
- The distinction between CellFM-80M and CellFM-800M matters: frozen-embedding annotation results from the smaller model should not be attributed automatically to the flagship model.

## Limitations

- The pretraining data are human-only, limiting cross-species analysis.
- The model does not incorporate explicit biological prior knowledge.
- Attention maps do not reliably recover all static or global biological relationships and should not be treated as causal explanations.
- Inputs are capped at `2,048` expressed genes, so some information is discarded in cells with longer detected-gene lists.
- Benchmark improvements combine changes in corpus, parameter count, representation, architecture, downstream heads, and fine-tuning procedure; they do not isolate a single causal source of gain.
- Reverse perturbation was evaluated for genes but not for drug molecules, which require drug-specific molecular information.

## Related Pages

- [CellFM](../entities/CellFM.md)
- [Continuous Expression Value Projection](../concepts/continuous-expression-value-projection.md)
- [Retention-Based Single-Cell Modeling](../concepts/retention-based-single-cell-modeling.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Study Guide: scGPT, scFoundation, Geneformer, and CellFM](../syntheses/scgpt-scfoundation-geneformer-cellfm-study-guide.md)

## Open Questions

- How much of CellFM's advantage comes from the `102.3M`-cell corpus, the `800M` parameter count, continuous value projection, or ERetNet?
- Why does the `800M` model lag the `80M` variant for frozen-embedding annotation but improve strongly after fine-tuning?
- How stable are the perturbation gains when the downstream model, dataset split, and classifier are held strictly constant across foundation models?
- Can retention-derived gene relationships be validated with perturbation or binding experiments beyond attention overlap?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T14:51:15+09:00
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.pdf -o raw/derived/opendataloader/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline -f markdown --image-output off`
- Manifest: [raw/derived/opendataloader/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline/opendataloader-run.json](../../raw/derived/opendataloader/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline/opendataloader-run.json)
- Output: [raw/derived/opendataloader/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md](../../raw/derived/opendataloader/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
- Poppler layout text: [raw/derived/pdftext/CellFM_Zeng_2025/CellFM_Zeng_2025.txt](../../raw/derived/pdftext/CellFM_Zeng_2025/CellFM_Zeng_2025.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
