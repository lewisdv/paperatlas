# How does this collection handle uncertainty, weak reference coverage, and low-confidence biological state assignment?

## Short Answer

- This collection currently shows three distinct responses to weakly supported biological state assignment.
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md) keeps some label information by backing off to a broader node.
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md), as implemented by [SCimilarity](../entities/SCimilarity.md), keeps the retrieved state but lowers confidence when the atlas does not cover the query well.
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md), as implemented by [HNOCA](../entities/HNOCA.md), diagnoses uncertainty at the system level by asking whether a protocol or organoid state is adequately represented by a primary reference at all.

## 1. Fallback Labels Under Within-Hierarchy Uncertainty

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md) is the clearest direct treatment of annotation uncertainty.
- Its solution is not to force a leaf label and not to collapse straight to `unknown`, but to return an internal node when the model lacks enough confidence for a fine-grained assignment.
- This strategy is most useful when the queried state is still plausibly inside the known hierarchy but the precise subtype is uncertain.
- The tradeoff is that this works only if the hierarchy follows transcriptomic structure well enough to make the broader label biologically meaningful.

## 2. Confidence Downgrading Under Weak Atlas Coverage

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md) handles uncertainty differently.
- [SCimilarity](../entities/SCimilarity.md) does not mainly solve low confidence by moving to a broader label node. Instead, it uses representation confidence to indicate that a query falls in a weakly supported region of the reference atlas.
- This is a better fit when the problem is not ambiguity between nearby known labels, but lack of strong training coverage for the queried tissue, disease, or in vitro context.
- The tradeoff is that confidence flags tell the user to be cautious, but they do not by themselves provide a graded fallback ontology answer the way hierarchical partial rejection does.

## 3. Fidelity and Coverage Diagnosis At The System Level

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) and [HNOCA](../entities/HNOCA.md) push the problem one level higher.
- The main question is not whether one cell should get a broader label, but whether an entire organoid protocol or projected dataset adequately covers the relevant primary developmental reference.
- This is closer to a `coverage and mismatch diagnosis` framework than to a classic uncertainty-threshold classifier.
- Its strength is that it can tell whether poor performance reflects missing states, immature timing, or common in vitro stress rather than just uncertain label assignment.
- Its tradeoff is that it is more resource- and reference-dependent, and it does not directly replace a per-cell annotation policy.

## What These Three Modes Suggest

- The collection does not currently have one unified uncertainty framework.
- Instead, uncertainty is being handled at three different levels:
- label level through hierarchical fallback
- query level through representation-confidence scoring
- system level through reference-fidelity and coverage benchmarking

## What Seems Missing In The Current Knowledge Base

- The currently ingested sources do not yet provide a dedicated method centered on explicit novel-cell-type discovery that is cleanly separated from confidence rejection or atlas coverage warnings.
- They also do not present one unified framework that links hierarchical fallback, retrieval confidence, and fidelity benchmarking into a single decision policy.

## Bottom Line

- The collection already supports a useful distinction: not every low-confidence state-assignment problem is the same problem.
- If the state belongs to a known hierarchy but is hard to localize finely, hierarchical partial rejection is the most appropriate current answer.
- If the query is weakly covered by the training atlas, SCimilarity-style confidence downgrading is the more natural response.
- If the problem is whether a whole in vitro system is adequately represented by a primary reference, HNOCA-style fidelity benchmarking is the strongest current answer in this collection.

## Pages Used

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md)
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [SCimilarity](../entities/SCimilarity.md)
- [HNOCA](../entities/HNOCA.md)
