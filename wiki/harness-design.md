---
type: concept
created: 2026-04-06
last-updated: 2026-04-15
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-07-repo-claude-memory-compiler.md
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, architecture, agentic]
---

# Harness Design

## Summary
The practice of designing multi-agent architectures (harnesses) around LLMs to achieve production-quality outputs on complex, long-running tasks. Inspired by GAN-style generator-evaluator loops. Core insight: decomposition into specialized roles (planner, generator, evaluator) outperforms monolithic single-agent approaches.

## Details
- **Core problem**: Naive single-agent approaches fail on long-running tasks due to [[context-anxiety]] and [[self-evaluation-bias]]
- **GAN-inspired solution**: Separate generation from evaluation — a generator produces, an evaluator critiques, quality improves iteratively over 5-15 rounds
- **Three-agent architecture** for full-stack coding:
  - **Planner**: Transforms brief prompts into ambitious specs, emphasizes deliverables over implementation
  - **Generator**: Works in feature-focused sprints (React, Vite, FastAPI, SQLite/PostgreSQL), self-evaluates before handoff
  - **Evaluator**: Uses Playwright MCP to test like a user — navigates UI, tests APIs, checks database state. Negotiates [[sprint-contracts]] defining success criteria before implementation
- **Performance**: Solo agent = 20 min / $9 (broken output). Full harness = 6 hours / $200 (functional, polished output)
- **Evolution**: As models improve (Sonnet → Opus), strip away components that are no longer load-bearing — [[assumptions-expire]]
- **Evaluation tuning**: Out-of-the-box Claude QA agents approve mediocre work. Requires multiple calibration cycles against human judgment.
- **Claude Code as concrete harness**: [[claude-code|Claude Code]] implements the harness pattern with 6 pillars. Its core design principle: "LLM as reasoning center; Harness provides perception, action, memory, and constraints." The [[query-loop]] (12-step state machine), [[context-management]] (4-layer compression), and [[permission-system]] (7-layer defense) are the harness infrastructure.
- **Formal definition** (Pachaar/Chawla): "The complete software infrastructure wrapping an LLM, including orchestration, tools, memory, context management, state persistence, error handling, and guardrails." The model is the CPU; the harness is the OS.
- **11 production components**: [[orchestration-loop]], tools, memory, [[context-management]], prompt construction, output parsing, state management, error handling, guardrails, [[verification-loops]], subagent orchestration
- **7 architectural decisions**: single vs multi-agent, ReAct vs plan-and-execute (3.6x speedup), context strategy, verification approach, permission architecture, tool scoping, harness thickness
- **Benchmark proof**: LangChain jumped from outside top-30 to #5 on TerminalBench 2.0 by modifying only the harness — same model
- **Thin vs thick harness**: Thin bets on model improvement; graph frameworks (LangGraph) bet on explicit control. Both valid depending on model trajectory.
- **[[ralph-wiggum|Ralph Loop]]** pattern: Same prompt runs in a loop against PRD + progress file. Agent chooses the task, not the human. Two modes: HITL (watch and intervene) and AFK (set and forget, capped iterations). [[matt-pocock|Matt Pocock]] documents 11 practical tips: scope definition with JSON `passes` field, progress tracking via `progress.txt`, mandatory [[verification-loops|feedback loops]], small steps to avoid [[context-rot]], Docker sandboxes for AFK safety. Key principle: "The repo wins" — agents amplify existing code quality ([[software-entropy]]). Alternative loops: test coverage, linting, duplication, entropy reversal.

- **Harness as memory system**: [[claude-memory-compiler]] demonstrates harness providing persistent memory via hooks — [[zero-friction-capture]] (automatic), [[time-gated-compilation]] (efficient), [[index-over-rag]] (retrieval). The harness doesn't just orchestrate tasks; it accumulates and retrieves knowledge across sessions.

- **The 4th layer — [[infrastructure-layer]]**: Rohit (@rohit4verse) argues the standard 3-layer model (weights, context, harness) misses a critical 4th layer: infrastructure. Multi-tenancy, RBAC, resource isolation, state persistence, distributed coordination. "Most teams talk about the first three because they are interesting. The fourth is where products die." Claude Code is the first agent system taking all four seriously. Retrofitting infrastructure is 10x harder than designing for it from day one.

- **[[thin-harness-fat-skills|Thin harness, fat skills]]** ([[garry-tan|Garry Tan]], 2026-04-11): The strongest articulation of *which* harness to build. Push intelligence **up** into reusable markdown skills (parameterized via [[skill-as-method-call]]); push execution **down** into deterministic tools (see [[latent-vs-deterministic]]); keep the harness ~200 LOC doing only 4 things (loop, file I/O, context, safety). Triggered by reading the leaked Claude Code source (2026-03-31). Adds three composing concepts to harness theory: [[resolvers]] (context routing tables), [[diarization]] (the synthesis step that beats RAG), and skill-as-method-call. Garry's discipline rule: "If I have to ask you for something twice, you failed" — every recurring task must be codified into a skill.

- **Managed Agents — Anthropic productizes the harness**: [[claude-managed-agents]] (2026-04-09) is Anthropic's first-party managed harness service. Architecture decouples brain (Claude + stateless loop), hands (containers + tools), and session (append-only event log as source of truth). See [[managed-agents-architecture]]. Validates the harness-as-product thesis — developers get the [[infrastructure-layer]] for free. Research previews include [[managed-agents-outcomes]] (rubric-driven grading, separate grader context — the GAN-inspired evaluator role built into the platform) and [[managed-agents-multiagent]] (coordinator + thread delegation).

## Connections
- Related: [[multi-agent-architecture]], [[context-anxiety]], [[self-evaluation-bias]], [[Anthropic]], [[Prithvi Rajasekaran]], [[claude-code]], [[claude-managed-agents]], [[managed-agents-architecture]], [[managed-agents-outcomes]], [[managed-agents-multiagent]], [[query-loop]], [[context-management]], [[claude-memory-compiler]], [[zero-friction-capture]], [[compiler-analogy]], [[orchestration-loop]], [[verification-loops]], [[assumptions-expire]], [[akshay-pachaar]], [[infrastructure-layer]], [[boris-cherny]], [[ralph-wiggum]], [[matt-pocock]], [[software-entropy]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[latent-vs-deterministic]], [[resolvers]], [[diarization]], [[garry-tan]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation — full concept from engineering blog |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code as concrete harness implementation |
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Added harness-as-memory-system pattern |
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Added formal definition, 11 components, 7 decisions, benchmarks, Ralph Loop |
| 2026-04-09 | raw/2026-04-09-rohit-harness-from-claude-code-leaks.md | Added 4th layer (infrastructure) thesis |
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-engineering-blog.md | Added Managed Agents as Anthropic's productized harness |
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Expanded Ralph Loop with 11 practical tips, HITL/AFK modes, software entropy |
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Added Garry Tan's thin-harness-fat-skills thesis: 5 definitions, 3-layer architecture, "skills are permanent upgrades" discipline |
