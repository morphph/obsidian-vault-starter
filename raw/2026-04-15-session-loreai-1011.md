# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing an AI news digest (April 15, 2026) covering Claude Code, robotics, cybersecurity models, and alignment research.

**Key Exchanges:**
- No interactive Q&A — this was a newsletter ingestion/review session.

**Decisions Made:**
- N/A (no user decisions recorded in this context)

**Lessons Learned:**
- **Data poisoning is model-size-agnostic**: Anthropic/UK AISI/Turing Institute joint research shows a 70B model is as vulnerable as a 7B — the attack exploits the learning process, not model capacity. Defense requires data provenance audits, not scaling.
- **Cybersecurity framing shift**: Simon Willison's "proof of work" framing — as AI makes attacks cheaper to generate, defense increasingly means proving computational effort was spent, not just detecting attacks.
- **MCP implementations widely misused**: Samuel Colvin (Pydantic creator) identified widespread protocol misuse — authoritative source to track.

**Action Items:**
- Ingest this digest into wiki — touches multiple active topics: [[anthropic]], [[claude-code]], alignment research, data poisoning, MCP, AI sovereignty (Mistral Compute), cybersecurity
- Consider creating/updating pages for: data-poisoning-attacks, gpt-5-cybersecurity, mistral-compute, claude-code-desktop
- Claude Code Desktop multi-session redesign (20K+ likes) is significant enough to warrant a dedicated wiki note under claude-code