---
type: concept
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, architecture, agentic, framework]
---

# Thin Harness, Fat Skills

## Summary
Architectural principle coined by [[garry-tan|Garry Tan]] (YC, 2026-04-11): the secret to 100x productivity with LLMs is *not* a smarter model — it's pushing intelligence **up** into reusable markdown skills, pushing execution **down** into deterministic tooling, and keeping the harness (the LLM-running shell) **thin**. Fits on an index card; explains the gap between 2x and 100x users of the same Claude model.

## Details

### The core claim
- "The 2x people and the 100x people are using the same models. The difference isn't intelligence. It's architecture."
- Triggered by [[claude-code]]'s accidental 2026-03-31 npm publish (512K lines) which Garry read end-to-end
- Validates that the value lives in the *wrapper around the model*, not the model itself

### Three-layer architecture (the index card)

```
┌─────────────────────────────────────┐
│  FAT SKILLS (90% of value)          │ ← markdown procedures encoding judgment
├─────────────────────────────────────┤
│  THIN CLI HARNESS (~200 LOC)        │ ← JSON in, text out, read-only by default
├─────────────────────────────────────┤
│  YOUR APPLICATION (deterministic)   │ ← QueryDB, ReadDoc, Search, Timeline
└─────────────────────────────────────┘
```

- **Directional principle**: Push intelligence *up*, push execution *down*, keep harness *thin*
- **Compounding effect**: Every model upgrade automatically improves every skill; deterministic layer stays perfectly reliable

### Five composing definitions
1. **[[skill-as-method-call|Skill files]]** — markdown procedures with parameters; same skill produces radically different capabilities depending on inputs
2. **The harness** — only does 4 things: model loop, file I/O, context management, safety enforcement. Anti-pattern: 40+ tool defs eating half the context window
3. **[[resolvers]]** — routing tables mapping task type → which docs to load. Garry's CLAUDE.md went from 20K lines (degraded attention) to 200 lines (pointers + on-demand loading)
4. **[[latent-vs-deterministic]]** — every step is either judgment (latent) or repeatable computation (deterministic); confusing them is the #1 design mistake
5. **[[diarization]]** — model reads everything about a subject and synthesizes a structured profile; the "analyst's brief" no SQL or RAG can produce

### Why thin harness wins
- **Speed**: Purpose-built CLI ≈ 100ms per browser op vs MCP ≈ 15s for screenshot-find-click-wait-read = **75x faster**
- **Tokens**: Fat harness with 40+ tool defs = 3x tokens, 3x latency, 3x failure rate
- **Maintenance**: 200 LOC harness rarely needs touching; markdown skills evolve freely
- **Compounds**: Skills are *permanent upgrades* — never degrade, never forget, run at 3 AM, get smarter every model release

### The discipline rule (Garry's instruction to his OpenClaw)
> "You are not allowed to do one-off work. If I ask you to do something and it's the kind of thing that will need to happen again: do it manually the first time on 3-10 items. Show me. If I approve, codify it into a skill file. If it should run automatically, put it on a cron. **The test: if I have to ask you for something twice, you failed.**"

### Production case study: YC Startup School (6,000 founders)
- `/enrich-founder` skill: pulls all sources (application, GitHub, advisor 1:1 transcripts, X, Claude Code transcripts) → diarizes → highlights "says vs. actually building" gaps
- 3 invocations of one matching skill: `/match-breakout` (1,200 ppl, sector clustering) · `/match-lunch` (600 ppl, serendipity) · `/match-live` (real-time 1:1 pairing)
- `/improve` skill: reads NPS surveys, diarizes "OK" responses, **writes new rules back into the matching skills** — the skill rewrites itself
- Result: 12% "OK" → 4% "OK" between events without anyone rewriting code

### Universal pattern this generalizes
- **Loop A**: retrieve → read → diarize → count → synthesize
- **Loop B**: survey → investigate → diarize → rewrite the skill
- Garry: "If you want to know what the most valuable loops are in 2026, it's those."

## Connections
- Related: [[skill-as-method-call]], [[resolvers]], [[latent-vs-deterministic]], [[diarization]], [[harness-design]], [[claude-code]], [[ralph-wiggum]], [[garry-tan]], [[assumptions-expire]], [[llm-judgment-vs-scripts]], [[zero-friction-capture]], [[boris-cherny]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — full framework + YC case study |
