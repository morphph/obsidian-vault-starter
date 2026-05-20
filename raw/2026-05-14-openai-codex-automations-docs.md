# OpenAI Codex Automations (Documentation)

**Source:** https://developers.openai.com/codex/app/automations
**Publisher:** OpenAI Developers (official docs)
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Overview

Codex Automations let you "schedule recurring Codex tasks" that run in the background. The system automatically adds findings to a Triage inbox or archives tasks when there's nothing to report.

## Three automation types

### 1. Thread Automations
Heartbeat-style recurring wake-up calls attached to the **current thread**. Preserves conversation context.

**Use when:**
- Monitoring a long-running command until it finishes
- Polling Slack / GitHub / connected source where results should stay in the same thread
- Review loop reminders
- Skill-driven workflows with plugins
- Ongoing research / triage tasks

Intervals: minute-based for active loops, or daily/weekly check-ins.

### 2. Standalone Automations
Start fresh runs on a schedule; results reported to **Triage inbox**. No conversation history carried over.

**Use when:**
- Each run should be independent
- One automation should run across one or more projects
- Findings should appear as separate runs in Triage

### 3. Project-scoped Automations
Run within specific Git repositories — either locally or on a dedicated background worktree to isolate changes.

> "For project-scoped automations, the app needs to be running, and the selected project needs to be available on disk."

For Git repos: choose between local project execution (modifies active work files) or dedicated worktrees (isolates automation changes). Non-version-controlled projects run automations directly in the project directory.

## Scheduling

Standard intervals: daily, weekly, minute-based.

Custom cadence: "if you need a custom cadence, choose a custom schedule and enter cron syntax."

## Security / sandbox

Automations use default sandbox settings:
- **read-only**: tool calls fail for modifications, network access, app interactions
- **workspace-write**: file modifications within workspace
- **danger-full-access**: elevated risk; enterprise admins can restrict via `requirements.toml`

Automations use `approval_policy = "never"` when organizational policy permits — meaning no permission prompts during the run.

## Skill integration

Automations can invoke skills using `$skill-name` syntax. Skills can also create or update automations programmatically.

## Model / reasoning configuration

Users can specify model and reasoning effort explicitly, or use defaults.

## Future direction (per OpenAI Academy)

"Future versions will let Codex run continuously in the background using cloud-based triggers, so jobs could execute even when a developer's computer is off." — current standalone automations are already cloud-capable; project-scoped require local app running.

---

## Mapping to Claude Code stack

| Codex automation feature | Claude Code equivalent |
|---|---|
| Thread automation (heartbeat) | `/loop` skill (in-session scheduled tasks) |
| Standalone automation (Triage) | Cloud routines (claude.ai/code) |
| Project-scoped (local with worktree) | `claude --bg` background sessions |
| Cron syntax | Routine cron triggers |
| Skill invocation `$skill-name` | Plugin skills invocation |
| `approval_policy = "never"` unattended mode | Cloud routine no-permission-prompt mode |

**Coverage:** Codex Automations span all 3 tiers of Anthropic's deployment model (in-session / local background / cloud), with the same security caveats (autonomous mode requires hooks as guardrails).
