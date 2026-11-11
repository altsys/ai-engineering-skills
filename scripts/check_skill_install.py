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
for skill in skills:
    doc = skill / "SKILL.md"
    data = doc.read_text(encoding="utf-8")
    if not data.startswith("---\n") or not re.search(r"(?m)^name:\s*\S+", data) or not re.search(r"(?m)^description:\s*\S+", data):
        failures.append(f"{skill.name}: missing YAML name/description")
    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", data):
        if "://" in target or target.startswith("#"):
            continue
        if not (skill / target).resolve().exists():
            failures.append(f"{skill.name}: missing linked file {target}")
print(f"Checked {len(skills)} skills at {root}")
if failures:
    for failure in failures:
        print("FAIL:", failure)
    raise SystemExit(1)
print("PASS: metadata and local Markdown links resolve")
