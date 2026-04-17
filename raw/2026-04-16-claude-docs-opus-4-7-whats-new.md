# What's new in Claude Opus 4.7

**Source:** https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
**Fetch date:** 2026-04-17
**Fetch method:** WebFetch

---

Claude Opus 4.7 is our most capable generally available model to date. It is highly autonomous and performs exceptionally well on long-horizon agentic work, knowledge work, vision tasks, and memory tasks.

## New model

| Model | API model ID | Description |
|:------|:-------------|:------------|
| Claude Opus 4.7 | `claude-opus-4-7` | Our most capable generally available model for complex reasoning and agentic coding |

Supports 1M token context window, 128k max output tokens, adaptive thinking, and the same set of tools and platform features as Claude Opus 4.6.

## New features

### High-resolution image support
First Claude model with high-res image support. Max resolution increased to **2576px / 3.75MP** (from 1568px / 1.15MP). Operations like mapping coordinates to images are now simpler — model's coordinates are 1:1 with actual pixels, no scale-factor math. High-res images use more tokens; downsample if fidelity is unnecessary. Also improved: low-level perception (pointing, measuring, counting) and image localization (bounding-box detection).

### New `xhigh` effort level
Start with `xhigh` for coding and agentic use cases; use minimum `high` for most intelligence-sensitive use cases. (Messages API only; Claude Managed Agents handles effort automatically.)

### Task budgets (beta)
Gives Claude a rough estimate of how many tokens to target for a full agentic loop (thinking + tool calls + tool results + final output). Model sees a running countdown and uses it to prioritize work and finish gracefully.

Beta header: `task-budgets-2026-03-13`

```python
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=128000,
    output_config={
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 128000},
    },
    messages=[...],
    betas=["task-budgets-2026-03-13"],
)
```

- Minimum value: 20k tokens
- Advisory cap, not hard cap. Distinct from `max_tokens` (hard per-request ceiling).
- `task_budget` is passed to the model; `max_tokens` is not.
- Use `task_budget` for self-moderation; `max_tokens` as hard ceiling.
- For open-ended agentic tasks where quality > speed, do NOT set a task budget.

## Breaking changes

(Messages API only. No breaking changes on Claude Managed Agents.)

### Extended thinking budgets removed
`thinking: {"type": "enabled", "budget_tokens": N}` returns 400 error.
Adaptive thinking is the only thinking-on mode. In internal evals it reliably outperforms extended thinking.

**Adaptive thinking is OFF by default on Opus 4.7.** Requests with no `thinking` field run without thinking. Set `thinking: {type: "adaptive"}` explicitly to enable.

```python
# Before (Opus 4.6)
thinking = {"type": "enabled", "budget_tokens": 32000}

# After (Opus 4.7)
thinking = {"type": "adaptive"}
output_config = {"effort": "high"}
```

### Sampling parameters removed
`temperature`, `top_p`, `top_k` set to non-default values return 400. Omit these parameters entirely; use prompting for behavioral guidance. `temperature = 0` never guaranteed identical outputs anyway.

### Thinking content omitted by default
Thinking blocks still appear in stream, but `thinking` field is empty unless explicitly opted in. Silent change — no error. Response latency slightly improved.

```python
thinking = {
    "type": "adaptive",
    "display": "summarized",  # or "omitted" (default)
}
```

If product streams reasoning to users, new default appears as long pause before output. Set `"display": "summarized"` to restore visible progress.

### Updated token counting
New tokenizer. May use **1.0x to 1.35x as many tokens** as previous models (up to ~35% more, varies by content). `/v1/messages/count_tokens` returns different numbers vs 4.6. Update `max_tokens` parameters to give headroom, including compaction triggers. 1M context at standard API pricing — no long-context premium.

## Capability improvements

### Knowledge work
- **.docx redlining and .pptx editing** — improved at producing and self-checking tracked changes and slide layouts
- **Charts and figure analysis** — improved at programmatic tool-calling with image-processing libraries (e.g. PIL) for pixel-level data transcription

If existing prompts have mitigations in these areas (e.g. "double-check the slide layout before returning"), try removing that scaffolding and re-baselining.

### Memory
Better at writing and using file-system-based memory. Agents that maintain scratchpads, notes files, or structured memory stores across turns should improve at jotting down notes and leveraging them in future tasks. Use the client-side memory tool for a managed scratchpad without building your own.

### Vision
See High-resolution image support above.

## Behavior changes (not breaking, but may require prompt updates)

- **More literal instruction following**, particularly at lower effort levels. Model will not silently generalize from one item to another, will not infer unrequested work.
- **Response length calibrates to perceived task complexity** rather than defaulting to fixed verbosity.
- **Fewer tool calls by default**, using reasoning more. Raising effort increases tool usage.
- **More direct, opinionated tone** with less validation-forward phrasing and fewer emoji than 4.6's warmer style.
- **More regular progress updates** throughout long agentic traces. If you've added scaffolding to force interim status messages, try removing it.
- **Fewer subagents spawned by default.** Steerable through prompting.
- **Real-time cybersecurity safeguards:** requests involving prohibited/high-risk topics may lead to refusals. Legitimate security work → apply to Cyber Verification Program.
