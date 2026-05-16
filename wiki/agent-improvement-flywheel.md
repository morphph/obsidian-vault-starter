---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-12-openai-cookbook-agent-improvement-loop.md
tags: [wiki, principle, agentic, eval, optimization, observability, openai]
---

# Agent Improvement Flywheel (Trace → Feedback → Eval → Optimize → Harness Change)

## Summary
OpenAI Cookbook's 6-step closed-loop pattern (Wesley Pasfield, 2026-05-12) for **systematically improving an agent's harness over time**. Distinct from [[iterative-repair-loop]] (per-task) — this operates **per-system-version**. Traces execution → collects feedback → converts to reusable evals → ranks improvements via **HALO** optimization → outputs developer-facing change recommendations Codex can apply. **The thesis: preserve evidence at each step so improvements compound.** Most actionable for us: the **6-required-artifacts-per-run** pattern and the **trace-as-OpenTelemetry-span** model.

## Details

### The 6-step flywheel

1. **Synthetic data** — Build a realistic dataset that **includes conflicting signals** (e.g., structured exports vs narrative claims). Conflicts are where agents fail.
2. **Define the harness** — System prompt + tool policies + required artifacts + validation rules = the **runtime contract**
3. **Traced runs** — Execute on ~5 distinct questions, capture **OpenTelemetry-compatible traces**
4. **Feedback** — Human + LLM-generated, on those runs
5. **Convert to evals** — Observations → **Promptfoo** test cases (reusable)
6. **Optimize with HALO** — Rank harness improvements by impact
7. **Hand off to Codex** — Codex generates developer-facing change recommendations

### Why 5 traces per cycle (not 50 or 500)
**Cookbook timing: ~20 minutes for 5 complete traces with GPT-5.5.** 5 is enough to surface failure patterns without burning a workday. The compounding comes from **doing the cycle weekly**, not from sampling a huge corpus per cycle.

### The 6-Required-Artifacts pattern (worth stealing for our work)

Each traced run produces 6 artifacts:

| Artifact | Purpose |
|----------|---------|
| `summary_answer.md` | Concise answer (the "headline") |
| `investment_memo.md` | Detailed review with evidence sections |
| `risk_register.json` | Structured risks with supporting evidence |
| `open_questions.md` | Missing evidence and unresolved questions |
| `citations.json` | Machine-readable claim-to-source mapping |
| `evidence_table.csv` | Audit trail of claims and sources |

**The split between machine-readable (`.json` / `.csv`) and human-readable (`.md`) is the key design choice.** Eval pipelines parse the JSON; humans review the markdown.

### Trace as OpenTelemetry span (cross-platform observability)

Agents SDK span types → OpenTelemetry observation kinds:
- `agent` → AGENT
- `generation` / `response` → LLM
- `function` / `mcp_tools` → TOOL
- `handoff` → CHAIN

This means **agent execution traces sit in the same observability infrastructure as backend services** — same dashboards, same query languages, same retention. Powerful operationally.

### What HALO actually does (inferred — not fully disclosed)
**HALO** ranks **recommended harness improvements** by impact. Given a corpus of traces + feedback + evals, it surfaces which change to the harness would close the most failure modes. **It does NOT auto-apply changes** — it generates a prioritized list Codex then implements.

This pairs with the [[claude-code-goal|self-healing resolver]] idea Garry Tan floated — same principle (use observed traffic to evolve the system) at a different layer.

### Failure modes the cookbook explicitly targets

The diligence-agent example is designed to surface common failures:
- Treating management narrative as validated metric when structured data disagrees
- Reporting unvalidated estimates as if officially sanctioned
- Collapsing parent-account concentration into weaker legal-entity views
- Overstating certifications ("SOC 2 complete" when only Type I done)
- **Producing polished answers while leaving citations incomplete**

The last one is the agentic version of [[silent-fallback-antipattern]]: looks good, fails on inspection.

### Concrete tools / stack mentioned
- **OpenAI Agents SDK** for execution
- **Promptfoo** for evals (Node-based)
- **HALO** for optimization ranking
- **OpenTelemetry** JSON Lines for trace transport
- Local Python utilities:
  - `check_evidence_coverage.py` — audits citations against real files
  - `validate_output_contract.py` — verifies required artifacts exist with expected schema

### Comparison to wiki's existing loop patterns

| Pattern | Granularity | Cycle frequency |
|---------|-------------|------------------|
| [[verification-loops]] | Per-step / per-tool | Per-iteration |
| [[quality-gate-loop]] | Per-output quality | Per-output |
| [[iterative-repair-loop]] | Per-artifact iteration | Per-task |
| **Agent Improvement Flywheel** (this) | **Per-system-version** | **Weekly / monthly** |
| [[skillify-meta-skill]] | Per-skill creation | Ad-hoc, on failure |

### The deeper principle
> "**Preserves evidence at each step:**
> - **Traces** show what happened
> - **Feedback** explains what mattered
> - **Evals** make expectations reusable
> - **Optimization** produces the next harness version"

Each step turns ephemeral signal into durable infrastructure. **Without this chain, every improvement is one-off; with it, improvements compound.**

### Practical adoption for this vault
- Our wiki doesn't have an analogous loop yet — we have `/lint` for static checks but no execution traces
- **Lightest-weight adoption:** start producing 6-artifact runs from `/ingest` (we already produce raw + wiki pages + log entry; could add explicit `citations.json` and `evidence_table.csv` for ingested sources)
- **Heavier adoption:** add a weekly `/improve` workflow that walks recent `/lint` findings + ingest logs and proposes wiki convention updates

### What's missing from the cookbook write-up
- **HALO's actual optimization algorithm** isn't disclosed — it's positioned as a service/feature, not a paper
- **No baseline comparison numbers** — we don't know "improvement vs no flywheel" empirically
- **Read between the lines:** this is OpenAI selling Agents SDK + HALO. The pattern is real and generalizable, but the specific tooling is theirs.

## Connections
- Related: [[iterative-repair-loop]], [[verification-loops]], [[trigger-evals]], [[agent-evaluation-traps]], [[claude-code-goal]], [[agentic-loop-tracking-files]], [[skillify-meta-skill]], [[silent-fallback-antipattern]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-12-openai-cookbook-agent-improvement-loop.md | Initial creation — OpenAI Cookbook's 6-step trace-to-harness-change flywheel |
