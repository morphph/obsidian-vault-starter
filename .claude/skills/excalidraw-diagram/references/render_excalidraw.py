"""Render Excalidraw JSON to PNG using Playwright + headless Chromium.

Usage:
    cd .claude/skills/excalidraw-diagram/references
    uv run python render_excalidraw.py <path-to-file.excalidraw> [--output path.png] [--scale 2] [--width 1920]

First-time setup:
    cd .claude/skills/excalidraw-diagram/references
    uv sync
    uv run playwright install chromium
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_excalidraw(data: dict) -> list[str]:
    """Validate Excalidraw JSON structure. Returns list of errors (empty = valid)."""
    errors: list[str] = []

    if data.get("type") != "excalidraw":
        errors.append(f"Expected type 'excalidraw', got '{data.get('type')}'")

    if "elements" not in data:
        errors.append("Missing 'elements' array")
    elif not isinstance(data["elements"], list):
        errors.append("'elements' must be an array")
    elif len(data["elements"]) == 0:
        errors.append("'elements' array is empty — nothing to render")

    return errors


def compute_bounding_box(elements: list[dict]) -> tuple[float, float, float, float]:
    """Compute bounding box (min_x, min_y, max_x, max_y) across all elements."""
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")

    for el in elements:
        if el.get("isDeleted"):
            continue
        x = el.get("x", 0)
        y = el.get("y", 0)
        w = el.get("width", 0)
        h = el.get("height", 0)

        # For arrows/lines, points array defines the shape relative to x,y
        if el.get("type") in ("arrow", "line") and "points" in el:
            for px, py in el["points"]:
                min_x = min(min_x, x + px)
                min_y = min(min_y, y + py)
                max_x = max(max_x, x + px)
                max_y = max(max_y, y + py)
        else:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x + abs(w))
            max_y = max(max_y, y + abs(h))

    if min_x == float("inf"):
        return (0, 0, 800, 600)

    return (min_x, min_y, max_x, max_y)


def effective_step(el: dict, by_id: dict[str, dict]) -> int:
    """Element's animation step: explicit customData.step, else inherited from
    its container (bound text), else 1 (base layer)."""
    step = (el.get("customData") or {}).get("step")
    if step is None and el.get("containerId"):
        container = by_id.get(el["containerId"])
        if container is not None:
            step = (container.get("customData") or {}).get("step")
    try:
        return max(1, int(step))
    except (TypeError, ValueError):
        return 1


def export_layers(excalidraw_path: Path, out_dir: Path, padding: int = 80) -> Path:
    """Export per-step layer SVGs (identical viewBox) + steps.json. Returns out_dir."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright not installed.", file=sys.stderr)
        sys.exit(1)

    raw = excalidraw_path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {excalidraw_path}: {e}", file=sys.stderr)
        sys.exit(1)
    errors = validate_excalidraw(data)
    if errors:
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    elements = [e for e in data["elements"] if not e.get("isDeleted")]
    by_id = {e["id"]: e for e in elements}

    steps_map: dict[int, list[dict]] = {}
    for el in elements:
        steps_map.setdefault(effective_step(el, by_id), []).append(el)
    step_nums = sorted(steps_map)

    min_x, min_y, max_x, max_y = compute_bounding_box(elements)
    frame = {
        "x": min_x - padding, "y": min_y - padding,
        "w": (max_x - min_x) + padding * 2, "h": (max_y - min_y) + padding * 2,
    }

    layers_dir = out_dir / "layers"
    layers_dir.mkdir(parents=True, exist_ok=True)

    template_url = (Path(__file__).parent / "render_template.html").as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto(template_url)
        page.wait_for_function("window.__moduleReady === true", timeout=30000)
        id_sets = [[e["id"] for e in steps_map[n]] for n in step_nums]
        result = page.evaluate(
            "([data, sets, frame]) => window.renderLayersSvg(data, sets, frame)",
            [data, id_sets, frame],
        )
        browser.close()

    if not result or not result.get("success"):
        msg = result.get("error", "renderLayersSvg returned null") if result else "null"
        print(f"ERROR: Layer export failed: {msg}", file=sys.stderr)
        sys.exit(1)

    layers = result["layers"]
    view_boxes = {l["viewBox"] for l in layers}
    if len(view_boxes) != 1:
        print(f"ERROR: layer viewBoxes differ: {view_boxes}", file=sys.stderr)
        sys.exit(1)

    steps_meta = []
    seen: list[dict] = []
    for i, n in enumerate(step_nums):
        els = steps_map[n]
        seen.extend(els)
        bx0, by0, bx1, by1 = compute_bounding_box(els)
        cx0, cy0, cx1, cy1 = compute_bounding_box(seen)
        label = next(
            ((e.get("customData") or {}).get("stepLabel") for e in els
             if (e.get("customData") or {}).get("stepLabel")), None)
        fname = f"step-{i + 1:02d}.svg"
        (layers_dir / fname).write_text(layers[i]["svg"], encoding="utf-8")
        steps_meta.append({
            "step": n, "label": label,
            "bbox": [bx0, by0, bx1 - bx0, by1 - by0],
            "cumulativeBbox": [cx0, cy0, cx1 - cx0, cy1 - cy0],
            "elementCount": len(els), "file": f"layers/{fname}",
        })

    steps_json = {
        "contract_version": "layer-export.v1",
        "source": excalidraw_path.name,
        "canvas": {
            "bbox": [frame["x"], frame["y"], frame["w"], frame["h"]],
            "padding": padding,
            "viewBox": layers[0]["viewBox"],
            "width": layers[0]["width"], "height": layers[0]["height"],
        },
        "steps": steps_meta,
    }
    (out_dir / "steps.json").write_text(
        json.dumps(steps_json, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_dir


def render(
    excalidraw_path: Path,
    output_path: Path | None = None,
    scale: int = 2,
    max_width: int = 1920,
) -> Path:
    """Render an .excalidraw file to PNG. Returns the output PNG path."""
    # Import playwright here so validation errors show before import errors
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright not installed.", file=sys.stderr)
        print("Run: cd .claude/skills/excalidraw-diagram/references && uv sync && uv run playwright install chromium", file=sys.stderr)
        sys.exit(1)

    # Read and validate
    raw = excalidraw_path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {excalidraw_path}: {e}", file=sys.stderr)
        sys.exit(1)

    errors = validate_excalidraw(data)
    if errors:
        print(f"ERROR: Invalid Excalidraw file:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    # Compute viewport size from element bounding box
    elements = [e for e in data["elements"] if not e.get("isDeleted")]
    min_x, min_y, max_x, max_y = compute_bounding_box(elements)
    padding = 80
    diagram_w = max_x - min_x + padding * 2
    diagram_h = max_y - min_y + padding * 2

    # Cap viewport width, let height be natural
    vp_width = min(int(diagram_w), max_width)
    vp_height = max(int(diagram_h), 600)

    # Output path
    if output_path is None:
        output_path = excalidraw_path.with_suffix(".png")

    # Template path (same directory as this script)
    template_path = Path(__file__).parent / "render_template.html"
    if not template_path.exists():
        print(f"ERROR: Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    template_url = template_path.as_uri()

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
        except Exception as e:
            if "Executable doesn't exist" in str(e) or "browserType.launch" in str(e):
                print("ERROR: Chromium not installed for Playwright.", file=sys.stderr)
                print("Run: cd .claude/skills/excalidraw-diagram/references && uv run playwright install chromium", file=sys.stderr)
                sys.exit(1)
            raise

        page = browser.new_page(
            viewport={"width": vp_width, "height": vp_height},
            device_scale_factor=scale,
        )

        # Load the template
        page.goto(template_url)

        # Wait for the ES module to load (imports from esm.sh)
        page.wait_for_function("window.__moduleReady === true", timeout=30000)

        # Inject the diagram data and render
        json_str = json.dumps(data)
        result = page.evaluate(f"window.renderDiagram({json_str})")

        if not result or not result.get("success"):
            error_msg = result.get("error", "Unknown render error") if result else "renderDiagram returned null"
            print(f"ERROR: Render failed: {error_msg}", file=sys.stderr)
            browser.close()
            sys.exit(1)

        # Wait for render completion signal
        page.wait_for_function("window.__renderComplete === true", timeout=15000)

        # Screenshot the SVG element
        svg_el = page.query_selector("#root svg")
        if svg_el is None:
            print("ERROR: No SVG element found after render.", file=sys.stderr)
            browser.close()
            sys.exit(1)

        svg_el.screenshot(path=str(output_path))
        browser.close()

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Excalidraw JSON to PNG")
    parser.add_argument("input", type=Path, help="Path to .excalidraw JSON file")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output PNG path (default: same name with .png)")
    parser.add_argument("--scale", "-s", type=int, default=2, help="Device scale factor (default: 2)")
    parser.add_argument("--width", "-w", type=int, default=1920, help="Max viewport width (default: 1920)")
    parser.add_argument("--export-layers", type=Path, default=None, metavar="OUTDIR",
                        help="Export per-step layer SVGs + steps.json to OUTDIR (uses customData.step)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.export_layers is not None:
        out = export_layers(args.input, args.export_layers)
        print(str(out))
        return

    png_path = render(args.input, args.output, args.scale, args.width)
    print(str(png_path))


if __name__ == "__main__":
    main()
