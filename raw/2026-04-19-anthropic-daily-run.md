# Anthropic + Claude Daily-Fetch Run — 2026-04-19

**Window:** 2026-04-18T00:00:00Z → 2026-04-19T05:46:00Z
**Mode:** daily (since last backfill on 2026-04-18)
**Run timestamp:** 2026-04-19T05:46:00Z

## Website results — all clear (nothing new since 2026-04-18)

| Source | Latest in-window? | Notes |
|---|---|---|
| anthropic.com/news | ❌ none | Latest = Apr 17 (Claude Design) |
| anthropic.com/engineering | ❌ none | Latest = Mar 25 (auto mode) |
| claude.com/blog | ❌ none | Latest = Apr 16 (best practices Opus 4.7) |
| support.claude.com release-notes | ❌ none | Latest = Apr 17 (Claude Design) |
| platform.claude.com API release-notes | ❌ none | Latest = Apr 16 (Opus 4.7 + Bedrock GA) |
| github releases (gh api filter `>= 2026-04-18T18:00:00Z`) | ❌ none | Latest = v2.1.114 at 2026-04-18T01:34Z |

## X handles — content scraping FAILS without login

Tested all 8 handles via Playwright `browser_navigate` + DOM evaluation:

| Handle | DOM `<article>` count | Latest visible | In-window? |
|---|---|---|---|
| @AnthropicAI | 3 | 2026-04-16 | ❌ |
| @mikeyk | 4 (pinned only) | 2025-09-30 | ❌ |
| @claudeai | 11 (after scroll) | 2025-10-31 | ❌ — X likely hiding 2026 posts |
| @alexalbert__ | 3 (pinned only) | 2025-02-25 | ❌ |
| @bcherny | 4 | 2025-11-13 | ❌ |
| @_catwu | 4 | 2025-08-09 | ❌ |
| @trq212 | 5 | 2026-03-21 | ❌ |
| @felixrieseberg | **0** | "@felixrieseberg hasn't posted" | ❌ — explicit X login wall |

### Critical operational finding

**Playwright without authentication is unreliable for X content scraping.** X serves a curated/limited view to logged-out browsers:

- Active accounts like @felixrieseberg (2,744 lifetime posts) show as "hasn't posted"
- Other accounts show only pinned/featured tweets, not chronological recent posts
- `@AnthropicAI` was the most useful — showed real recent content (3 tweets back to 2026-04-14)
- Cross-posts visible via repost are usable: 2026-04-16 Opus 4.7 was visible via @AnthropicAI repost

**Page-title verification still works** (browser_navigate → page.title returns `Display Name (@handle) / X` reliably). So handle existence verification is fine, but content scraping requires:
- A real X API key, OR
- Playwright with persisted authenticated session, OR
- Nitter-style proxy (community-run, may rate-limit)

## Daily digest items

**0 unique items** in window. Quiet day — no new product announcements, model releases, blog posts, or Claude Code releases since the major Apr 16-18 burst (Opus 4.7 launch + v2.1.111-v2.1.114).

## Recommendation

Update `wiki/anthropic-daily-sources.md` to flag the X-content-scraping limitation:
- X handles section: split into "verifiable" (page title) vs "scrapable" (requires auth)
- For now, daily X content is best captured via @AnthropicAI page (which shows reposts and originals reliably)
- Consider adding X API key as a future improvement if X-originated news matters

## State file (would-be content)

```json
{
  "last_run": "2026-04-19T05:46:00Z",
  "last_run_window": "2026-04-18T00:00:00Z..2026-04-19T05:46:00Z",
  "items_found": 0,
  "x_scraping_unauthenticated": "unreliable — see raw/2026-04-19-anthropic-daily-run.md",
  "sources": {
    "anthropic.com/news": "2026-04-19T05:46:00Z",
    "anthropic.com/engineering": "2026-04-19T05:46:00Z",
    "claude.com/blog": "2026-04-19T05:46:00Z",
    "support.claude.com/release-notes": "2026-04-19T05:46:00Z",
    "platform.claude.com/docs/en/release-notes/api": "2026-04-19T05:46:00Z",
    "github.com/anthropics/claude-code/releases": "2026-04-19T05:46:00Z",
    "code.claude.com/docs": "snapshot 2026-04-19",
    "claude.com/cowork": "snapshot 2026-04-18 (no new fetch this run)"
  }
}
```
