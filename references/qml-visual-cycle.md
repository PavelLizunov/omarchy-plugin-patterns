# Required QML visual development cycle

Use this cycle for native plugin UI work, including visible state and copy changes.
Read [design-review](design-review.md) and [visual-review](visual-review.md).
The existing project/host design contract owns the appearance. This guide does
not install tools, enable plugins, grant runtime authority or replace interaction
checks. Audit-only and explicit no-process tasks remain read-only.

## Preflight

1. Identify the actual consumer, affected components, imports, target host/Qt
   versions and meaningful states. Read startup hooks and dependencies before
   execution. Use reviewed inert models for filesystem writes, commands, device
   access and network. Offscreen is not a sandbox.
2. Discover the current tool catalog. An installed `qml-preview` MCP provides
   `healthcheck` and `render_qml`; clients may namespace these names. Check the
   advertised schema and version instead of guessing arguments.
3. Call healthcheck once for the current renderer/environment. Missing tools,
   imports, unsupported roots/backends or unsafe fixture operations are explicit
   blockers. Do not install MCP from this skill or substitute desktop capture.
   Confirm that the active model/client supports image input. If an attachment
   is rejected as unsupported, do not claim image inspection; use an authorized
   image-capable route or report that concrete blocker without changing providers.
4. Read the installed, versioned QML Preview MCP README through its configured
   command/source location. Version 0.2.0 adds PNG delivery, initial root properties,
   explicit locale, objectName measurements and explicit dependency hashes.
   Version 0.3.0 adds explicit geometryChecks, bounded snapshot, warningsPolicy
   and wrapper/renderer pairing. Discover support before using these arguments.
   Keep installation and renderer implementation in that project, not each plugin.
   Source and installation contract: [QML Preview MCP](https://github.com/PavelLizunov/qml-preview-mcp).
   Record the installed version/commit; a moving upstream README is not evidence
   of this client's installed capabilities.

## Render and inspect

- Capture the baseline when comparison needs it. After each coherent UI change,
  render affected states and repeat after corrections. Before delivery, evidence
  must match the final relevant QML, models, catalogs, assets, adapters and host.
- Load the actual candidate component through the owning consumer; do not rebuild
  it as an approximate QML/HTML mock. Keep production source unchanged by capture.
- Pass explicit imports, logical geometry, DPR and a readiness property that means
  the fixture state is settled. Prefer `initialProperties` for state selection.
  Use `locale` for Qt formatting and project-owned catalogs for translated strings.
- Record meaningful normal/loading/empty/error states where they exist. Add long
  strings, constrained geometry, relevant themes/locales and DPR 2 where the change
  creates those risks; avoid a blind Cartesian product of variants.
- Supply explicit `dependencyPaths` for the reviewed consumer/component/models/
  catalogs/assets. Hashes prove only listed files; unknown dependencies remain
  unknown. A failed render or warning needs investigation, not a false PASS.
- Use unique output names in an owned evidence directory. Preserve originals.
  Inspect the PNG attachment using image-capable tools, or request `imageMode: path`
  and read the returned PNG through the harness. No external image viewers,
  desktop screenshots, production panels, theme changes or shell restarts for
  development previews. A path string alone is not a viewed image.
- For geometry changes, request unique `measureObjects` objectName values. These
  are axis-aligned logical scene bounds, not compositor placement. Preserve actual
  sizing bindings; forcing a capture canvas must not conceal page-driven resize.
  On 0.3.0 use geometryChecks for declared alignment, symmetry, bounds, sizes and
  spacing invariants with a logical-unit tolerance. Do not enforce symmetry or
  no-overlap on deliberately asymmetric/layered designs. Failed checks retain a
  diagnostic PNG: inspect it, correct authorized findings and rerender. Use the
  bounded visual snapshot to discover names/state, not as a screen-reader test.
  Prefer warningsPolicy error for fixture acceptance; investigate typed warnings
  and explain any explicit report-policy exception. Geometry/diagnostic PASS is
  separate from native design, anti-slop and interaction acceptance.

## Native design and anti-slop review

Load `anti-slop` when available for changed UI/copy, preserving the project/host
contract and its carve-outs. If unavailable, use the checks below and state the
fallback. Web rules do not establish native QML units, mobile breakpoints or a
universal desktop target size. Do not change global anti-slop policy for a plugin.

Inspect hierarchy, alignment, spacing, readable density, semantic palette roles,
text clipping/overlap, long values and stable panel geometry. Prefer installed
host tokens/components over invented colors, typography and decorative chrome.
Check meaningful feedback, specific action labels and honest state text. Remove
unmotivated gradients/glows, decorative badges, generic AI icons and filler only
within authorized edits; appearance preferences are not confirmed defects.

Measure contrast for actual colors including alpha composition when claimed.
Review keyboard/focus and accessible naming separately; images alone do not prove
interaction or assistive-technology behavior. OpenDesign can support a requested
new direction, but host components and project brand guidance remain primary;
do not import a web reference as a replacement native design system.

## Evidence and completion

Record candidate/dependency hashes, renderer/host versions, palette, state, locale,
logical/pixel dimensions, DPR, backend, inspected images, observed findings and
missing coverage. Report rendering, image inspection, design review, anti-slop
and interaction outcomes separately as PASS/FAIL/NOT VERIFIED/N/A. The renderer
does not evaluate design quality; a call or image read cannot grant acceptance.

Fix confirmed in-scope defects, recapture affected states and inspect the new
images. Backend-only/doc work needs no ritual render when visible consumers are
unchanged. Reuse reviewed evidence for an unchanged snapshot. Hooks may remind
the agent, but cannot guarantee visual understanding or force every model's tool
selection. Do not claim universal native readiness or independent review.
