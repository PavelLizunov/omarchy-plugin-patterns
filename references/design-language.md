# Omarchy plugin design language

Use this reference when building or changing a plugin's visible interface. It
consolidates maintainer design iterations across messaging, monitoring, speech,
device and plugin-management tools, with selected community guidance. These are
product defaults, not an official Omarchy specification or measured usability
results. The current user's choices and the installed host contract take priority.

## Start with the job, not a component catalog

Before editing, identify the primary task, opening surface, information that must
remain visible, frequent actions and recovery route. Read the closest existing
native screen and preserve settled identity and interaction decisions. A bar
popover, voice client, device editor and workbench need different compositions.
Write down only the decisions useful to the current change, in existing project
documents when needed; do not create a new planning framework.

For each proposal ask: what will the user recognize, do and recover from here?
A matching palette alone is not a coherent interface. Prefer one obvious working
region with subordinate navigation and metadata over a gallery of equal cards.

## 1. Compact means task-complete, not featureless

For a bar-driven tool, normally open a useful anchored compact surface on the
primary click. Do not launch a large workbench merely to mute audio or inspect a
status. This does not require a bar entry point for headless services or unrelated
plugin kinds.

Preserve the task's essential context in compact mode: for a voice client that
can mean the active room, participants, mute and leave; for messaging, navigation,
search, readable messages and input. Reflow or navigate between meaningful pages
instead of hiding the panel the user came for. Avoid empty startup pages that
only tell the user to select an object without showing how.

If an expanded mode exists, keep its route available from relevant pages and
preserve the selected object and draft. Expansion is not a workaround for an
unusable compact picker, text selection or navigation.

## 2. Remove noise before shrinking content

Use alignment, concise labels and progressive disclosure to achieve density.
Do not shrink all typography, squeeze a diagram, overlap hit targets or cut
essential labels to fit. Avoid duplicate headings, large explanatory paragraphs,
redundant values and a border/card around every label. Put diagnostics and rare
settings behind a clear secondary route; keep essential actions visible.

A monitoring overview should reserve room for the useful graph or process list,
not spend the whole surface on tiles. A manager can start with icon, name and
state rather than a telemetry table. These are task-specific examples, not a
universal two-tile limit. Short content should fit naturally; long lists scroll
inside their intended viewport. A few pixels of accidental scrolling on the
normal overview is a layout defect, not evidence that scrolling solved fit.

## 3. Share geometry; adapt to available space

Keep the bar slot stable across ordinary status changes. Keep the same task
panel and its navigation anchored across tabs, editor entry and feedback. Let a
shared container own the frame and fit it to the host's available screen; scroll
long content internally. See [stable panel geometry](design-review.md#keep-tabbed-panel-geometry-stable).

Use common icon columns, baselines and trailing-action alignment. Preserve
optical balance rather than forcing asymmetric brand marks into mathematical
symmetry. Fit controls to their content and role: a small numeric field is not
a full-width primary action, and a command-menu row is not a dropdown option.
Reserve the largest applicable state border so hover/focus does not relayout
neighbors. Breakpoints follow actual content, text scale and orientation, not
a copied web breakpoint or one plugin's fixed dimensions.

## 4. Inherit the live host, not a second theme system

Use the installed `qs.Ui` components and `qs.Commons` Color, Style and Border
contracts. Follow semantic surface roles, configured typography, spacing,
state fills, borders and corner geometry. Honor theme/user overrides. Quiet,
mostly neutral chrome and restrained edges are the default; square construction
is a useful baseline, not permission to override the user's rounding.

Do not hard-code black/white, a permanent brand green, JetBrains Mono, opacity
recipes or fixed control heights merely because a reference uses them. Plain
host buttons may be borderless at rest; do not coat every action and selection
in accent fill. Prefer host state helpers over copying their current numeric
alphas. Distinguish surface edges, control edges and dividers.

Hosted plugins consume the shell's live theme. Standalone-app advice to parse
`colors.toml`, derive missing colors or add an explicit theme reload is not a
replacement for that contract. Where names collide, qualify the installed Color
singleton, for example `import qs.Commons as Commons` and
`Commons.Color.foreground` on the inspected Qt 6.12 host.

## 5. Recognizable identity, calibrated at native size

Keep the service or plugin recognizable while adapting its mark to the native
bar vocabulary. Preserve an already selected silhouette. Match painted size,
weight and baseline to neighboring native icons, not merely identical SVG boxes.
A thin hairline reference does not justify an almost invisible glyph; a custom
image can also become too small after a host update despite an unchanged slot.

Keep idle appearance quiet. Use color, badges and motion for real states rather
than decoration. Put auxiliary status inside the existing pixel budget without
covering the identity or widening the slot; a microphone must not compete with
the main service mark. Exact badge placement and one-pixel gaps are local design
choices, not ecosystem-wide constants.

Prefer available native glyphs for ordinary actions. Custom SVG/QML is valid for
an existing or requested identity/microgauge; neither SVG-only nor font-only is
a global rule. Detailed device content can use the requested accurate product
photo even when the bar uses a stylized mark. Where the installed skill includes
`references/icon-adaptation.md`, use it for actual slot, decoding and detail limits.

## 6. Use meaningful internal icons, with enough words

Carry identity into the panel and place meaningful native icons beside important
destinations, section headings and actions. A good bar mark alone does not finish
the internal UI. Keep one coherent vocabulary and retain labels where meaning is
not obvious. Unrecognizable server avatars need names, not more abstract symbols.
Do not decorate every value or paragraph. Use the relevant
[design review](design-review.md) iconography guidance when available.

A familiar compact utility may use an icon-only control when its meaning is
clear and its tooltip/accessibility name is supplied. This is not a license to
replace ambiguous destinations or destructive operations with unexplained glyphs.

## 7. Navigation follows the user's object and intent

Opening a container normally reveals its useful contents or overview, not a
random first/last child that the user did not select. In the voice-client case,
opening a server reveals channels; opening channel text is distinct from joining
a call. Do not turn browsing into an external action or saved configuration change.

Keep back, location and selection understandable. Visually distinguish system
destinations such as archive/settings from user objects while retaining the same
grid. Search needs a named scope and recognizable result types. Remembered state
is useful only when it preserves the current product contract rather than silently
replacing the expected landing page.

## 8. Prioritize actions by frequency and consequence

Keep immediate operational controls such as mute, stop stream and leave call
visible during the activity. Move rare account operations such as logout away
from frequent window controls and accidental-click paths, into a named secondary
route. A clean screen with a hidden emergency exit is not simple.

Distinguish dismissing a panel, stopping an operation, reconnecting a backend and
logging out. Offer task-appropriate retry/reconnect without requiring account
logout or a shared-shell restart. Recovery does not mean every trivial plugin
needs a permanent restart button. Preserve drafts and unrelated activity where
the operation permits; explain a genuinely destructive consequence.

## 9. Feedback reflects actual, scoped state

Differentiate loading, empty, unavailable, stale, pending, saved and failed where
relevant. Unknown telemetry is not zero. Device presence, active input device and
settings application are different states; using another mouse must not falsely
paint a connected device as disconnected. A status indicator needs real meaning.

Show the result of the current operation rather than an old success. If a control
is unavailable, explain the reason or omit an unimplemented feature; do not ship
an enabled-looking placeholder. Keep useful errors dismissible/copyable and offer
an appropriate recovery route without wiping unrelated work.

## 10. Contrast expresses information hierarchy

Separate identity, main content and metadata through alignment, weight and
semantic brightness before adding arbitrary colors. In messaging, author, body,
time and presence must not merge into one visual mass. Muted text must remain
readable; white-on-white and low-contrast idle icons are not native styling.
Status colors communicate an actual state, not a decorative default red.

Reason about the composited background, including translucent selection and
surface fills. Keep applicable light/dark themes and larger text in the design
scope; do not claim their contrast was measured without actual evidence.

## 11. Keep ordinary desktop interactions ordinary

Preserve selecting/copying part of a message, copying paths/errors/commands,
pasting and relevant context menus in compact and expanded views. A copy-whole
button does not replace partial text selection. Gesture/drag handlers must not
swallow text editing or unrelated clicks.

Nested pickers and menus must leave the essential working area reachable and
receive dismissal before their parent. Follow the host's Escape, outside-click
and focus-return behavior; do not hide a panel on every focus change or dismiss
an unresolved decision dialog as if it were a casual popover. External dialogs
must not be trapped behind the plugin's layer. Draggable surfaces need a clear
affordance when movement is part of their product contract.

## 12. Keyboard-first does not mean shortcut overload

Expose a small set of relevant, implemented shortcuts. Extend familiar mappings
without building physically awkward multi-modifier chords; a five-key translation
shortcut was explicitly rejected. Keep full help secondary and current. Do not
invent a keymap merely to fill a footer.

Use the host's keyboard and focus contract. Pointer and directional keys should
operate one transient cursor, distinct from persistent selection and text focus.
Suspend panel-level single-key shortcuts during text entry and nested popups.

## 13. Make repeated configuration easy to recognize and control

Where the task calls for profiles, expose the active named profile and a quick
switching route near its working context. Distinguish selecting, editing, applying
and saving rather than silently writing settings while browsing. Give supported
numeric controls an exact-value route when a slider alone cannot express the
requested value. Name sensors/devices for people, retaining technical identifiers
in details and admitting uncertain mappings instead of inventing certainty.

These are defaults for configuration-heavy tools, not a requirement to add
profiles, numeric editors or hardware diagrams to every plugin. An accurate
reference image is better than a speculative decorative schematic.

## Use and evidence

Apply only the rules relevant to the requested change. Existing user decisions
can justify exceptions; record a concrete reason, not a generic style apology.
This guide does not automatically start tests, audits, previews, recordings,
model reviews or desktop operations. Run discretionary checks only when the
current user requests them, following the host's execution policy. When visual
review is requested, use the existing
[design review](design-review.md), [visual review](visual-review.md) and
[QML visual cycle](qml-visual-cycle.md), not a second renderer.

Source implementation, installed files, loaded UI, inspected fixture pixels,
live interaction and user preference acceptance are different outcomes. Historical
positive feedback does not approve a later redesign. Textual guidance cannot
prove future agent compliance or repair existing plugins by being loaded.

## Community provenance and deliberate adaptations

- [huacnlee/omarchy-style, Design Guides](https://github.com/huacnlee/omarchy-style/blob/abd42e1b16a867445353e74958829ba8ebc48e19/skills/omarchy-style/references/design-guides.md),
  MIT, inspected revision `abd42e1b16a867445353e74958829ba8ebc48e19`.
  Adopted principles: whole-screen composition, quiet surfaces, intrinsic control
  sizing, painted icon alignment, distinct cursor/selection/focus and restraint
  in borders/accent. Its upstream baseline is Omarchy commit
  `945549699026df6c888a6b1bd4e06fbf55a67595`, not every installed version.
- [tcballard/build-omarchy-plugins, Theme/layout](https://github.com/tcballard/build-omarchy-plugins/blob/ee5a8e49646186097559946dffb91bb7a7368577/skills/omarchy-qml-patterns/references/theme-and-layout.md)
  and [plugin design](https://github.com/tcballard/build-omarchy-plugins/blob/ee5a8e49646186097559946dffb91bb7a7368577/skills/omarchy-plugin-design/SKILL.md),
  MIT, inspected revision `ee5a8e49646186097559946dffb91bb7a7368577`.
  Adopted principles: smallest useful surface, installed host over examples,
  qualified Color, orientation-aware layout and per-view interaction state.
- Local source comparison: Omarchy package `4.5.0rc2-1`,
  `shell/Ui/Button.qml`, `shell/Ui/OpticalGlyph.qml` and the state-token section
  of `shell/Commons/Style.qml`. This is source evidence, not runtime acceptance.

The recommendations above are rewritten synthesis, not bundled third-party
skills or copied templates. Their MIT licenses remain with their repositories.
Community branding advice is not official certification. Deliberately not adopted:
a mandatory font-only icon policy, universal pixel sizes, a theme parser inside
hosted plugins, treating invalid progress as zero, and poster/web asset rules for
native panels. None of those fits all of our plugin contracts. Private chat
transcripts are not part of this distributable reference.
