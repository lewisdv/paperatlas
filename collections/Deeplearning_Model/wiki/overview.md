# Overview

This collection now has seventeen deeply ingested anchors and is beginning to connect single-cell generative modeling, atlas-scale generative pretraining, read-depth-aware foundation embeddings, retrieval-style cell atlas foundation models, language-model-based transcriptomic reasoning, lightweight LLM-derived metadata embedding reuse, neural optimal-transport perturbation modeling, combinatorial perturbation generalization, Bayesian RNA-velocity dynamics, reinforcement-learning-based fate-decision analysis, diffusion-based stimulus-response generation, AI-virtual-cell roadmapping, broader multimodal human health modeling, explicit multimodal foundation-model blueprints for molecular cell biology, multiscale transformer architecture proposals, perturbation-atlas roadmaps for causal biology, and perturbation-trained single-cell scaling for oncology. The raw backlog is still much larger than the curated wiki, so the current picture is still early-stage.

## Current Focus

- Conditional and generative modeling for single-cell data.
- Atlas-scale generative pretraining and transfer learning for single-cell omics.
- Read-depth-aware foundation embeddings for lightly adapted downstream use.
- Retrieval-oriented foundation models for pan-body cell-state search and annotation.
- Language-model-based single-cell analysis that treats transcriptomes and biological text as one multimodal token space.
- Lightweight reuse of LLM-generated metadata embeddings as an alternative to heavy end-to-end biological FM pretraining.
- Neural optimal transport for perturbation-response prediction from unpaired single-cell populations.
- Knowledge-graph-guided prediction of unseen combinatorial perturbations and genetic interactions.
- Bayesian RNA-velocity modeling and interpretable temporal module discovery.
- Reinforcement-learning-based trajectory analysis that tries to localize early commitment states rather than only order cells along pseudotime.
- Diffusion-based generation of transient cell states across differentiation, perturbation, drug response, and injury-response settings.
- Multi-scale virtual-cell simulation roadmaps built around shared biological representations and in silico experimentation.
- Cross-modality reconstruction and intervention-aware modeling for broader human multi-omics.
- Explicit multimodal foundation-model blueprints that emphasize unified tokenization, intermodal attention, promptable generation, and lab-in-the-loop iteration.
- Multiscale transformer blueprints that combine modality-specific encoders, shared embedding spaces, and cross-attention across DNA, RNA, spatial, proteomic, image, and text modalities.
- Causal perturbation-atlas roadmaps that treat high-content pooled screens, compressed experimentation, and active-learning loops as foundation-model infrastructure.
- Perturbation-trained scaling strategies that use explicitly interventional pretraining corpora to improve zero-shot or few-shot response prediction in new contexts.
- Current anchor systems: [SAVE](entities/SAVE.md), [scGPT](entities/scGPT.md), [scFoundation](entities/scFoundation.md), [SCimilarity](entities/SCimilarity.md), [C2S-Scale](entities/C2S-Scale.md), [scELMo](entities/scELMo.md), [CellOT](entities/CellOT.md), [GEARS](entities/GEARS.md), [Cell2fate](entities/Cell2fate.md), [scRL](entities/scRL.md), [Squidiff](entities/Squidiff.md), [AIVC](entities/AIVC.md), [AURORA](entities/AURORA.md), and [Tahoe-x1](entities/Tahoe-x1.md).

## Emerging Themes

- Semantically structured representations, such as gene blocks or shared latent spaces, are used to compress biological complexity into model-ready tokens or embeddings.
- Large pretrained atlas models increasingly follow a `pretrain broadly, fine-tune per task` pattern rather than building each single-cell workflow from scratch.
- Some foundation-model work is explicitly trying to factor sequencing depth into pretraining rather than leaving that variation entirely to downstream normalization or integration methods.
- Transcriptomes are increasingly being serialized into language-like sequences so frontier LLM scaling and prompting techniques can be reused for biology.
- Not every FM-like strategy here requires building a monolithic pretrained biological model; some work instead imports semantic priors from external LLMs and combines them with lighter adaptors or downstream models.
- Fast nearest-neighbour retrieval over large pretrained atlases is emerging as a separate foundation-model pattern alongside generation and imputation.
- Perturbation modeling in this collection now spans both generative/token-based approaches and explicit transport-map approaches that try to preserve full response distributions rather than only average shifts.
- Perturbation prediction is also splitting into different inductive-bias families: graph-guided combinatorial extrapolation, transport-based response mapping, diffusion-based state generation, and perturbation-rich large-scale pretraining.
- Some models are explicitly exposing interpretable temporal modules and posterior uncertainty, suggesting that dynamic single-cell modeling is not only about better prediction but also about better inspection of developmental programs.
- This collection now also contains a distinct early-decision-analysis thread: some methods target the localization of commitment pressure before marker expression becomes obvious, rather than focusing only on final fate probabilities or smooth trajectories.
- Diffusion models are emerging here as a practical alternative to VAE, transport, and token-based approaches for reconstructing transient intermediate states and multi-stimulus response paths.
- Some newly ingested sources are moving beyond one-model papers toward field-level design blueprints, arguing that future biology models may need shared representations, modular virtual instruments, and community-scale benchmarking rather than isolated task wins.
- The collection now has a clearer umbrella concept of multimodal foundation models, tying together single-cell pretraining, cross-modality completion, perturbation modeling, and virtual-cell roadmaps into one broader design space.
- The collection now also contains a modular architecture thread, where `Super Transformer`-style proposals treat cross-attention, shared embeddings, and modality-specific tokenizers as a common design language across scales.
- Perturbation modeling is no longer only a downstream task layer in this collection; at least one source now argues that perturbation-rich pretraining data are themselves a key scaling ingredient for transferable causal modeling.
- A second perturbation-roadmap thread is emerging above individual models: perturbation data are being framed as the substrate for a `Perturbation Cell Atlas` that complements observational atlases and spans cell culture, organoids, animal models, and human genetics.
- Missing-data completion is becoming a core model function, either across unseen conditions or across unmeasured modalities.
- Evaluation is moving beyond reconstruction toward downstream utility: cell-state retrieval, large-scale annotation, natural-language interpretation, perturbation response, virtual screening, aging clocks, and disease prediction.

## Collection State

- Seventeen source pages have been deeply ingested so far.
- The normalized raw-source backlog is still large, so future ingests may substantially refine or challenge the current synthesis.
