---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, harness-engineering, pattern]
---

# Time-Gated Compilation

## Summary
Pattern where knowledge capture happens continuously but compilation (synthesis into structured knowledge) only triggers after a time gate — e.g., after 6 PM local time. Separates the accumulation phase (all day) from the synthesis phase (end of day). No cron job needed — piggybacks on the last capture event of the day.

## Details
- Implemented in [[claude-memory-compiler]]: flush.py checks current time + SHA-256 hash of daily log against state.json
- If after 18:00 AND today's log has changed since last compile → spawn compile.py as detached background process
- Avoids: compiling after every session (too expensive, too fragmented), manual triggers (too much friction), cron jobs (another thing to manage)
- Cost optimization: compile once per day (~$0.45-0.65) vs. every session (~$0.02-0.05 × N sessions)
- Applicable to any pipeline with frequent small inputs and expensive synthesis: RSS feeds, Telegram bot captures, email triage

## Connections
- Related: [[zero-friction-capture]], [[compiler-analogy]], [[claude-memory-compiler]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation |
