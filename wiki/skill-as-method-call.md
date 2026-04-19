---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, principle, skills, agentic]
---

# Skill as Method Call

## Summary
[[garry-tan|Garry Tan]]'s reframing: a skill file is not a prompt — it's a method definition. It encodes a **process of judgment**, takes **parameters** at invocation, and produces **radically different capabilities** depending on what arguments you pass. Markdown is the programming language; human judgment is the runtime.

## Details

### The reframe
- Most people treat skill files as elaborate prompts. Wrong frame.
- Correct frame: a skill file is a method. It has a signature (parameters), a body (the procedure), and behavior that varies by argument.
- "The skill describes a process of judgment. The invocation supplies the world."

### Worked example: `/investigate`
Same skill file. Seven steps: scope dataset → build timeline → diarize every document → synthesize → argue both sides → cite sources. Three parameters: TARGET, QUESTION, DATASET.

| TARGET | QUESTION | DATASET | Resulting capability |
|---|---|---|---|
| Safety scientist | Was a whistleblower silenced? | 2.1M discovery emails | Medical research analyst |
| Shell company | Coordinated donations? | FEC filings | Forensic political investigator |

Same seven steps. Same markdown file. Different worlds.

### Three matching-skill invocations (YC example)
| Invocation | Population | Strategy |
|---|---|---|
| `/match-breakout` | 1,200 founders | Sector clusters, 30/room — embedding + deterministic assignment |
| `/match-lunch` | 600 founders | Serendipity across sectors, 8/table, no repeats — LLM invents themes, deterministic seats |
| `/match-live` | Whoever's in the building | 200ms nearest-neighbor, 1:1, exclude met-before pairs |

One skill, three rooms.

### Why this matters
- **Compounds with model improvements.** When the next model drops, every skill instantly gets better — judgment in latent steps improves, deterministic steps stay reliable.
- **Encapsulates capability better than source code.** Markdown describes process, judgment, and context in the language the model already thinks in.
- **Refutes the "prompt engineering" framing.** This is software design with markdown as the language.
- **Justifies skill files as permanent assets.** Every skill you write is a permanent upgrade. Doesn't degrade. Doesn't forget. Runs at 3 AM.

### Practical implication for this wiki
Every command in `.claude/commands/` (`/ingest`, `/draft`, `/lint`, `/query`, `/visualize`, `/ingest-anthropic-daily`) already follows this pattern: the command is the procedure; the user supplies the URL/topic/window as the parameter. The article makes the pattern explicit and invocable as a design discipline.

## Connections
- Related: [[thin-harness-fat-skills]], [[garry-tan]], [[resolvers]], [[diarization]], [[harness-design]], [[claude-code]], [[llm-judgment-vs-scripts]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation |
