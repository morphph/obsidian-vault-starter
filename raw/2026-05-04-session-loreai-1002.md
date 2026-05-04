# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily AI newsletter (May 4, 2026 edition), selecting PICK and headline items from ~20 scored candidates.

**Key Exchanges:**
- Reviewed recent newsletter coverage (May 2-3) to avoid repeats: DeepSeek V4 Flash, Code with Claude conference, GPT-5.5 revenue, Codex /hatch & pets, AI CLI, o1 clinical study already touched
- Analyzed 20+ scored candidates across categories: LAUNCH, RESEARCH, INSIGHT, TECHNIQUE, TOOL, BUILD

**Decisions Made:**
- Coverage dedup tracked: Codex updates roundup, LangChain releases, CLAUDE.md config tips already covered in recent editions
- High-scoring candidates identified: Sam Altman on Agents SDK 2.0 (score 95), Ollama v0.23 Claude Desktop integration (92), Codex massive update wave (91), o1 ER diagnosis study (90)

**Lessons Learned:**
- "Bad at tool calling is almost always a harness bug, not a model limitation" — key insight from the DeepSeek vs Opus 4.7 item (Ahmad Awais thread)
- MCP has 5 primitives beyond tool calling (Prompts, Resources, Sampling, Roots, Notifications) — most builders only use 20% of the protocol
- Self-improving Claude Code skills via automated eval loops (32/50 → 47/50 overnight) — prompt engineering graduating to automated optimization
- Anthropic exploring chip supply diversification via UK startup Fractile (inference-focused chips)

**Action Items:**
- Final PICK and headline selections not yet confirmed in visible context — selection needs to be finalized and newsletter assembled
- Ollama Claude Desktop integration, NanoClaw (28.5K stars), and Lazyweb MCP design tool flagged as worth deeper coverage