# What does `multimodal` actually mean across this collection?

## Short Answer

- `Multimodal` does not mean one single thing in this collection.
- It now appears in at least eight operationally different senses:
  - integration under paired, unpaired, or mosaic measurement regimes
  - missing-modality generation from partial inputs
  - guidance-graph or feature-link-based alignment and regulatory inference
  - paired feature-feature association testing
  - DNA-sequence-conditioned prediction of several cell-specific profiles
  - shared pretrained foundation-model paradigms across assay types
  - multi-omic or spatial atlas resources used as reference substrates
  - multi-scale virtual-cell roadmaps that extend beyond omics alone

## 1. Multimodal As A Data-Integration Regime

- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md) separates `vertical` paired measurements, `diagonal` unpaired datasets with distinct feature spaces, and `mosaic` mixtures of paired and single-modality blocks.
- [MultiVI](../entities/MultiVI.md) is anchored by paired cells and extends that latent representation to single-modality cells.
- [MIDAS](../entities/MIDAS.md) targets flexible RNA/ATAC/ADT mosaic blocks.
- [GLUE](../entities/GLUE.md) and [scMODAL](../entities/scMODAL.md) align fully unpaired modalities, but GLUE uses a signed regulatory guidance graph whereas scMODAL constructs cross-modal cell anchors from linked features.
- Here `multimodal` is first a statement about which correspondences were measured and which assumptions must replace the missing correspondences.

## 2. Multimodal As Missing-Modality Completion

- [Cross-modality Generation](../concepts/cross-modality-generation.md) is the clearest direct example through [AURORA](../entities/AURORA.md).
- Here multimodality means aligning several assay or phenotype types into one latent space so an observed modality can stand in for an unmeasured one.
- MultiVI, MIDAS, and scMODAL bring the same completion goal into single-cell multi-omics, but with paired-reference, mosaic-block, and feature-link-guided supervision respectively.
- The important boundary is that reconstructed RNA, accessibility, protein, or phenotype values are model estimates rather than newly observed measurements.

## 3. Multimodal As Alignment Plus Regulatory Inference

- [GLUE](../entities/GLUE.md) uses a graph linking features across modalities to orient unpaired cell spaces, then derives peak-gene or TF-target scores from feature embeddings.
- [scMODAL](../entities/scMODAL.md) uses a smaller set of positive feature links to form mutual-nearest-neighbour cell anchors and can derive cross-modal feature relations after alignment.
- In this sense, multimodality is not only about producing a shared cell embedding: cross-modal structure is also used to propose regulatory relationships.
- The inferred relationships remain sensitive to the prior graph or feature links and do not by themselves establish causality.

## 4. Multimodal As Paired Feature-Feature Inference

- [scMultiMap](../entities/scMultiMap.md) is not primarily an integration model.
- It requires paired RNA and ATAC counts in the same cells and tests cell-type-specific peak-gene covariance while adjusting for sequencing depth and subject effects.
- Here multimodality supplies paired evidence for an analytic association test rather than a shared latent space or a missing-data decoder.
- See [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md) for why association, embedding similarity, and sequence perturbation have different evidential meanings.

## 5. Multimodal As Sequence-Conditioned Multiple Profiles

- [scooby](../entities/scooby.md) starts from DNA sequence and a continuous cell embedding, then predicts both single-cell RNA coverage and ATAC insertion profiles.
- Multimodality here names multiple cell-specific outputs from a shared sequence representation, not the integration of independently sampled assay datasets.
- Its motif deletion and variant-effect predictions connect sequence, accessibility, and expression, but remain in silico hypotheses.
- See [Sequence-to-Single-Cell Profile Modeling](../concepts/sequence-to-single-cell-profile-modeling.md).

## 6. Multimodal As A Foundation-Model Paradigm

- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md) captures a broader meaning.
- In [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md) and [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md), multimodality is not one decoder trick but a whole pretraining and architecture agenda.
- The emphasis is on unified tokenization, hybrid intramodal and intermodal attention, promptable cross-modal generation, and one shared representation layer across assay types.
- This meaning is broader than the six concrete methods above because it treats integration, generation, annotation, perturbation modeling, and cross-scale reasoning as parts of one pretraining agenda.

## 7. Multimodal As A Reference Substrate

- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md) shows a third meaning.
- In [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md), multimodality means paired transcriptional, epigenetic, and spatial measurements used to reconstruct developmental programs and disease-relevant structure.
- This is not mainly a generative system and not yet a reusable pretrained model family.
- Instead multimodality acts as a high-information biological scaffold that later predictive systems could train against, benchmark against, or use for interpretation.

## 8. Multimodal As Multi-Scale Virtual-Cell Ambition

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md) extends the meaning further.
- In the [AIVC](../entities/AIVC.md) roadmap, multimodality is only one layer inside a bigger multi-scale representation problem spanning molecular, cellular, and multicellular states.
- The goal is not just integrating several omics measurements, but building universal representations and virtual instruments for in silico experimentation.
- This is the broadest and most aspirational use of the word in the current collection.

## What The Collection Supports Right Now

- The collection clearly supports the claim that `multimodal` is being used at different abstraction levels.
- MIDAS, GLUE, MultiVI, and scMODAL provide concrete but differently supervised implementations of single-cell multimodal integration.
- AURORA, MIDAS, MultiVI, and scMODAL make missing-modality completion operational at different biological scales and under different pairing assumptions.
- GLUE, scMultiMap, and scooby show three distinct routes from multimodal data toward regulatory hypotheses: graph-linked embedding similarity, paired count association, and sequence perturbation.
- Cui 2025 and Khan 2025 are the strongest explicit roadmaps for multimodal foundation-model design.
- To 2024 is the clearest multimodal reference-substrate paper.
- AIVC is the clearest extension from multimodal molecular modeling into a broader virtual-cell agenda.

## What The Collection Does Not Yet Support

- It does not yet support the claim that one end-to-end validated multimodal foundation model has unified all of these meanings in practice.
- It also does not support treating latent alignment, imputation accuracy, enhancer-gene association, and causal sequence effects as interchangeable forms of evidence.
- The collection is richer in task-specific implementations, atlas substrates, and roadmap papers than in one settled multimodal winner.

## Bottom Line

- In this collection, `multimodal` is best read as a family resemblance term rather than a single architecture label.
- Sometimes it means `align cells despite missing pairings`.
- Sometimes it means `infer the missing modality`.
- Sometimes it means `infer cross-modal regulatory relationships`.
- Sometimes it means `predict multiple profiles from sequence`.
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
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [Sequence-to-Single-Cell Profile Modeling](../concepts/sequence-to-single-cell-profile-modeling.md)
- [AURORA](../entities/AURORA.md)
- [AIVC](../entities/AIVC.md)
- [MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- [GLUE](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- [MultiVI](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
- [scMODAL](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
- [scMultiMap](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- [scooby](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
