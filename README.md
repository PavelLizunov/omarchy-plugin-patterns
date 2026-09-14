# omarchy-plugin-patterns

An experimental agent skill for writing and reviewing Omarchy Quattro plugins in QML and Quickshell. It gives a coding agent guides for choosing system interfaces, handling processes and credentials, checking object lifetimes, and preparing UI strings for translation.

Use it when building a plugin or reviewing an existing one. The guides cover questions such as which updates should run while a panel is closed, where incoming data needs bounds, and what a localized message needs beyond a translated string. Check the examples against your installed Omarchy, Qt and Quickshell versions; they are not complete runtime-tested plugins.

## Install in OpenCode

Requires OpenCode with skill support. The package is six Markdown documents: no compiled libraries, npm packages, Python runtime, daemon or paid service is needed. Git is required only for the clone/update method below. A plugin you build may have its own dependencies.

Clone into a new directory. If the destination already exists, inspect it first and preserve any local edits:

```bash
mkdir -p "$HOME/.config/opencode/skills"
git clone https://github.com/PavelLizunov/omarchy-plugin-patterns.git \
  "$HOME/.config/opencode/skills/omarchy-plugin-patterns"
```

Start a new OpenCode session in your plugin project and ask:

> Load omarchy-plugin-patterns. Check the installed host versions and help me write a plugin for …

For a read-only translation-readiness review:

> Load omarchy-plugin-patterns and perform a Localization Readiness Review of this plugin. Read the source, report contextual findings and separate coverage measures. Do not modify files or translate yet.

A Russian prompt is also supported:

> Загрузи omarchy-plugin-patterns. Проверь готовность этого плагина к переводу: прочитай исходники, покажи подтверждённые проблемы, защитные механизмы и неизвестные данные. Пока ничего не меняй.

Confirm that the agent loads the skill. If it is missing, check the folder and `SKILL.md` spelling, duplicate skill names, skill-tool enablement and OpenCode permissions. Report a denied skill rather than bypassing the denial. See the [OpenCode documentation](https://opencode.ai/docs/skills/) for discovery rules.

For manual installation, copy `SKILL.md` and the five `references/*.md` files into the skill directory and retain the LICENSE with redistributed copies. A Claude-compatible layout is `~/.claude/skills/omarchy-plugin-patterns/`; avoid duplicate copies that OpenCode might also discover. Confirm loading in the actual client, since file layout alone cannot establish it.

## What the agent reads

The skill directs the agent to the references relevant to its task:

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Entry point, trust rules and task routing |
| [plugin-authoring.md](references/plugin-authoring.md) | Component architecture, parsing and memory ownership |
| [plugin-review.md](references/plugin-review.md) | Six-dimensional static review, reference matrix and evidence grades |
| [security-review.md](references/security-review.md) | Argv, authorization, secrets and configuration writes |
| [performance-review.md](references/performance-review.md) | Services, streaming helpers, timers and FileView |
| [localization-review.md](references/localization-review.md) | Readiness inventory, translation, CLDR plurals, RTL and accessibility |

A Localization Readiness Review covers one authorized plugin. It separates suspected patterns from demonstrated defects and reports source readiness, locale fill, structural validity and language-review coverage independently. Missing denominators remain unknown. This mode produces a review, not bulk scans, translation runtimes, exports or automatic pull requests.

For requested translations, the agent preserves technical tokens and whole-message meaning, translates, checks wording and verifies formatter structure. It can use a translation skill and `anti-slop` when available and authorized; bundled fallbacks keep them optional. Style checks do not replace language review.

## Update or pin a test

Check local edits and the current revision before updating:

```bash
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" status --short
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" rev-parse HEAD
```

Review the upstream changes, then update only with a clean working tree:

```bash
git -C "$HOME/.config/opencode/skills/omarchy-plugin-patterns" pull --ff-only
```

Keep the recorded commit for reproducible tests until you intentionally update. Do not discard local edits to force an update. To disable a Git-cloned installation, move its entire folder outside every skill-discovery directory; that keeps the edits and recorded revision together.

## Limits and feedback

These are community recommendations, not an official Omarchy API or security certification. A Markdown skill cannot force a model to follow instructions. Review its changes and dependencies, then run the authorized checks for the installed host before using a plugin. Installing the skill itself executes no plugin code.

Static review can identify a configured timer or command, but CPU, battery use and runtime behavior need measurements. Translation accuracy, rendered layout, RTL and screen-reader behavior need their own checks as well: valid keys and fluent-looking text do not establish those results. Unavailable reviewers, denied tools and unperformed checks must be reported, not simulated.

To report a problem, include the skill commit, host/client versions, a minimal non-sensitive example, and expected and observed behavior. Remove secrets and private paths; share another project's private code only with permission.

## Research context and provenance

The [Omarchy Plugin Observatory](https://github.com/PavelLizunov/omarchy-plugin-observatory) informed this skill with **3,086 historical plugin report records**, grouped into 311 chunks, and **10,310 preserved evidence anchors**. The automated assessments remain subject to source review and corrections. They are neither a verified ecosystem census nor runtime-tested findings.

Selected examples include a two-second timer requesting multiple `playerctl` processes and an 80ms `hyprctl` timer with guards against overlapping work. They motivate separating detail-only polling from necessary background status updates. Unix sockets and supported D-Bus services offer event-driven alternatives for particular data; their use alone says nothing about measured CPU or battery cost.

Credential handling and parsing require attention to the whole path. UI fields feeding `sudo -S` expose passwords to the plugin process, while an installer hook creating a symlink raises different integrity questions. Use operation-specific services with appropriate authorization and the session's authentication agent where supported. For external JSON, pair parse-error handling with bounds and structure/range checks. A `try/catch` cannot provide all of those protections.

Localized plugin copies also show why translation workflows matter. Shared catalogs can reduce synchronization work; the localization guide covers message context, plurals, fallbacks and accessibility while leaving room for the installed shell's capabilities and existing community work.

## Community sources and adaptation

The recommendations are written for Omarchy and informed by these sources. This package does not install, bundle or automatically load their skill packs:

- [Superpowers](https://github.com/obra/superpowers): investigate before fixing, verify completion against behavior and assess review feedback against the actual code. Destructive live-tree regression reverts and mandatory orchestration are not adopted here.
- [Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills): keep changes scoped and choose observable checks before editing.
- [Qt translation workflow](https://github.com/a5c-ai/babysitter/tree/main/library/specializations/desktop-development/skills/qt-translation-workflow): catalog context and translation lifecycle as review topics. The [Qt TS format](https://doc.qt.io/qt-6/linguist-ts-file-format.html) and [QTranslator contract](https://doc.qt.io/qt-6/qtranslator.html) provide the technical references; check the installed Qt version.
- [SkillCorpus](https://github.com/EverMind-AI/SkillCorpus): select relevant advice, including none when unsuitable. A catalog rank says nothing about safety, host compatibility or redistribution rights. No hosted retrieval service is required or enabled.
- [SkillsBench](https://www.skillsbench.ai/) and [Tessl](https://tessl.io/registry): their evaluations do not establish how this skill performs with your model.

No model benchmark has been run for this update. A future performance claim would need the exact skill/model/host versions, confirmation that the skill loaded, comparable tasks and budgets, repeated outcomes including failures, and resource measurements. Examples and third-party leaderboards cannot supply that evidence.

## License

Original package text and illustrative examples: [MIT](LICENSE). Linked documentation and software retain their own terms. This project is not affiliated with or endorsed by Omarchy, Quickshell or OpenCode.
