# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-04.

**Key Exchanges:**
- Newsletter produced covering: Ollama v0.23 Claude Desktop integration, Harvard o1 ER diagnosis trial, Codex platform sprint, Altman pushing Agents SDK 2.0, Anthropic/Fractile chip deal, tool-input repair layers

**Decisions Made:**
- Pick of the Day: Harvard o1 vs ER doctors trial (67% vs 50-55% accuracy) — chosen for its institutional/political implications beyond the technical result
- Framing of tool-input repair layer story as the week's most actionable insight for builders

**Lessons Learned:**
- "Bad at tool calling" is almost always malformed JSON or schema mismatches in the harness, not a model limitation — a $2 model with good plumbing beats a $60 model with sloppy integration
- When Sam Altman calls something "underrated," translate to "we need more adoption"
- Ollama v0.23 bridges local inference to Claude Desktop — changes calculus on local vs cloud for data residency teams

**Action Items:**
- Potential wiki pages to create/update: `ollama.md` (Claude Desktop integration), `tool-input-repair.md` (new technique), `openai-o1.md` (clinical evidence), `codex.md` (platform sprint + security plugin), `nanoclaw.md` (agent framework), `fractile.md` (Anthropic chip sourcing)
- Track: Academy AI ban for Oscars as precedent-setting creative industry policy
- Track: MCP primitives beyond tool calling (Prompts, Resources, Sampling, Roots, Notifications) — most builders only use 20%