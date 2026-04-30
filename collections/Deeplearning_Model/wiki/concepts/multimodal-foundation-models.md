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
- Interpretability, hallucination control, uncertainty reporting, benchmarking, privacy, and compute access remain central open problems.

## Sources

- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md)
- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
