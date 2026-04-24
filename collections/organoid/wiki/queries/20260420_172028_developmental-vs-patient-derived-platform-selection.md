---
title: "Organoid platform selection: developmental hPSC vs adult/patient-derived"
status: active
created: 2026-04-20T17:20:28+09:00
---

# 언제 developmental hPSC organoid 대신 adult/patient-derived platform을 선택해야 하나

## Question

Organoid 프로젝트를 설계할 때, 언제 hPSC 기반 developmental organoid를 쓰고 언제 adult stem cell 또는 patient-derived organoid platform을 써야 하나?

## Short answer

이 corpus 기준으로는 질문의 중심이 어디에 있느냐로 갈린다.

- **발생 과정, regional patterning, lineage emergence**가 핵심이면 developmental hPSC organoid가 더 맞다.
- **donor-specific biology, tumor context, translational screening, 장기 확장 가능한 epithelial platform**이 핵심이면 adult/patient-derived organoid가 더 맞다.
- **복합 niche나 boundary biology**가 핵심이면 둘 중 하나만으로는 부족할 수 있고, multi-lineage organoid 쪽으로 가야 한다.

## Decision table

| 연구 질문 | 더 적합한 출발점 | 이 corpus의 근거 | 대표 페이지 |
|---|---|---|---|
| 특정 장기나 뇌 subregion이 어떻게 형성되는가 | developmental hPSC organoid | patterning factor와 시점 제어가 프로토콜 핵심 축으로 정리돼 있음 | [Lancaster 2014](../sources/lancaster_2014_generation_of_cerebral_organoids_from.md), [Sloan 2018](../sources/sloan_2018_generation_and_assembly_of_human.md), [McCracken 2011](../sources/mccracken_2011_generating_human_intestinal_tissue_from.md), [Morizane 2016](../sources/morizane_2016_generation_of_nephron_progenitor_cells.md) |
| donor나 patient의 질환 상태를 최대한 빨리 assay로 옮기고 싶은가 | adult/patient-derived organoid | primary 또는 patient material에서 바로 expandable platform을 만들고 screening으로 이어감 | [Drost 2016](../sources/drost_2016_organoid_culture_systems_for_prostate.md), [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) |
| 장기간 배양 가능한 epithelial platform 위에 perturbation을 얹고 싶은가 | adult/patient-derived organoid | adult or fetal tissue organoid 위에 genetic manipulation이 바로 연결됨 | [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md), [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md), [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md) |
| developmental program 자체보다 niche composition이 더 중요한가 | multi-lineage organoid | 단일 epithelial platform보다 stromal, vascular, hematopoietic 관계가 중요해짐 | [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md), [Koike 2021](../sources/koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md) |

## What developmental hPSC organoids are best for

- **발생 논리 자체를 묻는 질문**: 어떤 morphogen과 timing이 region identity를 바꾸는지, 어떤 lineage가 언제 등장하는지 같은 질문.
- **patterning tradeoff를 비교하는 질문**: self-organization vs directed control, diversity vs reproducibility 같은 축.
- **organ emergence를 재구성하는 질문**: broad developmental diversity 또는 subregion-specific control이 실험 설계의 일부일 때.

이 corpus에서는 brain, gut, kidney, heart 쪽 프로토콜이 이 범주를 가장 잘 보여준다. 특히 [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)와 [Brain subregion-specific organoid protocols](../concepts/brain-subregion-specific-organoid-protocols.md)는 developmental hPSC route가 왜 필요한지를 요약한다.

## What adult or patient-derived platforms are best for

- **donor biology를 가능한 한 덜 희석하고 싶은 질문**
- **patient or tumor sample에서 바로 screening 또는 perturbation으로 넘어가려는 질문**
- **long-term expandable epithelial platform 자체가 중요한 질문**

이 corpus에서 adult/patient-derived branch의 핵심 장점은 developmental recapitulation보다 **질환 또는 donor 맥락의 보존과 실용성**에 있다. [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)도 같은 방향을 보여준다.

## The main tradeoff

### developmental hPSC organoids

- 장점: patterning logic, lineage emergence, organogenesis-style questions에 강함
- 약점: donor-specific disease context를 바로 보존하는 플랫폼은 아님

### adult/patient-derived organoids

- 장점: donor or disease specificity, translational screening, long-term expansion에 강함
- 약점: multicompartment developmental context는 약해지기 쉽고 epithelial bias가 남는다

## A practical selection rule

1. **질문이 “이 조직이 어떻게 만들어지는가”에 가까우면** developmental hPSC 쪽으로 간다.
2. **질문이 “이 환자/종양/기증자 상태가 어떻게 반응하는가”에 가까우면** adult/patient-derived 쪽으로 간다.
3. **질문이 “여러 compartment가 함께 있어야만 의미가 있는가”라면** multi-lineage organoid를 우선 검토한다.
4. **질문이 perturbation or screening readiness까지 포함한다면** baseline platform을 고른 뒤 engineering layer가 자연스럽게 붙는 프로토콜을 고른다.

## What this knowledge base does not settle

- 같은 organ system 안에서 developmental hPSC route와 patient-derived route를 **정면 비교한 head-to-head evidence**는 이 corpus에 충분하지 않다.
- adult/patient-derived platform이 donor context를 얼마나 오래 유지하는지, 그리고 어떤 non-epithelial compartment 부재가 가장 치명적인지는 여전히 open question으로 남아 있다.

## Related syntheses

- [Organoid developmental baseline and regionalization playbook](../syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md)
- [Organoid project design playbook](../syntheses/20260422_organoid-project-design-playbook.md)

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Drost 2016](../sources/drost_2016_organoid_culture_systems_for_prostate.md)
- [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Koike 2021](../sources/koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Lancaster 2014](../sources/lancaster_2014_generation_of_cerebral_organoids_from.md)
- [Sloan 2018](../sources/sloan_2018_generation_and_assembly_of_human.md)
- [McCracken 2011](../sources/mccracken_2011_generating_human_intestinal_tissue_from.md)
- [Morizane 2016](../sources/morizane_2016_generation_of_nephron_progenitor_cells.md)
