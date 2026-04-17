# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** AI news digest for April 16–17, 2026 — major model launches, tooling updates, and industry insights.

**Key Exchanges:**
- No dialogue — this is a raw news feed output, likely from a LoreAI or digest pipeline.

**Decisions Made:**
- N/A (no decisions recorded in this session)

**Lessons Learned:**
- **Opus 4.7 adaptive thinking UX gap:** Ethan Mollick flags that automatic effort-routing downgrades non-math/code queries with no manual override — a real friction point vs. ChatGPT.
- **Open-weight MoE catching up to frontier APIs:** Qwen3.6-35B-A3B (35B total / 3B active, Apache 2.0) beats Opus 4.7 on Simon Willison's pelican benchmark on a laptop — signals the capability gap is closing fast at consumer hardware scale.
- **Prompting patterns differ for Opus 4.7:** Boris Cherny (Claude Code creator) notes it took days to learn how to fully leverage 4.7's agentic features — prompting approach needs updating from 4.6.

**Action Items:**
- Ingest key items into wiki: Anthropic (Opus 4.7), OpenAI (GPT Rosalind, Codex expansion), Qwen3.6, Google (AI Mode in Chrome, Gemini Robotics + Spot), Tencent HY-World 2.0
- Update `[[anthropic]]` wiki page with Opus 4.7 launch details (Cursor: 58%→70% bench, Notion: 14% eval lift)
- Note Opus 4.7 migration tool available via Claude Code (`migrate to Opus 4.7` command)
- Track: GPT Rosalind (OpenAI's first vertical/domain-specific frontier model — biology/pharma)
- Track: Pull request workflow evolution (Latent Space "RIP Pull Requests" thesis)
- Track: Gas Town API credit controversy — trust/billing audit for AI tools