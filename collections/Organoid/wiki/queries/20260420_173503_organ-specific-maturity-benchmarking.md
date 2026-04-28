---
title: "Organ-specific maturity benchmarking for organoids"
status: active
created: 2026-04-20T17:35:03+09:00
---

# organ마다 maturity benchmark를 어떻게 다르게 잡아야 하나

## Question

Organoid의 "성숙도"를 평가할 때 모든 organ system에 공통인 maturity score를 쓰고 싶어지지만, 실제로는 organ마다 믿을 만한 benchmark가 다를 것 같다. 이 corpus에서는 organ-specific maturity benchmark를 어떻게 잡는 것이 가장 합리적인가?

## Short answer

이 corpus가 주는 가장 중요한 규칙은 하나다. **universal maturity score를 찾기보다, 그 organ에서 결론을 바꾸는 기능적 기준을 먼저 정해야 한다.**

- **brain**은 atlas fidelity, temporal mapping, reproducibility, electrophysiology가 핵심이다.
- **pancreas**는 GSIS, insulin content, granule morphology, cytoarchitecture처럼 분비기능에 직접 연결되는 readout이 핵심이다.
- **kidney**는 segment identity만으로는 부족하고 vascularization, polarity, perfusion-linked maturation이 중요하다.
- **intestine**는 단순 marker보다 apical access, microbe exposure, repair context처럼 assay suitability가 maturity 판단에 더 가깝다.
- **multi-lineage organs**에서는 개별 세포 성숙도만이 아니라 co-development나 niche completeness 자체가 benchmark가 된다.

## Why a single maturity scale breaks down

이 knowledge base에서 "성숙"은 같은 뜻으로 쓰이지 않는다.

- [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md)과 [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)는 brain에서 maturity를 **발달 시점과 primary atlas 상의 위치**로 본다.
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)는 pancreas에서 maturity를 **biphasic GSIS, granule ultrastructure, cytoarchitecture, proliferation exit**로 본다.
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)는 kidney에서 maturity를 **flow-linked vascularization, polarity, adult-like expression**의 증가로 다룬다.
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)와 [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)는 intestine에서 maturity를 단독 점수보다 **실제로 질문 가능한 geometry와 exposure state**로 바꾼다.

즉, maturity는 organ마다 다른 failure mode를 갖는다.

## Organ-by-organ benchmark table

| organ system | 먼저 봐야 할 maturity benchmark | 왜 중요한가 | 대표 근거 |
|---|---|---|---|
| brain | atlas fidelity + temporal map + reproducibility + functional oscillation | brain은 "무엇이 있는가"와 "언제 나오는가"가 모두 중요하다 | [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md), [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md), [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md), [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) |
| pancreas | GSIS biphasicity, insulin content, dense-core granules, cytoarchitecture | marker-positive보다 실제 endocrine function이 더 중요하다 | [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md), [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md) |
| kidney | segment bias + vascularization + polarity + adult-like expression | nephron marker만으로는 immature static culture를 놓치기 쉽다 | [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md), [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) |
| intestine | apical accessibility, microbial assay readiness, repair competence | 장 organoid는 access와 host-context가 없으면 질문이 막힌다 | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |
| heart / niche-rich systems | morphogenesis + co-development of relevant neighboring compartments | 단일 lineage 성숙도보다 multicompartment assembly가 결론을 바꾼다 | [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md), [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md) |

## 1. Brain maturity is not one number

이 corpus에서 brain organoid 성숙도는 최소 네 조각으로 쪼개진다.

- [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md): 어떤 cell state가 어느 시점에 나오는지
- [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md): 어떤 primary brain population과 얼마나 닮았는지
- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md): reproducibility와 fidelity가 같지 않다는 점
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md): electrophysiology와 oscillation readiness

따라서 brain에서는 "오래 키웠다"만으로 mature라고 보기 어렵고, **temporal, transcriptomic, functional benchmark를 분리해서 봐야 한다.**

## 2. Pancreas maturity should be anchored to secretion, not just identity

- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)는 robust한 SC-beta production baseline을 준다.
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)는 그다음 질문인 "얼마나 adult islet-like한가"를 functional benchmark로 푼다.

여기서 중요한 점은 INS+, PDX1+, NKX6-1+ 같은 lineage identity만으로는 부족하다는 것이다. 이 corpus에서는 pancreas maturity가 다음과 더 가깝다.

- biphasic GSIS가 생겼는가
- insulin content가 증가했는가
- dense-core granule morphology가 primary에 가까운가
- cytoarchitecture가 재배열되는가
- proliferation이 줄어드는가

## 3. Kidney maturity is partly a vascularization problem

- [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md)는 nephron-rich baseline을 준다.
- [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md)는 segment-biased refinement를 준다.
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)는 static kidney organoid가 놓치는 maturation bottleneck을 flow, PECAM1+ vessel expansion, polarity, adult-like expression으로 다룬다.

즉 kidney에서는 **segment marker가 맞는 것**과 **functionally more mature한 것**이 다를 수 있다. 이 corpus에서는 후자를 보기 위해 perfusion and vascular support가 핵심 benchmark 축으로 올라온다.

## 4. Intestinal maturity is often about usable geometry and context

Intestinal organoid에서는 성숙도를 단순 발현 패널로만 보기보다, 질문을 실제로 수행할 수 있는지로 평가하는 흐름이 강하다.

- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md): apical side를 실제로 열 수 있는가
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): microbe exposure와 viability assay를 운영할 수 있는가
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): repair context에서 host relevance를 확보할 수 있는가

따라서 intestine에서는 "mature marker"보다 **barrier/infection/repair question을 풀 수 있는 상태인가**가 더 실전적인 benchmark다.

## 5. Complex organs may need niche completeness as the maturity criterion

- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md)는 early heart, foregut, vasculature co-development를 baseline으로 둔다.
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)는 blood-generating extension과 imaging layer를 더한다.
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)는 vascular, stromal, hematopoietic niche 자체를 모델링 목표로 둔다.

이런 경우에는 개별 compartment 하나의 mature marker보다, **질문에 필요한 neighbor compartment가 실제로 함께 존재하는가**가 benchmark가 된다.

## Practical rule for this corpus

1. 먼저 organ마다 "무엇이 immature해서 결론이 흔들리는가"를 적는다.
2. 그다음 그 organ에서 가장 직접적인 functional or atlas benchmark를 고른다.
3. marker identity는 baseline으로만 보고, 가능하면 function or context benchmark를 추가한다.
4. one-size-fits-all maturity score를 만들기보다 organ-specific checklist를 만든다.

## What this corpus suggests avoiding

- 모든 organoid에 공통 maturity score를 강제로 적용하는 것
- marker positivity만으로 function을 대신 추정하는 것
- kidney나 intestine에서 vascularization, polarity, host-context 문제를 maturity 바깥으로 밀어내는 것
- multicompartment organoid를 단일 lineage 기준만으로 평가하는 것

## What this knowledge base does not settle

- cross-organ universal maturity metric은 이 corpus에 없다.
- pancreas, kidney, intestine, heart를 같은 척도로 정량 비교한 head-to-head benchmarking도 없다.
- non-brain organoid에서 atlas-scale maturity resource는 brain만큼 풍부하지 않다.

## Sources used

- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Cardiac and hematoendothelial organoids](../concepts/cardiac-and-hematoendothelial-organoids.md)
- [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md)
- [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md)
- [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
