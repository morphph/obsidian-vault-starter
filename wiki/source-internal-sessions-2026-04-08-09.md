---
type: source-summary
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-0953.md
  - raw/2026-04-08-session-unknown-1017.md
  - raw/2026-04-08-session-unknown-1126.md
  - raw/2026-04-08-session-unknown-1139.md
  - raw/2026-04-08-session-unknown-1216.md
  - raw/2026-04-08-session-unknown-1421.md
  - raw/2026-04-08-session-unknown-1644.md
  - raw/2026-04-09-session-unknown-1620.md
  - raw/2026-04-09-session-unknown-1915.md
tags: [wiki, source, pipeline-b, internal-knowledge]
---

# Source: Internal Session Captures (2026-04-08 ~ 2026-04-09)

## Summary
Nine Pipeline B session captures from coding work on [[blog2video]] and [[loreai]]. First batch of auto-captured internal knowledge from Claude Code hooks. Covers video pipeline engineering, SEO tooling, content distribution strategy, and a critical design pattern discovery ([[silent-fallback-antipattern]]).

## Sessions by Theme

### blog2video Pipeline (6 sessions)
- **0953:** Pipeline stages, narration.md as review checkpoint, manifest naming convention, parallel episode execution
- **1017:** Diagram type selection — D2 for architecture, Mermaid for flow. Thin mermaid rendering bug. Vercel CDN cache stale content.
- **1126:** Twitter/X fetching broken (Puppeteer text blocked as of ~2026-04). Engineered Playwright MCP → WebFetch → Puppeteer → Vision fallback chain.
- **1139:** MCP config moved from project-level to user-level (`~/.claude/.mcp.json`). Playwright MCP fetches X without login. Added Computer Use MCP.
- **1421:** **Critical discovery: [[silent-fallback-antipattern]]**. Pipeline completed "successfully" with image captions instead of full article text. Playwright MCP not loaded (session startup only). Fixed with preflight gate pattern.
- **1915:** Delivery metadata auto-generation for [[content-distribution-china|微信视频号 + 小红书]]. Authority hook pattern (价值先行 → 权威背书). Platform-specific title/description optimization.

### LoreAI Platform (2 sessions)
- **1644:** Dashboard secret persistence (PM2 env vars lost on restart → .env). Health report integration. Pipeline flow diagram organized by business purpose, not cron schedule. Created `/pipeline-flow` skill.
- **1620:** Content quality test — term-centric slugs over question-style. HTML comments visible to search engines/AI. No slug migrations during quality rounds.

### SEO Tooling (1 session)
- **1216:** [[keyword-grouping-engine]] — reusable prompt for intent classification, content type assignment, keyword clustering. Tested on "Claude Code Pricing" subtopic.

## Entities Extracted
- [[blog2video]] (new), [[loreai]] (new)

## Concepts Extracted
- [[silent-fallback-antipattern]] (new), [[content-distribution-china]] (new), [[keyword-grouping-engine]] (new)

## Key Lessons Across Sessions
- MCP servers only load at session startup — `/clear` won't reload. Critical for pipeline reliability.
- Playwright MCP accessibility tree is more robust than DOM scraping for JS-heavy sites
- PM2 env vars don't persist across restarts — always use `.env` files
- HTML comments are not truly hidden from search engines and AI crawlers
- Pipeline visualizations should organize by business purpose, not cron schedule
- TTS step is idempotent — safe to retry renders

## Source Files
`raw/2026-04-08-session-unknown-{0953,1017,1126,1139,1216,1421,1644}.md`, `raw/2026-04-09-session-unknown-{1620,1915}.md`
