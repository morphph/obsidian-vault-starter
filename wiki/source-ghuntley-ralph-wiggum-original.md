---
type: source-summary
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
tags: [wiki, source]
---

# Source: Ralph Wiggum as a "Software Engineer"

## Summary
Geoffrey Huntley's original blog post defining the Ralph Wiggum technique — the autonomous AI coding loop that went viral in late 2025. Core technical details: one-thing-per-loop, context stack allocation, subagent parallelization, deterministic backpressure. Includes the $50K→$297 case study and CURSED language project.

## Source Details
- **URL**: https://ghuntley.com/ralph/
- **Author**: [[geoffrey-huntley|Geoffrey Huntley]]
- **Date**: July 2025 (official launch)
- **Type**: Blog post — original source

## Key Claims
1. Ralph at its simplest: `while :; do cat PROMPT.md | claude-code ; done`
2. One thing per loop conserves the ~170K token context window
3. Subagent parallelization: up to 500 for research, only 1 for validation
4. $50,000 contract delivered for $297 in API costs
5. CURSED programming language built over 3 months of autonomous iteration
6. Works best for greenfield projects only — retrofitting is problematic
7. ~90% completion rate through automated loops
8. Operator skill (prompt engineering) is the critical success factor

## Pages Created/Updated
- [[geoffrey-huntley]] — Creator entity
- [[ralph-wiggum]] — Major expansion with original technical details

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-ghuntley-ralph-wiggum-original.md | Initial creation |
