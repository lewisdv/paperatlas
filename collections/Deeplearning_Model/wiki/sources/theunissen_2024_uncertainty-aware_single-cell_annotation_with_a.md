---
title: Uncertainty-aware single-cell annotation with a hierarchical reject option
kind: paper
status: ingested
added: 2026-04-29T22:01:53+09:00
raw_source: raw/sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.pdf
---

# Uncertainty-aware single-cell annotation with a hierarchical reject option

## Source

- File: [raw/sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.pdf](../../raw/sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.pdf)
- Added: 2026-04-29T22:01:53+09:00
- Venue/status: Bioinformatics article; advance access 5 March 2024
- Authors: Lauren Theunissen, Thomas Mortier, Yvan Saeys, and Willem Waegeman
- DOI: `10.1093/bioinformatics/btae128`

## Summary

This paper studies how single-cell annotation systems should handle predictive uncertainty, comparing no rejection, full rejection, and hierarchy-aware partial rejection for both flat and hierarchical probabilistic classifiers. Its main result is that when rejection is used, hierarchical classifiers plus partial rejection retain more useful label information than simply emitting `unknown`. In this collection, the paper matters because it adds an uncertainty-management axis to the annotation thread and shows that label hierarchies can be used as a graded fallback rather than an all-or-nothing abstention mechanism.

## Methods

- The study compares three annotation settings: no rejection, full rejection, and partial rejection.
- It evaluates both flat classifiers and hierarchical classifiers, using logistic regression, linear SVM, and random forests as the underlying probabilistic models.
- Five public single-cell transcriptomics datasets with available hierarchies are used: AMB, COVID, Azimuth PBMC, Flyhead, and Flybody.
- Rejection thresholds are analyzed with accuracy-rejection curves, which vary the confidence cutoff from `0` to `1` and measure both retained accuracy and rejection percentage.
- The hierarchy-aware setting supports partial rejection by returning an internal node rather than a leaf label when confidence is insufficient for a fine-grained assignment.

## Key Claims

- Hierarchical classifiers are superior to flat classifiers when rejection is applied, because they can partially reject to an intermediate label instead of discarding the annotation entirely.
- Partial rejection is preferable to full rejection because it preserves a significant amount of label information under uncertainty.
- Without rejection, flat and hierarchical annotation can perform similarly as long as the hierarchy reflects transcriptomic relationships rather than only ontology structure.
- Rejection thresholds should be tuned empirically for each use case, because model and dataset rejection behavior vary substantially.

## Evidence

- The paper explicitly evaluates three rejection strategies across five datasets and reports that hierarchical classifiers outperform flat ones under rejection while preserving more label information through partial rejection.
- Accuracy-rejection curves show substantial variation across classifiers: logistic regression rejects less aggressively at low thresholds than SVM or random forests, so the optimal threshold is setup-specific rather than universal.
- For annotation without rejection, the paper reports broadly similar flat versus hierarchical performance on manually annotated datasets such as AMB, Azimuth PBMC, and COVID.
- The Flyhead and Flybody results show that hierarchical annotation can degrade when ontology-based hierarchies do not align well with transcriptomic relationships.
- The paper also reports that technical variation can materially affect interdataset performance, whereas biological replicates sequenced with the same protocol remain much more consistent.

## Limitations

- The study focuses on confidence-based rejection, which the paper interprets as aleatoric uncertainty; it does not solve novel cell-type detection or broader epistemic uncertainty.
- The benefits of hierarchical rejection depend on having a hierarchy that matches transcriptomic structure, which is not guaranteed for ontology-derived trees.
- This is an evaluation paper for annotation strategy, not a new foundation model or atlas-scale embedding system.
- Marker-gene interpretability remains imperfect in some lower-level hierarchical classifiers even when predictive performance is acceptable.

## Related Pages

- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [SCimilarity](../entities/SCimilarity.md)

## Open Questions

- How should this collection compare confidence-aware annotation methods with retrieval-style annotation systems such as SCimilarity?
- If future sources add stronger epistemic-uncertainty or out-of-distribution detection, should those be separated from confidence-threshold rejection methods?
- When does a biologically curated ontology help annotation, and when does it become too structurally disconnected from transcriptomic similarity to be useful?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:01:09+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.pdf -o /tmp/odl-check-theunissen2 -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a/opendataloader-run.json](../../raw/derived/opendataloader/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a/opendataloader-run.json)
- Output: [raw/derived/opendataloader/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md](../../raw/derived/opendataloader/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
