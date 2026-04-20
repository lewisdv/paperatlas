---
title: "Triage disease models by the source of the phenotype"
status: active
created: 2026-04-20T17:41:25+09:00
---

# 질병 모델링에서는 phenotype source를 먼저 어떻게 구분해야 하나

## Question

Organoid disease modeling에서는 "어떤 organoid를 쓸까"를 너무 빨리 묻게 되기 쉽다. 하지만 실제로는 phenotype가 donor genotype에서 오는지, developmental state에서 오는지, external exposure에서 오는지, niche나 host context에서 오는지 먼저 갈라야 할 것 같다. 이 corpus에서는 disease model을 어떤 phenotype source 기준으로 triage하는 것이 가장 합리적인가?

## Short answer

이 corpus가 주는 가장 중요한 규칙은, **질병 phenotype의 원천을 먼저 분류하고 그다음 organoid를 고르라**는 것이다.

- **donor- or genotype-intrinsic phenotype**면 patient-derived 또는 disease-specific iPSC branch
- **developmental emergence phenotype**면 guided/developmental hPSC organoid branch
- **exposure- or interaction-driven phenotype**면 baseline organoid + assay layer
- **niche- or multicompartment-driven phenotype**면 richer niche model
- **host-response, repair, integration phenotype**면 transplantation or host-context validation

즉 disease modeling의 첫 질문은 "어떤 organ인가"보다 **질병 신호가 어디서 생기는가**에 가깝다.

## Phenotype-source decision table

| phenotype source | 먼저 볼 모델 | 왜 이게 맞는가 | 대표 근거 |
|---|---|---|---|
| donor specificity / patient state | adult or patient-derived expandable platform | donor biology를 가장 직접적으로 보존 | [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md), [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md) |
| disease emerging during lineage specification or regional development | developmental or region-specific hPSC organoid | phenotype가 발달 과정에서 생기므로 developmental context가 필요 | [Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md), [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md) |
| phenotype requiring external exposure or interacting partner | stable baseline + assay extension | 외부 자극이 없으면 phenotype 자체가 드러나지 않음 | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md), [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| phenotype requiring niche completeness | multi-lineage or niche-rich organoid | single epithelial or single-lineage model로는 병리 논리가 무너짐 | [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md), [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md) |
| phenotype requiring host repair or integration | transplantation / host engagement | in vitro만으로는 disease relevance가 불충분 | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) |

## 1. Use donor-derived platforms when the disease signal lives in the donor

[Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)는 donor or tumor state를 최대한 가깝게 유지하면서 downstream drug-screening으로 가는 branch를 보여준다. [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)도 stable patient-derived culture에서 engineering과 xenotransplantation을 이어 붙인다.

이런 모델은 특히 다음에 맞는다.

- 환자별 therapy response
- donor-specific tumor behavior
- patient-state preservation이 핵심인 translational question

반대로 multicompartment developmental context를 강하게 복원하진 않는다.

## 2. Use developmental organoids when the disease emerges during formation

[Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md)는 hippocampal identity를 가진 disease-oriented spheroid branch를 제공한다. [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)는 development, infection, disease를 한 workflow에서 다루려는 distal lung organoid branch다.

이 계열은 phenotype가 다음에서 생길 때 더 맞는다.

- 특정 regional identity가 형성되는 과정
- lineage emergence 자체의 실패
- immature but disease-relevant state가 핵심일 때

즉 질병이 "완성된 조직의 반응"보다 **만들어지는 과정의 왜곡**에 가까우면 developmental system이 더 설득력 있다.

## 3. If the disease needs exposure, add the exposure before changing the whole model

이 corpus는 많은 disease phenotype가 사실 derivation 문제가 아니라 assay problem임을 보여준다.

- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md): immune interaction
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md): apical access
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): host-microbe interaction

이 경우 baseline organoid를 갈아엎기보다, **missing exposure or interaction partner를 먼저 붙이는 편**이 더 논리적이다.

## 4. If the disease is a niche problem, simple organoids can mislead you

[Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)는 bone marrow disease modeling과 drug discovery를 vascular, stromal, hematopoietic niche와 함께 묶는다. [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)도 disease, infection, development가 단일 epithelial ball로는 충분하지 않다는 방향을 보여준다.

따라서 phenotype가 niche loss, support compartment, multicellular crosstalk에서 나온다면, 단순 donor-derived epithelial system은 충분하지 않을 수 있다.

## 5. If the disease claim is about repair or integration, host context becomes part of the model

- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): repair in colitis
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md): host circuit engagement

이 branch는 가장 강한 validation을 주지만, 동시에 host가 phenotype의 일부가 된다. 그래서 보통 first-pass disease model이 아니라 **late-stage confirmation or escalation path**로 더 적합하다.

## Practical triage rule

1. phenotype가 donor 안에 있는지, 발달 과정에 있는지, exposure에 있는지, niche에 있는지, host에 있는지 먼저 적는다.
2. donor phenotype면 patient-derived branch를 먼저 본다.
3. developmental phenotype면 hPSC developmental branch를 먼저 본다.
4. exposure phenotype면 assay layer를 먼저 붙인다.
5. niche phenotype면 multicompartment model을 고려한다.
6. host-repair phenotype면 transplantation을 validation layer로 둔다.

## What this corpus suggests avoiding

- disease model이라는 이유만으로 patient-derived를 무조건 우선하는 것
- developmental disease question을 mature adult platform으로만 푸는 것
- exposure-driven disease를 assay 없이 baseline organoid만으로 읽는 것
- niche disease를 single epithelial system에서 과도하게 해석하는 것
- host-context question을 pure in vitro endpoint만으로 마무리하는 것

## What this knowledge base does not settle

- 같은 disease에 대해 patient-derived와 developmental model을 정면 비교한 evidence는 제한적이다.
- immune, stromal, vascular, neural support가 각각 얼마나 중요한지 organ system마다 다르다.
- disease-model triage를 숫자로 환산한 scoring system은 이 corpus에 없다.

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Pomeshchik 2020](../sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.md)
- [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
