# Docs index

| Document | Description |
|----------|-------------|
| [`articles/`](articles/) | Versioned articles (Markdown); images in [`articles/assets/`](articles/assets/) |
| [`integrator-guide.md`](integrator-guide.md) | ~3-minute path: run the minimal example, understand the HTTP payload |
| [`inference-contract.md`](inference-contract.md) | Stable fields third-party backends should return (`decision`, `code`, `msg`, `backend`) |

## External articles (Medium / LinkedIn → canonical docs)

| Title | Channel | Link to article |
|-------|---------|-----------------|
| Why 13 Years of Traditional QA Prepared Me for the “Chaos” of GenAI | GitHub (repo) | [2026-05-13-why-traditional-qa-prepared-genai.md](articles/2026-05-13-why-traditional-qa-prepared-genai.md) |

When you publish or migrate a post:

1. Add the Markdown file under [`articles/`](articles/) (suggested name: `YYYY-MM-DD-short-slug.md`); optional images under [`articles/assets/`](articles/assets/).
2. Add a row above (title, channel, **URL to the article**).
3. In the article body, link **back** to this repo so steps stay versioned:
   - [`integrator-guide.md`](integrator-guide.md) — runnable path + payload
   - [`inference-contract.md`](inference-contract.md) — `decision` / `code` / `msg` / `backend`
   - [`../examples/mock_api_roundtrip/README.md`](../examples/mock_api_roundtrip/README.md) — server + client + troubleshooting

(For Medium/LinkedIn-first posts, you can keep the long post off-repo and add only a short stub `.md` under [`articles/`](articles/) plus a link in the table.)
