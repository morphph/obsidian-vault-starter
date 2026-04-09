# Session Capture: unknown

**Date:** 2026-04-08
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Implementing a robust Twitter/X content fetching fallback chain for the blog2video pipeline.

**Key Exchanges:**
- `fetch-twitter.mjs` (Puppeteer headless) can no longer extract tweet text from X — images download fine but text returns 0 paragraphs. X now blocks headless Puppeteer from reading text content.
- User wisely pushed back on quick-fix (image transcription only) and asked for a proper engineered solution with fallback chain.

**Decisions Made:**
- **Fallback chain order:** Playwright MCP (accessibility tree, highest accuracy) → WebFetch (built-in, no setup) → Puppeteer fetch-twitter.mjs (images may work, text may fail) → Vision transcription (Read tool on downloaded images) → Abort with instructions
- **Playwright MCP chosen as primary** because accessibility tree gives structured text without fighting DOM selectors
- **MCP config goes in `.mcp.json`** at project root (not in `settings.json` — that's for hooks/permissions)
- Restart only the current Claude Code session to pick up new `.mcp.json` — other sessions unaffected

**Lessons Learned:**
- X/Twitter now blocks headless Puppeteer from reading tweet text (as of ~2026-04). Images still load because they're `<img>` elements, but text content is blocked.
- MCP server config lives in `.mcp.json` at project root, read only at session startup — `/clear` won't reload it
- Playwright MCP's accessibility tree approach is more robust than DOM selector scraping for JS-heavy sites

**Action Items:**
- Test the new fallback chain with `/blog2video https://x.com/akshay_pachaar/status/2041146899319971922` after session restart
- First Playwright MCP use requires logging into X in Chrome — cookies persist after that
- Background task completed: agent-loop episode (stages 3-5) all passed, 15 slides generated for "Agent Loop凭什么只用14种状态？" (~23 min video)