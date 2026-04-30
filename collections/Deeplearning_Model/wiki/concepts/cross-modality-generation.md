# Cross-modality Generation

## Definition

- Cross-modality generation is the task of reconstructing unmeasured biological or phenotypic modalities from observed inputs by using a shared latent representation.
- In this collection, the AURORA paper treats it as a practical route from sparse measurements toward richer personalized health profiles.

## In AURORA

- Seven modalities are aligned into a common latent space across fragmented and partially paired datasets.
- Missing modalities are decoded from the shared embedding, allowing one measured modality to stand in for others.
- The generated outputs are then reused for downstream tasks such as aging clocks, disease prediction, and perturbation simulation.
- Compared with [Multimodal Foundation Models](multimodal-foundation-models.md), this is a narrower operational function inside a broader multimodal paradigm: the focus is specifically reconstructing missing modalities rather than defining the whole pretraining agenda.
- Compared with [Multi-Omic Developmental Atlases](multi-omic-developmental-atlases.md), the goal here is generation from partial observations, not building a reference substrate for developmental mapping and benchmarking.

## Claimed Benefits

- Reduces the impact of missing modalities and batch fragmentation.
- Expands effective training coverage for downstream predictors.
- Makes it possible to derive multimodal risk estimates from simpler inputs such as routine blood tests or facial imaging.

## Caveats

- The source explicitly says that flawless molecular reconstruction from limited unimodal inputs is still aspirational.
- Generated modalities still depend on paired multimodal ground truth for training and calibration.

## Sources

- [A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
