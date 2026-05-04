# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working with/ingesting a comprehensive comparison article: Codex CLI vs Claude Code.

**Key Exchanges:**
- Detailed technical comparison of two AI coding tools: OpenAI's Codex CLI (sandboxed cloud execution) vs Anthropic's Claude Code (local terminal execution)

**Decisions Made:**
- Article verdict: Claude Code for teams investing in AI-augmented dev workflows long-term; Codex CLI for safety-first/async/ChatGPT Pro subscribers
- Positioning: The tools complement rather than replace each other

**Lessons Learned:**
- Codex CLI: uploads repo to isolated cloud container, no network access, uses GPT-4.1, async by design, bundled with ChatGPT Pro ($200/mo), uses AGENTS.md for config
- Claude Code: runs locally in terminal, full environment access, interactive real-time, usage-based API billing, 7-layer programmable system (CLAUDE.md → skills → hooks → MCP → agent teams → auto-memory → permission modes)
- Codex CLI ≠ original Codex model (GPT-3 based, powered Copilot autocomplete) — completely different product sharing the name
- Cost crossover: light usage favors Claude Code ($5-30/mo API); heavy usage converges with or exceeds Codex's $200/mo bundled price
- OpenAI offers free Codex access for open source maintainers and student credits
- Codex has a VS Code extension; Claude Code has remote sessions, /btw side-chains, phone monitoring
- Both support PR creation; both can run multiple tasks (Codex via ChatGPT interface, Claude Code via formal agent teams system with sub-agent spawning)

**Action Items:**
- Ingest this content into wiki if not already done (covers: [[codex-cli]], [[claude-code]], pricing models, security tradeoffs, agent architecture patterns)
- Cross-reference with existing wiki pages on Claude Code features (hooks, skills, MCP, agent teams)