# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (Anthropic) and Codex (OpenAI) as agentic coding tools
- Claude Code = synchronous, local-first, terminal-based agent with explicit context (CLAUDE.md/SKILL.md)
- Codex = asynchronous, cloud-sandboxed, ticket-based agent with inferred context from repo patterns

**Decisions Made:**
- Decision framework: "If you'd pair-program, use Claude Code. If you'd write a ticket, use Codex."
- Recommendation: Start with Claude Code to build intuition for task scoping, then add Codex for batch work
- Both tools complement rather than compete — use Claude Code for investigation/integration, Codex for batched execution

**Lessons Learned:**
- Codex (2025) ≠ original Codex (2021 GPT-3 model for Copilot) — completely different product, powered by codex-1 (fine-tuned o3)
- Codex's isolation model (networkless sandbox) is inherently safer for compliance-sensitive environments
- Claude Code's local execution enables real-time verification (run tests, check builds) which catches cascading failures
- Codex's pricing: included with ChatGPT Pro ($200/mo as of early 2026); Claude Code: token-based API billing or included with Claude Pro/Max
- Codex has free tiers for open-source maintainers and students

**Action Items:**
- Wiki pages to create/update: `codex.md` (OpenAI's async coding agent), update `claude-code.md` with comparison positioning
- Consider ingesting this article as raw source once published
- Verify pricing accuracy before publication (noted as frequently changing)