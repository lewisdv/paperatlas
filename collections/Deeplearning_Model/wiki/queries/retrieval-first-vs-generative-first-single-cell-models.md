# How should this collection distinguish retrieval-first and generative-first single-cell models?

## Short Answer

- This collection supports a useful split between `retrieval-first` and `generative-first` single-cell models, even though some papers sit between the two poles.
- Retrieval-first models mainly ask `which known biological state is most similar to this query?`
- Generative-first models mainly ask `what missing, perturbed, integrated, or interpretable state should be predicted from this input?`
- In this collection, [SCimilarity](../entities/SCimilarity.md) is the clearest retrieval-first system, while [scGPT](../entities/scGPT.md) and [C2S-Scale](../entities/C2S-Scale.md) are the clearest generative-first branches. [scFoundation](../entities/scFoundation.md) sits somewhat in between as a reusable embedding foundation layer rather than a pure nearest-neighbour system or an open-ended generator.

## 1. Retrieval-First: SCimilarity

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md) frames the main problem as atlas-scale lookup of transcriptionally similar cells.
- Through [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md), the core act is embedding a query, searching a large reference, and returning traceable neighbors with tissue, study, and disease provenance.
- The output is therefore bounded by what exists in the reference atlas, and uncertainty appears as low representation confidence when the query sits outside strong coverage.

## 2. Generative-First: scGPT

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md) takes a different stance.
- Through [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md), one pretrained model is adapted to annotation, integration, perturbation prediction, and gene-network analysis.
- The model is not mainly trying to find an already known nearest state. It is trying to learn representations that can support many downstream predictions after task-specific fine-tuning.

## 3. Generative-First In A More Language-Native Form: C2S-Scale

- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md) pushes the generative side further.
- Through [Cell Sentences](../concepts/cell-sentences.md), whole-cell transcriptomes become language-like sequences that can be mixed with metadata and biological text in one token space.
- This enables not only annotation and perturbation prediction, but also dataset interpretation, question answering, and virtual screening.
- Compared with retrieval-first systems, the outputs are broader and more open-ended, which also means the paper explicitly worries more about hallucination and biological guardrails.

## 4. The Middle Case: scFoundation

- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md) is not best read as a pure retrieval-first or pure open-ended generative system.
- Through [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md), it behaves more like a reusable feature layer trained to make cell embeddings robust to sequencing-depth variation.
- In this collection, scFoundation is therefore a strong `foundation-layer` example: it supports many downstream tasks, but often through embeddings and cooperating task-specific models rather than by turning the base model directly into a nearest-neighbour search engine or a language-style generator.

## 5. What The Split Changes In Practice

- Retrieval-first models are strongest when the task is reference lookup, model finding, or provenance-aware annotation under known atlas coverage.
- Generative-first models are stronger when the task involves perturbation prediction, missing-state completion, multimodal integration, or open-ended interpretation.
- Retrieval-first behavior is usually easier to trace back to observed biology because returned neighbors come from an explicit reference set.
- Generative-first behavior is broader and often more powerful, but its success depends more heavily on pretraining design, fine-tuning objectives, and task-specific evaluation.

## What The Collection Supports Right Now

- The collection clearly supports treating SCimilarity as the canonical retrieval-first example.
- It supports treating scGPT and C2S-Scale as generative-first models, though with different representational languages.
- It supports treating scFoundation as a foundation-layer system that overlaps with the generative branch but is best understood through robust embeddings and depth-aware pretraining rather than through open-ended generation alone.

## What The Collection Does Not Yet Support

- The current knowledge base does not support a claim that retrieval-first models are uniformly better or worse than generative-first models.
- It also does not support collapsing annotation, perturbation prediction, atlas lookup, and biological question answering into one single benchmark axis.

## Bottom Line

- In this collection, retrieval-first models answer `what already known state is closest?`
- Generative-first models answer `what state, label, or effect should be produced from this input?`
- The distinction helps keep atlas search, robust embeddings, perturbation prediction, and language-native biological generation from being treated as if they were all the same kind of model behavior.

## Pages Used

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)
- [Cell Sentences](../concepts/cell-sentences.md)
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [SCimilarity](../entities/SCimilarity.md)
- [scGPT](../entities/scGPT.md)
- [scFoundation](../entities/scFoundation.md)
- [C2S-Scale](../entities/C2S-Scale.md)
