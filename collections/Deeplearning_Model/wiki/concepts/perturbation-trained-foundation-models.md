# Perturbation-Trained Foundation Models

## Definition

- Perturbation-trained foundation models are foundation-model systems whose pretraining corpora are deliberately enriched with intervention data, so the learned representation is shaped not only by passive cell-state diversity but also by observed responses to drugs or genetic perturbations.
- In this collection, the idea is stronger than generic downstream perturbation fine-tuning: it claims that perturbative pretraining itself changes what the model can generalize about causal biological change.

## In This Collection

- [Tahoe-x1](../entities/Tahoe-x1.md) is the clearest example, explicitly arguing that large perturbation-rich pretraining data are essential for context-generalizable oncology tasks.
- [CellOT](../entities/CellOT.md) represents a different perturbation modeling path: it learns transport maps between control and treated populations without requiring a foundation-model-scale pretraining stage.
- Compared with broader atlas models such as [scGPT](../entities/scGPT.md) and [scFoundation](../entities/scFoundation.md), Tahoe-x1 puts much more weight on interventional coverage than on observational scale alone.

## Claimed Benefits

- Better representation of context-dependent perturbation effects than observational atlas training alone.
- More transferable latent spaces for few-shot and zero-shot response prediction in unseen cellular contexts.
- Stronger alignment with translational tasks such as target prioritization, drug-response ranking, and precision-oncology workflows.

## Caveats

- Large perturbation compendia are expensive to generate and may be biased toward available cell lines, assay platforms, or drug libraries.
- Strong results in perturbation-rich in vitro systems do not automatically imply equal performance in primary tissue or in vivo disease settings.
- Even when the representation is perturbation trained, downstream prediction may still depend on separate transport or transition modules rather than on one unified end-to-end simulator.

## Sources

- [Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters](../sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md)
- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
