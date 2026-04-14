# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison article (draft) for the LoreAI blog: OpenAI Codex vs ChatGPT

**Key Exchanges:**
- Article created: `codex-chatgpt` slug, category `tools`, lang `zh`
- Covers: positioning (async Agent vs conversational AI), feature comparison table, workflow differences, pricing, use case recommendations

**Decisions Made:**
- Article framing: "complementary, not competing" — Codex = async engineer for GitHub tasks; ChatGPT = instant pair programmer
- Codex requires minimum Plus subscription; ChatGPT has free tier
- Related content linked: `codex-complete-guide`, `codex-for-students`, `codex-vscode`, `first-few-days-with-codex-cli`, `codex-download`

**Lessons Learned:**
- Key differentiator: Codex = "engineering execution" (runs tests in real repo sandbox); ChatGPT = "text generation" (code snippets without project context)
- Codex model: codex-1, fine-tuned from o3 series, optimized for software engineering tasks
- Codex supports concurrent async tasks; useful for team workflows

**Action Items:**
- None explicitly mentioned — article appears complete and ready for human polish before publishing