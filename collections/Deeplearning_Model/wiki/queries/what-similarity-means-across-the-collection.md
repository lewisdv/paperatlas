# What does `similarity` mean across this collection?

## Short Answer

- `Similarity` is not one stable concept in this collection.
- It currently appears in at least five different senses:
- nearest-neighbour resemblance in a learned cell-state embedding
- biologically meaningful positive-pair proximity in RNA sequence space
- shared-latent equivalence across partially observed modalities
- transportable response geometry between source and target cell populations
- fidelity or coverage relative to a primary biological reference

## 1. Similarity As Retrieval In Cell-State Space

- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md) is the clearest example through [SCimilarity](../entities/SCimilarity.md).
- Here similarity means that two cells should lie near each other in a learned embedding because they occupy comparable transcriptional states.
- The goal is retrieval, annotation, and coverage-aware confidence rather than generation or perturbation simulation.

## 2. Similarity As Biologically Chosen Positive Pairs

- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md) uses a different idea through [Orthrus](../entities/Orthrus.md).
- Similarity here is not nearest cell-state resemblance but functional relatedness between transcripts, especially splice isoforms and orthologs chosen as contrastive positives.
- The learned space is therefore organized around biologically motivated sequence relationships rather than around atlas retrieval or multimodal completion.

## 3. Similarity As Shared-Latent Cross-Modal Equivalence

- In [Cross-modality Generation](../concepts/cross-modality-generation.md), especially through [AURORA](../entities/AURORA.md), similarity means that different observed modalities from the same underlying biological condition should map into a shared latent representation.
- The point is not just that two cells or samples are neighbors, but that one modality can stand in for another closely enough to reconstruct missing measurements.
- This is a cross-modal equivalence notion of similarity rather than a retrieval-first or sequence-first one.

## 4. Similarity As Transportable Response Geometry

- [Neural Optimal Transport](../concepts/neural-optimal-transport.md) adds another meaning through [CellOT](../entities/CellOT.md).
- Similarity here concerns whether control and perturbed populations share enough geometry that a minimal-effort transport map can move mass from one to the other in a biologically meaningful way.
- In other words, the important question is not `who is my nearest neighbor?` but `which population geometry can be plausibly transformed into which other one?`

## 5. Similarity As Reference Fidelity And Coverage

- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md), especially through [HNOCA](../entities/HNOCA.md), uses similarity in a more evaluative sense.
- The main question is whether an organoid or modeled system resembles the right primary developmental references closely enough, and where important states are missing or stress-shifted.
- This is system-level fidelity similarity, not an embedding objective baked into one foundation model.

## What The Collection Supports Right Now

- The collection clearly supports the claim that `similarity` is doing different conceptual jobs across papers.
- SCimilarity treats it as retrieval utility.
- Orthrus treats it as biologically curated contrastive proximity.
- AURORA treats it as latent alignment across modalities.
- CellOT treats it as transformable source-target geometry.
- HNOCA treats it as fidelity to a primary reference space.

## What The Collection Does Not Yet Support

- The current knowledge base does not support collapsing these into one benchmark metric or one universal embedding story.
- It also does not support claiming that success in one similarity sense automatically transfers to the others.

## Bottom Line

- In this collection, `similarity` is best read as a family of related but non-interchangeable ideas.
- A paper can be strong at one form of similarity while contributing little to the others.
- Keeping those senses separate helps prevent over-reading retrieval models as simulators, sequence models as cell-state atlases, or atlas-fidelity tools as general generative systems.

## Pages Used

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [Orthrus: toward evolutionary and functional RNA foundation models](../sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md)
- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [SCimilarity](../entities/SCimilarity.md)
- [Orthrus](../entities/Orthrus.md)
- [AURORA](../entities/AURORA.md)
- [CellOT](../entities/CellOT.md)
- [HNOCA](../entities/HNOCA.md)
