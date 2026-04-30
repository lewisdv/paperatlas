# What does `multimodal` actually mean across this collection?

## Short Answer

- `Multimodal` does not mean one single thing in this collection.
- It currently appears in at least four different senses:
- missing-modality generation from partial inputs
- shared pretrained foundation-model paradigms across assay types
- multi-omic or spatial atlas resources used as reference substrates
- multi-scale virtual-cell roadmaps that extend beyond omics alone

## 1. Multimodal As Missing-Modality Completion

- [Cross-modality Generation](../concepts/cross-modality-generation.md) is the clearest direct example through [AURORA](../entities/AURORA.md).
- Here multimodality means aligning several assay or phenotype types into one latent space so an observed modality can stand in for an unmeasured one.
- The main goal is practical reconstruction and downstream prediction from fragmented human measurements.
- This is the most operational and completion-oriented meaning of `multimodal` in the current collection.

## 2. Multimodal As A Foundation-Model Paradigm

- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md) captures a broader meaning.
- In [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md) and [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md), multimodality is not one decoder trick but a whole pretraining and architecture agenda.
- The emphasis is on unified tokenization, hybrid intramodal and intermodal attention, promptable cross-modal generation, and one shared representation layer across assay types.
- This meaning is broader than AURORA-style completion because it includes annotation, temporal prediction, perturbation modeling, and cross-scale reasoning inside one conceptual umbrella.

## 3. Multimodal As A Reference Substrate

- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md) shows a third meaning.
- In [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md), multimodality means paired transcriptional, epigenetic, and spatial measurements used to reconstruct developmental programs and disease-relevant structure.
- This is not mainly a generative system and not yet a reusable pretrained model family.
- Instead multimodality acts as a high-information biological scaffold that later predictive systems could train against, benchmark against, or use for interpretation.

## 4. Multimodal As Multi-Scale Virtual-Cell Ambition

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md) extends the meaning further.
- In the [AIVC](../entities/AIVC.md) roadmap, multimodality is only one layer inside a bigger multi-scale representation problem spanning molecular, cellular, and multicellular states.
- The goal is not just integrating several omics measurements, but building universal representations and virtual instruments for in silico experimentation.
- This is the broadest and most aspirational use of the word in the current collection.

## What The Collection Supports Right Now

- The collection clearly supports the claim that `multimodal` is being used at different abstraction levels.
- AURORA is the strongest direct example of multimodal completion and downstream prediction.
- Cui 2025 and Khan 2025 are the strongest explicit roadmaps for multimodal foundation-model design.
- To 2024 is the clearest multimodal reference-substrate paper.
- AIVC is the clearest extension from multimodal molecular modeling into a broader virtual-cell agenda.

## What The Collection Does Not Yet Support

- It does not yet support the claim that one end-to-end validated multimodal foundation model has unified all of these meanings in practice.
- The current collection is richer in partial implementations, atlas substrates, and roadmap papers than in one settled multimodal winner.

## Bottom Line

- In this collection, `multimodal` is best read as a family resemblance term rather than a single architecture label.
- Sometimes it means `infer the missing modality`.
- Sometimes it means `pretrain one model across many modalities`.
- Sometimes it means `measure several modalities to build a stronger reference`.
- Sometimes it means `move toward a multi-scale virtual cell`.

## Pages Used

- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md)
- [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md)
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md)
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [AURORA](../entities/AURORA.md)
- [AIVC](../entities/AIVC.md)
