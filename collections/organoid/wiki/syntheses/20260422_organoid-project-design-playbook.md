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

If the project is donor-derived cancer rather than generic adult-platform work, add one extra gate before calling the baseline screening-ready:

- specimen adequacy
- line stability and expansion
- freeze-thaw recovery
- pathology or molecular concordance
- assay-endpoint credibility

This is the shortest translation of the new PDO-readiness rubric: do not treat "patient-derived" as equivalent to "treatment-guidance ready."

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

## Step 3: change the stack by organ, not just by ambition

| Organ branch | First bottleneck | What screening-ready means first |
|---|---|---|
| pancreas | maturity | secretion competence and believable GSIS-like function |
| intestine | access | apical or basal access, controlled exposure, or chip-enabled compartment sampling |
| BBB | barrier readout | selective compound entry or exclusion in a tri-cell barrier assay |
| lung | baseline complexity | the baseline must already preserve the disease or infection context before assay inflation starts |

This is one of the main practical takeaways from the April 23 query burst: the first screening bottleneck is not shared across organs.

## Step 4: decide how much complexity is enough

| Complexity tier | When it is the best choice | Representative branch |
|---|---|---|
| controlled and throughput-oriented | screening, perturbation comparison, batch consistency | miniaturized brain organoids, patient-derived cancer platforms |
| intermediate complexity with stronger readouts | later-stage function matters, but not every compartment is necessary | long-term brain maturation, semi-guided neural oscillation workflows, distal lung assay systems |
| multi-lineage or niche-rich systems | extra compartments materially change the answer | bone marrow niche, hepato-biliary-pancreatic boundary systems, blood-generating heart-forming organoids |

The practical rule is blunt:

- increase complexity only when you can name the compartment that would otherwise change the conclusion
- stay simple when screening, reproducibility, or causal attribution is the main goal
- choose intermediate complexity when readout quality matters more than maximal realism

## Step 5: escalation ladders by disease archetype

| Disease archetype | Minimal starting point | Next escalation | Later escalation |
|---|---|---|---|
| donor-specific cancer or therapy response | donor-preserving PDO baseline | coculture, perturbation, or editing | host-linked validation only if needed |
| developmental neuro disease | region-appropriate developmental baseline | functional readout or perturbation | host circuit validation if the claim becomes host-facing |
| infection or barrier disease | access-corrected epithelial baseline | exposure or coculture assay | richer context or host branch later |
| regenerative or injury disease | organ-specific baseline | injury or transplantation branch early | extended host-function validation |
| niche-defined disease | multicompartment baseline early | disease or screen readout on top of the niche model | host interface layer if needed |

The important point is that escalation is not a generic race toward more complexity. It is a claim-matched sequence.

For donor-derived cancer, a compact three-stop ladder is often more useful than a generic "keep escalating" rule:

1. compact ex vivo validation when the claim is tumor-intrinsic response
2. immune reconstruction when the missing layer is a defined immune partner
3. PDO-X when host-restored signaling, metastasis, or stromal biology could change the answer

## Step 6: recover weak assays in an organ-specific way

| Organ or platform | First recovery move | Only then consider |
|---|---|---|
| brain | reduce heterogeneity and move to readout-compatible formats | vascular support or host circuit validation |
| pancreas | push maturation benchmarks rather than marker lists | extra complexity or host claims |
| kidney | fix segment identity, then add perfusion and polarity gain | maturity claims from static markers alone |
| intestine | open access and exposure geometry | host repair escalation |
| patient-derived cancer | stabilize donor platform and expansion | coculture, editing, xenotransplantation |

This is where the corpus is especially useful: weak assay signal does not mean the same thing in every organ system.

## Step 7: choose the vascular route by endpoint

| Route | Best fit | Best current anchor |
|---|---|---|
| flow or perfusion | organ-specific in-dish maturation, especially kidney | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) |
| TF-driven vascularization | integrated vascular-like support inside brain organoids | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md) |
| mesodermal progenitor mixing | reusable multicompartment vascular addition across contexts | [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| stand-alone vessel organoid | vessel-only baseline or programmable vascular branch definition | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md), [L 2026](../sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md) |
| transplantation | repair, circulation integration, or host-only validation | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |

This is the shortest version of the new vascularization-route query: do not collapse all vascular moves into one generic "more vascularized" option.

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
- [PDO가 treatment-guidance형 translational screening에 들어갈 준비가 됐는지 어떻게 판정해야 하나](../queries/20260423_1554_pdo-readiness-rubric-for-treatment-guidance-screening.md)
- [donor-derived cancer work는 언제 compact ex vivo validation에서 멈추고 언제 immune reconstruction이나 PDO-X로 올라가야 하나](../queries/20260423_1600_compact-ex-vivo-vs-immune-reconstruction-vs-pdo-x.md)
- [pancreas, intestine, BBB, lung에서는 screening stack를 어떻게 다르게 짜야 하나](../queries/20260423_1620_organ-specific-screening-stacks-pancreas-intestine-bbb-lung.md)
- [flow, TF-driven vascularization, mesodermal mixing, stand-alone vessel addition, host transplantation은 organ과 질문에 따라 어떻게 골라야 하나](../queries/20260423_1626_vascularization-routes-by-organ-and-question.md)

## Entity shortcuts

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)
- [CRISPR-Cas9 and next-generation CRISPR editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md)
- [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
- [Host circuit engagement](../entities/host-circuit-engagement.md)
- [MEA electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
- [Organ-on-chip](../entities/organ-on-chip.md)
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
- [PDO가 treatment-guidance형 translational screening에 들어갈 준비가 됐는지 어떻게 판정해야 하나](../queries/20260423_1554_pdo-readiness-rubric-for-treatment-guidance-screening.md)
- [donor-derived cancer work는 언제 compact ex vivo validation에서 멈추고 언제 immune reconstruction이나 PDO-X로 올라가야 하나](../queries/20260423_1600_compact-ex-vivo-vs-immune-reconstruction-vs-pdo-x.md)
- [pancreas, intestine, BBB, lung에서는 screening stack를 어떻게 다르게 짜야 하나](../queries/20260423_1620_organ-specific-screening-stacks-pancreas-intestine-bbb-lung.md)
- [flow, TF-driven vascularization, mesodermal mixing, stand-alone vessel addition, host transplantation은 organ과 질문에 따라 어떻게 골라야 하나](../queries/20260423_1626_vascularization-routes-by-organ-and-question.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
