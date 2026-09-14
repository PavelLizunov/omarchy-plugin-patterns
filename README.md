# omarchy-plugin-patterns

An experimental agent skill for writing and reviewing Omarchy Quattro plugins with QML and Quickshell. It guides architecture, process and privilege handling, polling, data validation, ownership, localization readiness and translation.

**Community guidance informed by empirical static research, not an official Omarchy API or a security certification.** The architecture patterns in this skill were synthesized from static analysis records across 3,086 community plugin reports from the [Omarchy Plugin Observatory](https://github.com/PavelLizunov/omarchy-plugin-observatory). Examples need checking against your installed Omarchy, Qt and Quickshell versions; they are not complete runtime-tested plugins.

## Install in OpenCode

Requires OpenCode with skill support. Git is only needed for the clone/update method below. The skill itself is Markdown: no C/C++ library, npm package, Python runtime, daemon, paid translation service or separate anti-slop installation is required. Dependencies of a plugin you build are separate.

Clone into a new skill directory; if one already exists, inspect it first rather than overwrite it:

```bash
mkdir -p "$HOME/.config/opencode/skills"
git clone https://github.com/PavelLizunov/omarchy-plugin-patterns.git \
  "$HOME/.config/opencode/skills/omarchy-plugin-patterns"
```

Start a new OpenCode session in your plugin project and ask:

> Load omarchy-plugin-patterns. Check the installed host versions and help me write a plugin for …

For readiness only:

> Load omarchy-plugin-patterns and perform a Localization Readiness Review of this plugin. Read the source, report contextual findings and separate coverage measures. Do not modify files or translate yet.

Russian prompts work too:

> Загрузи omarchy-plugin-patterns. Проверь готовность этого плагина к переводу: прочитай исходники, покажи подтверждённые проблемы, защитные механизмы и неизвестные данные. Пока ничего не меняй.

Confirm that the agent actually loads the skill. If absent, check the exact folder/SKILL.md spelling, duplicate skill names, skill-tool enablement and OpenCode permissions. Do not bypass a denied skill. Installation paths and discovery rules: [OpenCode documentation](https://opencode.ai/docs/skills/).

Alternatively, download the repository and copy `SKILL.md` plus the five `references/*.md` files to that folder. Keep the LICENSE with redistributed copies. A Claude-compatible layout is `~/.claude/skills/omarchy-plugin-patterns/`; avoid installing duplicate copies that OpenCode would discover. Live client discovery is not certified by the package layout alone.

## What the agent reads

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Entry, trust rules and on-demand routing |
| [plugin-authoring.md](references/plugin-authoring.md) | Architecture, parsing and ownership |
| [plugin-review.md](references/plugin-review.md) | Six-dimensional static review, reference matrix and evidence |
| [security-review.md](references/security-review.md) | Argv, authorization, secrets and configuration writes |
| [performance-review.md](references/performance-review.md) | Services, helpers, timers and FileView |
| [localization-review.md](references/localization-review.md) | Readiness inventory, translation, anti-slop, CLDR, RTL and accessibility |

Localization Readiness Review reads one authorized plugin. It distinguishes suspected patterns from demonstrated defects and reports source readiness, locale fill, structural validity and language-review coverage separately. Missing denominators stay unknown. It is not a bulk scanner, translation runtime, exporter or automatic PR generator.

For requested translations, the agent preserves technical tokens and whole-message semantics, translates, checks style, then verifies meaning and formatter structure. It may use a suitable translation skill and `anti-slop` if actually available and authorized. Both have bundled local fallbacks; missing external skills do not become hidden dependencies. Style review is not language-quality approval.

## Update or pin a test

Check local edits and current revision before updating:

```bash
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" status --short
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" rev-parse HEAD
```

Only with a clean tree and after reviewing the upstream changes:

```bash
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" pull --ff-only
```

For reproducible tests, keep the recorded commit until you intentionally update. Do not discard local edits to force an update. To disable a Git-cloned installation, move the whole folder outside all skill-discovery directories; this preserves edits and the recorded revision.

## Limits and feedback

The skill cannot force a model to follow its instructions. Inspect generated changes, dependency choices and authorized runtime tests before using a plugin. Do not interpret a static `pass`, valid catalog keys or fluent-looking text as proof of safety, translation correctness, RTL layout or screen-reader behavior.

QML runtime behavior, actual client discovery on your laptop, energy measurements, rendered layout and fluent-human language acceptance remain separate checks. Permission-denied tools and unavailable reviewers must be reported, not simulated. No plugin code runs merely by installing this package.

Report a problem with the skill commit, relevant host/client versions, a minimal non-sensitive example, expected behavior and observed behavior. Remove secrets and private paths before opening an issue. Do not publish another project's private source without permission.

## Empirical research and provenance

The rules in this skill were informed by research from the [Omarchy Plugin Observatory](https://github.com/PavelLizunov/omarchy-plugin-observatory), an exploratory static analysis dataset comprising **3,086 plugin report records** across 311 chunks, capturing **10,310 preserved evidence anchors**. These records represent historical static observations from automated analysis, subject to ongoing review and corrections rather than an exhaustive census or blanket runtime verification:

- **Timer hygiene and background wakeups:** Selected static examples included unthrottled background timers running without UI visibility gating (such as repeating timers triggering multiple `playerctl` CLI processes every 2 seconds, or sub-100ms `hyprctl` polling loops). The skill guides gating detail polling to visible UI states while preserving necessary background status updates.
- **Event-driven IPC over process polling:** Integrating via native UNIX domain sockets (`Quickshell.Io.Socket`) or D-Bus signals (`Quickshell.Services`) handles events reactively and avoids recurring CLI queries for specific data.
- **Privilege boundaries and credential handling:** Historical review records identified patterns such as collecting passwords in UI `TextField` elements for `sudo -S`, installer hooks creating symlinks to user-writable files, or direct `/etc/` modifications. Rather than treating all privileged commands as malicious escalation, the skill emphasizes clear trust boundaries: avoid handling user passwords directly in UI fields, avoid silent system modifications, and delegate authentication to session Polkit agents and operation-scoped D-Bus services.
- **Defensive parsing:** Malformed or unexpected external JSON input can break QML property bindings. The skill guides wrapping external JSON parsing in `try/catch` with subsequent schema, type, and range validation, recognizing that syntax error handling alone is not complete data validation.
- **Centralized localization:** Localized copies of plugins exist across the ecosystem; adopting shared translation catalogs and workflows can reduce synchronization work while crediting ongoing upstream development. The skill provides guidelines for single-repository translation catalogs, message extraction context, CLDR plurals, fallback mechanisms, and accessibility.

## Community sources and adaptation

The guidance uses independently written, Omarchy-specific recommendations informed by these sources; it does not install, bundle or automatically load their skill packs:

- [Superpowers](https://github.com/obra/superpowers): investigate before fixing, verify completion claims and assess review feedback against the actual code. This package does not adopt destructive live-tree regression reverts or mandatory orchestration.
- [Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills): keep changes scoped and choose observable acceptance checks before editing.
- [Qt translation workflow](https://github.com/a5c-ai/babysitter/tree/main/library/specializations/desktop-development/skills/qt-translation-workflow): catalog context and translation lifecycle as review topics, not a copied implementation. The [Qt TS format](https://doc.qt.io/qt-6/linguist-ts-file-format.html) and [QTranslator contract](https://doc.qt.io/qt-6/qtranslator.html) are the technical references; check the installed Qt version.
- [SkillCorpus](https://github.com/EverMind-AI/SkillCorpus): select relevant advice, including none when unsuitable. Catalog ranking does not establish safety, host compatibility or a license to redistribute a particular skill. No hosted retrieval service is required or enabled here.
- [SkillsBench](https://www.skillsbench.ai/) and [Tessl](https://tessl.io/registry): skill quality and measured task outcomes are different questions. Their results are not evidence that this package improves your model.

For any future performance claim, record the exact skill/model/host versions, whether the skill actually loaded, comparable tasks and budgets, repeated outcomes including failures, and resource usage. A handful of examples or another project's leaderboard is not validation of this package. No model benchmark has been run for this update.

## License

Original package text and illustrative examples: [MIT](LICENSE). Linked upstream documentation and software retain their respective licenses. This repository is not affiliated with or endorsed by Omarchy, Quickshell or OpenCode.
