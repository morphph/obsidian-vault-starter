# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comprehensive comparison article: Codex CLI vs Claude Code.

**Key Exchanges:**
- Detailed architectural comparison of two AI coding agent tools (OpenAI's Codex CLI vs Anthropic's Claude Code)

**Decisions Made:**
- Claude Code's 5-layer extension stack (CLAUDE.md, SKILL.md, Hooks, MCP, Agent Teams) vs Codex CLI's limited customization (AGENTS.md + open-source forking)
- Claude Code = interactive/conversational workflow; Codex CLI = async/fire-and-forget workflow
- Security models are opposite: Codex = isolation-based (sandboxed container); Claude Code = permission-based (local execution with allow-lists)
- Codex CLI uses OpenAI models (codex-1/o3, GPT-4.1); Claude Code uses Anthropic models (Opus, Sonnet, Haiku)
- Both tools can coexist — common pattern: Claude Code for interactive daytime work, Codex for async overnight tasks

**Lessons Learned:**
- Codex penalizes vague instructions; Claude Code handles ambiguity through dialogue
- Codex's sandbox model is easier for enterprise security approval but limits local env access
- Claude Code has steeper learning curve but higher ceiling due to extension stack
- Per-token cost comparisons are misleading without factoring task-completion rates and rework frequency
- For teams (3+ engineers) needing consistent AI behavior, Claude Code's programmable stack is stronger
- For security-constrained / regulated environments, Codex's sandboxed model is simpler to approve
- Large codebases favor Claude Code (reads files on demand vs. Codex's full repo snapshot upload)

**Action Items:**
- This article is ready for `/ingest` into wiki — would create/update pages for: [[codex-cli]], [[claude-code]], [[ai-coding-agents-comparison]], and cross-references to existing pages on [[MCP]], hooks, etc.