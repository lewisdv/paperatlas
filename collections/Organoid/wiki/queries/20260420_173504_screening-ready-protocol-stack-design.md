---
title: "Designing a screening-ready organoid protocol stack"
status: active
created: 2026-04-20T17:35:04+09:00
---

# screening-ready organoid stack는 어떻게 설계해야 하나

## Question

Organoid를 언젠가 screening에 쓰고 싶다는 목표는 흔하지만, 실제로는 baseline derivation, maturation, assay layer, perturbation, readout이 뒤섞이기 쉽다. 이 corpus 기준으로 screening-ready organoid protocol stack는 어떤 순서와 기준으로 설계하는 게 가장 현실적인가?

## Short answer

이 corpus에서는 screening-ready system이 단일 프로토콜이 아니라 **stack**로 보인다. 가장 좋은 실전 규칙은 이렇다. **가장 단순하고 반복 가능한 baseline을 먼저 고르고, 질문을 바꾸는 레이어만 순서대로 추가하라.**

- **Layer 1:** baseline model choice
- **Layer 2:** reproducibility and scale control
- **Layer 3:** readout-specific assay or engineering
- **Layer 4:** perturbation or drug-screen operation
- **Layer 5:** higher-cost validation such as transplantation or richer niche context

즉, screening은 derivation 뒤에 바로 오는 것이 아니라, **robust baseline 위에 구축되는 operational stack**이다.

## The five-layer stack

| layer | 먼저 물어볼 것 | 대표 선택지 | 대표 근거 |
|---|---|---|---|
| 1. baseline model | donor specificity가 중요한가, developmental reconstruction이 중요한가 | patient-derived vs hPSC-derived | [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md), [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md), [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md) |
| 2. scale control | batch consistency와 miniaturization이 충분한가 | planar, miniaturized, controlled organoid | [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md), [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md) |
| 3. assay layer | 어떤 readout이 실제 hit를 정의하는가 | electrophysiology, microbial exposure, polarity control, imaging | [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md) |
| 4. perturbation layer | pooled perturbation이나 drug-response를 실제로 운영할 수 있는가 | CRISPR screening, drug screening | [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md), [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) |
| 5. secondary validation | dish hit가 host context에서도 유지돼야 하는가 | transplantation, repair, circulation integration | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) |

## 1. Start from the simplest baseline that preserves the biology

이 corpus에서 screening-ready baseline은 대체로 **complexity를 줄이고 반복성을 높이는 방향**에서 나온다.

- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md): miniaturized, necrosis-limited midbrain organoids
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md): planar SC-beta differentiation with cross-line robustness
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md): patient-derived expansion for translational drug testing

따라서 첫 단계는 "가장 biologically rich한 모델"이 아니라, **질문을 망치지 않으면서 가장 operationally stable한 baseline**을 고르는 것이다.

## 2. Miniaturization and reproducibility come before fancy readouts

[Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)가 요약하듯이, engineering layer는 baseline이 안정적일 때만 의미가 커진다.

- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)는 screening 적합성을 size control과 necrosis reduction에서 시작한다.
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)는 3D suspension dependency를 줄여 reproducibility를 높인다.

이 corpus의 메시지는 명확하다. **screening failure는 biology보다 baseline variance 때문에 먼저 오는 경우가 많다.**

## 3. Add only the assay layer that defines a believable hit

Screening-ready라고 해서 항상 pooled CRISPR나 giant imaging stack가 필요한 것은 아니다. readout을 정의하는 assay layer가 다를 뿐이다.

- neural function이 hit 정의면 [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) 같은 electrophysiology-compatible branch
- host-microbe or barrier question이면 [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- morphology-rich multicompartment question이면 [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md) 같은 advanced imaging extension

즉 readout layer는 optional decoration이 아니라, **무엇을 hit라고 부를지 정하는 operational definition**이다.

## 4. Only then add systematic perturbation

- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)는 neural organoid/assembloid를 pooled CRISPR system으로 바꾼다.
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)는 downstream therapeutic testing으로 이어지는 translational branch를 보여준다.

여기서 중요한 점은 pooled perturbation이 baseline instability를 고쳐주지 않는다는 것이다. 오히려 instability가 있으면 screen design, delivery, normalization 문제가 먼저 커진다.

## 5. Treat transplantation or host-context assays as secondary screens

- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): repair-context validation
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md): host circulation integration and arterial/venous specification

이런 validation은 중요하지만, 이 corpus에서 보는 한 **primary screen layer**라기보다 **secondary confirmation layer**에 가깝다. host variability와 logistics cost가 높기 때문이다.

## When higher complexity is justified in screening

복잡한 모델이 screening에 항상 불리한 것은 아니다. 다만 complexity는 **질문이 그 compartment를 필요로 할 때만** 정당화된다.

- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md): vascular, stromal, hematopoietic niche 없이는 bone marrow screening question이 무너질 수 있다
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md): blood-generating heart context가 질문의 일부일 수 있다

이 경우에도 complexity를 baseline으로 바로 쓰기보다, **간단한 primary screen -> richer follow-up model**의 2단 구조가 더 현실적이다.

## Practical build order

1. baseline platform을 고른다: developmental vs patient-derived
2. size, yield, batch variance를 먼저 잡는다
3. hit definition을 정하는 assay/readout layer를 하나 붙인다
4. 그다음 perturbation or drug screen을 얹는다
5. 꼭 필요할 때만 host-context or multicompartment validation으로 올린다

## Example stacks supported by this corpus

- **translational drug response**
  - baseline: [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
  - assay: disease- or donor-relevant response readout
  - follow-up: immune coculture or host validation if needed
- **controlled neural screening**
  - baseline: [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
  - assay: [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) style functional readout when required
  - perturbation: [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- **functional endocrine screening**
  - baseline: [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
  - maturity benchmark: [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
  - screen only after secretion-linked maturity is believable

## What this corpus suggests avoiding

- unstable baseline 위에 바로 CRISPR screen을 얹는 것
- primary screen 단계에서 transplantation을 기본 readout으로 잡는 것
- complexity를 realism 이유만으로 기본 선택하는 것
- hit definition 없이 imaging, editing, coculture를 한꺼번에 붙이는 것

## What this knowledge base does not settle

- throughput, cost, adoption barrier를 공통 숫자로 비교한 benchmark는 없다.
- 같은 biological question에 대해 simple versus complex screening stack를 정면 비교한 evidence도 제한적이다.
- non-brain pooled screening protocols는 brain만큼 풍부하지 않다.

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
- [Organ-on-chip](../entities/organ-on-chip.md)

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
