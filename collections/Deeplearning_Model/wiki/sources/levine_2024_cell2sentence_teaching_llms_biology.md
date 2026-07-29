---
title: Cell2Sentence: Teaching Large Language Models the Language of Biology
kind: paper
status: ingested
added: 2026-07-29T16:32:35+09:00
raw_source: raw/sources/levine_2024_cell2sentence_teaching_llms_biology.pdf
---

# Cell2Sentence: Teaching Large Language Models the Language of Biology

## Source

- File: [raw/sources/levine_2024_cell2sentence_teaching_llms_biology.pdf](../../raw/sources/levine_2024_cell2sentence_teaching_llms_biology.pdf)
- Added: 2026-07-29T16:32:35+09:00
- Venue/status: Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 2024
- Authors: Daniel Levine, Syed Asad Rizvi, Sacha Lévy, Nazreen Pallikkavaliyaveetil, David Zhang, Xingyu Chen, Sina Ghadermarzi, Ruiming Wu, Zihe Zheng, Ivan Vrkic, Anna Zhong, Daphne Raskin, Insu Han, Antonio Henrique de Oliveira Fonseca, Josue Ortega Caro, Amin Karbasi, Rahul M. Dhodapkar, and David van Dijk
- SHA-256: `0fda151a04d938a8299a231dbbd4af71f68cfc25003b4a6e991f200ad0789504`

## Summary

Cell2Sentence (`C2S`) is a framework for making single-cell transcriptomes directly consumable by ordinary causal language models. It converts each normalized expression profile into a `cell sentence`: gene names ordered from highest to lowest expression. GPT-2 and Pythia models are then fine-tuned on mixtures of these sequences, metadata prompts, and biological prose. The paper is an ICML 2024 proof of concept showing conditional cell generation, combinatorial label prediction, and abstract-like text generation. It is the methodological precursor to the later, much larger [C2S-Scale](../entities/C2S-Scale.md), not evidence for that later model's scale or capabilities.

## Representation And Reconstruction

- Cells with poor quality and rare genes are filtered; counts are cell-normalized to `10,000` and log-normalized before genes are ranked by descending abundance.
- The resulting sentence contains gene-name tokens but no explicit expression magnitudes.
- For each dataset, C2S fits a log-rank-to-expression regression, `e_i = a_d log(rank_i) + b_d`, and saves the dataset-specific slope and intercept.
- Generated sentences are converted back to expression by ignoring invalid genes, averaging the ranks of duplicated genes, applying the fitted regression, and assigning zero to absent genes.
- On the immune-tissue reconstruction analysis, rank alone explains `R² = 0.815` of expression variation; the reconstructed cells also preserve the broad UMAP geometry qualitatively.

## Models And Data

- Models: pretrained or randomly initialized GPT-2 small (`117M`), medium (`345M`), and large (`774M`), plus Pythia-160M.
- Because of compute constraints, GPT-2 inputs are truncated to the top `100` expressed genes. Pythia uses a maximum sequence length of `9,200` tokens and can process full cell sentences.
- Immune-tissue dataset: `273,502` cell sentences across `35` cell types, used for unconditional generation, conditional cell-type generation, and cell-type prediction.
- Cytokine-stimulation dataset: `9` stimulation combinations, `2` exposures, and `7` cell types, giving `140` combinatorial labels. Ten combinations with an exposure unseen for that cell-type/perturbation pair are held out for generation.
- Multi-tissue corpus: `99` human datasets totaling `37M` cells, with `19` studies held out (`2.7%` of cell sentences), `11` tissues, and `42` tissue combinations. The training corpus is augmented with synthetic abstract summaries.

## Tasks

- Generate cell sentences unconditionally or from text specifying cell type, tissue, perturbation, and exposure.
- Predict cell type or multipart metadata labels autoregressively in natural language.
- Generate abstract-like biological summaries from cell sentences and generate cells from summaries.

## Key Claims

- A simple rank-ordered gene-name representation is sufficient to reuse standard language-model training infrastructure for transcriptomics.
- Natural-language pretraining transfers useful structure to biological sequence generation and classification; it is not equivalent to training the same architecture from scratch on cell sentences.
- One language-model interface can support both transcriptomic outputs and free-text outputs without a custom single-cell architecture.
- C2S can extrapolate to held-out cytokine condition combinations in the paper's benchmark, but the result is a narrow conditional-generation experiment rather than general causal validation.

## Evidence

- Conditional immune-cell generation: Pythia-160M C2S obtains k-NN accuracies of `0.2588` to `0.2746` and a Gromov-Wasserstein distance of `54.3040`, outperforming the reported scGen, scVI, scDiffusion, and reimplemented scGPT baselines on those metrics.
- Held-out cytokine conditions: C2S reports Pearson `r = 0.9241`, top-20-DE Pearson `r = 0.9734`, Spearman `r = 0.6210`, and top-20-DE Spearman `r = 0.9752`; the delta-from-opposite-exposure correlations are substantially lower.
- Complex label prediction: GPT-2 large C2S has the best reported partial- and full-label accuracy among the tested k-NN, XGBoost, Geneformer, and scGPT baselines across cytokine, L1000, and GTEx datasets. Absolute full-label accuracy remains low: `0.149`, `0.202`, and `0.152`, respectively.
- Natural-language pretraining ablation: averaged generated-cell expression improves from Pearson `r = 0.947` and `R² = 0.873` when trained from scratch to `r = 0.984` and `R² = 0.949` after natural-language pretraining.
- Cell-type prediction on unseen immune cells improves from about `29%` accuracy without natural-language pretraining to `69.95%` for GPT-2 small and `74.26%` for GPT-2 medium with it.
- Output validity for pretrained-and-fine-tuned GPT-2 is high on top-100-gene generation: `99.60–99.70%` valid genes and `98.88–99.47%` unique genes.
- Abstract generation: only the C2S models show a statistically significant same-study versus other-study embedding-similarity separation in Table 4, with MMD `0.198`, compared with `0.298` for GPT-3.5 and higher values for the other tested LLMs.

## Interpretation

- The strongest result is the natural-language-pretraining ablation: a language-pretrained model learns cell generation and label prediction substantially better than an identical architecture initialized from scratch.
- C2S's apparent reversibility is approximate, not literal. The sentence preserves rank, while quantitative expression is reconstructed from a dataset-level regression.
- This paper establishes feasibility at GPT-2/Pythia scale. Claims about `410M–27B` models, more than `50M` cells, reinforcement learning, spatial reasoning, and experimental virtual screening belong to the later [Scaling Large Language Models for Next-Generation Single-Cell Analysis](rizvi_2025_scaling_large_language_models_for.md).

## Limitations

- Rank serialization discards exact expression magnitudes; the back-conversion is dataset-specific and the reported `R² = 0.815` leaves meaningful residual variation.
- GPT-2 experiments retain only the top `100` genes, whereas Pythia can use full sentences, so model comparisons also mix architecture and information-content differences.
- Benchmark comparability is uneven. For cytokine generation, C2S and scGen use `21,710` genes while scGPT uses `5,000` highly variable genes; the authors reimplemented scGPT's conditional-generation method because public code was unavailable.
- Prompt robustness is incomplete: Pythia-160M's k-NN generation accuracy drops from roughly `0.26–0.27` with seen templates to `0.19–0.21` with semantically similar unseen prompts.
- Generated outputs still require rules for invalid and duplicate gene names.
- Abstract similarity is an indirect text-embedding evaluation. Qualitative examples include plausible but incorrect or overgeneralized details, so it does not establish reliable biological interpretation.
- Attention heatmaps are descriptive model diagnostics, not evidence that attended genes are causal mechanisms.
- The paper reports no wet-lab validation.

## Related Pages

- [Cell2Sentence](../entities/Cell2Sentence.md)
- [Cell Sentences](../concepts/cell-sentences.md)
- [C2S-Scale](../entities/C2S-Scale.md)
- [Scaling Large Language Models for Next-Generation Single-Cell Analysis](rizvi_2025_scaling_large_language_models_for.md)

## Open Questions

- How much quantitative signal is lost when cell sentences move across datasets whose rank-expression curves differ?
- Does natural-language pretraining help because gene symbols and labels already carry biological semantics, because it gives better general sequence features, or both?
- How much of the conditional perturbation result survives evaluations with matched gene sets, fully external datasets, and direct experimental validation?
- What calibration or retrieval constraints are needed before abstract-like outputs can be treated as biological interpretation rather than plausible text?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T16:35:08+0900
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/levine_2024_cell2sentence_teaching_llms_biology.pdf -o raw/derived/opendataloader/levine_2024_cell2sentence_teaching_llms_biology -f markdown --image-output off -q`
- Manifest: [raw/derived/opendataloader/levine_2024_cell2sentence_teaching_llms_biology/opendataloader-run.json](../../raw/derived/opendataloader/levine_2024_cell2sentence_teaching_llms_biology/opendataloader-run.json)
- Output: [raw/derived/opendataloader/levine_2024_cell2sentence_teaching_llms_biology/levine_2024_cell2sentence_teaching_llms_biology.md](../../raw/derived/opendataloader/levine_2024_cell2sentence_teaching_llms_biology/levine_2024_cell2sentence_teaching_llms_biology.md)
- Layout text: [raw/derived/pdftext/Levine_2024_Cell2Sentence/Levine_2024_Cell2Sentence.txt](../../raw/derived/pdftext/Levine_2024_Cell2Sentence/Levine_2024_Cell2Sentence.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
