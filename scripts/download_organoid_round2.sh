#!/usr/bin/env bash
# Round 2: Fill corpus gaps — retina, spinal cord, vascular, pancreas, inner ear, brain benchmarking
set -euo pipefail

RAW_DIR="$(cd "$(dirname "$0")/../collections/Organoid/raw/sources" && pwd)"
cd "$RAW_DIR"

echo "=== Round 2 organoid paper collection ==="

# --- RETINAL ORGANOIDS ---
# Cowan et al 2020 — PNAS, highly reproducible retinal organoid protocol
echo "[1/13] Cowan 2020 — retinal organoid (PNAS)"
curl -sL -o "cowan_2020_a_highly_reproducible_and_efficient.pdf" \
  "https://www.pnas.org/doi/pdf/10.1073/pnas.2317285121" 2>/dev/null || echo "  SKIP (need manual download)"

# Zhong et al 2014 / Capowski et al 2019 — Stem Cell Reports, retinal organoid protocol
echo "[2/13] capowski_2019 — reproducibility of retinal organoid (Stem Cell Reports)"
curl -sL -o "capowski_2019_reproducibility_and_staging_of.pdf" \
  "https://www.cell.com/action/showPdf?pii=S2213-6711(18)30468-1" 2>/dev/null || echo "  SKIP (need manual download)"

# --- SPINAL CORD / MOTOR NEURON ---
# Andersen et al 2020 — Cell Stem Cell, cortico-motor assembloid
echo "[3/13] andersen_2020 — cortico-motor assembloid generation"
curl -sL -o "andersen_2020_generation_of_functional_human.pdf" \
  "https://www.cell.com/action/showPdf?pii=S1934-5909(19)30437-8" 2>/dev/null || echo "  SKIP (need manual download)"

# Faustino Martins et al 2020 — Cell Stem Cell, neuromuscular organoid
echo "[4/13] faustino_martins_2020 — self-organizing sensorimotor organoid"
curl -sL -o "faustino_martins_2020_self-organizing_3d_human_trunk.pdf" \
  "https://www.cell.com/action/showPdf?pii=S1934-5909(19)30449-4" 2>/dev/null || echo "  SKIP (need manual download)"

# Pereira et al 2021 — Nat Comms, human sensorimotor organoids
echo "[5/13] pereira_2021 — human sensorimotor organoids NMJ"
curl -sL -o "pereira_2021_human_sensorimotor_organoids_derived.pdf" \
  "https://www.nature.com/articles/s41467-021-24776-4.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# --- BLOOD VESSEL / VASCULARIZED ---
# Wimmer et al 2019 — Nature Protocols, blood vessel organoid
echo "[6/13] wimmer_2019 — blood vessel organoid (Nat Protoc)"
curl -sL -o "wimmer_2019_generation_of_blood_vessel_organoids.pdf" \
  "https://www.nature.com/articles/s41596-019-0213-z.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# --- PANCREATIC ISLET ---
# Hogrebe et al 2021 — Nature Protocols, SC-beta cells
echo "[7/13] hogrebe_2021 — insulin-producing beta cells (Nat Protoc)"
curl -sL -o "hogrebe_2021_generation_of_insulin-producing_pancreatic.pdf" \
  "https://www.nature.com/articles/s41596-021-00560-y.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# --- INNER EAR ---
# Koehler et al 2017 — Nature Biotech, inner ear organoid
echo "[8/13] koehler_2017 — inner ear organoid hair cells (Nat Biotech)"
curl -sL -o "koehler_2017_generation_of_inner_ear_organoids.pdf" \
  "https://www.nature.com/articles/nbt.3840.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# van der Valk et al 2025 — Nature Protocols, vestibular inner ear organoid
echo "[9/13] vandervalk_2025 — vestibular inner ear organoid (Nat Protoc)"
curl -sL -o "vandervalk_2025_generation_and_characterization_of_vestibular.pdf" \
  "https://www.nature.com/articles/s41596-025-01191-3.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# --- BRAIN BENCHMARKING / REPRODUCIBILITY ---
# Velasco et al 2019 — Nature, brain organoid reproducibility
echo "[10/13] velasco_2019 — brain organoid reproducibility (Nature)"
curl -sL -o "velasco_2019_individual_brain_organoids_reproducibly.pdf" \
  "https://www.nature.com/articles/s41586-019-1289-x.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# He et al 2024 — Nature, integrated neural organoid cell atlas
echo "[11/13] he_2024 — integrated neural organoid cell atlas (Nature)"
curl -sL -o "he_2024_an_integrated_transcriptomic_cell_atlas.pdf" \
  "https://www.nature.com/articles/s41586-024-08172-8.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

# Tanaka et al 2020 — Cell Reports, synthetic analyses brain organoids fetal brain
echo "[12/13] tanaka_2020 — synthetic analyses brain organoids fetal brain"
curl -sL -o "tanaka_2020_synthetic_analyses_of_single-cell.pdf" \
  "https://www.cell.com/action/showPdf?pii=S2211-1247(20)30053-X" 2>/dev/null || echo "  SKIP (need manual download)"

# Kanton et al 2019 — Nature, organoid scRNA-seq human-specific features
echo "[13/13] kanton_2019 — organoid scRNA-seq human-specific features (Nature)"
curl -sL -o "kanton_2019_organoid_single-cell_genomic_atlas.pdf" \
  "https://www.nature.com/articles/s41586-019-1654-9.pdf" 2>/dev/null || echo "  SKIP (need manual download)"

echo ""
echo "=== Download complete. Checking file sizes ==="
for f in cowan_2020*.pdf capowski_2019*.pdf andersen_2020*.pdf faustino_martins_2020*.pdf \
         pereira_2021*.pdf wimmer_2019*.pdf hogrebe_2021*.pdf koehler_2017*.pdf \
         vandervalk_2025*.pdf velasco_2019*.pdf he_2024*.pdf tanaka_2020*.pdf kanton_2019*.pdf; do
  if [ -f "$f" ]; then
    sz=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
    if [ "$sz" -lt 50000 ]; then
      echo "  WARNING: $f is only ${sz} bytes — likely blocked, needs manual download"
    else
      echo "  OK: $f ($(( sz / 1024 )) KB)"
    fi
  else
    echo "  MISSING: $f"
  fi
done
