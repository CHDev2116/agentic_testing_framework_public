# Docs index

| Document | Description |
|----------|-------------|
| [`articles/README.md`](articles/README.md) | **How to move or cross-post** technical writing from Medium/LinkedIn into this repo |
| [`integrator-guide.md`](integrator-guide.md) | ~3-minute path: run the minimal example, understand the HTTP payload |
| [`inference-contract.md`](inference-contract.md) | Stable fields third-party backends should return (`decision`, `code`, `msg`, `backend`) |

## External articles (Medium / LinkedIn → canonical docs)

| Title | Channel | Link to article |
|-------|---------|-----------------|
| Why 13 Years of Traditional QA Prepared Me for the “Chaos” of GenAI | GitHub (repo) | [2026-05-13-why-traditional-qa-prepared-genai.md](articles/2026-05-13-why-traditional-qa-prepared-genai.md) |

When you publish or migrate a post:

1. Add a row above (title, channel, **URL to the article**).
2. In the article body, link **back** to this repo so steps stay versioned:
   - [`integrator-guide.md`](integrator-guide.md) — runnable path + payload
   - [`inference-contract.md`](inference-contract.md) — `decision` / `code` / `msg` / `backend`
   - [`../examples/mock_api_roundtrip/README.md`](../examples/mock_api_roundtrip/README.md) — server + client + troubleshooting
