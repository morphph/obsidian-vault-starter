# mattpocock/skills

**Source:** https://github.com/mattpocock/skills
**Author/Org:** Matt Pocock (mattpocock)
**Stars:** 86,997 | **Forks:** 7,583 | **Language:** Shell | **Last updated:** 2026-05-17
**Fetch method:** GitHub Deep Scan (gh CLI)
**Fetched:** 2026-05-17

## What It Does

Matt Pocock's personal `.claude/` skills directory, open-sourced. "Skills for Real Engineers — not vibe coding." Designed to fix common failure modes of Claude Code, Codex, and other coding agents.

Approach contrast: GSD, BMAD, Spec-Kit own the process and take away control. These skills are small, composable, model-agnostic — built on decades of engineering experience. Hack around with them.

## Install

```bash
npx skills@latest add mattpocock/skills
```

After install, run `/setup-matt-pocock-skills` — asks: which issue tracker (GitHub/Linear/local), what triage labels, where to save docs.

## Why These Skills Exist — The Four Failure Modes

### #1 The agent didn't do what I want
**Problem:** Misalignment. Communication gap between you and agent.
**Fix:** `/grill-me` (non-code) or `/grill-with-docs` (code). Detailed questioning before any work. Matt's most popular skills.

### #2 The agent is way too verbose
**Problem:** Agents speak generic; teams have jargon. Quote: Eric Evans on ubiquitous language from DDD.
**Fix:** Shared language in `CONTEXT.md`. Built into `/grill-with-docs`.
**Concrete example:** "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)" → "There's a problem with the materialization cascade." Concision pays off session after session.
**Benefits:** consistent naming, easier navigation, fewer tokens spent thinking.

### #3 The code doesn't work
**Problem:** Without feedback loops on actual execution, agent flies blind.
**Fix:** Static types, browser access, automated tests. Specifically red-green-refactor TDD. Skills: `/tdd`, `/diagnose`.

### #4 We built a ball of mud
**Problem:** Agents accelerate software entropy. Codebases get complex at unprecedented rate.
**Fix:** Care about design every day. Skills: `/to-prd` (quizzes which modules touched), `/zoom-out` (system context), `/improve-codebase-architecture` (run every few days).

## Skill Catalog

### Engineering (daily code use)
- **diagnose** — Disciplined diagnosis loop: reproduce → minimise → hypothesise → instrument → fix → regression-test
- **grill-with-docs** — Grilling + CONTEXT.md + ADRs inline (THE keystone)
- **triage** — Issues through state machine of triage roles
- **improve-codebase-architecture** — Find deepening opportunities, informed by CONTEXT.md and ADRs
- **setup-matt-pocock-skills** — Per-repo config (issue tracker, labels, doc layout)
- **tdd** — Red-green-refactor; one vertical slice at a time
- **to-issues** — Break plan/spec/PRD into independently-grabbable GitHub issues using vertical slices
- **to-prd** — Turn current conversation into PRD as GitHub issue (no interview — just synthesizes)
- **zoom-out** — Tell agent to give broader system context
- **prototype** — Build throwaway prototype: runnable terminal app (logic) OR multiple radically different UI variations toggleable from one route

### Productivity
- **caveman** — Ultra-compressed communication; ~75% token reduction while preserving accuracy
- **grill-me** — Relentless interview about plan/design until every decision-tree branch resolved
- **handoff** — Compact conversation into handoff doc for another agent
- **write-a-skill** — Create new skills (progressive disclosure, bundled resources)

### Misc
- git-guardrails-claude-code, migrate-to-shoehorn, scaffold-exercises, setup-pre-commit

### Personal
- edit-article, obsidian-vault

## File Tree Highlights

```
.claude-plugin/plugin.json       # Distributed as Claude Code plugin
CLAUDE.md                        # Repo-level instructions
CONTEXT.md                       # Skills' OWN ubiquitous language doc
docs/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md
.out-of-scope/                   # Deliberate non-features (interesting governance pattern)
skills/engineering/
  diagnose/{SKILL.md, scripts/hitl-loop.template.sh}
  grill-with-docs/{SKILL.md, CONTEXT-FORMAT.md, ADR-FORMAT.md}
  improve-codebase-architecture/{SKILL.md, DEEPENING.md, INTERFACE-DESIGN.md, LANGUAGE.md}
  prototype/{SKILL.md, LOGIC.md, UI.md}
  setup-matt-pocock-skills/{SKILL.md, domain.md, issue-tracker-{github,gitlab,local}.md, triage-labels.md}
  tdd/{SKILL.md, deep-modules.md, interface-design.md, mocking.md, refactoring.md, tests.md}
  triage/{SKILL.md, AGENT-BRIEF.md, OUT-OF-SCOPE.md}
skills/in-progress/{review, writing-beats, writing-fragments, writing-shape}
skills/deprecated/{design-an-interface, qa, request-refactor-plan, ubiquitous-language}
```

Pattern notes:
- Each engineering skill ships with multiple supporting MD files (progressive disclosure)
- `.out-of-scope/` folder documents intentional non-features — governance pattern
- `skills/in-progress/` shows the writing-skills cluster he's building next
- `skills/deprecated/ubiquitous-language` — predecessor of grill-with-docs

## Quality Engineering Quotes Embedded in README

- David Thomas & Andrew Hunt (Pragmatic Programmer): "No-one knows exactly what they want"
- Eric Evans (DDD): "With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model"
- Kent Beck (XP): "Invest in the design of the system every day"
- John Ousterhout (Philosophy of Software Design): "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface"

Matt is intentionally framing skills as condensed engineering fundamentals, not vibe coding.

## Repo Vitals

- **Stars: 86,997 | Forks: 7,583** — top-tier popularity (rivals GBrain/GStack territory)
- Primary language: Shell (skills.sh installer)
- Active: last update same day as fetch (2026-05-17)
- Distributed via npx + Claude Code plugin
