---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
tags: [wiki, security, architecture]
---

# Permission System

## Summary
[[Claude Code]]'s seven-layer defense-in-depth security architecture. Uses two key design principles: fail-closed defaults (unknown = deny) for safety-critical operations, and fail-open degradation for configuration and external services.

## Details
- **Seven-layer defense-in-depth** — security is not a single gate but multiple overlapping layers
- **7 permission rule sources** — rules can come from multiple configuration levels
- **20 hook event types** — extensibility points for custom security behavior
- **Fail-closed defaults**: Unknown operations are denied. Safety-critical operations require explicit permission.
- **Fail-open degradation**: Configuration errors and external service failures don't crash the system — they degrade gracefully
- One of the six foundational pillars of Claude Code architecture
- Covered in a dedicated Security learning track in the Claude Reviews Claude analysis

## Connections
- Related: [[claude-code]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation |
