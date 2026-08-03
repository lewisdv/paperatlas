# Assembloid Technology Platform — Deep-Ingest 요약 (9편)

- **작성일:** 2026-07-01
- **컬렉션:** `collections/Organoid/`  ·  **등록 위치:** `collections/Organoid/wiki/sources/<파일명>`
- **원천:** `~/Downloads/2_assembloid-technology-platform` (9편, 전부 **Pașca lab**)
- **담당자 = 제1저자(연구 주도자)** 기준. 교신/책임저자는 대부분 **Sergiu P. Pașca**(공동책임: Agoglia→Fraser, Li→Cui·Bao, Yang→Cui, Peters→Carette).
- Revah 2022는 기존에 이미 deep-ingest되어 있어 **중복(재-ingest 아님)**, 참고용으로 표에 포함.

| 담당자(제1저자) | 논문 제목 | llm-wiki 등록 파일명(페이지) | 핵심 포인트 | 추가 확인 필요 사항 |
|---|---|---|---|---|
| **Aaron Gordon** (2021, Nat Neurosci) | Long-term maturation of human cortical organoids matches key early postnatal transitions | `gordon_2021_longterm_maturation_human_cortical_organoids_postnatal_transitions.md` | hCS 장기배양에서 **fetal→postnatal 성숙 스위치(~250–300일)**; DNAm 후성시계 r=+0.76, 전사체 BrainSpan 전이, HDAC2→HDAC1/11·GRIN2B→GRIN2A 스위치(단백질·전기생리 확인); GECO 웹툴 | 활동의존 프로그램·비피질세포(GABA/microglia/OPC/혈관)는 **미재현 gap**; 성숙에 **매우 긴 배양기간** 필요(실용성) → 이식(Revah)이 대안 |
| **Rachel M. Agoglia** (2021, Nature) | Primate cell fusion disentangles gene regulatory divergence in neurodevelopment | `agoglia_2021_primate_cell_fusion_gene_regulatory_divergence_neurodevelopment.md` | 인간×침팬지 **4배체 융합(hybrid) cortical spheroid**로 cis/trans 조절 발산 분해(**~39% cis**); 선택된 human astrocyte 유전자 모듈, human-biased **SSTR2** 칼슘 표현형 | 4배체/융합 세포의 **인공산물 가능성**; parental pair 2쌍(제한적 유전배경); ASD와는 **간접적** 연결 |
| **Thomas L. Li** (2022, Biomaterials) | Stretchable mesh microelectronics for the biointegration and stimulation of human neural organoids | `li_2022_stretchable_mesh_microelectronics_biointegration_stimulation_neural_organoids.md` | **16채널 PEDOT:PSS/SEBS stretchable mesh**(5µm, 50% 변형까지 임피던스 불변), hCO에 **>3개월 biointegration** + 강도의존 자극 | 채널수 적어 **공간 커버리지 제한**; pH/신경전달물질 센싱은 **미실증**(제안만); 표준화·처리량은 별도 과제 |
| **Jimena Andersen** (2023, Nat Neurosci) | Single-cell transcriptomic landscape of the developing human spinal cord | `andersen_2023_singlecell_transcriptomic_landscape_developing_human_spinal_cord.md` | **GW17–18 인간 척수 1차 아틀라스**(112,554 cells + 34,884 nuclei; GW4–25 통합 950,215); DV/RC 교세포 패턴, OPC→MOL 궤적, 초기 운동뉴런 다양화 | **1차 조직 아틀라스**(오가노이드 자체 아님) → 오가노이드 fidelity 벤치마크는 별도 대조 필요; 표본 GW 창이 좁음 |
| **Xiao Yang** (2024, Nat Biotechnol) | Kirigami electronics for long-term electrophysiological recording of human neural organoids and assembloids | `yang_2024_kirigami_electronics_electrophysiological_recording_neural_organoids_assembloids.md` | **KiriE 32전극 self-folding 3D "basket" MEA**, 무손상 hCO·corticostriatal assembloid를 **수개월** 단일유닛/네트워크 기록; 22q11.2(DGCR8) 과흥분 검증 | 32전극/~1mm 코어만 커버(**device 2–4개/조건**); **network 동기화·E-I 분해 분석 미수행**; 제작 난이도 높음 |
| **Neal D. Amin** (2024, Cell Stem Cell) | Generating human neural diversity with a multiplexed morphogen screen in organoids | `amin_2024_generating_human_neural_diversity_multiplexed_morphogen_screen_organoids.md` | **14-morphogen/46-조건 arrayed 스크린**(~1,500 오가노이드, 36,265 세포 → 1차 태아 CNS 클러스터 **65% 매핑**); morphogen 조합·타이밍 → 지정 regional fate; 신규 소뇌/선조 IN 오가노이드 | 조합·타이밍 커버리지의 **완전성**; 일부 fate의 성숙도·재현성; **ASD 적용은 후속 과제** |
| **Christine E. Peters** (2025, bioRxiv) | Human Assembloid Model of Emergent Neurotropic Enteroviruses | `peters_2025_human_assembloid_model_emergent_neurotropic_enteroviruses.md` | **hSpO–hSkM 척수-근육 assembloid**로 3종 엔테로바이러스(PV/EV-A71/EV-D68) 모델링; 전부 수축 소실→**rupintrivir 구제**; tropism 발산(MN vs astroglia) | **preprint(비심사)** → 정량치 provisional; 기전(astroglia→비세포자율 뉴런사) **상관적**; 항바이러스제 1종만; ASD와 **tangential** |
| **Genta Narazaki** (2025, Nat Biomed Eng) | Scalable production of human cortical organoids using a biocompatible polymer | `narazaki_2025_scalable_production_human_cortical_organoids_biocompatible_polymer.md` | **xanthan gum** 항융합 첨가제로 **>2,000 오가노이드 병렬**(298약물/2,400 스크린), 패턴·전사체(**R²=0.986**)·형태·칼슘활동 **불변** | 장기(>수개월) 안정성·**타 프로토콜 일반화**; 자동화·비용 정량은 별도 검증 |
| **Omer Revah** (2022, Nature) *(기존/중복)* | Maturation and circuit integration of transplanted human cortical organoids | `revah_2022_maturation_circuit_integration_transplanted_human_cortical_organoids.md` | hCO를 **신생쥐 S1 이식** → in-vivo 성숙·회로통합(시상피질 입력·감각반응·보상행동); **Timothy(CACNA1C) 표현형 in-vivo서만** 발현 | **이미 위키 등록됨**(이번 재-ingest 아님, {36224417}); lamination 없음·GABA 결여; 종간(rat) 이식 한계 |

---

### 공통 확인 사항
- 정량 수치는 대부분 **단일 논문(단일 스터디) 값** — 재현·교차검증 전 "illustrative"로 취급.
- 8편 신규는 저자 제공 PDF 전문(pdftotext) 기반 deep-ingest, `raw/sources/`에 사본 보관(원본 Downloads 유지).
- 교차링크 broken 0 (병렬 ingest 레이스로 생긴 pending 링크 4건: Li↔Yang, Peters→Andersen, Amin→Andersen 정리 완료).
- 카탈로그: `collections/Organoid/wiki/index.md`(신규 섹션) + `wiki/log.md`(배치 기록) 갱신.
