# Agentic Testing Framework — public docs & examples

**Multi-backend image QA with a stable inference contract and release-style gates (`GO` / `REVIEW` / `NO_GO`) in the full pipeline.**

This repository is the **public slice**: versioned docs, a normative JSON contract, and a **stdlib-only** mock roundtrip you can run in minutes. Batch CLI, evaluation, and CI are part of the **full Agentic Testing Framework** codebase, which is **not published in this repository**.

---

## 60 seconds for integrators

| | |
|---|---|
| **You are** | A backend or platform engineer wiring **third-party vision / LLM inference** into a batch or agentic QA pipeline |
| **The pain** | Every provider returns a different JSON shape; automation starts parsing `msg`, CI drifts, release logic forks per vendor |
| **What we publish here** | A small, stable DTO—`decision`, `code`, `msg`, optional `backend`—documented in [`docs/inference-contract.md`](docs/inference-contract.md) |
| **Prove your stack** | Run the mock server + client (no GPU, no API keys required): |

```bash
cd examples/mock_api_roundtrip
python3 mock_server.py   # terminal 1
python3 run_client.py    # terminal 2 → expect decision + code in JSON
```

| **Next step** | Link |
|---------------|------|
| ~3 min walkthrough | [`docs/integrator-guide.md`](docs/integrator-guide.md) |
| Field semantics (normative) | [`docs/inference-contract.md`](docs/inference-contract.md) |
| Why the contract exists (article) | [`docs/articles/2026-05-23-inference-contract-engineering.md`](docs/articles/2026-05-23-inference-contract-engineering.md) |

> **Scope:** Inference here answers *what the model thinks about the asset* (`Optimal`, `Blurry`, …). **Release gates** (`GO` / `REVIEW` / `NO_GO`) live in the evaluation layer of the full framework (not duplicated in this minimal example).

> **Full framework:** Batch CLI, Streamlit demo, full test suite, and CI belong to the complete Agentic Testing Framework pipeline, **outside this public slice**. This repo stays **small and reproducible** on purpose.

**Naming:** All articles and docs here use **Agentic Testing Framework** as the product name.

---

## Contents

| Path | Purpose |
|------|---------|
| [`docs/`](docs/) | Integrator notes, **inference contract**, and versioned articles |
| [`examples/mock_api_roundtrip/`](examples/mock_api_roundtrip/) | Minimal **mock HTTP server** + **stdlib client** for the `mock_api`-style JSON shape |

## Quick start (example only)

```bash
cd examples/mock_api_roundtrip
python3 mock_server.py
# other terminal:
python3 run_client.py
```

See [`examples/mock_api_roundtrip/README.md`](examples/mock_api_roundtrip/README.md) for troubleshooting and optional `MOCK_INFER_API_KEY`.

## Links

| Resource | Location |
|----------|----------|
| Full framework (batch CLI, eval, CI) | Not in this repo — see [public slice vs. full framework](docs/articles/2026-06-06-public-slice-vs-full-framework.md) |
| Docs index | [`docs/README.md`](docs/README.md) |
| Integrator guide | [`docs/integrator-guide.md`](docs/integrator-guide.md) |
| Inference contract | [`docs/inference-contract.md`](docs/inference-contract.md) |
| Technical articles | [`docs/articles/`](docs/articles/) |
| Mock API example | [`examples/mock_api_roundtrip/`](examples/mock_api_roundtrip/) |

## License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
