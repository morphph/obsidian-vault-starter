# Agent Improvement Loop with Traces, Evals, and Codex

**Source URL:** https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
**Author:** Wesley Pasfield
**Published:** 2026-05-12
**Publisher:** OpenAI Developers Cookbook (official)
**Fetch method:** WebFetch

---

## Overview

This notebook demonstrates **a complete improvement flywheel for AI agents**, integrating:
- Real execution traces
- Human and model feedback
- Automated evaluations
- Optimization
- → concrete harness changes

## Core Workflow (6-step flywheel)

1. **Create synthetic company data** — A realistic acquisition diligence dataset with structured exports and narrative documents that **can conflict**
2. **Define the agent harness** — System prompt, tool policies, required artifacts, validation rules — **the runtime contract**
3. **Generate traced runs** — Execute the agent on five distinct questions while capturing OpenTelemetry-compatible traces
4. **Add feedback** — Collect **human and LLM-generated** feedback on those runs
5. **Turn feedback into evals** — Convert observations into **Promptfoo** test cases
6. **Optimize with HALO** — Rank recommended harness improvements by impact
7. **Hand off to Codex** — Generate developer-facing change recommendations

## Key Components

### Agent Configuration
The agent operates as a **diligence analyst** reviewing fictional company materials. It requires:
- Strict dataroom grounding (files under `data/` only)
- Preference for structured exports over narratives when conflicts occur
- Citation of every material claim with workspace-relative paths
- **Six required output artifacts:** summary, memo, risk register, open questions, citations, and evidence table

### Validation Tools (two local Python utilities)
- `check_evidence_coverage.py` — Audits whether drafted claims cite real dataroom files
- `validate_output_contract.py` — Verifies required artifacts exist with expected JSON structure and valid citations

### Trace Export
The notebook implements a local **HALO-compatible JSON Lines exporter** that converts Agents SDK spans into OpenTelemetry format. **Preserves workflow context across multiple runs for later optimization analysis.**

## Execution Details

**Prerequisites:**
- Python 3.7+ with OpenAI SDK and agents library
- Node.js with `npx` for Promptfoo
- Valid `OPENAI_API_KEY` environment variable

**Timing:** ~20 minutes for five complete traces with default model (GPT-5.5)

**Model Configuration:**
- Agent execution: `gpt-5.5` (configurable via `OPENAI_AGENT_MODEL`)
- Analysis and feedback: `gpt-5.5` (configurable via `OPENAI_ANALYSIS_MODEL`)
- HALO optimization: `gpt-5.5` (configurable via `OPENAI_HALO_MODEL`)

## Artifact Structure (6 required artifacts per traced run)

| Artifact | Purpose |
|----------|---------|
| `summary_answer.md` | Concise answer for investment team |
| `investment_memo.md` | Detailed review with evidence sections |
| `risk_register.json` | Structured risks with supporting evidence |
| `open_questions.md` | Missing evidence and unresolved questions |
| `citations.json` | Machine-readable claim-to-source mapping |
| `evidence_table.csv` | Audit trail of claims and sources |

## Failure Modes Addressed

The notebook is designed to surface common agent failures:

- Treating management narrative as validated metric when structured data disagrees
- Reporting unvalidated estimates (like NRR) as if officially sanctioned
- Collapsing parent-account concentration into weaker legal-entity views
- Overstating security certifications (e.g., "SOC 2 complete" when only Type I done)
- Producing polished answers while leaving citations incomplete

## Implementation Notes

The harness uses **workspace-relative paths** for all shell commands. The agent runs in a Unix sandbox with mounted **read-only data and writable output directories**. Tool policies explicitly forbid modifying input files or agent configuration during execution.

### Trace exporter span mappings (Agents SDK → OpenTelemetry)
- `agent` → AGENT
- `generation` / `response` → LLM
- `function` / `mcp_tools` → TOOL
- `handoff` → CHAIN

## The Deeper Principle

**Preserves evidence at each step:**
- **Traces** show what happened
- **Feedback** explains what mattered
- **Evals** make expectations reusable
- **Optimization** produces the next harness version
