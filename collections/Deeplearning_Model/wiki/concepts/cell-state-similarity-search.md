# Cell-State Similarity Search

## Definition

- Cell-state similarity search is the task of retrieving transcriptionally similar cells from a large reference atlas using a learned representation and nearest-neighbour search.
- In this collection, the SCimilarity paper frames it as a scalable alternative to ad hoc gene-signature scans or per-dataset retraining.

## In SCimilarity

- A query can be either an individual cell profile or a centroid representing a target state.
- The query is embedded into the shared latent space and compared against precomputed nearest-neighbour indices over annotated or full-reference cells.
- Results remain traceable to original study, tissue, and disease metadata, which lets the search output function as both retrieval and hypothesis-generation support.

## Claimed Benefits

- Makes cross-study, cross-tissue cell-state retrieval feasible at atlas scale.
- Reuses one representation for annotation, confidence scoring, and biological model discovery rather than training separate task-specific models.
- Retrieves fibrosis-associated macrophage and myofibroblast states more faithfully than the paper's compared single-cell foundation models on the reported benchmarks.

## Caveats

- Search quality depends on how well the reference atlas covers the queried biology.
- Low-confidence outputs are more common in underrepresented tissues and in vitro settings.
- Similarity retrieval is not the same task as batch correction or generative prediction, so performance should not be conflated across those use cases.

## Sources

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
