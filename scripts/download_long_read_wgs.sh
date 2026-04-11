#!/bin/zsh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
COLLECTION_DIR="${1:-$ROOT_DIR/collections/longread-sequencing}"
MANIFEST="$COLLECTION_DIR/long_read_wgs_manifest.tsv"
TARGET_DIR="$COLLECTION_DIR/raw/sources"

mkdir -p "$TARGET_DIR"

tail -n +2 "$MANIFEST" | while IFS=$'\t' read -r published_date year first_author title article_url pdf_url filename legacy_filename local_path source_page focus; do
  output_path="$TARGET_DIR/$filename"

  if [[ -f "$output_path" ]]; then
    echo "skip  $filename"
    continue
  fi

  echo "fetch $filename"
  curl -L --fail --retry 2 --retry-delay 2 \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36" \
    "$pdf_url" \
    -o "$output_path"

  if ! file "$output_path" | grep -q "PDF"; then
    echo "downloaded file is not a PDF: $filename" >&2
    exit 1
  fi
done

echo "done"
