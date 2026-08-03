# Continual Single-Cell Atlas Integration

## Definition

- Continual integration updates a single-cell atlas as batches arrive over time while trying to preserve previously learned biological and technical structure.
- It is a `data-lifecycle` axis, not another integration geometry: a vertical, horizontal, diagonal, or mosaic dataset can each be integrated offline or continually.

## Update Strategies

- `Offline reintegration`: train again on all data observed so far. It is an upper benchmark for retention but grows in time and memory as the atlas expands.
- `Fixed-model generalization`: train a reference once and infer new batches without changing parameters. It is cheap but can fail on unseen biology, technology, or modality combinations.
- `Sequential fine-tuning`: update parameters using only the new batch. It adapts to novelty but risks catastrophic forgetting of earlier batches.
- `Rehearsal-based continual learning`: update on the new batch plus a bounded memory of older cells. This reduces full retraining while making memory selection central to the result.

## Design Requirements

- Preserve historical batches and rare states rather than optimizing only the newest input.
- Accommodate new features or modalities without discarding previously learned encoders and decoders.
- Keep a bounded, representative rehearsal memory; both interbatch proportions and intrabatch cell-state coverage matter.
- Recompute or version prior embeddings, labels, and imputed values after a model update, because they can change with the updated parameters.
- Record arrival order, preprocessing, model version, and memory composition as part of the atlas provenance.

## Evaluation

- Standard integration metrics still assess batch correction, modality alignment, and biological conservation.
- Continual-learning measures add historical retention: final average performance across earlier tasks and backward transfer, which exposes post-update degradation of earlier integrations.
- A meaningful comparison needs both an offline all-data reference and a no-rehearsal fine-tuning control; neither a static query mapper nor an offline score alone tests forgetting.

## Evidence Boundaries

- A bounded memory is an approximation, not a complete historical atlas. Results can depend on capacity, sampling design, and arrival order.
- Success on a staged benchmark does not establish that a deployed shared atlas will remain stable across new cohorts, changing protocols, or novel modalities.
- Continual label transfer and imputation remain predictions. Updating an atlas can refine them but does not convert them into newly measured or causal biological evidence.

## Related Methods

- [MIRACLE](../entities/MIRACLE.md) provides a rehearsal-based continual-learning wrapper around [MIDAS](../entities/MIDAS.md) for RNA, ATAC, and ADT mosaic integration.
- [StabMap](../entities/StabMap.md) addresses static multi-hop connectivity through reference projections; it does not itself specify how a shared atlas should retain prior information across repeated model updates.
- [scVAEIT](../entities/scVAEIT.md) and [MultiVI](../entities/MultiVI.md) are static probabilistic integration baselines in this collection rather than demonstrated continual-learning systems.

## Sources

- [Continual integration of single-cell multimodal data with MIRACLE](../sources/zhou_2026_miracle_continual_multimodal_integration.md)
