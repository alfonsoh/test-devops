#!/usr/bin/env bash
# setup_chf_optimizer.sh
# Cross-platform setup for macOS (Homebrew) and Ubuntu/Debian (apt)

set -euo pipefail

# -------------------------
# Config / Defaults
# -------------------------
ZIP_PATH="${1:-/tmp/chf_optimizer.zip}"         # path to the project zip
INSTALL_PREFIX="${2:-$HOME/chf_optimizer}"      # install location
RUN_AFTER="${RUN_AFTER:-false}"                  # set RUN_AFTER=true to run optimizer.py after setup
PY_PKGS="numpy pandas databento toml requests"

# -------------------------
# Helpers
# -------------------------
need_cmd() { command -v "$1" >/dev/null 2>&1; }
die() { echo "Error: $*" >&2; exit 1; }
msg() { printf "\n\033[1m%s\033[0m\n" "$*"; }

# -------------------------
# Pre-flight checks
# -------------------------
[ -f "$ZIP_PATH" ] || die "Zip file not found at: $ZIP_PATH"

OS="$(uname -s)"
case "$OS" in
  Darwin)   PLATFORM="macos" ;;
  Linux)    PLATFORM="linux" ;;
  *)        die "Unsupported OS: $OS" ;;
esac

# -------------------------
# macOS setup (Homebrew)
# -------------------------
install_macos_deps() {
  msg "Detected macOS"

  # Ensure Xcode Command Line Tools (for compilers, headers, etc.)
  if ! xcode-select -p >/dev/null 2>&1; then
    msg "Installing Xcode Command Line Tools… (this may prompt a GUI installer)"
    xcode-select --install || true
    echo "If a popup appeared, complete that installation, then re-run this script if it fails here."
  fi

  # Ensure Homebrew
  if ! need_cmd brew; then
    msg "Homebrew not found. Installing Homebrew…"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # add brew to PATH for current session if needed
    if [[ -d "/opt/homebrew/bin" ]]; then
      eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [[ -d "/usr/local/bin" ]]; then
      export PATH="/usr/local/bin:$PATH"
    fi
  else
    msg "Updating Homebrew…"
    brew update
  fi

  # Install packages. macOS has unzip and curl preinstalled, but brew ensures consistency.
  BREW_PKGS=(python wget unzip)
  msg "Installing packages with Homebrew: ${BREW_PKGS[*]}"
  brew install "${BREW_PKGS[@]}" || true

  # Prefer Homebrew Python if available
  if need_cmd python3; then
    PYTHON_BIN="$(command -v python3)"
  else
    die "python3 not found even after brew install."
  fi
}

# -------------------------
# Ubuntu/Debian setup (apt)
# -------------------------
install_linux_deps() {
  msg "Detected Linux (assuming Ubuntu/Debian)"
  if ! need_cmd apt-get; then
    die "apt-get not found. This script expects Ubuntu/Debian for Linux. For other distros, install:
      - build tools (e.g. base-devel / @development-tools)
      - python3, python3-venv, python3-pip, python3-dev
      - curl, wget, unzip"
  fi

  if [ "$EUID" -ne 0 ] && ! need_cmd sudo; then
    die "sudo not found. Run as root or install sudo."
  fi
  SUDO="$( [ "$EUID" -eq 0 ] && echo "" || echo "sudo" )"

  $SUDO apt-get update -y
  $SUDO apt-get install -y \
    software-properties-common \
    curl \
    wget \
    build-essential \
    python3 \
    python3-venv \
    python3-pip \
    python3-dev \
    unzip

  if need_cmd python3; then
    PYTHON_BIN="$(command -v python3)"
  else
    die "python3 not found after apt install."
  fi
}

# -------------------------
# Install system deps
# -------------------------
PYTHON_BIN=""
case "$PLATFORM" in
  macos) install_macos_deps ;;
  linux) install_linux_deps ;;
esac

# -------------------------
# Create project dir & venv
# -------------------------
msg "Creating project directory at: $INSTALL_PREFIX"
mkdir -p "$INSTALL_PREFIX"
cd "$INSTALL_PREFIX"

if [ ! -d ".venv" ]; then
  msg "Creating virtual environment in .venv"
  "$PYTHON_BIN" -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

# -------------------------
# Python packages
# -------------------------
msg "Upgrading pip and installing Python dependencies"
python -m pip install --upgrade pip
python -m pip install $PY_PKGS

# -------------------------
# Unzip project
# -------------------------
msg "Unzipping project from: $ZIP_PATH"
TMP_EXTRACT="$(mktemp -d)"
unzip -q "$ZIP_PATH" -d "$TMP_EXTRACT"

# If the archive contains a top-level chf_optimizer dir, use it; otherwise gather all into one.
if [ -d "$TMP_EXTRACT/chf_optimizer" ]; then
  mkdir -p "$INSTALL_PREFIX/chf_optimizer"
  rsync -a "$TMP_EXTRACT/chf_optimizer/" "$INSTALL_PREFIX/chf_optimizer/"
else
  mkdir -p "$INSTALL_PREFIX/chf_optimizer"
  rsync -a "$TMP_EXTRACT/" "$INSTALL_PREFIX/chf_optimizer/"
fi
rm -rf "$TMP_EXTRACT"

# -------------------------
# Done + optional run
# -------------------------
cd "$INSTALL_PREFIX/chf_optimizer"

cat <<EOF

✅ Setup complete!

To run the optimizer:
  cd "$INSTALL_PREFIX/chf_optimizer"
  source "$INSTALL_PREFIX/.venv/bin/activate"
  python optimizer.py

Tip: To auto-run at the end, set:
  RUN_AFTER=true ./setup_chf_optimizer.sh "$ZIP_PATH" "$INSTALL_PREFIX"

EOF

if [ "$RUN_AFTER" = "true" ]; then
  msg "RUN_AFTER=true — launching optimizer.py…"
  python optimizer.py
fi
