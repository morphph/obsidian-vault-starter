---
type: source-summary
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
tags: [wiki, source]
---

# Source: Claude Code Ralph Wiggum Plugin

## Summary
Anthropic's official Ralph Wiggum plugin for Claude Code. Uses Stop hook architecture (not bash loop) — agent works, tries to exit, hook intercepts and feeds same prompt back. Provides `/ralph-loop` and `/cancel-ralph` commands. Formalized by [[boris-cherny]] in late 2025.

## Source Details
- **URL**: https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum
- **Author**: [[anthropic|Anthropic]]
- **Date**: December 2025 (plugin release)
- **Type**: Official plugin README

## Key Claims
1. Stop hook architecture replaces external bash loop — loop happens inside session
2. `/ralph-loop` command with `--max-iterations` and `--completion-promise` options
3. Always use `--max-iterations` as safety net
4. Good for: well-defined tasks, automatic verification, greenfield projects
5. Not good for: human judgment tasks, unclear criteria, production debugging
6. Bash loop vs Stop hook is a fundamental architectural disagreement in the community

## Pages Created/Updated
- [[ralph-wiggum]] — Added Stop hook architecture, official commands
- [[claude-code]] — Added Ralph plugin

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-anthropic-ralph-wiggum-plugin.md | Initial creation |
