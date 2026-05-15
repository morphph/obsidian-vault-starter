---
type: entity
created: 2026-05-15
last-updated: 2026-05-15
sources:
  - raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md
tags: [wiki, person, openai, ai-builder]
---

# Chris Hayduk

## Summary
**FDE (Forward Deployed Engineer), Life Sciences @ OpenAI** (X: @ChrisHayduk). First **OpenAI-insider** source in our wiki — useful counterweight to the heavy Anthropic / Claude Code skew of prior sources. Blog at chrishayduk.com. Most relevant contribution to date: a tight three-tip playbook for using Codex's `/goal` command effectively (2026-05-11, 188K views, 2.7K bookmarks).

## Details

### Role / position
- **FDE Life Sciences @ OpenAI** — Forward Deployed Engineer specifically embedded with life-sciences customers. Cross-disciplinary AI work + writing.
- Has internal use of Codex goal mode + side projects (protein-structure-model architecture search, NeurIPS→ICML paper conversion) — practitioner, not preacher
- Personal site: chrishayduk.com

### Single longform in wiki (so far)
**2026-05-11 — Using Codex Goals Effectively** ([[source-chrishayduk-codex-goals-effectively]]). Three tips for Codex's `/goal` command (the OpenAI parallel to Claude Code's [[claude-code-goal|/goal]]):
1. Specify a **clear, quantitative goal** — vague goals fail in either "give up early" or "flail forever" mode
2. **Tight feedback loop** — speed up scoring without compromising signal (smaller model + subsampled dataset)
3. **Three markdown files for tracking**: PLAN.md / EXPERIMENTS.md / SCRATCHPAD.md — see [[agentic-loop-tracking-files]]

### Why his voice matters
- **Cross-vendor convergence point**: Codex `/goal` and Claude Code `/goal` are nearly identical features by name and behavior. Chris's playbook is vendor-agnostic — applies to both [[claude-code-goal|Claude Code's /goal]] and Codex's `/goal`
- **Hands-on ML practitioner**: His protein-structure-model architecture search example shows the feedback-loop tightening principle as applied to days→minutes scoring reductions — a real ML researcher problem, not a toy
- **Plain operational advice without ideology**: Doesn't push OpenAI vs Anthropic. The advice generalizes

### Notable framing
> "We've gotten lazy as prompters in our everyday workflows. We can vaguely gesture at what we want GPT-5.5 to build... This prompting style, however, is a major failure mode I've seen when using goal mode."

The model improvement *enabled* sloppy prompting in chat mode. But sloppy prompting in loop mode **breaks the loop** because the evaluator can't decide when "done."

### Publishing pattern
X long-form articles on his own account. Blog at chrishayduk.com (cross-disciplinary AI writing). One single piece in our wiki so far; worth tracking for future Codex/OpenAI-insider perspective.

## Connections
- Related: [[claude-code-goal]], [[agentic-loop-tracking-files]], [[sprint-contracts]], [[verification-loops]], [[source-chrishayduk-codex-goals-effectively]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-15 | raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md | Initial creation — first OpenAI-insider source in wiki |
