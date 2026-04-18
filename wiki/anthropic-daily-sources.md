---
type: synthesis
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-claude-daily-source-verification.md
tags: [wiki, ops, newsletter, ingestion]
---

# Anthropic & Claude Daily-Fetch Sources

## Summary
Master source list for daily ingestion across **all Anthropic + Claude products** — covers Anthropic (company-level news, engineering), Claude (consumer product), Claude API, Claude Code, and Claude Cowork. 18 sources total: 9 websites, 8 X accounts, 1 RSS feed. All websites tested via WebFetch; all X handles verified live via Playwright MCP on 2026-04-18. Used by `/ingest-anthropic-daily` for automated sweeps.

## Final Source List

| Product | Type | Source | Method |
|---|---|---|---|
| **Anthropic** | Website | anthropic.com/news | WebFetch |
| Anthropic | Website | anthropic.com/engineering | WebFetch |
| Anthropic | X | @AnthropicAI — Anthropic | Playwright |
| Anthropic | X | @mikeyk — Mike Krieger (CPO) | Playwright |
| **Claude** | Website | claude.com/blog | WebFetch |
| Claude | Website | support.claude.com/.../release-notes | WebFetch |
| Claude | X | @claudeai — Claude | Playwright |
| Claude | X | @alexalbert__ — Alex Albert *(double `_`)* | Playwright |
| **Claude API** | Website | platform.claude.com/docs/en/release-notes | WebFetch |
| Claude API | Website | platform.claude.com/docs/en/about-claude/models/overview | WebFetch |
| **Claude Code** | Website | platform.claude.com/docs/en/claude-code | WebFetch |
| Claude Code | Website | github.com/anthropics/claude-code/raw/refs/heads/main/CHANGELOG.md | WebFetch |
| Claude Code | X | @bcherny — Boris Cherny | Playwright |
| Claude Code | X | @_catwu — cat (Cat Wu) *(leading `_`)* | Playwright |
| Claude Code | X | @trq212 — Thariq | Playwright |
| Claude Code | Feed | github.com/anthropics/claude-code/releases.atom | RSS |
| **Claude Cowork** | Website | claude.com/cowork | WebFetch |
| Claude Cowork | X | @felixrieseberg — Felix Rieseberg | Playwright |

## Method Notes

- **WebFetch** works for all listed websites. Use canonical `platform.claude.com/docs/...` (not `docs.claude.com/...` — redirects).
- **Playwright MCP** required for X. WebFetch returns HTTP 402 on every x.com URL. `browser_navigate` → page title in format `Display Name (@handle) / X` confirms both handle and identity.
- **GitHub CHANGELOG**: use `raw/refs/heads/main/...` URL. Blob URLs return an HTML wrapper that hides content.
- **RSS/Atom**: standard feed reader.

## Excluded Sources (low signal for product newsletter)

| Source | Reason |
|---|---|
| anthropic.com/transparency | Policy/compliance reports (gov requests, abuse data) |
| @jackclarkSF | Policy & AI safety lead — Import AI macro trends |
| @DarioAmodei | CEO vision essays — strategic, not actionable product news |
| status.claude.com | Incident/uptime — ops value only |

If a "policy/vision" digest is added later, re-include @DarioAmodei + @jackclarkSF as a separate stream.

## Connections
- Related: [[anthropic]], [[claude-code]], [[boris-cherny]], [[claude-managed-agents]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-claude-daily-source-verification.md | Initial creation — 18 verified sources after WebFetch + Playwright testing |
