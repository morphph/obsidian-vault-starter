# Codex Use Case: Follow a Goal

**Source URL:** https://developers.openai.com/codex/use-cases/follow-goals
**Author:** OpenAI Developers (official Codex documentation)
**Estimated publish date:** ~2026-05-09 (likely concurrent with cookbook)
**Fetch date:** 2026-05-18
**Fetch method:** WebFetch
**Format:** Official Codex use-case documentation

---

## Overview

> "Use `/goal` when a task needs Codex to keep working across turns toward a verifiable stopping condition."

This is the **practical user-facing companion** to the more conceptual cookbook page. Cookbook explains the formalism; this page gives the action templates.

## When to Use Goals

Goals suit scenarios requiring:
- Extended coding work with clear success criteria
- Code migrations, large refactors, deployment loops
- Experiments and prototypes with validation loops
- Long-running tasks that can progress independently for hours

## 5-Step Setup Process

**Core principle**: Define what "done" means BEFORE starting.

1. **Name the objective and stopping condition** — be specific about the endpoint
2. **Point to source materials** — reference files, docs, issues, or plans Codex must read
3. **Define validation artifacts** — specify commands or outputs proving progress
4. **Request checkpoint reporting** — ask for compact status updates naming current progress, verified items, remaining work, and blockers
5. **Monitor via `/goal` commands** — check status, pause, resume, or clear as needed

**Basic syntax**: `/goal Complete [objective] without stopping until [verifiable end state].`

## Practical Examples (3 Templates)

### Code Migrations
```
/goal Migrate this project from [legacy stack] to [target stack]. 
Ensure all screens remain visually identical, using playwright 
interactive to verify.
```

### Prototype Development
```
/goal Implement PLAN.md, creating tests for each milestone and 
verifying output with playwright interactive.
```

### Prompt Optimization
```
/goal Optimize prompts in [file] until eval suite reaches [target 
score]. After each change, run [eval command], inspect failures, 
and keep edits minimal.
```

## Key Differences from Standard Usage

| Standard Codex | Goal-driven Codex |
|---|---|
| Concludes after one turn | Maintains context and autonomy across extended sessions |
| Requires manual steering per step | Independently validates progress against defined checkpoints |
| Output is conversational | Output is checkpoint reports + final state |
| User decides when to stop | Agent stops when condition met (or blocked) |

## Lifecycle Management

- **Enable**: Use `/experimental` or add `goals = true` in `config.toml`
- **Start**: `/goal <objective>`
- **Check**: `/goal` (view current objective)
- **Pause**: `/goal pause`
- **Resume**: `/goal resume`
- **Stop**: `/goal clear`

## Recommended Operational Patterns

1. **Compact progress reporting** — specify current checkpoint, what's been verified, what remains, whether Codex is blocked
2. **Tighten vague goals rather than adding ad hoc instructions mid-run** — don't patch with comments; rewrite the goal
3. **Let Codex work independently** — it stops when confident it has reached the stopping condition

## Comparison Notes

vs **Cookbook page** (Using Goals in Codex): cookbook is conceptual (6-element formalism); this page is templated (3 ready-to-use prompts).

vs **Claude Code /goal docs**: similar lifecycle, but Codex has explicit `pause`/`resume` (Claude doesn't); Claude's evaluator is transcript-only Haiku (Codex's eval model not stated).

vs **George (@nurijanian) PM template**: George's 6-section template is more elaborate than Codex's 5-step setup. George's adds explicit "negative cases" and "customer-facing success criteria" — the PM craft additions Codex official doesn't have.

## Key Tactical Insights

1. **"Tighten the goal" is the official OpenAI recommendation for mid-run drift** — don't add instructions, rewrite goal. This matches George's "stop and edit spec" calibration advice.
2. **Templates are scenario-flavored** (migration / prototype / prompt-optim) — OpenAI provides starting points, not abstract guidance.
3. **`playwright interactive` is mentioned twice** as the standard verification surface — implying browser-driven validation is the canonical "validation artifact" for UI work.
4. **Pause/resume is a 1st-class operation** in Codex — useful for "watch first loops" calibration (which George recommends but Claude /goal can't formally support).

## Source Authority

Official OpenAI Codex documentation. Authoritative. Companion to the cookbook page; both should be considered "official answer to how to use /goal" — cookbook for the formalism, this page for the practice.
