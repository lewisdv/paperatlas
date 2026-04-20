---
title: "Choosing functional validation for non-brain organoids"
status: active
created: 2026-04-20T17:35:05+09:00
---

# non-brain organoid는 어떤 functional validation을 붙여야 믿을 수 있나

## Question

Brain organoid는 atlas나 electrophysiology 같은 benchmark 축이 비교적 잘 보이는데, non-brain organoid는 종종 "marker는 맞는데 그래서 기능이 믿을 만한가?"가 더 애매하다. 이 corpus 기준으로 non-brain organoid는 어떤 functional validation을 우선 붙여야 가장 설득력이 커지나?

## Short answer

이 corpus에서 non-brain organoid validation의 핵심 원칙은 단순하다. **generic morphology를 반복하지 말고, 그 organ의 핵심 claim을 직접 시험하는 functional validation을 붙여야 한다.**

- **pancreas**면 secretion benchmark
- **kidney**면 perfusion, vascularization, polarity benchmark
- **intestine**면 access, microbe exposure, repair benchmark
- **vascular organoid**면 circulation integration benchmark
- **niche-rich organoid**면 missing compartment가 아니라 실제 multicompartment function이 유지되는지 봐야 한다

즉 non-brain organoid는 marker panel보다 **claim-matched validation**이 더 중요하다.

## Claim-first validation table

| claim | 먼저 붙일 validation | 왜 이게 맞는가 | 대표 근거 |
|---|---|---|---|
| endocrine function | GSIS, insulin content, granules, cytoarchitecture | pancreatic identity보다 secretion competence가 핵심 | [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md), [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md) |
| renal maturation | flow-enhanced vascularization, polarity, adult-like expression | kidney는 static nephron marker만으로 미성숙을 가리기 어렵다 | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md), [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md) |
| barrier or host-microbe biology | polarity control, lumen exposure, microbial coculture | geometry가 안 맞으면 biology 자체를 못 묻는다 | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| regenerative or repair relevance | transplantation in injury context | dish phenotype가 repair claim으로 이어지는지 직접 본다 | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |
| vascular maturity | host circulation integration, arterial/venous specification | vessel-like morphology만으로는 충분하지 않다 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) |
| multicompartment niche function | co-development or niche completeness readout | niche question은 single-lineage validation으로 대체되지 않는다 | [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md), [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md), [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md) |

## 1. Pancreas: function means secretion, not just beta-cell markers

- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)는 scalable SC-beta production baseline을 준다.
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)는 secretion-linked maturation benchmark를 가장 자세히 제공한다.

이 corpus에서는 pancreas claim을 믿으려면 최소한 다음 축이 중요하다.

- biphasic GSIS
- insulin content 증가
- dense-core granule morphology
- cytoarchitecture reorganization
- proliferation 감소

즉 "beta-cell marker가 있다"는 functional validation이 아니라 baseline에 가깝다.

## 2. Kidney: function means more than nephron identity

- [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md): nephron-rich baseline
- [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md): proximal-tubule refinement
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md): perfusable vascular network, 5x PECAM1+ area increase, enhanced polarity, more adult-like expression

따라서 kidney organoid에서 strong validation은 단순 segment marker보다 **flow와 vascular context를 통해 maturation bottleneck이 실제로 완화되는지**를 보는 것이다.

## 3. Intestine: first make the biology accessible

장 organoid에서는 validation이 종종 추가 complexity가 아니라 **실험 접근성 확보**에서 시작된다.

- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md): apical surface access
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): lumenal microinjection and microbial viability workflows
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): repair and host-context validation

이 흐름은 intestine에서 validation이 단계적이라는 것을 보여준다.

1. biology에 접근 가능한가
2. pathogen or microbe question을 실제로 운영할 수 있는가
3. repair claim이면 host context에서도 유지되는가

## 4. Vascular organoids need circulation-linked validation

[Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)는 endothelial plus pericyte structure만으로 끝나지 않고, transplantation 뒤 host circulation integration과 arterial/venous specification까지 본다.

이 corpus에서 vascular organoid validation은 **"tube-like morphology"를 넘어서 실제 vascular behavior로 가야 한다**는 기준을 가장 잘 보여준다.

## 5. Complex niche organoids should be validated as niches, not simplified back down

- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md): early heart, foregut, vasculature co-development
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md): blood-generating extension plus imaging
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md): vascular, stromal, hematopoietic niche

이런 시스템에서는 validation을 단일 lineage marker panel로 되돌리면 질문을 스스로 축소하게 된다. 더 적절한 기준은 다음과 같다.

- 필요한 neighbor compartment가 실제로 존재하는가
- multicompartment organization이 screening or disease question을 지탱하는가
- richer model이 simple model과 다른 결론을 내게 만드는가

## Practical rule for non-brain systems

1. 먼저 organoid가 주장하는 핵심 기능을 한 문장으로 쓴다.
2. 그 기능을 가장 직접적으로 시험하는 assay를 고른다.
3. morphology나 marker는 entry check로만 쓰고, 최종 validation으로 과신하지 않는다.
4. host-context가 claim의 일부면 transplantation이나 integration assay를 별도 단계로 둔다.
5. multicompartment organoid는 compartment completeness를 validation 축에 포함한다.

## What this corpus suggests avoiding

- 모든 non-brain organoid에 같은 marker 패널을 반복하는 것
- secretion claim을 lineage marker만으로 마무리하는 것
- kidney maturation claim을 static identity만으로 확정하는 것
- infection or barrier question인데 apical access를 무시하는 것
- niche organoid를 다시 single-lineage 기준으로만 평가하는 것

## What this knowledge base does not settle

- non-brain organoid 전반에 통용되는 공통 functional validation hierarchy는 없다.
- organ system 간 cost, throughput, interpretability tradeoff를 정량 비교한 head-to-head 자료도 부족하다.
- lung, skin, gastric 등 일부 organ system은 이 corpus에서 functional validation depth가 pancreas나 kidney만큼 풍부하지 않다.

## Sources used

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Takasato 2016](../sources/takasato_2016_generation_of_kidney_organoids_from.md)
- [Vanslambrouck 2023](../sources/vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Drakhlis 2021](../sources/drakhlis_2021_generation_of_heart-forming_organoids_from.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
