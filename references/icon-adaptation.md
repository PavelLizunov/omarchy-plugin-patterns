# Omarchy-style icon adaptation

Use this optional workflow when the user asks to make a plugin icon fit Omarchy,
explore an Omarchy-wordmark direction, or improve a native icon's legibility.
It is a design mode of this skill, not a new installed skill or a demand to
redraw every logo. Native host/project guidance and the user's selections win.

Verdict: Extend the existing SVG/QML consumer and
[QML visual cycle](qml-visual-cycle.md), not a second renderer or design system.
This reference grants no deployment, desktop capture, provider or account access.

## 1. Establish identity and the actual pixel budget

- Read the installed icon consumer, slot, optical canvas, palette and versions.
  The inspected Omarchy 4.0.4 host uses `BarIconButton`, `WidgetButton`,
  `Style.bar.iconSlot` and `Style.bar.iconCanvas`; 27x26 slots with a 16x16 canvas
  are an observed default, not a universal size. Theme/font scaling and vertical
  bars can differ. Keep the native bindings; do not widen the bar to fit a draft.
- When wordmark styling is requested, inspect a local official brand asset.
  Describe its applicable vocabulary, such as heavy orthogonal forms and stepped
  corners, rather than silently copying letter paths or claiming an official logo.
  A pixel-like appearance can still be an SVG vector; it need not be a bitmap.
- Preserve third-party recognition and the icon's function. Native adaptation
  does not justify replacing every service mark with the Omarchy logo or a chip.
  Keep the exact requested silhouette/face decisions separate from suggestions.
- Trace real semantic color roles. On this host they belong to `qs.Commons.Color`,
  not a guessed `Theme.colors` API. Prefer an explicit module alias where names
  collide, for example `import qs.Commons as Host` and `Host.Color.foreground`.
  Qt 6.12 also declares `QtQuick.Color`; unqualified `Color` can resolve differently.

## 2. Draw only useful detail

Choose a few coherent SVG/QML directions, not an unrequested catalog. For a
stepped design, integer geometry can preserve its rhythm, but optical centering,
asymmetric shapes and fractional native scaling still need inspection.

Check the native-size outline, internal holes, eye/track widths and remaining
height. Enlarged cheeks, letters or separator gaps may look attractive while
consuming the whole gauge budget at bar size. State the tradeoff explicitly:
three-unit-wide eyes can replace two-unit eyes inside the same body; adding
letters underneath can halve the usable height. These are examples, not presets.
Do not enlarge or redesign the outer shape after the user chose it by implication.

For an icon that carries values:

- Define each axis and supply a native tooltip/legend and accessible name where
  the host supports them. Exact values belong in the tooltip or panel, not tiny
  letters the user must decode. Source properties are not screen-reader evidence.
- State whether fill is continuous, whole rows, separated blocks or cells.
  Microgauges are approximate. For floor quantization, `active = floor(p * N / 100)`
  gives the first nonempty cell at `100 / N` percent, with full fill at 100%.
  Six whole rows give about 16.7-point steps; three separated blocks give about
  33.3-point steps. These counts depend on actual track geometry, not icon size alone.
- Compare low, middle, high and full input on the same immutable shape. A one-unit
  separator can consume half a short track. Counts alone do not prove users can
  distinguish levels. Continuous SVG fill is allowed; do not force quantization.
- Keep low load, zero and unavailable/stale data distinct in the consumer even if
  they share empty tracks. Explain any quantization threshold. Do not invent an
  idle deadband, new sampling cadence or sensor request merely to restyle an icon.
- Preserve existing load/heat meanings. High CPU is not proof of overheating;
  a temperature-triggered marker needs separate freshness. Cheeks should not
  borrow warning colors unless they intentionally communicate a warning state.

## 3. Verify SVG decoding, not just the requested size

Use the existing vector generator and native consumer. Retain its viewBox; a
16-unit viewBox is suitable when that is the chosen geometry, not a mandatory
format for every source asset. Percent-encode complete SVG markup for a UTF-8
data URL; raw `#` in URL content can become a fragment. File SVG and encoded
inline SVG are different decoding paths.

For Qt `Image`, request raster dimensions from actual item geometry and the
verified Qt DPR, with an appropriate bounded rounding policy. On the inspected
Qt 6.12 installation, a data URL with intrinsic width/height 16 decoded to 16
although `sourceSize` requested 224. File SVG respected 224. Explicitly declaring
the requested width/height inside the data-URL SVG produced the sharp raster
without changing its viewBox. Base64 alone did not fix that sizing behavior.

Therefore `sourceSize` is not sufficient evidence. In an inert regression check,
observe `Image.Ready`, decoded/implicit dimensions and pixels at the requested
DPR. When needed, pass pixel dimensions to the SVG generator as well as
`sourceSize`, preserving geometry and bounded inputs. Recheck the installed Qt
version; this is a reproduced compatibility example, not an assertion that all
Qt releases or image APIs behave the same. Compositor scale and Qt DPR need not
be identical. Do not claim sharpness from a parsed SVG or an Image.Ready flag alone.

## 4. Show the real-size comparison and make the decision explicit

Follow [design review](design-review.md), [visual review](visual-review.md) and the
existing [QML visual cycle](qml-visual-cycle.md). Do not duplicate their execution
protocol here. Use the actual candidate in the owning native icon consumer, with
reviewed inert I/O, explicit readiness, locale, geometry and dependency hashes.
A native-module renderer can defeat same-name I/O mocks; verify the fixture's
module identity and side effects before running it.

- Render relevant states at the measured native logical size and DPR 1/2 where
  supported. Include applicable stale/zero/low/high/heat states, not an unrelated
  full-panel matrix. A density change is not permission to change the design.
- Put a native-size row first. Add a clearly labeled enlargement only for detail;
  it is not proof of at-a-glance readability. Use the harness image reader, such
  as Pi `read`, to actually display the saved PNG inline. A path string alone is
  not presentation. Terminal rescaling, compositor behavior and user eyesight
  remain limits, not a universal 1:1 physical-size guarantee.
- Inspect silhouette, clipping, native alignment, palette meanings, low-load
  visibility and which states collapse together. Report render, image inspection,
  native-design and interaction evidence separately. Static drafts have no click
  claim; missing tools/imports/safe fixtures are blockers, never visual PASS.
- Explain one recommended direction and its material loss of resolution/detail.
  Do not claim 100% readability, energy savings or zero overhead without evidence.
  Keep vector work distinct from image-model generation; do not substitute it or
  start extra model/provider campaigns, another shell, desktop capture or viewer.
- Record silhouette, face and fill decisions independently. Choosing a face in a
  block-filled preview does not automatically select the fill. Approval of a
  draft is not installation unless the current task covers integration. Preserve
  still-valid lifecycle and publication authority; do not add routine approval
  ceremonies or update a production component just to demonstrate a concept.

## Acceptance summary

Record the requested style/identity, actual host consumer and pixel budget,
selected versus comparison-only inputs, candidate/dependency hashes, render
states/DPR, inspected images and unresolved real-consumer checks. The Markdown
workflow can guide future agents, not enforce their obedience. Discovery, loaded
reference text, executed checks and field effectiveness are separate states.
