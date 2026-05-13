# Technical articles in this repo

Use this folder when you want the **GitHub copy** to be part of your evidence chain (versioned text, reviewable diffs, linkable from interviews).

## Choose your “source of truth”

| Strategy | Best when | What you do |
|----------|-----------|----------------|
| **A. Repo-first** | You want Medium/LinkedIn to **point here** as canonical | Write or paste the article as Markdown under `docs/articles/`, then cross-post a short intro + link on Medium/LinkedIn. |
| **B. Medium-first** | You already invested in Medium layout/SEO | Keep the long post on Medium; in this repo add a **short stub** (abstract + key commands + link) under `docs/articles/`, and add the Medium URL to [`../README.md`](../README.md) “External articles” table. |
| **C. LinkedIn-only** | Post is short or LinkedIn-native | Add a **stub** here (summary + bullets + link to the LinkedIn post) so git still shows continuity. |

You can mix strategies by article.

## File naming

Suggested pattern (easy to sort):

```text
docs/articles/YYYY-MM-DD-short-slug.md
```

Example: `docs/articles/2026-05-13-mock-api-contract.md`

## Stub template (for B or C)

Copy this into a new file and fill in:

```markdown
# Title

**Published:** YYYY-MM-DD  
**Original (canonical):** <https://...>  
**Audience:** e.g. integrators / DevRel / vision QA

## Summary

2–4 sentences.

## Canonical links in this repo

- [Integrator guide](../integrator-guide.md)
- [Inference contract](../inference-contract.md)
- [Minimal example README](../../examples/mock_api_roundtrip/README.md)

## Key commands (optional)

Keep only what must stay copy-paste accurate.
```

## Full article template (for A)

Use normal Markdown: headings, code fences, images via relative paths (store images under `docs/articles/assets/` if needed).

At the top, optional front matter (not required by GitHub):

```markdown
---
title: "Your title"
date: 2026-05-13
---

First paragraph...
```

## After you add a file

1. Add a row to the **External articles** table in [`../README.md`](../README.md) (link to the **article**—Medium, LinkedIn, or the new `.md` file on GitHub).  
2. If the article lives **on GitHub**, the “Link to article” column can point to  
   `https://github.com/CHDev2116/agentic_testing_framework_public/blob/main/docs/articles/YYYY-MM-DD-slug.md`  
3. `git add`, `commit`, `push`.

## Medium-specific tip

Medium can **import** a URL or you can paste Markdown; if the **canonical** text is in git, paste from your local `.md` so Medium stays in sync manually, or treat Medium as a mirror and accept occasional drift.
