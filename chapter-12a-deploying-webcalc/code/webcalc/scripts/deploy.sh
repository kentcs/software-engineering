#!/usr/bin/env bash
# Run on webcalc.kentcs.org as webcalc.
set -euo pipefail
cd /home/webcalc
command -v screen >/dev/null
command -v curl >/dev/null
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt

# Stop only the named app session; the first deployment has none.
screen -S webcalc -X quit 2>/dev/null || true
for attempt in {1..20}; do
    if ! curl -fsS --max-time 1 http://127.0.0.1:8080/ >/dev/null 2>&1; then break; fi
    sleep 1
done
if curl -fsS --max-time 1 http://127.0.0.1:8080/ >/dev/null 2>&1; then
    echo 'Port 8080 is still serving an app; refusing to start another.' >&2
    exit 1
fi
screen -dmS webcalc bash -c 'exec .venv/bin/python main.py >> /home/webcalc/webcalc.log 2>&1'
for attempt in {1..30}; do
    if curl -fsS --max-time 2 http://127.0.0.1:8080/ >/dev/null; then
        echo 'WebCalc is running in Screen on port 8080.'
        exit 0
    fi
    sleep 1
done
echo 'WebCalc did not start. See /home/webcalc/webcalc.log' >&2
exit 1
