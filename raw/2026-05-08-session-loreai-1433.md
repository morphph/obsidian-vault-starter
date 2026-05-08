# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting a Chinese-language comparison article "OpenAI Codex vs ChatGPT" for the LoreAI blog.

**Key Exchanges:**
- Generated a full `compare/` format article (`codex-chatgpt`) covering positioning, feature comparison, pricing, use-case guidance, and FAQ
- Article frames Codex as an agentic coding tool (cloud sandbox, repo-level context, issue→PR workflow) vs ChatGPT as a general-purpose conversational AI where coding is one capability
- Core verdict: not competitors but different layers of the same toolchain — "帮你想" (ChatGPT) vs "帮你做" (Codex)

**Decisions Made:**
- Used `codex-1` model name (based on o3) as Codex's underlying model — reflects May 2025 launch info
- Pricing anchored at Pro $200/month for Codex access, Plus $20/month for ChatGPT — noted Pro includes both
- Cross-linked to existing LoreAI content: `codex-complete-guide`, `codex-for-students`, `codex-vscode`, `first-few-days-with-codex-cli`, glossary entries (`what-does-codex-mean`, `agentic-coding`)

**Lessons Learned:**
- Compare articles work best when they identify the *mode of interaction* difference (agent vs conversation) rather than listing feature checkboxes
- For zh-language SEO comparison posts, the "选 X 的理由" / "选 Y 的理由" structure with a clear 判决 (verdict) section performs well

**Action Items:**
- Article needs to be saved to the appropriate `compare/` or `drafts/` path and committed
- Verify all cross-linked slugs (`codex-complete-guide`, `codex-for-students`, etc.) actually exist on loreai.dev
- Consider whether pricing info needs a date stamp — $200/month Pro tier could change