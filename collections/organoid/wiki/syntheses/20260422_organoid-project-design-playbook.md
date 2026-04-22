---
title: Organoid project design playbook
status: active
created: 2026-04-22T19:13:10+09:00
---

# Organoid project design playbook

## Scope

- This synthesis compresses the 2026-04-20 decision-query burst into one project-design page.
- Use it when the question is not "which paper says what?" but "what should we build next, and in what order?"
- It assumes the current active source corpus is already curated and deep-ingested.

## The shortest usable rule set

1. Start from the biological bottleneck, not from the fanciest available model.
2. Choose the minimal baseline that preserves the phenotype source.
3. Fix access, geometry, or baseline stability before adding more biological partners.
4. Add only the next layer that could change the answer.
5. Escalate to host validation only when the endpoint is genuinely host-defined.

## Step 1: choose the right baseline

| Question type | Best first baseline | Why | Entry points |
|---|---|---|---|
| organ emergence, regional patterning, lineage timing | developmental hPSC organoid | the protocol question is developmental control itself | [언제 developmental hPSC organoid 대신 adult/patient-derived platform을 선택해야 하나](../queries/20260420_172028_developmental-vs-patient-derived-platform-selection.md), [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md) |
| donor-specific disease, tumor response, translational screening | adult or patient-derived organoid platform | donor state and expandable epithelial practicality matter more than organogenesis recapitulation | [언제 developmental hPSC organoid 대신 adult/patient-derived platform을 선택해야 하나](../queries/20260420_172028_developmental-vs-patient-derived-platform-selection.md), [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md) |
| boundary biology, appendages, constitutive niche dependence, multicompartment support | niche-rich or multi-lineage organoid | the answer changes if the extra compartment is absent | [얼마나 복잡한 organoid가 정말 필요한가](../queries/20260420_172824_complexity-vs-throughput-tradeoff.md), [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md) |

## Step 2: choose the first added layer

| Dominant missing function | First move | Why | Do not confuse it with |
|---|---|---|---|
| apical access, exposure geometry, barrier entry | polarity or access correction | the readout surface is blocked | a missing immune or vascular compartment |
| defined immune, microbial, or partner interaction | coculture or exposure branch | the phenotype is an interaction event | host validation by default |
| hypoxia, stressed core, perfusion ceiling, maturation plateau | vascular or perfusion support | tissue support is limiting the baseline | partner-specific interaction failure |
| repair, host circuit participation, circulation-linked integration | transplantation or host validation | the endpoint lives in host context | a dish-only interaction assay |
| constitutive stromal, vascular, or hematopoietic dependence | niche-rich baseline or model switch | the model is over-reductionist without the missing compartment | a single add-on layer |

This is the main sequence the corpus keeps repeating:

1. Access first if geometry is wrong.
2. Defined partner next if the phenotype is an interaction.
3. Vascular support next if the tissue itself is collapsing.
4. Host validation only when the claim remains host-defined.

## Step 3: decide how much complexity is enough

| Complexity tier | When it is the best choice | Representative branch |
|---|---|---|
| controlled and throughput-oriented | screening, perturbation comparison, batch consistency | miniaturized brain organoids, patient-derived cancer platforms |
| intermediate complexity with stronger readouts | later-stage function matters, but not every compartment is necessary | long-term brain maturation, semi-guided neural oscillation workflows, distal lung assay systems |
| multi-lineage or niche-rich systems | extra compartments materially change the answer | bone marrow niche, hepato-biliary-pancreatic boundary systems, blood-generating heart-forming organoids |

The practical rule is blunt:

- increase complexity only when you can name the compartment that would otherwise change the conclusion
- stay simple when screening, reproducibility, or causal attribution is the main goal
- choose intermediate complexity when readout quality matters more than maximal realism

## Step 4: escalation ladders by disease archetype

| Disease archetype | Minimal starting point | Next escalation | Later escalation |
|---|---|---|---|
| donor-specific cancer or therapy response | donor-preserving PDO baseline | coculture, perturbation, or editing | host-linked validation only if needed |
| developmental neuro disease | region-appropriate developmental baseline | functional readout or perturbation | host circuit validation if the claim becomes host-facing |
| infection or barrier disease | access-corrected epithelial baseline | exposure or coculture assay | richer context or host branch later |
| regenerative or injury disease | organ-specific baseline | injury or transplantation branch early | extended host-function validation |
| niche-defined disease | multicompartment baseline early | disease or screen readout on top of the niche model | host interface layer if needed |

The important point is that escalation is not a generic race toward more complexity. It is a claim-matched sequence.

## Step 5: recover weak assays in an organ-specific way

| Organ or platform | First recovery move | Only then consider |
|---|---|---|
| brain | reduce heterogeneity and move to readout-compatible formats | vascular support or host circuit validation |
| pancreas | push maturation benchmarks rather than marker lists | extra complexity or host claims |
| kidney | fix segment identity, then add perfusion and polarity gain | maturity claims from static markers alone |
| intestine | open access and exposure geometry | host repair escalation |
| patient-derived cancer | stabilize donor platform and expansion | coculture, editing, xenotransplantation |

This is where the corpus is especially useful: weak assay signal does not mean the same thing in every organ system.

## Shared anti-patterns

- Adding a pooled screen before the baseline organoid is stable.
- Treating an access problem as if it were a missing compartment problem.
- Using host validation to rescue a poor in vitro baseline.
- Choosing the highest-complexity model for a screening-first question.
- Applying the same assay-recovery logic across brain, pancreas, kidney, intestine, and PDO systems.
- Assuming host validation is automatically stronger than a well-matched coculture assay.

## Best entry points inside this wiki

- [언제 developmental hPSC organoid 대신 adult/patient-derived platform을 선택해야 하나](../queries/20260420_172028_developmental-vs-patient-derived-platform-selection.md)
- [baseline organoid가 만들어진 뒤 어떤 assay 또는 engineering layer를 먼저 붙여야 하나](../queries/20260420_172030_assay-and-engineering-layer-selection.md)
- [얼마나 복잡한 organoid가 정말 필요한가](../queries/20260420_172824_complexity-vs-throughput-tradeoff.md)
- [Immune, vascular, niche 보완 중 무엇을 먼저 붙여야 하나](../queries/20260420_190409_immune-vascular-vs-niche-compensation-priority.md)
- [언제 coculture로 충분하고 언제 host validation이 필요한가](../queries/20260420_191749_coculture-vs-host-validation-for-interaction-questions.md)
- [Organ마다 assay가 약할 때 recovery move를 어떻게 다르게 잡아야 하나](../queries/20260420_191750_organ-specific-assay-recovery-playbook.md)
- [질병 종류별로 organoid escalation ladder를 어떻게 짜야 하나](../queries/20260420_191751_disease-specific-organoid-escalation-ladders.md)

## Entity shortcuts

- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)
- [CRISPR-Cas9 and next-generation CRISPR editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md)
- [MEA electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
- [Optical coherence tomography (OCT)](../entities/optical-coherence-tomography-oct.md)
- [NLRP3 inflammasome](../entities/nlrp3-inflammasome.md)

## Concept entry points

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Sources used

- [언제 developmental hPSC organoid 대신 adult/patient-derived platform을 선택해야 하나](../queries/20260420_172028_developmental-vs-patient-derived-platform-selection.md)
- [baseline organoid가 만들어진 뒤 어떤 assay 또는 engineering layer를 먼저 붙여야 하나](../queries/20260420_172030_assay-and-engineering-layer-selection.md)
- [얼마나 복잡한 organoid가 정말 필요한가](../queries/20260420_172824_complexity-vs-throughput-tradeoff.md)
- [Immune, vascular, niche 보완 중 무엇을 먼저 붙여야 하나](../queries/20260420_190409_immune-vascular-vs-niche-compensation-priority.md)
- [언제 coculture로 충분하고 언제 host validation이 필요한가](../queries/20260420_191749_coculture-vs-host-validation-for-interaction-questions.md)
- [Organ마다 assay가 약할 때 recovery move를 어떻게 다르게 잡아야 하나](../queries/20260420_191750_organ-specific-assay-recovery-playbook.md)
- [질병 종류별로 organoid escalation ladder를 어떻게 짜야 하나](../queries/20260420_191751_disease-specific-organoid-escalation-ladders.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
