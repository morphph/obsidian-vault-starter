# Anthropic Daily-Fetch Sources

Verified source list for daily ingestion of Anthropic / Claude product updates.
Scope: model launches, product features, developer-facing changes.

**Last verified:** 2026-04-18 (X handles confirmed live via Playwright; websites confirmed via WebFetch)

## Sources (18 total)

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

**Breakdown:** 9 websites · 8 X accounts · 1 feed

## Excluded sources (intentionally dropped)

| Source | Type | Reason |
|---|---|---|
| anthropic.com/transparency | Website | Policy/compliance reports — not product |
| @jackclarkSF | X | Policy & AI safety lead — macro AI commentary, not Anthropic features |
| @DarioAmodei | X | CEO vision essays — strategic but rarely actionable product news |
| status.claude.com | Feed | Incident/uptime alerts — ops value only |

If a "policy/vision" digest is added later, re-add @DarioAmodei + @jackclarkSF as a separate stream.

## Pipeline notes

- **Websites** — WebFetch works for all listed; use canonical `platform.claude.com/docs/...` (not `docs.claude.com/...` which 301-redirects)
- **X accounts** — WebFetch returns HTTP 402; must use Playwright MCP
- **GitHub CHANGELOG** — use `raw/refs/heads/main/...` URL, not the blob URL (HTML wrapper hides content)
- **Atom feeds** — standard RSS reader

## Handle gotchas

- `@alexalbert__` ends in **two** underscores
- `@_catwu` starts with an underscore
