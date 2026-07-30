# Multimodal Foundation Models

## Definition

- Multimodal foundation models (MFMs) are large pretrained models that learn shared biological representations across multiple omics modalities and then transfer those representations to many downstream tasks.
- In this collection, the term refers not just to a large model with many inputs, but to a data-centric paradigm that treats genomics, transcriptomics, epigenomics, proteomics, metabolomics, and spatial data as one connected learning problem.

## In This Collection

- The 2025 Cui et al. perspective makes MFMs explicit as an umbrella concept for molecular cell biology and argues that they should unify tokenization, pretraining, cross-modal generation, temporal prediction, and perturbation-response modeling.
- [scGPT](../entities/scGPT.md) and [scFoundation](../entities/scFoundation.md) represent single-cell-heavy foundation-model ingredients that emphasize large-scale pretraining and transfer.
- [AURORA](../entities/AURORA.md) shows a broader human multi-omics generative system that uses a shared latent space to reconstruct missing modalities and support downstream prediction.
- [AIVC](../entities/AIVC.md) extends the idea upward into a field-level roadmap for multi-scale virtual-cell simulation rather than only one molecular foundation model.
- [Multi-Omic Developmental Atlases](multi-omic-developmental-atlases.md) are adjacent but distinct: they supply multimodal biological reference structure even when they are not themselves pretrained foundation models.
- [MIDAS](../entities/MIDAS.md), [GLUE](../entities/GLUE.md), [MultiVI](../entities/MultiVI.md), and [scMODAL](../entities/scMODAL.md) are concrete multimodal integration systems rather than broad foundation models. Together they expose the paired, unpaired, and mosaic data constraints that a future MFM would need to absorb.
- [scMultiMap](../entities/scMultiMap.md) and [scooby](../entities/scooby.md) cover two additional MFM ambitions without unifying the whole agenda: cross-modal regulatory inference and cell-conditioned sequence-to-profile prediction.
- [Baião et al. 2025](../sources/baiao_2025_technical_review_multi-omics_integration_methods.md) places foundation models after a long continuum of classical, probabilistic, network, and deep-generative integration methods. In that review, foundation models are an emerging direction rather than an established default.

## Claimed Benefits

- Supports continuous representations of cell states rather than only discrete labels.
- Reuses one broadly pretrained system across annotation, regulatory inference, modality completion, trajectory analysis, and perturbation prediction.
- Creates a path toward lab-in-the-loop experimentation in which models help prioritize informative next measurements.

## Proposed Technical Ingredients

- Unified tokenization across different molecular resolutions and assay types.
- Hybrid intramodal and intermodal attention so the model can learn both within-modality structure and cross-modality coupling.
- Mixed training objectives spanning masked reconstruction, contrastive pairing, cross-modal prediction, temporal generation, and conditional perturbation tasks.
- Optional integration of structured priors such as pathway or regulatory knowledge graphs plus unstructured literature knowledge.

## Caveats

- The collection currently contains more partial implementations and roadmaps than fully validated end-to-end MFMs.
- Paired multimodal data remain scarce relative to the scale envisioned by the paradigm.
- Unpaired and mosaic methods can reduce the need for cell-level pairing, but they replace it with guidance graphs, feature links, reference datasets, or model assumptions rather than eliminating supervision requirements.
- The review literature still questions where foundation models outperform strong task-specific statistical or machine-learning approaches after accounting for data and compute.
- Interpretability, hallucination control, uncertainty reporting, benchmarking, privacy, and compute access remain central open problems.

## Sources

- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md)
- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
- [Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS](../sources/he_2024_midas_mosaic_integration_knowledge_transfer.md)
- [Multi-omics single-cell data integration and regulatory inference with graph-linked embedding](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- [MultiVI: deep generative model for the integration of multimodal data](../sources/ashuach_2023_multivi_deep_generative_multimodal_integration.md)
- [scMODAL: a general deep learning framework for comprehensive single-cell multi-omics data alignment with feature links](../sources/wang_2025_scmodal_alignment_with_feature_links.md)
- [scMultiMap: Cell-type-specific mapping of enhancers and target genes from single-cell multimodal data](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- [scooby: Modeling multi-modal genomic profiles from DNA sequence at single-cell resolution](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
- [A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches](../sources/baiao_2025_technical_review_multi-omics_integration_methods.md)
