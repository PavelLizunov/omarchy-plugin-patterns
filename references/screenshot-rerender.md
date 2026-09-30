# High-resolution screenshots from QML sources

Use this workflow when a screenshot shows a plugin UI whose actual QML components and project imports are available. It improves text and control edges by rendering the real interface at a higher pixel density. It does not recover missing pixels from a raster image.

First apply [visual-review](visual-review.md): inventory allowed capture tools, inspect consumer/import/startup effects, use inert models and record provenance. Offscreen rendering does not isolate processes, files or network access. If no safe harness or allowed capture path exists, deliver the source/supplied-image review and name the missing evidence; do not execute the production plugin just for a picture.

## Preserve the source content

- Keep every supplied screenshot unchanged as the “before” source. Record the source filenames and intended UI state; remove duplicate entries from the comparison set without deleting the originals.
- Render the real QML components with a controlled fixture. Read visible labels and values from the screenshot, then cross-check them against the current source/catalog and the fixture. Do not invent controls, labels, states, colors, or values to fill gaps. Mark unresolved details for review.
- Reuse the project's Qt/QML imports and render harness. Do not substitute an approximate HTML mockup or image-generation model when exact text and controls matter.

## Render at 2×

An installed qml-preview MCP 0.2.0 supports explicit `dpr: 2`; first discover its
current schema and follow [the QML visual cycle](qml-visual-cycle.md). Preserve
logical geometry, inspect the PNG attachment or harness-read PNG, and record
actual pixel dimensions. Loading this guide does not install or enable MCP.

- Record logical geometry, source pixel dimensions and device-pixel ratio (DPR) separately, including crop origin and any letterboxing. Pixel dimensions alone do not establish logical size. If source DPR/geometry is unknown, identify the assumption instead of deriving layout size from the PNG.
- Keep the QML consumer's logical geometry unchanged and select an explicit target density, normally 2 pixels per logical unit (DPR 2). For a 400×300 logical card, DPR 1 is 400×300 pixels and DPR 2 is 800×600. A source already at DPR 2 needs DPR 4 only if the request is specifically twice its existing pixel dimensions. Use the project's verified high-DPI capture path; confirm saved dimensions and redrawn text/vector edges. Do not enlarge a PNG or double the layout dimensions by mistake.
- Prefer the project's existing offscreen Qt Quick test runner and software backend for repeatable captures. For example, the MX Ergo workflow uses `qmltestrunner` with `QT_QPA_PLATFORM=offscreen` and `QT_QUICK_BACKEND=software`; use the target project's imports and runner rather than copying machine-specific absolute paths.
- Save new PNGs separately from the originals, with names that identify their theme, screen and scale. Keep the capture script and fixture beside the project-specific artifact when that makes the run reproducible; do not add temporary absolute paths to distributable skill files.

## Compare and verify

- Make an HTML “before / after” page that displays each original and its 2× render at the same CSS width. Link the rendered image to its native-resolution PNG so the user can inspect the extra pixels.
- Include each unique screen once, preserve the source ordering where practical, and identify the output honestly as a QML rerender rather than a pixel-preserving upscale.
- Inspect every pair at the shared display size and at native resolution. Check exact text, selected states, geometry, clipping, theme, device imagery and stray borders/artifacts. Correct capture/fixture errors and rerender; report product defects unless fixing them is already within the user's scope.
- State the limitation in the comparison: a source-based rerender can sharpen text and controls, but theme values, spacing and details can differ from the captured application. It is not pixel-identical. If pixel identity is mandatory or the real QML source is unavailable, do not claim this method preserves the image exactly; use a non-generative resize only when useful and disclose that it adds no real detail.
- A comparison gallery shows how the captured source and rerender look; it does not by itself verify the live plugin, its interactions, accessibility or runtime behavior.
