---
title: Transfer learning enables predictions in network biology
kind: paper
status: ingested
added: 2026-07-29T14:43:42+09:00
raw_source: raw/sources/theodoris_2023_transfer_learning_network_biology_Geneformer.pdf
---

# Transfer learning enables predictions in network biology

## Source

- File: [raw/sources/theodoris_2023_transfer_learning_network_biology_Geneformer.pdf](../../raw/sources/theodoris_2023_transfer_learning_network_biology_Geneformer.pdf)
- Added: 2026-07-29T14:43:42+09:00
- Venue/status: Nature article; published online 31 May 2023
- Authors: Christina V. Theodoris, Ling Xiao, Anant Chopra, Mark D. Chaffin, Zeina R. Al Sayed, Matthew C. Hill, Helene Mantineo, Elizabeth M. Brydon, Zexian Zeng, X. Shirley Liu, Patrick T. Ellinor
- DOI: `10.1038/s41586-023-06139-9`
- Model and code: [ctheodoris/Geneformer](https://huggingface.co/ctheodoris/Geneformer)
- Pretraining corpus: [ctheodoris/Genecorpus-30M](https://huggingface.co/datasets/ctheodoris/Genecorpus-30M)

## Summary

This paper introduces Geneformer, a BERT-like single-cell foundation model built to transfer broad transcriptomic knowledge into network-biology tasks with limited task-specific data. Each cell is converted into a rank-value sequence that prioritizes genes whose expression is unusually high relative to their corpus-wide non-zero median. Geneformer is pretrained by masking gene positions and then fine-tuned for gene or cell classification. The paper's distinctive contribution is not only annotation performance: it uses contextual embeddings and rank-sequence perturbations to predict dosage sensitivity, chromatin state, network hierarchy, disease-state shifts, and candidate cardiomyopathy targets.

## Corpus And Representation

- Genecorpus-30M contains `29,900,531` human single-cell transcriptomes from `561` public datasets; `27,406,217` cells pass the paper's quality filters.
- Only droplet-based datasets are included to improve expression-unit comparability.
- Malignant cells and immortalized cell lines are excluded because high mutational burdens may rewire networks without paired genome data needed for interpretation.
- The vocabulary contains `25,424` protein-coding or miRNA genes plus padding and mask tokens.
- For each gene, the tokenizer calculates its non-zero median expression across the corpus. Within each cell, normalized gene values are ranked to form the input sequence.
- This rank-value encoding deprioritizes ubiquitous housekeeping genes and can elevate lowly expressed but state-discriminative transcription factors.
- The tradeoff is explicit: rank encoding is non-parametric and potentially robust to depth and platform effects, but it discards precise transcript-count magnitudes.

## Architecture And Pretraining

- The published model contains six Transformer encoder units.
- Maximum input length is `2,048` genes, which fully represents `93%` of corpus cells.
- Hidden size is `256`, with four dense self-attention heads per layer and feed-forward size `512`.
- Pretraining masks `15%` of the genes in each cell and predicts which gene belongs at every masked position.
- The model is pretrained for three epochs on `12` NVIDIA V100 32-GB GPUs across three nodes, taking about three days.
- Dynamic length-grouped padding is reported to produce a `29.4x` pretraining speedup.
- Outputs include contextual gene embeddings, cell embeddings formed by averaging gene embeddings, attention weights, and task-specific predictions.

## Transfer And In Silico Perturbation

- Fine-tuning initializes from the pretrained weights and adds a task-specific gene- or cell-classification layer.
- The same basic fine-tuning hyperparameters were deliberately reused across tasks, usually for one epoch, to test transfer rather than maximize every benchmark.
- In silico deletion removes a gene from a cell's rank-value encoding and measures changes in cell or remaining-gene embeddings.
- In silico activation moves a gene to the front of the rank sequence.
- These operations are embedding-space interventions on the model's input representation; they are not direct simulations of molecular kinetics or absolute expression changes.

## Evaluations And Evidence

### Dosage Sensitivity

- Fine-tuning on `10,000` cells to distinguish dosage-sensitive from insensitive transcription factors achieved AUC `0.91`.
- On recently reported neurodevelopmental-disease genes, moderate-confidence genes were predicted dosage-sensitive in fetal cerebral cells with `84%` concordance.
- High-confidence genes were predicted dosage-sensitive at similar rates in fetal cerebral and other cells (`96%` and `95%`), while moderate-confidence predictions were more cell-context-dependent.
- Pretrained in silico deletion in fetal cardiomyocytes prioritized known cardiomyopathy genes and the candidate `TEAD4`; CRISPR knockout of `TEAD4` reduced contractile stress in engineered cardiac microtissues, supporting its predicted dosage sensitivity.

### Chromatin State

- Geneformer was fine-tuned on about `15,000` embryonic stem cells and only `56` conserved labelled loci.
- It distinguished bivalent promoters from unmethylated or H3K4-only promoters with AUC `0.93` and `0.88`, respectively.
- The learned classifier generalized to genome-wide loci excluded from fine-tuning.

### Network Hierarchy

- Using about `30,000` normal heart endothelial cells and no perturbation data, Geneformer predicted central versus peripheral nodes in a NOTCH1-dependent network with AUC `0.81`.
- Similar predictive power was retained down to about `5,000` cells.
- Fine-tuning on only `884` more context-relevant healthy or dilated-aorta endothelial cells achieved AUC `0.74`, exceeding alternative models trained on the larger `30,000`-cell set.
- `20%` of attention heads attended transcription factors more strongly than other genes, and some attention heads preferentially attended central network nodes.
- In silico deletion of `GATA4` and `TBX5` preferentially disrupted known direct or cobound targets, including a greater-than-additive effect for the double deletion.

### Cardiomyopathy And Therapeutic Candidates

- A classifier distinguishing non-failing, hypertrophic-cardiomyopathy, and dilated-cardiomyopathy cardiomyocytes achieved `90%` out-of-sample accuracy.
- The model identified `447` genes whose loss shifted non-failing cells toward hypertrophic cardiomyopathy and `478` whose loss shifted them toward dilated cardiomyopathy.
- Reverse in silico treatment analysis prioritized candidate targets expected to move disease embeddings toward the non-failing state.
- CRISPR knockout of predicted targets `GSN` and `PLN` significantly improved contractile stress in `TTN+/-` engineered cardiac microtissues.

## Key Claims

- Large, self-supervised single-cell pretraining can make biologically specialized predictions possible with limited labelled data.
- Rank-value encoding provides a context-sensitive and technically robust input representation for transfer learning.
- Contextual embeddings and attention weights contain useful information about gene-network hierarchy.
- Embedding-space perturbation can prioritize dosage-sensitive genes and experimentally actionable therapeutic candidates.

## Interpretation

- Geneformer is most distinctive as a low-data network-biology transfer model, not as a general-purpose generator of full post-perturbation transcriptomes.
- Its strongest evidence combines benchmark transfer with limited wet-lab validation, especially `TEAD4`, `GSN`, and `PLN`.
- The rank-value representation is a deliberate biological prior: it defines importance relative to corpus-wide expression rather than preserving the original quantitative count vector.
- Attention enrichment and in silico deletion are hypothesis-generation tools. The experimental validations strengthen particular examples but do not turn all attention weights into causal edges.

## Limitations

- Rank-value encoding does not fully use precise transcript-count magnitude.
- The pretraining corpus excludes malignant cells and immortalized lines, limiting coverage of heavily rewired cancer states.
- Full dense attention over `2,048` genes remains quadratic even though length-grouped padding improves efficiency.
- Much of the mechanistic evidence is concentrated in cardiovascular networks, especially NOTCH1 and cardiomyopathy.
- In silico deletion and activation are token-sequence manipulations, not explicit mechanistic models of transcription, dosage, or protein activity.
- Experimental validation is compelling but narrow relative to the breadth of the model's claimed downstream applicability.
- Fine-tuning results depend on relevance as well as amount of task-specific data; there is no universal sample-count threshold.

## Related Pages

- [Geneformer](../entities/Geneformer.md)
- [Rank-Value Encoding](../concepts/rank-value-encoding.md)
- [Embedding-Space In Silico Perturbation](../concepts/embedding-space-in-silico-perturbation.md)
- [Study Guide: scGPT, scFoundation, Geneformer, and CellFM](../syntheses/scgpt-scfoundation-geneformer-cellfm-study-guide.md)

## Open Questions

- How much of Geneformer's downstream transfer comes from corpus scale versus the corpus-derived rank normalization?
- How reliably do the original model's attention-derived network claims reproduce across unrelated tissues and disease mechanisms?
- When should rank-sequence perturbation be preferred to models that predict quantitative post-perturbation expression?
- How do later Geneformer variants change the original paper's representation, scale, and validation claims?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T14:51:15+09:00
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/theodoris_2023_transfer_learning_network_biology_Geneformer.pdf -o raw/derived/opendataloader/theodoris_2023_transfer_learning_network_biology_Geneformer -f markdown --image-output off`
- Manifest: [raw/derived/opendataloader/theodoris_2023_transfer_learning_network_biology_Geneformer/opendataloader-run.json](../../raw/derived/opendataloader/theodoris_2023_transfer_learning_network_biology_Geneformer/opendataloader-run.json)
- Output: [raw/derived/opendataloader/theodoris_2023_transfer_learning_network_biology_Geneformer/theodoris_2023_transfer_learning_network_biology_Geneformer.md](../../raw/derived/opendataloader/theodoris_2023_transfer_learning_network_biology_Geneformer/theodoris_2023_transfer_learning_network_biology_Geneformer.md)
- Poppler layout text: [raw/derived/pdftext/Theodoris_2023_Geneformer/Theodoris_2023_Geneformer.txt](../../raw/derived/pdftext/Theodoris_2023_Geneformer/Theodoris_2023_Geneformer.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
