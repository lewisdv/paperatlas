---
title: Zhang 2026 ProteinAligner tri-modal contrastive PLM
kind: paper
status: pending_pdf
added: 2026-05-15T14:06:27+09:00
doi: 10.1016/j.crmeth.2026.101407
notion_url: https://www.notion.so/347302d9c598811d82a5f8446fb8bf92
notion_hub: 한미암 / 표적항암치료제 멀티오믹스 (폐암 후향적 코호트)
pdf_status: not_found
---

# Zhang 2026 ProteinAligner tri-modal contrastive PLM

## Source

- File: _PDF not yet downloaded (not_found)_
- DOI: [10.1016/j.crmeth.2026.101407](https://doi.org/10.1016/j.crmeth.2026.101407)
- Notion: [Zhang 2026 — ProteinAligner: 시퀀스+구조+텍스트 tri-modal contrastive PLM](https://www.notion.so/347302d9c598811d82a5f8446fb8bf92)
- Hub: 한미암 / 표적항암치료제 멀티오믹스 (폐암 후향적 코호트)
- Added: 2026-05-15T14:06:27+09:00

## Notion Summary

**한 줄 요약:** ProteinAligner는 아미노산 시퀀스, 3D 구조, 논문/기능 텍스트를 sequence-anchored contrastive learning으로 정렬한 867M 파라미터 단백질 파운데이션 모델. 6개 다운스트림 태스크에서 ESM-2/ESM-3(1.4B)/ProtST/ESM-S/ProTrek 능가.

**과제 관련성:**

pathogenic missense variant 예측 F1 0.72 (ESM-3 1.4B: 0.47)로 암 유전자 missense 변이 기능 평가 직접 활용. bioactive peptide 발굴 7개 태스크 중 6개 ESM-3 초과 — peptide drug 스크리닝. thermostability 치료용 단백질 engineering. 표적항암치료제 멀티오믹스에서 단백질 수준 기능 예측에 활용.

**주요 결과:**

- Pathogenic missense F1 0.72 (ESM-3 0.47).
- Thermostability F1 0.608 / Acc 0.577.
- Bioactive peptides 7 tasks 중 6/7 ESM-3 초과, 5/7 ProTrek 초과.
- AMP MIC MSE 0.449 (ESM-3 1.1).
- Tri-modal: ESM-2 650M(sequence) + ESM-IF1 GVP-GNN 124M(structure) + 78M text.
- Sequence-anchored contrastive로 모달 누락 robust.

## Summary

Pending ingest.

## Key Claims

- Pending ingest.

## Open Questions

- Pending ingest.
