**CLAUDE.md loads deterministically.** When Claude Code starts a session, it reads every CLAUDE.md file in the hierarchy (global, project root, current subdirectory) and injects their full contents into the system prompt. Every instruction is present every time. If your CLAUDE.md says "use Vitest, not Jest," Claude will follow that rule in every conversation without exception. The tradeoff is context window cost — everything in CLAUDE.md consumes tokens whether or not it's relevant to the current task.

**Claude Memory loads selectively.** The `MEMORY.md` index is always present in context, but individual memory files are loaded based on relevance. Claude reads the one-line descriptions in the index and decides which memories to pull in for the current conversation. A memory about "newsletter dedup architecture" won't load when you're working on CSS — in theory. This selective loading is more token-efficient but introduces non-determinism. Sometimes Claude loads a memory you needed; sometimes it doesn't.

This has practical implications. If a rule **must** fire every time — build commands, quality gates, forbidden patterns — it belongs in CLAUDE.md. If context is only **sometimes relevant** — a teammate's name, a debugging insight from last week, a project deadline — Memory is the right home. The [Claude Code memory system deep dive](/blog/claude-code-memory) covers the technical details of how both systems interact during session initialization.

## Collaboration and Team Dynamics: Where Each System Fits

The collaboration story is where these two systems diverge most sharply, and it's often the deciding factor for teams.

**CLAUDE.md is a team contract.** When your CLAUDE.md contains `npm run build` as a quality gate, every developer on the team — and every Claude Code instance they run — follows that rule. New team members clone the repo and immediately get the same AI behavior as everyone else. Changes to CLAUDE.md go through code review, which means the team has a say in how their AI assistant behaves. This is powerful for maintaining consistency, but it also means CLAUDE.md changes require consensus.

**Claude Memory is a personal notebook.** Your memories about preferring terse responses, your understanding of the auth module's quirks, your correction that Claude should never amend commits — these are yours alone. A teammate using Claude Code on the same repo will have a completely different memory bank reflecting their own preferences and workflow history.

This separation is intentional. You don't want every developer's personal preferences baked into a shared config file, and you don't want shared project rules silently diverging across different developers' memory banks. The two systems complement each other: CLAUDE.md handles the "we" (team agreements), Memory handles the "I" (personal context).

For teams adopting Claude Code, the recommended pattern is to start with a strong CLAUDE.md that covers build commands, testing requirements, coding conventions, and architectural constraints. Then let Memory naturally accumulate individual context over time. If you find yourself repeatedly saving the same type of memory across team members, that's a signal it should be promoted to CLAUDE.md instead.

## Content Strategy: What Goes Where

Choosing between Memory and CLAUDE.md comes down to three questions: Does the team need this? Must it fire every time? Will it change often?

### Put in CLAUDE.md

- **Build and test commands**: `npm run build`, `npm test`, `npm run lint` — these are non-negotiable project operations
- **Quality gates**: "ALL tests must pass before commit" — deterministic enforcement
- **Coding conventions**: "Use Vitest, not Jest" or "CJK content must use CJK word count" — team-wide standards
- **Architectural constraints**: "Don't import Next.js modules in pipeline scripts" — guardrails that prevent common mistakes
- **File structure rules**: "Every new script gets an entry in PIPELINE.md" — documentation standards
- **Forbidden patterns**: "Never skip failing tests. Never comment out lint rules." — hard limits

### Put in Claude Memory

- **User preferences**: "This user prefers terse responses with no trailing summaries"
- **Role context**: "User is a data scientist, new to the React side of the codebase"
- **Project state**: "Merge freeze begins 2026-03-05 for mobile release cut"
- **Corrections**: "Don't mock the database in integration tests — team got burned by mock/prod divergence"
- **External references**: "Pipeline bugs tracked in Linear project INGEST"
- **Workflow feedback**: "User prefers one bundled PR over many small ones for refactors"

### The Gray Zone

Some context types could go either way. A rule like "commit messages must describe what changed" could live in CLAUDE.md (team standard) or Memory (personal preference). The deciding factor: if only you care about it, Memory. If the team would benefit, CLAUDE.md.

A practical test: if a new developer joins the team tomorrow, would they need this context to work effectively with Claude Code? If yes, CLAUDE.md. If no, Memory.

## Maintenance and Lifecycle

**CLAUDE.md requires deliberate maintenance.** Someone has to write it, update it when conventions change, and remove rules that no longer apply. Stale CLAUDE.md instructions waste context tokens and can cause Claude to follow outdated practices. The upside: because it's in git, you can trace when rules were added, who added them, and why (via commit messages and PR descriptions).

**Claude Memory is mostly self-maintaining** but not zero-maintenance. Claude automatically saves memories when it detects important context — corrections, confirmations, role information. Over time, memories can become stale as the project evolves. Claude is instructed to verify memories against current code state before acting on them, but this verification isn't perfect. Periodically reviewing your `MEMORY.md` index and pruning outdated entries keeps the system accurate.

The lifecycle pattern differs too. CLAUDE.md entries tend to be long-lived — a build command stays relevant for months or years. Memory entries have mixed lifespans — a user preference might last forever, but a project deadline becomes irrelevant the day after it passes. Claude handles some of this naturally (it checks freshness), but explicit cleanup helps.

## Failure Modes: What Goes Wrong with Each

Understanding how each system fails helps you use them more effectively.

**CLAUDE.md failure modes:**
- **Over-stuffing**: Packing too many rules into CLAUDE.md bloats the system prompt and wastes context tokens. Every instruction competes for attention. Keep it focused on rules that genuinely need deterministic enforcement.
- **Stale instructions**: A CLAUDE.md that references a deprecated testing framework or an old directory structure actively misleads Claude. Treat it like any other code file — update it when the codebase changes.
- **Conflicting levels**: A subdirectory CLAUDE.md that contradicts the project-root CLAUDE.md creates confusion. Subdirectory files should specialize, not override.

**Claude Memory failure modes:**
- **Stale memories**: A memory that says "the auth module uses JWT tokens" is harmful if the team migrated to session-based auth last month. Claude tries to verify, but it can miss.
- **Over-accumulation**: Hundreds of memories make the MEMORY.md index long, increasing the chance Claude loads irrelevant context or misses what it needs.
- **False corrections**: If you accidentally correct Claude ("no, do it this way") when Claude's original approach was actually correct, that false correction persists as a memory and may misguide future sessions.
- **Non-determinism**: You can't guarantee that a specific memory will load in a specific conversation. Critical rules that must always apply belong in CLAUDE.md, not Memory.

## The Integration Pattern: Using Both Together

The most effective Claude Code setup uses CLAUDE.md and Memory as complementary layers in a deliberate hierarchy. This is how the [Claude Code extension stack](/blog/claude-code-extension-stack-skills-hooks-agents-mcp) is designed to work — each layer handles a different type of context.

**Layer 1 — CLAUDE.md (deterministic, team-shared):** Project rules, build commands, quality gates, architectural constraints. Always loaded. Shared with every developer.

**Layer 2 — Claude Memory (adaptive, personal):** User preferences, learned corrections, project state, external references. Selectively loaded. Personal to each developer.

**Layer 3 — Conversation context (ephemeral):** The current task, files being edited, recent tool outputs. Gone when the conversation ends.

This layering means Claude Code starts every conversation with a solid foundation of project rules (CLAUDE.md), enriched by personal context that makes interactions smoother (Memory), and then focuses on the immediate task (conversation context). Each layer has a clear purpose, a clear lifecycle, and a clear owner.

When adopting this pattern, start with CLAUDE.md. Get your build commands, test requirements, and core conventions documented. Use Claude Code for a week and let Memory accumulate naturally. Then review what Memory saved — if you see patterns (multiple developers saving the same correction), promote those to CLAUDE.md. The system is designed to evolve with your team's workflow, not to be configured perfectly upfront.

## When to Choose Claude Memory

Choose Claude Memory as your primary context mechanism when:

- **You're a solo developer** and there's no team to share CLAUDE.md with — Memory captures your personal workflow context with zero configuration effort
- **Context is personal**: your communication preferences, your role-specific needs, your debugging history
- **Context is temporal**: project deadlines, sprint goals, temporary architectural decisions that will change next quarter
- **Context is reactive**: corrections and confirmations that emerge naturally during conversations, not rules you'd think to write down in advance
- **You want low maintenance**: Memory self-populates from conversation signals — you don't need to write or maintain a config file

## When to Choose CLAUDE.md

Choose CLAUDE.md as your primary context mechanism when:

- **You're on a team** and need consistent AI behavior across all developers
- **Rules are non-negotiable**: build commands, quality gates, and coding conventions that must fire every single time
- **Context needs review**: you want changes to AI behavior to go through pull requests and code review
- **Onboarding matters**: new developers should get the same AI experience on day one as veterans
- **Auditability is important**: you need to trace when AI behavior rules were added and by whom
- **Instructions are long-lived**: conventions that won't change for months or years

## Verdict

**Use both.** CLAUDE.md and Claude Memory aren't alternatives — they're complementary layers designed to work together. **CLAUDE.md is the foundation**: deterministic, shared, version-controlled rules that define how Claude Code behaves in your project. **Claude Memory is the personalization layer**: adaptive, individual context that makes Claude Code smarter about your specific workflow over time.

If you're forced to pick one, **start with CLAUDE.md**. A well-written CLAUDE.md gives you 80% of the value — consistent builds, enforced quality gates, and shared conventions. Memory adds the remaining 20% — personal preferences, learned corrections, and temporal project context — but it's additive, not foundational.

For teams evaluating Claude Code's full context architecture, our analysis of [how skills, hooks, agents, and MCP fit together](/blog/claude-code-extension-stack-skills-hooks-agents-mcp) explains where Memory and CLAUDE.md sit in the broader programmable stack. And for practical guidance on writing effective instruction files, [9 Principles for Writing Great Claude Code Skills](/blog/9-principles-writing-claude-code-skills) covers patterns that apply equally to CLAUDE.md authoring.

## Frequently Asked Questions

### Can Claude Memory override instructions in CLAUDE.md?

No. CLAUDE.md instructions are loaded deterministically into the system prompt and take precedence over memory-based context. If CLAUDE.md says "use Vitest" and a memory says "this user prefers Jest," the CLAUDE.md rule wins. Memory is additive context, not an override mechanism — it fills gaps that CLAUDE.md doesn't cover.

### Does Claude Memory sync across machines?

No. Claude Memory is stored locally in `~/.claude/projects/` and is tied to your machine and user profile. If you work on the same project from two different computers, each will accumulate its own separate memory bank. CLAUDE.md, by contrast, syncs automatically because it's checked into git with the rest of your repository.

### How much should I put in CLAUDE.md before it becomes too long?

Keep CLAUDE.md under 200 lines for a typical project. Every line consumes context tokens in every conversation, whether relevant or not. Focus on rules that need deterministic enforcement — build commands, quality gates, hard constraints. Move situational context (project timelines, role-specific notes, workflow preferences) to Claude Memory, where it loads selectively.

### Will Claude automatically promote Memory entries to CLAUDE.md?

No. Claude does not modify CLAUDE.md automatically. If you notice the same correction being saved to Memory repeatedly across team members, that's a manual signal to promote it to CLAUDE.md via a commit. The boundary between personal memory and shared configuration is intentionally maintained by human decision.

### Can I disable Claude Memory entirely and just use CLAUDE.md?

Yes. You can avoid using Claude Memory by not saving memories and clearing the memory directory. Claude Code will function normally using only CLAUDE.md for persistent context. This is a reasonable choice for teams that prefer fully deterministic, version-controlled AI behavior with no adaptive components.

---

*Want more AI insights? [Subscribe to LoreAI](/subscribe) for daily briefings.*
```
