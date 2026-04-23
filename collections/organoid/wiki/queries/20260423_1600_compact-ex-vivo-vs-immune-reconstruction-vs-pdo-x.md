---
title: "donor-derived cancer work는 언제 compact ex vivo validation에서 멈추고 언제 immune reconstruction이나 PDO-X로 올라가야 하나"
status: active
created: 2026-04-23T16:00:49+09:00
---

# donor-derived cancer work는 언제 compact ex vivo validation에서 멈추고 언제 immune reconstruction이나 PDO-X로 올라가야 하나

## Question

Patient-derived cancer organoid work를 하다 보면, 어떤 프로젝트는 간단한 ex vivo drug-response assay로도 충분해 보이고, 어떤 프로젝트는 T-cell reconstruction 같은 중간 레이어가 필요해 보이며, 또 어떤 프로젝트는 결국 PDO-X까지 올라가야 할 것 같다. 이 corpus 기준으로 언제 어느 단계에서 멈추는 게 맞나?

## Short answer

이 corpus의 가장 실용적인 규칙은 이렇다. **tumor-intrinsic drug-response나 sensitization만 묻는다면 compact ex vivo validation에서 멈추고, missing partner가 명확하면 immune reconstruction으로 가고, host-dependent stromal, metastatic, or context-restored biology가 핵심이면 PDO-X로 올라간다.**

- **compact ex vivo validation**
  - 질문: donor-derived tumor가 특정 drug 또는 perturbation에 반응하는가
  - stop here when: endpoint가 short-turnaround viability, sensitization, 또는 direct tumor-cell response로 충분할 때
- **immune reconstruction**
  - 질문: 반응을 바꾸는 missing partner가 T cell 같은 정의 가능한 effector인가
  - escalate here when: host 전체가 아니라 reconstructed immune interaction이 핵심일 때
- **PDO-X**
  - 질문: stromal remodeling, metastasis, host-restored signaling, in vivo pharmacology가 필요한가
  - escalate here when: dish 안에서는 핵심 readout이 사라지거나 false negative가 날 가능성이 클 때

즉 기준은 complexity preference가 아니라 **무슨 readout이 아직 빠져 있는가**다.

## Practical decision table

| branch | 먼저 묻는 질문 | 여기서 멈춰도 되는 경우 | 더 올라가야 하는 신호 | 대표 anchor |
|---|---|---|---|---|
| Compact ex vivo validation | tumor-intrinsic response가 보이는가 | short-term donor-aware drug response나 sensitization이 이미 해석 가능하다 | 결과가 plausibly negative인데 context loss가 의심된다 | [L 2024](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md) |
| Immune reconstruction | missing layer가 defined immune partner인가 | T-cell infiltration, killing, checkpoint-response 같은 readout이 reconstructed coculture로 operationalize된다 | bone/stroma/metastatic niche까지 readout을 바꾸는 것 같다 | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md), [W 2026](../sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md) |
| PDO-X | host context가 결과를 바꾸는가 | metastasis, stromal remodeling, context-restored pathway, in vivo pharmacology가 최종 claim이다 | dish readout만으로는 undercall 또는 false negative 위험이 크다 | [J 2026](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md), [Patient-derived 2026](../sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md) |

## 1. Compact ex vivo validation is enough when the claim is tumor-intrinsic and operationally clear

[Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)은 compact ex vivo validation이 언제 충분한지 가장 잘 보여준다.

- donor-derived colon cancer organoids에서 short-term drug assay를 돌린다
- 핵심 질문은 broad host biology가 아니라 **cisplatin sensitization이 donor-derived 3D context에서도 보이는가**다
- 여기서는 viability plus combination logic만으로도 translational checkpoint 역할을 할 수 있다

이 branch에서는 다음이 맞으면 멈춰도 된다.

- readout이 tumor-cell intrinsic response에 가깝다
- effect direction이 clear하다
- extra compartment가 없어서 오히려 interpretation이 단순하다
- 이 assay가 mechanistic claim의 마지막 sanity check 역할을 한다

즉 compact ex vivo는 "간이판"이라서 약한 것이 아니라, **질문이 충분히 작고 direct할 때 가장 효율적인 종착점**이다.

## 2. Move to immune reconstruction when the missing layer is a defined effector, not whole-host context

[Tumor organoid-T-cell coculture systems](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)는 immune-interaction assay를 dish 안에서 복원할 수 있음을 보여주고, [Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy](../sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md)은 그 논리를 훨씬 더 translational하게 밀어붙인다.

[W 2026](../sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md)의 포인트는 이렇다.

- organoid biobank를 만든다
- fidelity와 size control을 먼저 맞춘다
- 그 위에 PBMC/T-cell infiltration을 재구성한다
- anti-PD1 같은 immunotherapy logic을 test한다

여기서는 host 전체가 필요한 게 아니라, **빠져 있는 partner가 immune effector라는 점이 분명**하다. 그래서 PDO-X보다 먼저 immune reconstruction으로 가는 것이 맞다.

이 branch로 올라갈 신호는 다음과 같다.

- plain PDO assay만으로는 immune killing이나 infiltration을 말할 수 없다
- 하지만 stromal/metastatic host niche까지는 아직 필요 없다
- 프로젝트 목표가 personalized immunotherapy triage처럼 빠른 assay 운영성과를 요구한다

따라서 immune reconstruction은 단순한 중간 복잡도가 아니라, **defined missing partner를 복구하는 정확한 escalation**이다.

## 3. Move to PDO-X when host context changes the biology rather than merely decorating it

[Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)와 [Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression](../sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md)는 왜 PDO-X가 필요한지 보여준다.

### J 2026: host-restored signaling

- isolated PDO culture에서는 context-sensitive SRC-family kinase activity가 눌린다
- PDO-X에서는 그 신호가 부분적으로 다시 나타난다
- 따라서 in vitro negative가 true negative가 아닐 수 있다

### Patient-derived 2026: metastasis and stromal remodeling

- breast PDO biobank에서 먼저 front-end perturbation screen을 한다
- 그 다음 selected models만 PDO-X로 올린다
- in vivo에서 stromal programs, splicing changes, lung metastasis burden을 본다

이 두 source를 합치면 PDO-X는 보통 다음 상황에서 필요하다.

- readout이 metastasis다
- stromal remodeling이나 host pharmacology가 claim의 일부다
- isolated culture가 pathway를 undercall하거나 suppress할 가능성이 높다
- in vitro screen은 triage 역할만 하고 final biology는 host context에서 결정된다

즉 PDO-X는 "더 리얼한 모델"이라서 가는 것이 아니라, **질문 자체가 host-restored biology를 요구하기 때문에 가는 것**이다.

## 4. A clean escalation ladder for donor-derived cancer work

이 corpus를 기준으로 donor-derived cancer work의 기본 순서는 이렇게 정리하는 게 좋다.

1. **Compact ex vivo PDO**
   - tumor-intrinsic response, short-turnaround drug triage, sensitization assay
2. **Immune reconstruction**
   - defined immune partner가 빠져 있을 때
3. **PDO-X**
   - metastasis, stromal remodeling, host-restored signaling, in vivo persistence가 claim일 때

중요한 점은 이 세 단계가 반드시 전부 필요한 것은 아니라는 것이다. 오히려 많은 프로젝트는 **앞 단계에서 멈춰야 더 정확하다**.

## Rule of thumb

- **compact ex vivo에서 멈춘다**
  - donor-derived response signal이 이미 선명하고
  - endpoint가 short-term viability, sensitization, 또는 direct perturbation response일 때
- **immune reconstruction으로 간다**
  - missing biology가 T-cell infiltration, killing, checkpoint interaction처럼 defined partner 문제일 때
- **PDO-X로 간다**
  - host stroma, metastasis, or context-restored pathway가 없으면 claim이 바뀔 때

## What this corpus suggests avoiding

- host-like complexity가 좋아 보인다는 이유만으로 PDO-X를 너무 빨리 선택하는 것
- immune partner 문제를 whole-animal escalation으로 바로 해결하려는 것
- compact ex vivo negative를 context loss 가능성 검토 없이 final negative로 처리하는 것
- metastasis나 stromal-response claim을 simple PDO viability assay만으로 대신하려는 것

## What this knowledge base does not settle

- immune reconstruction과 PDO-X를 같은 immunotherapy question에서 정면 비교한 head-to-head evidence는 제한적이다
- humanized host나 stromal partial-reconstitution 같은 중간 단계는 corpus 안에서 아직 얇다
- 각 branch의 turnaround time, cost, and predictive value를 정량 비교한 공통 benchmark는 없다

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Triage organoid systems for translational screening](20260420_174126_translational-screening-triage.md)
- [Deciding when coculture is enough versus when host validation is necessary](20260420_191749_coculture-vs-host-validation-for-interaction-questions.md)
- [Designing escalation ladders for different disease-modeling goals](20260420_191751_disease-specific-organoid-escalation-ladders.md)
- [Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)
- [Tumor organoid-T-cell coculture systems](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy](../sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md)
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)
- [Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression](../sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md)
