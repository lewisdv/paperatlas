---
title: "Choosing whether to add immune, vascular, or niche compensation first"
status: active
created: 2026-04-20T19:04:09+09:00
---

# Immune, vascular, niche 보완 중 무엇을 먼저 붙여야 하나

## Question

Adult or patient-derived organoid, 혹은 screening-ready baseline organoid를 돌리다 보면 immune coculture, vascularization, niche-rich model transition이 모두 필요해 보일 때가 있다. 이 corpus 기준으로 셋 중 무엇을 먼저 붙이는 것이 가장 합리적인가?

## Short answer

이 corpus는 **가장 적은 복잡도로 질문에 직접 닿는 보완 레이어부터 붙이라**고 말한다.

- **직접적인 cell-cell interaction이 질문의 핵심이면 immune layer를 먼저** 붙인다.
- **조직 크기, hypoxia, perfusion, maturation plateau가 문제면 vascular layer를 먼저** 붙인다.
- **애초에 현상이 multicompartment niche 없이는 성립하지 않으면 niche-rich model로 먼저** 간다.

다만 그 전에 한 번 더 봐야 하는 것이 있다. [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)처럼 **geometry or access problem**이 먼저라면 immune, vascular, niche 중 무엇을 더하든 핵심 readout은 계속 막힐 수 있다.

## The practical priority rule

1. **access가 막혀 있으면 geometry부터 고친다**
2. **질문이 특정 partner와의 직접 상호작용이면 immune or coculture를 먼저 붙인다**
3. **질문이 survival, diffusion, or maturation barrier면 vascular support를 먼저 붙인다**
4. **질문이 steady-state multicompartment support 자체면 niche-rich model로 간다**

즉, 셋 중 무엇이 빠졌는지를 묻기보다 **무엇이 현재 해석을 가장 직접적으로 바꾸는 missing function인지**를 먼저 묻는 편이 맞다.

## Decision table

| dominant missing function | first upgrade in this corpus | why |
|---|---|---|
| apical access or exposure geometry | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)-style polarity/access fix | interaction assay 이전에 readout surface가 열려야 함 |
| immune effector engagement | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)-style immune coculture | phenotype가 target cell alone이 아니라 interaction event에서 나옴 |
| host-microbe or lumen-facing interaction | [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) plus access control | organism/epithelium interface가 실험의 핵심 |
| hypoxia, perfusion, or maturation bottleneck | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) | tissue support 문제가 baseline phenotype을 누르고 있음 |
| multicompartment homeostasis or niche dependence | [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md) | vascular, stromal, hematopoietic-like support를 분리해서는 질문이 안 섬 |

## 1. Choose immune first when the phenotype is an interaction event

[Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)는 organoid의 value가 derivation 자체보다 **immune-interaction assay**에서 생긴다고 보여준다. 여기서 missing piece는 perfusion이 아니라 **effector partner**다.

[Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)도 같은 구조를 가진다. baseline epithelium만으로는 host-microbe biology가 성립하지 않고, microbial exposure branch가 있어야 질문이 열린다.

이 경우 vascularization이나 niche expansion을 먼저 넣는 것은 우회일 수 있다. 먼저 붙여야 하는 것은 **현상을 실제로 만드는 interaction partner**다.

## 2. Choose vascular first when tissue support limits the baseline

[Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)는 공통적으로 **조직 내부 support 부족이 baseline biology를 누를 수 있다**는 점을 보여준다.

- brain에서는 hypoxia, apoptosis, vascular-like integration이 중요해질 수 있다.
- kidney에서는 flow와 perfusion이 maturation과 polarity를 크게 바꾼다.
- portable multicompartment upgrade 관점에서는 mesodermal progenitor mixing이 먼저 검토될 수 있다.

따라서 phenotype가 interaction failure보다 **stressed core, poor maturation, diffusion limit** 쪽으로 보이면 vascular support가 immune layer보다 우선이다.

## 3. Choose niche-rich models first when the biology is constitutively multicompartment

[Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)는 어떤 질문은 vascular or immune single add-on으로는 충분하지 않음을 보여준다. bone marrow-like biology는 vascular, stromal, hematopoietic 관계가 함께 있어야 해석 가능하다.

이런 경우에는 "무엇을 하나만 더할까"보다 **single-lineage organoid를 유지하는 것 자체가 reductionist failure인가**를 먼저 물어야 한다.

즉 niche-first는 가장 비싼 선택이지만, 질문이 niche-defined라면 오히려 가장 직접적인 선택이다.

## 4. Access problems often masquerade as missing-compartment problems

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)는 standard organoid geometry 자체가 assay를 막을 수 있음을 보여준다. apical surface가 안 열려 있으면 infection, barrier, exposure biology가 계속 왜곡된다.

그래서 이 corpus에서의 실제 우선순위는 종종 이렇게 읽힌다.

1. **surface와 geometry를 먼저 맞춘다**
2. **그 다음 실제 partner를 붙인다**
3. **그 후에도 tissue support가 부족하면 vascular branch로 간다**
4. **여전히 biology가 단순화되어 있으면 niche-rich model로 넘어간다**

## 5. Full niche should not be the default first move

Full niche model은 강하지만 해석과 표준화 비용도 같이 오른다. [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)가 보여주듯 multicompartment gain이 큰 대신 simpler assay보다 throughput과 attribution이 나빠질 수 있다.

그래서 이 corpus는 **niche-first를 default로 두지 않는다.** niche dependence가 핵심일 때만 먼저 간다. 그렇지 않으면 immune or vascular single branch가 더 좋은 first correction일 때가 많다.

## Rule of thumb

- **Immune first**: phenotype가 killing, recognition, immune evasion, inflammatory interaction에 달려 있을 때
- **Vascular first**: phenotype가 hypoxia, necrotic core, perfusion, maturation ceiling에 달려 있을 때
- **Niche first**: phenotype가 multicompartment support 없이는 성립하지 않을 때
- **Access first**: assay entry point가 막혀 있을 때

## What this query does not settle

- 같은 organoid system에서 immune, vascular, niche priority를 head-to-head로 비교한 evidence는 없다.
- immune과 vascular을 동시에 붙이는 hybrid path의 일반 규칙도 아직 corpus가 충분히 주지 않는다.
- organ-specific cost와 scalability를 숫자로 비교할 수 있을 정도의 data는 없다.

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
