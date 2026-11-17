#!/usr/bin/env bash
# Build the release artifact: dist/calculator-<release-id>.tar.gz and its checksum.
# Usage: scripts/build_release.sh RELEASE_ID FULL_COMMIT_ID
set -euo pipefail

release_id="${1:?usage: build_release.sh RELEASE_ID FULL_COMMIT_ID}"
commit="${2:?usage: build_release.sh RELEASE_ID FULL_COMMIT_ID}"

root="$(cd "$(dirname "$0")/.." && pwd)"
stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT

mkdir -p "$root/dist"
cp "$root/calculator.py" "$stage/"
cp "$root/scripts/smoke_test.sh" "$stage/"
printf '%s\n' "$commit" > "$stage/VERSION"

archive="$root/dist/calculator-$release_id.tar.gz"
tar -czf "$archive" -C "$stage" VERSION calculator.py smoke_test.sh

cd "$root/dist"
if command -v sha256sum >/dev/null; then
  sha256sum "calculator-$release_id.tar.gz" > "calculator-$release_id.tar.gz.sha256"
else
  shasum -a 256 "calculator-$release_id.tar.gz" > "calculator-$release_id.tar.gz.sha256"
fi
echo "Built $archive"
