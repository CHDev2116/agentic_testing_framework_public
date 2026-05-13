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

## Relationship to technical articles

Long-form posts (e.g. on Medium) can **link here** as the canonical place for commands, contracts, and reproducible steps. This repo is the stable “home” for anything that should stay versioned with git.

## License

Specify your license in a `LICENSE` file before publishing (e.g. MIT, Apache-2.0). This stub does not ship a license file by default.
