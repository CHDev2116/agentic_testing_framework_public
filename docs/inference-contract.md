# Inference response contract (normalized surface)

Third-party HTTP backends integrated in the style of a **`mock_api` provider** should return JSON that downstream batch code can normalize to the following **minimum** fields.

## Required fields (post-normalization)

| Field | Type | Description |
|-------|------|----------------|
| `decision` | string | One of: `Optimal`, `Blurry`, `Under-exposed`, `Over-exposed`, `Error` |
| `code` | string | Stable, machine-oriented status (e.g. `SUCCESS_200`, `ERR_MODEL_BACKEND_503`) |
| `msg` | string | Human-readable explanation (support queues, logs); **do not** rely on exact wording for automation |

## Recommended fields

| Field | Type | Description |
|-------|------|----------------|
| `backend` | string | Provider id (e.g. `mock_api`). In resilient setups, failures may annotate `provider->simulated` when a fallback path produced the result. |

## Optional

| Field | Type | Description |
|-------|------|----------------|
| `confidence` | number | Float in `[0, 1]` when the model supports it |

## HTTP wrapper conventions

- **Preferred response envelope:** `{ "result": { ...fields... } }`  
- **Also accepted:** a bare object `{ ...fields... }` at the top level.

## Design intent (one sentence)

**Machine path uses `code`; humans read `msg`; `decision` drives product QA labels**—so automation and support can share one payload without parsing free text.
