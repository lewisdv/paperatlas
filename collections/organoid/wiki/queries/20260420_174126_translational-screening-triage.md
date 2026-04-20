---
title: "Triage organoid systems for translational screening"
status: active
created: 2026-04-20T17:41:26+09:00
---

# 어떤 organoid가 translational screening에 가장 먼저 올라가야 하나

## Question

Organoid 논문을 보다 보면 거의 다 screening이나 drug discovery에 쓸 수 있어 보이지만, 실제로는 어떤 시스템은 곧바로 translational screening에 가깝고 어떤 시스템은 아직 discovery-stage에 머무는 것 같다. 이 corpus 기준으로 translational screening에 우선 올려야 할 organoid를 어떻게 triage해야 하나?

## Short answer

이 corpus에서는 translational screening 적합성을 이렇게 나누는 것이 가장 실용적이다.

- **Tier 1: near-term translational screens**
  - donor- or disease-preserving expandable systems
  - miniaturized or simplified high-reproducibility systems
- **Tier 2: assay-dependent screens**
  - baseline은 충분하지만, assay layer나 device layer가 성패를 좌우하는 systems
- **Tier 3: discovery-first complex models**
  - biology는 풍부하지만, 표준화와 throughput이 screening보다 discovery에 더 맞는 systems

즉 translational screening의 첫 후보는 보통 **가장 biologically ambitious한 모델**이 아니라 **가장 repeatable하면서 clinically interpretable한 모델**이다.

## A practical triage table

| tier | 특징 | corpus examples | 이유 |
|---|---|---|---|
| Tier 1: near-term | expandable, reproducible, interpretable, screen-compatible | [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md), [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md), [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md) | 바로 operational screen으로 옮기기 쉽다 |
| Tier 2: assay-dependent | baseline 위에 assay, perturbation, coculture, device layer 필요 | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md) | screening leverage는 크지만 protocol stack이 더 길다 |
| Tier 3: discovery-first | multicompartment richness가 크고 interpretability/throughput cost도 큼 | [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md), [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) | first-pass screen보다 discovery and follow-up validation에 더 어울린다 |

## 1. Tier 1: what is closest to translational screening now

### Patient-derived / adult expandable systems

- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)

이 branch는 donor specificity, long-term expansion, downstream manipulation이 좋아서 translational workflow와 가장 직접적으로 닿아 있다.

### Simplified controlled hPSC systems

- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)

이들은 scale control과 reproducibility를 screening-ready 쪽으로 밀어준다. 특히 Chen은 miniaturized controlled unit이라는 점에서, Hogrebe는 planar robust differentiation이라는 점에서 operational 이득이 크다.

## 2. Balboa shows why even Tier 1 systems need a maturity checkpoint

[Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)는 screening에 바로 들어가기 전 functional fidelity checkpoint가 필요하다는 점을 보여준다.

- biphasic GSIS
- insulin content
- granule morphology
- cytoarchitecture

즉 simplified baseline이 Tier 1이라도, **readout이 믿을 만한 maturity threshold를 넘었는지**는 별도로 확인해야 한다.

## 3. Tier 2 systems are powerful, but only after the stack is stable

- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md): immune coculture
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): host-microbe assay
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md): device-based perfused maturation
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md): pooled CRISPR screening

이들은 screening value가 높다. 하지만 baseline variance, geometry, delivery, device 운영, normalization 같은 추가 실패 지점이 생긴다. 그래서 이 corpus에서는 **Tier 1 baseline을 이미 확보한 뒤 올리는 레이어**에 가깝다.

## 4. Tier 3 models are often the wrong first screen, even if biologically richer

- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)

이 모델들은 biological richness가 크고 discovery 가치도 높다. 하지만 translational screening 첫 단계에서 요구되는 다음 조건에는 불리할 수 있다.

- batch standardization
- clear hit definition
- operational simplicity
- cost-efficient scale-up

그래서 이 corpus에서는 보통 **primary translational screen**보다 **mechanistic follow-up or richer validation layer**로 읽는 편이 더 맞다.

## 5. A simple triage rubric for this corpus

다음 다섯 질문에 "예"가 많을수록 screening 우선순위가 올라간다.

1. donor or disease state가 직접 보존되는가
2. batch-to-batch reproducibility를 설계상 확보하려는가
3. hit definition이 분명한가
4. scale-up이 상대적으로 단순한가
5. 해석을 흐리는 extra compartment가 적은가

이 기준으로 보면:

- **Tier 1**: Driehuis, Chen, Hogrebe, 일부 adult expandable platforms
- **Tier 2**: Cattaneo, Puschhof, Homan, Meng
- **Tier 3**: Drakhlis, Dardano, Olijnik, Wörsdorfer

## Practical rule

1. 먼저 Tier 1에서 screen을 설계한다.
2. Tier 2는 hit definition이 assay layer에 달려 있을 때만 올린다.
3. Tier 3는 first-pass screen보다 mechanistic refinement나 biological escalation에 쓴다.
4. complex model은 screen의 시작점이 아니라, 좋은 hit를 더 믿게 만드는 후속 단계로 두는 편이 낫다.

## What this corpus suggests avoiding

- translational relevance를 이유로 가장 복잡한 organoid를 바로 screen에 쓰는 것
- maturity checkpoint 없이 simplified system을 곧바로 clinical proxy로 쓰는 것
- assay-heavy system을 baseline robustness 검증 전에 screen으로 돌리는 것
- hit definition보다 visual richness를 우선하는 것

## What this knowledge base does not settle

- 각 tier의 throughput, cost, hit rate를 숫자로 비교한 자료는 없다.
- organ system별로 Tier 이동 기준이 다를 수 있다.
- patient-derived와 simplified hPSC system을 같은 therapeutic question에서 직접 비교한 head-to-head screen evidence는 제한적이다.

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
