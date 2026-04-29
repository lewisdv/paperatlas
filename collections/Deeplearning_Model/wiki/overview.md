# Overview

This collection now has seven deeply ingested anchors and is beginning to connect single-cell generative modeling, atlas-scale generative pretraining, read-depth-aware foundation embeddings, retrieval-style cell atlas foundation models, language-model-based transcriptomic reasoning, neural optimal-transport perturbation modeling, and broader multimodal human health modeling. The raw backlog is still much larger than the curated wiki, so the current picture is still early-stage.

## Current Focus

- Conditional and generative modeling for single-cell data.
- Atlas-scale generative pretraining and transfer learning for single-cell omics.
- Read-depth-aware foundation embeddings for lightly adapted downstream use.
- Retrieval-oriented foundation models for pan-body cell-state search and annotation.
- Language-model-based single-cell analysis that treats transcriptomes and biological text as one multimodal token space.
- Neural optimal transport for perturbation-response prediction from unpaired single-cell populations.
- Cross-modality reconstruction and intervention-aware modeling for broader human multi-omics.
- Current anchor systems: [SAVE](entities/SAVE.md), [scGPT](entities/scGPT.md), [scFoundation](entities/scFoundation.md), [SCimilarity](entities/SCimilarity.md), [C2S-Scale](entities/C2S-Scale.md), [CellOT](entities/CellOT.md), and [AURORA](entities/AURORA.md).

## Emerging Themes

- Semantically structured representations, such as gene blocks or shared latent spaces, are used to compress biological complexity into model-ready tokens or embeddings.
- Large pretrained atlas models increasingly follow a `pretrain broadly, fine-tune per task` pattern rather than building each single-cell workflow from scratch.
- Some foundation-model work is explicitly trying to factor sequencing depth into pretraining rather than leaving that variation entirely to downstream normalization or integration methods.
- Transcriptomes are increasingly being serialized into language-like sequences so frontier LLM scaling and prompting techniques can be reused for biology.
- Fast nearest-neighbour retrieval over large pretrained atlases is emerging as a separate foundation-model pattern alongside generation and imputation.
- Perturbation modeling in this collection now spans both generative/token-based approaches and explicit transport-map approaches that try to preserve full response distributions rather than only average shifts.
- Missing-data completion is becoming a core model function, either across unseen conditions or across unmeasured modalities.
- Evaluation is moving beyond reconstruction toward downstream utility: cell-state retrieval, large-scale annotation, natural-language interpretation, perturbation response, virtual screening, aging clocks, and disease prediction.

## Collection State

- Seven source pages have been deeply ingested so far.
- The normalized raw-source backlog is still large, so future ingests may substantially refine or challenge the current synthesis.
