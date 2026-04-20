---
title: "How much organoid complexity is enough?"
status: active
created: 2026-04-20T17:28:24+09:00
---

# 얼마나 복잡한 organoid가 정말 필요한가

## Question

Organoid 실험을 설계할 때, biological richness를 위해 더 복잡한 multi-lineage organoid로 가야 하는지, 아니면 더 단순하고 throughput-friendly한 모델에 머물러야 하는지 어떻게 판단해야 하나?

## Short answer

이 corpus가 주는 가장 실용적인 규칙은 단순하다. **답을 바꾸는 compartment가 명확할 때만 complexity를 올리고, 그렇지 않으면 가장 단순한 안정적 모델에 머무는 편이 낫다.**

- **screening, reproducibility, clean perturbation**이 우선이면 더 단순하고 controlled한 모델이 유리하다.
- **boundary biology, appendage formation, vascular/stromal/hematopoietic niche, multi-organ coordination**가 질문의 핵심이면 complexity를 올릴 이유가 있다.
- complexity는 보통 realism을 올리지만, 동시에 **표준화, 해석 용이성, 비용, throughput**을 떨어뜨린다.

## A three-tier decision framework

| 모델 tier | 언제 선택 | 장점 | 대표 근거 |
|---|---|---|---|
| Controlled and throughput-oriented | perturbation, screening, batch consistency가 핵심일 때 | 해석이 비교적 깨끗하고 반복성이 높다 | [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md), [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) |
| Intermediate complexity with stronger readouts | 장기 identity는 유지하되 function이나 later-stage maturation이 필요할 때 | 너무 무겁지 않으면서도 readout value를 키운다 | [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md), [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md) |
| Multi-lineage or boundary-rich systems | 단일 lineage로는 질문 자체가 무너질 때 | richer tissue interactions와 niche logic를 포착한다 | [Lee 2022](../sources/lee_2022_generation_and_characterization_of_hair-bearing.md), [Koike 2021](../sources/koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md), [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md) |

## When lower-complexity models are the better choice

복잡도가 낮은 모델이 “덜 발전된” 모델인 것은 아니다. 이 corpus에서는 오히려 **질문을 가장 깔끔하게 푸는 모델**일 때가 많다.

- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)는 midbrain organoid를 miniaturized controlled unit으로 만들어 screening-scale 실험에 맞춘다.
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) 같은 patient-derived platform은 donor context와 screening practicality를 우선한다.

이런 모델은 다음 질문에 적합하다.

- perturbation 결과를 빠르게 비교해야 하는가
- 실험 수를 많이 돌려야 하는가
- organoid 내부의 extra compartment보다 baseline reproducibility가 더 중요한가

## When intermediate complexity is enough

이 corpus는 “복잡함 vs 단순함”의 이분법 대신, **중간 계층**도 꽤 중요하다고 보여준다.

- [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md)는 later-stage maturation 쪽으로 밀어준다.
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)는 semi-guided brain organoid를 oscillation, calcium imaging, MEA 같은 기능 readout과 연결한다.
- [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)는 developmental, disease, infection question을 하나의 lung workflow에 묶는다.

이 계층은 “compartment를 무한정 늘리기”보다, **현재 organoid identity를 유지하면서 readout value를 높이는 쪽**에 가깝다.

## When high complexity is actually necessary

Complexity가 정당화되는 경우는 대체로 단일 epithelial 또는 단일 lineage model이 질문을 잘못 단순화할 때다.

- [Lee 2022](../sources/lee_2022_generation_and_characterization_of_hair-bearing.md): appendage와 sensory feature가 없으면 skin question의 일부가 사라진다
- [Koike 2021](../sources/koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md): foregut-midgut boundary와 inter-organ relation이 핵심
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md): vascular, stromal, hematopoietic niche가 없으면 bone marrow question이 붕괴한다
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md): cardiac와 hematoendothelial co-development가 질문의 일부다

즉, **extra compartment가 “있으면 좋다”가 아니라 “없으면 답이 바뀐다”면** 고복잡도 모델이 필요하다.

## Practical rule of thumb

1. **질문이 marker, perturbation, screening 비교 중심이면** 가장 단순하고 repeatable한 모델부터 시작한다.
2. **질문이 later-stage maturation이나 function readout 중심이면** intermediate complexity를 먼저 본다.
3. **질문이 tissue boundary, appendage, niche, multicompartment interaction 중심이면** multi-lineage 모델로 올라간다.
4. complexity를 올릴 때는 반드시 “어떤 compartment가 어떤 결론을 바꿀 것인지”를 먼저 명시한다.

## What this corpus suggests avoiding

- realism을 이유로 무조건 complexity를 올리는 것
- screening question인데 boundary-rich organoid를 먼저 택하는 것
- niche question인데 single-lineage model로 답을 확정하는 것

## What this knowledge base does not settle

- complexity와 throughput를 수치화한 공통 score는 이 corpus에 없다.
- 같은 biological question에 대해 low-complexity와 high-complexity 모델을 정면 비교한 head-to-head evidence도 제한적이다.

## Sources used

- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Lee 2022](../sources/lee_2022_generation_and_characterization_of_hair-bearing.md)
- [Koike 2021](../sources/koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)
- [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
