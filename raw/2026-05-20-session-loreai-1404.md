# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft or source article comparing Claude Code vs OpenAI Codex as AI coding agents.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (Anthropic) and OpenAI Codex covering interaction model, extensibility, security, DX, and pricing

**Decisions Made:**
- Claude Code = real-time, local-first, deeply extensible (CLAUDE.md, SKILL.md, hooks, MCP, agent teams)
- Codex = async delegation, cloud sandbox, simpler setup, bundled with ChatGPT subscriptions
- Verdict framing: "work alongside the agent (Claude Code) vs delegate to it (Codex)"
- Both tools can coexist — complementary strengths, not mutually exclusive

**Lessons Learned:**
- Codex's async sandbox model is better for well-defined batch tasks; Claude Code wins for exploratory/ambiguous work requiring judgment calls
- Claude Code's extension stack (CLAUDE.md → SKILL.md → hooks → MCP → agent teams) is a structural advantage for teams with established conventions
- Security difference is architectural: Claude Code keeps code local, sends only context to API; Codex clones full repo to cloud sandbox
- Codex setup friction comes from sandbox environment mirroring; Claude Code friction comes from extension system configuration investment
- CLAUDE.md/SKILL.md don't transfer to Codex — migration requires translating instructions into task prompts
- Pricing: Codex bundled with ChatGPT plans (free incremental); Claude Code offers Pro/Max/API tiers with usage-based scaling

**Action Items:**
- Ingest this as a raw source and update wiki pages for [[claude-code]], [[openai-codex]], and potentially a dedicated comparison page
- Cross-reference with existing wiki entries on Claude Code hooks, agent teams, MCP
- Pricing details are freshness-sensitive — flag for periodic review