# Claude Code Official Docs — Automate work with routines

Captured 2026-05-14 from https://code.claude.com/docs/en/routines.md

> Put Claude Code on autopilot. Define routines that run on a schedule, trigger on API calls, or react to GitHub events from Anthropic-managed cloud infrastructure.

> [!note]
> Routines are in research preview.

A routine is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically. Routines execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed.

Each routine can have one or more triggers:
* **Scheduled**: recurring cadence (hourly, nightly, weekly) or once at specific future time
* **API**: HTTP POST to per-routine endpoint with bearer token
* **GitHub**: react to repository events (PRs, releases)

Single routine can combine triggers. PR review routine can run nightly, trigger from deploy script, and react to every new PR.

Available on Pro, Max, Team, Enterprise plans with Claude Code on the web enabled. Manage at claude.ai/code/routines or CLI `/schedule`.

Team/Enterprise admins can disable routines for all members via toggle.

## Example use cases

* **Backlog maintenance**: schedule trigger nightly, reads issues, applies labels, posts Slack summary
* **Alert triage**: monitoring tool calls routine's API endpoint when error threshold crossed, passing alert body as `text`. Routine correlates with recent commits, opens draft PR.
* **Bespoke code review**: GitHub trigger on `pull_request.opened`. Apply team's review checklist, inline comments, summary.
* **Deploy verification**: CD pipeline calls API endpoint after each production deploy. Smoke checks, scan error logs.
* **Docs drift**: schedule trigger weekly. Scan merged PRs, flag docs referencing changed APIs.
* **Library port**: GitHub trigger on `pull_request.closed` merged PRs in SDK repo. Port to parallel SDK in another language.

## Create a routine

From web (claude.ai/code/routines), Desktop app, or CLI. All three surfaces write to same cloud account.

Routines run autonomously as full Claude Code cloud sessions. No permission-mode picker. No approval prompts during run. Can run shell commands, use skills committed to cloned repo, call connectors.

What a routine can reach is determined by:
* Repositories you select + their branch-push setting
* Environment's network access and variables
* Connectors you include

Routines belong to individual claude.ai account. Not shared with teammates. Count against your daily run allowance. Commits/PRs carry your GitHub user.

### From web

1. Visit claude.ai/code/routines → New routine
2. Name + prompt (with model selector)
3. Select repositories (cloned at start of run from default branch; Claude creates `claude/`-prefixed branches)
4. Select environment (network access, env vars, setup script)
5. Select trigger (Schedule / GitHub event / API)
6. Review connectors and permissions
7. Create

### From CLI

```text
/schedule daily PR review at 9am
/schedule clean up feature flag in one week
```

CLI creates scheduled routines only. To add API or GitHub trigger, edit on web.

`/schedule list`, `/schedule update`, `/schedule run`.

## Configure triggers

### Schedule trigger

Presets: hourly, daily, weekdays, weekly. Times in your local zone, converted automatically.

For custom interval (every 2 hours, first of month): pick closest preset, then `/schedule update` to set specific cron. Minimum interval: 1 hour.

#### One-off run

Single time at specific timestamp:
```text
/schedule tomorrow at 9am, summarize yesterday's merged PRs
/schedule in 2 weeks, open a cleanup PR that removes the feature flag
```

After firing, auto-disables. To re-run, edit and set new one-off time.

One-off runs do NOT count against daily routine run cap. They draw from subscription usage like any other session.

### API trigger

Dedicated HTTP endpoint. POST with bearer token starts new session, returns session URL.

API triggers added from web. CLI cannot create or revoke tokens.

1. Edit routine on web → Add another trigger → API
2. Copy URL + Generate token (shown once, store securely)
3. Send token in `Authorization: Bearer` header

#### Trigger via curl

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

Response:
```json
{
  "type": "routine_fire",
  "claude_code_session_id": "session_01HJKLMNOPQRSTUVWXYZ",
  "claude_code_session_url": "https://claude.ai/code/session_01HJKLMNOPQRSTUVWXYZ"
}
```

`/fire` endpoint ships under `experimental-cc-routine-2026-04-01` beta header. Breaking changes ship behind new dated beta header versions; two most recent versions continue to work.

`text` field is freeform. If you send JSON, routine receives as literal string.

### GitHub trigger

Each matching event starts its own session. During research preview, per-routine and per-account hourly caps apply.

Configured from web UI only.

1. Edit routine → Add trigger → GitHub event
2. Install Claude GitHub App (separate from `/web-setup` which only grants repository access for cloning)
3. Configure: select repo, choose event, optional filters

#### Supported events

* Pull request (opened, closed, assigned, labeled, synchronized)
* Release (created, published, edited, deleted)

#### Filter pull requests

All conditions must match. Filter fields: Author, Title, Body, Base branch, Head branch, Labels, Is draft, Is merged.

Operators: equals, contains, starts with, is one of, is not one of, matches regex.

`matches regex` tests ENTIRE field value, not substring. To match titles containing `hotfix`: `.*hotfix.*`. For literal substring, use `contains`.

Example filter combinations:
* Auth module review: base branch `main`, head branch contains `auth-provider`
* Ready-for-review only: is draft = `false`
* Label-gated backport: labels include `needs-backport`

#### How sessions map to events

Each matching event starts new session. No session reuse for GitHub-triggered routines.

## Manage routines

Click routine → detail page. Shows repos, connectors, prompt, schedule, API tokens, GitHub triggers, past runs.

### View and interact with runs

Click run → opens as full session. See what Claude did, review changes, create PR, continue conversation.

> [!note]
> Green status = session started and exited without infrastructure error. Does NOT mean task succeeded. Open run to read transcript.

### Edit and control

* Run now (immediate start)
* Pause/resume schedule (toggle in Repeats section)
* Edit (pencil icon)
* Delete (past sessions remain)

### Repositories and branch permissions

Each repository cloned on every run. Claude starts from default branch.

By default Claude can only push to branches prefixed with `claude/`. To remove: enable "Allow unrestricted branch pushes" for that repository.

### Connectors

Connectors = claude.ai integrations on your account. MCP servers added locally with `claude mcp add` are on machine, not claude.ai account. To use one in routine, add as connector at claude.ai/customize/connectors, or declare in committed `.mcp.json`.

When you create routine, all currently connected connectors included by default.

### Environments and network access

Each routine runs in cloud environment that controls network access, env vars, setup scripts.

Default environment uses **Trusted** network access: default allowlist of package registries, cloud provider APIs, container registries, common development domains. Arbitrary domains NOT reachable (403 with `x-deny-reason: host_not_allowed`).

MCP connector traffic routed through Anthropic's servers, so connectors work without adding hosts to Allowed domains.

To allow additional domains: Edit routine → environment selector → settings → Update cloud environment → Network access → Custom → Allowed domains.

## Usage and limits

Routines draw down subscription usage like interactive sessions. Plus daily cap on routine runs per account.

When routine hits daily cap or subscription limit, organizations with extra usage enabled can keep running on metered overage.

One-off runs do not count against daily routine cap.

## Troubleshooting

### "Routines are disabled by your organization's policy"

Team/Enterprise admin has turned off Routines toggle. Server-side org setting, cannot be overridden locally. Contact admin.

## Related resources

* `/loop` and in-session scheduling: schedule local tasks within open CLI session
* Desktop scheduled tasks: local on machine, access to files
* Cloud environment: runtime for cloud sessions
* MCP connectors: external services
* GitHub Actions: run Claude in CI on repo events
