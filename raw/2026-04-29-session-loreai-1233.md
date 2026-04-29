# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing `/ingest-anthropic-daily` sweep — 20 signals from Twitter, GitHub trending, and Anthropic blog on 2026-04-28/29.

**Key Exchanges:**
- Routed 20 signals: 8 actionable (refresh or refresh_and_create), 12 ignored as duplicates/noise
- Highest-impact signal: Claude Code **2.1.121 release** (signal 20) ships MCP `alwaysLoad`, `plugin prune` command, `/skills` search filter, fullscreen scroll fixes, SDK session fixes — touches 6 subtopics simultaneously
- Anthropic published **"Onboarding Claude Code like a new developer"** blog (signal 6) — first-party authoritative content on CLAUDE.md and project setup
- Anthropic released **13 free courses with certificates** covering Claude Code 101, MCP, Bedrock/Vertex, Agent Skills (signal 10)

**Decisions Made:**
- **Pages to refresh:** `claude-code-memory`, `claude-code-skills`, `claude-code-subagents-examples`, `claude-code-mcp-setup`, `claude-code-plugin-json-manifest`, `claude-code-cli`, `claude-code-is-not-a-coding-tool`, `claude-code-for-product-managers`, `claude-code-install`, `claude-code` (hub)
- **New content to create:**
  1. Blog: "How to onboard Claude Code to an existing codebase" (from signal 6)
  2. Blog: "Anthropic free Claude Code courses with certificates" (from signal 10)
  3. FAQ: "claude-code-setup plugin how to use" (from signal 14 — **needs verification** against official sources before publishing)
  4. Blog: "Claude Code 2.1.121 new features release notes" (from signal 20)
- Ethan Mollick (signal 4) framing Claude Code as a **live meeting demo tool** → route to non-technical use case pages
- CLAUDE.md trending on GitHub as community "project brain" pattern (signals 9, 11) → memory page needs ecosystem framing, not just file-format docs

**Lessons Learned:**
- CLAUDE.md has crossed into viral social proof territory — developers sharing `.md` files on GitHub as standalone artifacts. The memory page should reflect this cultural shift.
- Skill packs are emerging as an ecosystem pattern: open-design (19 skills for design), evanflow (16 skills for TDD). The skills page needs a "skill pack" concept section.
- Signal 14 (`claude-code-setup` plugin) is unverified — came from a single tweet, not official Anthropic channels. Must cross-reference before creating content.

**Action Items:**
- [ ] Execute refreshes on the 10 identified wiki pages with new signal data
- [ ] Create 4 new content pieces (3 blogs, 1 FAQ) from `refresh_and_create` signals
- [ ] Verify `claude-code-setup` plugin claim (signal 14) against official Anthropic docs before publishing
- [ ] Update `wiki/index.md` and `wiki/log.md` after all changes
- [ ] Note version milestone: Claude Code is now at **2.1.121** — update any pages referencing older version numbers