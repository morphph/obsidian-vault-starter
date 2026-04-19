---
type: synthesis
created: 2026-04-18
last-updated: 2026-04-19
sources:
  - raw/2026-04-18-claude-daily-source-verification.md
  - raw/2026-04-19-anthropic-daily-backfill-gap-fixes.md
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
| **Claude Code** | Website | code.claude.com/docs *(canonical; old `platform.claude.com/docs/en/claude-code` redirects here)* | Playwright |
| Claude Code | Website | github.com/anthropics/claude-code/raw/refs/heads/main/CHANGELOG.md | WebFetch |
| Claude Code | API | `gh api repos/anthropics/claude-code/releases?per_page=100` *(dated releases — preferred over atom)* | gh CLI |
| Claude Code | X | @bcherny — Boris Cherny | Playwright |
| Claude Code | X | @_catwu — cat (Cat Wu) *(leading `_`)* | Playwright |
| Claude Code | X | @trq212 — Thariq | Playwright |
| Claude Code | Feed | github.com/anthropics/claude-code/releases.atom | RSS |
| **Claude Cowork** | Website | claude.com/cowork | WebFetch |
| Claude Cowork | X | @felixrieseberg — Felix Rieseberg | Playwright |

## Method Notes

- **WebFetch** works for most listed websites. Use canonical `platform.claude.com/docs/...` (not `docs.claude.com/...` — redirects).
- **Playwright MCP for X — verification yes, content scraping NO.** `browser_navigate` → page title `Display Name (@handle) / X` reliably verifies handle existence. **However**, content scraping (timeline tweets) is unreliable without authentication — X serves only pinned/featured posts to logged-out browsers, and some active accounts (e.g., @felixrieseberg with 2,744 posts) explicitly return "hasn't posted." The only handle reliably showing recent content is **@AnthropicAI** (likely because of high-engagement reposts). For trustworthy daily X capture, wire up an X API key or persisted authenticated Playwright session. (Documented 2026-04-19, see `raw/2026-04-19-anthropic-daily-run.md`.)
- **Playwright also required for `code.claude.com/docs`** — JS-rendered SPA, WebFetch returns "Not Found - Loading...".
- **claude.com/blog pagination** uses Webflow-style `?<token>_page=N` query params and is not reliably fetchable via WebFetch — use Playwright + `browser_evaluate` to dump dated cards.
- **GitHub CHANGELOG**: use `raw/refs/heads/main/...` URL. Blob URLs return an HTML wrapper that hides content. Note: the file has no per-version dates — pair with `gh api releases` for timestamps.
- **GitHub releases**: `gh api repos/.../releases?per_page=100` returns all dated releases. The `releases.atom` feed only returns latest 10 entries.
- **RSS/Atom**: standard feed reader for entries within the feed window.

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
| 2026-04-19 | raw/2026-04-19-anthropic-daily-backfill-gap-fixes.md | Updated Claude Code docs URL → code.claude.com/docs (Playwright); added gh CLI as preferred releases source; documented Webflow pagination caveat for claude.com/blog |
| 2026-04-19 | raw/2026-04-19-anthropic-daily-run.md | Documented X content-scraping limitation: page-title verification works, timeline scraping does not without authentication |
