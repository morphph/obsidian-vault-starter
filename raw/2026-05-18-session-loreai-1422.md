# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a comprehensive comparison article: Codex CLI vs Claude Code — positioning, architecture, and use cases.

**Key Exchanges:**
- Detailed feature comparison covering execution model (cloud sandbox vs local), security, pricing, ecosystem, and multi-agent capabilities

**Decisions Made:**
- **Codex CLI = async task delegation; Claude Code = interactive pair programming** — framed as complementary, not competing
- **Pricing structure is the durable differentiator**: Codex CLI bundles cloud compute into subscription ($200/mo Pro); Claude Code charges per-token with local execution (cheaper for heavy users)
- **Security tradeoff framing**: Codex sandbox = secure-by-default but limited; Claude Code local = powerful but requires active trust via permission system
- **Recommendation**: Teams should use both — Claude Code for active dev, Codex CLI for batch tasks. Individuals choose based on work style (interactive vs delegator)

**Lessons Learned:**
- Codex CLI ≠ old OpenAI Codex model (GPT-3 based autocomplete) — completely different product, worth clarifying explicitly
- Codex CLI's parallelism is task-level (independent containers, no coordination); Claude Code's is intra-task (sub-agents sharing context) — leads to different failure modes (merge conflicts vs coordination overhead)
- Large codebases favor Claude Code — avoids clone-and-setup overhead of cloud sandbox model
- Claude Code has broader IDE coverage (JetBrains + VS Code + terminal); Codex CLI wins on cross-platform (browser-based, no WSL needed on Windows)

**Action Items:**
- Article appears complete as draft — needs human review and publication to `drafts/`
- Pricing numbers flagged as volatile ("check official pricing pages") — may need periodic refresh
- Could extract wiki pages for: [[codex-cli]], [[claude-code-vs-codex-cli]], [[coding-agent-pricing-models]]