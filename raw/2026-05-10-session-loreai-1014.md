# Session Capture: loreai

**Date:** 2026-05-10
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Assembling the May 10, 2026 daily AI newsletter issue — curating, categorizing, and writing up AI industry news items.

**Key Exchanges:**
- Newsletter compiled covering ~20+ items across categories: headlines, tools, techniques, model literacy, quick links, and pick of the day
- Content spans Baidu Ernie-5.1 launch, Anthropic alignment research, Altman crowdsourcing model priorities, and numerous tool/technique updates

**Decisions Made:**
- **Pick of the Day:** Anthropic's "Teaching Claude Why" alignment research — chosen because it reframes alignment as a reasoning capability rather than rule-matching, with implications for enterprise trust and model autonomy
- **Top 3 structure:** Baidu Ernie-5.1, Anthropic alignment research, Altman crowdsourcing — prioritizing a surprise model drop, foundational research, and market signal
- **Model Literacy topic:** Weight quantization — tied to Antirez's ds4 running DeepSeek v4 Flash at 2-bit on a Mac, explaining the 8x memory savings tradeoff

**Lessons Learned:**
- Claude Code token audit: 14% consumed by CLAUDE.md, 13% re-reading history — actionable for optimizing our own CLAUDE.md size
- Factory AI's multi-agent insight: validation contracts written *before* implementation prevent drift in long-running agents
- WebRTC is architecturally mismatched for server-to-client AI audio streaming (latency, session management, scaling)

**Action Items:**
- Anthropic alignment research (`teaching-claude-why`) and Claude Certified Architect are both worth ingesting into wiki as they directly relate to Anthropic tracking
- GitHub Copilot Grok deprecation deadline: May 15 — time-sensitive
- Claude Code v2.1.137-138 fixes Windows VSCode bug — note for tooling page