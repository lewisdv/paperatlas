---
title: Conditional Monge Gap enables generalizable single-cell perturbation modelling
kind: paper
status: ingested
added: 2026-08-03T18:26:05+09:00
raw_source: raw/sources/driessen_2026_cmonge_generalizable_perturbation.pdf
---

# Conditional Monge Gap enables generalizable single-cell perturbation modelling

## Source

- File: [raw/sources/driessen_2026_cmonge_generalizable_perturbation.pdf](../../raw/sources/driessen_2026_cmonge_generalizable_perturbation.pdf)
- Added: 2026-08-03T18:26:05+09:00
- Authors: Alice Driessen, Dhruva Abhijit Rajwade, Benedek Harsanyi, Marianna Rapsomaniki, and Jannis Born
- Venue/status: *Nature Machine Intelligence* 8, 984–996 (2026); published 1 June 2026
- DOI: [10.1038/s42256-026-01242-8](https://doi.org/10.1038/s42256-026-01242-8)
- License shown in the supplied PDF: CC BY-NC-ND 4.0
- SHA-256: `31c68b21d4fe0d151d5fd9d97625f68a057f806cd824ef501fa4cbebcd20f6bb`

## Summary

- [CMonge](../entities/CMonge.md) is a conditional neural optimal-transport model for unpaired single-cell perturbation data.
- It learns one parameterized transport rule across contexts, rather than training an independent control-to-treated map for every drug and dose. Inputs include a source cell and a condition representation; the output is a predicted target cell produced by adding a learned shift.
- The `Conditional Monge Gap` objective combines distribution matching through Sinkhorn divergence with a Monge-Gap term that encourages cost-optimal transport.
- In this collection, it extends [CellOT](../entities/CellOT.md)'s distributional-transport branch toward generalization across doses, drugs, and drug combinations.

## Method

- Drug identity is represented with RDKit features derived from SMILES strings or, in an alternative setting, with mechanism-of-action information. Dose is encoded alongside drug features.
- Separate encoders form a condition embedding, which is combined with the source cell in a multilayer perceptron. The MLP predicts a condition-specific displacement vector.
- Multi-drug contexts are encoded with a DeepSets-style average pooling operation, allowing the model to accept an unordered set of drug representations.
- Training compares predicted and observed target-cell distributions without paired before/after cells. The loss contains a Sinkhorn-divergence distribution term and a conditional Monge-Gap regularizer.
- The model therefore predicts a population-level conditional distribution through transformed source cells; it does not identify a true matched target cell for each measured source cell.

## Data and Reported Evidence

- The central sci-Plex benchmark comprises `762,039` cells from A549, K562, and MCF7 cancer cell lines, treated with `188` compounds (including `187` drugs) at four doses: `10`, `100`, `1,000`, and `10,000` nM.
- The study evaluates in-sample contexts and held-out drug or dose regimes, and includes multiplexed `4i` protein-imaging perturbation data as a second modality setting.
- The paper reports stronger distributional and differential-expression agreement than condition-specific transport and conditional generative baselines in several held-out settings, with particular emphasis on out-of-sample dose and drug generalization.
- The reported evidence is benchmark-specific. It shows that structure-aware condition representations can help within these screens; it does not establish that arbitrary unseen perturbagens or cell types will generalize equally well.

## Interpretation Boundaries and Limitations

- Generalization depends on the quality and coverage of the supplied condition embedding. An unseen drug represented by chemical descriptors is not equivalent to proving a novel biological mechanism is captured.
- The model assumes a transport geometry and chosen ground cost that make the source and target populations comparable. Large state changes, poorly represented populations, or preprocessing artifacts can break this assumption.
- Distribution matching does not furnish cell-level causal correspondence. Predicted shifts, differential expression, and pathway effects remain model-assisted estimates.
- The supplied evaluations focus on drug perturbations and cancer cell lines. They should not be conflated with multigene perturbation generalization, where [GEARS](../entities/GEARS.md) uses a different graph-based inductive bias.

## Related Pages

- [CMonge](../entities/CMonge.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [CellOT](../entities/CellOT.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Squidiff](../entities/Squidiff.md)

## Open Questions

- Which chemical or mechanistic condition representation best supports out-of-sample biological response prediction?
- How does a globally conditioned transport map trade local perturbation fidelity against broad cross-condition reuse?
- Can the Monge-Gap formulation be extended to multimodal cell states, time-series paths, or experimentally validated causal interventions?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-03T18:26:05+0900
- Manifest: [raw/derived/opendataloader/driessen_2026_cmonge_generalizable_perturbation/opendataloader-run.json](../../raw/derived/opendataloader/driessen_2026_cmonge_generalizable_perturbation/opendataloader-run.json)
- Output: [raw/derived/opendataloader/driessen_2026_cmonge_generalizable_perturbation/driessen_2026_cmonge_generalizable_perturbation.md](../../raw/derived/opendataloader/driessen_2026_cmonge_generalizable_perturbation/driessen_2026_cmonge_generalizable_perturbation.md)
- Layout text: [raw/derived/pdftext/Driessen_2026_CMonge/Driessen_2026_CMonge.txt](../../raw/derived/pdftext/Driessen_2026_CMonge/Driessen_2026_CMonge.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
