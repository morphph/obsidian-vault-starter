# How to Ralph Wiggum — Official Playbook

**Source:** https://github.com/ghuntley/how-to-ralph-wiggum
**Author:** Geoffrey Huntley
**Fetch method:** WebFetch (GitHub repo)
**Date fetched:** 2026-04-15

---

## Overview

The official methodology repository documenting the AI-driven software development technique that uses Claude to automate coding tasks through iterative loops. Three phases, two prompts.

## Core Workflow — Three Phases

### Phase 1: Requirements Definition
Human and LLM collaborate to:
- Identify Jobs-to-Be-Done (JTBD)
- Break them into discrete topics
- Generate specification files in `specs/`

### Phase 2: Planning Mode
Claude analyzes specs versus existing code to produce `IMPLEMENTATION_PLAN.md` with prioritized tasks. Uses `PROMPT_plan.md`.

### Phase 3: Building Mode
Claude implements tasks from the plan, runs tests, commits changes, and updates the plan. Uses `PROMPT_build.md`.

## Key Files and Structure

| File | Purpose |
|------|---------|
| `loop.sh` | Bash script that continuously feeds prompts to Claude |
| `PROMPT_plan.md` | Planning mode instructions |
| `PROMPT_build.md` | Building mode instructions |
| `AGENTS.md` | Operational guide: build/test commands (~60 lines, kept brief) |
| `IMPLEMENTATION_PLAN.md` | Disposable, markdown-based task list updated by Claude |
| `specs/*` | Topic-specific requirement documents |

## Critical Principles

**Context Efficiency**: "Context is everything" when working within token limits. Tight task scope. Spawn subagents rather than loading everything into main context.

**Backpressure Mechanisms**: Tests, builds, and lints force Claude to fix issues before committing. The prompt says "run tests" generically; `AGENTS.md` specifies actual commands per project.

**Loop Control**: A simple bash loop restarts Claude with fresh context after each task. The persistent `IMPLEMENTATION_PLAN.md` file acts as shared state between iterations.

## Enhanced Loop Script

The repository provides a sophisticated shell script supporting:
- Mode selection (`plan` vs `build`)
- Iteration limits
- Automatic git pushes
- Claude CLI flags like `--dangerously-skip-permissions` for autonomous operation

## Advanced Enhancements

### Acceptance-Driven Backpressure
Derive test requirements from acceptance criteria during planning, preventing incomplete implementations.

### Non-Deterministic Testing
Using LLM-as-judge for subjective criteria (tone, aesthetics) with binary pass/fail reviews. "Is this UX good?" as a test.

### Work-Scoped Branches
Create focused `IMPLEMENTATION_PLAN.md` files per feature branch rather than filtering at runtime.

### JTBD → Story Map → SLC Release
Structure releases around Simple/Lovable/Complete principles aligned with audience needs. Not MVP (Minimum Viable Product) but SLC (Simple, Lovable, Complete).

## Key Language Patterns for Prompts

The prompts use specific phrasing Claude learns to follow:
- "study" (not "read") — implies deeper analysis
- "don't assume not implemented" — forces codebase search
- "using parallel subagents" — triggers parallelization
- "capture the why" — documents reasoning
- "keep it up to date" — maintains living documentation

## Operational Philosophy

**"Let Ralph Ralph"** — Trust the LLM to self-correct through iteration. The plan is disposable; regenerate when wrong. Observe patterns, add signs for improvement, and tune like a guitar rather than prescribing everything upfront.

The methodology aims to reduce development costs while maintaining code quality through automated iteration, intelligent backpressure, and human oversight of the loop rather than individual tasks.
