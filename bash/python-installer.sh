#!/usr/bin/env bash
# macOS auto-installer for chf_optimizer
# Uses Homebrew Python 3.12/3.11 automatically

set -euo pipefail

ZIP_PATH="${1:-/tmp/chf_optimizer.zip}"
INSTALL_PREFIX="${2:-$HOME/chf_optimizer}"
RUN_AFTER="${RUN_AFTER:-false}"

# Must be initialized for "set -u"
PYTHON_BIN=""

msg() { echo -e "\033[1;32m[INFO]\033[0m $*"; }
warn() { echo -e "\033[1;33m[WARN]\033[0m $*"; }
err()  { echo -e "\033[1;31m[ERROR]\033[0m $*" >&2; exit 1; }

# -------------------------------------------------------
# Ensure Homebrew exists
# -------------------------------------------------------
ensure_homebrew() {
  if ! command -v brew &>/dev/null; then
    warn "Homebrew not found. Installing Homebrew…"
    /bin/bash -c \
      "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi

  eval "$(/opt/homebrew/bin/brew shellenv)"
}

# -------------------------------------------------------
# Detect brew Python, or install python@3.12 automatically
# -------------------------------------------------------
detect_python() {
  local py312="/opt/homebrew/opt/python@3.12/bin/python3.12"
  local py311="/opt/homebrew/opt/python@3.11/bin/python3.11"

  if [[ -x "$py312" ]]; then
    PYTHON_BIN="$py312"
    msg "Using Python 3.12 ($PYTHON_BIN)"
    return
  fi

  if [[ -x "$py311" ]]; then
    PYTHON_BIN="$py311"
    msg "Using Python 3.11 ($PYTHON_BIN)"
    return
  fi

  warn "No suitable Python found. Installing python@3.12…"
  brew install python@3.12

  if [[ ! -x "$py312" ]]; then
    err "python@3.12 did not install correctly."
  fi

  PYTHON_BIN="$py312"
  msg "Python installed: $PYTHON_BIN"
}

# -------------------------------------------------------
# Prepare venv and upgrade pip
# -------------------------------------------------------
prepare_environment() {
  msg "Preparing install directory $INSTALL_PREFIX"
  rm -rf "$INSTALL_PREFIX"
  mkdir -p "$INSTALL_PREFIX"

  msg "Creating virtual environment..."
  "$PYTHON_BIN" -m venv "$INSTALL_PREFIX/.venv"

  msg "Activating venv and upgrading pip tools..."
  source "$INSTALL_PREFIX/.venv/bin/activate"
  pip install --upgrade pip setuptools wheel
}

# -------------------------------------------------------
# Extract Zip + Install dependencies
# -------------------------------------------------------
install_project() {
  msg "Extracting ZIP to $INSTALL_PREFIX"
  unzip -o "$ZIP_PATH" -d "$INSTALL_PREFIX"

  cd "$INSTALL_PREFIX/chf_optimizer" || \
    err "chf_optimizer directory not found."

  msg "Installing databento..."
  pip install databento

  msg "Installing remaining Python packages..."
  pip install numpy pandas toml requests
}

# -------------------------------------------------------
# Optional auto-run
# -------------------------------------------------------
run_optimizer() {
  msg "Running optimizer.py…"
  source "$INSTALL_PREFIX/.venv/bin/activate"
  cd "$INSTALL_PREFIX/chf_optimizer"
  python optimizer.py
}

# -------------------------------------------------------
# Main workflow
# -------------------------------------------------------
main() {
  msg "Starting macOS CHF optimizer installation…"

  ensure_homebrew
  detect_python       # MUST run before using $PYTHON_BIN
  prepare_environment
  install_project

  msg "Setup complete!"
  echo
  echo "To run manually:"
  echo "  cd \"$INSTALL_PREFIX/chf_optimizer\""
  echo "  source \"$INSTALL_PREFIX/.venv/bin/activate\""
  echo "  python optimizer.py"
  echo

  if [[ "$RUN_AFTER" == "true" ]]; then
    run_optimizer
  fi
}

main "$@"

