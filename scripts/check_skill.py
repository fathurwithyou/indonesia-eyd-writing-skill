#!/usr/bin/env python3
"""Validate routing, metadata and plugin packaging; does not grade writing quality."""
import json
import re
from pathlib import Path

import yaml

from sync_distribution import DEST, ROOT, differences


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_package(base):
    text = (base / "SKILL.md").read_text()
    parts = text.split("---", 2)
    require(len(parts) == 3 and not parts[0].strip(), f"Missing frontmatter: {base}")
    data = yaml.safe_load(parts[1])
    require(isinstance(data, dict) and set(data) == {"name", "description"}, "Expected name and description")
    require(data["name"] == "indonesia-eyd-writing-skill", "Unexpected skill name")
    require(isinstance(data["description"], str) and 0 < len(data["description"]) <= 1024, "Invalid description")
    require(len(text.splitlines()) < 500, "Main skill is too large")
    links = re.findall(r"\]\((references/[^)#]+)(?:#[^)]*)?\)", text)
    require(len(links) >= 8, "Expected profile and editorial routing links")
    for link in links:
        require((base / link).is_file(), f"Missing routing target: {link}")
    require(len(list((base / "references/profiles").glob("*.md"))) == 5, "Expected five profiles")
    for folder in ("eyd", "seri-penyuluhan", "highlights"):
        require(any((base / "references" / folder).glob("*.md")), f"Missing references: {folder}")
    require((base / "references/eyd/eyd-edisi-v-2022.md").is_file(), "Missing primary EYD source")
    interface = yaml.safe_load((base / "agents/openai.yaml").read_text())["interface"]
    require(25 <= len(interface["short_description"]) <= 64, "Invalid UI blurb length")
    require("$" + data["name"] in interface["default_prompt"], "Default prompt must mention skill")


def main():
    check_package(ROOT)
    check_package(DEST)
    require(not differences(), "Plugin copy has drifted; run scripts/sync_distribution.py")
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"][0]
    require(plugin["name"] == market["name"] == "indonesia-eyd-writing-skill", "Plugin name mismatch")
    require(plugin["version"] == market["version"], "Plugin version mismatch")
    require(market["source"] == "./", "Unexpected plugin source")
    cases = json.loads((ROOT / "evals/cases.json").read_text())
    require(len(cases) >= 8, "Expected behavioral coverage")
    require(len({c["id"] for c in cases}) == len(cases), "Duplicate case IDs")
    for case in cases:
        require(case["prompt"] and case["criteria"], f"Incomplete case: {case['id']}")
    print(f"PASS: two packages, five profiles, matching distribution, manifests, {len(cases)} evaluation cases.")


if __name__ == "__main__":
    main()
