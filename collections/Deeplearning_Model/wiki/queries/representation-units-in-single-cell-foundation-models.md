# How do the main single-cell foundation-model papers in this collection differ in their basic representation units?

## Short Answer

- The main single-cell model papers in this collection do not only differ by scale or downstream task.
- They also disagree on what the basic thing to represent is.
- The current knowledge base shows at least six distinct representation choices: semantically grouped gene blocks, genes plus expression and condition tokens, ranked cell sentences, read-depth-aware whole-expression modeling, external semantic feature embeddings, and retrieval-oriented cell embeddings.

## 1. Gene Blocks As The Basic Unit

- [SAVE](../entities/SAVE.md) is the clearest example through [Gene Block Attention](../concepts/gene-block-attention.md).
- It does not treat each gene as a fully independent token. Instead it groups genes into equal-sized semantic blocks built from NCBI summary embeddings and optimal-transport assignment.
- This choice tries to make higher-order biological modules part of the tokenization itself.
- Tradeoff: the representation depends on text coverage and can inherit literature bias for poorly characterized genes.

## 2. Genes Plus Expression And Condition Tokens

- [scGPT](../entities/scGPT.md) is the clearest example of this family through [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md).
- The model keeps genes as tokens but augments them with expression values and condition tokens such as batch, modality, or perturbation context.
- This preserves a relatively direct link to original expression structure while still fitting a transformer-style generative recipe.
- Tradeoff: because gene-expression profiles are not naturally sequential, the paper needs a specially engineered attention mask to make the autoregressive analogy work.

## 3. Ranked Cell Sentences

- [C2S-Scale](../entities/C2S-Scale.md) uses [Cell Sentences](../concepts/cell-sentences.md), where the top expressed genes are rank-ordered and serialized into one language-like sequence.
- The advantage is that transcriptomes, metadata, papers, and biological text can all live in one token space.
- This is the most language-native representation currently in the collection.
- Tradeoff: rank order is an engineered linearization, so causal attention over token order may not map well onto true biological dependency structure.

## 4. Read-Depth-Aware Whole-Expression Modeling

- [scFoundation](../entities/scFoundation.md) is the clearest example through [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md).
- Rather than language-style serialization, it keeps the representation close to the original expression matrix and explicitly conditions on source and target total counts `S` and `T`.
- The important claim is that technical depth variation should be part of the representation problem, not only a preprocessing nuisance.
- Tradeoff: this representation is strong for harmonization and enhancement, but it is less obviously unified with natural-language reasoning than cell-sentence models.

## 5. External Semantic Feature Embeddings

- [scELMo](../entities/scELMo.md) represents a different strategy through [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md).
- It does not train a large biological foundation model directly on transcriptomes. Instead it asks a general LLM to summarize genes or metadata, embeds those descriptions, and aggregates them into cell-level features.
- This makes the semantic prior external to the model rather than inside a newly pretrained end-to-end architecture.
- Tradeoff: the approach is lighter and cheaper, but it depends on outside LLM behavior and its gains are less uniform across tasks than the strongest dedicated pretrained models.

## 6. Retrieval Embeddings For Cell-State Search

- [SCimilarity](../entities/SCimilarity.md) takes a sixth route through [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md).
- Its main representation goal is not generation or reconstruction but embedding cells so biologically similar states become nearest neighbours in a very large atlas.
- This makes the latent space itself the product, because retrieval, annotation, and confidence scoring all operate on that shared embedding.
- Tradeoff: the representation is powerful for search and transfer, but it is not designed as a direct generator of unseen perturbation or developmental states.

## Cross-Collection Pattern

- These representation choices track different ambitions.
- SAVE and scGPT try to make generation or conditional modeling easier by structuring the tokenization.
- C2S-Scale pushes hardest toward unifying transcriptomes with natural language.
- scFoundation pushes hardest toward making technical count variation part of the foundation layer.
- scELMo pushes toward low-cost semantic reuse from external LLMs.
- SCimilarity pushes toward reference retrieval rather than open-ended generation.

## Bottom Line

- The most important difference among these papers is not simply `which model is bigger`.
- It is `what they think a cell should look like to the model`.
- In this collection, the representation unit is already a major fork in design philosophy, and many downstream tradeoffs follow directly from that choice.

## Pages Used

- [SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](../sources/li_2026_save_a_generalizable_framework_for.md)
- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](../sources/rizvi_2025_scaling_large_language_models_for.md)
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
- [scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis](../sources/liu_2023_scelmo_embeddings_from_language_models.md)
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [Gene Block Attention](../concepts/gene-block-attention.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Cell Sentences](../concepts/cell-sentences.md)
- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)
- [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
