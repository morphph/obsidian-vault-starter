# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Review of a comparison article between Claude Code and OpenAI Codex (likely a draft for LoreAI or AI精读 publication).

**Key Exchanges:**
- No interactive Q&A occurred — the context is a completed comparison article, not a dialogue session.

**Decisions Made:**
- N/A (no decisions captured in this session)

**Lessons Learned:**
- Claude Code = local execution, interactive pair programmer, full env access, code stays on-machine, CLAUDE.md + SKILL.md + hooks + MCP for customization, terminal-native, per-token billing
- Codex = cloud sandbox, async task queue, isolated containers, code uploaded to OpenAI infra, AGENTS.md, ChatGPT/VS Code interface, bundled subscription pricing
- Key differentiator for enterprise: Claude Code keeps code local (easier security review); Codex requires cloud data handling evaluation
- Recommended split: Claude Code for interactive/complex/environment-dependent work; Codex for batch/parallelizable/well-defined tasks
- Models differ: Claude Code uses Claude (Opus/Sonnet), Codex uses codex-1/o3

**Action Items:**
- Consider ingesting this article as a raw source → `/ingest` → generate wiki page `claude-code-vs-codex.md` covering execution model, security posture, pricing, and use-case split
- Article ends with LoreAI subscribe CTA — confirm publish destination before finalizing