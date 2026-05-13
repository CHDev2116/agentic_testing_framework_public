# Agentic Testing Framework — public docs & examples

This repository is the **public slice** of work on a configuration-driven, multi-backend image QA / release-gating pipeline. It exists so integrators and readers can clone **documentation and a minimal runnable example** without depending on the full private codebase.

> **Note:** The complete framework (batch CLI, Streamlit demo, full test suite, and CI) may live in a separate private repository. What you find here is intentionally **small, honest, and reproducible**—README, `docs/`, and one example you can run locally.

## Contents

| Path | Purpose |
|------|---------|
| [`docs/`](docs/) | Integrator-focused notes and the **inference response contract** |
| [`examples/mock_api_roundtrip/`](examples/mock_api_roundtrip/) | **Minimal mock HTTP server** + **stdlib HTTP client** demonstrating the same JSON shape the full framework expects from a `mock_api`-style backend |

## Quick start (example only)

```bash
cd examples/mock_api_roundtrip
python3 mock_server.py
# other terminal:
python3 run_client.py
```

See [`examples/mock_api_roundtrip/README.md`](examples/mock_api_roundtrip/README.md) for details.

## Linking from Medium or LinkedIn

Use this repo as the **canonical “home”** for anything that should stay versioned: full command sequences, JSON contracts, and the runnable example. In articles, a practical split is:

| Channel | What to put there |
|---------|-------------------|
| **Medium / blog** | Narrative, diagrams, trade-offs, screenshots; **link out** for steps that must stay copy-paste accurate. |
| **LinkedIn** | Short hook + 3–6 bullets; **one primary link** (usually `docs/integrator-guide.md` or this README). |

**Stable deep links** (replace `OWNER` and `REPO` after you publish on GitHub):

- Integrator guide: `https://github.com/OWNER/REPO/blob/main/docs/integrator-guide.md`
- Inference contract: `https://github.com/OWNER/REPO/blob/main/docs/inference-contract.md`
- Docs index: `https://github.com/OWNER/REPO/blob/main/docs/README.md`
- Minimal example (folder): `https://github.com/OWNER/REPO/tree/main/examples/mock_api_roundtrip`
- Example README (run + troubleshoot): `https://github.com/OWNER/REPO/blob/main/examples/mock_api_roundtrip/README.md`

**Tip:** In LinkedIn, prefer linking to a **specific file** (e.g. the integrator guide) so readers land directly on reproducible steps; in Medium, sprinkle the same links at the end of each major section so skimmers still find the repo.

## License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
