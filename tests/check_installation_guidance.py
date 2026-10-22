#!/usr/bin/env python3
"""Offline guidance wiring only; not a model, browser or installation test."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]


def covers_installation(entry, authoring):
    entry_parts = (
        "## Critical Marketplace installation acceptance",
        "#user-installation-path", "installAvailable: false", "installCommand",
    )
    authoring_parts = (
        "**Critical delivery gate:**", "Before submission", "fresh isolated",
        "real useful result", "stubbed shell dispatch", "developer builds",
        "After publication", "installAvailable: true", "installCommand",
        "visible copy action", "Execute the copied command", "Manual setup",
        "incomplete", "green CI cannot substitute", "NOT VERIFIED",
        "standard-installation request", "installer-only exception",
        "maintainer decision", "mutable upstream HEAD", "unsupported SHA option",
        "Publication can be complete while", "genuinely is necessary",
    )
    return all(x in entry for x in entry_parts) and all(x in authoring for x in authoring_parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publication-skill", type=Path,
                        help="Optional installed companion skill to check, never inferred")
    args = parser.parse_args()
    entry = (ROOT / "SKILL.md").read_text()
    authoring = (ROOT / "references/plugin-authoring.md").read_text()
    assert covers_installation(entry, authoring), "Critical one-command guidance is incomplete"
    assert "#user-installation-path" in (ROOT / "README.md").read_text()
    assert "tests/check_installation_guidance.py" in (ROOT / "README.md").read_text()

    # Each previously mistaken success is insufficient, without manufacturing a site test.
    for incomplete in (
        "README includes omarchy plugin add URL --enable; ready to publish.",
        "Verified and all CI passed; the package installs locally.",
        "Manual setup; record a catalog correction and finish the task.",
        "installAvailable: true; command exists in HTML; copy/install untested.",
        "Request approved; no need to inspect the deployed card.",
        "Require an unsupported SHA install option to pass acceptance.",
    ):
        assert not covers_installation(entry, incomplete), incomplete
    for needed in ("visible copy action", "fresh isolated", "installer-only exception",
                   "mutable upstream HEAD", "Publication can be complete while"):
        assert not covers_installation(entry, authoring.replace(needed, "")), needed
    assert not covers_installation("User installation path", authoring), "Entry point must load the gate"

    if args.publication_skill:
        companion = args.publication_skill.resolve(strict=True)
        skill = (companion / "SKILL.md").read_text()
        checklist = (companion / "references/PUBLISHING-CHECKLIST.md").read_text()
        assert "#critical-one-command-installation-gate" in skill
        for text in (skill, checklist):
            assert "critical" in text.lower() and "installAvailable" in text and "installCommand" in text
        for needed in ("### Critical one-command installation gate", "Before submission:",
                       "After publication:", "visible copy action", "fresh isolated",
                       "installer-only", "mutable upstream HEAD", "NOT VERIFIED",
                       "one-command installation acceptance separately"):
            assert needed in checklist, needed
    print("PASS installation guidance wiring; README/Verified/CI/manual/hidden-command/request-only false-success controls rejected. No model/site/install effectiveness claim.")


if __name__ == "__main__":
    main()
