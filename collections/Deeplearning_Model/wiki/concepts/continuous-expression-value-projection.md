# Continuous Expression Value Projection

## Definition

- Continuous expression value projection maps each scalar gene-expression value directly into a dense vector before sequence modeling.
- The goal is to preserve quantitative resolution that gene ranking or expression binning can discard.

## In CellFM

- An MLP projects each scalar expression value to a `1,536`-dimensional representation.
- The projected value is added to a gene-ID embedding and processed by ERetNet.
- Twenty percent of expressed genes are masked, and the model reconstructs their expression representations with MSE-based objectives.

## In scFoundation

- [scFoundation](../entities/scFoundation.md) also remains close to continuous expression and predicts masked values.
- Its distinctive contribution is [Read-Depth-Aware Pretraining](read-depth-aware-pretraining.md), which conditions reconstruction on source and target total-count indicators.

## Comparison

- [Rank-Value Encoding](rank-value-encoding.md) emphasizes corpus-relative gene importance and robustness but discards precise magnitude.
- scGPT-style value categorization preserves expression through learned value embeddings but discretizes or bins the signal.
- Value projection retains more quantitative detail, but the projection, normalization, masking rule, and loss still impose a model-specific abstraction over counts.

## Caveats

- Preserving continuous values does not automatically solve batch effects, dropout, or normalization bias.
- Benchmark gains cannot be attributed to value projection alone when corpus size, model scale, backbone, and downstream heads also change.
- A high-dimensional projection is not itself a mechanistic account of expression.

## Sources

- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
