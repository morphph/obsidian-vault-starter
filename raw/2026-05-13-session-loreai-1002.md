# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily AI newsletter (~May 13, 2026), selecting headlines from a scored candidate pool while avoiding overlap with May 12 coverage.

**Key Exchanges:**
- Reviewed May 10–12 newsletters to avoid repeating headlines (OpenAI Deployment Company was May 12 PICK; agent view, AWS platform, Karpathy HTML were May 12 headlines)
- Selected 22 candidates spanning Anthropic launches, OpenAI moves, research breakthroughs, and tooling

**Decisions Made:**
- **Opus 4.7 fast mode** (score 92) — 2.5x faster output, $30/$150 per 1M tokens, available on API and Claude Code
- **OpenAI Symphony** (score 91) — each task spawns a dedicated Codex agent; direct competitor to Claude Code agent view, same week
- **DeepMind AI pointer** (score 90) — rethinking mouse pointer with motion/speech/gesture, pre-Google I/O
- **Code with Claude SF 2026** (score 88) — flagship dev event recap, roadmap signals
- **GPT 5.5 solves first ProgramBench task** (score 87) — new benchmark ceiling, chose different languages at different settings
- **Anthropic cybersecurity case study** (score 87) — dogfooding Claude Code for internal threat detection
- **Claude for legal** (score 86) — vertical industry play for $1T+ market

**Lessons Learned:**
- **Needle project**: 26M param model replicates Gemini tool-calling (1000x smaller) — if tool-calling distills this aggressively, agent cost structures change fundamentally
- **Claude Code memory**: Simon Willison found processes consuming ~30GB, largest single process 7.8GB — practical concern for multi-session users
- **MCP codebase knowledge graph**: Cuts Claude Code tool calls by 94% via local knowledge graph indexing (19+ languages, no API keys) — addresses token overhead problem
- **Mollick's ASI heuristic**: "You'll know labs believe in ASI when they disband their consulting groups" — as long as forward-deployed engineering teams are needed, ASI timeline is further than marketing suggests
- **Study Mode removal**: OpenAI quietly removed Study Mode from ChatGPT; evidence shows AI assistant mode hurts learning. Claude and Gemini still have theirs — competitive differentiator

**Action Items:**
- Ingest Opus 4.7 fast mode details into wiki (new capability, pricing)
- Update OpenAI wiki page with Symphony launch
- Track ProgramBench as a model capability benchmark
- Note Claude Code v2.1.140 release (agent color palette, /goal fix)
- Watch Google I/O for Gemini Omni reveal