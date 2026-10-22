# Authoring: contracts before callbacks

[Entry](../SKILL.md) · [Lifecycle recipes](performance-review.md) · [Security](security-review.md) · [Translation hook](localization-review.md)

## Host and delivery checklist

- Verify the installed manifest schema, author namespace (not reserved `omarchy.*`), declared kinds/entryPoints, exact case-sensitive paths, packaged imports/assets/helpers, permissions and supported Qt/Quickshell versions. A panel loaded internally by a bar widget belongs to that widget; declare a separate `panel` kind only when the target host supports and loads that standalone entry point. Do not assume every host supplies `bar.shell`; use its documented integration point inside the existing shell.
- `root.opened`, `sleeping`, formatter, screen and theme adapters below are application contracts, not promised host APIs. Wire actual enable/suspend/disable events; unknown state must not authorize work. Render unavailable/loading/stale/error states through catalog keys.
- Prefer existing platform features. A is reactive service; B is one owned streaming helper; C is gated/dual-cadence polling; D replaces command-based file reads. D can combine with C. These are architecture policies, not corpus prevalence or CPU claims.

## User installation path

**Critical delivery gate:** for an ordinary plugin intended for one-command
installation, a user must be able to start at the Marketplace detail page, copy
one native command and obtain the working plugin. A published or `Verified`
listing is not proof of installation availability. This is this skill's delivery
criterion, not a claim that official policy forbids genuinely manual plugins.

Before submission, put a copyable `omarchy plugin add <public-repository-url> --enable`
command near the top of the README, before long feature/media sections. Use the
exact public repository URL and stable manifest ID. Check the installed CLI's
options rather than inventing an installer. Separate optional developer builds
and tests from the ordinary user path. Do not require make, a compiler, a first-run
download, an extra service or privileges when the reviewed package does not need
them. Disclose real prerequisites, update/removal paths and changes to user state.
If manual setup genuinely is necessary, document the reason and working steps,
chain failures before enablement, and report the one-command exception explicitly.

Test that exact packaged command in a fresh isolated destination without relying
on a developer checkout, installed local artifacts or an undeclared toolchain.
Check clone, validation, executable bits/assets/helpers, enable dispatch and a
real useful result. Exercise failed installation/setup and existing-ID refusal
without overwriting user data. Label any stubbed shell dispatch separately from
actual loaded/physical behavior. For a bundled executable, bind it to reviewed
source with a reproducible build and direct byte comparison when claiming that
equivalence; repository-declared hashes alone do not supply independent proof.

After publication, inspect both the live catalog entry and the actual Marketplace
detail page. Require `installAvailable: true`, a non-empty correct `installCommand`,
and a visible copy action that copies that command; an HTTP 200 or command hidden
in HTML/source is not this check. Execute the copied command through the fresh
consumer above. `Manual setup`, `installAvailable: false`, an empty/wrong command,
failed copy or failed installation leaves one-command acceptance incomplete.
A README command or green CI cannot substitute for the public consumer. Missing
browser/clipboard/install evidence is NOT VERIFIED, not an inferred pass.

Read current Marketplace verification/installation policy and issue templates.
If a registry manual override hides the command, use the supported exact-listed-
snapshot standard-installation request and provide the acknowledgment and
packaging evidence, when that action is authorized. Reuse an open request for
the same action; an already closed update is not an open installation request.
Check baseline/review eligibility: an accepted bundled binary is not automatically
eligible for an installer-only exception. A rejected/ineligible path needs an
explicit maintainer decision or supported policy correction, not an approval
label applied by the plugin author, a speculative code rewrite or hidden capability.
Keep the request open/blocked with the concrete next owner until the live catalog
and card actually change. A submitted request or approval label is not deployment.

Record the reviewed full SHA and exact source installed by the command separately.
The current native add/update command follows mutable upstream HEAD; do not invent
an unsupported SHA option or claim installation is bound to the verified snapshot.
Keep repository publication, verification, installation availability, fresh install,
loaded identity and human acceptance separate. Publication can be complete while
one-command acceptance is blocked; continue remaining authorized work or state
the actual external blocker. This guidance grants no new publication authority.

## Diagnose and change only what is needed

Before a fix, record the symptom, expected behavior, host/source version and a safe reproduction. If reproduction is unavailable, state the limit instead of inventing a failure. Trace the relevant binding, callback or process lifecycle; name one hypothesis and the observation that would disprove it. Prefer one attributable change over several speculative fixes. For a new feature, define the observable result first.

Choose an existing host capability before adding an abstraction or helper. Keep edits within the requested behavior: match local style, avoid unrelated formatting/refactors, and remove only unused code introduced by your change. Existing unrelated defects belong in a separate note. Do not remove working code merely because it predates a test.

Pair each planned change with a check using the [review evidence ladder](plugin-review.md). Preserve valid evidence for an unchanged snapshot; rerun affected checks after relevant code, configuration or environment changes. Never reproduce a regression by reverting a live desktop worktree. Use an authorized temporary copy or isolated test input; isolation still does not authorize executing untrusted plugins.

For work spanning sessions, leave a short handoff: source/version, decisions, rejected alternatives, changed paths, observed checks, remaining risks and next action. A small plugin task needs neither an obligatory swarm nor a new persistent service.

## A — Reactive PipeWire example

QML component body; QtQuick and the installed PipeWire service are prerequisites. Documented Quickshell v0.2.x member names below still require target-version checking.

```qml
import QtQuick
import Quickshell.Services.Pipewire
Item {
    id: root
    readonly property var sink: Pipewire.defaultAudioSink
    PwObjectTracker { objects: [root.sink] }
    readonly property var volume: root.sink && root.sink.audio
        ? root.sink.audio.volume : null
}
```

No plugin subprocess or polling timer. Null is unavailable, not muted/zero. The tracker binds node details; hotplug may temporarily remove the sink. For MPRIS use `Quickshell.Services.Mpris`; Hyprland uses **`Quickshell.Hyprland`**, not a guessed Services namespace. Read each actual service API. Do not copy a polling CLI fallback without explaining why the service cannot supply the feature.

## Text and markup rendering safety (`SEC-003`)

In Qt Quick, `Text` and `Label` components default to `Text.AutoText`. Qt Quick's text engine heuristically inspects strings for HTML tags and formatting:
- If dynamic or untrusted text contains HTML elements (e.g. `<font color=...>`, `<b>`, `<img>`, or entities), Qt parses them as rich markup rather than literal text.
- This creates layout displacement, visual corruption, and potential unintended network fetches (such as inline `<img src="http://...">` tags triggering remote HTTP connections).
- Always specify explicit `textFormat: Text.PlainText` on any UI element rendering dynamic or external text:

```qml
Text {
    text: root.dynamicMessage
    textFormat: Text.PlainText
}
```

## Remote asset handling and image loading (`SEC-005`)

In Qt Quick, `Image` elements loading remote `http://` or `https://` URLs load asynchronously across the network. However, directly binding `Image.source` to untrusted or external remote URLs introduces privacy tracking (referrer/IP leakage), cache-poisoning risks, and unexpected network resource consumption. Furthermore, local images load synchronously by default, which can stall the QML render thread on large asset decodes unless explicitly decoupled.

- **Local assets:** When loading local disk images, ensure paths are anchored to approved application directories and specify `asynchronous: true` to prevent main-thread decoding stalls on large bitmaps:
  ```qml
  Image {
      source: "file://" + root.safeAssetPath
      asynchronous: true
  }
  ```
- **Remote images:** First establish the permitted destinations and input trust, then prefer an existing reviewed host fetch/cache facility. For untrusted URLs, cover destination and redirect validation, DNS-rebinding protections where applicable, TLS authentication, byte/dimension/decode limits, deadlines and private cache ownership before handing QML a verified asset. A URL scheme check alone is insufficient. Choose bounds for the actual workload; do not add a new helper merely to match an example.
- **Optional WebP profile:** Projects that explicitly adopt the [SEC-005 WebP profile v1.0.0](https://github.com/PavelLizunov/omarchy-plugin-observatory/blob/9b55c22a55d1d9faac5149b0ceaf8a930022fece/docs/specs/sec005-webp-profile.md) must follow that profile's destination, pinned-IP/TLS, redirect, structural-validation, isolated-decode and cache contract, including its failure cases and limits. Read the pinned specification before implementing or auditing conformance. It is an Observatory project profile, not a universal Omarchy API, Marketplace requirement or mandatory dependency for every plugin. Report profile conformance separately from contextual security findings.

## Dynamic evaluation sinks (`SEC-006`)

Never pass non-literal or dynamically formatted strings to `Qt.createQmlObject()`. Dynamic QML evaluation acts as an unconstrained script execution sink. Replace dynamic component creation with declarative `Loader` items referencing developer-controlled static component files, passing dynamic values strictly via properties:

```qml
Loader {
    source: "components/DynamicCard.qml"
    active: root.showCard
    onLoaded: {
        item.cardData = Qt.binding(function() { return root.safeData; });
    }
}
```

This binding keeps a non-required `cardData` property current while the item lives. A plain assignment is an initial snapshot only. For a `required` property, supply it at creation time using a declarative `sourceComponent` binding or the verified Loader initialization API; `onLoaded` is too late to satisfy construction requirements. Test data replacement without reload and destroy/recreate behavior.

## Parse, validate, preserve evidence

Pure JS functions for already byte-bounded, complete frames. Put inside the owning QML component or a local JS module. `null` explicitly means unknown/unusable.

```js
function evidenceBoolean(value) {
    return typeof value === "boolean" ? value : null;
}
function decodeFrame(text) {
    try {
        const x = JSON.parse(text);
        if (!x || typeof x !== "object" || Array.isArray(x)) return null;
        if (typeof x.value !== "number" || !isFinite(x.value)
                || x.value < 0 || x.value > 100) return null;
        return { value: x.value, enabled: evidenceBoolean(x.enabled) };
    } catch (_) { return null; }
}
```

Syntax guard is not schema validation; false and zero survive. Decide whether failure clears data or retains explicitly stale last-good state. Bound nesting, frame bytes, rate and stored history independently. Do not log secrets or unbounded invalid input. A finite one-shot `head -c 65536` limits bytes, but cannot by itself prove complete JSON or detect all truncation: use an upstream length/EOF contract or reject ambiguous completion. Preserve producer failure; never use this cap as a permanent streaming protocol.

## Ownership and hotplug

For every resource record **creator / owner / maximum / cancellation / late-result policy**. QObject parentage, visual parenting and JS references differ. C++ bridges need RAII, thread-affinity-safe queued delivery, cancellation and no dangling QObject callbacks; parentage does not prove thread safety.

Inside an `Item { id: root }`, with a ready Component containing no unbounded side effects:

```qml
property var rows: []
readonly property int maxItems: 64
function addRow(component, properties) {
    const object = component.createObject(root, properties);
    if (!object) return;
    const next = rows.slice();
    next.push(object);
    while (next.length > maxItems) next.shift().destroy();
    rows = next;
}
```

Only destroy exclusively owned dynamic objects, never shared services or Loader/Repeater-owned children. Eviction bounds ongoing sessions; root parentage only supplies teardown. Use a fixed positive cap and cap item payloads too; plain data uses splice/reassignment, not destroy. Reassign QML `var` collections when change notification is needed. Disconnect subscriptions and discard obsolete responses after lifecycle changes.

Screen example: `readonly property string screenName: targetScreen ? targetScreen.name : "default"`, where `targetScreen` is the actual declared nullable screen. A guard or `Variants` must cover that dereference and delegate removal, not merely exist nearby. Use verified host theme/spacing tokens (e.g. Color/Style only if supplied). Test hotplug, scaling, theme changes, repeated enable/disable and long-session eviction; ordinary JS errors do not establish native crashes.

## Integration checks and sources

Recipes are not complete plugins or executed Qt tests. Exercise malformed/oversized data, false/zero/unknown, dependency absence, sleep/wake, cancellation, stale replies and ownership. Any changed UI string triggers the local translation pipeline before completion.

API references: [Pipewire](https://quickshell.org/docs/v0.2.0/types/Quickshell.Services.Pipewire/Pipewire/), [PwObjectTracker](https://quickshell.org/docs/v0.2.1/types/Quickshell.Services.Pipewire/PwObjectTracker/), [Qt dynamic object creation](https://doc.qt.io/qt-6/qtqml-javascript-dynamicobjectcreation.html). These are optional provenance links, not required runtime downloads.
