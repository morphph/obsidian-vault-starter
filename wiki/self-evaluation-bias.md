---
type: concept
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, failure-mode, agentic]
---

# Self-Evaluation Bias

## Summary
A failure mode where LLM agents confidently praise their own mediocre outputs. Intensifies for subjective tasks lacking binary verification criteria. The fundamental reason why generator-evaluator separation matters in [[harness-design]].

## Details
- Agents evaluating their own work are systematically overconfident
- Problem is worse for subjective quality (design, UX) vs. objective checks (tests pass/fail)
- **Solution**: Separate generation from evaluation — use a dedicated evaluator agent tuned to be skeptical
- External evaluation beats self-criticism by a significant margin
- Out-of-the-box Claude QA agents still approve mediocre work — requires multiple calibration cycles against human judgment
- This is one of two core failure modes in long-running agentic coding (the other being [[context-anxiety]])

## Connections
- Related: [[harness-design]], [[context-anxiety]], [[multi-agent-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation |
