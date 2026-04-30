# How does this collection distinguish sequence foundation models from cell-state foundation models?

## Short Answer

- This collection uses `foundation model` for at least two different biological objects.
- [Orthrus](../entities/Orthrus.md) is a sequence foundation model: it pretrains over mature RNA transcript sequences and transfers to transcript-property tasks.
- [scGPT](../entities/scGPT.md), [scFoundation](../entities/scFoundation.md), [C2S-Scale](../entities/C2S-Scale.md), and [SCimilarity](../entities/SCimilarity.md) are cell-state-oriented models: they learn from whole-cell transcriptomic profiles or atlas states and transfer to annotation, retrieval, perturbation, or integration tasks.

## 1. Sequence Foundation Model: Orthrus

- [Orthrus: toward evolutionary and functional RNA foundation models](../sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md) is the clearest sequence branch in this collection.
- Through [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md), it treats the basic pretrained object as a mature RNA transcript sequence.
- Its contrastive positives come from splice isoforms and orthologous transcripts, and its downstream targets are mature RNA properties such as half-life, localization, translational efficiency, and isoform function.
- In other words, the learned representation is organized around sequence-level functional similarity, not around cell identity, tissue context, or atlas-scale state neighborhoods.

## 2. Cell-State Foundation Models: scGPT, scFoundation, C2S-Scale, and SCimilarity

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md) and [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md) represent the clearest atlas-pretraining branch.
- scGPT pretrains over millions of normal human cells and then fine-tunes for annotation, integration, perturbation prediction, and gene-regulatory analysis.
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md) and [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md) keep the same cell-profile focus but make sequencing-depth variation part of the pretraining target.
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md) and [Cell Sentences](../concepts/cell-sentences.md) remain cell-state-oriented too, even though they borrow language-model infrastructure by serializing whole cells into ranked gene-token sequences.
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md) pushes the same broad branch in a retrieval-first direction through [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md): the object is still the cell state, but the main downstream act is atlas retrieval rather than generative transfer.

## 3. What Changes When The Pretrained Object Changes

- Sequence models and cell-state models differ not only in architecture but in what counts as one training example.
- For Orthrus, one example is a transcript sequence, and good transfer means recovering mature RNA properties from sequence-informed embeddings.
- For scGPT, scFoundation, C2S-Scale, and SCimilarity, one example is a cell profile or atlas query state, and good transfer means annotation, integration, perturbation prediction, retrieval, or biological interpretation.
- This difference also changes what kinds of context matter: Orthrus emphasizes evolutionary and splice-related biological relationships, whereas the cell-state models emphasize atlas diversity, batch or depth handling, cell-state neighborhoods, and perturbational or textual context.

## 4. What The Collection Supports Right Now

- The collection clearly supports treating sequence foundation models and cell-state foundation models as parallel branches rather than one unified benchmark class.
- Orthrus extends the collection outward from single-cell atlas modeling into mature RNA sequence modeling.
- scGPT and scFoundation are the strongest reusable atlas-pretraining examples.
- C2S-Scale shows a language-native reformulation of the cell-state branch.
- SCimilarity shows that a cell-state foundation model can be retrieval-first rather than generative-first.

## What The Collection Does Not Yet Support

- The current knowledge base does not support putting Orthrus on the same simple leaderboard as scGPT or scFoundation, because their pretrained objects and downstream targets are different.
- It also does not support the claim that success on cell-state tasks such as atlas retrieval or perturbation prediction automatically implies strong transfer on mature RNA sequence-property tasks, or the reverse.

## Bottom Line

- In this collection, `foundation model` is not one homogeneous category.
- Some papers pretrain over transcript sequences.
- Others pretrain or index over whole-cell states.
- The key distinction is therefore not only model size or architecture, but what biological object the model is actually trying to represent and transfer.

## Pages Used

- [Orthrus: toward evolutionary and functional RNA foundation models](../sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md)
- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)
- [Cell Sentences](../concepts/cell-sentences.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Orthrus](../entities/Orthrus.md)
- [scGPT](../entities/scGPT.md)
- [scFoundation](../entities/scFoundation.md)
- [C2S-Scale](../entities/C2S-Scale.md)
- [SCimilarity](../entities/SCimilarity.md)
