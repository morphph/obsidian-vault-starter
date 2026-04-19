---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, architecture, agentic, principle]
---

# Thin Harness, Fat Skills

## Summary
Architectural slogan from [[garry-tan]] (2026-04-11): the wrapper around the LLM should be small (~200 lines, JSON-in/text-out, read-only by default), and the procedural knowledge should live in markdown skill files. Inverts the common anti-pattern of fat harnesses with 40+ tool definitions and thin skills. Explains the gap between 2x and 100x AI-coding productivity using the same models.

## Details

### The three-layer architecture
1. **Fat skills** (top) — markdown procedures encoding judgment, process, domain knowledge. *90% of value lives here.*
2. **Thin CLI harness** (middle) — ~200 lines. Runs the model in a loop, reads/writes files, manages context, enforces safety. JSON in, text out. Read-only by default.
3. **Deterministic application** (bottom) — QueryDB, ReadDoc, Search, Timeline. Same input, same output, every time.

### The directional principle
- Push **intelligence up** into skills.
- Push **execution down** into deterministic tooling.
- Keep the **harness thin**.
- Result: every model improvement automatically improves every skill, while the deterministic layer stays perfectly reliable.

### The anti-pattern Garry calls out
- 40+ tool definitions eating half the context window
- "God-tools" with 2-5 second MCP round-trips
- REST API wrappers turning every endpoint into a separate tool
- Cost: 3x tokens, 3x latency, 3x failure rate
- Counter-example: Playwright CLI doing each browser op in 100ms vs Chrome MCP taking 15s for screenshot-find-click-wait-read = **75x faster**

### Why the "100x" gap exists
Steve Yegge: AI-agent coders are 10x-100x more productive than Cursor/chat users. The 2x people and 100x people use the **same models**. Difference is architecture. Garry's read of the [[claude-code]] source leak (3/31/2026 npm incident, 512K lines) confirmed the pattern: live repo context, prompt caching, purpose-built tools, context bloat minimization, structured session memory, parallel sub-agents — none make the model smarter; all give the model the right context at the right time.

### Five definitions that compose into the architecture
1. [[skill-as-method-call|Skill files]] — markdown procedures invoked with parameters
2. **The harness** — thin program running the LLM loop
3. [[resolvers]] — routing table for context ("when X appears, load Y")
4. [[latent-vs-deterministic]] — every step is one or the other; confusing them is the most common agent-design mistake
5. [[diarization]] — model reads everything, writes a structured one-page profile

### Worked example: YC Startup School (July 2026 Chase Center)
6,000 founders. Skills:
- `/enrich-founder` — pulls all sources nightly via cron, diarizes, surfaces SAYS-vs-ACTUALLY-BUILDING gap
- `/match-breakout` — 1,200 founders, sector clusters, 30/room
- `/match-lunch` — 600 founders, serendipity matching across sectors, 8/table, no repeats
- `/match-live` — 200ms nearest-neighbor for whoever's in the building right now
- `/improve` — reads NPS, diarizes "OK" responses, writes new rules back into the matching skill files. **The skill rewrites itself.** July: 12% "OK" → next event: 4%.

### Why this validates [[harness-design]] convergent evolution
Anthropic's formal frame: "LLM as reasoning center; harness provides perception, action, memory, constraints." Garry's pop frame: "thin harness, fat skills." Same architecture from different starting points. Also validates [[llm-judgment-vs-scripts]] (Sarver's independently-derived rule) — Garry's "latent vs deterministic" is the same line.

### Connection to existing wiki concepts
- [[harness-design]] → Garry's article is the most accessible field guide; provides the slogan.
- [[llm-judgment-vs-scripts]] → "latent vs deterministic" is a synonymous reformulation, with one new contribution: the explicit name for *why* the line matters (latent space = where intelligence lives; deterministic = where trust lives).
- [[claude-code]] → described as the canonical implementation; its skill-description-as-resolver pattern is the worked example.
- [[ralph-wiggum]] / [[orchestration-loop]] → the loop *is* the thin harness; Garry's contribution is pushing the procedural content out of the loop and into skill files.

## Connections
- Related: [[garry-tan]], [[skill-as-method-call]], [[resolvers]], [[diarization]], [[latent-vs-deterministic]], [[harness-design]], [[llm-judgment-vs-scripts]], [[claude-code]], [[openclaw]], [[orchestration-loop]], [[context-management]], [[infrastructure-layer]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation — full concept from Garry Tan's longform |
