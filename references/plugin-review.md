# Review: evidence before verdict

[Entry](../SKILL.md) · [Security](security-review.md) · [Performance](performance-review.md) · [Localization](localization-review.md)

## Worker → frozen draft → independent reviewer

1. State authorized scope and source identity: repository, revision if verified, directory and file hashes when available. Cache names are not revision evidence. List the plugin directory, including hidden/nested files. Personally read **every in-scope file fully** with the host's read tool, continuing beyond output limits. Resolve imports, manifest assets, scripts and native helpers. Binary/unavailable/unread content stays `[U]`; no fabricated coverage or regex/batch source audit.
2. Missing local files may reflect incomplete checkout. Check only an authorized, verified upstream repository/ref/path. A genuine 404 establishes absence there, not at an unknown revision or across the project. Auth/network errors stay unknown. With consent, retrieve into an isolated cache, record provenance and read fully; never silently modify or execute the user's plugin tree.
3. Record risks **and protections**, surrounding guards, alternative explanations and unresolved checks. Freeze the draft and source snapshot before review.
4. An independent reviewer reopens quoted lines, checks exact characters including whitespace, and reads surrounding control/data flow. Shifted/invented quotations require correction. Changed files invalidate affected anchors. Self-review is not independence or revision attestation. If an independent reviewer is unavailable, deliver a useful unsigned `REVIEW-REQUIRED` draft, not a simulated approval. Do not spawn agents against host/user policy.

## Six review dimensions

| Dimension | Mandatory questions |
|---|---|
| 1 Manifest/delivery | Valid schema/kinds/entryPoints, namespace, paths, assets, imports, executable dependencies and supported versions? |
| 2 Processes/privileges | Actual dispatch paths, argv and environment, input control, authorization, helper ownership, consented writes? |
| 3 Timers/cadence | Interval/repeat/rearm, detail/status distinction, enable/sleep gates, overlap, retries and cancellation? |
| 4 Resilience/data | Transport byte caps, guarded JSON, shape/range checks, truncation, EOF, failure/stale state and recovery? |
| 5 Memory lifecycle | Bounded collections/payloads, dynamic parentage plus eviction, callbacks, requests and native ownership? |
| 6 Multimonitor/theme | Guards covering actual screen dereferences, Variants delegate lifecycle, hotplug, scale and verified theme tokens? |

Localization, translation and a11y cut across all six, including denial/error messages; do not replace a dimension with i18n. For focused review, explicitly mark omitted dimensions, never imply full coverage.

## Anchor and verdict contract

Template only, not an observed finding:

```text
file: <exact authorized relative path>
line: <actual 1-based integer>
snippet: <verbatim entire cited line including whitespace>
type: <risk OR protective category>
proof: <function/callsite; supporting ranges; evidence grade;
        input → operation → guard → consequence; limits/counterevidence>
```

- `[D]`: directly documented observation from identified source, not automatically observed runtime behavior.
- `[I]`: supported interpretation with explicit preconditions and scope.
- `[H]`: hypothesis with competing explanation and falsifier/test.
- `[U]`: evidence unavailable; list what would resolve it. Missing/null/nonboolean evidence never becomes false.

Protective categories: `GUARDED_JSON_PARSE`, `GATED_TIMER`, `DEBOUNCE_TIMER`, `DISCRETE_ARGV_DISPATCH`, `SYSTEM_AUTH_DELEGATION`. Explain coverage and remaining risk; a protection keyword alone proves no safety.

| Tempting finding | Required false-positive check |
|---|---|
| sudo/pkexec = escalation exploit | Is this executable code, not UI/comment/URL? What authorized action and policy? |
| Process = running subprocess | Identify launch path, lifecycle and frequency; declarations are not executions. |
| concat = injection | Array vs script string? Attacker-controlled operand reaching shell? Inspect actual enum/quoting guard. |
| Subsecond timer = periodic drain | repeat:false? Rearm rate? Animation vs polling? Dispatch gate? No energy inference. |
| screen/Variants = crash/safe | Guard covers exact dereference and hotplug lifetime? JS exception is not proof of native crash. |
| push/parent/splice = leak/safe | Bound every allocation path during root lifetime; distant cleanup is insufficient. |
| try/catch = validated data | Verify schema/ranges, input byte cap and honest fallback. |
| Translation looks fluent = correct | Check meaning, uncertainty, IDs, placeholders, CLDR and actual RTL/a11y tests. |

Use local report vocabulary, not a claim about an official marketplace rating: `pass` means completed scoped static checklist; `warning` is a supported shortcoming; `broken` is an established delivery/load blocker; `suspicious` is a supported serious security-risk mechanism, not inferred malice/exploitation. Incomplete evidence has separate review status and no final pass. Report actual checks separately from proposals; signoff does not grant commit, publication or runtime permission.

## Evidence boundary

This experimental package does not publish a research corpus, source-revision attestations or measured defect rates. Its recommendations must be checked against the plugin being reviewed and the installed host. Never manufacture examples as real findings, infer energy measurements from syntax, or describe these instructions as a security certification.
