# Integrator guide (minimal public slice)

This guide matches the **smallest** integration surface published in this repo. It is enough to validate your HTTP stack, JSON contract, and local tooling before wiring a larger batch pipeline.

## Goal

Run a **mock inference HTTP service** and a **stdlib-only client** that POSTs the same JSON shape a `mock_api`-style backend consumes in the full Agentic Testing Framework.

## Prerequisite

- Python 3.9+

## Steps

1. Clone this repository.
2. Open a terminal in `examples/mock_api_roundtrip/`.
3. Start the server:

   ```bash
   python3 mock_server.py
   ```

4. In a second terminal, run the client:

   ```bash
   python3 run_client.py
   ```

You should see HTTP 200 and a JSON body whose `result` (or top-level) includes `decision`, `code`, and `msg`.

## Payload shape (request)

The mock server expects POST JSON with:

- `photo_path` (string)
- `metrics` (object)
- `thresholds` (object)

## Response shape

Either:

- `{ "result": { "decision": "...", "code": "...", "msg": "..." } }`, or  
- a bare `{ "decision": "...", "code": "...", "msg": "..." }`.

See [`inference-contract.md`](inference-contract.md) for valid `decision` labels used in the full framework.

## Optional auth (same convention as the full framework)

If the environment variable `MOCK_INFER_API_KEY` is set, the server requires:

`Authorization: Bearer <same value>`

`run_client.py` reads the same variable and sends the header when present.

## Next

- Read [`inference-contract.md`](inference-contract.md).  
- See [`README.md`](README.md) for the article index and links to the [full framework](https://github.com/CHDev2116/agentic_testing_framework).
