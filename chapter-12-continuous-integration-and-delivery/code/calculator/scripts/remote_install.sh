#!/usr/bin/env bash
# Runs on the server. Unpack an uploaded release, check it, and make it current.
# Usage: remote_install.sh BASE_DIRECTORY RELEASE_ID [install|activate]
#   install   unpack BASE/incoming/calculator-ID.tar.gz, smoke-test, switch "current"
#   activate  switch "current" to a release already in BASE/releases (recovery)
set -euo pipefail

base="${1:?usage: remote_install.sh BASE_DIRECTORY RELEASE_ID [install|activate]}"
id="${2:?usage: remote_install.sh BASE_DIRECTORY RELEASE_ID [install|activate]}"
mode="${3:-install}"
keep=5

releases="$base/releases"
mkdir -p "$releases" "$base/incoming"

sha_check() {
  if command -v sha256sum >/dev/null; then sha256sum -c "$1"; else shasum -a 256 -c "$1"; fi
}

activate() {
  local target="$releases/$1"
  [ -d "$target" ] || { echo "No such release: $1" >&2; exit 1; }
  if [ -L "$base/current" ]; then
    basename "$(readlink "$base/current")" > "$base/previous"
  fi
  ln -sfn "$target" "$base/current"
  echo "current -> $1"
}

case "$mode" in
  install)
    archive="$base/incoming/calculator-$id.tar.gz"
    (cd "$base/incoming" && sha_check "calculator-$id.tar.gz.sha256")
    staging="$releases/.staging-$id"
    rm -rf "$staging"
    mkdir -p "$staging"
    tar -xzf "$archive" -C "$staging"
    "$staging/smoke_test.sh" "$staging"
    rm -rf "$releases/$id"
    mv "$staging" "$releases/$id"
    activate "$id"
    "$base/current/smoke_test.sh" "$base/current"
    # Keep the newest releases so a recent one is still there to go back to.
    ls -1t "$releases" | tail -n +$((keep + 1)) | while read -r old; do
      [ "$old" = "$id" ] || rm -rf "${releases:?}/$old"
    done
    ;;
  activate)
    activate "$id"
    "$base/current/smoke_test.sh" "$base/current"
    ;;
  *)
    echo "Unknown mode: $mode" >&2
    exit 2
    ;;
esac
