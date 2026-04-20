---
title: "Choosing a vascularization strategy by payoff versus adoption cost"
status: active
created: 2026-04-20T17:41:24+09:00
---

# 어떤 vascularization 전략이 도입 비용 대비 가장 큰 payoff를 주나

## Question

Organoid에 vasculature나 perfusion을 붙이고 싶을 때 선택지는 많아 보인다. stand-alone vessel organoid, TF-driven co-development, flow-based perfusion, mesodermal progenitor mixing, transplantation까지 있는데, 이 corpus 기준으로 어떤 전략이 adoption cost 대비 payoff가 가장 큰가?

## Short answer

이 corpus에서는 단일한 승자가 없다. 대신 **무엇을 얻고 싶은지와 무엇을 감당할 수 있는지가 전략을 갈라놓는다.**

- **가장 portable한 general upgrade**는 [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) 쪽이다.
- **가장 큰 organ-specific maturation payoff**는 kidney 맥락에서 [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)가 준다.
- **brain-specific hypoxia relief와 integrated vascular-like network payoff**는 [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)가 강하다.
- **vasculature 자체가 모델의 주인공**이면 [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)가 baseline이다.
- **가장 강한 final validation**은 여전히 transplantation이지만, 보통 first upgrade라기보다 downstream confirmation layer에 가깝다.

즉, "best tradeoff"는 하나가 아니라 **general portability, organ-specific maturity, engineering burden, host dependence** 중 무엇을 최적화하는지에 따라 달라진다.

## Four adoption-cost dimensions in this corpus

이 collection에서 vascularization strategy의 도입 비용은 대략 네 종류로 나뉜다.

| cost axis | 질문 | 전략별 차이 |
|---|---|---|
| engineering burden | genome editing이나 TF induction이 필요한가 | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md) 쪽 부담이 큼 |
| hardware burden | custom chip, perfusion setup, device 운영이 필요한가 | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) 쪽 부담이 큼 |
| cell-prep burden | 별도 progenitor population을 따로 만들어 섞어야 하는가 | [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) 부담이 중간 |
| validation burden | host transplantation 없이는 핵심 claim이 안 서는가 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md), transplantation branch 전반 |

## Strategy-by-strategy table

| strategy | main payoff | main adoption cost | best fit in this corpus |
|---|---|---|---|
| stand-alone vessel organoid | vasculature 자체를 정의하고 검증 가능 | organ-specific integration은 따로 풀어야 함 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) |
| TF-driven integrated vascularization | organoid 내부에서 hypoxia 완화, vascular-like network, BBB-like features | genetic engineering burden | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md) |
| flow/perfusion-based maturation | endogenous vascular expansion, polarity, adult-like expression | custom device + perfusion workflow | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) |
| mesodermal progenitor mixing | relatively portable modular vascularization, mural cells, microglia-like component까지 확장 | extra progenitor prep와 mixing optimization | [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| transplantation | strongest host-linked maturation/integration confirmation | in vivo logistics, attribution difficulty | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md), [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md), [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |

## 1. Wimmer is the clean baseline when vasculature itself is the question

[Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)는 가장 먼저 "혈관 organoid가 무엇인가"를 정의하는 쪽이다.

- endothelial cells + pericytes + basement membrane
- 2-3주 안에 microvasculature 형성
- transplantation 후 host circulation integration
- diabetic vasculopathy modeling

이 전략의 장점은 conceptually 깨끗하다는 점이다. 단점은 organ-specific maturation question, 예를 들어 kidney maturation이나 cortical hypoxia를 바로 해결하지는 못한다는 것이다.

## 2. Cakir has a strong payoff when the problem is inside brain organoids

[Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)는 brain organoid의 necrotic core, hypoxia, BBB-like feature 부족을 정면으로 푼다.

- 20% ETV2+ cell mixing
- day 18 induction
- perfusable vascular-like lumen
- dramatic hypoxia/apoptosis reduction
- cortical architecture를 크게 흐리지 않음

대신 이 전략은 **genetic engineering을 감당할 수 있을 때만** 효율이 좋다. 따라서 brain-specific payoff는 크지만, 가장 universally adoptable한 방법이라고 보긴 어렵다.

## 3. Homan gives the highest in vitro maturation payoff, but hardware cost is real

[Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)는 이 corpus 안에서 가장 강하게 "vascularization이 organ maturation을 얼마나 바꾸는가"를 보여준다.

- 5x PECAM1+ vessel area
- perfusable vascular networks
- podocyte/tubule polarity 향상
- more adult-like vascular and tubular expression

이건 payoff가 매우 크다. 하지만 custom 3D-printed millifluidic chip, ECM setup, perfusion 운영이 필요하다. 따라서 **가장 좋은 biology payoff 중 하나지만, 가장 가벼운 adoption path는 아니다.**

## 4. Wörsdorfer may be the best general tradeoff for many labs

[Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)는 general-purpose modular strategy로 읽히는 부분이 크다.

- MPC를 따로 만들어 섞기만 하면 됨
- vascular networks와 mural cells 형성
- neural and tumor contexts 둘 다 시연
- microglia-like cells까지 같이 들어옴
- source page 기준, chip 접근보다 cheaper and more scalable하게 해석됨

이 전략은 organ-specific optimization은 덜하지만, **custom hardware나 TF engineering 없이 multicompartment payoff를 얻을 수 있다는 점**에서 많은 프로젝트의 first vascularization attempt로 가장 현실적이다.

## 5. Transplantation is strongest validation, not usually the first upgrade

[Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md), [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)는 공통적으로 host-context가 최종 confirmation으로 매우 강하다는 점을 보여준다.

하지만 transplantation은:

- host environment가 phenotype 일부가 되고
- attribution이 어려워지고
- adoption barrier가 높다

그래서 이 corpus에서는 보통 **first vascularization choice**라기보다 **downstream validation branch**로 읽는 편이 더 맞다.

## Practical rule of thumb

1. **vasculature 자체가 모델 주인공이면** Wimmer부터 본다.
2. **brain organoid hypoxia와 BBB-like integration이 문제면** Cakir을 본다.
3. **kidney maturation을 실제로 끌어올리고 싶으면** Homan을 본다.
4. **여러 organoid에 portable한 vascular upgrade가 필요하면** Wörsdorfer를 먼저 검토한다.
5. **최종 host-context confirmation이 목표면** transplantation으로 간다.

## What this corpus suggests avoiding

- vasculature가 왜 필요한지 정의하지 않고 가장 화려한 전략부터 고르는 것
- organ-specific maturation question인데 stand-alone vessel module만으로 끝내는 것
- screening readiness가 중요한데 first step부터 transplantation으로 가는 것
- adoption burden을 무시하고 device-heavy 또는 TF-heavy 방법을 default로 두는 것

## What this knowledge base does not settle

- 네 전략을 같은 organoid system에서 정면 비교한 head-to-head evidence는 없다.
- adoption cost의 숫자화된 benchmark도 없다.
- lung, intestine 등 다른 organ system에서 Homan-style flow payoff가 재현되는지는 아직 corpus가 충분히 말해주지 않는다.

## Sources used

- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
