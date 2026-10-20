#!/usr/bin/env python3
"""Build or check the plugin copy from the root skill. Python 3.10+, stdlib only."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "skills" / "indonesia-eyd-writing-skill"
MANAGED = ("SKILL.md", "references", "agents")


def source_files():
    result = {}
    for name in MANAGED:
        path = ROOT / name
        if path.is_file():
            result[Path(name)] = path.read_bytes()
        else:
            if not path.is_dir():
                raise FileNotFoundError(path)
            for child in path.rglob("*"):
                if child.is_file():
                    result[child.relative_to(ROOT)] = child.read_bytes()
    return result


def differences():
    expected = source_files()
    actual = {
        p.relative_to(DEST): p.read_bytes()
        for name in MANAGED
        for p in ([DEST / name] if (DEST / name).is_file() else (DEST / name).rglob("*"))
        if p.is_file()
    }
    return sorted(str(p) for p in expected.keys() | actual.keys() if expected.get(p) != actual.get(p))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    args = parser.parse_args()
    source_files()  # Fail before changing the generated copy if any source is missing.
    if args.check:
        drift = differences()
        if drift:
            print("Distribution differs: " + ", ".join(drift))
            return 1
        print("Distribution matches source.")
        return 0
    DEST.mkdir(parents=True, exist_ok=True)
    for name in MANAGED:
        target = DEST / name
        if target.is_symlink() or target.is_file():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)
    print(f"Synced {len(source_files())} files to {DEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
