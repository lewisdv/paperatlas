---
title: "When to choose vascularization, perfusion, or transplantation"
status: active
created: 2026-04-20T17:20:29+09:00
---

# 언제 vascularization, perfusion, transplantation 중 무엇을 선택해야 하나

## Question

Organoid를 더 성숙하게 만들거나 기능 검증을 강화하려고 할 때, in vitro vascularization, flow/perfusion, transplantation 중 무엇을 언제 선택해야 하나?

## Short answer

이 corpus에서는 세 전략이 같은 것이 아니다.

- **vascularization**은 organoid 안에 혈관성 구조나 혈관 세포를 도입하는 설계 선택이다.
- **perfusion/flow**는 기계적 환경과 mass transport를 바꿔 endogenous maturation을 밀어주는 전략이다.
- **transplantation**은 host environment 자체를 실험 변수로 끌어들이는 검증 전략이다.

따라서 “더 강한 버전의 같은 방법”으로 보기보다, **질문이 in-dish mechanism인지, organ-specific maturation인지, host-context validation인지**로 골라야 한다.

## Decision table

| 목표 | 우선 선택 | 이 corpus의 근거 | 대표 페이지 |
|---|---|---|---|
| 혈관 organoid 자체를 baseline으로 만들고 싶다 | stand-alone vascular organoid | vessel-only baseline을 제공하고 microvascular identity를 정의함 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) |
| brain organoid 내부에서 hypoxia를 줄이며 vascular-like network를 만들고 싶다 | TF-driven vascularization | ETV2-driven endothelial fate induction으로 cortical organoid 안에서 network 형성 | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md) |
| kidney organoid의 endogenous vascular compartment와 maturation을 in vitro에서 끌어올리고 싶다 | flow/perfusion | mechanical flow, device geometry, ECM가 kidney maturation을 밀어줌 | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) |
| 여러 organoid context에 재사용 가능한 vascular addition이 필요하다 | mesodermal progenitor mixing | vasculature와 mural cell, microglia-like component까지 같이 넣는 모듈형 전략 | [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| host repair, circuit engagement, in vivo rescue를 직접 보고 싶다 | transplantation | host context에서 engraftment와 functional validation을 봄 | [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md), [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |

## How to think about the three branches

## 1. Vascularization is best when the question is still mostly in vitro

혈관화 전략은 “organoid 안에서 무엇을 더 넣어야 biological failure mode가 줄어드는가”에 가깝다.

- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md): 혈관 organoid 자체를 baseline으로 정의
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md): brain organoid 내부에서 vascular-like network를 형성해 hypoxia와 apoptosis를 줄임
- [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md): organ-independent하게 vascular component를 주입하는 범용 전략

즉, **host 없이도 해결하고 싶은 병목이 산소/영양/vascular compartment 부재인지**가 핵심이다.

## 2. Perfusion is best when mechanical environment is part of the bottleneck

[Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)는 vascularization을 단순히 endothelial cell 추가로 보지 않고, **flow 자체가 maturation variable**이라고 본다.

이 접근은 특히 다음 질문에 맞는다.

- organ-specific maturation이 필요하다
- endogenous vascular compartment를 키우고 싶다
- genetic engineering 없이 in vitro 환경을 바꾸고 싶다

대신 장치, ECM, 운영 복잡도가 올라가므로 screening-ready simplicity는 떨어질 수 있다.

## 3. Transplantation is best when validation question이 바뀐다

Transplantation은 vascularization이나 perfusion의 상위 호환이 아니라, 질문 자체를 바꾼다.

- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md): cortical organoid가 host circuit와 실제로 맞물리는지 검증
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): intestinal organoid를 repair context로 옮겨 functional relevance를 테스트
- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md): transplantation이 in vitro stress-linked fidelity defects를 완화한다는 해석에 연결됨

장점은 가장 강한 validation을 준다는 점이지만, 약점은 **host environment가 phenotype의 일부가 되어 attribution이 어려워진다**는 점이다.

## A practical decision rule

1. **질문이 “in vitro system 안에서 hypoxia/vascular absence를 줄일 수 있는가”면** vascularization을 먼저 본다.
2. **질문이 “flow나 perfusion이 organ maturation에 필요한가”면** perfusion을 본다.
3. **질문이 “이 결과가 host context에서도 유지되는가”면** transplantation을 본다.
4. **질문이 “범용 모듈이 필요한가, organ-specific tuning이 필요한가”면** Worsdorfer-type modular approach와 Homan-type organ-specific approach를 나눠서 본다.

## What this corpus implies

- brain에서는 [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)과 [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)가 “in vitro rescue”와 “host validation”을 분리해 보여준다.
- kidney에서는 [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)가 flow를 maturity variable로 만든다.
- generalized vascular module이 필요할 때는 [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)과 [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)가 더 직접적이다.

## What this knowledge base does not settle

- 같은 organ system에서 vascularization, perfusion, transplantation을 **head-to-head로 비교한 통합 evidence**는 없다.
- vessel maturity, adoption cost, throughput, interpretability를 동시에 점수화한 공통 benchmark는 이 corpus에 없다.

## Sources used

- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md)
