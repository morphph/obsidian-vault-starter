---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-anthropic-managed-agents-docs.md
tags: [concept, agents, verification]
---

# Managed Agents Outcomes

## Summary
Research preview feature of [[claude-managed-agents]] that elevates sessions from conversation to goal-directed work. You define what "done" looks like via a rubric; a separate grader agent evaluates the artifact and feeds gaps back to the working agent for iteration. Essentially a productized version of the [[verification-loops]] pattern.

## Details

### How It Works
- Define a rubric: markdown document with explicit, gradeable per-criterion scoring
- Send `user.define_outcome` event with description, rubric, and optional `max_iterations` (default 3, max 20)
- Harness provisions a **grader** in a separate context window (avoids bias from main agent's implementation)
- Grader returns per-criterion breakdown: satisfied or specific gaps
- Feedback loops back to agent for next iteration

### Evaluation Results
| Result | What Happens |
| --- | --- |
| `satisfied` | Session → idle. All criteria met. |
| `needs_revision` | Agent starts new iteration with grader feedback. |
| `max_iterations_reached` | One final revision, then idle. |
| `failed` | Rubric/task mismatch. Session → idle. |
| `interrupted` | User interrupted during evaluation. |

### Rubric Best Practices
- Structure as explicit, gradeable criteria (not "the data looks good")
- Each criterion scored independently
- Can use Files API to upload rubrics for reuse across sessions
- For bootstrapping: give Claude a known-good artifact, ask it to analyze what makes it good, turn analysis into rubric

### Deliverables
- Agent writes to `/mnt/session/outputs/`
- Fetch via Files API scoped to session after completion

### Connection to Existing Concepts
- Productizes the [[verification-loops]] pattern (rules-based, visual, LLM-as-judge)
- Addresses [[self-evaluation-bias]]: separate grader context avoids the "approving own mediocre work" trap
- The grader is essentially the "evaluator" role from [[harness-design]]'s GAN-inspired architecture, now built into the platform

## Connections
- Related: [[claude-managed-agents]], [[verification-loops]], [[self-evaluation-bias]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Initial creation from outcomes documentation |
