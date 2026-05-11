# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs ChatGPT for coding — likely for LoreAI blog publication.

**Key Exchanges:**
- Comprehensive feature comparison between OpenAI Codex (agentic, async, repo-aware) and ChatGPT (conversational, real-time, snippet-based)
- Pricing breakdown: Free (ChatGPT only), Plus $20/mo (no Codex), Pro $200/mo (both), Team $30/user/mo (both, best value)
- Codex uses `codex-1` model, runs in cloud sandboxes, produces PRs; ChatGPT uses GPT-4o, works conversationally

**Decisions Made:**
- Article verdict: Codex and ChatGPT serve different workflow stages, not competing use cases
- Decision rule framed as: "describe task in one message and walk away → Codex; think through interactively → ChatGPT"
- Team tier ($30/user/mo) positioned as best value for full toolkit access
- Combined workflow recommended: Explore (ChatGPT) → Implement (Codex) → Review (ChatGPT) → Iterate (Codex)

**Lessons Learned:**
- Codex scales with project complexity (multi-file), ChatGPT doesn't — 50-file refactor is one Codex shot vs dozens of ChatGPT messages
- Codex has sandbox limitations: no private APIs, external DBs, or auth-dependent runtime state
- Codex's test-run feedback loop is a meaningful quality advantage over ChatGPT's prediction-only approach
- ChatGPT remains superior for pedagogy, explanation, and diverse solution exploration
- VS Code extension reduces Codex friction but execution is still cloud-based and async
- "Most developers don't need Codex" — only justified when regularly doing 30+ min multi-file tasks

**Action Items:**
- This content references several internal links (`/blog/codex-complete-guide`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/glossary/agentic-coding`, `/glossary/what-does-codex-mean`) — wiki pages for these topics may be needed
- Consider ingesting this as a raw source and creating/updating wiki pages for: OpenAI Codex, ChatGPT coding capabilities, agentic coding tools landscape, AI coding tool pricing