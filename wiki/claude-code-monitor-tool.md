---
type: concept
created: 2026-04-11
last-updated: 2026-04-11
sources:
  - raw/claude-code-monitor-tool-docs-2026-04.md
tags: [claude-code, tool, event-driven, automation]
---

# Claude Code Monitor Tool

## Summary
Built-in [[claude-code]] tool (v2.1.98, April 9 2026) that transforms the agent loop from time-driven polling to event-driven automation. Runs a shell command in the background; each stdout line becomes a notification that wakes the session. Zero token cost when nothing happens.

## Details
- **Core shift:** Before Monitor, background watching required `/loop` or `CronCreate` — both fire a full API call per interval just to ask "did anything happen?" Monitor inverts this: Claude watches and reacts only when an event arrives.
- **How it works:** Launches a shell command whose stdout becomes an event stream. Lines arriving within 200ms batch into a single notification. Stderr captured to file but doesn't trigger events.
- **Four parameters:**
  - `description` — short label shown in notifications (e.g., "errors in deploy.log")
  - `command` — shell script generating the event stream
  - `timeout_ms` — auto-kill duration (default 300,000ms / 5min, max 3,600,000ms / 1hr)
  - `persistent` — boolean; `true` keeps the monitor running for the full session
- **Two patterns:**
  - **Stream filters** — watch continuous output, surface matching lines:
    ```bash
    tail -f /var/log/app.log | grep --line-buffered "ERROR"
    inotifywait -m --format '%e %f' /watched/dir
    ```
  - **Poll-and-if filters** — check a source at intervals, emit only on change:
    ```bash
    while true; do
      gh api "repos/owner/repo/issues/123/comments?since=$last" \
        --jq '.[] | "\(.user.login): \(.body)"'
      last=$now; sleep 30
    done
    ```
- **Three critical rules:**
  1. Always use `grep --line-buffered` in pipes — without it, buffering delays events by minutes
  2. Handle transient failures with `|| true` to prevent one timeout killing the monitor
  3. Be selective with output — every line costs a conversation message; auto-stops on excessive events
- **Token economics:** `/loop` checking tests every 2 min over 10 min = 5 full API calls. Monitor: failure line pushes into session instantly, Claude starts fixing while remaining tests still run. Zero wasted calls.
- **Use cases:** dev server monitoring, test suite triage, CI/CD watching, PR polling, log monitoring
- **Permissions:** Same rules as Bash — `allow` and `deny` patterns apply
- **Availability:** Not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry
- **Announced by:** Noah Zweben (@noahzweben), Claude Code PM

## Monitor vs. Alternatives
| Mechanism | Trigger | Best for |
|-----------|---------|----------|
| **Hooks** | Claude's own actions (pre/post edit, commit) | Internal event reactions |
| **CronCreate** (Scheduled Tasks) | Fixed time intervals | Periodic checks |
| **Monitor** | External events (stdout lines) | Real-time output reaction |
| **Bash run_in_background** | Completion only (fire-and-forget) | One-shot background tasks |

## Connections
- Related: [[claude-code]], [[orchestration-loop]], [[forked-agent-pattern]], [[prompt-cache-optimization]], [[query-loop]]
- Monitor extends the [[forked-agent-pattern]] — background process with event-driven wakeup
- Token savings align with [[prompt-cache-optimization]] philosophy — minimize unnecessary API calls

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-11 | raw/claude-code-monitor-tool-docs-2026-04.md | Initial creation from official docs + community analysis |
