# Virtual Instruments

## Definition

- Virtual instruments (VIs) are the AIVC paper's proposed neural-network tools that operate on universal representations of biological state.
- They serve as computational counterparts of laboratory instruments or interventions that read from, decode, or manipulate a virtual biological system.

## In AIVC

- Decoder VIs take a universal representation as input and produce human-readable outputs such as labels, images, structures, or predicted measurements.
- Manipulator VIs take a universal representation as input and output another universal representation, for example a predicted post-perturbation or future cell state.
- Because multiple VIs operate over the same shared representation, the paper argues that they could be reused across datasets, assays, and scientific questions.

## Claimed Benefits

- Enables in silico experiments that would otherwise be too expensive, slow, or impossible in the lab.
- Supports active lab-in-the-loop workflows by pairing predictions with uncertainty and suggesting informative next experiments.
- Provides a modular way to connect one biological state representation with many downstream readouts, perturbation prompts, and scientific interfaces.

## Caveats

- Useful VI behavior depends on the quality and calibration of the shared representation underneath it.
- The paper treats uncertainty estimation, trust, and biological fidelity as essential but still open design constraints.
- Many attractive use cases, especially for strong perturbations or complex dynamics, still depend on richer data and future modeling advances.

## Sources

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
