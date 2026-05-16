# Using Goals in Codex

**Source URL:** https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
**Authors:** Raj Pathak, Stefano Fabbri
**Published:** 2026-05-09
**Publisher:** OpenAI Developers Cookbook (official)
**Fetch method:** WebFetch

---

## Overview

**Goals** are persistent objectives in Codex that maintain focus on a defined outcome across multiple conversational turns. They provide a **completion condition** specifying what should be true, **how success is verified**, and **what constraints must remain intact**.

Goals work best for tasks where **subsequent steps depend on discovered information** — profiling, patching, benchmarking, flaky test reproduction, or research questions requiring evidence-based audits. They differ fundamentally from one-off prompts: rather than requesting immediate work, they establish **durable targets that Codex evaluates against concrete evidence.**

## Core Concepts

**The Basic Model:**

- **Prompt:** ask → work → result → wait
- **Goal:** work → check → continue or complete

Goals transform threads from isolated prompts into **stateful loops**. Codex continues automatically only when **idle, within budget, and when no user input is queued.**

## Getting Started

### Installation
```
npm install -g @openai/codex@latest
codex --version
```

### Basic Commands
```
/goal [objective]      Create or view current Goal
/goal pause            Pause active Goal
/goal resume           Resume paused Goal
/goal clear            Remove current Goal
```

### Example Goal
> "Reduce p95 latency below 120 ms without regressing correctness tests"

## Writing Effective Goals

Strong Goals define **six elements**:

1. **Outcome** — What should be true upon completion
2. **Verification surface** — Tests, benchmarks, artifacts, or reports proving success
3. **Constraints** — What must not regress
4. **Boundaries** — Permitted files, tools, data, or resources
5. **Iteration policy** — How to choose next steps after attempts
6. **Blocked stop condition** — When to halt and report blockers

### Weak vs Strong

**Weak Goal:**
> "Improve performance"

**Strong Goal:**
> "Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service and related tests. Between iterations, record changes, benchmark results, and next experiments to attempt. If blocked, stop with attempted paths, evidence, and blockers."

## When to Use Goals

### Appropriate
- Performance optimization
- Flaky test investigation
- Dependency migrations
- Multi-step bug reproduction
- Refactoring with test verification
- Research requiring final artifacts

### Not Appropriate
- One-line edits
- Simple explanations
- Code reviews
- Single-answer questions
- Tasks with vague finish lines

## Research Example: Paper Reproduction

For reproducing **"Deep Hedging"** by Buehler et al., the Goal was:

> "Produce strongest evidence-backed reproduction using available materials and local resources. Attempt headline results, verify outputs, and end with a report separating reproduced mechanics, approximate trained results, blocked exact replay, and remaining uncertainty."

This Goal enabled Codex to:
- Separate headline from supporting claims
- Map claims to available evidence
- Rebuild testable components
- Label irreproducible sections honestly

## Architecture

Goals are implemented as **thread-scoped persistent state**, not global memory. Key design features:

- **Thread-scoped:** Objectives belong to the thread containing relevant context
- **Event-driven continuation:** Codex checks for continuation only at safe boundaries
- **Evidence-based completion:** Objectives marked complete only after checking against concrete evidence
- **Budget-explicit:** Reaching budget limits stops substantive work and triggers summaries
- **Lifecycle controls:** Users manage pause, resume, clear operations

## Key Distinctions from Prompts

When Goals are active, three changes occur:

1. **Objectives remain visible across turns**
2. **Automatic continuation becomes possible** from idle threads
3. **Completion requires evidence-based verification**, not model confidence

A Goal remains active until marked complete, cleared, paused, or constrained by budget limits.
