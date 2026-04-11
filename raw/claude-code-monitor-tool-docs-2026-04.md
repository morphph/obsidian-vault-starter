# Claude Code Monitor Tool — Official Documentation + Community Analysis

Source: https://code.claude.com/docs/en/tools-reference#monitor-tool + https://claudefa.st/blog/guide/mechanics/monitor
Captured: 2026-04-11

## Official Documentation (code.claude.com)

The Monitor tool requires Claude Code v2.1.98 or later. Released April 9, 2026.

The Monitor tool lets Claude watch something in the background and react when it changes, without pausing the conversation. Ask Claude to:

- Tail a log file and flag errors as they appear
- Poll a PR or CI job and report when its status changes
- Watch a directory for file changes
- Track output from any long-running script you point it at

Claude writes a small script for the watch, runs it in the background, and receives each output line as it arrives. You keep working in the same session and Claude interjects when an event lands. Stop a monitor by asking Claude to cancel it or by ending the session.

Monitor uses the same permission rules as Bash, so allow and deny patterns you have set for Bash apply here too. It is not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

## Detailed Technical Analysis (claudefa.st)

### Core Concept

The Monitor tool transforms Claude Code from time-driven to event-driven automation. Rather than polling at intervals, it "watches things and reacts when they happen," eliminating wasted API calls on silent checks.

### Problem It Solves

Background tasks previously operated as black boxes — you'd launch a command and get a single notification upon completion. The alternative was polling via /loop or scheduled tasks, which fires a complete prompt every N minutes and costs a full API call per iteration just to ask "did anything happen yet?"

### How It Works

Monitor launches a shell command whose standard output becomes an event stream. Each line of output triggers a notification that wakes the main session. Lines arriving within 200ms of each other batch into a single notification, so multi-line output from one event groups naturally.

Stderr is captured to a file but doesn't trigger events.

### Four Essential Parameters

| Parameter | Purpose |
|-----------|---------|
| description | Short label in notifications (e.g., "errors in deploy.log") |
| command | Shell script generating the event stream |
| timeout_ms | Auto-kill duration (default 300,000ms/5min, max 3,600,000ms/1hr) |
| persistent | Boolean; true keeps monitor running the full session |

### Two Monitor Patterns

**Stream filters** — watch continuous output and surface matching lines:

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
inotifywait -m --format '%e %f' /watched/dir
node watch-for-events.js
```

**Poll-and-if filters** — check a source at intervals and emit when conditions change:

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  gh api "repos/owner/repo/issues/123/comments?since=$last" \
    --jq '.[] | "\(.user.login): \(.body)"'
  last=$now; sleep 30
done
```

### Three Critical Rules

1. Always use `grep --line-buffered` in pipes — without it, buffering delays events by minutes
2. Handle transient failures in poll loops with `|| true` to prevent one timeout from killing the entire monitor
3. Be selective with output — every line becomes a conversation message; auto-stops occur with excessive events; use filters instead of unfiltered streams

### Token Economics

A /loop checking tests every 2 minutes over 10 minutes costs 5 full API calls. Monitor inverts this: Claude watches the test runner's output through a filter. When test #23 fails at minute 4, that failure line pushes directly into the session. Claude starts diagnosing the error while tests 24-47 are still running. No wasted calls.

### Use Cases

- Dev server monitoring: Catch build errors and crashes instantly
- Test suite triage: Surface failing tests as they fail
- CI/CD watching: Follow deployment pipelines for failures
- PR polling: Watch for new comments or status checks
- Log monitoring: Tail production logs with pattern filters

### Monitor vs. Alternatives

- Hooks: Fire on Claude's own actions (before file edits, after commits)
- Scheduled Tasks (CronCreate): Fire on fixed time intervals
- Monitor: Fire on external events — best for reacting to real-time output
- run_in_background (Bash): Fire-and-forget with one notification at completion

### Availability

Not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.
Requires Claude Code v2.1.98+.

## Changelog Entry

Version 2.1.98: "Added Monitor tool for streaming events from background scripts"

## Source Tweet

Noah Zweben (@noahzweben), Claude Code PM, announced: "Thrilled to announce the Monitor tool which lets Claude create background scripts that wake the agent up when needed. Big token saver and great way to move away from polling in the agent loop."
