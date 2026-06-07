#!/usr/bin/env bash
# Start mock_server, run contract_smoke.py, exit non-zero on contract violation.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

python3 mock_server.py &
SERVER_PID=$!

cleanup() {
  kill "$SERVER_PID" 2>/dev/null || true
  wait "$SERVER_PID" 2>/dev/null || true
}
trap cleanup EXIT

for _ in $(seq 1 30); do
  if python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/infer', data=b'{}')" 2>/dev/null; then
    break
  fi
  sleep 0.2
done

python3 contract_smoke.py
