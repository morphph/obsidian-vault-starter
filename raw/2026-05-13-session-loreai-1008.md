# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Composing the daily AI newsletter digest for May 13, 2026.

**Key Exchanges:**
- User provided raw source material (tweets, blog posts, articles) and the assistant assembled them into a structured newsletter with headline stories, quick hits, model literacy, and pick of the day sections.

**Decisions Made:**
- **Top 3 stories selected:** Opus 4.7 fast mode (2.5x speed, speculative decoding), OpenAI Symphony (per-task Codex agents), DeepMind AI pointer (gesture/speech replacing mouse cursor)
- **Pick of the Day:** DeepMind's AI pointer framed as a platform play, not a UX experiment — timing before Google I/O is deliberate
- **Model Literacy topic:** Speculative decoding — explaining the technique behind Opus 4.7's fast mode
- **Claude for Legal** added as a headline-worthy item (Anthropic's first vertical play) even though it wasn't in the original source material — pulled from context

**Lessons Learned:**
- Opus 4.7 fast mode pricing matches Opus 4.6 fast ($30/$150 per 1M tokens) — speed gain without price increase
- GPT 5.5 ProgramBench result: the approach diversity (different languages at different settings) is more significant than the benchmark solve itself — frontier models developing strategic preferences
- Mollick's ASI heuristic is a useful filter: watch when AI labs disband "forward deployed engineering" teams as the real capability signal
- Needle (26M params replicating Gemini tool-calling) suggests tool-calling can be distilled 1000x — changes cost structure for agent architectures fundamentally
- Claude Code memory footprint: single process can hit 7.8GB, total ~30GB across sessions (Simon Willison finding)

**Action Items:**
- Ingest this newsletter edition into `raw/` for wiki knowledge base
- Update wiki pages: [[anthropic]] (Opus 4.7 fast mode, Claude for Legal, Code with Claude SF), [[openai]] (Symphony), [[google-deepmind]] (AI pointer), [[voice-ai]] (KAME tandem architecture, TML-Interaction-Small)
- Track speculative decoding as a concept worth a wiki page — it's becoming a recurring technique across multiple model releases