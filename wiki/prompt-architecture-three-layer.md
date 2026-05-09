---
type: concept
created: 2026-05-09
last-updated: 2026-05-09
sources:
  - raw/2026-05-05-khairallah-3-ai-agents-replace-first-hires.md
tags: [wiki, principle, agentic, prompt-engineering]
---

# Three-Layer Prompt Architecture

## Summary
[[eng-khairallah|Khairallah]]'s framing for production agent prompts: **three explicit layers** — **System** (role + standards), **Workflow** (cycle steps), **Output** (format) — instead of one monolithic prompt. Each layer changes for different reasons, so they should be edited separately. This is a *prompt-engineering* sibling to the [[thin-harness-fat-skills|thin-harness/fat-skills]] *architectural* split: separate concerns by lifetime and authority.

## Details

### The three layers, with examples

**Layer 1 — System prompt** (defines the agent)
> *"It is an experienced market analyst specializing in your industry who produces concise, actionable intelligence briefs."*

- Role identity, expertise, voice, output standards, quality bar
- **Stable across cycles.** Changes when you reposition the agent or notice systemic quality issues.

**Layer 2 — Workflow prompt** (defines what it does each cycle)
> *"Check these sources. Look for these signals. Compare against last week's brief. Flag anything that changed. Prioritize by potential impact on the business."*

- Sequence of steps, sources to consult, comparisons to make, prioritization rule
- **Changes per cadence.** Edit when you want a different kind of cycle (e.g., add a new source).

**Layer 3 — Output prompt** (defines the format)
> *"Executive summary at the top. Three key developments with context. One recommended action per development. Links to sources. Everything on one page."*

- Layout, sections, length cap, tone, citation format
- **Changes most often.** Tune until "the brief is genuinely useful, not just long."

### Why three layers (not one big prompt)

| Layer | Change frequency | Authority | Failure mode if conflated |
|-------|------------------|-----------|---------------------------|
| System | Rarely | Founder / agent designer | If you mix output format into the system prompt, refining format means rewriting the agent's identity |
| Workflow | Per cadence | Operator | If you mix it into output, you can't change "what to check" without changing "what the brief looks like" |
| Output | Frequently | User-facing tuner | If you mix it into system, every UI tweak triggers full re-evaluation |

**Decoupling = independent iteration.** Same principle as the [[documentation-layers|documentation-layers]] table in this vault's CLAUDE.md.

### Mapping to Anthropic's Skills standard
The [[agent-skills-standard|Agent Skills standard]] enforces a parallel split:

| Khairallah's three-layer | Agent Skills (SKILL.md) |
|---|---|
| System prompt | YAML frontmatter (`name`, `description`, role-defining intro) |
| Workflow prompt | "Phases" / numbered steps in the markdown body |
| Output prompt | "Output Format" section (GBrain-style) or a final block in the body |

GBrain's mandatory `Contract / Phases / Output Format / Anti-Patterns` skill structure is **the three-layer architecture made structural**. See [[gbrain]].

### Mapping to the [[3-agent-starter-team]]

| Agent | Layer 1 (System) | Layer 2 (Workflow) | Layer 3 (Output) |
|-------|-----------------|---------------------|---------------------|
| Research | Senior market analyst for {industry} | Monday sweep: 10 competitors + industry news + social signals + diff-against-last-week | One-page brief: exec summary, 3 developments + actions, sources |
| Content | Voice-matched ghostwriter for {founder} | Monthly: 30 ideas from pillars + trends → drafts → quality gate → repurpose | Per-piece scoring (voice match / hook / value density / originality), repurposed variants |
| Operations | Chief of staff for {founder} | Daily: triage + pre-meeting brief + Friday report | Email categories with urgency, 1-page meeting brief, weekly metric snapshot |

### How to use it in this vault

The slash commands in `.claude/commands/` already partially follow this — but mostly fuse System and Workflow. Concrete suggestion: when next editing a slash command, **explicitly delineate the three layers** with H2 headers (`## Role`, `## Workflow`, `## Output Format`). Especially helpful for `/ingest`, `/draft`, and `/query`.

### What this is *not*

- Not a multi-pass prompting technique (chain-of-thought, ReAct, etc.) — those are runtime patterns
- Not a system/user-message split — those are API positions, not separation of concerns
- Not the same as [[skill-as-method-call|skill = method call]] (that's about parameterization). This is about *structure within a single prompt*.

## Connections
- Related: [[eng-khairallah]], [[3-agent-starter-team]], [[quality-gate-loop]], [[agent-skills-standard]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[gbrain]], [[documentation-layers]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-09 | raw/2026-05-05-khairallah-3-ai-agents-replace-first-hires.md | Initial creation |
