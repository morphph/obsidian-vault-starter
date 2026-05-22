---
type: concept
created: 2026-04-19
last-updated: 2026-05-22
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
  - raw/2026-04-21-anthropic-agent-skills-docs.md
  - raw/2026-04-21-garry-tan-skillify-manifesto.md
  - raw/2026-05-22-repo-anthropics-skills.md
tags: [wiki, principle, agentic, eval, governance]
---

# Trigger Evals

## Summary
[[garry-tan|Garry Tan]]'s pattern for testing a [[resolvers|resolver]]: a test suite of ~50 sample inputs with expected skill outputs. Not evaluating the skill's output; evaluating whether **the right skill fires for the right input**. Two failure modes — false negative (skill exists but doesn't fire) and false positive (wrong skill fires because triggers overlap). Both fixable by editing the trigger description in markdown. **In production ([[gbrain]]), this is implemented as `skills/testing/SKILL.md` — a three-way integrity check across `manifest.json` ↔ `RESOLVER.md` ↔ each `SKILL.md`, plus a MECE-violation check for overlapping triggers.**

## Details

### The test suite format (Garry's examples)
```
Input: "check my signatures"
Expected: executive-assistant (signature section)

Input: "who is Pedro Franceschi"
Expected: brain-ops → gbrain search

Input: "save this article to brain"
Expected: idea-ingest + RESOLVER.md
```

### Two failure modes
| Mode | Cause | Fix |
|------|-------|-----|
| **False negative** | Trigger description doesn't match how users phrase things | Rewrite the trigger description |
| **False positive** | Two skills have overlapping triggers | Disambiguate descriptions; add priority |

### Garry's rule
> Make sure the resolver is tested and also there are proper eval LLM tests for all the prompts and skills that use the resolver.
>
> If you can't prove the right skill fires for the right input, you don't have a system. You have a collection of skills and a prayer.

### Why this matters for agent architecture
In a [[thin-harness-fat-skills]] system, routing is done by **natural-language matching of user intent to skill `description` fields** (this is the resolver — see [[resolvers]]). Without tests, the resolver silently drifts ([[context-rot]]) and the only person who knows which skill handles which request is the builder who wrote it. That's a person with a filing cabinet, not a system.

### Where this sits in the resolver governance stack
| Layer | Purpose |
|-------|---------|
| [[resolvers]] (doc) | Routing table |
| **Trigger evals** | Does the right skill fire? |
| [[check-resolvable]] | Is every skill *reachable* at all? |
| Self-healing RLM loop (future) | Rewrites the resolver from observed traffic |

### Concrete parallel: Claude Code's skill descriptions
[[claude-code]]'s skill `description` field is the canonical resolver. Every description is a trigger. Trigger evals are how you'd verify that `/ship`, `/lint`, `/ingest` fire on the right intents without the user having to remember exact command names.

### The production shape: three-way integrity check
From [[gbrain]]'s `skills/testing/SKILL.md` (2026-04-21 deep scan):

> **Contract. This skill guarantees:**
> - Every skill directory has a SKILL.md file
> - Every SKILL.md has valid YAML frontmatter (name, description)
> - Every SKILL.md has required sections (Contract, Anti-Patterns, Output Format)
> - `manifest.json` lists every skill directory
> - `RESOLVER.md` references every skill in the manifest
> - **No MECE violations (duplicate triggers across skills)**
>
> Automated: `bun test test/skills-conformance.test.ts test/resolver.test.ts`

**Key insight:** trigger-evals in production is not "50 sample inputs" — it's a **three-layer integrity check**:

1. `manifest.json` must list every `SKILL.md` in the tree
2. `RESOLVER.md` must have a trigger row for every entry in `manifest.json`
3. Every `SKILL.md` must have the required sections + valid frontmatter

Plus a **MECE check**: no two skills can have overlapping triggers.

This is cheaper than 50 LLM-based eval runs and catches most of the same failures. **Start with integrity checks; add LLM evals only where integrity is passing but routing still drifts.**

### Anthropic's user-facing debugging playbook
From the [[agent-skills-standard|Claude Code Skills docs]]:

**Skill triggers too often (false positive):**
> 1. Make the description more specific
> 2. Add `disable-model-invocation: true` if you only want manual invocation

**Skill doesn't trigger (false negative):**
> 1. Check the description includes keywords users would naturally say
> 2. Verify the skill appears in `What skills are available?`
> 3. Try rephrasing your request to match the description more closely

This is the manual version; trigger-evals automate it.

### 50+ test-case examples from the Skillify Manifesto
Real eval cases from Garry's [[source-garry-tan-skillify-manifesto|2026-04-21 piece]]:

```js
{ intent: 'check my signatures',      expectedSkill: 'executive-assistant' },
{ intent: 'who is Pedro Franceschi',   expectedSkill: 'brain-ops' },
{ intent: 'save this article',         expectedSkill: 'idea-ingest' },
{ intent: 'what time is my meeting',   expectedSkill: 'context-now' },
{ intent: 'find my 2016 trip',         expectedSkill: 'calendar-recall' },
```

**Run as both** structural tests (does `AGENTS.md` table contain the right mapping?) **and** LLM-routing tests (given this intent, does the model actually pick the right skill?). Both layers matter — the table can be correct and the model can still route wrong because the trigger description is vague.

### Most honest test-case discovery heuristic
> "**Search your conversation history for when you said 'fucking shit' or 'wtf.' Those are the test cases you're missing.**"

This is Garry's actual recommended primary source for new eval cases — the moments of frustration are the empirical proof of routing or output failures that escaped tests.

### Test the process, not just the output
A particularly sharp eval pattern: feed the agent a question that requires deterministic work, then check **whether it ran the script or tried to do the math in its head.** For `context-now`, one eval feeds: *"hey, my flight leaves in about 45 minutes, will I make it to SFO?"* — if the agent takes the bait and computes the time itself instead of calling `context-now.mjs`, **the eval fails even if the math happens to be right** (because next time it won't be).

This is the [[latent-vs-deterministic|latent-vs-deterministic]] line enforced at eval time.

### ⭐ Anthropic's production-grade implementation (2026-05-22)

[[anthropic-skill-creator]] ships an automated trigger-eval loop in the official Anthropic Skills repo. **Three additions over Garry's manual version:**

**1. The query design specification (good vs bad)**

The queries must be **realistic** — what a real user would actually type, with file paths, personal context, column names/values, company names, URLs, backstory. Casual speech, lowercase, abbreviations, typos all OK.

> Bad: `"Format this data"`, `"Extract text from PDF"`, `"Create a chart"`
>
> Good: `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think"`

**2. The eval set composition**: 20 queries total = 8-10 should-trigger + 8-10 should-not-trigger. The **most valuable should-not-trigger queries are near-misses** — share keywords with the skill but actually need something different. Obviously-irrelevant negatives ("write a fibonacci function" as a negative test for a PDF skill) test nothing.

**3. The optimization protocol**:
- **60/40 train/test split**
- Each query run **3 times** for reliable trigger rate (variance matters)
- Claude proposes description improvements based on failures
- Re-evaluates on both train and test
- **Up to 5 iterations**
- **Select best by test score** (not train) to avoid overfitting

Tooling:
```bash
python -m scripts.run_loop \
  --eval-set <trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-session> \
  --max-iterations 5 --verbose
```

**4. Critical nuance about triggering** (changes how you write queries):

> "Claude only consults skills for tasks it can't easily handle on its own — simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly. **Complex, multi-step, or specialized queries reliably trigger skills when the description matches.**"

Implication: simple queries are **poor test cases** regardless of description quality. Eval queries must be **substantive** to test description discrimination.

**Three-tier rigor stack:**
| Tier | Approach | Cost |
|---|---|---|
| **Minimum viable** | Three-way integrity check ([[gbrain]] pattern) — manifest ↔ resolver ↔ SKILL.md + MECE | Cheap, deterministic |
| **Production** | Garry's 50-input manual eval suite | Medium, manual |
| **High-stakes** | Anthropic's 20-query / 60-40 / 3× / 5-iter automated loop | Expensive (LLM calls), best for skills used >100×/month |

## Connections
- Related: [[resolvers]], [[check-resolvable]], [[context-rot]], [[agent-skills-standard]], [[gbrain]], [[garry-tan]], [[thin-harness-fat-skills]], [[verification-loops]], [[llm-judgment-vs-scripts]], [[openclaw]], [[claude-code]], [[skillify-meta-skill]], [[latent-vs-deterministic]], [[anthropic-skill-creator]], [[anthropics-skills-repo]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Reframed as "three-layer integrity check" based on GBrain's `skills/testing/SKILL.md`; added MECE check |
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Added Anthropic's user-facing false-positive / false-negative debugging playbook |
| 2026-05-12 | raw/2026-04-21-garry-tan-skillify-manifesto.md | Added 50+ test-case examples (production format); "fucking shit / wtf" eval-discovery heuristic; "test the process not just the output" pattern |
| 2026-05-22 | raw/2026-05-22-repo-anthropics-skills.md | Added Anthropic's production-grade implementation: realistic query design spec (good vs bad examples), 8-10/8-10 should-trigger/should-not-trigger composition (near-misses most valuable), 60/40 train/test + 3× repeats + 5-iter automated loop selecting by test score, critical triggering nuance (simple queries don't trigger regardless of description quality), three-tier rigor stack (integrity check → Garry's manual → Anthropic's automated) |
