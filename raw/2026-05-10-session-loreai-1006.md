# Session Capture: loreai

**Date:** 2026-05-10
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the May 10, 2026 newsletter edition — filtering ~23 AI news candidates against last 3 issues to avoid duplicates.

**Key Exchanges:**
- Identified recent coverage overlap: "Teaching Claude Why" (blackmail fix), HTML-as-markdown, OpenAI CoT monitoring, Realtime voice stack, Natural Language Autoencoders, Claude in Office, GPT-Realtime-2 launch, Codex in Chrome — all skip as duplicates
- Applied hard filter on Code with Claude conference celebration/event content

**Decisions Made:**
- Dedupe against May 8 and May 9 newsletters before scoring
- GPT-Realtime-2 voice translation (BUILD) and CRM integration (TOOL) kept as candidates despite Realtime-2 *launch* being covered May 8 — these are application/how-to posts, not launch announcements

**Lessons Learned:**
- Three Chinese AI contenders now at frontier level: DeepSeek, Qwen, Ernie (Baidu's Ernie-5.1 surprise Saturday launch)
- MCP supply chain attacks are a real and growing threat — fake servers with polished READMEs and purchased accounts
- Anthropic professionalizing Claude ecosystem with formal certification (Claude Certified Architect)
- Industry bifurcation signal: Anthropic 10x headcount growth vs competitors cutting 10%+
- Antirez's ds4 engine enables local DeepSeek v4 Flash on 128GB Mac with 2-bit quant — open-source inference leapfrog moment
- GitHub deprecating Grok Code Fast 1 on May 15 — migration deadline

**Action Items:**
- Final newsletter pick selection not yet completed — need to finalize the PICK and 5-6 featured items
- Grok Code Fast 1 deprecation May 15 — time-sensitive, worth flagging to readers