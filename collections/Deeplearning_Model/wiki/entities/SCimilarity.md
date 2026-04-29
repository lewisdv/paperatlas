# SCimilarity

## Type

- Named system / model

## Definition

- SCimilarity is a deep metric-learning foundation model for single-cell profiles.
- The source presents it as a shared representation plus nearest-neighbour retrieval system for finding transcriptionally similar cells across a pan-body human atlas.

## Core Architecture

- The model combines a supervised triplet loss with a reconstruction loss so that similar cell types are close in embedding space while fine-grained expression variation is preserved.
- Triplet supervision is derived from Cell Ontology annotations, with ancestor-descendant label relationships excluded as ambiguous during sampling.
- Querying and annotation operate on precomputed hnswlib nearest-neighbour indices built over large annotated and unannotated references.
- The system also assigns a confidence score that reflects how well a query cell is represented by the training distribution.

## Reported Uses

- Rapid search for similar cell states across `23.4` million reference profiles.
- Cell-type annotation of new datasets without fine-tuning.
- Outlier detection or low-confidence flagging for weakly represented tissues and experimental contexts.
- Linking in vivo disease states to candidate in vitro models, including a validated `3D` hydrogel macrophage system.

## Caveats

- The validated training regime is centered on 10x Chromium scRNA-seq and snRNA-seq data rather than every possible single-cell platform.
- Confidence and annotation quality degrade in tissues or settings that were absent or sparse in the training atlas, especially many in vitro contexts.
- The paper treats SCimilarity as a retrieval and representation model, not as a generative simulator of unseen perturbations.

## Related

- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Source: A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
