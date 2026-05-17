# 5 Agent Skills I Use Every Day

**Source:** https://www.aihero.dev/5-agent-skills-i-use-every-day
**Author:** Matt Pocock (AI Hero)
**Fetch method:** WebFetch
**Fetched:** 2026-05-17

## Premise

Matt's system of five agent skills imposes strict processes on AI agents that lack memory. Skills encode engineering best practices into reusable prompts.

## The Five

### 1. /grill-me — Deep Idea Exploration
Three-sentence skill: "interview relentlessly about every aspect of this plan."

Draws from Frederick P. Brooks' design tree — walks systematically through all branches before committing to implementation. Single conversation: 16–50 clarifying questions. Ensures shared understanding between human and AI before code is written.

### 2. /to-prd — Discussion → Specification
Transforms conversational understanding into PRD. Strategically skips unnecessary steps if already completed. Culminates in user stories written in Agile language. PRD becomes authoritative blueprint.

### 3. /to-issues — Plans → Executable Tasks
Vertical slices (thin features cutting through all integration layers), NOT horizontal layers. Surfaces unknowns quickly. Enables parallel work across multiple agents. Maps dependencies between tasks for scheduling.

### 4. /tdd — Test-Driven Implementation
Red-green-refactor: agents write tests before implementation. Matt: "the most consistent way to improve agent outputs." Emphasizes interface design for testability and deep modules with thin surface areas.

### 5. /improve-codebase-architecture — Structural Optimization
Regular scans for architectural weaknesses: unclear module boundaries, overcomplicated navigation, tightly coupled components. Suggests "deepening" shallow modules. "Garbage codebase input yields poor AI output."

## Integrated Workflow

```
grill-me  →  to-prd  →  to-issues  →  tdd  →  improve-codebase-architecture
   ↑                                                          │
   └──────────────────────────────────────────────────────────┘
```

Sequential pipeline with feedback loop. Each skill assumes output of previous one.

## About Matt
Nearly a decade of engineering experience. Created skills to address agents' lack of persistent memory between sessions.

## Connections

This article is the higher-level marketing version of the mattpocock/skills README. Same content, less code-focused; emphasizes the engineering philosophy. Useful as the "elevator pitch" version.
