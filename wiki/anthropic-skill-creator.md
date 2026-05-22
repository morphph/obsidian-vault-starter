---
type: entity
created: 2026-05-22
last-updated: 2026-05-22
sources:
  - raw/2026-05-22-repo-anthropics-skills.md
  - raw/2026-05-22-anthropic-equipping-agents-skills-blog.md
tags: [wiki, entity, claude-code, skills, meta-skill, anthropic, official]
---

# anthropic skill-creator

## Summary
Anthropic's **official meta-skill for creating, improving, and optimizing skills**, shipped in [[anthropics-skills-repo|github.com/anthropics/skills]] at `skills/skill-creator/SKILL.md`. Treats skill creation as a small ML problem — train/test split, baseline comparison, quantitative + qualitative double-rail evaluation, iteration workspaces, automated description optimization loop. The Anthropic-internal counterpart to [[skillify-meta-skill|Garry Tan's /skillify]]: same idea, different implementation (Garry: governance/verification; Anthropic: ML-style optimization). **The operational implementation of the "iterate with Claude" methodology Anthropic introduced in [[source-anthropic-equipping-agents-skills-blog|the original 2025-10-16 Skills announcement]].**

## Details

### The core loop (stated 3× in the SKILL.md file)
```
1. Figure out what the skill is about
2. Draft or edit the skill
3. Run claude-with-access-to-the-skill on test prompts
4. With the user, evaluate the outputs (quantitative + qualitative)
5. Improve based on feedback
6. Repeat until satisfied
7. Package and return
```

### The 4-question intent capture
1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases? **Objectively verifiable outputs → yes; subjective outputs (writing style, art) → often no.**

### ⭐ "Pushy description" — the official counter-intuitive guidance

> "Currently Claude has a tendency to **'undertrigger'** skills — to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit **'pushy'**."

| Version | Description |
|---|---|
| Too passive | "How to build a simple fast dashboard to display internal Anthropic data." |
| **Correct (pushy)** | "...**Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'**" |

**Important nuance:** combine with [[source-tw93-agent-architecture-engineering|Tw93's measured "Don't use when..." finding]] — pushy positives + explicit negatives is the complete pattern.

### The 4 improvement principles (the heart of the loop)

> **1. Generalize from the feedback.** "Rather than put in fiddly overfitty changes, or oppressively constrictive MUSTs... you might try branching out and using different metaphors, or recommending different patterns of working."
>
> **2. Keep the prompt lean.** "Make sure to read the transcripts, not just the final outputs — if it looks like the skill is making the model waste a bunch of time doing things that are unproductive, you can try getting rid of the parts of the skill that are making it do that."
>
> **3. Explain the why.** "If you find yourself writing **ALWAYS or NEVER in all caps**, or using super rigid structures, that's a **yellow flag** — if possible, reframe and explain the reasoning."
>
> **4. Look for repeated work across test cases.** "If all 3 test cases resulted in the subagent writing a `create_docx.py` or a `build_chart.py`, that's a strong signal the skill should bundle that script."

This is the operational equivalent of [[latent-vs-deterministic]] applied at the skill-improvement layer.

### Description Optimization Loop (the most distinctive piece)

1. Generate **20 trigger eval queries** — 8-10 should-trigger + 8-10 should-not-trigger
2. Queries must be **realistic** — file paths, personal context, column names, backstory, casual speech OK
3. Run via `scripts.run_loop`:
   - **60/40 train/test split**
   - Each query run **3 times** for reliable trigger rate
   - Claude proposes description improvements based on failures
   - Re-evaluates on both train and test
   - **Up to 5 iterations**, **select best by test score** (avoid overfitting)

**Why queries must be realistic:**

> Bad: `"Format this data"`, `"Extract text from PDF"`, `"Create a chart"`
>
> Good: `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think"`

**For should-not-trigger queries:** the most valuable are **near-misses** — share keywords but need something different. Obviously-irrelevant negatives ("write a fibonacci function" as a negative test for a PDF skill) test nothing.

### How skill triggering actually works (important nuance)
> "Claude only consults skills for tasks it can't easily handle on its own — simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly. **Complex, multi-step, or specialized queries reliably trigger skills when the description matches.**"

Implication: trigger eval queries must be **substantive**.

### Quantitative workspace structure (load-bearing)
```
<skill-name>-workspace/
├── iteration-1/
│   ├── eval-0/
│   │   ├── with_skill/outputs/
│   │   ├── without_skill/outputs/   # baseline for new skill
│   │   ├── eval_metadata.json
│   │   ├── timing.json
│   │   └── grading.json
│   └── eval-1/ ...
│   ├── benchmark.json
│   └── benchmark.md
└── feedback.json
```

**Critical rules:**
- Spawn with-skill AND baseline **in the same turn, in parallel** — don't sequence them
- Baseline depends on context: new skill → no-skill baseline; improving → snapshot the old version
- Use field names `text`, `passed`, `evidence` **exactly** — the viewer depends on them
- Aggregate via `python -m scripts.aggregate_benchmark` to get **mean ± stddev** with delta

### Anthropic's own writing style guidance (in skill-creator)
- **Imperative form preferred**
- **Don't use heavy-handed MUSTs** — use theory of mind, explain the why
- **Make skills general, not super-narrow to specific examples**
- "Write a draft, then look at it with fresh eyes and improve"

### Communication style guidance (notable for user-tier ranging)
> "There's a trend now where the power of Claude is inspiring **plumbers to open up their terminals, parents and grandparents to google 'how to install npm'**."

Phrasing tiers:
- "evaluation" / "benchmark" — borderline OK
- "JSON" / "assertion" — wait for cues before using without explanation

### Platform-specific behavior
| Platform | Notes |
|---|---|
| **Claude Code** | Full workflow (subagents in parallel, browser viewer, description optimization) |
| **Claude.ai** | No subagents → run tests inline; no browser → inline review; skip quantitative benchmark; skip description optimization (no `claude -p`) |
| **Cowork (headless)** | Has subagents; use `--static <path>` for viewer; "GENERATE THE EVAL VIEWER BEFORE evaluating inputs yourself" (in all-caps in the file — unusual emphasis from Anthropic) |

### Updating existing skills (sharp practical rule)
- **Preserve the original name** — don't append `-v2`
- **Copy to writeable location before editing** — installed paths may be read-only
- **Stage in `/tmp/`** if packaging manually

### Comparison: skill-creator vs /skillify
| Dimension | skill-creator (Anthropic) | /skillify (Garry Tan) |
|---|---|---|
| Trigger | Manual ("I want to create a skill") | One word: "skillify this" |
| Sequencing | Pre-design (4-question interview) | Post-execution (do-then-extract) |
| Verification | ML-style train/test eval | 10-step checklist + check-resolvable + DRY audit |
| Description | Automated optimization loop | Manual "if-I-ask-twice" rule |
| Iteration | iteration-N workspace dirs | RESOLVER.md edits + re-test |
| Strength | Rigor (quantitative metrics) | Speed (one-sentence creation) |

**They are not competitors but complements.** Garry's approach maximizes per-skill velocity; Anthropic's maximizes per-skill quality.

## Connections
- Related: [[anthropics-skills-repo]], [[anthropic]], [[claude-code]], [[agent-skills-standard]], [[skillify-meta-skill]], [[trigger-evals]], [[skill-as-method-call]], [[thin-harness-fat-skills]], [[latent-vs-deterministic]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-22 | raw/2026-05-22-repo-anthropics-skills.md | Initial creation from anthropics/skills repo deep scan |
| 2026-05-22 | raw/2026-05-22-anthropic-equipping-agents-skills-blog.md | Cross-referenced as the operational implementation of "iterate with Claude" methodology introduced in Anthropic's foundational 2025-10-16 Skills announcement |
