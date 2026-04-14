---
type: source-summary
created: 2026-04-06
last-updated: 2026-04-06
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
tags: [wiki, source, engineering-blog]
---

# Source: Harness Design for Long-Running Application Development

## Summary
[[Anthropic]] Labs engineering blog post by [[prithvi-rajasekaran|Prithvi Rajasekaran]] (March 24, 2026) exploring GAN-inspired multi-agent architectures for improving Claude's performance on complex, long-running coding tasks.

## Key Takeaways
- Two core failure modes in agentic coding: [[context-anxiety]] and [[self-evaluation-bias]]
- GAN-style generator-evaluator loops push quality through iterative critique (5-15 rounds)
- Three-agent architecture (planner, generator, evaluator) dramatically outperforms single-agent for full-stack coding
- Cost: $200/6hrs (harness) vs $9/20min (solo) — but solo output was broken, harness output was functional
- Evaluator uses Playwright MCP to test like a real user
- As models improve ([[assumptions-expire]]), strip scaffolding — Opus 4.6 doesn't need the sprint contracts that Sonnet did
- Evaluation tuning is real work — default QA agents are too lenient

## Entities Extracted
- [[Anthropic]], [[prithvi-rajasekaran|Prithvi Rajasekaran]], [[claude-model-family]]

## Concepts Extracted
- [[harness-design]], [[context-anxiety]], [[self-evaluation-bias]], [[multi-agent-architecture]], [[assumptions-expire]]

## Source File
`raw/2026-04-06-anthropic-harness-design-long-running-apps.md`
