# Orthrus

## Type

- Named system / model

## Definition

- Orthrus is a mature RNA foundation model that uses biologically motivated contrastive pretraining over splice isoforms and orthologous transcripts.
- The source emphasizes that it is Mamba-based, parameter-efficient, and designed to transfer to mature RNA property prediction tasks.

## Core Architecture

- Uses a Mamba encoder to process mature RNA sequences with linear-memory scaling.
- Constructs positive pairs from alternative splicing and orthology relationships rather than relying only on generic reconstruction.
- Optimizes a decoupled contrastive loss and optionally combines contrastive learning with MLM in one variant.
- Produces fixed-length transcript embeddings that can be linearly probed or fine-tuned for downstream tasks.

## Reported Uses

- Predicting mRNA half-life, localization, translational efficiency, and related mature RNA properties.
- Low-data fine-tuning for property prediction tasks.
- Grouping transcript isoforms by shared function and exposing divergent isoform biology within the same gene.
- Serving as a biologically informed alternative to larger generic genomic foundation models.

## Caveats

- The model is focused on mature RNA sequence properties rather than cell-state or multimodal cellular modeling.
- Its contrastive objective depends on biological assumptions about isoform and ortholog similarity that may not hold uniformly.
- The collection does not yet contain enough parallel RNA-sequence sources to fully benchmark Orthrus against a broader within-collection landscape.

## Related

- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md)
- [Source: Orthrus: toward evolutionary and functional RNA foundation models](../sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md)
