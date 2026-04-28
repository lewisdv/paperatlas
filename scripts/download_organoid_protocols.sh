#!/bin/zsh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
COLLECTION_DIR="${1:-$ROOT_DIR/collections/Organoid}"
MANIFEST="$COLLECTION_DIR/organoid_protocols_manifest.tsv"
TARGET_DIR="$COLLECTION_DIR/raw/sources"
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"

mkdir -p "$TARGET_DIR"

download_pdf() {
  local url="$1"
  local output_path="$2"

  curl -L --fail --retry 2 --retry-delay 2 \
    -A "$USER_AGENT" \
    "$url" \
    -o "$output_path"
}

download_pmc_pdf() {
  local url="$1"
  local output_path="$2"
  local challenge_path
  local challenge
  local difficulty
  local cookie_name
  local cookie_value

  challenge_path="$(mktemp)"
  download_pdf "$url" "$challenge_path"

  if file "$challenge_path" | grep -q "PDF"; then
    mv "$challenge_path" "$output_path"
    return
  fi

  challenge="$(sed -n 's/.*POW_CHALLENGE = "\([^"]*\)".*/\1/p' "$challenge_path")"
  difficulty="$(sed -n 's/.*POW_DIFFICULTY = "\([^"]*\)".*/\1/p' "$challenge_path")"
  cookie_name="$(sed -n 's/.*POW_COOKIE_NAME = "\([^"]*\)".*/\1/p' "$challenge_path")"
  rm -f "$challenge_path"

  if [[ -z "$challenge" || -z "$difficulty" || -z "$cookie_name" ]]; then
    echo "downloaded PMC response is not a PDF or proof-of-work challenge: $url" >&2
    exit 1
  fi

  cookie_value="$(python3 -c 'import hashlib, sys
challenge = sys.argv[1]
difficulty = int(sys.argv[2])
prefix = "0" * difficulty
nonce = 0
while True:
    digest = hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest()
    if digest.startswith(prefix):
        print(f"{challenge},{nonce}")
        break
    nonce += 1
' "$challenge" "$difficulty")"

  curl -L --fail --retry 2 --retry-delay 2 \
    -A "$USER_AGENT" \
    --cookie "${cookie_name}=${cookie_value}" \
    "$url" \
    -o "$output_path"
}

tail -n +2 "$MANIFEST" | while IFS=$'\t' read -r published_date year first_author organ title article_url pdf_url filename local_path source_page focus; do
  output_path="$TARGET_DIR/$filename"

  if [[ -f "$output_path" ]]; then
    echo "skip  $filename"
    continue
  fi

  echo "fetch $filename"
  if [[ "$pdf_url" == https://pmc.ncbi.nlm.nih.gov/*.pdf* ]]; then
    download_pmc_pdf "$pdf_url" "$output_path"
  else
    download_pdf "$pdf_url" "$output_path"
  fi

  if ! file "$output_path" | grep -q "PDF"; then
    echo "downloaded file is not a PDF: $filename" >&2
    exit 1
  fi
done

echo "done"
