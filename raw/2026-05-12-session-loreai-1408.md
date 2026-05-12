# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User was working with a detailed comparison article: Claude Code vs OpenAI Codex — likely for ingestion or reference.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (Anthropic) and OpenAI Codex covering architecture, customization, workflow, pricing, and model capabilities

**Decisions Made:**
- None explicitly made in this session — content appears to be source material for the wiki

**Lessons Learned:**
- **Claude Code = local interactive agent** — runs in your terminal with full env access (DBs, SSH, staging). Strength: iterative complex work, deep customization (CLAUDE.md → Skills → Hooks → MCP → Agent Teams)
- **Codex = cloud sandbox task runner** — each task gets a fresh microVM, returns git artifacts. Strength: parallel async execution of well-scoped tickets, inherent safety via isolation
- **Customization gap is the widest difference** — Claude Code has 7 programmable layers (CLAUDE.md, SKILL.md, Hooks, MCP, Agent Teams); Codex has AGENTS.md + task prompt only
- **Pricing model difference** — Claude Code: usage-based per-token (light users ~$20-50/mo); Codex: bundled in ChatGPT Pro at $200/mo
- **Model backends** — Claude Code: Opus 4 / Sonnet 4 with extended thinking; Codex: codex-1 (RL-trained for sandboxed coding) + GPT-4.1 + o3
- **Decision heuristic:** bottleneck = task complexity → Claude Code; bottleneck = task volume → Codex. They're complementary, not competing
- **Monorepo advantage for Claude Code** — local execution avoids clone + dependency install overhead that Codex repeats per task

**Action Items:**
- Consider ingesting this article into `raw/` and creating/updating wiki pages for [[claude-code]], [[openai-codex]], and possibly a comparison page
- Could inform updates to builder tools / workflows sections of the wiki