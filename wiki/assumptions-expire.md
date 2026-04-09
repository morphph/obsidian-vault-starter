---
type: concept
created: 2026-04-06
last-updated: 2026-04-09
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
tags: [wiki, principle, agentic]
---

# Assumptions Expire

## Summary
A design principle for agentic systems: as LLM models improve, regularly re-test and strip away scaffolding components that are no longer load-bearing. Harness complexity should decrease as model capability increases.

## Details
- When Claude Opus 4.6 shipped, the sprint construct that was essential for Sonnet became removable
- Continuous sessions with automatic compaction replaced structured sprint cycles
- The evaluator agent remained valuable at capability edges but became overhead for simpler tasks
- **Implication**: Don't assume harness complexity is permanent. Improved models shift the frontier, creating new opportunities for simpler configurations
- The space of interesting architectural combinations *expands* as capabilities grow — new problems become tractable
- **"Scaffolding principle"** (Pachaar/Chawla): Construction scaffolding enables workers to build structures they couldn't reach otherwise — but gets removed when complete. Models increasingly internalize capabilities that once required harness management.
- **Thin vs thick harness**: Thin harnesses bet on model improvement; graph frameworks (LangGraph) bet on explicit control. The right choice depends on how fast you believe models will improve.
- **Concrete evidence at tool level** ([[tw93]], [[connection-assumptions-expire-and-tool-evolution]]):
  - **TodoWrite:** Added because model was weak (needed reminders every 5 turns). Model got stronger → tool became a shackle (Claude interpreted Todo as rigid instructions, lost flexibility). "当初加这个工具是因为模型不够强，模型变强之后它反而变成了枷锁"
  - **AskUserQuestion:** Evolved through 3 versions (parameter → format convention → dedicated tool) as each approach revealed model behavior assumptions that didn't hold
  - **Search:** RAG → Grep → progressive disclosure. "Claude didn't like using" RAG; self-directed search worked better
  - **Implication:** Periodically audit tools. Ask "Was this designed because the model couldn't do X? Can it now?"

## Connections
- Related: [[harness-design]], [[claude-model-family]], [[multi-agent-architecture]], [[orchestration-loop]], [[tw93]], [[connection-assumptions-expire-and-tool-evolution]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added scaffolding principle metaphor, thin vs thick harness tradeoff |
| 2026-04-09 | raw/2026-04-09-tw93-claude-code-architecture-governance.md | Added concrete tool-level evidence: TodoWrite, AskUserQuestion, Search evolution |
