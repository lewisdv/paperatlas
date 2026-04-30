# Evolutionary Contrastive RNA Pretraining

## Definition

- Evolutionary contrastive RNA pretraining is a self-supervised strategy that learns RNA embeddings by maximizing similarity between biologically related transcript pairs, especially splice isoforms and orthologous transcripts.
- In this collection, the idea contrasts with generic masked-token or next-token genomic pretraining by using biological relationships as the main inductive bias.

## In This Collection

- [Orthrus](../entities/Orthrus.md) is the direct example and uses splice isoforms from ten species plus orthologous transcripts from more than `400` mammals as contrastive positives.
- The source argues that these augmentations preserve function better than random sequence variation and therefore structure the latent space more usefully for RNA-property transfer.
- Compared with [Cell-State Similarity Search](cell-state-similarity-search.md), the similarity target here is functional or evolutionary relatedness between transcripts, not nearest-neighbour resemblance between single-cell states.
- Compared with [Cross-modality Generation](cross-modality-generation.md), this concept is sequence-centric and does not try to align multiple assay types into one interchangeable shared latent state.
- Compared with [Single-Cell Generative Pretraining](single-cell-generative-pretraining.md), the pretrained object here is the mature RNA transcript rather than the atlas-scale cell profile.
- Compared with [Cell Sentences](cell-sentences.md), the sequence is a biological RNA sequence with splice and orthology structure, not a language-like serialization of a whole-cell expression profile.

## Claimed Benefits

- Focuses pretraining on function-preserving sequence diversity rather than generic reconstruction.
- Improves parameter efficiency relative to scale-only genomic FM strategies.
- Supports strong low-data transfer for mature RNA property prediction.

## Caveats

- It assumes biological similarity between selected positive pairs, which may not be equally valid for every isoform family.
- The idea is sequence-centric and does not directly address multimodal or cell-state integration.

## Sources

- [Orthrus: toward evolutionary and functional RNA foundation models](../sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md)
