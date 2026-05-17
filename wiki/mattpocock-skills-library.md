---
type: entity
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
tags: [wiki, skills, claude-code, library]
---

# mattpocock/skills (Skills For Real Engineers)

## Summary
Matt Pocock's open-sourced `.claude/` skills directory: 86,997 stars / 7,583 forks. The most-starred Claude Code skill library. Designed to fix four common failure modes of coding agents using engineering fundamentals encoded as composable prompts. Distributed via `npx skills@latest add mattpocock/skills` and as a Claude Code plugin.

## Details

### Install
```bash
npx skills@latest add mattpocock/skills
# Then in your agent: /setup-matt-pocock-skills
```

Setup asks: which issue tracker (GitHub/Linear/local), what triage labels, where to save docs.

### The Four Failure Modes (designed against)
1. **Agent didn't do what I want** → misalignment → fix with `/grill-me` or `/grill-with-docs`
2. **Agent is too verbose** → no shared vocabulary → fix with CONTEXT.md (built into `/grill-with-docs`)
3. **Code doesn't work** → no feedback loops → fix with `/tdd` and `/diagnose`
4. **Built a ball of mud** → no design investment → fix with `/to-prd`, `/zoom-out`, `/improve-codebase-architecture`

### The 5-Skill Production Loop
```
/grill-with-docs  →  /to-prd  →  /to-issues  →  /tdd  →  /improve-codebase-architecture
       ↑                                                              │
       └──────────────────────────────────────────────────────────────┘
```
Each skill's output is the next's input. The architecture-cleanup back-edge is non-negotiable — skip it and quality monotonically degrades.

### Full Catalog

**Engineering (daily code use)**
- [[grill-with-docs]] — keystone discovery + CONTEXT.md + ADRs
- `/grill-me` — non-code variant (productivity)
- `/to-prd` — turn current conversation into PRD as GitHub issue (no interview — synthesizes)
- `/to-issues` — break plan/PRD into vertical-slice issues with [[hitl-vs-afk-classification|HITL/AFK]] labels
- `/tdd` — red-green-refactor TDD per vertical slice (Matt: "most consistent way to improve agent outputs")
- `/diagnose` — disciplined bug/perf diagnosis loop
- `/improve-codebase-architecture` — deletion test, deepen shallow modules, run every few days
- `/triage` — state-machine issue triage
- `/zoom-out` — make agent give system-level perspective
- `/prototype` — throwaway prototype: runnable terminal app (logic) OR multiple UI variations (presentation)
- `/setup-matt-pocock-skills` — per-repo config bootstrap

**Productivity**
- `/caveman` — ~75% token reduction while keeping accuracy
- `/grill-me` — interview about any plan/design (non-code)
- `/handoff` — compact conversation for another agent
- `/write-a-skill` — meta-skill for creating new skills

**Misc**
- `/git-guardrails-claude-code`, `/migrate-to-shoehorn`, `/scaffold-exercises`, `/setup-pre-commit`

### Design Philosophy
Matt explicitly contrasts with GSD / BMAD / Spec-Kit:
- Those "own the process" — take control from developer, hard to debug
- His skills are **small, composable, model-agnostic**
- Built on decades of engineering fundamentals (DDD, XP, TDD, Pragmatic Programmer)
- "Hack around with them. Make them your own."

### Skill Structure (progressive disclosure exemplar)
Each engineering skill ships with multiple supporting MD files:
- `SKILL.md` — short triggers and main instructions
- Supporting files — detailed rules loaded only when needed

Example `/tdd`:
```
tdd/
├── SKILL.md
├── deep-modules.md
├── interface-design.md
├── mocking.md
├── refactoring.md
└── tests.md
```

### Governance Pattern: `.out-of-scope/`
Root-level `.out-of-scope/` folder documents intentional non-features with rationale (e.g., `mainstream-issue-trackers-only.md`). Prevents repeat discussions of declined features. **Worth copying to any well-maintained repo.**

### `/to-issues` HITL/AFK Labeling
Critical for autonomous workflows: each issue gets labeled HITL (needs human decisions) or AFK (agent-executable). The AFK queue is what feeds Ralph loops. See [[hitl-vs-afk-classification]].

### Vertical Slicing
`/to-issues` breaks work into vertical slices (schema + API + UI + tests per issue), NOT horizontal layers. Each slice is independently shippable, surfaces unknowns early, enables parallel agents. See [[vertical-slicing]].

## Connections
- Owner: [[matt-pocock]]
- Keystone skill: [[grill-with-docs]]
- AFK execution layer: [[sandcastle]]
- Related concepts: [[agent-skills-standard]], [[skill-as-method-call]], [[thin-harness-fat-skills]], [[skillify-meta-skill]]
- Workflow integration: [[idea-to-afk-agent-flow]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Skills repo + AI Hero article + Aditya walkthrough | Initial creation |
