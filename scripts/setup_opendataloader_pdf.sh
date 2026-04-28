#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv-opendataloader"
WITH_HYBRID=0

for arg in "$@"; do
  case "$arg" in
    --with-hybrid)
      WITH_HYBRID=1
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 1
      ;;
  esac
done

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required but was not found on PATH." >&2
  exit 1
fi

if ! brew list python@3.11 >/dev/null 2>&1; then
  echo "Installing python@3.11 with Homebrew..."
  brew install python@3.11
fi

if ! brew list openjdk@21 >/dev/null 2>&1; then
  echo "Installing openjdk@21 with Homebrew..."
  brew install openjdk@21
fi

PYTHON_BIN="$(brew --prefix python@3.11)/bin/python3.11"
OPENJDK_PREFIX="$(brew --prefix openjdk@21)"
JAVA_HOME_DIR="$OPENJDK_PREFIX/libexec/openjdk.jdk/Contents/Home"
export JAVA_HOME="$JAVA_HOME_DIR"
export PATH="$OPENJDK_PREFIX/bin:$PATH"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "Creating virtual environment at $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

export PATH="$VENV_DIR/bin:$PATH"

echo "Upgrading pip tooling..."
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel

if [[ "$WITH_HYBRID" -eq 1 ]]; then
  echo "Installing opendataloader-pdf with hybrid extras..."
  "$VENV_DIR/bin/python" -m pip install -U "opendataloader-pdf[hybrid]"
else
  echo "Installing opendataloader-pdf..."
  "$VENV_DIR/bin/python" -m pip install -U opendataloader-pdf
fi

echo ""
echo "OpenDataLoader PDF setup complete."
echo "Venv: $VENV_DIR"
echo "CLI: $VENV_DIR/bin/opendataloader-pdf"
echo "JAVA_HOME: $JAVA_HOME"
echo ""
echo "Examples:"
echo "  python3 scripts/wiki.py --collection Organoid parse-source collections/Organoid/raw/sources/eura_2020_brainstem_organoids_from_human_pluripotent.pdf --parse-format json,markdown"
echo "  python3 scripts/wiki.py --collection Organoid add-source /absolute/path/to/paper.pdf --title \"Paper Title\" --parse-with-opendataloader"
