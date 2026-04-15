---
type: concept
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
tags: [wiki, quality, agentic]
---

# Software Entropy

## Summary
The tendency of codebases to deteriorate over time, dramatically accelerated by AI coding agents. Agents amplify what they see: poor code leads to poorer code. A human commits once or twice a day; AI agents can pile dozens of commits in hours, compounding quality issues faster than any human could.

## Details
- **"The repo wins"**: Agent instructions compete with codebase evidence. The prompt is a few lines; the codebase is thousands of lines of evidence. When they conflict, agents follow the codebase, not instructions.
  - Example: "never use `any` types" in prompt, but `any` throughout existing code → agent uses `any`
- **Acceleration effect**: Human = 1-2 commits/day. [[ralph-wiggum|Ralph]] = dozens of commits in hours. If those commits are low quality, entropy compounds fast.
- **Mitigations**:
  1. Keep codebase clean before letting agents loose
  2. Use [[verification-loops|feedback loops]] (linting, types, tests) to enforce standards
  3. Make quality expectations explicit and visible (in AGENTS.md, CLAUDE.md, or prompts)
  4. Communicate repo type: prototype ("speed over perfection"), production ("must be maintainable"), library ("backward compatibility matters")
- **Entropy reversal**: The "Entropy Loop" — a [[ralph-wiggum|Ralph]] variant that scans for code smells (unused exports, dead code, inconsistent patterns) and cleans them up, one issue per iteration.
- **Philosophical framing**: "You are not just writing code. You are shaping the future of this project. The patterns you establish will be copied. The corners you cut will be cut again."

## Connections
- Related: [[ralph-wiggum]], [[verification-loops]], [[self-evaluation-bias]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Initial creation — from Matt Pocock's "The Repo Wins" principle |
