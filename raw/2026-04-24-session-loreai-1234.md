# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Automated `/ingest-anthropic-daily` signal sweep for 2026-04-23/24, routing Claude Code ecosystem events to wiki/blog content actions.

**Key Exchanges:**
- 20 signals processed; 7 ignored (retweets, off-topic, niche); 13 routed to specific pages with action types (refresh, refresh_and_create, ignore)

**Decisions Made:**
- **Highest priority create:** New blog on April 2026 Claude Code quality regression post-mortem (keyword: "claude code april 2026 quality issue explained") — primary source is Anthropic Engineering post at `anthropic.com/engineering/april-23-postmortem`
- **Pricing FAQ urgent refresh:** Simon Willison coverage + `claudecode_lab` tweet confirm Claude Code pricing FAQ is stale; fix version `v2.1.116+` restores paid user limits; new FAQ page suggested (keyword: "how much does Claude Code cost per month")
- **Marketplace blog:** Community-built 1000+ asset marketplace (agents, skills, MCPs, hooks) installable via single command — warrants new blog (keyword: "claude code plugin marketplace free")
- **Root cause confirmed:** Quality regression caused by harness/infrastructure configuration (Agent SDK), NOT model weights — critical distinction for Agent SDK and CI/CD subtopics
- **Google Cloud official Agent Skills repo** (13 skills compatible with Claude Code, Gemini CLI, Codex, OpenCode) — new tutorial warranted (keyword: "google cloud agent skills claude code setup")
- **PM use case content gap:** Lenny's Podcast episode with Claude Code PM on product velocity → new blog (keyword: "how product managers use Claude Code")
- **Harness ranking controversy:** Fucory ranked Claude Code C-tier during regression — comparison pages need note that regression is resolved; new compare page for harness ecosystem (Amp, Conductor, OpenCode, Warp) suggested

**Lessons Learned:**
- The April 2026 quality incident was infrastructure-level, not model-level — a pattern worth flagging in any future quality regression coverage
- Social media content automation (100+ post patterns via skills) is a validated non-technical Claude Code use case
- n8n + MCP server is a confirmed third-party connectivity pattern for the MCP subtopic

**Action Items:**
- Create: blog on April 2026 post-mortem (`blog/claude-code-april-2026-quality-issue`)
- Create: FAQ on Claude Code pricing tiers (`faq/claude-code-pricing-2026`)
- Create: blog on plugin/asset marketplace
- Create: tutorial on Google Cloud Agent Skills + Claude Code
- Create: blog on PM use cases (reference Lenny's Podcast)
- Create: compare page for harness ecosystem alternatives
- Refresh: `faq/claude-code-pricing`, `faq/claude-code-skills`, `blog/claude-code-mcp-setup`, `blog/claude-code-hooks-*`, `compare/claude-code-vs-cursor`, `compare/claude-code-vs-codex`, `blog/claude-code-is-not-a-coding-tool`