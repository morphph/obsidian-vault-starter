# Vendored excalidraw export module

- `excalidraw-export.mjs` — single-file ESM exposing `exportToSvg`, built from
  `@excalidraw/excalidraw@0.18.1` + react 18.3.1 (esbuild `--bundle --format=esm
  --platform=browser --define:process.env.NODE_ENV='"production"'`, entry:
  `export { exportToSvg } from "@excalidraw/excalidraw"`).
- `fonts/` — copied from the same package's `dist/prod/fonts/` (lazy-loaded via
  `window.EXCALIDRAW_ASSET_PATH = "./vendor/"` in render_template.html).

Why vendored (2026-07-07): esm.sh dep-chunk URLs for this package 404'd upstream
(both pinned and unpinned), breaking all rendering; and CDN re-resolution breaks
the byte-determinism the layer exporter (`--export-layers`) is specced to provide.
To upgrade: rebuild with the same esbuild recipe at the new version, re-run the
layer-export golden test (specs/excalidraw-layer-export.md in content-ops).
