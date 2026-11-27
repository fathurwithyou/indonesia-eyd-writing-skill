#!/usr/bin/env python3
"""Inventaris dan perbandingan naskah UTF-8. Python 3.10+, pustaka standar."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re


MARKDOWN_HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$")
LATEX_HEADING = re.compile(
    r"\\(?:chapter|section|subsection|subsubsection)\*?(?:\[[^\]]*\])?\{([^{}]+)\}"
)
CITATION = re.compile(
    r"\\(?:textcite|parencite|autocite|footcite|citep|citet|cite|nocite)"
    r"\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}"
)
MARKDOWN_CITATION = re.compile(r"\[(?:[^\]\n]*?(?<!\w)@[\w:.-]+)[^\]\n]*\]")
URL = re.compile(r"https?://[^\s<>{}\[\]\\\"')]+")
NUMBER = re.compile(r"(?<![\w.,])[-−+]?\d+(?:[.,]\d+)*(?:[ \t]*\\?%)?(?![\w])")
PLACEHOLDER = re.compile(r"\[(?:TODO|TBD|ISI\b|PERLU\b)[^\]\n]*\]", re.IGNORECASE)
VERBATIM = re.compile(r"\\begin\{(verbatim\*?|lstlisting|minted)\}")


def latex_without_comment(line):
    """Remove the first percent sign preceded by an even number of backslashes."""
    slash_count = 0
    for index, char in enumerate(line):
        if char == "%" and slash_count % 2 == 0:
            return line[:index]
        slash_count = slash_count + 1 if char == "\\" else 0
    return line


def prose_lines(path):
    """Yield line numbers with common code and comment blocks excluded."""
    markdown = path.suffix.lower() in {".md", ".markdown"}
    latex = path.suffix.lower() in {".tex", ".latex"}
    fence = ""
    verbatim = ""
    for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if markdown:
            marker = re.match(r"^ {0,3}(\x60{3,}|~{3,})(.*)$", line)
            if fence:
                if marker and marker[1].startswith(fence) and not marker[2].strip():
                    fence = ""
                continue
            if marker:
                fence = marker[1]
                continue
            line = re.sub(r"(\x60+)(?!\x60).*?(?<!\x60)\1(?!\x60)", "", line)
        elif latex:
            if verbatim:
                if "\\end{" + verbatim + "}" in line:
                    verbatim = ""
                continue
            line = latex_without_comment(line)
            if match := VERBATIM.search(line):
                if "\\end{" + match[1] + "}" not in line[match.end():]:
                    verbatim = match[1]
                line = line[:match.start()]
        yield number, line


def inspect(path):
    found = {name: [] for name in ("judul", "angka", "sitasi", "tautan", "penanda")}
    latex = path.suffix.lower() in {".tex", ".latex"}

    def add(kind, value, line):
        found[kind].append({"teks": value, "baris": line})

    for number, line in prose_lines(path):
        heading = LATEX_HEADING.search(line) if latex else MARKDOWN_HEADING.match(line)
        if heading:
            add("judul", heading[1], number)
        for match in PLACEHOLDER.finditer(line):
            add("penanda", match[0], number)
        for match in URL.finditer(line):
            add("tautan", match[0].rstrip(".,;:!?"), number)
        line = URL.sub("", line)
        if latex:
            for match in CITATION.finditer(line):
                for key in match[1].split(","):
                    if key.strip():
                        add("sitasi", key.strip(), number)
            line = CITATION.sub("", line)
            line = re.sub(r"\\(?:label|ref|eqref|pageref|cref|Cref)\{[^{}]*\}", "", line)
        else:
            for match in MARKDOWN_CITATION.finditer(line):
                for key in re.findall(r"(?<!\w)@([\w:.-]+)", match[0]):
                    add("sitasi", key.rstrip("."), number)
            line = MARKDOWN_CITATION.sub("", line)
            line = re.sub(r"\]\([^)]+\)", "]", line)
            line = re.sub(r"^ {0,3}\d+[.)]\s+", "", line)
        for match in NUMBER.finditer(line):
            value = re.sub(r"[ \t\\]", "", match[0]).replace("−", "-")
            add("angka", value, number)
    return found


def compare(before, after):
    changes = {}
    for kind in before:
        old = Counter(item["teks"] for item in before[kind])
        new = Counter(item["teks"] for item in after[kind])
        removed = old - new
        added = new - old
        if removed or added:
            changes[kind] = {
                "berkurang": dict(sorted(removed.items())),
                "bertambah": dict(sorted(added.items())),
            }
    return changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inventory = commands.add_parser("inspect", help="Temukan judul, angka, sitasi, tautan, dan penanda.")
    inventory.add_argument("file", type=Path)
    difference = commands.add_parser("compare", help="Bandingkan inventaris dua versi naskah.")
    difference.add_argument("before", type=Path)
    difference.add_argument("after", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            result = {"berkas": str(args.file), "inventaris": inspect(args.file)}
        else:
            result = {
                "sebelum": str(args.before),
                "sesudah": str(args.after),
                "perubahan": compare(inspect(args.before), inspect(args.after)),
            }
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
