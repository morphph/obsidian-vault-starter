# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article for LoreAI: "Claude Code vs Codex：终端 Agent 与云端 Agent 的正面交锋"

**Key Exchanges:**
- Generated a full-length `/zh/compare/` article comparing Claude Code (Anthropic) and OpenAI Codex across architecture, workflow, pricing, and use cases

**Decisions Made:**
- Framing: Not "which is better" but "two fundamentally different architectures" — local synchronous agent vs cloud async sandbox
- Verdict: Claude Code more practical for daily engineering (deeper context, real-time feedback); Codex better for batch-distributing independent tasks; best strategy is to combine both
- Cross-linked to existing blog posts: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-enterprise-engineering-ramp-shopify-spotify`, `claude-code-vs-cursor`, etc.

**Lessons Learned:**
- Core architectural distinction worth remembering: Claude Code = full local shell access + human-approval safety model; Codex = isolated sandbox container + no-network default security model
- Codex's sandbox limitation (no local DB, no private APIs, no integration tests) is its key trade-off for security/parallelism
- Enterprise adoption patterns differ: Claude Code via engineering teams (Ramp, Shopify, Spotify); Codex via ChatGPT ecosystem + open source/student programs

**Action Items:**
- Article needs to be saved to `drafts/` or the appropriate compare directory if not already committed
- Confirm internal links resolve correctly (glossary: `agentic-coding`, `agent-sdk`; related compares/blogs)