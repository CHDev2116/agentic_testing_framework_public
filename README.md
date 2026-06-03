# Agentic Testing Framework — public docs & examples

**Multi-backend image QA with a stable inference contract and release-style gates (`GO` / `REVIEW` / `NO_GO`) in the full pipeline.**

This repository is the **public slice**: versioned docs, a normative JSON contract, and a **stdlib-only** mock roundtrip you can run in minutes—without the private monorepo.

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

> **Full framework:** Batch CLI, Streamlit demo, full test suite, and CI may live in a **separate private repository**. This repo stays **small, honest, and reproducible** on purpose.

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

## Linking from Medium or LinkedIn

Use this repo as the **canonical “home”** for anything that must stay copy-paste accurate: commands, JSON contracts, and the runnable example.

| Channel | What to put there |
|---------|-------------------|
| **Medium / blog** | Narrative, diagrams, trade-offs; **link out** for exact steps and schemas |
| **LinkedIn** | Short hook + 3–6 bullets; **one primary link** (this README, [`integrator-guide.md`](docs/integrator-guide.md), or a specific article) |

**Stable deep links** (this repo on GitHub):

- Repository root: [github.com/CHDev2116/agentic_testing_framework_public](https://github.com/CHDev2116/agentic_testing_framework_public)
- Integrator guide: [docs/integrator-guide.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/integrator-guide.md)
- Inference contract: [docs/inference-contract.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/inference-contract.md)
- Docs index: [docs/README.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/README.md)
- Article — *Why 13 Years of Traditional QA Prepared Me for the “Chaos” of GenAI*: [docs/articles/2026-05-02-why-traditional-qa-prepared-genai.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-05-02-why-traditional-qa-prepared-genai.md)
- Article — *Why LLM Outputs Break Your System — and How a QA Mindset Fixes It*: [docs/articles/2026-05-08-why-llm-outputs-break-your-system.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-05-08-why-llm-outputs-break-your-system.md)
- Article — *Beyond Pass/Fail: Bounded Self-Healing for Visual QA*: [docs/articles/2026-05-16-bounded-self-healing-vision-qa-probabilistic-evaluation.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-05-16-bounded-self-healing-vision-qa-probabilistic-evaluation.md)
- Article — *Engineering the Inference Contract*: [docs/articles/2026-05-23-inference-contract-engineering.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-05-23-inference-contract-engineering.md)
- Article — *From Inference Labels to Release Gates*: [docs/articles/2026-05-30-from-inference-labels-to-release-gates.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-05-30-from-inference-labels-to-release-gates.md)
- Article — *Public Slice vs. Full Framework*: [docs/articles/2026-06-06-public-slice-vs-full-framework.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/2026-06-06-public-slice-vs-full-framework.md)
- Minimal example (folder): [examples/mock_api_roundtrip/](https://github.com/CHDev2116/agentic_testing_framework_public/tree/main/examples/mock_api_roundtrip)
- Example README (run + troubleshoot): [examples/mock_api_roundtrip/README.md](https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/examples/mock_api_roundtrip/README.md)

**Tip:** On LinkedIn, link to a **specific file** (e.g. integrator guide or the inference-contract article) so readers land on reproducible steps.

## License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
