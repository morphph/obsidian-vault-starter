---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, connection, insight]
---

# Connection: LLM Judgment vs Scripts and Harness Design

## The Connection

[[llm-judgment-vs-scripts]] (Sarver's design rule for personal AI assistants) and [[harness-design]] (Anthropic's architecture for agentic coding) arrived at the **same fundamental boundary** from completely different domains. Sarver: "LLMs handle judgment, scripts handle everything else." Anthropic: "LLM as reasoning center; Harness provides perception, action, memory, and constraints."

## Key Insight

This is **convergent evolution** — a VC building a personal chief of staff and an AI lab engineering multi-agent coding systems independently discovered that the critical design decision is **where you draw the line between LLM and deterministic code**. The principle is domain-independent:

- In coding agents: the harness manages tools, permissions, context compression, file I/O. The LLM reasons about what to do next.
- In personal assistants: scripts manage API calls, file reads, timestamp comparisons, message sending. The LLM reasons about priorities and drafts.
- In this wiki: the compiler harness manages file creation, index updates, log appends. The LLM reasons about entity extraction, synthesis, and connections.

The failure mode is also identical across domains: **routing deterministic operations through an LLM introduces stochastic failures that destroy user trust.** Sarver says "things break in unpredictable ways and you stop trusting the system." Anthropic's [[permission-system]] uses fail-closed defaults for the same reason — safety-critical operations can't be probabilistic.

## Where Else This Applies

Any LLM-powered system should ask: "Is this operation judgment or procedure?" If procedure, it belongs in code. This includes:
- Database queries: deterministic → script
- "Should we query the database?" → judgment → LLM
- Sending an email: deterministic → script
- "What should the email say?" → judgment → LLM
- Running tests: deterministic → script
- "Which tests are relevant?" → judgment → LLM

## Related Concepts
- [[llm-judgment-vs-scripts]] — The personal assistant formulation
- [[harness-design]] — The agentic coding formulation
- [[permission-system]] — Fail-closed defaults as another expression of "don't leave deterministic safety to probabilistic judgment"
- [[compiler-analogy]] — The compiler does the deterministic orchestration; LLM does the reasoning within each compilation step

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | Cross-source analysis: Sarver × Anthropic | Initial creation — convergent evolution of LLM/scaffolding boundary |
