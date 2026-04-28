---
title: "Designing escalation ladders for different disease-modeling goals"
status: active
created: 2026-04-20T19:17:51+09:00
---

# 질병 종류별로 organoid escalation ladder를 어떻게 짜야 하나

## Question

질병 모델링에서는 단순히 “어떤 organoid를 쓸까”보다, baseline organoid에서 assay layer, niche layer, host validation까지 어떤 순서로 complexity를 올릴지가 중요하다. 이 corpus 기준으로 질병 종류별 escalation ladder를 어떻게 짜는 것이 가장 합리적인가?

## Short answer

이 corpus는 **질병 archetype마다 escalation 순서가 다르다**고 말한다.

- **patient-specific cancer or donor-state disease**: donor platform에서 시작해 coculture or perturbation으로 넓힌다.
- **developmental neuro disease**: region-specific developmental baseline에서 시작해 functional readout으로 간다.
- **infection or barrier disease**: access correction과 exposure assay가 먼저다.
- **repair or regenerative disease**: host injury context가 비교적 빨리 필요하다.
- **niche-defined disease**: multicompartment model을 초기에 채택하는 편이 낫다.

즉 escalation은 한 방향의 complexity race가 아니라 **질병이 요구하는 validation sequence**다.

## Ladder table

| disease archetype | minimal starting point | next escalation | later escalation |
|---|---|---|---|
| donor-specific cancer / therapy response | [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md) or [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md) | xenotransplant or host-linked validation if needed |
| developmental neuro disease | [Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md) or region-specific brain baseline | [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md) | [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) if host circuit claim appears |
| infection / barrier disease | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md) | [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) or [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md) | host repair branch only if translational question appears |
| regenerative / injury disease | organ-specific baseline | injury or transplantation model such as [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) | extended host-function validation |
| niche-defined disease | [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md) or other multicompartment baseline | disease or screen readout on top of niche model | host branch if niche-host interface matters |

## 1. Donor-specific cancer ladders start simple and donor-preserving

[Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)는 donor-relevant screening platform을 제공한다. 여기서는 escalation의 첫 단계가 whole host가 아니라 **expandable donor platform 확보**다.

그 다음 branch는 보통:

- immune interaction이면 [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- genetic manipulation or longer platform leverage면 [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)

로 읽힌다.

즉 cancer ladder는 donor state를 잃지 않는 범위에서 **assay and perturbation complexity**를 먼저 올리고, host branch는 뒤로 미루는 편이 자연스럽다.

## 2. Developmental neuro disease ladders start from the right developmental context

[Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md)는 region-specific hippocampal disease baseline을 보여준다. 여기에 [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) 같은 functional readout layer나 [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md) 같은 perturbation layer를 붙일 수 있다.

이 ladder에서 host branch는 default가 아니다. [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)로 가는 시점은 **host circuit participation**이 claim이 될 때다.

즉 developmental neuro disease는:

1. right region
2. interpretable function or perturbation
3. host circuit validation if required

순으로 커진다.

## 3. Infection and barrier ladders start with access, not transplantation

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)는 infection/barrier ladder의 0단계가 geometry correction임을 보여준다. [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)는 그 다음 exposure branch를 operationalize한다.

[Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)는 disease, infection, development를 함께 다루는 more complex lung baseline을 제공한다.

따라서 infection/barrier 질환에서 흔한 ladder는:

1. access correction
2. exposure or microbial assay
3. richer tissue context if needed
4. host branch only when repair or translational relevance가 필요할 때

다.

## 4. Regenerative disease ladders escalate to host earlier

[Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)는 repair question에서 host injury context가 early escalation point가 될 수 있음을 보여준다.

이 type의 disease에서는:

- organoid establishment
- assay layer

보다 **repair in damaged tissue**가 더 빨리 핵심 endpoint가 된다. 그래서 regenerative ladder는 다른 disease보다 host branch가 앞당겨진다.

## 5. Niche-defined disease should not wait too long to adopt niche-rich models

[Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)는 some diseases가 multicompartment niche 없이 아예 설득력을 잃는다는 점을 보여준다.

이런 경우 escalation ladder는:

1. simple epithelial baseline
2. niche model

이 아니라, 종종 **niche model에서 출발**하는 것이 맞다.

즉 niche-defined disease는 complexity를 늦게 붙이는 대신 **질문에 맞는 complexity를 초기에 채택**해야 한다.

## A shared escalation rule across diseases

모든 ladder에 공통된 규칙도 있다.

1. **최소한의 baseline에서 시작한다**
2. **질병 질문이 요구하는 missing layer를 하나씩 추가한다**
3. **host-only claim이 생길 때만 host validation으로 간다**

이 원칙은 [질병 모델링에서는 phenotype source를 먼저 어떻게 구분해야 하나](20260420_174125_disease-phenotype-source-triage.md)에서 제시한 source triage를 **실제 순서 설계**로 옮긴 것이다.

## Rule of thumb

- **cancer precision model**: donor platform -> coculture or perturbation -> host if needed
- **developmental neuro model**: region-specific baseline -> function or perturbation -> host circuit if needed
- **infection/barrier model**: access -> exposure -> richer context -> host later
- **repair model**: host branch earlier
- **niche disease**: multicompartment baseline earlier

## What this query does not settle

- 같은 disease에서도 endpoint가 달라지면 ladder가 달라질 수 있다.
- immune host models, stromal partial-support models 같은 중간 단계는 이 corpus에서 충분히 풍부하지 않다.
- 질병별 ladder의 cost and throughput 비교도 정량화되어 있지 않다.

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Host circuit engagement](../entities/host-circuit-engagement.md)

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
