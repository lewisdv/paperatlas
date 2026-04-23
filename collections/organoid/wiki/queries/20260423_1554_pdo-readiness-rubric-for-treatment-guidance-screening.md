---
title: "PDO가 treatment-guidance형 translational screening에 들어갈 준비가 됐는지 어떻게 판정해야 하나"
status: active
created: 2026-04-23T15:54:03+09:00
---

# PDO가 treatment-guidance형 translational screening에 들어갈 준비가 됐는지 어떻게 판정해야 하나

## Question

Patient-derived organoid는 전부 translational screening에 가까워 보이기 쉽지만, 실제로는 어떤 라인은 아직 establishment 단계에 머물고 어떤 라인은 treatment-guidance형 assay까지 감당할 수 있을 정도로 operationally ready해 보인다. 이 corpus 기준으로 PDO가 정말 screening-ready라고 부를 수 있으려면 어떤 gate를 넘어야 하나?

## Short answer

이 corpus에서는 PDO readiness를 단순히 "patient tissue에서 자랐다"로 보지 않는 편이 맞다. 가장 실용적인 규칙은 **specimen adequacy, line stability, freeze-thaw recoverability, pathology or molecular concordance, assay-endpoint credibility**를 순서대로 통과한 뒤에만 treatment-guidance형 screening으로 올리는 것이다.

- **Gate 1: specimen adequacy**
  - clinically available sample이라도 tumor cellularity와 pre-analytic handling이 충분해야 한다
- **Gate 2: establishment stability**
  - 일회성 outgrowth가 아니라 passaging과 expansion이 가능해야 한다
- **Gate 3: banking and thaw QC**
  - banking 후에도 regrowth가 재현돼야 operational screen이 된다
- **Gate 4: disease fidelity**
  - 최소한 histology, IHC, 또는 핵심 분자 특징이 원시료와 연결돼야 한다
- **Gate 5: assay-endpoint credibility**
  - viability, sensitization, 또는 response readout이 screening claim에 맞게 해석 가능해야 한다

즉 이 corpus에서 screening-ready PDO는 **patient-derived인 것 자체**가 아니라 **specimen-to-bank-to-assay pipeline이 이미 안정화된 PDO**다.

## A practical readiness rubric

| gate | 확인할 것 | ready로 볼 기준 | 아직 이르면 보이는 신호 | 대표 anchor |
|---|---|---|---|---|
| 1. specimen adequacy | sample type, transport, tumor cellularity | clinic이 실제로 주는 specimen으로도 viable epithelial input이 확보된다 | sample은 있으나 stromal-heavy, delayed, low-input라 take rate가 흔들린다 | [S 2025](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md), [N 2025](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md) |
| 2. establishment stability | expansion, passaging, line maintenance | serial passage와 scale-up이 가능하다 | 첫 outgrowth는 있지만 line처럼 운영되지는 않는다 | [Driehuis 2020](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) |
| 3. banking and thaw QC | cryostorage 후 regrowth | freeze-thaw 후에도 regrowth와 morphology가 유지된다 | thaw 이후 recovery가 불안정해 batch scheduling이 안 된다 | [S 2025](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md) |
| 4. disease fidelity | pathology or molecular concordance | histology, IHC, transcriptional, 또는 핵심 phenotype이 원시료와 이어진다 | organoid는 자라지만 original lesion과 연결되는 evidence가 약하다 | [N 2025](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md), [J 2026](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) |
| 5. assay-endpoint credibility | readout가 실제 decision을 지지하는가 | response metric이 단순 생존률을 넘어 treatment question에 맞게 해석된다 | dose toxicity와 sensitization이 섞이거나, endpoint가 임상적 질문과 어긋난다 | [L 2024](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md) |
| 6. escalation rule | in vitro만으로 충분한가 | missing niche가 claim을 바꾸지 않는다고 판단 가능하다 | microenvironment-dependent pathway라면 compact PDO만으로는 false negative가 생길 수 있다 | [J 2026](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) |

## 1. Readiness starts before culture: specimen adequacy is the first gate

[Protocol for generation and utilization of patient-derived organoids from multimodal specimen.](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md)와 [Protocol for the establishment and characterization of South African patient-derived intestinal organoids.](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md)는 같은 점을 강하게 보여준다. PDO readiness의 첫 병목은 media recipe보다 **sample logistics**다.

- small biopsy, fluid specimen, 혹은 metastatic core sample도 PDO 출발점이 될 수는 있다
- 하지만 tumor cellularity, transport delay, digestion timing, specimen size가 take rate를 크게 바꾼다
- 따라서 screening-ready의 첫 기준은 "수술 검체가 있느냐"가 아니라 **clinic이 실제로 주는 specimen에서 반복적으로 line을 세울 수 있느냐**다

이 corpus에서는 specimen adequacy를 넘기지 못하면 뒤의 assay sophistication은 큰 의미가 없다.

## 2. Outgrowth is not enough: line stability and expansion are the real baseline

[Establishment of patient-derived cancer organoids for drug-screening applications](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)는 PDO를 translational screening branch로 올릴 수 있는 최소 baseline이 무엇인지 가장 또렷하게 보여준다.

- PDO는 primary tissue에서 한번 살아남는 것만으로는 부족하다
- downstream drug testing을 감당하려면 expansion과 maintenance가 가능해야 한다
- 이 안정성이 있어야 replicate, dose matrix, re-test, perturbation follow-up이 가능해진다

따라서 이 corpus에서 **established PDO**와 **screening-ready PDO**는 비슷하지만 같은 말은 아니다. 후자는 line-like operational stability를 전제한다.

## 3. Banking and thaw recovery decide whether screening can become a program

[S 2025](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md)의 가장 중요한 실전 메시지 중 하나는 biobanking과 thaw QC를 downstream convenience가 아니라 readiness gate로 다룬다는 점이다.

- bankable하지 않으면 한 번의 successful derivation이 프로그램으로 이어지지 않는다
- thaw 후 regrowth가 흔들리면 plate scheduling, replicate alignment, retrospective re-test가 어려워진다
- 따라서 treatment-guidance형 screening은 culture establishment보다 **bank-to-assay continuity**를 더 강하게 요구한다

이 corpus 기준으로 freeze-thaw recovery를 확인하지 않은 PDO는 promising할 수는 있어도 아직 operational screening asset이라고 부르기 어렵다.

## 4. Fidelity must be shown, not assumed

[N 2025](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md)는 histology, immunofluorescence, RT-qPCR, lipid or cholesterol characterization까지 붙여서 organoid가 원시료와 어떻게 이어지는지 보여주고, [J 2026](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)는 더 나아가 **무엇이 유지되고 무엇이 빠지는지**를 정량화한다.

이 두 source를 합치면 다음 규칙이 나온다.

- morphology concordance가 있으면 출발점으로는 좋다
- 하지만 signaling이나 context-sensitive pathway가 question의 핵심이면 morphology만으로는 부족하다
- 따라서 readiness는 "원시료와 닮았다"보다 **screen에서 중요한 feature가 culture에서도 유지되는가**로 판정해야 한다

즉 fidelity gate는 generic authenticity check가 아니라, **질문에 맞는 fidelity check**여야 한다.

## 5. A believable assay endpoint matters more than a generic viability screen

[Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)는 compact ex vivo PDO assay가 언제 유용한지 잘 보여준다.

- donor-derived colon cancer organoids를 짧은 viability assay에 올린다
- 하지만 핵심은 단순 killing이 아니라 **cisplatin sensitization이 실제로 생겼는지**를 보는 것이다
- arsenic 자체 독성이 있기 때문에 dose choice와 combination logic이 해석 가능성을 좌우한다

이 corpus에서 treatment-guidance형 screening readiness는 단순히 "CellTiter assay가 가능하다"가 아니다. **endpoint가 mechanistic question이나 treatment decision과 맞물려 해석 가능한가**가 더 중요하다.

## 6. Some PDOs are screen-ready for ex vivo triage, but not for final claims

[J 2026](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)는 중요한 경고를 준다. 어떤 metastatic PDO는 histology와 많은 signaling을 유지하지만, SRC-family 같은 microenvironment-sensitive module은 in vitro에서 눌리고 host re-engraftment에서 다시 나타날 수 있다.

이 말은 다음을 뜻한다.

- 어떤 PDO는 **compact ex vivo treatment triage**에는 ready일 수 있다
- 하지만 host-dependent pathway, metastatic niche, immune reconstruction이 질문의 핵심이면 그것만으로 final claim을 내리면 안 된다
- readiness rubric의 마지막 gate는 "screen을 할 수 있나"가 아니라 **이 screen이 어디까지 말해줄 수 있나**다

따라서 treatment-guidance형 PDO screen은 종종 end point가 아니라 **escalation decision을 거는 중간 단계**다.

## A simple decision rule for this corpus

1. specimen이 반복적으로 viable epithelial input을 준다
2. line이 serial passage와 expansion을 견딘다
3. thaw 후 regrowth가 재현된다
4. 원시료와 연결되는 pathology or molecular QC가 있다
5. assay endpoint가 treatment question과 직접 맞물린다
6. missing niche가 결과를 뒤집을 수 있으면 PDO-X, immune reconstruction, 또는 richer follow-up을 예약한다

이 여섯 개 중 앞의 다섯 개가 충족되면 이 corpus에서는 보통 **screen-ready PDO**, 여섯 번째까지 명시되면 **well-scoped translational PDO workflow**에 가깝다.

## Practical rule

- **Not ready yet**
  - specimen 확보는 됐지만 take rate와 growth consistency가 흔들릴 때
  - passaging이나 thaw recovery 없이 첫 derivation만 성공했을 때
  - morphology는 그럴듯하지만 treatment endpoint가 아직 generic viability에 머물 때
- **Ready for compact ex vivo screening**
  - specimen-to-line-to-bank 파이프라인이 안정화되고, response readout이 donor-aware하게 해석 가능할 때
- **Needs escalation before strong claim**
  - pathway가 host, stromal, immune, 또는 metastatic context에 크게 의존할 때

## What this corpus suggests avoiding

- freshly established PDO 하나만으로 screening-ready라고 부르는 것
- banking or thaw QC 없이 longitudinal program처럼 운영하려는 것
- pathology concordance 없이 donor relevance를 당연하게 가정하는 것
- toxicity assay를 곧바로 treatment-guidance readout으로 해석하는 것
- host-dependent pathway인데 in vitro negative를 final negative로 처리하는 것

## What this knowledge base does not settle

- take rate, thaw success, turnaround time의 공통 numerical benchmark는 corpus 전반에 없다
- tumor type별로 최소 QC panel이 얼마나 달라야 하는지도 아직 표준화돼 있지 않다
- 실제 patient treatment decision에 얼마나 직접 연결할 수 있는지에 대한 prospective evidence는 제한적이다

## Related entities

- [Biobanking and freeze-thaw QC](../entities/biobanking-and-freeze-thaw-qc.md)
- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)

## Sources used

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Establishment of patient-derived cancer organoids for drug-screening applications](../sources/driehuis_2020_establishment_of_patient-derived_cancer_organoids.md)
- [Protocol for generation and utilization of patient-derived organoids from multimodal specimen.](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md)
- [Protocol for the establishment and characterization of South African patient-derived intestinal organoids.](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md)
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)
- [Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)
