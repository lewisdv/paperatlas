# Overview

This collection now has thirty-four deeply ingested anchors and is beginning to connect single-cell generative modeling, atlas-scale generative pretraining, rank-value network-biology transfer, read-depth-aware foundation embeddings, continuous expression-value projection, retention-based single-cell scaling, retrieval-style cell atlas foundation models, transcriptome-as-language modeling, language-model-based transcriptomic reasoning, lightweight LLM-derived metadata embedding reuse, uncertainty-aware hierarchical annotation, neural optimal-transport perturbation modeling, Gaussian-process-based perturbation regression, biologically motivated mature-RNA foundation modeling, combinatorial perturbation generalization, Bayesian RNA-velocity dynamics, reinforcement-learning-based fate-decision analysis, clinical reinforcement-learning translation for dynamic treatment regimes, diffusion-based stimulus-response generation, AI-virtual-cell roadmapping, broader multimodal human health modeling, paired, unpaired, and mosaic single-cell multi-omics integration, missing-modality imputation, cross-modal regulatory inference, cell-type-specific enhancer-gene mapping, DNA-sequence-to-single-cell profile prediction, explicit multimodal foundation-model blueprints for molecular cell biology, multiscale transformer architecture proposals, perturbation-atlas roadmaps for causal biology, atlas-based transcriptomic fidelity benchmarking, developmental multi-omic atlas substrates, region-specific developmental trajectory maps, sex-stratified psychiatric transcriptomic burden, and perturbation-trained single-cell scaling for oncology. The normalized raw-source ingest backlog is now effectively exhausted except for `.DS_Store`, so the collection has moved from source accumulation into a synthesis-and-lint phase.

## Current Focus

- Conditional and generative modeling for single-cell data.
- Atlas-scale generative pretraining and transfer learning for single-cell omics.
- Corpus-normalized rank-value encoding for low-data, context-specific network biology.
- Read-depth-aware foundation embeddings for lightly adapted downstream use.
- Continuous expression-value projection and retention-based scaling for atlas-scale human transcriptomics.
- Retrieval-oriented foundation models for pan-body cell-state search and annotation.
- Rank-ordered transcriptome serialization that lets standard causal LLMs generate cells, predict labels, and emit biological prose.
- Language-model-based single-cell analysis that treats transcriptomes and biological text as one multimodal token space.
- Lightweight reuse of LLM-generated metadata embeddings as an alternative to heavy end-to-end biological FM pretraining.
- Uncertainty-aware cell annotation with hierarchy-based partial rejection instead of only full abstention.
- Neural optimal transport for perturbation-response prediction from unpaired single-cell populations.
- Sparse Bayesian Gaussian-process perturbation regression for interpretable gene-level and dosage-sensitive effect estimation.
- Mature RNA foundation modeling with biologically motivated contrastive pretraining over isoforms and orthologous transcripts.
- Knowledge-graph-guided prediction of unseen combinatorial perturbations and genetic interactions.
- Bayesian RNA-velocity modeling and interpretable temporal module discovery.
- Reinforcement-learning-based trajectory analysis that tries to localize early commitment states rather than only order cells along pseudotime.
- Clinical translation of reinforcement learning for precision medicine and dynamic treatment regimes, with emphasis on reward design, interpretability, offline validation, and EHR-compatible workflows.
- Diffusion-based generation of transient cell states across differentiation, perturbation, drug response, and injury-response settings.
- Multi-scale virtual-cell simulation roadmaps built around shared biological representations and in silico experimentation.
- Cross-modality reconstruction and intervention-aware modeling for broader human multi-omics.
- Paired, unpaired, and mosaic single-cell multi-omics integration with explicit attention to the measurement correspondences available across datasets.
- Missing-modality imputation under paired-reference, mosaic-block, and feature-link-guided supervision.
- Guidance-graph and feature-link approaches that orient otherwise unpaired omics spaces and support cross-modal regulatory inference.
- Cell-type-specific enhancer-gene mapping from paired RNA and chromatin-accessibility counts with explicit depth and subject adjustment.
- DNA-sequence-to-single-cell RNA and ATAC profile prediction conditioned on continuous cell-state representations.
- Explicit multimodal foundation-model blueprints that emphasize unified tokenization, intermodal attention, promptable generation, and lab-in-the-loop iteration.
- Multiscale transformer blueprints that combine modality-specific encoders, shared embedding spaces, and cross-attention across DNA, RNA, spatial, proteomic, image, and text modalities.
- Causal perturbation-atlas roadmaps that treat high-content pooled screens, compressed experimentation, and active-learning loops as foundation-model infrastructure.
- Queryable atlas resources for projecting new datasets, benchmarking protocol fidelity, and comparing diseased versus reference in vitro states.
- Multi-omic developmental atlases that combine transcriptomic, epigenomic, and spatial signals into reusable substrates for lineage modeling and disease-oriented inference.
- Region-specific developmental trajectory maps that can benchmark whether future models preserve anatomically grounded maturation logic rather than only endpoint labels.
- Sex-stratified transcriptomic burden analysis as a heterogeneity-aware reference axis for psychiatric disease modeling.
- Perturbation-trained scaling strategies that use explicitly interventional pretraining corpora to improve zero-shot or few-shot response prediction in new contexts.
- Current anchor systems: [SAVE](entities/SAVE.md), [scGPT](entities/scGPT.md), [scFoundation](entities/scFoundation.md), [Geneformer](entities/Geneformer.md), [CellFM](entities/CellFM.md), [SCimilarity](entities/SCimilarity.md), [Cell2Sentence](entities/Cell2Sentence.md), [C2S-Scale](entities/C2S-Scale.md), [scELMo](entities/scELMo.md), [CellOT](entities/CellOT.md), [GEARS](entities/GEARS.md), [GPerturb](entities/GPerturb.md), [Orthrus](entities/Orthrus.md), [Cell2fate](entities/Cell2fate.md), [scRL](entities/scRL.md), [Squidiff](entities/Squidiff.md), [AIVC](entities/AIVC.md), [AURORA](entities/AURORA.md), [Tahoe-x1](entities/Tahoe-x1.md), [MIDAS](entities/MIDAS.md), [GLUE](entities/GLUE.md), [MultiVI](entities/MultiVI.md), [scMODAL](entities/scMODAL.md), [scMultiMap](entities/scMultiMap.md), and [scooby](entities/scooby.md). Supporting reference resource: [HNOCA](entities/HNOCA.md).

## Emerging Themes

- Semantically structured representations, such as gene blocks or shared latent spaces, are used to compress biological complexity into model-ready tokens or embeddings.
- Large pretrained atlas models increasingly follow a `pretrain broadly, fine-tune per task` pattern rather than building each single-cell workflow from scratch.
- Some foundation-model work is explicitly trying to factor sequencing depth into pretraining rather than leaving that variation entirely to downstream normalization or integration methods.
- Single-cell representation now has an explicit three-way fork between rank-based ordering, expression categorization, and continuous value projection; the choice determines what quantitative information is preserved or discarded.
- Efficient sequence backbones are becoming part of the biological scaling argument: CellFM uses retention to make `800M` parameters and a `102.3M`-cell corpus tractable.
- Geneformer adds a low-data network-transfer branch in which contextual embeddings and rank-sequence perturbations are used to prioritize dosage-sensitive genes, network regulators, and disease targets.
- The original Cell2Sentence paper establishes transcriptome serialization as a workable interface to GPT-2/Pythia; C2S-Scale later turns the same representation into a much larger multi-task scaling program.
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
- Reinforcement learning in this collection now spans both cell-state analysis and patient-level decision support, but the clinical side raises translation constraints around reward alignment, transparency, retrospective bias, and workflow fit.
- Some useful reference sources here are not predictive models at all; sex-stratified burden studies can supply heterogeneity targets that future psychiatric or multimodal models may need to preserve.
- Missing-data completion is becoming a core model function, either across unseen conditions or across unmeasured modalities.
- Multimodal integration is now a concrete implementation branch rather than only a roadmap theme: vertical, diagonal, and mosaic regimes expose different amounts of cross-modal supervision and therefore require different assumptions.
- Regulatory inference now spans GLUE's guidance-graph embedding similarity, scMultiMap's paired count association, and scooby's sequence perturbation. These outputs have different evidential semantics and should not be compared as if they were equivalent causal claims.
- Sequence foundation-model transfer now reaches cell-conditioned multimodal profiles: scooby adapts a long-context DNA model to predict cell-specific RNA and ATAC readouts rather than only producing a sequence embedding.
- Evaluation is moving beyond reconstruction toward downstream utility: cell-state retrieval, large-scale annotation, natural-language interpretation, perturbation response, virtual screening, aging clocks, and disease prediction.
- The cleanest first-pass map is now by evaluation task family rather than by architecture label alone: retrieval and annotation, transferable foundation representations, perturbation prediction, transition analysis, multimodal completion, reference benchmarking, and roadmap or translation work.

## Collection State

- Thirty-four source pages have been deeply ingested so far.
- The normalized raw-source ingest backlog is effectively exhausted except for `raw/sources/.DS_Store`.
- The next high-value work is cross-link refinement, synthesis, and question-driven comparison rather than more raw-source ingestion.
