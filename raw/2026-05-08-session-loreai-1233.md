# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage session — evaluating 20 monitoring signals (Twitter + GitHub) for Claude Code content pipeline, dated 2026-05-07/08.

**Key Exchanges:**
- Triaged 20 signals into 7 actionable (refresh/create) and 13 ignored (duplicate retweets, third-party tools, social noise)

**Decisions Made:**
- **Signal 3+8 → refresh** `faq/claude-code-pricing`: Anthropic + SpaceX compute deal doubled Claude Code 5-hour rate limits across Pro, Max, Team, Enterprise tiers
- **Signal 7 → refresh_and_create**: Claude Code stopped a 13M req/min DDoS on BridgeMind in <10 min. New blog angle: incident response security (distinct from static vuln scanning)
- **Signal 9 → create**: Claude Code desktop Preview gained DOM element attachment + freehand pencil annotation for visual UI context. New FAQ needed.
- **Signal 11 → refresh_and_create**: "Harness engineering" framing — beat any default harness by tuning prompts/tools/skills/hooks per task. New blog for power users.
- **Signal 12 → refresh_and_create**: Claude Code Skills adopted by marketing teams (brand-to-ad pipeline for DTC). New blog: Claude Code for marketing/creative teams.
- **Signal 13 → refresh**: v2.1.132 changes — `CLAUDE_CODE_SESSION_ID` propagation to hooks, `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` env var, risky-action policy promoted in system prompt.
- **Signal 14 → refresh_and_create**: v2.1.129 — `--plugin-url` flag enables URL-based plugin distribution. New FAQ on sharing/installing plugins by URL.
- **Signal 20 → refresh**: Salesforce Data 360 MCP Server is a notable first-party enterprise integration to add to MCP setup blog.

**Action Items:**
- Refresh `faq/claude-code-pricing` with doubled limits + SpaceX compute context
- Refresh `faq/claude-code-cli` with new env vars from v2.1.129 and v2.1.132
- Refresh `blog/claude-code-hooks-mastery` and hooks guide with `CLAUDE_CODE_SESSION_ID` propagation pattern
- Refresh `blog/claude-code-mcp-setup` with Salesforce Data 360 as named enterprise example
- Refresh `faq/claude-code-skills` and `blog/claude-code-is-not-a-coding-tool` with marketing/creative use case
- Create new blog: Claude Code for incident response / security ops
- Create new FAQ: Claude Code desktop visual context (DOM attach + pencil tool)
- Create new blog: Harness engineering — task-specific optimization of prompts/tools/skills/hooks
- Create new blog: Claude Code Skills for marketing/creative production
- Create new FAQ: Installing Claude Code plugins from URL (`--plugin-url`)