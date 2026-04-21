---
type: entity
created: 2026-04-19
last-updated: 2026-04-21
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
tags: [wiki, product, open-source, skills, agentic]
---

# GStack

## Summary
[[garry-tan|Garry Tan]]'s open-source **coding/skills layer** for Claude Code — the "fat skills in markdown" layer from [[thin-harness-fat-skills]]. **78,692 stars on GitHub** (2026-04-21, up from 72K in the April 15 article). 23 specialist skills that turn Claude Code into a virtual engineering team: CEO, Eng Manager, Senior Designer, Staff Engineer, QA Lead, CSO, Release Engineer, SRE, Debugger. **Template-based generation compiles to 10 agent runtimes** (Claude Code, Codex, Cursor, Factory, OpenCode, Slate, Kiro, Hermes, GBrain, OpenClaw) — the first cross-vendor proof of the [[agent-skills-standard|Agent Skills standard]].

## Details

### What it is
- Library of reusable fat skills written as markdown files
- Each skill is a procedure with parameters (TARGET / QUESTION / DATASET) — see [[skill-as-method-call]]
- Designed to call [[gbrain|GBrain]]'s knowledge layer (`gbrain search` is referenced in Garry's trigger eval examples)
- Runs under any thin harness that executes markdown skills: [[claude-code]], [[openclaw]], Hermes Agent

### Why "fat" matters
Garry's architectural claim: in the 2026 stack, **90% of value lives in skills**, not in harnesses or models. [[thin-harness-fat-skills]]. A skill is not a prompt; it's a codified procedure that:
- Gets re-used across 100s of invocations
- Automatically improves with every model release (model is the runtime; skill is the program)
- Can be moved between harnesses without rewriting — it's just markdown

### Traction signal
72K+ GitHub stars is in the same league as large AI-tooling repos. Suggests that the fat-skills pattern has found product-market fit among AI builders.

### Garry's three-project stack
| Layer | Project | What it owns |
|-------|---------|--------------|
| Harness | [[openclaw|OpenClaw]] / Hermes Agent | Event loop, sessions, crons |
| **Skills** | **GStack** | **Reusable markdown procedures** |
| Knowledge | [[gbrain|GBrain]] | Filing rules, resolver, compiled memory |

### Relationship to Claude Code
Claude Code's native "skills" concept (skill descriptions as [[resolvers|resolver]] entries) is the same primitive. GStack is a curated library of skills that plug into that primitive — fat skills that have been hardened across many production runs.

### The 23-skill specialist roster (2026-04-21 Deep Scan)

**Planning (the sprint front-end):**
- `/office-hours` — YC Office Hours: 6 forcing questions that reframe your product
- `/plan-ceo-review` — CEO review: find the 10-star product hiding in the request
- `/plan-eng-review` — Eng Manager: lock architecture, data flow, edge cases, tests
- `/plan-design-review` — Senior Designer: rate each dimension 0-10, AI-slop detection
- `/plan-devex-review` — DX Lead: TTHW benchmarking, onboarding friction map
- `/autoplan` — CEO → design → eng pipeline (auto-review)
- `/design-consultation` — Design Partner: full design system
- `/design-shotgun` — 4-6 AI mockup variants with taste memory
- `/design-html` — Production HTML from mockup (not demo)

**Execution (the sprint middle):**
- `/review` — Staff Engineer: finds bugs that pass CI but break in prod
- `/investigate` — Debugger: root cause, no-fix-without-investigation
- `/design-review` — audit + fix loop with atomic commits
- `/devex-review` — live onboarding test, compares against plan-devex-review scores
- `/qa` — QA Lead: opens real browser, finds bugs, fixes, re-verifies
- `/qa-only` — same methodology, report-only
- `/pair-agent` — multi-agent browser sharing via ngrok

**Shipping (the sprint back-end):**
- `/cso` — Chief Security Officer: OWASP + STRIDE, 17 false-positive exclusions
- `/ship` — Release Engineer: tests + PR
- `/land-and-deploy` — merge → CI → deploy → verify
- `/canary` — post-deploy monitoring loop
- `/benchmark` — performance regression detection
- `/document-release` — doc sync
- `/retro` — weekly engineering retrospective

**Safety skills:** `/careful`, `/freeze`, `/guard`, `/unfreeze`

### The 10-host template system (the portability breakthrough)
**SKILL.md files are GENERATED from `.tmpl` templates.** `bun run gen:skill-docs --host <agent>` produces the per-runtime variant:

| Agent | Flag | Install dir |
|-------|------|-------------|
| Claude Code | (default) | `~/.claude/skills/gstack-*/` |
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |
| OpenClaw | (via ACP / ClawHub) | native install |

One source of truth. 10 runtimes. **This is the first concrete proof that the [[agent-skills-standard|Agent Skills open standard]] generalizes beyond Anthropic.**

### Team mode — version governance without git submodules
> `./setup --team` + `gstack-team-init required` → teammates get gstack on first Claude Code session. Auto-update check throttled to once/hour, network-failure-safe, completely silent.
>
> **No vendored files, no version drift, no manual upgrades.**

Blueprint for how this vault could distribute skills to forks without shipping copies.

### Karpathy quote (README opens with it)
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — Andrej Karpathy, No Priors podcast, March 2026

Garry's claim: 2026 logical-lines-per-day run rate is **~810× his 2013 Bookface-era pace** (11,417 vs 14). Methodology in `docs/ON_THE_LOC_CONTROVERSY.md` (AI-inflation-corrected, 40 repos).

### Test tiers (free vs paid, gate vs periodic)
| Tier | Cost | When it runs |
|------|------|--------------|
| Gate | Free, <5s | Every commit (CI default) |
| Periodic | ~$4/run | Weekly cron or manual |
| Diff-based selection | — | Only tests impacted by the diff |

`test/helpers/touchfiles.ts` maps each test to its file dependencies. This is how you make expensive LLM evals affordable in CI.

### For this vault
The `.claude/commands/` slash commands in this repo are already fat-ish skills. GStack represents a mature library worth surveying for patterns — especially:
- **Skill structure**: name, when-to-use paragraph, clear output contract
- **Sprint composition**: skills that feed each other (`/office-hours` → `/plan-ceo-review` → `/plan-eng-review` → `/review` → `/qa` → `/ship`)
- **Safety skills as advisories**: `/careful` / `/freeze` aren't hooks; they add inline prose Claude respects
- **Diff-based test selection**: apply to our `/lint` so cheap-validation runs on every edit but expensive checks only run when relevant

## Connections
- Related: [[garry-tan]], [[gbrain]], [[openclaw]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[resolvers]], [[agent-skills-standard]], [[claude-code]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Major expansion from GitHub Deep Scan: 78,692 stars; 23-skill specialist roster; 10-host template system (first cross-vendor Agent Skills proof); team mode auto-update; Karpathy quote + 810× productivity claim; gate-vs-periodic test tiers |
