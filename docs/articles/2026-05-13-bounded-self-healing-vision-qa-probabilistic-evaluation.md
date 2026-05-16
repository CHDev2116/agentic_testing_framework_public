---
title: "Beyond Pass/Fail: Bounded Self-Healing for Visual QA"
date: 2026-05-13
---

# Beyond Pass/Fail: Bounded Self-Healing for Visual QA

**Published:** 2026-05-13  
**Audience:** QA engineers, ML integrators, and anyone shipping vision pipelines on probabilistic models.

> The prompt did not change.  
> The model did not change.  
> But suddenly, the pipeline broke.

That was the moment I realized **traditional testing assumptions do not translate cleanly** to probabilistic AI systems.

Recently, I have been experimenting with a **self-healing AI vision testing** approach for Visual QA workflows, aligned with the **Agentic Testing Framework** documented in this repository—a configuration-driven pipeline with engine, model, and evaluation layers.

## Why classic approaches stumble

Traditional approaches tend to fall into two extremes:

- **Manual inspection** — too slow and expensive.
- **Pixel-level comparison** — too brittle for real-world variability.

A slight lighting change can trigger a **false failure** even when the product is acceptable.

With generative and vision-heavy systems, what often matters more is **semantic quality**:

- Does the image look natural?
- Is the primary subject recognizable?
- Is the output **usable from a human perspective**?

That is where **Vision Language Models (VLMs)** get interesting—and where **inference instability** shows up.

AI outputs are **probabilistic**, not deterministic. **Static assertions alone** are no longer enough.

## Bounded self-healing instead of brittle pass/fail

Rather than treating evaluation as simple pass/fail logic, the framework uses a **bounded self-healing loop**.

When the system detects a **NO_GO** decision, it can:

1. **Diagnose probable causes**, for example:
   - under-exposure  
   - over-exposure  
   - blur / sharpness degradation  

2. **Apply targeted remediation**, for example:
   - brightness adjustment  
   - dimming  
   - sharpening  

3. **Re-run inference** through the stack:

```text
Engine → Model → Eval
```

Recovery stays **guardrail-bounded**:

- retry limits  
- gain thresholds  
- oscillation checks  
- bounded remediation policies  

That prevents the system from degrading into “retry until green.”

In practice, the workflow behaves less like a static test script and more like **iterative QA**. For example, when an image is flagged as too dark, the framework can brighten it, re-run inference, and check whether the result improves—all within a **constrained retry budget**.

## Output format: JSON is never guaranteed

Another challenge surfaced quickly during development:

**LLM outputs are not guaranteed to be valid JSON.**

Even with unchanged prompts, the model may suddenly emit:

- malformed JSON  
- Markdown wrappers  
- unexpected prose  
- partially invalid structured output  

To improve resilience, a lightweight recovery path performs:

- best-effort JSON extraction  
- schema normalization  
- graceful fallback handling  

If parsing still fails, remote inference can fall back to a **deterministic simulated** backend so **batch pipelines keep running**.

The goal is not “perfect AI behavior.” **The goal is operational resilience.**

## Local inference and backend flexibility

On the infrastructure side, the stack also explores **local inference** using:

- GGUF / Q4-style quantized models  
- Ollama  
- llama.cpp  
- deterministic, CI-style simulation backends  

That cuts latency and most marginal inference cost for **large batch runs**, while keeping sensitive datasets **local**.

Architecturally, the system is deliberately split into:

- **Engine** — deterministic image metrics  
- **Model** — backend abstraction  
- **Evaluation** — **GO / REVIEW / NO_GO** arbitration  

That separation makes **swapping backends** a configuration change instead of a rewrite.

## From boolean testing to probabilistic evaluation

One thing became very clear while building this:

Traditional QA tooling assumed **determinism**. **AI violates those assumptions.**

We are moving from:

```text
Boolean Testing
```

toward:

```text
Probabilistic Evaluation.
```

This work is my experiment in **resilient AI testing**: systems that not only detect failures, but diagnose instability and attempt **bounded recovery**.

We are no longer **only** validating correctness. **We are engineering reliability for probabilistic software.**

Tags: #AI #LLM #GenAI #Testing #QA #MachineLearning #Ollama #LlamaCpp #AIEngineering #SoftwareEngineering

## Canonical links in this repo

- [Integrator guide](../integrator-guide.md) — runnable path and HTTP payload  
- [Inference contract](../inference-contract.md) — `decision`, `code`, `msg`, `backend`  
- [Minimal mock API example](../../examples/mock_api_roundtrip/README.md) — server, client, troubleshooting  
- [Docs index](../README.md) — external articles table and publishing notes  
