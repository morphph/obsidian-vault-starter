# Session Capture: unknown

**Date:** 2026-04-08
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Running blog2video pipeline on Twitter/X article about Agent Harness architecture, discovering and fixing a silent quality degradation issue.

**Key Exchanges:**
- Video rendered successfully but source content was only image captions (vision transcription of 8 infographics), not the full article text
- Root cause: Playwright MCP was configured in `~/.claude/.mcp.json` but not loaded in this session — MCP servers only initialize at session startup
- Without Playwright, the fetch-source fallback chain silently degraded to vision transcription, producing a shallower video with no warning

**Decisions Made:**
- Added **hard-stop pre-flight gate** in both `fetch-source.md` (Step 3) and `SKILL.md` (Step 0): for Twitter/X URLs, ToolSearch must confirm `browser_navigate` is available. If not → immediate stop with restart instructions. No silent fallback to vision.
- This was committed and pushed.

**Lessons Learned:**
- MCP servers only load at session startup — `/clear` won't reload them. Must exit and restart Claude Code.
- Silent fallback chains are dangerous: the pipeline completed "successfully" but with dramatically lower quality (image captions vs full article). Always prefer hard stops over silent degradation for critical dependencies.
- The pre-flight check pattern (ToolSearch for required MCP tools before proceeding) is reusable for any pipeline step that depends on a specific MCP server.

**Action Items:**
- Re-run `/blog2video-script` for the Akshay Pachaar harness article after restarting session with Playwright MCP loaded
- Consider configuring `rclone gdrive:` remote for automated Google Drive uploads