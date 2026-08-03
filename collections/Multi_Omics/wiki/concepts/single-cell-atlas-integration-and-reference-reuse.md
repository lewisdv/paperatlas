# Single-cell atlas integration and reference reuse

## Current position

Single-cell resources become reusable when raw datasets are normalized into comparable references, but reuse must preserve source-study uncertainty.

## Evidence in this collection

- [PanglaoDB](../sources/20260718_234516_franzen-2019-panglaodb-a-web-server-for.md) demonstrates database-scale preprocessing and marker curation across heterogeneous public studies.
- [Human chromatin accessibility atlas](../sources/20260718_234516_zhang-2021-a-single-cell-atlas-of-chromatin.md) shows how cross-tissue references can localize candidate regulatory elements and noncoding trait associations.
- [Systemic-sclerosis immune profiling](../sources/20260718_234516_shimagami-2025-single-cell-analysis-reveals-immune-cell.md) illustrates the opposite direction: a clinically stratified cohort uses single-cell resolution to identify complication-specific states.

## Working rule

Use broad atlases to define candidate identities and regulatory context, then return to cohort-specific data for disease association and to perturbation for causality. Do not treat reference mapping as validation by itself.

## Open questions

- How should batch, donor, tissue-processing, and protocol uncertainty be propagated into downstream cell labels?
- Which atlas-derived regulatory links have direct perturbational support?

