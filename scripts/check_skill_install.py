#!/usr/bin/env python3
"""Check skill packaging and relative Markdown links without extra dependencies.

Usage:
  python3 scripts/check_skill_install.py
  python3 scripts/check_skill_install.py ~/.agents/skills
"""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "skills"
if not root.is_dir():
    raise SystemExit(f"Skills directory not found: {root}")
skills = sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
if not skills:
    raise SystemExit(f"No SKILL.md files found in {root}")
failures = []
if len(sys.argv) == 1:
    expected = {
        "ai-engineering-coach",
        "ai-engineering-foundations",
        "ai-engineering-knowledge-systems",
        "ai-engineering-agents",
        "ai-engineering-production",
    }
    actual = {skill.name for skill in skills}
    if actual != expected:
        failures.append(f"Expected five grouped skills; found {sorted(actual)}")
for skill in skills:
    doc = skill / "SKILL.md"
    data = doc.read_text(encoding="utf-8")
    if not data.startswith("---\n") or not re.search(r"(?m)^name:\s*\S+", data) or not re.search(r"(?m)^description:\s*\S+", data):
        failures.append(f"{skill.name}: missing YAML name/description")
    for nested in skill.rglob("SKILL.md"):
        if nested != doc:
            failures.append(f"{skill.name}: nested skill would appear separately: {nested.relative_to(skill)}")
    for page in skill.rglob("*.md"):
        data = page.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", data):
            if "://" in target or target.startswith("#"):
                continue
            if not (page.parent / target).resolve().exists():
                failures.append(f"{skill.name}: {page.relative_to(skill)} has missing link {target}")
print(f"Checked {len(skills)} skills at {root}")
if failures:
    for failure in failures:
        print("FAIL:", failure)
    raise SystemExit(1)
print("PASS: metadata and local Markdown links resolve")
