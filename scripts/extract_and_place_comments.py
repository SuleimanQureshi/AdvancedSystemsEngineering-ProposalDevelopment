"""Extract the 40 inline comments from the source .docx and insert them
as MkDocs Material admonitions next to the text they annotate.

For each comment we read the anchored text from word/document.xml
(via the commentRangeStart/End markers), normalise it (strip bold/italic/
heading/list markdown), then search each deliverable .md file for the
same normalised string. We insert a `??? note "Sadaf · YYYY-MM-DD"`
admonition after the paragraph (or after the containing table, when the
anchor falls inside a `<table>`).

A report of placed vs orphaned comments is printed at the end. Re-running
the script is idempotent: it skips any anchor whose comment ID already
appears in the target file.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from pathlib import Path
from textwrap import indent

REPO = Path(__file__).resolve().parent.parent
DOCX = REPO / "source" / "Copy of ASEPD Deliverables.docx"
STAGES = REPO / "docs" / "stages"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


@dataclass
class Comment:
    cid: str
    author: str
    date: str          # YYYY-MM-DD
    body: str
    anchor: str        # plain-text anchor from the docx range


def parse_comments() -> list[Comment]:
    with zipfile.ZipFile(DOCX) as z:
        doc_xml = z.read("word/document.xml").decode("utf-8")
        com_xml = z.read("word/comments.xml").decode("utf-8")

    ctree = ET.fromstring(com_xml)
    meta: dict[str, dict] = {}
    for c in ctree.findall(f"{W}comment"):
        cid = c.get(f"{W}id")
        author = c.get(f"{W}author") or ""
        date = (c.get(f"{W}date") or "")[:10]
        texts = [t.text or "" for t in c.iter(f"{W}t")]
        meta[cid] = {
            "author": author,
            "date": date,
            "body": " ".join(texts).strip().replace("\xa0", " "),
        }

    dtree = ET.fromstring(doc_xml)
    body = dtree.find(f"{W}body")

    anchors: dict[str, str] = {cid: "" for cid in meta}
    open_cids: set[str] = set()

    def walk(el: ET.Element) -> None:
        if el.tag == f"{W}commentRangeStart":
            cid = el.get(f"{W}id")
            if cid is not None:
                open_cids.add(cid)
            return
        if el.tag == f"{W}commentRangeEnd":
            cid = el.get(f"{W}id")
            open_cids.discard(cid or "")
            return
        if el.tag == f"{W}t":
            text = (el.text or "").replace("\xa0", " ")
            for cid in open_cids:
                anchors[cid] += text
        for child in el:
            walk(child)

    walk(body)

    out: list[Comment] = []
    for cid, m in meta.items():
        out.append(Comment(
            cid=cid,
            author=m["author"],
            date=m["date"],
            body=m["body"],
            anchor=anchors[cid].strip(),
        ))
    # Sort by date for deterministic placement order
    out.sort(key=lambda c: (c.date, c.cid))
    return out


# Normalisation: remove markdown decoration so plain-text anchor strings match.
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_BOLD_UNDER_RE = re.compile(r"__([^_]+)__")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_ITALIC_UNDER_RE = re.compile(r"(?<!_)_([^_\n]+)_(?!_)")
_HEADING_RE = re.compile(r"^#{1,6}\s+")
_LIST_RE = re.compile(r"^\s*(?:\d+\.\s+|[-*+]\s+|>\s*)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_HTML_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def normalise_line(line: str) -> str:
    s = line
    s = _LINK_RE.sub(r"\1", s)
    s = _BOLD_RE.sub(r"\1", s)
    s = _BOLD_UNDER_RE.sub(r"\1", s)
    s = _ITALIC_RE.sub(r"\1", s)
    s = _ITALIC_UNDER_RE.sub(r"\1", s)
    s = _HEADING_RE.sub("", s)
    s = _LIST_RE.sub("", s)
    s = _HTML_TAG_RE.sub(" ", s)
    s = s.replace("\xa0", " ")
    s = _WS_RE.sub(" ", s).strip()
    # smart-quote normalisation
    s = (s.replace("‘", "'")
           .replace("’", "'")
           .replace("“", '"')
           .replace("”", '"')
           .replace("–", "-")
           .replace("—", "-"))
    return s


def normalise_anchor(anchor: str) -> str:
    s = anchor.replace("\xa0", " ")
    s = _WS_RE.sub(" ", s).strip()
    s = (s.replace("‘", "'")
           .replace("’", "'")
           .replace("“", '"')
           .replace("”", '"')
           .replace("–", "-")
           .replace("—", "-"))
    return s


def find_anchor_line(file_lines: list[str], anchor: str) -> int | None:
    """Return the 0-indexed line number where the anchor occurs, or None."""
    norm_anchor = normalise_anchor(anchor)
    if not norm_anchor:
        return None
    # Try line-by-line first (fast, common case).
    for idx, line in enumerate(file_lines):
        if norm_anchor in normalise_line(line):
            return idx
    # Try across joined lines for anchors that span paragraph boundaries.
    normalised = [normalise_line(line) for line in file_lines]
    joined = " ".join(normalised)
    offsets = []
    pos = 0
    for n in normalised:
        offsets.append(pos)
        pos += len(n) + 1
    hit = joined.find(norm_anchor)
    if hit < 0:
        # Try with parenthetical content stripped (handles "Title (Del. 1)" → "Title").
        no_paren = re.sub(r"\s*\([^)]*\)\s*", " ", norm_anchor).strip()
        no_paren = _WS_RE.sub(" ", no_paren)
        if no_paren and no_paren != norm_anchor:
            hit = joined.find(no_paren)
    if hit < 0:
        # Try with all hyphens treated as optional (handles "Low -level" vs "Low-level").
        flex = re.escape(norm_anchor).replace(r"\ ", r"\s*").replace(r"\-", r"\s*-?\s*")
        m = re.search(flex, joined)
        if m:
            hit = m.start()
    if hit < 0:
        # Last resort: try the first 6 words of the anchor.
        prefix = " ".join(norm_anchor.split()[:6])
        if not prefix or len(prefix) < 15:
            return None
        hit = joined.find(prefix)
        if hit < 0:
            return None
    for idx, off in enumerate(offsets):
        if off > hit:
            return max(0, idx - 1)
    return len(file_lines) - 1


def paragraph_end(file_lines: list[str], start_idx: int) -> int:
    """Return the index of the LAST line of the paragraph that contains start_idx.

    Walks forward until a blank line. If start_idx falls inside an HTML
    table block (line begins with `<table` somewhere above with no
    `</table>` between), walks to the `</table>` close instead.
    """
    # Detect table context
    in_table = False
    for j in range(start_idx, -1, -1):
        line = file_lines[j].strip()
        if line.startswith("</table>"):
            break
        if line.startswith("<table"):
            in_table = True
            break
    if in_table:
        for j in range(start_idx, len(file_lines)):
            if "</table>" in file_lines[j]:
                return j
        return len(file_lines) - 1

    # Plain paragraph: walk forward until blank line
    j = start_idx
    while j + 1 < len(file_lines) and file_lines[j + 1].strip() != "":
        j += 1
    return j


def render_admonition(c: Comment) -> str:
    # CLAUDE.md convention: first-name label
    first_name = c.author.split()[0] if c.author else "Reviewer"
    label = f"{first_name} · {c.date}"
    body = c.body.replace("\xa0", " ").strip()
    indented = indent(body, "    ")
    return f"\n??? note \"{label}\"\n{indented}\n"


# "(Del. N)" hint: when an anchor mentions a specific deliverable number,
# prefer files whose name starts with d<N>- and whose stage matches the
# rough position of the anchor in the source doc.
_DEL_HINT_RE = re.compile(r"\(Del\.\s*(\d+)\)", re.IGNORECASE)


def deliverable_hint(anchor: str) -> int | None:
    m = _DEL_HINT_RE.search(anchor)
    return int(m.group(1)) if m else None


def already_placed(file_text: str, cid: str) -> bool:
    return f"<!-- comment:{cid} -->" in file_text


def place_comments() -> None:
    comments = parse_comments()
    target_files = sorted(STAGES.rglob("d*.md"))

    placed: list[tuple[Comment, Path]] = []
    orphans: list[Comment] = []

    # Build a per-file working copy as list of lines, plus a list of (insertion_idx, text)
    file_lines_map: dict[Path, list[str]] = {
        p: p.read_text().splitlines() for p in target_files
    }
    file_inserts: dict[Path, list[tuple[int, str, str]]] = {p: [] for p in target_files}

    for c in comments:
        # Idempotency: if this comment ID is already present anywhere, skip.
        if any(already_placed("\n".join(file_lines_map[p]), c.cid) for p in target_files):
            placed.append((c, next(p for p in target_files
                                   if already_placed("\n".join(file_lines_map[p]), c.cid))))
            continue

        # Reorder target files so hinted deliverables are tried first.
        ordered = list(target_files)
        hint_num = deliverable_hint(c.anchor)
        if hint_num is not None:
            stem_prefix = f"d{hint_num}-"
            ordered.sort(key=lambda p: (0 if p.name.startswith(stem_prefix) else 1, p.name))

        located: tuple[Path, int] | None = None
        for path in ordered:
            idx = find_anchor_line(file_lines_map[path], c.anchor)
            if idx is not None:
                located = (path, idx)
                break

        if located is None:
            orphans.append(c)
            continue
        path, idx = located

        end_idx = paragraph_end(file_lines_map[path], idx)
        admonition = render_admonition(c) + f"<!-- comment:{c.cid} -->\n"
        file_inserts[path].append((end_idx, admonition, c.cid))
        placed.append((c, path))

    # Apply inserts in reverse order per file (so earlier indices stay valid)
    for path, inserts in file_inserts.items():
        if not inserts:
            continue
        inserts.sort(key=lambda t: t[0], reverse=True)
        lines = file_lines_map[path]
        for end_idx, admonition, _cid in inserts:
            insertion_lines = admonition.split("\n")
            lines[end_idx + 1:end_idx + 1] = insertion_lines
        path.write_text("\n".join(lines) + "\n")

    # Report
    print(f"Placed: {len(placed)} / {len(comments)} comments")
    print(f"Orphans: {len(orphans)}")
    if orphans:
        print("\nOrphaned (anchor text not found):")
        for c in orphans:
            print(f"  id={c.cid} date={c.date}")
            print(f"    anchor: {c.anchor[:120]!r}")
            print(f"    body:   {c.body[:120]!r}")
    # Where comments landed
    from collections import Counter
    counts = Counter(p.name for _, p in placed)
    print("\nPlacements per file:")
    for fname, n in sorted(counts.items()):
        print(f"  {n:2d}  {fname}")


if __name__ == "__main__":
    place_comments()
