---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
tags: [source, anthropic, engineering]
---

# Source: Scaling Managed Agents — Engineering Blog

## Summary
Anthropic engineering blog post detailing the architecture behind Claude Managed Agents. Core thesis: decouple the brain (Claude + harness), hands (sandboxes + tools), and session (append-only event log) so each can fail or be replaced independently. The session is the source of truth, not the harness.

## Key Takeaways
- Session as append-only event log is the key architectural insight — everything else is stateless and replaceable
- Lazy container provisioning: spin up only when tools need them → p50 TTFT improved ~60%, p95 improved >90%
- Uniform tool interface: `execute(name, input) → string` for everything
- Credential isolation: OAuth vault + proxy pattern, git tokens never exposed to running code
- This is Anthropic productizing the [[harness-design]] patterns they published about earlier

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-engineering-blog.md | Initial creation |
