#!/usr/bin/env python3
"""Offline wiring check; this does not test model compliance or rendered UI."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def covers_panel_icons(entry, design):
    return all(part in entry for part in (
        "## Internal panel iconography", "#internal-panel-iconography",
        "header or bar icon alone", "labels and accessible names",
    )) and all(part in design for part in (
        "## Internal panel iconography", "**Identity:**", "**Semantic icons:**",
        "header-only", "Button.iconText", "Button.text", "accessible",
        "localized", "constrained", "do not silently drop",
    ))


def main():
    entry = (ROOT / "SKILL.md").read_text()
    design = (ROOT / "references/design-review.md").read_text()
    assert covers_panel_icons(entry, design), "Required panel icon guidance is incomplete"
    assert not covers_panel_icons(entry, "## Internal panel iconography\nAdd a branded header icon."), "Header-only must not satisfy semantic icon coverage"
    for name in ("README.md", "references/icon-adaptation.md"):
        assert "#internal-panel-iconography" in (ROOT / name).read_text(), name
    print("Panel identity + semantic-icon guidance wired; header-only rejected. Model/UI effectiveness not tested.")


if __name__ == "__main__":
    main()
