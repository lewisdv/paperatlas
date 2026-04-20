---
title: "How to compensate for missing compartments in adult/patient-derived organoids"
status: active
created: 2026-04-20T17:28:26+09:00
---

# adult 또는 patient-derived organoid의 빠진 compartment는 어떻게 보완해야 하나

## Question

Adult stem cell 또는 patient-derived organoid는 donor specificity와 실용성은 좋지만, stromal, immune, vascular, luminal, host context 같은 요소가 빠지기 쉽다. 이 빠진 compartment를 어떻게 보완하는 게 가장 합리적인가?

## Short answer

이 corpus에서는 adult/patient-derived epithelial platform을 버릴 필요가 항상 있는 것은 아니다. 오히려 **어떤 compartment가 빠져서 어떤 결론이 흔들리는지**를 먼저 정한 뒤, 그 결손에 맞는 보완 레이어를 붙이는 게 더 합리적이다.

- **apical/luminal access 문제**면 polarity control 또는 microbial exposure
- **immune interaction 결손**이면 immune coculture
- **vascular or stromal support 결손**이면 vascularization or niche-rich model
- **host repair or translational validation 결손**이면 transplantation
- **결손이 너무 많아 baseline platform 자체가 질문을 왜곡하면** multi-lineage organoid로 옮긴다

## Baseline problem in this corpus

[Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)에 요약된 것처럼, adult/patient-derived branch는 donor or disease specificity에는 강하지만 **whole-organ multicompartment context**를 충분히 재현하지 못할 수 있다.

이 문제는 특히 다음 source들에서 공통적으로 드러난다.

- [Drost 2016](../sources/drost_2016_organoid_culture_systems_for_prostate.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)

이 플랫폼들은 보통 **expandable epithelial or donor-derived system**으로 강점이 있지만, missing compartment를 어떻게 다룰지 별도 선택이 필요하다.

## Missing-compartment decision table

| 빠진 요소 | 우선 보완 방식 | 이유 | 대표 페이지 |
|---|---|---|---|
| apical/lumen access | polarity control or microbial coculture | geometry 때문에 막혀 있던 biology를 열어준다 | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| immune interaction | immune coculture | donor-derived epithelial baseline 위에 immune layer를 얹는다 | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md) |
| host repair or translational relevance | transplantation | dish 결과를 host context에서 재검증 | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) |
| vascular support | vascular module or vascularized niche model | epithelial-only bias를 줄이고 tissue support를 보완 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md), [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| stromal + hematopoietic + vascular niche 자체 | multi-lineage niche model로 이동 | 단순 보정이 아니라 모델 전환이 필요할 수 있다 | [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md) |

## 1. Fix access problems before rebuilding the whole model

어떤 경우에는 compartment가 비어 있는 것이 아니라, **접근 방식이 틀린 것**일 수 있다.

- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md): apical side를 실험 가능한 방향으로 노출
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): microbial coculture를 실제로 운영 가능한 workflow로 만든다

즉, epithelial organoid가 단순해서가 아니라 geometry 때문에 질문을 못 푸는 경우라면, baseline을 버리기보다 access layer를 먼저 붙이는 편이 낫다.

## 2. Add the biologically missing partner when interaction is the question

- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md): immune engagement가 핵심일 때 T-cell coculture를 추가

이 경우의 핵심은 “organoid를 다시 설계하는 것”이 아니라, **빠져 있던 interaction partner를 실험적으로 호출하는 것**이다.

## 3. Use transplantation when the missing compartment is really host context

- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): repair context
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md): host circuit engagement

Host context가 빠져서 결론이 불안정하다면, 결국 가장 직접적인 보완은 transplantation이다. 다만 이 경우부터는 organoid-intrinsic interpretation이 더 어려워진다.

## 4. Move to vascular or niche-rich models when support compartments matter continuously

- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md): vessel module 자체를 준다
- [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md): vascular and microglia-like component를 넣는 modular strategy
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md): niche 자체가 질문일 때는 아예 richer model이 필요하다

즉, missing compartment가 일회성 assay layer가 아니라 **항상성이나 niche logic 자체**를 좌우한다면, 보조 실험보다 모델 전환이 낫다.

## Practical rule

1. 먼저 빠진 것이 **access인지, interaction partner인지, host context인지, 지속적 support compartment인지**를 구분한다.
2. access 문제면 geometry를 고친다.
3. interaction 문제면 coculture를 붙인다.
4. host relevance 문제면 transplantation을 붙인다.
5. 그래도 질문이 무너지면 multi-lineage 또는 niche-rich model로 옮긴다.

## What this corpus suggests avoiding

- epithelial bias가 큰 baseline 위에 너무 많은 해석을 얹는 것
- luminal access 문제를 complexity 부족으로 오해하는 것
- host-context question을 coculture만으로 해결하려는 것
- niche question인데 single epithelial donor-derived system에 집착하는 것

## What this knowledge base does not settle

- adult/patient-derived organoid에 어떤 missing compartment가 가장 치명적인지는 organ system마다 다르다.
- stromal, immune, vascular, neural support를 하나의 공통 프레임으로 비교한 head-to-head evidence는 이 corpus에 충분하지 않다.

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Drost 2016](../sources/drost_2016_organoid_culture_systems_for_prostate.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
