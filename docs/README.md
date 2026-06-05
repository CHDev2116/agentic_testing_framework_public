# Docs index

| Document | Description |
|----------|-------------|
| [`articles/`](articles/) | Versioned articles (Markdown); images in [`articles/assets/`](articles/assets/) |
| [`integrator-guide.md`](integrator-guide.md) | ~3-minute path: run the minimal example, understand the HTTP payload |
| [`inference-contract.md`](inference-contract.md) | Stable fields third-party backends should return (`decision`, `code`, `msg`, `backend`) |

## External articles (Medium / LinkedIn → canonical docs)

| Title | Channel | Link to article |
|-------|---------|-----------------|
| Why 13 Years of Traditional QA Prepared Me for the “Chaos” of GenAI | GitHub (repo) | [2026-05-02-why-traditional-qa-prepared-genai.md](articles/2026-05-02-why-traditional-qa-prepared-genai.md) |
| Why LLM Outputs Break Your System — and How a QA Mindset Fixes It | GitHub (repo) | [2026-05-08-why-llm-outputs-break-your-system.md](articles/2026-05-08-why-llm-outputs-break-your-system.md) |
| Beyond Pass/Fail: Bounded Self-Healing for Visual QA | GitHub (repo) | [2026-05-16-bounded-self-healing-vision-qa-probabilistic-evaluation.md](articles/2026-05-16-bounded-self-healing-vision-qa-probabilistic-evaluation.md) |
| Engineering the Inference Contract: Why decision, code, msg, and backend | GitHub (repo) | [2026-05-23-inference-contract-engineering.md](articles/2026-05-23-inference-contract-engineering.md) |
| From Inference Labels to Release Gates: GO, REVIEW, and NO_GO | GitHub (repo) | [2026-05-30-from-inference-labels-to-release-gates.md](articles/2026-05-30-from-inference-labels-to-release-gates.md) |
| What the Public Repo Actually Gives You — Public Slice vs. Full Framework | GitHub (repo) | [2026-06-06-public-slice-vs-full-framework.md](articles/2026-06-06-public-slice-vs-full-framework.md) |

When you publish or migrate a post:

1. Add the Markdown file under [`articles/`](articles/) (suggested name: `YYYY-MM-DD-short-slug.md`); optional images under [`articles/assets/`](articles/assets/).
2. Add a row above (title, channel, **URL to the article**).
3. In the article body, link **back** to this repo so steps stay versioned:
   - [`integrator-guide.md`](integrator-guide.md) — runnable path + payload
   - [`inference-contract.md`](inference-contract.md) — `decision` / `code` / `msg` / `backend`
   - [`../examples/mock_api_roundtrip/README.md`](../examples/mock_api_roundtrip/README.md) — server + client + troubleshooting
