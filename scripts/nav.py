#!/usr/bin/env python3
"""Obsidian-style navigation for GitHub.

Run from the repo root:  python3 scripts/nav.py

It does two things, and only touches text between its own markers:
1. Any README.md that contains the index markers gets a list of every note
   in its folder and subfolders (the root README.md lists the whole repo).
2. Every other note gets a footer: a way back up (Home, folder) and the list
   of notes that link to it ("Linked from"), like Obsidian's backlinks.

Links are found in Markdown form [text](path.md) and in wikilink form
[[note]] or [[note|alias]], so notes written in Obsidian count too.
A GitHub Action runs this after every push (.github/workflows/nav.yml).
"""

import os
import re
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", ".obsidian", ".trash", "scripts", "node_modules"}

INDEX_START, INDEX_END = "<!-- nav:index -->", "<!-- /nav:index -->"
FOOT_START, FOOT_END = "<!-- nav:footer -->", "<!-- /nav:footer -->"

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+?\.md)(?:#[^)]*)?\)")
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FOOT_BLOCK = re.compile(r"\n*" + re.escape(FOOT_START) + r".*?" + re.escape(FOOT_END) + r"\n*", re.S)
INDEX_BLOCK = re.compile(re.escape(INDEX_START) + r".*?" + re.escape(INDEX_END), re.S)
CODE = re.compile(r"```.*?```|`[^`\n]+`", re.S)


def notes():
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(filenames):
            if name.endswith(".md"):
                found.append(Path(dirpath, name).relative_to(ROOT))
    return found


def title(path, text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def link(src, dst):
    rel = os.path.relpath(dst, src.parent)
    return quote(rel.replace(os.sep, "/"))


def body_only(text):
    """Note text without generated blocks and code, so links in them don't count."""
    text = FOOT_BLOCK.sub("\n", text)
    text = INDEX_BLOCK.sub("", text)
    return CODE.sub("", text)


def main():
    paths = notes()
    texts = {p: (ROOT / p).read_text(encoding="utf-8") for p in paths}
    titles = {p: title(p, t) for p, t in texts.items()}
    by_stem = {}
    for p in paths:
        by_stem.setdefault(p.stem.lower(), p)

    # Who links to whom.
    backlinks = {p: set() for p in paths}
    for src, text in texts.items():
        body = body_only(text)
        targets = set()
        for raw in MD_LINK.findall(body):
            if "://" in raw:
                continue
            dst = Path(os.path.normpath(src.parent / unquote(raw)))
            if dst in backlinks:
                targets.add(dst)
        for name in WIKI_LINK.findall(body):
            dst = by_stem.get(Path(name.strip()).stem.lower())
            if dst:
                targets.add(dst)
        for dst in targets - {src}:
            backlinks[dst].add(src)

    home = Path("README.md")
    changed = []
    for p in paths:
        text = texts[p]
        new = text

        if p.name == "README.md" and INDEX_START in text:
            folder = p.parent
            loose, groups = [], {}
            for q in paths:
                if q == p or folder not in q.parents:
                    continue
                parts = q.relative_to(folder).parts
                if len(parts) == 1:
                    loose.append(q)
                else:
                    groups.setdefault(parts[0], []).append(q)
            lines = [f"- [{titles[q]}]({link(p, q)})" for q in loose]
            for group in sorted(groups):
                readme = folder / group / "README.md"
                head = f"[{group}/]({link(p, readme)})" if readme in texts else f"{group}/"
                lines.append(f"\n**{head}**\n")
                items = [q for q in groups[group] if q != readme]
                lines += [f"- [{titles[q]}]({link(p, q)})" for q in items] or ["- _nothing yet_"]
            block = INDEX_START + "\n" + ("\n".join(lines).strip() or "_Nothing here yet._") + "\n" + INDEX_END
            new = INDEX_BLOCK.sub(lambda _: block, new)

        if p != home:
            crumbs = [f"↑ [Home]({link(p, home)})"]
            folder_readme = p.parent / "README.md"
            if p.name != "README.md" and folder_readme in texts and p.parent != Path("."):
                crumbs.append(f"[{p.parent.as_posix()}]({link(p, folder_readme)})")
            foot = [" · ".join(crumbs)]
            refs = sorted(backlinks[p], key=str)
            if refs:
                foot.append("Linked from: " + " · ".join(f"[{titles[r]}]({link(p, r)})" for r in refs))
            block = FOOT_START + "\n\n---\n\n" + "  \n".join(foot) + "\n\n" + FOOT_END + "\n"
            new = FOOT_BLOCK.sub("\n", new).rstrip("\n") + "\n\n" + block

        if new != text:
            (ROOT / p).write_text(new, encoding="utf-8")
            changed.append(str(p))

    print("updated:", ", ".join(changed) if changed else "nothing")


if __name__ == "__main__":
    main()
