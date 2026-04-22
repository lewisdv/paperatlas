---
title: MEA electrophysiology readouts
status: active
created: 2026-04-22T19:29:26+09:00
kind: entity
entity_type: assay-readout
---

# MEA electrophysiology readouts

## Current role in this corpus

MEA appears in this corpus as a shorthand for dish-level network-activity readouts that matter most in brain organoid protocol selection.

## Strong supporting pages

- [Generation of ‘semi-guided’ cortical organoids with complex neural oscillations](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [brain organoid는 functional readout에 따라 어떻게 고르는 게 맞나](../queries/20260420_172825_brain-functional-readout-selection.md)
- [Organ마다 assay가 약할 때 recovery move를 어떻게 다르게 잡아야 하나](../queries/20260420_191750_organ-specific-assay-recovery-playbook.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Working synthesis

- In this collection, MEA is not treated as a generic add-on. It is one of the clearest examples where readout compatibility changes which baseline protocol should be chosen in the first place.
- The semi-guided cortical branch is the main anchor because it ties oscillations, calcium imaging, and MEA readiness together as part of protocol design.
- MEA therefore sits at the point where organoid generation stops being the endpoint and becomes substrate preparation for network-level functional assays.

## Main tension

- richer dish-level functional readout versus extra protocol burden and readout-specific failure modes
- neural activity compatibility versus broader developmental diversity

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)

## Open questions

- Which brain organoid branches in this corpus are most likely to produce comparable MEA phenotypes across batches?
- When is MEA enough, and when does a project need host-circuit validation instead?
- How much protocol optimization should be spent on electrophysiology readiness before escalating to more complex models?
