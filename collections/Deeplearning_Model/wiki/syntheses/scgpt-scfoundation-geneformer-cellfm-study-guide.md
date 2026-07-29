# Study Guide: scGPT, scFoundation, Geneformer, and CellFM

## Bottom Line

- These four papers are all atlas-scale single-cell foundation models, but they solve different representation and transfer problems.
- The fastest way to understand them is to compare what each model preserves from a cell, what it masks during pretraining, and what counts as a successful downstream prediction.

## Four One-Sentence Anchors

- [scGPT](../entities/scGPT.md): a generative Transformer that combines gene, expression, and condition tokens for broad task-specific fine-tuning.
- [scFoundation](../entities/scFoundation.md): a continuous-expression foundation layer that makes sequencing depth part of the pretraining problem.
- [Geneformer](../entities/Geneformer.md): a rank-based BERT-style encoder optimized for low-data, context-specific network and disease transfer.
- [CellFM](../entities/CellFM.md): a large continuous-value model that uses an efficient retention backbone to scale to `102.3M` cells and `800M` parameters.

## Comparison Table

| Dimension | scGPT | scFoundation | Geneformer | CellFM |
|---|---|---|---|---|
| Paper corpus | `>33M` normal human cells | `>50M` human cells | `29.9M` human cells; `27.4M` pass QC | `102.3M` human cells |
| Basic representation | gene tokens + expression/value + condition tokens | quantitative expression with source/target depth indicators | corpus-normalized ranked gene tokens | continuous value projection + gene-ID embeddings |
| Backbone | 12-block Transformer | asymmetric encoder-decoder | 6-layer Transformer encoder | 40-block ERetNet |
| Published scale emphasized | hidden size `512`, 8 heads | about `100M` parameters | hidden size `256`, 4 heads | `800M` parameters, hidden size `1,536`, 48 heads |
| Pretraining focus | generative masked expression/token modeling | read-depth-aware masked reconstruction | mask `15%` of gene positions and recover gene identity | mask `20%` of expressed genes and recover expression representations |
| Adaptation style | task-specific fine-tuning and objectives | frozen/lightly adapted embeddings plus downstream models | low-data gene or cell classification and embedding perturbation | frozen embeddings, LoRA fine-tuning, or insertion into GEARS/CellOT |
| Strongest identity | broad multi-task generative transfer | depth-aware reusable representation | context-specific network biology with scarce labels | scale, continuous values, and efficient retention |
| Main caution | gains often rely on task-specific objectives | depth modeling does not remove all technical variation | ranks lose quantitative magnitude; perturbations are embedding proxies | `80M` and `800M` results differ; many tasks use external heads |

## The Central Representation Fork

### Geneformer: Importance As Relative Rank

- [Rank-Value Encoding](../concepts/rank-value-encoding.md) asks whether a gene is unusually informative for the current cell relative to its typical expression across a large corpus.
- This can suppress housekeeping abundance and highlight state-specific regulators.
- It also discards exact magnitude.

### scGPT: Gene, Value, And Context Tokens

- scGPT keeps genes as tokens and adds expression and condition information.
- Its advantage is flexibility across annotation, integration, perturbation, and multi-omic tasks.
- Its specialized masking scheme reflects the fact that a transcriptome is not naturally an ordered sentence.

### scFoundation And CellFM: Preserve Quantitative Values

- Both models stay closer to expression magnitude through [Continuous Expression Value Projection](../concepts/continuous-expression-value-projection.md).
- scFoundation makes depth conversion explicit with source and target count indicators.
- CellFM emphasizes scale and swaps dense Transformer attention for [Retention-Based Single-Cell Modeling](../concepts/retention-based-single-cell-modeling.md).

## What The Pretraining Objective Teaches

- Geneformer learns which gene token fits a masked rank position in a particular cellular context.
- scGPT learns reusable gene and cell representations through generative masked objectives plus later task-specific losses.
- scFoundation learns gene context together with transformations between effective read depths.
- CellFM learns to recover masked continuous expression representations and cell-level gene-vocabulary signals.
- All four are self-supervised, but `masked prediction` does not mean they learn the same object.

## What Perturbation Means In Each Paper

- Geneformer uses [Embedding-Space In Silico Perturbation](../concepts/embedding-space-in-silico-perturbation.md): delete or reposition a gene token and measure representation movement.
- scGPT predicts post-perturbation expression and also ranks perturbations that could produce a target state.
- scFoundation contributes embeddings to GEARS-style quantitative response prediction.
- CellFM evaluates gene embeddings inside GEARS, cell embeddings inside CellOT, and reverse perturbation retrieval.
- A result about embedding movement is not directly comparable to a result about mean expression, a ranked intervention, or a full response distribution.

## Evidence Worth Remembering

### scGPT

- `33M`-cell pretraining.
- Broad evaluation across annotation, integration, perturbation, and gene-network analysis.
- Reverse perturbation retrieval and multi-omic integration are especially characteristic.

### scFoundation

- `>50M` cells and about `100M` parameters.
- Explicit tests on downsampled low-depth profiles.
- Reusable embeddings improve annotation, clustering, perturbation, drug response, and regulatory analyses.

### Geneformer

- Dosage-sensitivity AUC `0.91` with `10,000` cells.
- Network-centrality AUC `0.81` with about `30,000` endothelial cells and useful transfer down to `884` context-relevant cells.
- Cardiomyopathy classifier accuracy `90%`.
- Experimental support for `TEAD4` dosage sensitivity and functional improvement after `GSN` or `PLN` knockout in engineered cardiac microtissues.

### CellFM

- `102,304,686` cells and `800M` parameters.
- CellFM-80M frozen-embedding annotation accuracy `92.91%` across eight intra-datasets.
- Reverse perturbation top-10 recovery `81.8%` in the paper's 20-gene benchmark.
- Average `18/20` top attention-ranked genes matched ChIP-Atlas across nine perturbation cases.

## Common Comparison Traps

- `Zero-shot` may still mean a frozen encoder followed by a supervised classifier trained on the target task.
- A larger model is not automatically the model used for every reported benchmark; CellFM's annotation section is the key example.
- Corpus composition differs: normal-only, disease-inclusive, malignant-excluding, and technology-filtered corpora do not teach the same biology.
- Task-specific heads can account for part of the gain, especially when foundation embeddings are inserted into GEARS or CellOT.
- Attention and retention weights are not causal regulatory edges.
- Reverse perturbation, response prediction, and embedding perturbation are related but distinct tasks.
- Scaling, tokenization, architecture, normalization, and fine-tuning all change at once across papers, so leaderboards rarely isolate one cause.

## Recommended Study Order

1. Start with the input representation: rank, binned/value tokens, depth-aware continuous values, or projected continuous values.
2. Identify the masked object: gene identity, expression value, or depth-conditioned expression.
3. Identify the reusable output: gene embedding, cell embedding, generator, or downstream task head.
4. Separate frozen-encoder, light-adaptation, and full-fine-tuning results.
5. For perturbation, write down the exact prediction target before comparing metrics.
6. Finish with biological validation: benchmark-only evidence is weaker than held-out patient, cross-platform, or wet-lab validation.

## Questions To Test Understanding

- Why can Geneformer's rank encoding be robust to depth variation while losing information at the same time?
- What does scFoundation model explicitly that the other three mostly leave to preprocessing or downstream adaptation?
- Why is CellFM's `800M` parameter count not enough to interpret its frozen-annotation results?
- Which perturbation outputs are expression profiles, which are intervention rankings, and which are embedding shifts?
- What evidence supports a biological network claim beyond an attention heatmap?
- Which model would be the most natural starting point for low-data network biology, depth correction, multimodal integration, or atlas-scale continuous-value encoding?

## Sources Used

- [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](../sources/cui_2024_scgpt_toward_building_a_foundation.md)
- [Large-scale foundation model on single-cell transcriptomics](../sources/hao_2024_large-scale_foundation_model_on_single-cell.md)
- [Transfer learning enables predictions in network biology](../sources/theodoris_2023_transfer_learning_network_biology_Geneformer.md)
- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
