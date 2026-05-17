# Skills Changelog: Ubiquitous Language → /grill-with-docs

**Source:** https://www.aihero.dev/skills-changelog-ubiquitous-language-grill-with-docs
**Author:** Matt Pocock (AI Hero)
**Fetch method:** WebFetch
**Fetched:** 2026-05-17

## Summary

Matt deprecated the original `/ubiquitous-language` skill and merged its functionality directly into `/grill-with-docs`. Two reasons:

1. **Ubiquitous-language was a single project-wide file** — but real systems have multiple bounded contexts (ordering vs billing), each with its own language. The new design supports per-context CONTEXT.md plus a root CONTEXT-MAP.md.
2. **Grilling and documenting were redundant if separated** — the grilling session naturally surfaces the terms that need to be in the glossary. Bundling them means you don't context-switch between "discuss" and "document."

## DDD connection

The skill is an applied implementation of Eric Evans' Domain-Driven Design concepts:
- **Ubiquitous Language** — shared vocabulary between devs and domain experts
- **Bounded Context** — distinct domain models in a single system
- **Context Map** — relationships between bounded contexts

Honors Conway's Law: system architecture mirrors team communication patterns. Each team's bounded context develops its own language naturally.

## Files created/updated

- **CONTEXT.md** per bounded context — glossary, no implementation details
- **ADRs (Architectural Decision Records)** under `docs/adr/` — only for decisions that are (1) hard to reverse, (2) surprising without context, (3) result of real trade-off

## Why this matters for Matt's broader workflow

CONTEXT.md becomes the "team-specific vocabulary" that the model inherits — e.g., "customer" instead of "user," "materialization cascade" instead of a verbose paragraph. This:
- Reduces token cost (concise terms vs verbose explanations)
- Improves agent naming consistency (variables, files match domain language)
- Makes future grilling sessions faster (don't re-resolve same terms)
- Surfaces hidden disagreements early (when the agent says "I think you mean X")

## Practical pattern

Run `/grill-with-docs` at the start of any non-trivial change. It will:
1. Ask one question at a time about the planned change
2. Cross-check against CONTEXT.md — flag any term collisions
3. Cross-check against the actual codebase — flag any contradictions
4. Update CONTEXT.md inline when new terms are resolved
5. Offer ADR when a decision passes the 3-criteria gate

Output: clarified plan + updated CONTEXT.md + maybe a new ADR. Now you're ready to write the prompt for the implementation agent (or hand off to AFK).
