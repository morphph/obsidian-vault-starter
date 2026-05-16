---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
tags: [wiki, anthropic, computer-use, browser, vision, agentic]
---

# Computer and Browser Use (with Claude)

## Summary
Anthropic's official API capability for letting Claude **drive a real computer or browser via screenshots + click/keystroke output**. Tool type: `computer_20251124`. Beta: `computer-use-2025-11-24`. The 2026-05-13 best-practices post (Lucas Gonzalez + Luca Weihs) compresses a year of production lessons into a tight playbook: **the dominant issue is screenshot-to-API resolution mismatch**, and the other ~80% is choosing the right model + thinking-effort + context-management for the workload. Prompt-injection classifiers run free with the official tool type.

## Details

### The single most-important rule: pre-downscale screenshots
The #1 cause of bad click accuracy is sending images that exceed the model's resolution budget. **Pre-downscale on the client side** before sending, then map returned coordinates back to native resolution.

| Model | Max long edge | Max total pixels |
|-------|---------------|------------------|
| **Claude 4.6 family** (Sonnet 4.6) | 1568 px | 1.15 MP |
| **Claude Opus 4.7** | 2576 px | 3.75 MP |

**Starting points:**
- Most use cases: **1280×720** (works for both 4.6 and 4.7)
- Opus 4.7 with quality priority: **1080p** (good token efficiency, sharper text)

Returned `(api_x, api_y)` must be scaled back: `screen_x = api_x * (native_w / display_w)`.

### Content ordering: text BEFORE image
> Place text instructions *before* images in the messages array to improve click accuracy. The model uses the instruction context while processing the screenshot.

This is the single cheapest accuracy improvement available — zero added tokens, zero new logic. Just message-array ordering.

### Model selection
| Model | When to use |
|-------|-------------|
| **Sonnet 4.6** | Best **balance** — clicking accuracy + reasoning + cost |
| **Opus 4.7** | Superior reasoning; click precision *matches* Sonnet 4.6; higher resolution budget (3.75 MP) means less downscaling needed |
| **Haiku 4.5** | Latency-priority tasks |

Surprising finding: **Opus 4.7 does not beat Sonnet 4.6 on click accuracy alone** — it ties. Opus's win is reasoning + the ability to skip downscaling.

### Thinking effort defaults

| Model | Default | Cost-sensitive | Critical one-shot |
|-------|---------|----------------|--------------------|
| **Opus 4.7** | `high` | `low` | `max` |
| **4.6 family** | `medium` | `low` (high-throughput) | `high` (complex tasks) |

### Zoom for small targets
Enable in tool config:
```json
{
    "type": "computer_20251124",
    "name": "computer",
    "display_width_px": 1280,
    "display_height_px": 720,
    "enable_zoom": true
}
```

When the model needs to click a small element, it asks for a zoomed-in screenshot of the region, gets higher resolution within the same MP budget, clicks more precisely.

### Three-layer context management
Computer-use sessions accumulate screenshots fast (each turn = a new image). Three layers:

1. **Cache breakpoints (deterministic):** 1 on stable prefix, 3 on recent tool results
2. **Rolling buffer (mid-range):** Keep 3 most recent screenshots; prune older ones in batches (not one-at-a-time, to avoid cache invalidation)
3. **LLM compaction (long-range):** At ~150K tokens, summarize history with a custom prompt

The interaction with [[prompt-cache-optimization]]: pruning screenshots in *batches* means cache invalidation happens once per batch, not once per screenshot. **Always prune at a batch boundary.**

### Prompt injection defense
**Built-in classifiers** run automatically with the official `computer_20251124` tool type, **at no extra cost**. (Custom-built computer-use tools don't get this — apply for access.)

**Best practices regardless of classifier:**
- Human-in-the-loop for high-stakes actions (purchases, sends, deletes)
- Strictly scope agent permissions (origin allowlists, action allowlists)
- Log and monitor all actions
- **Treat web content as untrusted** — same model that produces output reads the web; injected text becomes prompt

### Demonstration-based teaching (`enable_demonstrations`)
See [[demonstration-based-teaching]]. Instead of describing a workflow in natural language, **record one demonstration with screenshots + click annotations**. During playback, Claude adapts the recorded sequence to the *current* UI state rather than blindly replaying coordinates. Pattern is robust to:
- UI layout changes
- Resolution differences
- Minor element repositioning

Data captured per step: action type · description · CSS selector · coordinates · annotated screenshot · viewport · optional voice narration.

### Experimental techniques
- **Batch tools** — combine sequential non-dependent actions into a single tool call. Faster, but error compounding is a risk in exploratory workflows. Use only when the action chain is known-safe.
- **Advisor tool** — pair an executor model (cheap, fast) with a higher-intelligence advisor (Opus) for strategic guidance on long-horizon tasks, *without* extra API round-trips. Advisor sits inside the same call.

### Common failure modes (Anthropic's own catalog)
| Symptom | Cause | Fix |
|---------|-------|-----|
| Clicks consistently offset | Dimension mismatch or over-limit images | Downscale to 1280×720; use `compute_max_api_fit` helper |
| Clicks miss small targets | High-res source got over-downscaled | Enable zoom; increase target size if possible |
| Wrong element clicked | Ambiguous instruction or complex UI | Specific positional context; break into smaller steps |
| Poor accuracy across the board | Screenshots exceed limits | Pre-downscale before sending |

### Canonical code pattern
```python
import anthropic

client = anthropic.Anthropic()
b64, display_w, display_h = prepare_screenshot(screenshot, native_w, native_h)

# Scale returned coordinates back to native resolution
screen_x = int(api_x * (native_w / display_w))
screen_y = int(api_y * (native_h / display_h))

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["computer-use-2025-11-24"],
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Click the Submit button"},  # text BEFORE image
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}}
        ]
    }],
    tools=[{"type": "computer_20251124", "name": "computer",
            "display_width_px": display_w, "display_height_px": display_h}]
)
```

### Where this fits in the wiki

- **[[claude-opus-4-7]]** — the high-res vision (3.75 MP) feature is *what enables* the higher resolution budget for computer-use. The Opus 4.7 announcement focused on agentic coding; this post is the canonical other use case.
- **[[plan-mode-as-tools]]** — `computer_20251124` is itself a perfect example: tool-as-capability with `enable_zoom` as a tool-level flag (not a runtime prompt rewrite).
- **[[prompt-cache-optimization]]** — the rolling-buffer + batch-prune rule is one of the cleanest examples of "don't break the cache" in production design.
- **[[verification-loops]]** — the "human-in-the-loop for high-stakes actions" recommendation is verification-loop applied to *side-effects*, not just outputs.
- **[[silent-fallback-antipattern]]** — Anthropic's failure-mode catalog is exactly the kind of explicit-failure surface that silent fallback would erase.

## Connections
- Related: [[claude-opus-4-7]], [[claude-model-family]], [[anthropic]], [[demonstration-based-teaching]], [[prompt-cache-optimization]], [[plan-mode-as-tools]], [[verification-loops]], [[silent-fallback-antipattern]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md | Initial creation from Anthropic engineering blog post |
