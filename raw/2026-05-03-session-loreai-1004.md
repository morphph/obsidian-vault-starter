# Session Capture: loreai

**Date:** 2026-05-03
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generating the daily AI newsletter digest (2026-05-03 edition) with curated items from feed sources.

**Key Exchanges:**
- Generated a 21-item newsletter covering DeepSeek V4 launch, fine-tuning data efficiency research, and agent tooling developments

**Decisions Made:**
- Pick of the Day: The 250-example SWE-Bench paper — thesis is that coding agent moats may be about data curation, not compute
- Model Literacy concept: "Fine-Tuning Data Efficiency" — surgical fine-tuning beating scale for specific tasks
- DeepSeek V4 gets dual hero treatment (Flash for speed, Pro for benchmark quality)
- Code with Claude developer conference flagged as INSIGHT hero (next week, high engagement signal)

**Lessons Learned:**
- DeepSeek V4 Pro now benchmarks above Opus 4.7 Medium — open-source frontier closing gap with closed models
- 250 curated training examples on an old architecture produced a SWE-bench solve — challenges scaling assumptions
- Agent harness-outside-sandbox pattern gaining traction as architectural best practice
- Narrative flipped from "AI bubble" to "not enough data centers" in ~6 months, driven by agent compute demand

**Action Items:**
- Track Code with Claude conference (next week) for builder-facing announcements
- Monitor DeepSeek V4 adoption and real-world performance reports
- The fine-tuning data efficiency finding deserves a wiki page if confirmed by follow-up research