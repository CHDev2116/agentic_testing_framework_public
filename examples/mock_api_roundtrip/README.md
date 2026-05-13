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
