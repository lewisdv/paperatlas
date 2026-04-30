# Hierarchical Partial Rejection

## Definition

- Hierarchical partial rejection is a prediction strategy that returns an intermediate label in a hierarchy when a model is not confident enough to assign a leaf label.
- In this collection, the concept is specifically about uncertainty-aware single-cell annotation, where the fallback is a broader cell-type label rather than a complete abstention.

## In This Collection

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md) is the direct source and compares partial rejection against full rejection and no rejection.
- Compared with full rejection, the method aims to preserve more label information by exploiting transcriptomically meaningful cell-type hierarchies.
- The paper also notes that bottom-up partial rejection can be layered on top of flat classifiers if reliable class-probability outputs are available.
- [SCimilarity](../entities/SCimilarity.md) addresses a neighboring uncertainty problem through low-confidence retrieval flags; unlike partial rejection, it responds to weak atlas coverage by downgrading confidence rather than backing off to an internal label node.
- [HNOCA](../entities/HNOCA.md) provides a third adjacent mode, where uncertainty appears as missing or weakly matched reference coverage during fidelity benchmarking rather than as a per-cell fallback label.
- Generative-first model families in this collection, such as [scGPT](../entities/scGPT.md) and [C2S-Scale](../entities/C2S-Scale.md), are broader in task scope but are not currently represented here by one comparably explicit fallback-label mechanism.
- Compared with [Gene-Level Perturbation Uncertainty](gene-level-perturbation-uncertainty.md), the uncertainty object here is label depth in a hierarchy, not whether an intervention effect estimate is directionally and quantitatively trustworthy.

## Claimed Benefits

- Retains useful label information under uncertainty instead of collapsing to `unknown`.
- Makes hierarchical annotation more useful in practical atlas annotation settings where confidence varies by cell and label depth.
- Provides a principled way to inspect threshold behavior using accuracy-rejection curves.

## Caveats

- The approach depends on the hierarchy matching transcriptomic relationships; ontology structure alone may be misleading.
- Confidence-threshold rejection mainly addresses aleatoric uncertainty and does not solve novel cell-type detection by itself.
- Optimal rejection thresholds vary across classifiers and datasets, so there is no one-size-fits-all setting.

## Sources

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md)
