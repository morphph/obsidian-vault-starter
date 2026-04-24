# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Session appears to have ingested or reviewed a LoreAI blog article comparing Codex CLI vs Claude Code.

**Key Exchanges:**
- No interactive exchanges found — session context contains only the article content itself, with no user Q&A or back-and-forth.

**Decisions Made:**
- (None recorded in this session)

**Lessons Learned:**
- The article is a substantive comparison of Codex CLI vs Claude Code that is directly relevant to the wiki's domain (builder tools, Claude Code workflows). Key distinctions worth capturing:
  - Codex CLI = async, cloud-sandboxed, bundled with ChatGPT Pro/Team, weaker extensibility
  - Claude Code = sync/real-time, local execution, deep extensibility (CLAUDE.md, SKILL.md, hooks, MCP, agent teams)
  - Codex safety model = structural (sandbox); Claude Code safety model = permission-based
  - Pricing: Codex bundled in ChatGPT Pro ($200/mo); Claude Code = usage-based API or Max plan ($100–200/mo)
  - Many teams use both: Codex for batch/async tasks, Claude Code for interactive/iterative work

**Action Items:**
- This article (`loreai.dev` blog, Codex CLI vs Claude Code comparison) is a strong candidate for `/ingest` — it touches Claude Code extensibility, MCP, agent teams, and pricing, all relevant wiki topics. Consider running `/ingest <url>` on the source URL when available.