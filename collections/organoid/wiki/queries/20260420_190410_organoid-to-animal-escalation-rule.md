---
title: "Knowing when an organoid project should escalate to animal validation"
status: active
created: 2026-04-20T19:04:10+09:00
---

# 언제 organoid에서 animal로 escalation해야 하나

## Question

Organoid project를 하다 보면 transplantation이나 animal validation으로 빨리 넘어가고 싶어진다. 하지만 in vitro에서 더 해결할 수 있는 문제도 많다. 이 corpus 기준으로 언제 organoid-only 단계에서 animal branch로 올라가는 것이 맞나?

## Short answer

이 corpus는 **animal을 generic rescue step으로 쓰지 말고, host-only question이 생겼을 때 escalation하라**고 말한다.

- **repair, engraftment, regeneration**이 claim이면 animal branch가 필요하다.
- **circuit integration, long-range host engagement**이 claim이면 animal branch가 필요하다.
- **host circulation or injury context**가 phenotype의 일부면 animal branch가 필요하다.
- 반대로 **geometry, coculture, perfusion, screening, perturbation**으로 풀 수 있는 문제라면 in vitro에서 더 오래 머무는 편이 낫다.

즉 escalation 기준은 "organoid가 완벽하지 않다"가 아니라 **질문이 host를 본질적으로 요구하느냐**다.

## The core rule

**host가 없으면 claim이 아예 정의되지 않는 경우에만 animal로 간다.**

반대로 host가 없어도 답할 수 있는 질문이라면, 먼저 in vitro branch를 더 밀어붙이는 편이 해석과 throughput 모두에서 유리하다.

## When escalation is clearly justified

## 1. Repair or engraftment is the endpoint

[Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)는 intestinal organoid를 colitis repair context로 옮긴다. 여기서 핵심 질문은 organoid가 dish에서 예쁘게 자라느냐가 아니라 **injury setting에서 repair or engraftment를 하느냐**다.

이런 질문은 host context 없이 대체하기 어렵다. 따라서 translational repair claim에서는 animal escalation이 자연스럽다.

## 2. Circuit engagement is the endpoint

[Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)는 cortical organoid를 host circuit 안으로 넣어 본다. 여기서 필요한 것은 단순 firing이 아니라 **host neural circuit engagement**다.

MEA, calcium imaging, oscillation은 in vitro에서 가능하지만, **host-connected circuit participation**은 별개의 질문이다. 그래서 brain organoid가 animal branch로 넘어갈 이유는 "더 성숙해 보이게 만들고 싶어서"가 아니라 **host-connected function을 검증해야 해서**다.

## 3. Circulation-linked validation matters

[Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)는 transplantation 후 host circulation integration을 본다. 혈관이 실제 순환계와 연결되는가는 dish assay만으로는 완전히 대체하기 어렵다.

따라서 vasculature가 구조가 아니라 **functional circulation interface**를 요구할 때는 animal branch의 가치가 커진다.

## When escalation is premature

## 1. The real problem is access or geometry

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)는 exposure surface가 막혀 있으면 readout이 왜곡될 수 있음을 보여준다. 이런 경우 animal로 가기 전에 **apical access or geometry**를 고치는 편이 먼저다.

## 2. The real problem is a missing interaction partner

[Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)와 [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)는 many questions가 host transfer 없이도 **specific coculture layer**로 열릴 수 있음을 보여준다.

즉 immune or microbial interaction 질문을 바로 animal로 넘기는 것은 종종 과도한 escalation이다.

## 3. The real problem is diffusion or maturation

[Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)는 in vitro 안에서도 vascularization or perfusion branch로 maturation barrier를 상당 부분 건드릴 수 있음을 보여준다.

따라서 necrotic core, hypoxia, poor polarity, weak maturation이 보일 때 animal로 바로 넘어가기보다 **in vitro tissue-support branch**를 먼저 시도하는 편이 낫다.

## 4. The goal is perturbation or screening

[Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md), [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)는 platform value가 **controlled readout, comparability, throughput**에 있음을 보여준다.

이런 프로젝트는 host context보다 standardized baseline이 더 중요하다. animal로 너무 빨리 올라가면 attribution과 scale이 무너질 수 있다.

## Decision table

| main question | default branch in this corpus | why |
|---|---|---|
| does it repair damaged tissue | animal | host injury context가 질문의 일부 |
| does it engage host circuits | animal | host network participation이 endpoint |
| does it respond to immune or microbial partner | in vitro coculture first | partner를 먼저 명시적으로 붙일 수 있음 |
| is the tissue too immature or stressed | in vitro vascular/perfusion first | maturation rescue가 animal 없이도 가능할 수 있음 |
| is the project a screen or perturbation platform | in vitro first | comparability와 throughput이 우선 |

## A good escalation sequence

1. **baseline organoid를 reproducible하게 만든다**
2. **질문에 맞는 in vitro assay branch를 먼저 붙인다**
3. **그래도 host-only claim이 남으면 animal로 간다**
4. **animal 결과는 host-influenced phenotype으로 해석한다**

이 순서를 따르면 animal branch가 rescue move가 아니라 **claim-matched validation move**가 된다.

## What escalation changes interpretively

Animal로 가면 biology가 richer해지지만, [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)와 [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)가 보여주듯 **host environment가 phenotype의 일부**가 된다.

그래서 animal data는 더 강한 validation일 수 있지만, 동시에 organoid-intrinsic effect를 덜 깨끗하게 만든다. 이 tradeoff를 감수할 이유가 있을 때만 escalation하는 것이 맞다.

## Rule of thumb

- **animal로 간다**: repair, engraftment, host circuit, circulation-linked integration이 endpoint일 때
- **in vitro에 남는다**: geometry, coculture, perfusion, screening, perturbation으로 질문을 더 직접 풀 수 있을 때
- **animal을 미루지 않는다**: 최종 claim이 원래부터 host-defined일 때
- **animal을 서두르지 않는다**: baseline이 아직 noisy하고 assay logic이 정리되지 않았을 때

## What this query does not settle

- organ별로 언제 animal escalation benefit이 급격히 커지는지 정량 기준은 없다.
- humanized immune model 같은 중간 단계는 이 corpus에서 충분히 다뤄지지 않는다.
- long-term transplantation이 in vitro maturity claim을 얼마나 대체할 수 있는지도 아직 불완전하다.

## Sources used

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
