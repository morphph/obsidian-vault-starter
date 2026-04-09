---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-claude-md-self-audit.md
tags: [wiki, practice, claude-code, self-audit]
---

# Source: CLAUDE.md Self-Audit

## Summary
Applied [[boris-cherny]]'s best practices and [[tw93]]'s context layering framework to audit our own project's CLAUDE.md. Found 4 critical gaps despite being under the 200-line ceiling. Restructured from 180 → 87 lines (52% reduction) by moving content to correct context layers.

## Key Findings
- 55% of CLAUDE.md content was only needed sometimes (templates, ingest-specific details, derivable infrastructure docs)
- No Compact Instructions — context compression could discard architecture decisions
- No NEVER list — hard guardrails scattered implicitly instead of consolidated
- No meta-governance — no mechanism to prevent future drift back to "dump everything in CLAUDE.md"
- Source Fetching Tools section was pure duplication (already in commands/ingest.md)

## Changes Made
- Wiki Page Format (29 lines) → `.claude/rules/wiki-page-format.md` with `paths: ["wiki/**"]`
- Log Format (17 lines) → `.claude/rules/log-format.md` with `paths: ["wiki/log.md"]`
- Source Types + Fetching Tools (27 lines) → removed (already in commands/ingest.md)
- Pipeline B (30 → 3 lines) → kept only safety-critical info
- Added: NEVER list, Compact Instructions, [[documentation-layers]] table

## Connections
- Related: [[context-noise-governance]], [[claude-code-best-practices-guide]], [[connection-context-layers-and-best-practices]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-claude-md-self-audit.md | Initial creation |
