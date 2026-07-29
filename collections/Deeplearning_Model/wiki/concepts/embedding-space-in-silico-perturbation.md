# Embedding-Space In Silico Perturbation

## Definition

- Embedding-space in silico perturbation changes a model's input representation and measures how the learned gene or cell embedding moves.
- It is a hypothesis-generation strategy rather than a direct simulator of molecular kinetics.

## In Geneformer

- Deletion removes a gene from the cell's [Rank-Value Encoding](rank-value-encoding.md).
- Activation moves a gene toward the front of the ranked sequence.
- Effects are measured by cosine changes in the cell embedding or in contextual embeddings of the remaining genes.
- Reverse treatment analysis searches for perturbations that move disease-cell embeddings toward a non-diseased state.

## Distinction From Response Prediction

- Geneformer's original perturbation analysis asks how a learned representation moves when tokens are deleted or reordered.
- scGPT and CellFM also support reverse perturbation questions, but they are evaluated with different objectives and downstream systems.
- GEARS and diffusion or transport models more directly target post-perturbation expression or population distributions.
- These outputs should not be placed on one leaderboard without checking whether the task predicts an embedding shift, a ranked intervention, a mean expression profile, or a full response distribution.

## Evidence And Limits

- Geneformer recovered known GATA4 and TBX5 target relationships and prioritized cardiomyopathy candidates later tested in engineered cardiac microtissues.
- Those validations support selected hypotheses, not every embedding movement.
- The intervention is defined by the tokenizer and representation, so its biological meaning inherits the assumptions of rank encoding.
- Experimental validation remains necessary before interpreting model-space movement as a therapeutic effect.

## Sources

- [Transfer learning enables predictions in network biology](../sources/theodoris_2023_transfer_learning_network_biology_Geneformer.md)
- [CellFM: a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](../sources/CellFM_Zeng_2025_100M_cells_RetNet_atlas_scale_baseline.md)
