# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting the May 18, 2026 AI newsletter issue, transforming raw source links into a structured newsletter with editorial commentary.

**Key Exchanges:**
- Raw source material covered ~20 stories; final newsletter elevated 3 to top stories, compressed the rest into quick hits
- Editorial framing chose "Anthropic overtakes OpenAI in enterprise spend" as the lead and pick of the day

**Decisions Made:**
- **Lead story = Ramp enterprise spend data** — chosen because it's a concrete data signal (corporate card transactions), not a vibes narrative. Editorial angle: the shift from ChatGPT seats to API line items signals AI moving from experiment to infrastructure.
- **LeCun world model timeline (12-18 months) added as story #2** — this wasn't in the raw source bullet points but was elevated to a top story in the final draft, suggesting it was sourced separately or deemed important enough to promote.
- **Model routing** kept as the Model Literacy explainer — ties directly to the agent swarms story and is an architectural concept worth tracking for builder audience.

**Lessons Learned:**
- Newsletter structure pattern: 3 top stories with commentary → quick hits (one-liners) → model literacy explainer → pick of the day. This is the repeating template.
- The "pick of the day" can overlap with the lead story (both were Ramp/Anthropic) — it serves as the editorial opinion section.

**Action Items:**
- Wiki pages to create/update: [[anthropic]] (enterprise spend overtaking OpenAI), [[open-weight-models]] (Gemma 4, DeepSeek V4, Kimi K2.6, MiMo 2.5, GLM-5.1 — "most eventful month"), [[model-routing]] (new concept worth tracking), [[claude-code]] (claude-code-setup plugin, DeepSeek-TUI as competitor)
- Track: LeCun's 12-18 month world model prediction (late 2027 checkpoint)
- Track: Bindu as agent payments infrastructure — relevant to multi-agent architecture coverage
- Track: Clara Health $660M raise — AI healthcare is a recurring theme