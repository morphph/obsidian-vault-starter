# New Capabilities for Building Agents on the Anthropic API

Source: https://claude.com/blog/agent-capabilities-api
Date: 2026-04-09
Author: Anthropic

## Overview

Anthropic announces four new beta capabilities for building AI agents on the API, plus Claude Managed Agents as a fully managed agent hosting service.

## Four New Beta Features

### 1. Code Execution Tool
- Claude runs Python in a sandboxed environment
- For data analysis, visualizations, financial modeling, scientific computing, business intelligence, document processing, statistical analysis
- 50 free hours/org/day, then $0.05/hour additional

### 2. MCP Connector
- Connect to remote Model Context Protocol servers without custom client code
- API handles connection management, tool discovery, error handling automatically
- Works with providers like Zapier, Asana

### 3. Files API
- Upload documents once for repeated reference across conversations
- Streamlines workflows for knowledge bases and datasets
- Integrates with code execution tool

### 4. Extended Prompt Caching
- 1-hour TTL option (vs standard 5-minute)
- Maintains context in long-running agent workflows
- Up to 90% cost reduction

## Claude Managed Agents

Fully managed agent infrastructure:
- Deploy and manage autonomous agents in stateful sessions with persistent event history
- Pre-built harness with prompt caching, compaction, and performance optimizations
- Supports simple single-task flows and complex multi-agent pipelines
- Teams focus on designing agent tasks rather than backend operations

All features available in public beta.
