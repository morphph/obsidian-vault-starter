# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article comparing Claude Code vs OpenAI Codex CLI — positioning, architecture, and use-case guidance.

**Key Exchanges:**
- Claude Code = interactive/pair-programming model; Codex CLI = delegative/async ticket model
- Claude Code runs locally with permission-based security; Codex CLI runs in cloud sandbox with strong isolation
- Claude Code has deeper extensibility (hooks, MCP, skills, agent teams, custom commands); Codex CLI is simpler (AGENTS.md, GitHub integration, VS Code extension)
- Claude Code uses CLAUDE.md; Codex CLI uses AGENTS.md — both can coexist in same repo

**Decisions Made:**
- Verdict: Claude Code stronger for individual daily coding; Codex CLI better for teams delegating well-scoped tasks at scale
- Combined workflow recommended: Claude Code for active dev + Codex CLI for parallel background/batch tasks
- Market heading toward convergence — both will add the other's strengths over time

**Lessons Learned:**
- Codex CLI ≠ old OpenAI Codex model (GPT-3 fine-tune for Copilot). Codex CLI is agentic tool using GPT-4.1/o3/o4-mini
- Codex CLI weakness: feedback latency — misunderstandings caught only at delivery, not in real-time
- Claude Code weakness: approval fatigue from permission prompts; no strong isolation guarantee for compliance
- Claude Code improves over sessions (memory persists); Codex CLI is stateless per task
- Security tradeoff: sandbox (auditable isolation) vs permissions (practical capability with transparency)

**Action Items:**
- This content appears ready for wiki ingestion as a comparison page (e.g., `wiki/claude-code-vs-codex-cli.md`)
- Pricing tiers worth tracking: Claude Max $100-200/mo, Codex Pro $200/mo, both have $20/mo entry tier