---
type: synthesis
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-19-anthropic-daily-run.md
tags: [wiki, digest, anthropic, claude, daily]
---

# Anthropic + Claude Daily Digest — 2026-04-19

## Summary
**Quiet day. 0 new items in window 2026-04-18 → 2026-04-19.**

Coming off the busy week of Opus 4.7 launch (Apr 16) and Claude Design (Apr 17), no new product news, model releases, blog posts, engineering posts, support release notes, API release notes, or Claude Code releases since 2026-04-18.

Most recent activity by source:
- News: Apr 17 — Claude Design (Anthropic Labs)
- Blog: Apr 16 — Best practices for Opus 4.7 with Claude Code
- API release notes: Apr 16 — Opus 4.7 launch + Bedrock GA
- Claude Code: v2.1.114 at 2026-04-18T01:34Z (last release of the burst)

## ⚠️ X scraping limitation discovered

Daily mode included X handle scraping per Option B. **All 8 handles were checked via Playwright but content scraping does not work reliably without authentication** — X serves only pinned/featured tweets (or "hasn't posted" message) to logged-out browsers.

- @AnthropicAI is the only handle returning real recent content (latest 2026-04-16)
- @felixrieseberg explicitly returned "hasn't posted" despite having 2,744 lifetime posts
- Page-title verification (used for source-list verification on 2026-04-18) still works fine — only content/timeline scraping is broken

**Followups flagged in `wiki/anthropic-daily-sources.md`:** treat X handles as low-confidence in daily mode until X API key or authenticated session is wired up.

## Categories

| Category | New items |
|---|---|
| Models | 0 |
| Anthropic (company) | 0 |
| Claude (consumer product) | 0 |
| Claude API | 0 |
| Claude Code | 0 |
| Claude Cowork | 0 |

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-19-anthropic-daily-run.md | First daily run after backfill — all sources clear, X scraping limitation documented |
