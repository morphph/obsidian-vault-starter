---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-03-19-tw93-agent-architecture-and-engineering.md
tags: [wiki, principle, architecture, agentic, taxonomy]
---

# Agent vs Workflow (and the Five Patterns Underneath)

## Summary
Anthropic's clean definitional split, popularized in Chinese by [[tw93|Tw93]]: **a Workflow has its execution path written in code; an Agent has its execution path decided by the LLM at runtime**. The split is about *who holds control*, not about quality — many products labeled "Agent" are actually Workflows, and that's often the right choice. Most production systems are combinations of five canonical patterns: **Prompt Chaining · Routing · Parallelization · Orchestrator-Workers · Evaluator-Optimizer.**

## Details

### The single-sentence distinction
> **Workflow:** execution path is *pre-defined by code*. The LLM is called at specific steps.
>
> **Agent:** execution path is *dynamically determined by the LLM*. The LLM decides what to do next at each turn.

Neither is intrinsically better. **The right question is which pattern fits the task** — high-stakes regulated work usually wants more code-defined path; open-ended exploration needs more LLM control. Many "Agent" products on inspection are actually Workflows with one LLM step, and that's fine.

### The Five Patterns (Anthropic's taxonomy)

Most AI systems decompose into combinations of these five. Knowing the menu prevents you from reaching for "Agent" when a Workflow would do.

#### 1. Prompt Chaining (sequential)
Task split into ordered steps; each step processes the previous step's output. Can insert deterministic code checkpoints between steps.

**Examples:** generate-then-translate, outline-then-write, parse-then-validate.

**When:** linear workflow where each step's output is the next step's input, and steps are stable.

#### 2. Routing
Classify input; dispatch to specialized downstream flow. Trivial-but-decisive optimization at scale.

**Examples:** simple question → cheap model; complex question → expensive model. Tech support → support flow; billing → billing flow.

**When:** workload has obvious skill clusters and you want to assign the cheapest viable model per cluster.

#### 3. Parallelization
Two variants:
- **Sectioning:** task split into independent subtasks that run concurrently
- **Voting:** same task run multiple times; consensus wins

**When:** high-stakes decisions; need multiple perspectives; benefits exceed extra cost.

**Examples:** code-security review (security + quality + style independently); content moderation (multiple classifiers vote).

#### 4. Orchestrator-Workers
A central LLM dynamically decomposes the task and dispatches to worker LLMs; consolidates results. **This is the canonical "agentic" pattern** — the orchestrator's role is itself decided at runtime.

**Reference implementations Tw93 cites:**
- nanobot's `spawn` tool
- learn-claude-code's sub-agent pattern
- [[gbrain]]'s minion-orchestrator skill (see [[gbrain]])

**When:** task structure isn't known in advance; sub-task allocation needs reasoning.

#### 5. Evaluator-Optimizer
Generator produces; evaluator critiques; loop until threshold met. Same primitive as [[quality-gate-loop]] and [[verification-loops]].

**Examples:** translation polishing, creative writing, generated-code quality refinement.

**When:** quality criteria hard to express in deterministic code; iteration improves outcome.

### How the patterns combine
- **Routing → Orchestrator-Workers:** classify, then dispatch to specialized agent
- **Orchestrator-Workers + Evaluator-Optimizer:** generate via workers, evaluate centrally
- **Prompt Chaining inside a single Orchestrator-Worker leg:** breakdown of a sub-task
- **Voting (Parallelization)** can replace a single Evaluator-Optimizer pass when you want cheap consensus

The takeaway: **most production systems are combinations of these five**. Recognizing which combination you're using clarifies where to invest engineering effort.

### Practical decision rules (from Tw93's article)
- **Start with the simplest pattern that could work.** Prompt Chaining beats Orchestrator-Workers if the steps are knowable.
- **Don't reach for Agent (LLM-decides) when Workflow (code-decides) is reliable enough.** The control-by-LLM "tax" only pays off when you genuinely need runtime adaptation.
- **The model size doesn't determine the pattern.** A simple Routing step using a Haiku-class model is sometimes the entire product.

### Where this fits in the wiki
- **[[harness-design]]** — patterns describe *what's in the harness*, not how it runs
- **[[multi-agent-architecture]]** — Orchestrator-Workers is the foundational multi-agent pattern
- **[[verification-loops]]** + **[[quality-gate-loop]]** — Evaluator-Optimizer is the same shape
- **[[thin-harness-fat-skills]]** — Garry Tan's argument is essentially "make Orchestrator very thin, push intelligence into the workers' skill files"
- **[[claude-code-goal]]** + **[[agentic-loop-tracking-files]]** — `/goal` is Evaluator-Optimizer at the *turn* granularity, with the evaluator as a small fast model
- **[[plan-mode-as-tools]]** — within an Agent (pattern 4 or 5), mode transitions should still be tool calls, not prompt rewrites

### Why this matters
Builders often over-engineer to "Agent" when a Workflow would have been more reliable and cheaper. Tw93's framing — and Anthropic's underlying taxonomy — gives you the explicit menu so you can pick by task, not by hype.

## Connections
- Related: [[tw93]], [[harness-design]], [[multi-agent-architecture]], [[verification-loops]], [[quality-gate-loop]], [[thin-harness-fat-skills]], [[claude-code-goal]], [[orchestration-loop]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-03-19-tw93-agent-architecture-and-engineering.md | Initial creation — Anthropic-via-Tw93 framing of Workflow/Agent split + five canonical patterns |
