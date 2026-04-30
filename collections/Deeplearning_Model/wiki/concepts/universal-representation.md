# Universal Representation

## Definition

- In this collection, universal representation refers to a shared embedding of biological state that is intended to work across species, modalities, datasets, contexts, and physical scales.
- The AIVC paper treats this shared representation as the core substrate on which prediction, simulation, and experimental querying are built.

## In AIVC

- The AIVC maps biological data into UR spaces that span molecular, cellular, and multicellular scales.
- These embeddings are intended to be modality-agnostic enough that the same biological entity can be represented consistently from different measurement technologies.
- URs are also intended to generalize to previously unseen cell states, perturbations, or contexts and to act as the common interface for decoder and manipulator virtual instruments.
- Compared with [Multimodal Foundation Models](multimodal-foundation-models.md), universal representation is the broader state-space ambition behind many possible models rather than one pretraining recipe or model family.
- Compared with [Super Transformer Architecture](super-transformer-architecture.md), the focus here is not a concrete tokenizer-and-fusion stack but the desired biological latent state that a future architecture would need to support across scales.

## Claimed Benefits

- Makes it possible to compare and align biological state across assays, scales, and contexts.
- Provides a shared latent substrate for cross-modal reconstruction, perturbation prediction, and active data collection.
- Recasts many downstream tasks as operations over one reusable biological state space rather than as isolated single-task models.

## Caveats

- The source stresses that URs must remain self-consistent across contexts, scales, and modalities, which is a demanding unresolved requirement rather than a solved property.
- Strong generalization depends on broad, diverse, and well-calibrated training data and on benchmarks that test biologically meaningful extrapolation.
- A highly compressed shared representation may improve utility while still leaving interpretability and causal understanding incomplete.

## Sources

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
