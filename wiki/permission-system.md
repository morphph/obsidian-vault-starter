---
type: concept
created: 2026-04-06
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
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
- **Three-level guardrail enforcement** (Pachaar/Chawla): input guardrails (first agent), output guardrails (final output), tool guardrails (every invocation)
- Claude Code independently gates ~40 discrete tool capabilities with permission checks before execution
- **Architectural decision**: Permissive (fast, risky) vs restrictive (safe, slow) — Claude Code leans restrictive with fail-closed defaults

## Connections
- Related: [[claude-code]], [[harness-design]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Initial creation |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added 3-level guardrails, 40 tool gates, permissive vs restrictive tradeoff |
