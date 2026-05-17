---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-amplitude-ralph-loop-102-features.md
tags: [wiki, pattern, ralph, dispatcher]
---

# Opportunity Finder Pattern (Dispatcher)

## Summary
Architectural pattern from Amplitude's 102-features-in-a-week Ralph loop experiment: replace "what should the agent build next?" with a structured ranked queue produced by a separate analytics-driven component. **The loop is the engine; the dispatcher is the intelligence.** Generalizes beyond product analytics — applies to any AFK pipeline.

## Details

### The thesis
> "The loop itself is secondary. The dispatcher and verification gate matter most. Any loop requires honest outcome signals and clearly defined objective functions to progress toward value."

`while true; do agent; done` with no scorer is noise. The dispatcher is what makes the loop converge on value.

### Amplitude's specific dispatcher (Opportunity Finder)
Inputs:
- Analytics signals (what users do)
- Session replays (where users struggle)
- Customer feedback (what users say)
- Agent traces (what worked / what didn't last cycle)
- Competitive gaps (what competitors have, you don't)

Output: ranked queue of structured opportunity specs (problem + proposed solution + behavioral evidence).

### Generalized dispatcher inputs (any AFK pipeline)
For your own AFK projects, the dispatcher needs:
1. **Demand signal** — what is needed (user metrics, backlog, complaint queue)
2. **Quality signal** — what worked last time (agent traces, test pass rates, A/B results)
3. **Cost signal** — what to skip (low impact, high risk)
4. **Recency signal** — freshness gate (stale opportunities decay)

### Pattern in 2 sentences
Build a small "what-to-do-next-and-why" producer that runs OUTSIDE the loop. Pipe its output INTO the loop as ranked, scoped, evidence-backed tasks.

### Why this beats Ralph's bare loop
- **Bare Ralph** (`while true; do agent; done`): agent invents tasks from scratch each cycle, no memory, no priority
- **Dispatcher + Ralph**: each cycle starts from a curated, ranked, evidence-backed input — agent does execution, dispatcher does selection

This is the same separation as [[llm-judgment-vs-scripts]] applied at the meta level: the LLM (loop) does work; deterministic code (dispatcher) does scoring/ranking.

### Self-instrumentation as feedback to dispatcher
The agent wires up its own telemetry on each ship. Dispatcher's next-cycle ranking uses this. **Without telemetry, dispatcher has no learning loop.** This is what makes "self-instrumentation enables compounding" non-optional.

## Connections
- [[ralph-wiggum]] (the loop it complements)
- [[verification-loops]] (the other half — gates)
- [[llm-judgment-vs-scripts]] (the design principle)
- [[silent-fallback-antipattern]] (skipped verification is the failure)
- Phase 5 of: [[idea-to-afk-agent-flow]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Amplitude Ralph loop case study | Initial creation |
