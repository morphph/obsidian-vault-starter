# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Building the daily AI newsletter editorial plan for 2026-05-13.

**Key Exchanges:**
- Structured a 22-item newsletter covering Opus 4.7 fast mode, OpenAI Symphony, DeepMind's post-cursor UI research, and more
- Pick of the day: DeepMind's AI pointer as a platform-layer bet (item 36844)
- Model literacy topic: Speculative Decoding — the technique enabling Opus 4.7's 2.5x speed at same quality

**Decisions Made:**
- **Hero stories chosen:** Opus 4.7 speed (LAUNCH), OpenAI Symphony multi-agent (TOOL), DeepMind pointer replacement (RESEARCH), Code with Claude SF ecosystem play (INSIGHT)
- **Narrative framing:** Multi-agent IDE war is now a two-front fight (Symphony vs Claude Code agent view); voice AI design space is forking (single-model vs tandem architecture)
- **Anthropic vertical play:** Claude for Legal flagged as first industry-specific move, signaling margin strategy shift

**Lessons Learned:**
- Opus 4.7 fast mode uses existing Opus 4.6 fast mode pricing/rate limits — waitlist required, set `speed: fast` with beta header
- Claude Code RAM issue: single processes hitting 7.8GB, totaling ~30GB across sessions (Willison report)
- Mollick's ASI heuristic: watch consulting/FDE team sizes at labs, not benchmarks
- GPT 5.5 is first model to solve any ProgramBench task; high/xhigh settings independently chose different languages (approach diversity)
- Needle project: tool-calling distilled to 26M params (1000x smaller than Gemini) — local tool routing becomes viable

**Action Items:**
- Wiki pages to create/update: [[opus-4.7]], [[openai-symphony]], [[speculative-decoding]], [[claude-for-legal]], [[deepmind-post-cursor]], [[code-with-claude-sf-event]]
- Track: MCP knowledge graph server (94% tool call reduction, 19 languages, fully local)
- Track: Sakana KAME tandem architecture for real-time voice
- Track: TML-Interaction-Small (276B-A12B) eliminating VAD for voice agents