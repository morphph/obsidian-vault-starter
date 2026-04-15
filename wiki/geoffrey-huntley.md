---
type: entity
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
  - raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md
  - raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md
  - raw/2026-04-15-humanlayer-brief-history-of-ralph.md
tags: [wiki, person, builder]
---

# Geoffrey Huntley

## Summary
Creator of the [[ralph-wiggum]] technique — the autonomous AI coding loop that went viral in late 2025. Software engineer who proved that a simple bash `while :; do` loop could deliver production-grade results, including a $50K contract for $297 in API costs and the CURSED programming language built over 3 months of autonomous iteration.

## Details
- Started experimenting with Ralph around **June 2025**, officially launched via blog post in **July 2025**
- Original implementation used Amp/Sourcegraph before becoming primarily associated with [[claude-code|Claude Code]]
- Core philosophy: **"The loop is the hero, not the model"** — don't wait for smarter models, build persistent systems
- Operator mindset: "tune like a guitar" — when Ralph misbehaves, add instructional signs (prompt refinements) rather than blaming the tool
- Built **CURSED** — a Gen Z programming language with `slay` (function), `sus` (variable), `based` (true). Compiled to Zig via LLVM. Created entirely by Ralph over 3 months.
- Key technical contributions:
  - **One-thing-per-loop** — conserve context window (~170K tokens)
  - **Context stack allocation** — `@fix_plan.md`, `@specs/*`, `@AGENT.md`
  - **Subagent parallelization** — up to 500 for research, only 1 for validation
  - **Deterministic backpressure** — immediate testing after every change
  - **Self-learning agent** — agent updates `@AGENT.md` when discovering better approaches
- Honest about limitations: Ralph works best for **greenfield projects only**. Retrofitting existing codebases is problematic.
- Emphasizes senior engineer oversight remains essential — Ralph amplifies skilled guidance
- Authored the official playbook: [how-to-ralph-wiggum](https://github.com/ghuntley/how-to-ralph-wiggum) with three-phase workflow and prompt templates
- Coined future concepts: **Gas Town** ("Kubernetes for agents") with **MEOW** (Molecular Expression of Work) for parallel agent coordination
- Official Anthropic plugin was formalized by [[boris-cherny]] in Dec 2025, based on Huntley's work — but uses Stop hook instead of bash loop, which Huntley considers a deviation from the core principle of fresh context per iteration

## Connections
- Related: [[ralph-wiggum]], [[claude-code]], [[boris-cherny]], [[matt-pocock]], [[harness-design]], [[software-entropy]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-ghuntley-ralph-wiggum-original.md | Initial creation — original blog post |
| 2026-04-15 | raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md | Added playbook methodology |
| 2026-04-15 | raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md | Added Gas Town, MEOW (from newsletter text; 58-min podcast audio not transcribed) |
| 2026-04-15 | raw/2026-04-15-humanlayer-brief-history-of-ralph.md | Added timeline context |
