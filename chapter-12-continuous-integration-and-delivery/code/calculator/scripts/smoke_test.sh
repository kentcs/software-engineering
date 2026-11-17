#!/usr/bin/env bash
# Run the calculator from an unpacked release and check one known answer.
# Usage: smoke_test.sh RELEASE_DIRECTORY
set -euo pipefail

dir="${1:?usage: smoke_test.sh RELEASE_DIRECTORY}"
expected="5.0"
actual="$(python3 "$dir/calculator.py" 2 3)"

if [ "$actual" != "$expected" ]; then
  echo "Smoke test failed in $dir: 2 + 3 gave '$actual', expected '$expected'" >&2
  exit 1
fi
echo "Smoke test passed in $dir (version $(cat "$dir/VERSION"))"
