# AURORA

## Type

- Named system / model

## Definition

- AURORA expands to "AI unification and reconstruction of omics reassembly atlas."
- The source presents AURORA as a generative deep-learning framework for unifying fragmented human multi-omics and phenotypic data into a shared latent representation.

## Core Architecture

- AURORA Unification learns feature embeddings for heterogeneous modalities and aligns modality-specific sample embeddings in a shared latent space.
- One latent dimension is explicitly disentangled to encode age, while the remaining dimensions preserve age-confounding biological variation.
- A decoder reconstructs missing or target modalities from the unified embedding.
- AURORA Perturbation applies latent-space condition effects to simulate lifestyle, medication, or other intervention changes.

## Reported Uses

- Cross-modality reconstruction of missing data.
- Multimodal aging clocks and biological age deviation estimates.
- Chronic disease risk prediction in China cohorts and the UK Biobank.
- In silico lifestyle and drug perturbation, including personalized metformin-response stratification.
- A proof-of-concept AI agent for multimodal report generation from sparse inputs.

## Caveats

- The source states that perfect molecular reconstruction from sparse unimodal data is not yet realistic.
- The source also notes that prospective validation and experimental follow-up are still needed for newly proposed interventions.

## Related

- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Source: A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](../sources/chen_2026_a_generative_ai_framework_unifies.md)
