# Brain Organoid Subregion별 프로토콜 비교

## Question

Organoid brain subregion별 프로토콜 차이를 정리해줘.

## Answer

이 corpus에 포함된 brain organoid 논문 13편(ingested 7 + raw 6)을 기반으로, 뇌 subregion별 프로토콜 핵심 차이를 정리한다.

---

## 1. Whole Cerebral (비유도, unguided)

**Lancaster 2014**

- 출발세포: hPSCs (iPSC/ESC)
- 핵심 전략: 외부 patterning factor 최소화, 자가 조직화(self-organization)
- 주요 단계: EB 형성 → neural induction medium → Matrigel embedding → orbital shaker
- 핵심 시약: 특별한 morphogen 없음 (dual SMAD inhibition 미사용)
- 산출 세포: cortex, hippocampus, retina 등 다양한 region이 혼재
- 장점: 넓은 regional diversity
- 한계: 배치 간 variability 높음, 특정 region 농축 어려움

Related: [Lancaster 2014](../sources/lancaster_2014_generation_of_cerebral_organoids_from.md)

---

## 2. Dorsal/Ventral Forebrain & Assembloids

**Sloan 2018**

- 출발세포: hPSCs
- 핵심 전략: directed patterning으로 dorsal vs ventral forebrain을 분리 생성 후 조립
- Dorsal (cortical) spheroid: dual SMAD inhibition (SB431542 + LDN193189)
- Ventral (subpallium) spheroid: SHH agonist (SAG) + WNT inhibitor (IWP-2)
- Assembloid: dorsal + ventral spheroid을 물리적으로 융합 → interneuron migration 연구
- 산출 세포: glutamatergic (dorsal) / GABAergic interneuron (ventral)
- 장점: region 순도 높음, migration/circuit 연구 가능
- 한계: 단일 spheroid에서는 cell diversity 제한적

Related: [Sloan 2018](../sources/sloan_2018_generation_and_assembly_of_human.md)

---

## 3. Telencephalon (Single Rosette 기반)

**Ullah 2025**

- 출발세포: hPSCs → 단일 neural rosette 분리
- 핵심 전략: rosette 수준에서 출발 상태를 균일화하여 variability 감소
- Patterning: forebrain/telencephalic identity
- 장점: 배치 간 재현성 향상, 조직 구조 더 균일
- 한계: rosette isolation이 기술적으로 까다로움

Related: [Ullah 2025](../sources/ullah_2025_generating_and_characterizing_human_telencephalic.md)

---

## 4. Cortical (Semi-guided)

**Fitzgerald 2024**

- 핵심 전략: unguided와 fully guided의 중간 접근 — "semi-guided"
- 최적화 목표: neural oscillation, MEA, calcium imaging 등 전기생리학적 readout
- 장점: 재현성과 diversity 사이 균형, 기능적 분석에 바로 사용 가능
- 한계: baseline organoid 품질에 의존

Related: [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)

---

## 5. Midbrain (중뇌)

### Zagare 2021

- 출발세포: hNESCs (iPSC 유래 neuroepithelial stem cells, 확립에 ~2개월)
- Base medium: N2B27 (DMEM/F12 + Neurobasal + N2 + B27 without vitamin A)
- Maintenance (day 0-8): CHIR-99021 3 uM (WNT) + PMA 0.75 uM (SHH) + ascorbic acid 150 uM
- Embedding: Geltrex droplet (day 6)
- Differentiation (day 10-16): BDNF 10 ng/mL + GDNF 10 ng/mL + db-cAMP 500 uM + TGFb3 1 ng/mL + AA 200 uM + PMA 1 uM (첫 6일만)
- Shaking: day 14부터 (80 rpm)
- 산출: ~60% TH+ dopaminergic neuron (day 30), GFAP+/S100b+ astrocyte, oligodendrocyte
- 적용: Parkinson's disease 모델링

### Chen 2023 (Miniaturized MiCO)

- 출발세포: hPSCs 직접
- Floor plate patterning (day 0-9): SB 10 uM + LDN 100 nM + CHIR 0.6 uM + SAG 400 nM
- Day 9-11: FGF8b 100 ng/mL
- Day 11-16: FGF8b + LM22A4 2 uM + AA 200 uM
- Maturation (day 16+): LM22A4 + AA + GDNF 10 ng/mL + dcAMP 500 uM + DAPT 1 uM
- Matrix-free: AggreWell400 → EB-Disk360 (Matrigel 불필요)
- 300-750 cells/organoid → necrotic core 없음
- 적용: high-throughput compound screening

**공통 핵심**: SHH + WNT 활성화로 ventral midbrain (floor plate) identity 유도, dopaminergic neuron 농축

Related: [Zagare 2021 raw](../../raw/sources/zagare_2021_a_robust_protocol_for_the.pdf), [Chen 2023 raw](../../raw/sources/chen_2023_protocol_for_generating_reproducible_miniaturized.pdf)

---

## 6. Brainstem (뇌간)

**Eura 2020**

- 출발세포: hPSCs (iPSC/ESC)
- 핵심 전략: cortical organoid 프로토콜 변형 — SHH/WNT 미사용 (dorsal brainstem 조직)
- Day 0-3: mTeSR1 + ROCK inhibitor + dorsomorphin 1 mM + SB431542 10 uM
- Day 3-9: neurobasal + Gem21NeuroPlex + NEAA + GlutaMAX + dorsomorphin + SB431542 + transferrin 10 uM + insulin 5 mg/L + progesterone 0.063 mg/L
- Day 9-16: bFGF 20 ng/mL (NPC 증식)
- Day 16-22: bFGF 20 ng/mL + EGF 20 ng/mL
- Day 22-28: ascorbic acid + cAMP + BDNF + GDNF + NT-3 (성숙)
- Day 28+: growth factor 철회
- Orbital shaker 사용
- 산출 세포: midbrain/hindbrain progenitor (OTX2+), dopaminergic (TH+), cholinergic (ChAT+), noradrenergic (DBH+), melanocyte (neural crest), oligodendrocyte, astrocyte
- scRNA-seq: 10개 cell population, GTEx 비교 시 cerebellum/substantia nigra/hypothalamus 유사
- 독특한 점: melanocyte (neural crest 유래) 포함 — 다른 brain organoid에서 미보고
- 한계: region specificity 낮음 (brainstem 전반 혼재)

Related: [Eura 2020 raw](../../raw/sources/eura_2020_brainstem_organoids_from_human_pluripotent.pdf)

---

## 7. Hippocampus (해마)

**Pomeshchik 2020**

- 출발세포: human iPSCs
- 핵심 전략: Pasca EB 방법 기반, 2단계 patterning
  1. Dorsomedial telencephalic 유도 (day 0-10): dual SMAD (LDN + SB) + XAV-939 (WNT 억제) + cyclopamine (SHH 억제) → caudal/ventral fate 차단
  2. Hippocampal identity 전환 (day 10-100+): CHIR-99021 (WNT 활성화) + BDNF
- 핵심 논리: 먼저 dorsal telencephalon으로 제한 → WNT 활성화로 medial pallium (해마 원기) 유도
- 산출 세포: ZBTB20+ (90%), PROX1+ (45-60%) hippocampal neuron, TBR1+, calretinin+, calbindin+
- 검증: LEF1+ (medial pallium marker), mouse hippocampus 이식 후 생착 확인
- 적용: AD 모델링 (APP/PS1 variant → Ab42/40 ratio 증가, tau 인산화, synapse 손실 재현)

Related: [Pomeshchik 2020 raw](../../raw/sources/pomeshchik_2020_human_ipsc-derived_hippocampal_spheroids_an.pdf)

---

## 8. Hindbrain / Serotonin Neurons (후뇌)

**Valiulahi 2021**

- 출발세포: hPSCs
- 핵심 전략: ventral + caudal 동시 유도 (serotonin neuron은 ventral hindbrain 유래)
- 2D 프로토콜:
  - Day 0-7: KSR + SB431542 (SMAD inhibition)
  - Day 3+: purmorphamine (SHH agonist → ventral identity)
  - Day 5-13: retinoic acid 2 uM (caudalizing agent — 핵심 구별 인자)
  - Day 10+: LDN193189
  - Day 13+: NB/B27 + BDNF
- 3D organoid 버전: AggreWell EB → purmorphamine + RA (day 7부터) → Matrigel → agitation
- 산출: 30-40% 5-HT+ serotonin neuron (TPH2+/FEV+), caudal hindbrain identity (r5-r8)
- Regional marker: HOXA2, HOXA3, HOXB2, HOXB3, HOXB4
- Transcriptome: medulla oblongata, cerebellum과 높은 matching score
- 핵심 차이: midbrain 프로토콜과 유사한 ventral 유도이나, RA가 caudalizing agent로 추가되어 hindbrain fate 결정

Related: [Valiulahi 2021 raw](../../raw/sources/valiulahi_2021_generation_of_caudal-type_serotonin_neurons.pdf)

---

## 9. Cerebellum (소뇌)

**Atamian 2024**

- 출발세포: hPSCs (hES/hiPS)
- 핵심 전략: isthmic organizer (중뇌-후뇌 경계) 환경을 재현하는 3단계 프로토콜
- Stage 1 (day 0-16) — Isthmic organizer 확립:
  - gfCDM+i (growth factor-free chemically defined medium + insulin)
  - Dual SMAD: SB431542 + Noggin (기존 cerebellar 프로토콜은 SB만 사용)
  - CHIR-99021 (WNT → caudalization)
  - FGF8b (isthmic organizer 특이적 — 기존 FGF2 대체, 핵심 차별점)
  - CerDM1 배지 전환 (day 6)
- Stage 2 (day 16-30) — Progenitor 확장:
  - CerDM2 배지, 10 cm dish shaking/bioreactor
  - Ventricular zone (inhibitory) + rhombic lip (excitatory) progenitor 동시 생성
- Stage 3 (day 30-8개월) — 성숙:
  - CerDM3 (serum-free + lipids, heparin, B27, N2, BDNF, T3)
  - SDF1a + Matrigel → laminar layering 유도
- 산출 세포: Purkinje cell (SKOR2+/CALB1+/PCP2+), granule cell (PAX6+/BARHL1+/NEUROD1), VZ/RL progenitor
- 기능 검증: calcium imaging + patch clamp, optogenetic Purkinje cell modulation
- 기존 프로토콜 대비: 대부분 SB (single SMAD) + FGF2 사용 → 이 프로토콜은 dual SMAD (SB+Noggin) + CHIR + FGF8b

Related: [Atamian 2024 raw](../../raw/sources/atamian_2024_generation_and_long-term_culture_of.pdf)

---

## 핵심 비교 요약표

| Subregion | 핵심 Patterning 전략 | 주요 Morphogen | Caudalizing Agent | 대표 Cell Type |
|---|---|---|---|---|
| Whole cerebral | 비유도 (self-org) | 없음 | 없음 | 혼재 (cortex, hippocampus 등) |
| Dorsal forebrain | Dual SMAD | SB + LDN | 없음 | Glutamatergic cortical neuron |
| Ventral forebrain | SHH activation | SAG + IWP-2 | 없음 | GABAergic interneuron |
| Hippocampus | Dual SMAD → WNT on | LDN + SB → CHIR + BDNF | 없음 | ZBTB20+/PROX1+ hippocampal neuron |
| Midbrain | SHH + WNT | SAG/PMA + CHIR | FGF8b (일부) | TH+ dopaminergic neuron |
| Brainstem | Dual SMAD 변형 | Dorsomorphin + SB | 없음 | DA + cholinergic + noradrenergic + melanocyte |
| Hindbrain (5-HT) | SHH + RA | PMA + SB | Retinoic acid | 5-HT serotonin neuron |
| Cerebellum | Dual SMAD + WNT + FGF8 | SB + Noggin + CHIR + FGF8b | CHIR (WNT) | Purkinje + granule cell |

## 핵심 원리

1. **Anteroposterior axis**: WNT/CHIR (caudalization) → RA (더 강한 caudalization → hindbrain) → FGF8b (isthmic organizer → cerebellum)
2. **Dorsoventral axis**: SHH agonist (SAG/PMA/purmorphamine) → ventral; 미사용 시 → dorsal
3. **Forebrain default**: patterning 없으면 hPSC는 forebrain-like fate를 취함 → caudal region은 반드시 caudalizing signal 필요
4. **Region 순도 vs diversity**: unguided (Lancaster) → semi-guided (Fitzgerald) → fully guided (Sloan, midbrain, hindbrain, cerebellum) 순으로 순도 증가, diversity 감소

## Related syntheses

- [Organoid developmental baseline and regionalization playbook](../syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md)

## Sources used

- [Lancaster 2014](../sources/lancaster_2014_generation_of_cerebral_organoids_from.md)
- [Sloan 2018](../sources/sloan_2018_generation_and_assembly_of_human.md)
- [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Ullah 2025](../sources/ullah_2025_generating_and_characterizing_human_telencephalic.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- Eura 2020 (raw PDF — brainstem)
- Pomeshchik 2020 (raw PDF — hippocampus)
- Zagare 2021 (raw PDF — midbrain)
- Valiulahi 2021 (raw PDF — hindbrain/serotonin)
- Chen 2023 (raw PDF — miniaturized midbrain)
- Atamian 2024 (raw PDF — cerebellum)
