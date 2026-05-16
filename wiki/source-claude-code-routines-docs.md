---
type: source-summary
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-14-anthropic-claude-code-routines.md
tags: [claude-code, official-docs, routines, cloud, schedule, github-trigger, api-trigger, research-preview]
---

# Source: Automate work with routines (cloud-hosted unattended Claude Code)

## Summary
Official Anthropic doc on **routines** — saved [[claude-code]] configurations (prompt + repos + connectors) that run autonomously on Anthropic-managed cloud infrastructure. Keep working when your laptop is closed. Each routine can have one or more triggers: **scheduled (cron), API (HTTP POST + bearer token), or GitHub event** (PR/release). The cloud-hosted answer to "I want Claude to do this unattended" that [[source-claude-code-scheduled-tasks-docs|`/loop`]] can't deliver. **Available on Pro, Max, Team, Enterprise plans with Claude Code on the web enabled.** Research preview.

## When to use routines vs `/loop` vs Desktop tasks

|  | Routines (this doc) | [[source-claude-code-scheduled-tasks-docs\|`/loop`]] | Desktop tasks |
| :--- | :--- | :--- | :--- |
| Runs on | **Anthropic cloud** | Your machine | Your machine |
| Requires machine on | **No** | Yes | Yes |
| Requires open session | **No** | Yes | No |
| Access to local files | **No** (fresh clone) | Yes | Yes |
| MCP servers | claude.ai connectors per task | Inherits from session | Config + connectors |
| Permission prompts | **None — autonomous** | Inherits from session | Configurable |
| Minimum interval | 1 hour | 1 minute | 1 minute |
| Triggers | **Schedule + API + GitHub** | Schedule only | Schedule only |

## Trigger types

### Schedule trigger
Presets: hourly, daily, weekdays, weekly. Times in local zone, converted automatically. Custom intervals via `/schedule update` to set cron expression. Minimum: 1 hour.

### One-off run (sub-type of schedule)
Single time at specific timestamp:
```text
/schedule tomorrow at 9am, summarize yesterday's merged PRs
/schedule in 2 weeks, open a cleanup PR that removes the feature flag
```

After firing, auto-disables. **One-off runs do NOT count against daily routine cap.**

### API trigger
Dedicated HTTP endpoint per routine. POST with bearer token starts new session.

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

Returns:
```json
{
  "type": "routine_fire",
  "claude_code_session_id": "session_01HJKLMNOPQRSTUVWXYZ",
  "claude_code_session_url": "https://claude.ai/code/session_01HJKLMNOPQRSTUVWXYZ"
}
```

The `text` field is **freeform** — JSON or other structured payload received as literal string.

API triggers configured from **web only**. CLI cannot create/revoke tokens. `/fire` endpoint ships under `experimental-cc-routine-2026-04-01` beta header. Breaking changes ship behind new dated headers; two most recent versions continue to work.

### GitHub trigger
Each matching event starts its own session. Per-routine and per-account hourly caps during research preview.

Supported events:
- Pull request (opened, closed, assigned, labeled, synchronized)
- Release (created, published, edited, deleted)

Filter fields: Author, Title, Body, Base branch, Head branch, Labels, Is draft, Is merged. Operators: equals/contains/starts with/is one of/matches regex.

> [!warning]
> `matches regex` operator tests **ENTIRE field value**, not substring. Match titles containing `hotfix` → use `.*hotfix.*`. For literal substring, use `contains`.

Requires installing the **Claude GitHub App** on the repository — `/web-setup` grants cloning access only, NOT webhook delivery.

## Architecture — autonomous cloud session

Routines run as full Claude Code cloud sessions with:
- **No permission-mode picker, no approval prompts** during run
- Can run shell commands, use skills committed to cloned repo, call connectors
- Each run = new session viewable in claude.ai/code

What a routine can reach is determined by:
- Repos you select + branch-push setting (default: only `claude/`-prefixed branches)
- Environment's network access + env vars
- Connectors included

Routines belong to **individual claude.ai account** — commits/PRs carry your GitHub user; Slack/Linear actions use your linked accounts.

## Environment + network access

Default environment: **Trusted network access** = default allowlist of package registries + cloud provider APIs + container registries + dev domains. Arbitrary domains return `403` with `x-deny-reason: host_not_allowed`.

MCP connector traffic routed through Anthropic's servers — connectors work without adding hosts to Allowed domains.

To allow additional domains: edit routine → environment settings → Network access → Custom → Allowed domains.

## Connectors vs locally-added MCP servers

> [!warning]
> Connectors are **claude.ai integrations on your account** (at claude.ai/customize/connectors). MCP servers you added locally with `claude mcp add` are stored on your machine and **do NOT appear in routines' connector list**.

To use a local MCP server in a routine: add it as connector on claude.ai, or declare in committed `.mcp.json` so it's part of cloned repo.

## Usage and limits

Routines draw down subscription usage like interactive sessions. Plus **daily cap on routine runs per account**. Beyond cap: organizations with extra usage enabled run on metered overage. Without extra usage: rejected until window resets.

One-off runs exempt from daily routine cap (draw from regular subscription only).

## "Green status" gotcha

> [!warning]
> Green status in run list = session started + exited without **infrastructure** error. Does NOT mean task succeeded. Open run to read transcript. Blocked network requests, missing connector tools, task-level failures all surface there.

## Connection to our `/schedule` skill

The `/schedule` slash command (which appears in my user-invocable skills) creates routines specifically — it's the conversational entry point to this exact system. The `routines` term is the underlying primitive that `/schedule` produces.

## Connections
- Related: [[claude-code]], [[source-claude-code-scheduled-tasks-docs]], [[claude-managed-agents]], [[source-claude-code-mcp-docs]], [[source-claude-code-channels-docs]], [[managed-agents-architecture]]
- Cloud-hosted sibling of [[source-claude-code-scheduled-tasks-docs|`/loop`]]; together they cover the "scheduling Claude Code" surface
- Architectural sibling of [[claude-managed-agents]] — both run Claude on Anthropic infrastructure, but routines are saved-configuration triggered, Managed Agents are programmatic-API spawned

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-14-anthropic-claude-code-routines.md | Initial creation — new cloud automation primitive |
