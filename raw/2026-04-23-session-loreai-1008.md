# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewed an `/ingest-anthropic-daily` digest of ~25 scored AI news items dated ~2026-04-23.

**Key Exchanges:**
- No interactive Q&A — session was a data review of a scored daily digest JSON payload.

**Decisions Made:**
- N/A (no decisions captured in context)

**Lessons Learned:**
- High-signal items from this digest worth tracking in wiki:
  - **Claude Code /ultrareview** (score 96): Multi-agent cloud fleet for parallel bug-hunting across codebases
  - **Google TPU v8 split** (score 93): 8T for training, 8I for inference — first purpose-built agentic inference chip
  - **Qwen3.6-27B** (score 90): Dense 27B beats Opus 4.5 on LiveBench, runs quantized on consumer hardware (16GB)
  - **Anthropic prompt caching stat** (score 85): 79% of API orgs don't use prompt caching; top integrations hit 92–96% cache rates; new dashboard shipped
  - **Shopify CTO reveal** (score 83): Unlimited Opus 4.6 budget per engineer; internal tools = Tangle, Tangent, SimGym
  - **OpenAI DeployCo** (score 80): $1.5B PE JV for enterprise AI deployment; signals OpenAI moving beyond models into infra
  - **Claude Code v2.1.117** (score 78): Forked subagents via env flag (`CLAUDE_CODE_FORK_SUBAGENT=1`), MCP in agent sessions, persistent model selection
  - **Google Cloud 13 agent skills** (score 81): Cross-platform skills working across Gemini CLI, Codex, Claude Code — notable competitor compatibility play
  - **VS Code Copilot BYOM** (score 84): Bring-your-own-model/API key now supported — breaks vendor lock-in vs Cursor/Windsurf
  - **Karpathy pixel-stream demo** (score 87): Entire screen rendered pixel-by-pixel from a model — no HTML/layout engine; if it scales, obsoletes frontend stack

**Action Items:**
- Ingest high-score items (≥85) into wiki pages: `claude-code.md`, `anthropic.md`, `open-source-models.md`, `agent-platforms.md`, `prompt-caching.md`
- Create or update `qwen.md` for Qwen3.6-27B entry
- Note Shopify internal tooling (Tangle/SimGym) as case study in `enterprise-ai-adoption.md` or similar