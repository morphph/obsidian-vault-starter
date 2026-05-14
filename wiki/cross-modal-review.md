---
type: concept
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
tags: [wiki, principle, agentic, eval, quality, multi-model]
---

# Cross-Modal Review

## Summary
[[garry-tan|Garry Tan]]'s name for **multi-model quality review** as a production skill in [[gbrain]]. Same output, three different model families, three different failure modes scored independently: **Opus 4.7 1M for precision** (factual errors), **GPT-5.5 for recall** (missing context), **DeepSeek V4-Pro for "generic" detection** (AI slop). The fix for [[self-evaluation-bias|self-evaluation bias]]: a model can't reliably grade itself, but cross-family scoring approximates an independent judge. The skill that caught the three factual errors in Garry's first [[book-mirror]] before he shipped it.

## Details

### The three scoring axes (and which model is good at each)
| Axis | What it catches | Model | Why |
|------|-----------------|-------|-----|
| **Precision** | Factual errors, hallucinated details | Opus 4.7 1M | Best instruction following; literal verification against source docs |
| **Recall** | Missing context, omitted key facts | GPT-5.5 | Exhaustive extraction; surfaces what the primary model left out |
| **Genericness** | Sounds like every other AI-generated piece | DeepSeek V4-Pro | Trained on a different mix; sees common-mode AI patterns the other two emit |

Each model produces a score 0-10 on its axis. Any axis below threshold → kick back for rewrite ([[quality-gate-loop]]).

### Why "cross-modal" — three failures live in three different model families
The naming references that the three errors are best caught by models from different *labs*, not different *modes* of the same model. Independent training data, independent fine-tuning objectives, independent confabulation patterns. Same output, three orthogonal lenses.

### Where it sits in the [[skillify-meta-skill|Skillify]] 10-step checklist
**Step 5: LLM evals.** Cross-modal review is the production implementation of "LLM-as-judge" — except instead of one judge, three judges from different families.

### Concrete failure pattern caught (from [[book-mirror]])
Garry's first book-mirror of Pema Chödrön's *When Things Fall Apart* shipped V1 with three factual errors about his own family:
- Said his parents were divorced (they weren't)
- Said he grew up in Hong Kong (he was born in Canada)
- Generic "this applies to leaders" mapping instead of cited specifics

Adding cross-modal-eval to the skill caught all three:
- **Precision check** (Opus) cross-referenced family facts against brain pages → caught divorce/birthplace errors
- **Recall check** (GPT-5.5) noticed the right-column mapping had no specific brain-page citations
- **Genericness check** (DeepSeek) flagged "this applies to leaders" as common-mode AI output

Every subsequent book-mirror inherits these checks. **One fix, all future mirrors covered.**

### Sibling to [[self-evaluation-bias]]
The original failure mode: an LLM grading its own output trends toward 7/10 on every axis, regardless of true quality. The defense:
1. Use a different prompt / different role for the judge (weak)
2. Use a different model from the same family (medium)
3. **Use a different model from a different family** (cross-modal-review) ← strongest

This is the production implementation of "multi-agent evaluation," generalized beyond GAN-style adversarial pairing.

### Cost-aware deployment
Garry runs cross-modal-review on outputs that ship to him as final products (book-mirror, weekly briefing, meeting prep). Not on every micro-task — that would burn tokens with no proportional benefit. **Use where the cost of a single wrong output is high.**

### How this fits this vault
- Our `/draft` command currently does single-pass generation. Adding a cross-modal-review pass would catch voice-mismatch / factual-drift before publication.
- Our `/ingest` could optionally cross-modal-check Chinese 要点解读 sections against the raw article — useful when ingesting longer pieces where the summary is doing real synthesis.
- Cheap variant: a single "second judge" using a different model than the writer (not full three-model cross-modal). Captures most of the benefit at one-third the cost.

## Connections
- Related: [[garry-tan]], [[gbrain]], [[skillify-meta-skill]], [[quality-gate-loop]], [[book-mirror]], [[self-evaluation-bias]], [[verification-loops]], [[trigger-evals]], [[multi-agent-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Initial creation — extracted from "book-mirror got better through iteration" section |
| 2026-05-14 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Added cross-modal-review SKILL.md as production reference in GBrain's skills directory |
