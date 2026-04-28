# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a comparison article: Codex CLI vs Claude Code — agentic coding tools.

**Key Exchanges:**
- Comprehensive feature comparison between Codex CLI (OpenAI, cloud sandbox, async) and Claude Code (Anthropic, local execution, real-time)
- Architecture distinction: Codex CLI = isolated cloud sandbox + PR output; Claude Code = local terminal agent + permission-based safety

**Decisions Made:**
- Framing: "workflow fit, not raw capability" — the verdict positions the tools as complementary, not competing
- Claude Code advantages: 5-layer extension stack (CLAUDE.md → SKILL.md → Hooks → MCP → Agent teams), real-time interaction, full local env access
- Codex CLI advantages: architectural security isolation, async batch execution, PR-based output, included with ChatGPT Pro
- Pricing: Claude Code = API pay-per-token or Max subscription ($100–200/mo); Codex CLI = bundled with ChatGPT Pro ($200/mo) or Team plans

**Lessons Learned:**
- Codex CLI (2025) is unrelated to original OpenAI Codex (2021) — naming causes confusion, worth clarifying
- Codex CLI models: codex-mini, o3, o4-mini (reasoning-optimized); Claude Code models: Opus, Sonnet, Haiku (up to 200K context)
- Codex CLI customization gap: no hooks, no SKILL.md equivalent, no MCP — may narrow over time
- Both tools can coexist: Claude Code for interactive dev, Codex CLI for batch/parallel task execution

**Action Items:**
- This content should be ingested into `wiki/` as a page on agentic coding tools comparison (covers Codex CLI, Claude Code, pricing, architecture, use-case guidance)
- Freshness note: pricing and feature details are mid-2026 snapshot — flag for periodic review