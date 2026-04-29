# Index

## Overview

- [Overview](overview.md) - top-level summary of the current collection.

## Sources

- [SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](sources/li_2026_save_a_generalizable_framework_for.md) - ICLR 2026 paper on gene block attention, conditional flow matching, and multi-condition scRNA-seq generation.
- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](sources/chen_2026_a_generative_ai_framework_unifies.md) - Cell Metabolism 2026 paper on AURORA, multimodal aging clocks, disease prediction, and perturbation-aware health modeling.
- [A cell atlas foundation model for scalable search of similar human cells](sources/heimberg_2025_a_cell_atlas_foundation_model.md) - Nature paper on SCimilarity, metric-learning-based cell-state retrieval, large-scale annotation, and confidence-aware atlas search.
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](sources/rizvi_2025_scaling_large_language_models_for.md) - 2025 preprint on C2S-Scale, cell sentences, multimodal LLM training, perturbation prediction, and natural-language single-cell reasoning.
- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](sources/cui_2024_scgpt_toward_building_a_foundation.md) - Nature Methods paper on generative pretraining over 33 million cells for annotation, integration, perturbation prediction, and gene-network inference.
- [Large-scale foundation model on single-cell transcriptomics](sources/hao_2024_large-scale_foundation_model_on_single-cell.md) - Nature Methods paper on scFoundation, read-depth-aware pretraining, large-scale embeddings, and broad downstream transfer.
- [Learning single-cell perturbation responses using neural optimal transport](sources/bunne_2023_learning_single-cell_perturbation_responses_using.md) - Nature Methods paper on CellOT, neural optimal transport, unpaired perturbation-response prediction, and generalization across patients, species, and developmental settings.
- [Cell2fate infers RNA velocity modules to improve cell fate prediction](sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md) - Nature Methods paper on Bayesian RNA velocity, interpretable module decomposition, uncertainty-aware fate inference, and spatial mapping of transcriptional dynamics.
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](sources/bunne_2024_how_to_build_the_virtual.md) - Cell perspective on AI virtual cells, universal representations, virtual instruments, and a collaborative roadmap for multi-scale biological simulation.
- [Towards multimodal foundation models in molecular cell biology](sources/cui_2025_towards_multimodal_foundation_models_in.md) - Perspective on multimodal foundation models, unified tokenization, lab-in-the-loop workflows, and promptable cross-modal biology modeling.
- [Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters](sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md) - Preprint on perturbation-rich single-cell foundation-model scaling, oncology-focused benchmarks, and compute-efficient training to 3B parameters.
- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md) - Biology paper on actor-critic trajectory analysis, early fate-decision localization, and regulator discovery in single-cell systems.
- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](sources/he_2025_squidiff_predicting_cellular_development_and.md) - Nature Methods paper on conditional diffusion modeling for development, perturbation response, drug screening, and organoid injury dynamics.
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md) - Nature Biotechnology paper on knowledge-graph-guided prediction of unseen multigene perturbations and genetic interaction ranking.
- [scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis](sources/liu_2023_scelmo_embeddings_from_language_models.md) - Manuscript on GPT-derived metadata embeddings, zero-shot single-cell analysis, and lightweight adaptor-based downstream modeling.
- [Multimodal foundation transformer models for multiscale genomics](sources/khan_2025_multimodal_foundation_transformer_models_for.md) - paper source queued for ingest.
## Entities

- [SAVE](entities/SAVE.md) - Single-cell Gene Block Attention-based Variational gEnerative framework for conditional scRNA-seq modeling.
- [AURORA](entities/AURORA.md) - Generative framework for unifying fragmented multi-omics and phenotypic data into shared digital human representations.
- [SCimilarity](entities/SCimilarity.md) - Metric-learning foundation model for pan-body retrieval of transcriptionally similar cells.
- [C2S-Scale](entities/C2S-Scale.md) - LLM family that treats transcriptomes as language-like sequences for multimodal single-cell analysis.
- [scGPT](entities/scGPT.md) - Generative pretrained transformer foundation model for single-cell omics and transfer learning across downstream tasks.
- [scFoundation](entities/scFoundation.md) - Large read-depth-aware foundation model for transcriptomic embeddings and lightweight downstream transfer.
- [CellOT](entities/CellOT.md) - Neural optimal transport model for predicting perturbation responses from unpaired single-cell populations.
- [Cell2fate](entities/Cell2fate.md) - Fully Bayesian RNA-velocity model with interpretable dynamic modules and posterior uncertainty estimates.
- [AIVC](entities/AIVC.md) - Proposed AI virtual cell framework for multi-scale, multi-modal biological representation and simulation.
- [Tahoe-x1](entities/Tahoe-x1.md) - Perturbation-trained single-cell foundation model family scaled to 3B parameters for oncology-focused functional genomics.
- [scRL](entities/scRL.md) - Actor-critic reinforcement-learning framework for identifying early fate-decision states in single-cell trajectories.
- [Squidiff](entities/Squidiff.md) - Conditional diffusion model for transcriptomic state transitions under development, perturbation, and environmental stimuli.
- [GEARS](entities/GEARS.md) - Knowledge-graph-guided model for predicting unseen single-gene and multigene perturbation responses.
- [scELMo](entities/scELMo.md) - Pipeline that reuses GPT-derived biological metadata embeddings for zero-shot and adaptor-based single-cell analysis.

## Concepts

- [Gene Block Attention](concepts/gene-block-attention.md) - Coarse-grained attention over semantically clustered gene blocks.
- [Cross-modality Generation](concepts/cross-modality-generation.md) - Reconstructing missing biological modalities from observed inputs via a shared latent space.
- [Cell-State Similarity Search](concepts/cell-state-similarity-search.md) - Retrieval of transcriptionally similar cells from a large reference atlas using learned embeddings.
- [Cell Sentences](concepts/cell-sentences.md) - Serializing transcriptomes into ranked gene-token sequences so standard LLMs can operate on them.
- [Single-Cell Generative Pretraining](concepts/single-cell-generative-pretraining.md) - Pretraining large generative models on cell atlases before adapting them to multiple single-cell tasks.
- [Read-Depth-Aware Pretraining](concepts/read-depth-aware-pretraining.md) - Pretraining that explicitly models sequencing-depth variation with source and target count indicators.
- [Neural Optimal Transport](concepts/neural-optimal-transport.md) - Learning perturbation maps between unpaired cell-state distributions by parameterizing optimal transport with neural networks.
- [RNA Velocity Modules](concepts/rna-velocity-modules.md) - Interpretable dynamic programs derived from RNA-velocity modeling over spliced and unspliced counts.
- [Universal Representation](concepts/universal-representation.md) - Shared biological state embedding intended to align modalities, contexts, and physical scales.
- [Virtual Instruments](concepts/virtual-instruments.md) - Decoder and manipulator networks that operate on universal biological representations.
- [Multimodal Foundation Models](concepts/multimodal-foundation-models.md) - Shared pretrained biological models that span multiple omics modalities and downstream tasks.
- [Perturbation-Trained Foundation Models](concepts/perturbation-trained-foundation-models.md) - Foundation models whose pretraining corpus is explicitly enriched with intervention data.
- [Fate Decision Intensity](concepts/fate-decision-intensity.md) - A model-derived score for early commitment pressure before overt lineage commitment.
- [Stimulus-Response Diffusion Modeling](concepts/stimulus-response-diffusion-modeling.md) - Conditional diffusion-based generation of transcriptomic state changes under stimuli.
- [Combinatorial Perturbation Generalization](concepts/combinatorial-perturbation-generalization.md) - Predicting unseen multigene intervention effects beyond directly observed perturbation combinations.
- [LLM-Derived Feature Embeddings](concepts/llm-derived-feature-embeddings.md) - Reusing LLM-generated biological descriptions and their embeddings as feature priors.

## Queries

## Syntheses
