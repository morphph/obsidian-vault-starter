# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the 2026-05-15 daily AI newsletter digest (likely via `/ingest-anthropic-daily`).

**Key Exchanges:**
- Produced a full-format daily digest covering Anthropic, Google, OpenAI, and open-source AI developments

**Decisions Made:**
- Newsletter lead framed around the tension between Anthropic's $200M social impact bet vs Google's cost-curve disruption with Gemini 3.2 Flash
- "Today's Pick" focused on the 92% performance at 1/15th price thesis — the commercial implications of diminishing returns at the frontier

**Lessons Learned:**
- The digest format works well with: 发布动态 → 开发者工具 → 技术实战 → 研究前沿 → 行业洞察 → 值得一试 → 模型小课堂 → 快讯 → 今日精选
- Including engagement metrics (likes/RTs) adds credibility signals to source selection

**Action Items:**
- Wiki pages to create/update from this digest:
  - `anthropic.md` — $200M Gates Foundation partnership, US-China AI paper, AI-Native Startup Playbook, Claude for Small Business launch
  - `claude-code.md` — v2.1.142 agent orchestration flags, 50% usage limit increase (until Jul 13), Fast mode default to Opus 4.7
  - `claude-pricing.md` — Paid users get monthly API credits starting June 15
  - `gemini.md` — Gemini 3.2 Flash rumor: 92% GPT-5.5 perf at 1/15–1/20 cost, <200ms latency
  - `model-distillation.md` — Explainer written; tie to Gemini Flash cost compression
  - `mcp.md` — AWS official MCP Server launched (full API coverage, sandbox execution)
  - `mythos.md` — 250 vulnerabilities found vs 22 by prior SOTA; not cybersecurity-specific
  - `openai.md` — Codex on mobile, Windows sandbox fix
  - `open-source-models.md` — GLM 5.1 topped Artificial Analysis intelligence index; IBM Granite Embedding R2 (<100M params, 32K ctx, Apache 2.0)