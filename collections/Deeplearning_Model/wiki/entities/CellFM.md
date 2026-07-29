# CellFM

## Type

- Named system / single-cell foundation model

## Definition

- CellFM is an `800M`-parameter human transcriptomic foundation model pretrained on `102.3M` single cells.
- It combines continuous expression-value projection with an efficient retention-based backbone.

## Corpus And Representation

- Pretrained on `102,304,686` cells from `19,914` samples.
- Each scalar expression value is projected into a dense vector and added to a learned gene-ID embedding.
- The model accepts up to `2,048` expressed genes per cell and uses a cell-level aggregation token.
- Pretraining masks `20%` of non-padding genes and reconstructs their expression representations.

## Core Architecture

- `40` ERetNet blocks with `48` retention heads per block and hidden size `1,536`.
- ERetNet combines linear-complexity retention, SGLU, and DeepNorm.
- LoRA supports parameter-efficient adaptation.
- The flagship model was trained with MindSpore on `32` Ascend 910 NPUs.

## Reported Uses

- Frozen-embedding and fine-tuned cell annotation.
- Gene-function prediction.
- GEARS-based genetic perturbation response prediction.
- CellOT-based drug-response prediction.
- Reverse perturbation retrieval.
- Gene-program and gene-relationship analysis.

## Caveats

- Some headline evaluations use CellFM embeddings inside separate task-specific systems.
- The paper uses the `80M` model for frozen-embedding annotation and the `800M` model for fine-tuned comparisons; those results should not be conflated.
- Human-only pretraining and the absence of explicit biological priors limit the model's scope.
- Attention-derived relationships remain incomplete and non-causal.

## Related

- [Source: CellFM](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
- [Continuous Expression Value Projection](../concepts/continuous-expression-value-projection.md)
- [Retention-Based Single-Cell Modeling](../concepts/retention-based-single-cell-modeling.md)
- [Study Guide: scGPT, scFoundation, Geneformer, and CellFM](../syntheses/scgpt-scfoundation-geneformer-cellfm-study-guide.md)
