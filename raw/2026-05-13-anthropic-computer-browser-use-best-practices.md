# Best Practices for Computer and Browser Use with Claude

**Source:** https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
**Authors:** Lucas Gonzalez and Luca Weihs
**Published:** 2026-05-13
**Category:** Agents
**Reading time:** 5 minutes
**Fetch method:** WebFetch (claude.com static blog, two passes — one for prose, one for code blocks)

---

## Summary

Comprehensive guide on building reliable computer and browser use integrations with Claude's latest models (Claude 4.6 family, Opus 4.7, Haiku 4.5). Core thesis: **"click accuracy is the foundation of any computer use integration,"** with screenshot resolution being the highest-impact lever.

## Screenshot Resolution & Scaling

**Defaults:**
- **1280x720** is the recommended starting resolution — balances visual fidelity with token efficiency.
- For **Opus 4.7**, **1080p** is recommended for improved quality (higher API limits unlock it).

**API limits per model:**

| Model | Max long edge | Max total pixels |
|---|---|---|
| Claude 4.6 family | 1568 px | 1.15 MP |
| Opus 4.7 | 2576 px | 3.75 MP |

Images exceeding these limits are **silently downscaled by the API**, causing coordinate misalignment — "the primary cause of click inaccuracy at high resolutions." Always pre-scale on the client.

```python
import math
from PIL import Image
import base64
import io

MAX_LONG_EDGE = 1568  # 1568 for 4.6, 2576 for Opus 4.7
MAX_PIXELS = 1_150_000  # 1.15MP for 4.6, 3.75MP for Opus 4.7

def compute_max_api_fit(native_w, native_h):
    aspect = native_w / native_h
    h_from_pixels = math.sqrt(MAX_PIXELS / aspect)
    w_from_pixels = h_from_pixels * aspect
    if native_w >= native_h:
        w = min(w_from_pixels, MAX_LONG_EDGE)
        h = w / aspect
    else:
        h = min(h_from_pixels, MAX_LONG_EDGE)
        w = h * aspect
    w = min(w, native_w)
    h = min(h, native_h)
    return int(w), int(h)

def scale_coordinates(api_x, api_y, display_w, display_h, screen_w, screen_h):
    screen_x = int(api_x * (screen_w / display_w))
    screen_y = int(api_y * (screen_h / display_h))
    return screen_x, screen_y

def prepare_screenshot(screenshot, native_w, native_h):
    display_w, display_h = 1280, 720
    resized = screenshot.resize((display_w, display_h), Image.LANCZOS)
    buffer = io.BytesIO()
    resized.save(buffer, format="PNG")
    b64 = base64.standard_b64encode(buffer.getvalue()).decode()
    return b64, display_w, display_h
```

## Content Ordering — Text Before Image

Place text instructions **before** images in the messages array. "Lets the model know what it's looking for as it processes the screenshot, which improves click accuracy."

```python
content = [
    {"type": "text", "text": "Click on the Submit button"},
    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": screenshot_b64}},
]
```

## Model Selection

- **Sonnet 4.6** — better click precision, more robust under heavy downscaling. Default mechanical-task choice.
- **Opus 4.6** — stronger reasoning, slightly less mechanical accuracy.
- **Opus 4.7** — bridges the gap; recommended when you need both reasoning and accuracy, supports the higher 2576px/3.75MP limits.

## Small Targets — Use `enable_zoom`

For checkboxes, icons, tiny UI elements:

```python
{
    "type": "computer_20251124",
    "name": "computer",
    "display_width_px": 1280,
    "display_height_px": 720,
    "enable_zoom": True
}
```

Additional remedies:
- Make UI targets larger when you control the UI.
- Use keyboard alternatives for system tray icons.
- Consider source image resolution at capture time.

**What didn't work:** splitting images into tiles, overlaying coordinate grids — "did not produce reliable gains."

## Thinking Effort Configuration

**Claude Opus 4.7:**
- `high` effort is the default — achieves near-maximum success with **~50% token usage** of `max`.
- Reserve `max` for complex one-shot tasks.
- Even `low` effort produces quality between Opus 4.6's `high` and `max`.

**Claude 4.6 models:**
- `medium` effort is the sweet spot — top accuracy at half the tokens of `high`.
- `low` actually uses fewer tokens than no-thinking, due to reduced errors and retries.
- Skip thinking entirely only for simple, predictable workflows.

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    betas=["computer-use-2025-11-24"],
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},
    messages=[...],
    tools=[{
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": 1280,
        "display_height_px": 720,
    }],
)
```

## Context Management for Long Sessions — Three Layers

1. **Prompt caching** — one cache breakpoint on stable content (system prompt), three on recent tool results.
2. **Rolling buffer** — keep the 3 most recent screenshots; replace older ones with text placeholders in batches every 25 screenshots.
3. **Server-side compaction** — summarize history at ~150k tokens using a custom summarization prompt.

Goal: preserve task context while keeping total tokens bounded and maximizing cache hit rates.

**Cache breakpoint placement:**

```python
def set_trailing_cache_control(messages, max_breakpoints=3):
    for msg in messages:
        for block in msg.get("content", []):
            if isinstance(block, dict):
                block.pop("cache_control", None)
    placed = 0
    for msg in reversed(messages):
        for block in reversed(msg.get("content", [])):
            if placed >= max_breakpoints:
                return
            if isinstance(block, dict) and block.get("type") == "tool_result":
                block["cache_control"] = {"type": "ephemeral"}
                placed += 1
```

**Server-side compaction:**

```python
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["compact-2026-01-12", "computer-use-2025-11-24"],
    context_management={
        "edits": [{
            "type": "compact_20260112",
            "trigger": {"type": "input_tokens", "value": 150_000},
            "instructions": COMPACT_PROMPT,
        }]
    },
    messages=[...],
    tools=[...],
)
```

## Prompt Injection Defense

The official `computer_20251124` tool ships with **built-in prompt injection classifiers that run automatically** — "approximately zero additional latency and no additional cost."

Additional defenses:
- Human-in-the-loop confirmation for high-stakes actions.
- Scoped agent permissions.
- Full action logging and monitoring.
- Clear system prompts distinguishing user instructions from encountered page content.

## Teaching Claude Through Demonstrations

Alternative to prompt iteration: record yourself performing the task with annotated screenshots. Bundle = action type, description, selector, coordinates, URL, screenshot, optional voice narration. Claude reads the demonstration as context and adapts to UI changes.

## Debugging Click Issues

| Symptom | Likely cause | Solution |
|---|---|---|
| Consistent offset in one direction | Display dimensions mismatch or image exceeds API limits | Verify dimensions match resized screenshot; pre-downscale to 1280x720 |
| Clicks miss small targets | Target too small or heavy downscaling | Enable zoom; increase UI element size |
| Model clicks wrong element | Ambiguous instructions | Use positional context in prompts |
| Poor accuracy across the board | Images exceed API limits | Pre-downscale before sending |

## Experimental Patterns

- **Batch tools** — combine sequential actions into single tool calls when no intermediate visual feedback needed.
- **Advisor tool** — pair a Sonnet executor with an Opus 4.7 advisor for strategic reasoning during mechanical tasks.
- **Periodic reminders** — brief nudges help long-running agents remember available tools.

## Ecosystem

The article references a new demo implementation in the Claude quickstarts repository encapsulating these practices, with debugging utilities: trajectory viewer, tool debug panel, localization playground.

## Reference API Call

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Click on the Submit button"},
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}},
        ]
    }],
    tools=[{
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": display_w,
        "display_height_px": display_h,
    }],
)
```
