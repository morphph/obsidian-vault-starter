---
type: source-summary
created: 2026-04-15
last-updated: 2026-04-15
sources:
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
tags: [wiki, source]
---

# Source: Claude Code Sandboxing — Anthropic Official

## Summary
Anthropic's engineering blog and official documentation on Claude Code's native sandboxing. OS-level filesystem and network isolation using Seatbelt (macOS) and bubblewrap (Linux). 84% reduction in permission prompts. Open-sourced as `@anthropic-ai/sandbox-runtime`.

## Source Details
- **URL**: https://www.anthropic.com/engineering/claude-code-sandboxing + https://code.claude.com/docs/en/sandboxing
- **Author**: [[anthropic|Anthropic]]
- **Type**: Engineering blog + official documentation

## Key Claims
1. Effective sandboxing requires BOTH filesystem and network isolation
2. 84% reduction in permission prompts internally
3. OS-level enforcement (Seatbelt/bubblewrap) covers all child processes
4. Two modes: auto-allow (best for autonomous) and regular permissions
5. Open-sourced: `npx @anthropic-ai/sandbox-runtime <command>`
6. Docker sandboxes (`docker sandbox run claude`) provide maximum isolation for AFK Ralph
7. Domain-level network filtering only — domain fronting possible

## Pages Created/Updated
- [[claude-code-sandboxing]] — New concept page
- [[claude-code]] — Added sandboxing details
- [[ralph-wiggum]] — Security foundation context

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-15 | raw/2026-04-15-anthropic-claude-code-sandboxing.md | Initial creation |
