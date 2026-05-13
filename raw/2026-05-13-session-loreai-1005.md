# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-13, covering Anthropic, OpenAI, and DeepMind announcements.

**Key Exchanges:**
- Newsletter produced covering: Opus 4.7 fast mode (2.5x speed, `speed: fast` API param), OpenAI Symphony (per-task Codex agents), DeepMind post-cursor gesture/speech interfaces, GPT 5.5 ProgramBench breakthrough, Claude for Legal vertical launch

**Decisions Made:**
- Pick of the Day: DeepMind's AI pointer as a platform play (owns interaction layer → owns platform; Google already controls Android/Chrome/browser)
- Model Literacy topic: Speculative decoding — explains how Opus 4.7 fast mode achieves 2.5x speed without quality loss

**Lessons Learned:**
- Anthropic's first vertical play (Legal) signals shift from horizontal API to purpose-built industry tooling
- OpenAI Symphony vs Claude Code agent view = official two-front multi-agent IDE war
- `claude agents` command exists as a terminal control plane across sessions (run from project root, left-arrow to register)
- Claude Code can consume ~30GB RAM across sessions (Simon Willison finding) — check Activity Monitor
- Mollick's ASI heuristic: watch when labs disband "forward deployed engineering" teams, not benchmarks
- ChatGPT quietly killed Study Mode — Claude/Gemini still have equivalents (matters for education use cases)
- Needle: tool-calling distilled to 26M params (1000x smaller than Gemini) — changes cost structure for agent architectures
- Sakana KAME and TML-Interaction-Small represent diverging voice AI architectures (tandem vs native interaction vs single-model)

**Action Items:**
- Ingest this newsletter into wiki: update pages for [[anthropic]], [[openai]], [[google-deepmind]], [[claude-code]], [[opus-4.7]] (or create), [[speculative-decoding]]
- Create/update wiki page for OpenAI Symphony and the multi-agent IDE landscape
- Track DeepMind post-cursor interfaces as a recurring thread (pre-Google I/O timing)
- GPT 5.5 ProgramBench result worth tracking in model capabilities page