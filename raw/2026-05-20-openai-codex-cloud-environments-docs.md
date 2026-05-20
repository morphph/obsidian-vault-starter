# OpenAI Codex Cloud / Web + Cloud Environments (Documentation)

**Sources:**
- https://developers.openai.com/codex/cloud
- https://developers.openai.com/codex/cloud/environments

**Publisher:** OpenAI Developers (official docs)
**Fetch date:** 2026-05-20
**Fetch method:** WebFetch

---

## Codex Web / Cloud Overview

Codex web is OpenAI's cloud-based coding agent for asynchronous task execution. Users can "delegate to Codex in the cloud" for background coding jobs, including parallel execution.

### Access

- ChatGPT.com/codex with connected GitHub account
- Eligibility: Plus / Pro / Business / Edu / Enterprise ChatGPT plans (some Enterprise workspaces need admin setup)

### Capabilities

- Codex "can read, edit, and run code" and create pull requests from completed work
- Tasks run in cloud environment
- Internet access can be configured (off by default for agent, on for setup)
- Background + parallel execution supported

### Triggers

- Direct request via Codex web interface
- GitHub integration: tagging `@codex` on issues / PRs
- Delegation from IDE extension

---

## Cloud Environments (configuration)

Codex Cloud environments enable unattended AI agent execution by providing customizable container configurations.

### Setup & dependencies

For projects using common package managers (`npm`, `yarn`, `pnpm`, `pip`, `pipenv`, `poetry`), Codex auto-installs dependencies and tools.

Custom bash scripts support complex setups; persist configuration to `~/.bashrc`.

### Secrets & variables

- Environment variables persist throughout task execution
- Secrets receive encrypted storage and are restricted to setup phases for security

### Network access

- Setup scripts: internet enabled
- Agent execution: internet defaults to off; can be configured for limited or unrestricted use via separate settings

### Container caching

> "Codex caches container state for up to 12 hours to speed up new tasks and follow-ups."

- Acceleration applies across team members on Business / Enterprise tiers
- Maintenance script can run when resuming cached containers to refresh deps on newer commits

### Execution flow

1. Repository checkout
2. Setup script execution (internet enabled)
3. Internet access configuration (per agent rules)
4. Agent loop execution with code edits + validation checks

---

## Comparison with Anthropic Claude Code cloud routines

| Dimension | Codex Cloud | Anthropic Cloud Routines |
|---|---|---|
| Runs unattended? | ✓ (autonomous mode) | ✓ |
| Laptop can be off? | ✓ | ✓ |
| Container caching | 12 hours cross-task | Per-routine (not explicitly bounded) |
| Network access | Configurable, off by default | Configurable, trusted network allows package install |
| Triggers | GitHub @codex / IDE delegate / direct web / automation cron | GitHub PR labels / HTTP POST / cron schedule (≥1 hour) |
| Output channel | PR created in repo + Triage inbox | PR created in repo + run history in claude.ai/code |
| Per-task isolation | Cloud container | Fresh `git clone` |
| Hooks support in cloud | Yes (project `.codex/hooks.json` commits to repo) | Yes (project `.claude/settings.json` commits to repo) |

**Verdict:** Functional parity. Differs in (a) trigger surface (Codex has built-in `@codex` GitHub mention; Anthropic uses labels), and (b) container caching is more explicitly documented in Codex.
