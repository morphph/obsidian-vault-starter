---
type: concept
created: 2026-05-09
last-updated: 2026-05-09
sources:
  - raw/2026-05-05-khairallah-3-ai-agents-replace-first-hires.md
tags: [wiki, principle, agentic, quality, content]
---

# Quality Gate Loop

## Summary
[[eng-khairallah|Khairallah]]'s pattern for production-grade AI content (and any agent output where quality varies): **score → if-below-threshold-rewrite → loop until pass → human final pass for "soul."** Sister-pattern to [[verification-loops]] but specifically about *automated rewrite-until-good*, not just *judge-pass*. The 80/20 production split is what separates this from "AI slop": agent does 80% of production, founder adds 20% of personality.

## Details

### The pattern

```
generate first draft
  ↓
score on N dimensions (e.g., voice match / hook strength / value density / originality)
  ↓
if any dimension < threshold:
    rewrite with critique attached
    loop back to score
  ↓
human final pass (5-10 min): personal stories, insider perspectives, hot takes
  ↓
publish
```

### Why this works (and why most AI content fails)

> "The reason most AI content feels generic is that **people publish first drafts**."

The first draft of any LLM output is the average of the model's training distribution. The 5th draft, after auto-critique, is closer to your specific quality bar. Without a quality gate:
- First-draft quality → mediocre at scale → reader stops engaging
- With a quality gate: every published piece meets *your* threshold, not the model's median

### Khairallah's recommended scoring dimensions for content

- **Voice match** — does it sound like the founder?
- **Hook strength** — does the first 3 lines earn a click?
- **Value density** — substance per word?
- **Originality** — would someone else have written exactly this?

Each scored 0-10, threshold typically ≥ 7-8. Below threshold → rewrite with the score as critique.

### The 80/20 production split

> "The agent handles 80% of the production. You handle 20% of the soul."

Production = formatting, variations, scheduling, repurposing across platforms — the time-consuming non-creative work.
Soul = personal stories, insider perspectives, hot takes that only the founder can provide.

This split is **why** the quality-gate loop is necessary: you trust the agent with 80% of output volume, so you need a mechanical quality bar to keep that 80% from dragging the brand down.

### How it differs from [[verification-loops]]

| Dimension | [[verification-loops]] | Quality Gate Loop |
|-----------|------------------------|---------------------|
| Goal | Catch failures (tests pass, no bugs) | Improve until threshold (good enough to publish) |
| Verdict | Binary pass/fail | Multi-dimensional score |
| Action on fail | Stop, alert, retry | Auto-rewrite with critique attached |
| Domain | Code, UI rendering, factual correctness | Subjective output (content, drafts, briefs) |
| End state | Pass = ship | Pass = *agent* says good, *human* still does final pass |

They're complementary. Use verification-loops for code; use quality-gate-loops for content.

### Why "score-then-rewrite" beats "regenerate"

The naive alternative is "if bad, regenerate." Two failure modes:
- **Stochastic improvement** — a new draft might be better OR worse, just different
- **Lost context** — you discard what was almost-right

Score-then-rewrite uses the score as **explicit critique attached to the prompt** — the rewrite is targeted: *"This scored 6/10 on voice match because the tone is too academic. Rewrite preserving the structure but matching this voice sample: ..."* — convergent, not random.

### Connection to existing wiki concepts

- [[self-evaluation-bias]] — agents that grade themselves trend toward 7/10 on everything. Defense: use a *separate* evaluator agent (different prompt, ideally different model) to score.
- [[verification-loops]] — they share the "feedback loop" shape. Quality gate is a specialization for subjective output.
- [[diarization]] — Garry's pattern of "model reads everything, writes a structured one-page profile." Quality gates are how you keep that one page sharp.
- [[blog2video]] — the publication pipeline where this would land in our domain. Could replace the current single-pass draft generation with score-rewrite-loop on voice-match + hook-strength.

### When NOT to use it
- For factual correctness — that's [[verification-loops]] territory (deterministic check, not score)
- For one-off output — the loop overhead only pays off at volume
- When the threshold isn't well-defined — if you can't articulate what 9/10 looks like, the score is noise

## Connections
- Related: [[eng-khairallah]], [[3-agent-starter-team]], [[prompt-architecture-three-layer]], [[verification-loops]], [[self-evaluation-bias]], [[diarization]], [[blog2video]], [[loreai]], [[multi-agent-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-09 | raw/2026-05-05-khairallah-3-ai-agents-replace-first-hires.md | Initial creation |
