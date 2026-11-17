#!/usr/bin/env bash
# Check the deployment settings before anything touches the server.
# Reports names and problems only; it never prints a secret value.
set -uo pipefail

problems=0
fail() { echo "CONFIG ERROR: $1" >&2; problems=$((problems + 1)); }

for name in DEPLOY_HOST DEPLOY_USER DEPLOY_PATH DEPLOY_SSH_KEY DEPLOY_KNOWN_HOSTS; do
  if [ -z "${!name:-}" ]; then
    fail "$name is not set"
  fi
done

host="${DEPLOY_HOST:-}"
user="${DEPLOY_USER:-}"
path="${DEPLOY_PATH:-}"

if [ -n "$host" ] && ! [[ "$host" =~ ^[A-Za-z0-9.-]+$ ]]; then
  fail "DEPLOY_HOST should be a host name or address with no user or port"
fi
if [ "$user" = "root" ]; then
  fail "DEPLOY_USER is root; use an account that can write only the deployment directory"
fi
if [ -n "$path" ]; then
  case "$path" in
    /|/root|/home|/usr|/etc|/var) fail "DEPLOY_PATH points at a system directory" ;;
    /*) ;;
    *) fail "DEPLOY_PATH must be an absolute path" ;;
  esac
fi
if [ -n "${DEPLOY_SSH_KEY:-}" ] && ! printf '%s' "$DEPLOY_SSH_KEY" | grep -q 'BEGIN .*PRIVATE KEY'; then
  fail "DEPLOY_SSH_KEY does not look like a private key"
fi
if [ -n "${DEPLOY_KNOWN_HOSTS:-}" ] && [ -n "$host" ] \
   && ! printf '%s' "$DEPLOY_KNOWN_HOSTS" | grep -qF "$host"; then
  fail "DEPLOY_KNOWN_HOSTS has no entry for $host"
fi

if [ "$problems" -gt 0 ]; then
  echo "Deployment stopped: $problems configuration problem(s)." >&2
  exit 1
fi
echo "Deployment configuration looks complete for $user@$host:$path"
