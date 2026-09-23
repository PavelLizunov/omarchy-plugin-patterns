# High-resolution screenshots from QML sources

Use this workflow when a screenshot shows a plugin UI whose actual QML components and project imports are available. It improves text and control edges by rendering the real interface at a higher pixel density. It does not recover missing pixels from a raster image.

## Preserve the source content

- Keep every supplied screenshot unchanged as the “before” source. Record the source filenames and intended UI state; remove duplicate entries from the comparison set without deleting the originals.
- Render the real QML components with a controlled fixture. Read visible labels and values from the screenshot, then cross-check them against the current source/catalog and the fixture. Do not invent controls, labels, states, colors, or values to fill gaps. Mark unresolved details for review.
- Reuse the project's Qt/QML imports and render harness. Do not substitute an approximate HTML mockup or image-generation model when exact text and controls matter.

## Render at 2×

- Keep the logical/display dimensions equal to the source screenshot and render at twice the pixel width and height. Scale the QML item tree or use the project's established high-DPI capture path so text and vector edges are drawn at the output resolution; do not merely enlarge the source PNG.
- Prefer the project's existing offscreen Qt Quick test runner and software backend for repeatable captures. For example, the MX Ergo workflow uses `qmltestrunner` with `QT_QPA_PLATFORM=offscreen` and `QT_QUICK_BACKEND=software`; use the target project's imports and runner rather than copying machine-specific absolute paths.
- Save new PNGs separately from the originals, with names that identify their theme, screen and scale. Keep the capture script and fixture beside the project-specific artifact when that makes the run reproducible; do not add temporary absolute paths to distributable skill files.

## Compare and verify

- Make an HTML “before / after” page that displays each original and its 2× render at the same CSS width. Link the rendered image to its native-resolution PNG so the user can inspect the extra pixels.
- Include each unique screen once, preserve the source ordering where practical, and identify the output honestly as a QML rerender rather than a pixel-preserving upscale.
- Inspect every pair at the shared display size and at native resolution. Check exact text, selected states, geometry, clipping, theme, device imagery and stray borders/artifacts. Fix fixture or layout errors and rerender when needed.
- State the limitation in the comparison: a source-based rerender can sharpen text and controls, but theme values, spacing and details can differ from the captured application. It is not pixel-identical. If pixel identity is mandatory or the real QML source is unavailable, do not claim this method preserves the image exactly; use a non-generative resize only when useful and disclose that it adds no real detail.
- A comparison gallery shows how the captured source and rerender look; it does not by itself verify the live plugin, its interactions, accessibility or runtime behavior.
