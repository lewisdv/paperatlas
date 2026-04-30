# Read-Depth-Aware Pretraining

## Definition

- Read-depth-aware pretraining is the strategy of teaching a single-cell foundation model to reason jointly about gene context and sequencing-depth variation during pretraining.
- In this collection, scFoundation operationalizes this with source and target total-count indicators so the model can learn from both unchanged and downsampled versions of the same cell.

## In scFoundation

- The RDA objective extends masked prediction by conditioning on a low-depth or duplicated input sample plus two total-count indicators, `S` and `T`.
- This lets the model learn both within-cell gene relationships and relationships between cells observed at different effective read depths.
- At inference time, setting `T` above `S` is used to generate read-depth-enhanced embeddings or expression estimates from low-depth cells.
- Compared with [Cell Sentences](cell-sentences.md), the representation stays closer to the original expression matrix and treats read depth as a first-class signal instead of translating cells into ranked language-like tokens.
- Compared with [Single-Cell Generative Pretraining](single-cell-generative-pretraining.md), the main differentiator is not only atlas-scale pretraining but the explicit technical abstraction for depth variation.
- Compared with [Evolutionary Contrastive RNA Pretraining](evolutionary-contrastive-rna-pretraining.md), this concept remains cell-profile-centric and technical-noise-aware rather than sequence-centric and function-pair-aware.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md), the downstream center of gravity is reusable embeddings and enhancement rather than nearest-neighbour atlas lookup with explicit provenance.

## Claimed Benefits

- Helps harmonize cells with different sequencing depth before downstream analysis.
- Enables useful enhancement or clustering performance even without dataset-specific fine-tuning.
- Makes pretrained embeddings more reusable for downstream methods such as clustering, perturbation modeling, and drug response prediction.

## Caveats

- Read depth is only one component of batch or modality variation.
- The objective still depends on an engineered abstraction of sequencing depth rather than a full generative account of all technical noise.
- Strong downstream performance may still rely on cooperating task-specific models after pretraining.

## Sources

- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
