# Minimal example: mock API round-trip

Demonstrates the **HTTP + JSON contract** documented in [`../../docs/inference-contract.md`](../../docs/inference-contract.md).

## Run

**Terminal A — server**

```bash
python3 mock_server.py
```

**Terminal B — client (stdlib only)**

```bash
python3 run_client.py
```

Expected: printed JSON containing `result` with `decision`, `code`, and `msg`.

## CI contract smoke

Same checks as [GitHub Actions](../../.github/workflows/contract-smoke.yml) — no second terminal:

```bash
bash ci_smoke.sh
```

Or run the validator alone while the server is already up:

```bash
python3 contract_smoke.py
```

`contract_smoke.py` exits **0** when required fields match [`inference-contract.md`](../../docs/inference-contract.md); **1** otherwise. It does **not** assert exact `msg` wording.

See [Gating merges on the inference contract (article)](../../docs/articles/2026-06-13-gating-merges-on-inference-contract-ci.md).

## Optional: auth + custom URL

```bash
export MOCK_INFER_API_KEY=dev-secret
# Terminal A: restart server after setting env
python3 mock_server.py

# Terminal B:
export MOCK_INFER_API_KEY=dev-secret
python3 run_client.py
```

```bash
export MOCK_INFER_URL=http://127.0.0.1:8080/infer
python3 run_client.py
```

## Troubleshooting

| Symptom | Check |
|---------|--------|
| `Connection failed` | Server not running, or wrong port |
| HTTP 401 | Set `MOCK_INFER_API_KEY` on **both** processes, same value |
| HTTP 404 | Client URL path must be `/infer` |
