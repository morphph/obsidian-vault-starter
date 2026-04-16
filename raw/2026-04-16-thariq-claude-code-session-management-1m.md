# Using Claude Code: Session Management & 1M Context

**Source:** https://x.com/trq212/status/2044548257058328723
**Author:** Thariq (@trq212, Anthropic)
**Fetch method:** Playwright MCP (browser snapshot)
**Date published:** April 16, 2026
**Metrics:** 157.5K views, 77 replies, 225 reposts, 1,735 likes, 2,943 bookmarks

---

## Context

Today Anthropic rolled out a new update to /usage to help users understand their usage with Claude Code. This was informed by conversations with customers. What came up again and again is variance in session management, especially with the new 1 million context in Claude Code.

Questions: Do you only use one session or two sessions in a terminal? Start a new session with every prompt? When do you use compact, rewind or subagents? What causes a bad compact?

There's a surprising amount of detail here that can really shape your experience with Claude Code and almost all of it comes from managing your context window.

## A Quick Primer on Context, Compaction & Context Rot

The context window is everything the model can "see" at once: system prompt, conversation, every tool call and its output, every file read. Claude Code has a context window of **one million tokens**.

**Context rot**: Model performance degrades as context grows because attention gets spread across more tokens, and older, irrelevant content starts to distract from the current task.

**Compaction**: When nearing the end of the context window, you summarize the task into a smaller description and continue in a new context window. You can also trigger compaction yourself.

## Every Turn Is a Branching Point

After Claude finishes a turn and you're about to send a new message, you have these options:

1. **Continue** — send another message in the same session
2. **/rewind (esc esc)** — jump back to a previous message and try again from there
3. **/clear** — start a new session, usually with a brief you've distilled from what you just learned
4. **Compact** — summarize the session so far and keep going on top of the summary
5. **Subagents** — delegate the next chunk of work to an agent with its own clean context, and only pull its result back in

While the most natural is just to continue, the other four options exist to help manage your context.

## When to Start a New Session

General rule of thumb: when you start a new task, you should also start a new session.

1M context windows mean you can now do longer tasks more reliably, for example building a full-stack app from scratch.

Sometimes you may do related tasks where some context is still necessary but not all. Example: writing documentation for a feature you just implemented. While you could start a new session, Claude would have to reread the files you just implemented, which would be slower and more expensive.

## Rewinding Instead of Correcting

**"If I had to pick one habit that signals good context management, it's rewind."**

Double-tapping Esc (or running /rewind) lets you jump back to any previous message and re-prompt from there. Messages after that point are dropped from context.

Rewind is often the better approach to correction. Example: Claude reads five files, tries an approach, and it doesn't work. Instinct: "that didn't work, try X instead." Better move: rewind to just after the file reads, and re-prompt with what you learned. "Don't use approach A, the foo module doesn't expose that — go straight to B."

**"summarize from here"**: Have Claude summarize its learnings and create a handoff message — kind of like a message to the previous iteration of Claude from its future self that tried something and it didn't work.

## Compacting vs. Fresh Sessions

Once a session gets long, two ways to shed weight: /compact or /clear (start fresh). They feel similar but behave very differently.

**Compact**: Asks the model to summarize the conversation, then replaces history with that summary. It's lossy — you trust Claude to decide what mattered. But you didn't have to write anything yourself and Claude might be more thorough. You can steer it: `/compact focus on the auth refactor, drop the test debugging`.

**Clear (/clear)**: You write down what matters ("we're refactoring the auth middleware, the constraint is X, the files are A and B, we've ruled out approach Y") and start clean. More work, but the resulting context is what you decided was relevant.

## What Causes a Bad Compact?

Bad compacts happen when **the model can't predict the direction your work is going**.

Example: autocompact fires after a long debugging session and summarizes the investigation. Your next message is "now fix that other warning we saw in bar.ts." But because the session was focused on debugging, the other warning might have been dropped from the summary.

This is particularly difficult because **due to context rot, the model is at its least intelligent point when compacting**. With one million context, you have more time to `/compact` proactively with a description of what you want to do.

## Subagents & Fresh Context Windows

Subagents are a form of context management. Useful when you know in advance that a chunk of work will produce a lot of intermediate output you won't need again.

When Claude spawns a subagent via the Agent tool, it gets its own fresh context window. It can do as much work as needed, then synthesize results so only the final report comes back.

**The mental test**: "Will I need this tool output again, or just the conclusion?"

While Claude Code automatically calls subagents, you may want to tell it to explicitly:
- "Spin up a subagent to verify the result of this work based on the spec file"
- "Spin off a subagent to read through this other codebase and summarize how it implemented the auth flow, then implement it yourself in the same way"
- "Spin off a subagent to write the docs on this feature based on my git changes"

## Summary

When Claude has ended a turn and you're about to send a new message, you have a decision point. Over time Claude will help handle this itself, but for now this is one of the ways you can guide Claude's output.
