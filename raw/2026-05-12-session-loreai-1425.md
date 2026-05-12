# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Codex CLI vs Claude Code for AI-assisted development.

**Key Exchanges:**
- Comprehensive feature comparison across 7 dimensions: context systems, extensibility, workflow patterns, security models, pricing, and use-case fit
- Claude Code strengths: layered context (CLAUDE.md/SKILL.md), local execution, hooks/MCP/agent teams extensibility, interactive synchronous workflow
- Codex CLI strengths: sandboxed cloud execution, async task delegation, OpenAI ecosystem integration, safety-first for beginners/regulated environments

**Decisions Made:**
- Verdict framing: "not interchangeable — different development philosophies" rather than a winner/loser comparison
- Recommended hybrid approach: Claude Code as primary interactive agent, Codex CLI for async/sandboxed tasks
- For individual daily coding: Claude Code wins on power/flexibility; for teams needing isolation: Codex CLI wins on security guarantees

**Lessons Learned:**
- Context persistence is the key differentiator for complex codebases — CLAUDE.md/SKILL.md compound over time vs Codex's per-task instruction model
- Sandbox isolation vs local execution is a fundamental design tradeoff (security vs capability)
- Async delegation reshapes team workflows — tech leads can batch-assign tasks, a pattern worth tracking
- Codex CLI's free tiers for students/open-source maintainers is a notable go-to-market strategy
- Local execution avoids per-task compute overhead, making Claude Code cheaper at high volume

**Action Items:**
- Article references wiki-worthy concepts: [[AEO as distribution strategy]] link in footer, internal links to other blog posts — ensure these exist or are created
- Consider ingesting this as a raw source for wiki pages on: Codex CLI, Claude Code extensibility stack, AI coding agent comparison frameworks