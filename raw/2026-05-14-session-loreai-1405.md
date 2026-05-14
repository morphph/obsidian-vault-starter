# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on/reviewing a comparative analysis article: Claude Code vs OpenAI Codex.

**Key Exchanges:**
- Detailed feature-by-feature comparison covering architecture, developer experience, pricing, security, and model quality

**Decisions Made:**
- Framing: Claude Code and Codex are **complementary, not competing** — interactive partner vs async task runner
- Recommendation: Many teams should use both — Claude Code for active development, Codex for well-defined backlog tasks
- Claude Code strengths: local execution, deep context stack (CLAUDE.md/SKILL.md/hooks/MCP), real-time iteration, terminal-native
- Codex strengths: sandboxed security, async delegation, VS Code/GUI experience, GitHub Issues integration, predictable pricing

**Lessons Learned:**
- CLAUDE.md multi-layer context (project → skills → hooks → MCP) has no Codex equivalent — Codex relies on AGENTS.md + existing repo docs
- Original Codex (2021, GPT-3 based, powered early Copilot) ≠ current Codex (o3-based cloud agent) — only shares the name
- Agent harness quality matters as much as raw model capability — direct model comparisons are misleading
- Codex sandbox self-verification (runs tests before presenting results) vs Claude Code's interactive approval loop — different quality assurance strategies
- Claude Code agent teams feature partially bridges the async gap but interaction remains fundamentally interactive

**Action Items:**
- Article references `/blog/claude-code-agent-teams`, `/blog/codex-vscode`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/compare/claude-code-vs-cursor` — ensure these wiki cross-references exist
- Could extract a standalone wiki page on **Codex (OpenAI)** covering the product evolution and current capabilities
- Pricing data is date-sensitive (Claude Pro $20/mo, Max $100-200/mo, ChatGPT Pro $200/mo) — flag for staleness checks