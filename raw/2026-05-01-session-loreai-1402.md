# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Detailed feature-by-feature comparison of Claude Code (interactive, local, terminal-native) vs OpenAI Codex (async, sandboxed, task-queue)
- Clarified that 2025 Codex is NOT the 2021 Codex model — completely different product sharing only the name

**Decisions Made:**
- Framing: Not "which is better" but "two different philosophies" — real-time collaborator vs async task worker
- Decision rules provided per section (environment, workflow, security, pricing) rather than a single verdict
- Recommendation: many teams will use both — Claude Code for complex interactive work, Codex for batch processing
- Internal links woven to existing LoreAI content (/compare/claude-code-vs-cursor, skills guide, hooks guide, etc.)

**Lessons Learned:**
- Claude Code advantage: layered context system (CLAUDE.md + SKILL.md) produces compounding returns with setup investment; Codex's AGENTS.md is simpler but narrower
- Codex advantage: trivial parallelism (5-10 tasks in separate containers), strong isolation, included with ChatGPT Pro ($200/mo)
- Key tradeoff: Codex sandboxing = safer but can't access local services/DBs/API keys; Claude Code local execution = powerful but requires trust
- Large monorepos favor Claude Code due to full local context access
- Code quality depends more on project context/task scoping than underlying model

**Action Items:**
- Article appears ready for `drafts/` — consider running `/draft` to formalize
- Ensure wiki pages exist for: [[claude-code]], [[openai-codex]], [[coding-agents]] with cross-references
- CTA at bottom links to /subscribe — verify that route exists on loreai.dev