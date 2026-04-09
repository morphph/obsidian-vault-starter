# Scaling Managed Agents: Decoupling the Brain from the Hands

Source: https://www.anthropic.com/engineering/managed-agents
Date: 2026-04-09
Author: Anthropic Engineering

## Overview

Claude Managed Agents is a hosted service within the Claude Platform designed for long-horizon agent work. The service runs agents on behalf of customers through "a small set of interfaces meant to outlast any particular implementation."

## Core Architecture: Decoupling Brain from Hands

The system decouples three main components:

1. **Brain** (Claude + Harness): The inference engine and control loop
2. **Hands** (Sandboxes + Tools): Execution environments and action mechanisms
3. **Session**: An append-only log of all events

This decoupling allows each component to fail or be replaced independently without affecting others.

### The Session as Durable State

- Session is a durable, append-only event log stored outside the harness
- Accessed via `getEvents()` to select positional slices of the event stream
- Enables flexible context interrogation
- Context durably stored in session log, lives outside Claude's context window

### The Harness as Stateless Loop

- Now stateless and provisioned separately from execution environments
- Calls Claude and routes tool calls to infrastructure
- Can be restarted or replaced without losing session state

### Tools as Uniform Interface

- Any executable target: containers, sandboxes, custom tools
- Called uniformly as `execute(name, input) → string`
- Events written via `emitEvent(id, event)` for durable transaction logs

## Performance Improvements

- p50 time-to-first-token (TTFT) improved ~60%
- p95 TTFT improved >90%
- Containers provisioned only when needed, not upfront
- Lazy provisioning eliminates cold-start penalty for sessions that don't need containers

## Security Model

Credentials never reach code execution sandboxes. Three auth patterns:

1. **Bundle credentials with resources during sandbox initialization** — e.g., git tokens used during repo cloning, not exposed to generated code
2. **Store OAuth tokens in secure vaults** — accessed via dedicated proxy, Claude calls MCP tools through proxy
3. **Git tokens handled during cloning** — never exposed to running code

## Key Design Principles

- **Session as source of truth** — not the harness, not the container
- **Lazy provisioning** — containers spun up only when tools actually need them
- **Uniform tool interface** — every tool, whether container command or API call, follows same pattern
- **Credential isolation** — secrets never touch code execution environments
- **Component independence** — brain, hands, and session can fail/restart independently

## MCP Integration

For custom tools, Managed Agents support MCP and store OAuth tokens in a secure vault. Claude calls MCP tools via a dedicated proxy that takes in a token associated with the session.
