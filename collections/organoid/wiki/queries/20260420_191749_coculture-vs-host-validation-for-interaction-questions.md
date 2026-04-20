---
title: "Deciding when coculture is enough versus when host validation is necessary"
status: active
created: 2026-04-20T19:17:49+09:00
---

# 언제 coculture로 충분하고 언제 host validation이 필요한가

## Question

Interaction biology를 보려는 organoid 프로젝트에서는 coculture를 붙일지, 아니면 더 빨리 transplantation이나 host-context validation으로 올라갈지 항상 애매하다. 이 corpus 기준으로 언제 coculture만으로 충분하고, 언제 host validation이 꼭 필요한가?

## Short answer

이 corpus의 기본 규칙은 간단하다. **상호작용 상대가 명시적으로 정의될 수 있으면 coculture를 먼저 하고, 상호작용 자체가 host environment를 요구하면 host validation으로 간다.**

- **T cell, microbe, apical exposure 같은 defined partner question**이면 coculture가 먼저다.
- **repair, host circuit engagement, circulation-linked integration**이 endpoint면 host validation이 필요하다.
- **interaction 전에 access가 막혀 있으면** coculture와 host 둘 다 아직 이르다.
- **interaction 전에 tissue quality가 무너지고 있으면** host보다 vascular or perfusion correction이 먼저일 수 있다.

즉 기준은 complexity가 아니라 **interaction의 상대를 dish 안에서 충분히 정의할 수 있느냐**다.

## The practical ladder

1. **access and geometry를 먼저 맞춘다**
2. **defined coculture를 먼저 시도한다**
3. **필요하면 tissue-support branch를 붙인다**
4. **그래도 host-only interaction claim이 남으면 host validation으로 간다**

## Decision table

| interaction question | first branch in this corpus | why |
|---|---|---|
| immune killing or tumor-reactive engagement | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)-style coculture | effector partner를 직접 추가할 수 있음 |
| host-microbe or lumen-facing epithelial biology | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md) + [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) | access와 exposure route가 핵심 |
| host repair or injury response | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) | injury context가 질문의 일부 |
| host circuit participation | [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) | host neural network 없이는 endpoint가 정의되지 않음 |
| circulation-linked vascular behavior | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) or later host validation | vessel-host interface가 질문의 일부 |

## 1. Coculture is the right first move when the partner is specific

[Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)는 tumor organoid가 immune-interaction assay로 확장될 수 있음을 보여준다. 여기서 필요한 것은 whole host가 아니라 **T-cell partner**다.

[Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)도 같은 구조다. host-microbe question은 baseline epithelium alone으로는 열리지 않지만, microbial coculture로 직접 operationalize할 수 있다.

이런 질문에서는 host model로 바로 가는 것보다 **missing partner를 dish 안에서 명시적으로 추가하는 것**이 더 직접적이다.

## 2. Access problems should be solved before choosing coculture or host

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)는 apical surface accessibility가 없으면 interaction readout이 계속 왜곡될 수 있음을 보여준다.

즉 many interaction failures는:

- partner가 없어서가 아니라
- partner가 올바른 surface에 닿지 못해서

생긴다.

그래서 이 corpus에서 interaction ladder의 첫 단계는 종종 coculture도 host도 아니라 **geometry correction**이다.

## 3. Host validation becomes necessary when the interaction is host-defined

[Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)는 organoid를 injury repair context로 옮긴다. 여기서 interaction의 상대는 isolated cell type가 아니라 **손상된 host tissue environment**다.

[Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)는 organoid를 host neural circuits 안에 넣어 본다. 여기서는 firing이나 calcium signal만으로는 부족하고, **host circuit participation**이 endpoint다.

따라서 interaction이 specific partner가 아니라 **host-organ system과의 관계**로 정의되면 coculture만으로는 충분하지 않다.

## 4. Some projects need tissue support before they need host validation

[Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)는 vascular-like support가 brain organoid의 hypoxia와 apoptosis를 크게 낮출 수 있음을 보여준다. interaction assay가 안 나오는 이유가 host absence가 아니라 **tissue-support collapse**일 수도 있다는 뜻이다.

이 경우 host로 급히 올라가기보다:

- vascularization
- perfusion
- tissue-quality stabilization

을 먼저 붙이는 편이 더 해석 가능하다.

## 5. Vascular host validation is special because circulation is the claim

[Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)는 vessel organoid가 host circulation과 통합되는지를 본다. 여기서는 partner가 단순 immune cell도 microbe도 아니고 **circulatory host interface**다.

그래서 vascular organoid에서는 coculture가 일부 정보를 줄 수 있어도, **functional circulation integration**은 host validation 쪽에 남는 질문이다.

## A good interaction-validation sequence

1. **access가 맞는지 확인한다**
2. **defined partner가 있으면 coculture를 먼저 한다**
3. **interaction 전에 tissue quality가 무너지면 support branch를 붙인다**
4. **host-specific endpoint가 남을 때만 transplantation이나 in vivo validation으로 간다**

이 순서를 따르면 host model이 "막히면 올리는 마지막 복잡도"가 아니라 **claim-matched final layer**가 된다.

## Rule of thumb

- **coculture로 충분하다**: partner가 specific하고 dish 안에서 정의 가능할 때
- **host validation이 필요하다**: repair, circuit, circulation 같은 host-defined endpoint일 때
- **둘 다 아직 이르다**: geometry가 틀렸거나 tissue quality가 무너질 때

## What this query does not settle

- humanized immune host 같은 중간 단계는 이 corpus에 충분히 없다.
- coculture와 host validation을 같은 biological question에 정면 비교한 head-to-head evidence도 없다.
- stromal-only or partial host mimic branch의 일반 규칙은 아직 빈약하다.

## Sources used

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
