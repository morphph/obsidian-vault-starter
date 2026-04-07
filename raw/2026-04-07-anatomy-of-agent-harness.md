---
source-url: https://x.com/akshay_pachaar/status/2041146899319971922
blog-url: https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness
fetched: 2026-04-07
fetch-method: WebSearch + WebFetch (blog mirror)
author: Akshay Pachaar / Avi Chawla
title: The Anatomy of an Agent Harness
---

# The Anatomy of an Agent Harness

## Overview
Agent performance depends far more on infrastructure than model choice. When LangChain modified only the harness around an identical LLM, rankings jumped from outside top 30 to position 5 on TerminalBench 2.0.

## Core Definition
The agent harness is "the complete software infrastructure wrapping an LLM, including orchestration, tools, memory, context management, state persistence, error handling, and guardrails." Think of it as an operating system where the raw model is merely a CPU without RAM, disk storage, or I/O.

## The 11 Production Components

### 1. Orchestration Loop
The Thought-Action-Observation (TAO) cycle forms the heartbeat. It assembles prompts, calls the LLM, parses outputs, executes tool calls, and loops until completion. Anthropic describes this as a "dumb loop" where intelligence lives in the model.

### 2. Tools
Tools are defined as schemas injected into context. The harness handles registration, validation, sandboxed execution, and result formatting. Claude Code provides tools across six categories: file operations, search, execution, web access, code intelligence, and subagent spawning.

### 3. Memory
Multiple timescales exist: short-term (conversation history within sessions) and long-term (persisting across sessions). Claude Code uses lightweight indices (~150 characters), detailed topic files, and raw transcripts accessed via search.

### 4. Context Management
Performance degrades 30%+ when key content falls in mid-window positions. Production strategies include compaction (summarizing history), observation masking (hiding old outputs), just-in-time retrieval (dynamic loading), and subagent delegation (condensed summaries).

### 5. Prompt Construction
Hierarchical assembly includes system prompt, tool definitions, memory files, conversation history, and user message. Priority stacking ensures critical information remains accessible throughout context windows.

### 6. Output Parsing
Modern harnesses rely on native tool calling rather than free-text parsing. Models return structured `tool_calls` objects. Schema-constrained responses via Pydantic models add reliability for complex outputs.

### 7. State Management
LangGraph uses typed dictionaries flowing through graph nodes with reducers merging updates. Checkpointing enables resumption after interruptions. Claude Code employs git commits as checkpoints and progress files as scratchpads.

### 8. Error Handling
A 10-step process with 99% per-step success has only ~90.4% end-to-end success. Systems distinguish transient errors (retry with backoff), LLM-recoverable errors (return as ToolMessage), user-fixable errors (interrupt), and unexpected errors (bubble up).

### 9. Guardrails and Safety
Three-level enforcement: input guardrails (first agent), output guardrails (final output), and tool guardrails (every invocation). Claude Code independently gates ~40 discrete tool capabilities with permission checks before execution.

### 10. Verification Loops
Rules-based feedback (tests, linters), visual feedback (screenshots), and LLM-as-judge approaches improve quality by 2-3x. Separate subagents evaluate outputs using deterministic or inferential verification.

### 11. Subagent Orchestration
Execution models include Fork (identical copy), Teammate (separate terminal with mailbox), and Worktree (isolated git branch). OpenAI supports agents-as-tools for subtasks and handoffs for full control transfer.

## Key Architectural Decisions

Teams face seven critical choices:

1. **Single vs. multi-agent**: Maximize single agents first; split only when tools exceed ~10 overlapping functions
2. **ReAct vs. plan-and-execute**: ReAct interleaves reasoning/action (higher cost); plan-and-execute separates phases (3.6x speedup reported)
3. **Context management strategy**: Time-based clearing, summarization, masking, note-taking, or delegation
4. **Verification approach**: Computational (deterministic) vs. inferential (semantic)
5. **Permission architecture**: Permissive (fast, risky) vs. restrictive (safe, slow)
6. **Tool scoping**: Fewer tools often yield better results; Vercel removed 80% and improved performance
7. **Harness thickness**: Thin harnesses bet on model improvement; graph frameworks bet on explicit control

## The Scaffolding Principle

As models improve, harness complexity should decrease. Construction scaffolding enables workers to build structures they couldn't reach otherwise—but gets removed when complete. Models increasingly internalize capabilities that once required harness management.

## Practical Workflow

A single cycle flows through seven steps: prompt assembly (with important content positioned at beginning/end), LLM inference, output classification, tool execution (concurrent for read-only, serial for mutations), result packaging (errors returned as ToolMessages), context updates (with compaction triggers), and looping until termination.

Long-running tasks use the "Ralph Loop" pattern: an Initializer Agent sets up environment and progress files, while subsequent Coding Agents read git logs and progress files to orient themselves, completing high-priority features iteratively across multiple context windows.

## Framework Implementations

- **Anthropic Claude SDK**: Single `query()` function creating async iteration; "dumb loop" philosophy
- **OpenAI Agents SDK**: Runner class with async/sync/streamed modes; code-first workflow logic
- **LangGraph**: Explicit state graphs with conditional routing; evolved from deprecated AgentExecutor
- **CrewAI**: Role-based multi-agent with deterministic Flows backbone; orchestrates autonomous collaboration

## Bottom Line

"The harness is not a wrapper around a prompt. It is the complete system that makes autonomous agent behavior possible." When agents fail, examine infrastructure before blaming the model.
