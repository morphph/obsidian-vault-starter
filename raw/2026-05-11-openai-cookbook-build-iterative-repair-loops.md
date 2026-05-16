# Build Iterative Repair Loops with Codex

**Source URL:** https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex
**Author:** Shreekant Agrawal
**Published:** 2026-05-11
**Publisher:** OpenAI Developers Cookbook (official)
**Fetch method:** WebFetch

---

## Overview

This cookbook demonstrates **closed-loop agent workflows** where agents produce output, validate it, and use feedback to improve subsequent iterations. The example focuses on **documentation reliability** — detecting, repairing, and validating stale or broken API and SDK examples using intentionally outdated notebooks.

## Workflow Architecture — Three distinct phases

The repair process follows three distinct phases:

**Review Phase:** Inspects artifacts and returns **structured findings without editing files**.

**Repair Phase:** Applies focused edits to **copied** artifacts using findings and validation feedback.

**Validation Phase:** Runs relevant checks and reports remaining issues.

## Setup Requirements

The notebook requires Codex CLI installation and an `OPENAI_API_KEY` environment variable. Installation command:

```bash
npm install -g @openai/codex@0.130.0
```

Key configuration variables include `REPAIR_MODEL`, `COOKBOOK_CHAT_MODEL`, and `REPAIR_REASONING_EFFORT`.

## Structured Output Schemas

Each phase produces JSON following defined schemas:
- **Review findings**: artifact name, issue type, severity, description, suggested fixes
- **Repair outputs**: iteration number, changes made, unresolved items, updated artifact paths
- **Validation**: pass/fail status with case-by-case evidence and remaining deltas

## Business Rules Definition

The workflow operates under **explicit rules** covering preferred models, API modernization targets, and reader experience standards. Examples include:
- "client.chat.completions.create -> client.responses.create" (API modernization)
- Requirements that "included examples remain runnable with local data and the standard library"

## Iterative Execution

Testing with three sample notebooks demonstrates progression:

- **Iteration 1:** One notebook passes; deeper cases generate focused deltas
- **Iteration 2:** Medium-complexity fixture clears after validation feedback
- **Iteration 3:** Most complex case resolves with evidence-driven repairs

## Validation as Feedback

Validation **executes notebooks end-to-end**, capturing execution failures as structured feedback. **This grounds subsequent repairs in observed behavior rather than inference from diffs alone.**

## Production Considerations

Real implementations require:
- Clear stop conditions (validation passes, max iterations reached, delta stabilization)
- Complete audit trails for each pass
- Human review checkpoints for unresolved cases

## Broader Applications

The pattern applies beyond documentation:
- Protocol optimization
- Regulatory remediation
- Support article updates
- Code modernization

**The key principle remains separating judgment from proof through structured handoffs.**
