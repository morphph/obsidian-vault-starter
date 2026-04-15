# Getting Started With Ralph — Quickstart Guide

**Source:** https://www.aihero.dev/getting-started-with-ralph
**Author:** Matt Pocock (AI Hero)
**Fetch method:** WebFetch
**Date fetched:** 2026-04-15

---

## Overview

Step-by-step practical setup guide for the Ralph Wiggum technique. Prerequisites, Docker sandbox setup, and progression from HITL to AFK scripts.

## Prerequisites

- Linux OS (or adapt for your system)
- Claude Code CLI tool
- Docker Desktop 4.50+

## Step-by-Step Setup

### Step 1: Install Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Run `claude` to authenticate with your Anthropic credentials.

### Step 2: Install Docker Desktop

Docker Desktop provides an isolated sandbox environment. Install version 4.50 or newer, then initialize:

```bash
docker sandbox run claude
```

Key advantages: automatic Git configuration injection and persistent state across multiple runs.

### Step 3: Create Your PRD and Progress File

Use Claude's plan mode (`shift-tab`) to develop your PRD iteratively, save as `PRD.md`.

```bash
touch progress.txt
```

The PRD can follow any format — markdown checklists, JSON, or plain text — as long as individual tasks are clearly extractable.

### Step 4: Build the HITL Script (ralph-once.sh)

```bash
#!/bin/bash

claude --permission-mode acceptEdits "@PRD.md @progress.txt \
1. Read the PRD and progress file. \
2. Find the next incomplete task and implement it. \
3. Commit your changes. \
4. Update progress.txt with what you did. \
ONLY DO ONE TASK AT A TIME."
```

Make executable: `chmod +x ralph-once.sh`

### Step 5: Create the AFK Loop Script (afk-ralph.sh)

```bash
#!/bin/bash
set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  exit 1
fi

for ((i=1; i<=$1; i++)); do
  result=$(docker sandbox run claude --permission-mode acceptEdits -p \
  "@PRD.md @progress.txt \
  1. Find the highest-priority task and implement it. \
  2. Run your tests and type checks. \
  3. Update the PRD with what was done. \
  4. Append your progress to progress.txt. \
  5. Commit your changes. \
  ONLY WORK ON A SINGLE TASK. \
  If the PRD is complete, output <promise>COMPLETE</promise>.")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "PRD complete after $i iterations."
    exit 0
  fi
done
```

Execute with iteration limits:
```bash
./afk-ralph.sh 20
```

### Step 6: Customize

Adapt for: alternate task sources (GitHub Issues, Linear), different outputs (branches/PRs), specialized loops (test coverage, linting, duplication).

## Key Configuration

| Component | Function |
|-----------|----------|
| `--permission-mode acceptEdits` | Prevents loop interruption from edit confirmations |
| `@PRD.md` and `@progress.txt` | Reference documents for task tracking |
| `-p` flag | Enables print mode for capturing output |
| `<promise>COMPLETE</promise>` | Completion indicator for autonomous loops |
