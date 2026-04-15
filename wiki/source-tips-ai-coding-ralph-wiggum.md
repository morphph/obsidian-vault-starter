---
type: source-summary
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
tags: [wiki, source]
---

# Source: 11 Tips For AI Coding With Ralph Wiggum

## Summary
Matt Pocock's comprehensive practical guide on the [[ralph-wiggum]] pattern — autonomous AI coding loops where the agent chooses tasks from a PRD and works unsupervised. Covers 11 tips spanning loop mechanics, HITL/AFK modes, scope definition, progress tracking, feedback loops, task sizing, prioritization, quality standards, Docker sandboxes, cost, and customization.

## Source Details
- **URL**: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
- **Author**: [[matt-pocock|Matt Pocock]] (AI Hero)
- **Date**: 2026-04 (approximate)
- **Type**: Long-form article / practical guide

## Key Claims
1. AI coding evolution: vibe coding → planning → multi-phase plans → Ralph (autonomous loop)
2. The agent choosing the task (not human) is the key shift from multi-phase plans
3. HITL first to build trust, AFK once prompt is solid — always cap iterations
4. PRD with JSON `passes` field (from Anthropic research) as living TODO list
5. `progress.txt` short-circuits exploration — agent reads state instead of re-exploring repo
6. Feedback loops are non-negotiable: types, tests, linting, pre-commit hooks block bad commits
7. Smaller tasks = higher quality due to [[context-rot]] (LLM output degrades as context fills)
8. Prioritize risky/architectural tasks first; save easy wins for later
9. "The repo wins" — agents amplify existing code patterns, good or bad ([[software-entropy]])
10. Docker sandboxes essential for AFK safety
11. Open-source local models not yet good enough for Ralph; "golden age" where AI outpaces human wages

## Pages Created
- [[ralph-wiggum]] — The autonomous loop pattern
- [[matt-pocock]] — Author entity
- [[software-entropy]] — AI-accelerated codebase deterioration

## Pages Updated
- [[harness-design]] — Expanded Ralph Loop section
- [[orchestration-loop]] — Added Ralph as concrete implementation
- [[verification-loops]] — Added Ralph feedback loop context
- [[context-anxiety]] — Added context rot as related term

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Initial creation |
