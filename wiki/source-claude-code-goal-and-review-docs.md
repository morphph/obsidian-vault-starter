---
type: source-summary
created: 2026-05-13
last-updated: 2026-05-13
sources:
  - raw/2026-05-13-claude-code-goal-and-code-review.md
tags: [claude-code, source, official-docs, autonomy, code-review]
---

# Source: Claude Code `/goal` + Code Review official docs (2026-05-13 fetch)

## Summary
Two new Claude Code features captured from official Anthropic documentation: **`/goal`** (session-scoped autonomous turn-loop with model evaluator) and **Code Review** (managed multi-agent PR review on GitHub). Both implement the same "agent + verifier" pattern at different layers — `/goal` at the turn boundary inside a session, Code Review at the PR boundary across an org.

## Origin
- `/goal` docs: https://code.claude.com/docs/en/goal
- Code Review docs: https://code.claude.com/docs/en/code-review
- Announcement blog: https://claude.com/blog/code-review (returned HTTP 405 on direct fetch, content cross-referenced via InfoQ)
- InfoQ writeup: https://www.infoq.com/news/2026/04/claude-code-review/

## What's in here
- Full mechanics of `/goal`: how to set, status, clear, resume; the prompt-based Stop-hook implementation; evaluator transcript-only constraint; condition-writing guidance; comparison vs `/loop` / Stop hooks / auto mode.
- Full mechanics of Code Review: trigger modes, severity model (🔴/🟡/🟣), check-run integration, `CLAUDE.md` vs `REVIEW.md` roles, manual trigger commands, pricing ($15–25/review), spend caps, analytics.
- Reported quality metrics: <1% false positive rate, 84% finding rate on >1000 LOC PRs.
- Example REVIEW.md from docs.

## Wiki pages produced
- [[claude-code-goal]] — concept page on `/goal`
- [[claude-code-review]] — concept page on Code Review managed service
- This page — source summary

## Wiki pages updated
- [[claude-code]] — added two new commands/services to the official surface
- [[index.md]] — registered new pages

## Key non-obvious facts
1. `/goal`'s evaluator is **transcript-only** — no tool access. Conditions must be checkable from what Claude has surfaced. This is the single biggest gotcha and informs all condition-writing patterns.
2. `/goal` is implemented as a session-scoped **prompt-based Stop hook**, which means it inherits all the hook-system trust/permission constraints (blocked by `disableAllHooks`, etc.).
3. Code Review's check run **always completes neutral** by design — it never blocks merge. Gating on findings requires custom CI parsing the machine-readable severity JSON.
4. `REVIEW.md` is **injected verbatim** with NO `@` import expansion — opposite of `CLAUDE.md` which is hierarchical and resolvable.
5. The Code Review GitHub App requests **read+write** on contents/issues/PRs (broader than strictly needed) to support optional GitHub Actions integration later.
6. Reactions (👍/👎) feed back into reviewer tuning — production-scale [[trigger-evals]] pattern.
7. Code Review is **NOT available** with Zero Data Retention enabled.

## Connections
- [[claude-code-goal]], [[claude-code-review]] — the two concept pages.
- [[verification-loops]], [[multi-agent-architecture]] — the underlying patterns.
- [[claude-code]] — the parent product.

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-13 | raw/2026-05-13-claude-code-goal-and-code-review.md | Initial source summary |
