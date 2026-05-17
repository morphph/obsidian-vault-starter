---
type: entity
created: 2026-04-15
last-updated: 2026-05-17
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-15-aihero-getting-started-with-ralph.md
  - raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
  - raw/2026-05-17-repo-mattpocock-sandcastle.md
  - raw/2026-05-17-mattpocock-chapter-creator-thread.md
  - raw/2026-05-17-aihero-5-agent-skills.md
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
tags: [wiki, person, builder]
---

# Matt Pocock

## Summary
Developer and content creator behind AI Hero (aihero.dev). One of the most influential voices in Claude Code methodology — author of the most-starred Claude Code skills library ([[mattpocock-skills-library]], 87K stars), creator of [[sandcastle]] (the AFK orchestration framework, 4.5K stars), and originator of the [[idea-to-afk-agent-flow]] methodology. Also authored the definitive practical guide on the [[ralph-wiggum]] autonomous coding pattern.

## Details

### Three Major Open-Source Drops (2026)
1. **[[mattpocock-skills-library]]** — 87K stars, 7.6K forks. Personal `.claude/` directory open-sourced. 5 engineering skills + 4 productivity + misc. The reference for "skills for real engineers."
2. **[[sandcastle]]** — `@ai-hero/sandcastle`, 4.5K stars. TypeScript framework for orchestrating AFK coding agents in Docker/Podman/Vercel sandboxes. `sandcastle.run()` as the AFK primitive.
3. **[[idea-to-afk-agent-flow]]** — methodology (his 6-step chapter-creator tweet is the seed text). End-to-end recipe for going from fuzzy idea to autonomous agent.

### Engineering Methodology
- The "skills for real engineers" thesis: skills should be small, composable, model-agnostic; encode engineering fundamentals (DDD, XP, TDD), not vibe-code generators
- Four-failure-modes framework: misalignment / verbosity / no feedback / ball-of-mud — each maps to specific skills
- 5-skill production loop: `/grill-with-docs` → `/to-prd` → `/to-issues` → `/tdd` → `/improve-codebase-architecture` (closed loop with architecture-cleanup back-edge)
- Vertical slicing as unit of work ([[vertical-slicing]])
- HITL/AFK per-issue labeling ([[hitl-vs-afk-classification]])
- Interactive→AFK escalation as the canonical pattern (Sandcastle's `createWorktree()` API)

### Ralph Contributions
- Practical 11-tip framework for running autonomous loops
- HITL → AFK progression model
- "The repo wins" principle ([[software-entropy]])
- Alternative loop types (test coverage, linting, entropy reversal)
- JSON PRD with `passes: false` as living TODO
- "Context rot" terminology

### Original Projects
- AI Hero — newsletter (~60K devs) and educational content
- AI Hero CLI — used Ralph to add tests (16% → 100% coverage)
- Course Video Manager — Ralph-built; the `course-video-manager` repo demonstrates `materialization cascade` term from CONTEXT.md
- `evalite`, `software-factory` (`.factory/` pattern inside sandcastle)

### Working Setup
- On Anthropic 5x Max plan (~$90/mo), mostly HITL usage with occasional AFK
- Built CLI to ping via WhatsApp when Ralph loops finish — reduces context switching
- Typical loops run 30-45 minutes; can run for hours

### Public Education
- Viral X thread on Ralph (Jan 5, 2026): 204K views, 2.5K likes, 4.8K bookmarks — "Ship while you kip"
- Ran a half-day live Ralph workshop (Feb 11, 2026) — 40 developers, $199
- Chapter-creator tweet (May 2026): seed text for [[idea-to-afk-agent-flow]] runbook
- Cohort: "Claude Code for Real Engineers" (aihero.dev)

### Influence Signal
- 87K stars on skills repo puts him in top tier alongside Garry Tan's GBrain/GStack
- ~60K newsletter subs
- Multiple third-party walkthroughs (Aditya Puri 2026-05, Tosea.ai, knightli.com)
- Cited by Anthropic engineers (Thariq) in adjacent ecosystem discussions

## Connections
- Major projects: [[mattpocock-skills-library]], [[sandcastle]]
- Skills authored: [[grill-with-docs]] (keystone)
- Methodology: [[idea-to-afk-agent-flow]]
- Concepts coined/popularized: [[hitl-vs-afk-classification]], [[vertical-slicing]], [[context-md-pattern]]
- Related: [[ralph-wiggum]], [[claude-code]], [[software-entropy]]
- Adjacent: [[geoffrey-huntley]] (Ralph creator), [[boris-cherny]] (Claude Code creator), [[garry-tan]] (GBrain/GStack parallel), [[thariq]] (Anthropic insider)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Initial creation |
| 2026-04-15 | raw/2026-04-15-aihero-getting-started-with-ralph.md | Added quickstart guide |
| 2026-04-15 | raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md | Added viral X thread (204K views) |
| 2026-05-17 | raw/2026-05-17-repo-mattpocock-skills.md | MAJOR refresh — added mattpocock/skills library (87K stars), 5-skill workflow, 4-failure-modes framework |
| 2026-05-17 | raw/2026-05-17-repo-mattpocock-sandcastle.md | Added Sandcastle AFK orchestration framework (4.5K stars) |
| 2026-05-17 | raw/2026-05-17-mattpocock-chapter-creator-thread.md | Added chapter-creator tweet as seed for idea-to-afk-agent-flow methodology |
| 2026-05-17 | raw/2026-05-17-aihero-5-agent-skills.md + raw/2026-05-17-adityapuri-matt-pocock-5-skills.md | Added 5-skill workflow details + third-party validation |
| 2026-05-17 | raw/2026-05-17-mattpocock-grill-with-docs-skill.md + raw/2026-05-17-aihero-grill-with-docs-changelog.md | Added grill-with-docs as keystone skill + DDD lineage |
