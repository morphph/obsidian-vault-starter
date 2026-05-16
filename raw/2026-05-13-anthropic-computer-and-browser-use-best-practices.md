# Best Practices for Computer and Browser Use with Claude

**Source URL:** https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
**Publication Date:** 2026-05-13
**Authors:** Lucas Gonzalez and Luca Weihs (Anthropic)
**Category:** Agents
**Reading Time:** 5 minutes
**Fetch method:** WebFetch (static blog, no fallback needed)

---

## Key Recommendations

### Screenshot Resolution & Scaling

The most critical optimization for click accuracy is **pre-downscaling screenshots before sending to the API**. Claude 4.6 models have these limits:
- Max long edge: 1568 pixels
- Max total pixels: 1.15 megapixels

Opus 4.7 supports higher resolution:
- Max long edge: 2576 pixels
- Max total pixels: 3.75 megapixels

**Recommended starting resolution:** 1280x720 for most use cases. For Opus 4.7, 1080p provides better quality with good token efficiency.

### Content Ordering

Place text instructions *before* images in the messages array to improve click accuracy. The model uses the instruction context while processing the screenshot.

### Model Selection

- **Sonnet 4.6:** Best balance of clicking accuracy, reasoning, and cost
- **Opus 4.7:** Superior reasoning with click precision matching Sonnet 4.6; higher resolution budget reduces needed downscaling
- **Haiku 4.5:** Optimal for latency-priority tasks

### Thinking Effort Settings

**For Opus 4.7:**
- Default: `high` effort (best accuracy-to-token ratio)
- Cost-sensitive: `low` effort
- One-shot critical tasks: `max` effort

**For 4.6 models:**
- Default: `medium` effort (sweet spot for accuracy vs. cost)
- High-throughput: `low` effort
- Complex tasks: `high` effort

### Handling Small Targets

Enable zoom for dense UIs:
```json
{
    "type": "computer_20251124",
    "name": "computer",
    "display_width_px": 1280,
    "display_height_px": 720,
    "enable_zoom": True
}
```

### Context Management Layers

1. **Cache breakpoints:** Place 1 on stable prefix, 3 on recent tool results
2. **Rolling buffer:** Keep 3 most recent screenshots; prune older ones in batches
3. **LLM compaction:** Summarize history at ~150k tokens using custom prompt

### Prompt Injection Defense

Built-in classifiers run automatically with the official `computer_20251124` tool type at **no extra cost**. For custom tools, classifiers are not yet available — request access via interest form.

**Best practices regardless:**
- Implement human-in-the-loop for high-stakes actions
- Scope agent permissions strictly
- Log and monitor all actions
- Treat web content as untrusted

### Teaching Claude via Demonstrations

Record workflow demonstrations with screenshots and annotated click positions. During playback, **Claude adapts the recorded sequence to current UI state rather than blindly replaying coordinates.**

Data model includes:
- Action type (click, type, navigate, scroll, select)
- Human-readable description
- CSS selector and coordinates
- Screenshot with visual annotation
- Viewport dimensions
- Optional voice narration

## Experimental Techniques

**Batch tools:** Combine sequential non-dependent actions into single tool calls for efficiency, though error compounding is a risk in exploratory workflows.

**Advisor tool:** Pairs executor model with higher-intelligence advisor for strategic guidance on long-horizon tasks without extra API round trips.

## Common Failure Causes & Fixes

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Clicks consistently offset | Dimension mismatch or exceeding API limits | Downscale to 1280x720 or use `compute_max_api_fit` |
| Clicks miss small targets | High-resolution source heavily downscaled | Enable zoom; increase target size if possible |
| Wrong element clicked | Ambiguous instruction or complex UI | Use specific positional context; break into smaller steps |
| Poor accuracy across board | Screenshots exceed limits | Pre-downscale all images before sending |

## Implementation Code Pattern

```python
import anthropic

client = anthropic.Anthropic()

# Prepare screenshot
b64, display_w, display_h = prepare_screenshot(screenshot, native_w, native_h)

# Scale returned coordinates back to native resolution
screen_x = int(api_x * (native_w / display_w))
screen_y = int(api_y * (native_h / display_h))

# Send with text before image
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["computer-use-2025-11-24"],
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Click the Submit button"},
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}}
        ]
    }],
    tools=[{"type": "computer_20251124", "name": "computer", "display_width_px": display_w, "display_height_px": display_h}]
)
```

**Authors:** Lucas Gonzalez and Luca Weihs
