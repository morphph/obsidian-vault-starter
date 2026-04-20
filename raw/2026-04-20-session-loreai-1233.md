# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** `/ingest-anthropic-daily` sweep processed 20 signals from Twitter, GitHub trending, official Anthropic blogs, and platform docs — generating a triage output with content actions.

**Key Exchanges:**
- The sweep covered sources from 2026-04-19 and produced a structured JSON decision matrix across 20 signals with actions: `create`, `refresh`, `refresh_and_create`, or `ignore`.

**Decisions Made:**
- **Ignore:** Hackathon announcement (stale), vague sentiment tweet, official repo trending (no new angle)
- **Refresh only:** Claude Code v2.1.113 native binary install (FAQ update), CLAUDE.md "AI engineering infrastructure" framing (absorb into memory blog), `awesome-claude-code` repo (add as discovery link to skills/plugin FAQs)
- **Create new content:**
  - Claude Code Bluetooth API for hardware integrations (desktop app, maker use case)
  - Claude Code 1M context window + session management blog
  - Desktop redesign for parallel agents blog
  - Claude Code Routines feature (highest priority — brand new named feature, zero prior coverage)
  - Auto mode vs Plan mode blog (new execution posture, reshapes permissions mental model)
  - `ant` CLI — new Anthropic first-party command-line client
  - Community agent harness patterns (everything-claude-code trending)
- **Refresh + Create:** Opus 4.7 in Claude Code (pricing/workflow pages + delegation-over-pair-programming blog), `ant` CLI FAQ + blog, subagents official guidance (review-agents blog + new FAQ), "Seeing like an agent" design post (MCP blog + agent tools blog), claude-mem plugin (memory blog + new FAQ)

**Lessons Learned:**
- **Routines** is the single highest-priority create action — new named feature with no coverage anywhere
- **Auto mode** is a distinct execution posture from Plan mode and needs dedicated coverage — don't conflate
- **Opus 4.7** shifts the recommended workflow from pair-programming → delegation; pricing and topic hub pages both need updating
- Time-limited events (hackathons, apply-by-Sunday) should always be ignored — stale within days
- Vague sentiment tweets with no product specifics = ignore regardless of author

**Action Items:**
- Create wiki/blog stubs for: Routines, Auto mode, 1M context, Desktop redesign, Bluetooth API, `ant` CLI, subagents FAQ, agent harness patterns, memory plugin FAQ
- Refresh: install FAQ (v2.1.113 binary), pricing FAQ (Opus 4.7), memory blog (claude-mem + CLAUDE.md framing), MCP setup blog (agent design post), review-agents blog (subagents guidance), skills/plugin FAQs (awesome-claude-code link)