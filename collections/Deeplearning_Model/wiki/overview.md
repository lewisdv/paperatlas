# Overview

This collection now has twenty-three deeply ingested anchors and is beginning to connect single-cell generative modeling, atlas-scale generative pretraining, read-depth-aware foundation embeddings, retrieval-style cell atlas foundation models, language-model-based transcriptomic reasoning, lightweight LLM-derived metadata embedding reuse, uncertainty-aware hierarchical annotation, neural optimal-transport perturbation modeling, Gaussian-process-based perturbation regression, biologically motivated mature-RNA foundation modeling, combinatorial perturbation generalization, Bayesian RNA-velocity dynamics, reinforcement-learning-based fate-decision analysis, diffusion-based stimulus-response generation, AI-virtual-cell roadmapping, broader multimodal human health modeling, explicit multimodal foundation-model blueprints for molecular cell biology, multiscale transformer architecture proposals, perturbation-atlas roadmaps for causal biology, atlas-based transcriptomic fidelity benchmarking, developmental multi-omic atlas substrates, region-specific developmental trajectory maps, and perturbation-trained single-cell scaling for oncology. The raw backlog is still much larger than the curated wiki, so the current picture is still early-stage.

## Current Focus

- Conditional and generative modeling for single-cell data.
- Atlas-scale generative pretraining and transfer learning for single-cell omics.
- Read-depth-aware foundation embeddings for lightly adapted downstream use.
- Retrieval-oriented foundation models for pan-body cell-state search and annotation.
- Language-model-based single-cell analysis that treats transcriptomes and biological text as one multimodal token space.
- Lightweight reuse of LLM-generated metadata embeddings as an alternative to heavy end-to-end biological FM pretraining.
- Uncertainty-aware cell annotation with hierarchy-based partial rejection instead of only full abstention.
- Neural optimal transport for perturbation-response prediction from unpaired single-cell populations.
- Sparse Bayesian Gaussian-process perturbation regression for interpretable gene-level and dosage-sensitive effect estimation.
- Mature RNA foundation modeling with biologically motivated contrastive pretraining over isoforms and orthologous transcripts.
- Knowledge-graph-guided prediction of unseen combinatorial perturbations and genetic interactions.
- Bayesian RNA-velocity modeling and interpretable temporal module discovery.
- Reinforcement-learning-based trajectory analysis that tries to localize early commitment states rather than only order cells along pseudotime.
- Diffusion-based generation of transient cell states across differentiation, perturbation, drug response, and injury-response settings.
- Multi-scale virtual-cell simulation roadmaps built around shared biological representations and in silico experimentation.
- Cross-modality reconstruction and intervention-aware modeling for broader human multi-omics.
- Explicit multimodal foundation-model blueprints that emphasize unified tokenization, intermodal attention, promptable generation, and lab-in-the-loop iteration.
- Multiscale transformer blueprints that combine modality-specific encoders, shared embedding spaces, and cross-attention across DNA, RNA, spatial, proteomic, image, and text modalities.
- Causal perturbation-atlas roadmaps that treat high-content pooled screens, compressed experimentation, and active-learning loops as foundation-model infrastructure.
- Queryable atlas resources for projecting new datasets, benchmarking protocol fidelity, and comparing diseased versus reference in vitro states.
- Multi-omic developmental atlases that combine transcriptomic, epigenomic, and spatial signals into reusable substrates for lineage modeling and disease-oriented inference.
- Region-specific developmental trajectory maps that can benchmark whether future models preserve anatomically grounded maturation logic rather than only endpoint labels.
- Perturbation-trained scaling strategies that use explicitly interventional pretraining corpora to improve zero-shot or few-shot response prediction in new contexts.
- Current anchor systems: [SAVE](entities/SAVE.md), [scGPT](entities/scGPT.md), [scFoundation](entities/scFoundation.md), [SCimilarity](entities/SCimilarity.md), [C2S-Scale](entities/C2S-Scale.md), [scELMo](entities/scELMo.md), [CellOT](entities/CellOT.md), [GEARS](entities/GEARS.md), [GPerturb](entities/GPerturb.md), [Orthrus](entities/Orthrus.md), [Cell2fate](entities/Cell2fate.md), [scRL](entities/scRL.md), [Squidiff](entities/Squidiff.md), [AIVC](entities/AIVC.md), [AURORA](entities/AURORA.md), and [Tahoe-x1](entities/Tahoe-x1.md). Supporting reference resource: [HNOCA](entities/HNOCA.md).

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
- Competitive perturbation modeling in this collection no longer implies deep latent architectures by default; sparse Bayesian Gaussian-process models can remain competitive while exposing gene-level effects and dosage sensitivity more directly.
- Annotation quality is increasingly tied to uncertainty handling: hierarchy-aware partial rejection can preserve useful label information, but only when the hierarchy tracks transcriptomic structure rather than ontology structure alone.
- Sequence foundation modeling in this collection now branches beyond cell-state modeling: Orthrus suggests that mature RNA representations may benefit more from biologically motivated contrastive pairing than from generic reconstruction-heavy genomic pretraining.
- Atlas infrastructure is emerging as its own modeling substrate: HNOCA acts less like a predictor and more like a queryable reference and fidelity benchmark that future generative or retrieval systems could train against or evaluate against.
- Reference atlases in this collection are increasingly acting as modeling substrates rather than only descriptive resources, with skeletal, organoid, and hypothalamic atlases all contributing different supervision or evaluation scaffolds.
- Developmental trajectory resources now span organoids, hypothalamus, and embryonic skeletal development, which strengthens the collection's ability to benchmark region-aware and stage-aware future models.
- Missing-data completion is becoming a core model function, either across unseen conditions or across unmeasured modalities.
- Evaluation is moving beyond reconstruction toward downstream utility: cell-state retrieval, large-scale annotation, natural-language interpretation, perturbation response, virtual screening, aging clocks, and disease prediction.

## Collection State

- Twenty-three source pages have been deeply ingested so far.
- The normalized raw-source backlog is still large, so future ingests may substantially refine or challenge the current synthesis.
