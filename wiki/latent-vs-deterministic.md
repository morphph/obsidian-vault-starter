---
type: concept
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, agentic, design-principle]
---

# Latent vs. Deterministic

## Summary
Every step in an agent system is either a **latent** computation (LLM judgment, synthesis, pattern recognition) or a **deterministic** computation (SQL, arithmetic, compiled code with reproducible outputs). Coined by [[garry-tan|Garry Tan]] as one of the five definitions in [[thin-harness-fat-skills]]. Putting the wrong work on the wrong side of this line is the **#1 design mistake in agent systems**. Closely parallel to (and sharper than) [[llm-judgment-vs-scripts]].

## Details

### The two spaces

| Space | Where it lives | What it's good for |
|---|---|---|
| **Latent** | LLM forward pass | Judgment, interpretation, synthesis, pattern recognition, argument |
| **Deterministic** | Code, SQL, arithmetic | Same input → same output, every time. Trust. Scale. Verification. |

> "Latent space is where intelligence lives. Deterministic is where trust lives."

### The canonical failure mode (Garry's example)
- LLM **can** seat 8 people at a dinner table, accounting for personalities and social dynamics ✓ (latent — judgment-rich, small)
- Ask it to seat **800** and it will hallucinate a seating chart that looks plausible but is completely wrong ✗
- Why: combinatorial optimization is a **deterministic problem forced into latent space**
- Fix: have the LLM invent the *theme* of each table (latent), then a deterministic algorithm assigns seats

### How to apply the test
For every step in an agent pipeline, ask:
- "Could this be done with a SQL query, a script, or arithmetic with the same answer every time?" → **deterministic side**
- "Does this require reading, weighing, and synthesizing across non-uniform inputs?" → **latent side**
- "Does the answer need to be the *same* twice?" → if yes, deterministic. If no (and shouldn't be), latent.

### The worst systems
- Force optimization, lookup, math into latent space (hallucination, drift, non-reproducibility)
- Force judgment into deterministic code (rigid rules, brittle, miss context)

### The best systems
- Are **ruthless** about the line
- Use latent space *only* for the irreducible judgment work
- Push everything else into deterministic infra below the harness

### Concrete pairings
| Task | Side | Why |
|---|---|---|
| "Cluster these 1,200 founders by sector" | Deterministic | Embeddings + k-means is reproducible |
| "Notice that Maria says 'observability' but builds 'billing'" | Latent | Cross-source synthesis, judgment-heavy |
| "Compute total $ donated by entity X across FEC filings" | Deterministic | SQL/SUM |
| "Decide whether the donations look coordinated" | Latent | Pattern recognition + argument |
| "Schedule 200 meetings, no one meets twice" | Deterministic | Constraint satisfaction |
| "Pick the *theme* of each meeting room" | Latent | Conceptual clustering |

### How this lands in our setup
- **Wiki ingest**: latent (synthesizing claims, detecting contradictions). Should NOT be turned into a script.
- **Index update**: deterministic (parse pages, write entries). Should NOT be a free-form LLM task.
- **Source dedup**: deterministic (filename hash). Should NOT be LLM-judged.
- **Drafting article structure**: latent (judgment about what's interesting). LLM-driven.
- **Compile.py time gate**: deterministic. The 6 PM check is a script, the synthesis is the LLM.

## Connections
- Related: [[thin-harness-fat-skills]], [[llm-judgment-vs-scripts]], [[harness-design]], [[garry-tan]], [[diarization]], [[skill-as-method-call]], [[verification-loops]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — Garry's framing of latent vs deterministic |
