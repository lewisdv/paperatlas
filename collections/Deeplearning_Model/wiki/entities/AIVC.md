# AIVC

## Type

- Named system / proposed framework

## Definition

- AIVC, or AI virtual cell, is the paper's proposed multi-scale, multi-modal, large-neural-network-based framework for representing and simulating molecules, cells, and tissues across diverse states.
- The source frames it as a learned simulator and experimental scaffold rather than as one narrow benchmark model.

## Core Architecture

- Uses a universal representation (UR) that should align biological state across species, modalities, datasets, and contexts.
- Organizes modeling across three physical scales: molecular, cellular, and multicellular.
- Relies on virtual instruments (VIs) that either decode URs into human-readable outputs or manipulate URs to simulate interventions and trajectories.
- Envisions combining multiple AI model families, including sequence transformers and LLMs, vision models, diffusion-style generators, and graph-based models.

## Reported Uses

- In silico perturbation experiments and virtual screening.
- Phenotypic drug discovery and cell engineering.
- Precision oncology and spatial tumor-microenvironment analysis.
- Personalized diagnostics or digital-twin-style patient monitoring.

## Caveats

- The paper presents a roadmap and design vision, not a released end-to-end AIVC system with one validated benchmark suite.
- The framework depends on very large multimodal, multi-scale datasets plus shared infrastructure and collaborative governance.
- Dynamic molecular processes, interpretability, trust, privacy, and equitable representation are explicitly identified as unresolved challenges.

## Related

- [Universal Representation](../concepts/universal-representation.md)
- [Virtual Instruments](../concepts/virtual-instruments.md)
- [Source: How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
