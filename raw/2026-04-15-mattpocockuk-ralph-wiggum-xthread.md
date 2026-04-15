# Matt Pocock X Thread — Ralph Wiggum Approach

**Source:** https://x.com/mattpocockuk/status/2007924876548637089
**Author:** Matt Pocock (@mattpocockuk)
**Fetch method:** Playwright MCP (browser snapshot)
**Date fetched:** 2026-04-15
**Metrics:** 204.4K views, 130 replies, 176 reposts, 2,493 likes, 4,882 bookmarks
**Date posted:** January 5, 2026

---

## Full Thread Content

"There's an AI coding approach that lets you run seriously long-running AI agents (hours, days) that ship code while you sleep. I've tried it, and I'm not going back. It's the Ralph Wiggum approach.

Here it is in a nutshell: Run a coding agent with a clean slate, again and again until a stop condition is met.

### The Bash Script

Running ralph involves a single bash script.

1. Set up a bash for loop that runs a set number of times, let's say 10. You choose a finite number to prevent the agent running infinitely.
2. Inside the loop, you get the coding agent (Claude Code, OpenCode, Codex etc) to work on a single feature in the repo until that single feature is done. You prompt it to say "if, after implementing, there is no further work to be done, reply with <promise>COMPLETE</promise>."
3. Check for <promise>COMPLETE</promise> inside the loop and exit early if it exists.

### The Stop Condition

How does the LLM know when to emit <promise>COMPLETE</promise>? There are multiple approaches:
- **Raw Prompting**: Just pass a very clear stop condition to the prompt inside the bash loop. "The job is complete when X conditions are met"
- **TODO list**: Give the agent a TODO list to complete
- **PRD**: My preferred approach, explained below

### Progress Reports

In your prompt, you MUST tell the agent to commit its work, and append its progress to a local progress.txt file. Committing its work allows future agents to navigate what was done via the git history. The progress.txt is a standard long-running agent practice. Feed it in to the agent via the prompt, and use the verb 'append' to make sure it doesn't update previous entries.

### Keep CI Green

Each commit MUST pass all tests and types. This means you have to prompt the agent to run typechecks and tests on each commit. If you don't do this, you're hamstringing future agent runs with bad code, and they'll need to bisect to find bugs. Super nasty.

This means that building really healthy feedback loops is CRITICAL to Ralph's success.

### The PRD

Two problems immediately emerge with Ralph:

1. **The agent picks tasks which are too large.** They don't scope the amount of work correctly and they try things which are too ambitious. This means they run out of context window and just end up failing.
2. **The agent doesn't know when to stop.**

To solve this, I use a PRD-based approach that formalizes the work I want Ralph to complete in a list of user stories. It's a mix of a PRD and a TODO-list, where the PRD is a JSON file of user stories with 'passes: false'. I then prompt the agent to pick the highest priority feature, and ONLY work on that feature. It then updates the passing status of the relevant PRD item at the end.

This scopes it down extremely effectively, meaning it utilizes only a small part of its context window, and thus isn't swamped by context rot.

### Summary

- Bash script
- JSON-based PRD
- progress.txt
- Keep CI green
- Feedback loops

You'll have an AI coding setup that can ship while you kip."
