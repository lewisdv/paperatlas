# How do virtual-cell roadmaps differ from multimodal foundation-model roadmaps in this collection?

## Short Answer

- In this collection, `virtual-cell roadmap` and `multimodal foundation-model roadmap` are overlapping but not identical ideas.
- The virtual-cell side, led by [AIVC](../entities/AIVC.md), is broader in biological ambition: it wants one reusable state space plus instruments for simulation, intervention, and scientific interaction across molecular, cellular, and multicellular scales.
- The multimodal foundation-model side, led by [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md) and [Super Transformer Architecture](../concepts/super-transformer-architecture.md), is more concrete about tokenization, fusion, and pretraining patterns across assay types.

## 1. What The Virtual-Cell Roadmap Emphasizes

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md) frames the main problem around [Universal Representation](../concepts/universal-representation.md) and [Virtual Instruments](../concepts/virtual-instruments.md).
- The key idea is that many downstream acts such as decoding labels, predicting readouts, simulating perturbations, or planning experiments should all operate over one reusable biological state representation.
- This roadmap is explicitly multi-scale: it spans molecular, cellular, and multicellular levels rather than staying only inside one omics layer.
- The design center is scientific capability and in silico experimentation, not only a better encoder backbone.

## 2. What The Multimodal Foundation-Model Roadmap Emphasizes

- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md) and [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md) put more weight on architecture and pretraining strategy.
- Their design language revolves around unified tokenization, modality-specific encoders, shared embeddings, intermodal attention, contrastive alignment, multitask heads, and large heterogeneous corpora.
- The [Super Transformer Architecture](../concepts/super-transformer-architecture.md) page is especially explicit about this side of the roadmap.
- In other words, this branch answers more of the question `how should we build the model stack?`

## 3. Where They Overlap

- Both roadmaps want shared representations rather than isolated specialist models.
- Both expect cross-modal completion, perturbation reasoning, and iterative lab-in-the-loop workflows to matter.
- Both see current single-cell systems such as [scGPT](../entities/scGPT.md), [scFoundation](../entities/scFoundation.md), [C2S-Scale](../entities/C2S-Scale.md), and [AURORA](../entities/AURORA.md) as partial ingredients rather than complete solutions.

## 4. Where They Diverge

- The virtual-cell agenda is broader in scientific end state.
- It explicitly asks for reusable instruments that can decode, manipulate, and query one latent biological world model.
- The multimodal foundation-model agenda is narrower but more operational in architecture terms.
- It is usually more specific about tokenizers, fusion operators, attention structure, and pretraining tasks.
- Put differently: AIVC is closer to `what kind of virtual scientific system do we want`, while Super Transformer and MFM papers are closer to `what model family and training recipe might get us there`.

## 5. How To Read Current Collection Papers Through This Split

- [AURORA](../entities/AURORA.md) looks closer to the multimodal completion and shared-latent side of the MFM agenda.
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md), [scGPT](../entities/scGPT.md), and [scFoundation](../entities/scFoundation.md) contribute narrower foundation-model ingredients but do not yet realize the full virtual-instrument vision.
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md) and [Neural Optimal Transport](../concepts/neural-optimal-transport.md) can be read as local manipulator-like behaviors, but only inside limited perturbation or trajectory tasks.

## Collection-Level Conclusion

- The current knowledge base does not support treating `virtual cell` and `multimodal foundation model` as interchangeable phrases.
- It does support a layered reading:
- multimodal foundation-model roadmaps are architectural and pretraining blueprints
- virtual-cell roadmaps are broader systems visions that also require interfaces, instruments, simulation behavior, and cross-scale coherence

## Bottom Line

- In this collection, AIVC is the broader scientific ambition.
- Multimodal foundation-model and Super Transformer papers provide more concrete modeling blueprints that could become part of that larger ambition.
- The relation is therefore best read as `MFM roadmaps may be ingredients for a virtual-cell program`, not as one-to-one synonyms.

## Pages Used

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md)
- [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md)
- [Universal Representation](../concepts/universal-representation.md)
- [Virtual Instruments](../concepts/virtual-instruments.md)
- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [Super Transformer Architecture](../concepts/super-transformer-architecture.md)
- [AIVC](../entities/AIVC.md)
- [AURORA](../entities/AURORA.md)
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
