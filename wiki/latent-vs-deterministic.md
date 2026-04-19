---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
  - raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md
tags: [wiki, principle, agentic, system-design]
---

# Latent vs Deterministic

## Summary
[[garry-tan|Garry Tan]]'s framing of what may be the most common mistake in agent design: every step in your system is either **latent** (intelligence — judgment, synthesis, pattern recognition) or **deterministic** (trust — same input, same output, every time). Putting work on the wrong side of the line is how systems fail. Synonym/sibling concept to [[llm-judgment-vs-scripts]] — same boundary, different vocabulary, different failure-mode emphasis.

## Details

### The two modes
| Mode | What it is | Where it lives | Examples |
|---|---|---|---|
| **Latent** | Intelligence | Inside the LLM | Judgment, synthesis, pattern recognition, ambiguous reasoning |
| **Deterministic** | Trust | Compiled code, SQL, scripts | Arithmetic, combinatorial optimization, file I/O, API calls |

### The canonical illustration
> An LLM can seat 8 people at a dinner table, accounting for personalities and social dynamics. Ask it to seat 800 and it will hallucinate a seating chart that looks plausible but is completely wrong. That's a deterministic problem — combinatorial optimization — forced into latent space.

### The rule
- **Worst systems**: put the wrong work on the wrong side of the line.
- **Best systems**: are *ruthless* about the line.

### Worked applications (from [[thin-harness-fat-skills]] YC example)
| Step | Side | Why |
|---|---|---|
| Read 6,000 founder profiles + spot SAYS-vs-ACTUALLY-BUILDING gap | Latent | Cross-document judgment; no keyword search finds it |
| Pull GitHub commits / SQL queries / browser tests | Deterministic | Same input, same output, every time |
| Decide "Santos and Oram are both AI infra but not competitors" | Latent | Domain judgment about company positioning |
| Assign 600 people to 8-per-table with no repeats | Deterministic | Combinatorial constraint satisfaction |
| Invent serendipity *themes* for each table | Latent | Creative synthesis |

### Relationship to [[llm-judgment-vs-scripts]]
- **Same line, different framing.** [[ryan-sarver|Sarver]] derived the rule from building Stella on [[openclaw]] in early April 2026; Garry articulated the same boundary in his April 11 article.
- **Sarver's emphasis**: failure mode of *trust*. Routing deterministic work through LLMs introduces stochastic errors in places that should be reliable; users lose trust.
- **Garry's emphasis**: failure mode of *capability*. Forcing combinatorial work into latent space produces hallucinated outputs that *look* plausible.
- **Together**: stochasticity damages both reliability (Sarver) and correctness (Garry). The convergent evolution itself is significant — see [[connection-llm-judgment-vs-scripts-and-harness-design]].

### Compounding benefit
Push intelligence up into [[skill-as-method-call|skills]] (latent), push execution down into deterministic tooling. Then **every model improvement automatically improves every skill, while the deterministic layer stays perfectly reliable** — see [[thin-harness-fat-skills]].

## Connections
- Related: [[llm-judgment-vs-scripts]], [[thin-harness-fat-skills]], [[garry-tan]], [[ryan-sarver]], [[harness-design]], [[diarization]], [[skill-as-method-call]], [[connection-llm-judgment-vs-scripts-and-harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation — Garry's framing |
| 2026-04-19 | raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md | Cross-linked to Sarver's earlier formulation |
