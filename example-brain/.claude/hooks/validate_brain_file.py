#!/usr/bin/env python3
"""
PostToolUse hook — validates a just-written brain file before the agent claims success.

Runs after Write/Edit. Reads the Claude Code PostToolUse JSON payload from stdin.
Only validates files under hypotheses/ or decisions/ (where orphan-evidence and broken
provenance links cause the most damage). Other writes pass through silently.

Two severity tiers — both matter, but blocking only the truly in-turn-fixable ones
avoids penalizing legitimate ordering (hypothesis written before its matching source
file lands, or mutually-referencing files A↔B that can't both be created in one write).

  BLOCKING (exit 2):
    - Evidence row with ZERO provenance attempt — no enum tag AND no
      [ingestion/...] / [source/...] link of any kind. Fixing this requires
      nothing external: add (intuition, PM, <date>) or a link. Always doable in-turn.

  WARNING (exit 0 + stderr):
    - Path-typed provenance link whose target doesn't resolve (yet).
    - Any other broken internal markdown link.
    These usually mean an out-of-order write or a forward reference. The agent sees
    the message and can fix when the dependency appears. They're caught hard by the
    structural audit at end-of-scenario, so nothing slips through silently.

Standalone — no imports from tests/harness/. Mirrors the logic of
tests/harness/checks/structural.py at scaffold-creation time.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


# ----- provenance enum -----

_PROVENANCE_NON_PATH_RES = (
    re.compile(r"\(stakeholder-verbal,\s*[^,]+,\s*\d{4}-\d{2}-\d{2}\)", re.IGNORECASE),
    re.compile(r"\(intuition,\s*[^,]+,\s*\d{4}-\d{2}-\d{2}\)", re.IGNORECASE),
    re.compile(r"\(industry-knowledge\)", re.IGNORECASE),
    re.compile(r"\(chat,\s*no artifact\)", re.IGNORECASE),
)

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
_ROW_RE = re.compile(r"^\s*[-*]\s+(.*)$")

_BARE_PLACEHOLDER_RE = re.compile(
    r"^\s*[*_`]*\s*"
    r"\(?\s*(none(\s+yet)?|n/?a|tbd|todo|"
    r"nothing\s+yet|no\s+evidence(\s+yet)?|"
    r"not\s+yet|pending|open|[—–-])\s*\)?"
    r"\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)

_PAREN_ABSENCE_RE = re.compile(
    r"^\s*[*_`]*\s*\(\s*(none|nothing|no\s+evidence|n/?a|tbd|not\s+yet|nothing\s+yet)\b"
    r"[^)]*\)\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)

_BOLD_EVIDENCE_LABEL_RE = re.compile(
    r"^\s*[-*]\s+\*\*Evidence\s+(for|against)\s*:\*\*\s*$", re.IGNORECASE
)

_FENCED_CODE_RE = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.DOTALL | re.MULTILINE)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def _strip_code_spans(text: str) -> str:
    text = _FENCED_CODE_RE.sub("", text)
    text = _INLINE_CODE_RE.sub("", text)
    return text


def _is_empty_evidence_placeholder(row: str) -> bool:
    stripped = row.strip()
    return bool(_BARE_PLACEHOLDER_RE.match(stripped) or _PAREN_ABSENCE_RE.match(stripped))


def _classify_provenance(row_text: str, file_parent: Path, work_dir: Path) -> tuple[str, str]:
    """
    Returns (verdict, reason). Verdict:
      "ok"      — has a valid enum tag or a resolvable path-typed link
      "warn"    — has a path-typed link attempt, but target doesn't resolve yet
                  (likely an ordering issue — flag, don't block)
      "orphan"  — no provenance attempt at all (must add an enum tag or a link;
                  always fixable in-turn, so this is blocking)
    """
    for rx in _PROVENANCE_NON_PATH_RES:
        if rx.search(row_text):
            return "ok", ""
    has_attempt = False
    warn_reason = ""
    for lm in LINK_RE.finditer(row_text):
        target = lm.group(2).split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if "ingestion/" in target or "source/" in target:
            has_attempt = True
            resolved = (file_parent / target).resolve()
            if not resolved.exists():
                warn_reason = f"path-typed tag doesn't resolve yet: {target}"
                continue
            try:
                rel = resolved.relative_to(work_dir.resolve())
            except ValueError:
                warn_reason = f"path-typed tag outside work_dir: {target}"
                continue
            parts = rel.parts
            if not parts or parts[0] not in {"source", "ingestion"}:
                warn_reason = f"path-typed tag not under source/ or ingestion/: {target}"
                continue
            return "ok", ""
    if has_attempt:
        return "warn", warn_reason
    return "orphan", "no provenance tag (must be path-typed or match enum)"


def _iter_evidence_rows(text: str):
    in_evidence = False
    depth = 0
    for line in text.splitlines():
        hm = re.match(r"^(#{1,6})\s+(.*)$", line)
        if hm:
            d = len(hm.group(1))
            header = hm.group(2).lower()
            if "evidence" in header:
                in_evidence = True
                depth = d
            elif in_evidence and d <= depth:
                in_evidence = False
            continue
        if not in_evidence:
            continue
        rm = _ROW_RE.match(line)
        if not rm:
            continue
        row = rm.group(1).strip()
        if not row:
            continue
        if row.startswith("<") and "<provenance-tag>" in row:
            continue
        if re.match(r"^\*\*[^*]+:\*\*\s*$", row):
            continue
        if _is_empty_evidence_placeholder(row):
            continue
        yield row


def _iter_bold_evidence_rows(text: str):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if _BOLD_EVIDENCE_LABEL_RE.match(lines[i]):
            i += 1
            while i < len(lines):
                line = lines[i]
                if re.match(r"^\s*$", line):
                    i += 1
                    continue
                if re.match(r"^#{1,6}\s+", line):
                    break
                sub = re.match(r"^\s+[-*]\s+(.*)$", line)
                if sub:
                    row = sub.group(1).strip()
                    if (not (row.startswith("<") and "<provenance-tag>" in row)
                            and not _is_empty_evidence_placeholder(row)):
                        yield row
                    i += 1
                    continue
                break
            continue
        i += 1


# ----- work_dir discovery -----

# Markers that strongly suggest "this is a PM brain root".
_BRAIN_ROOT_MARKERS = ("INDEX.md", "CLAUDE.md")
_BRAIN_ROOT_DIRS = ("hypotheses", "decisions", "knowledge", "ingestion", "source", "stakeholders")


def _find_work_dir(file_path: Path) -> Path | None:
    cur = file_path.parent.resolve()
    while True:
        has_marker = any((cur / m).is_file() for m in _BRAIN_ROOT_MARKERS)
        sub_count = sum(1 for d in _BRAIN_ROOT_DIRS if (cur / d).is_dir())
        if has_marker and sub_count >= 2:
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent


# ----- main -----

def _read_payload() -> dict:
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def _extract_file_paths(payload: dict) -> list[Path]:
    out: list[Path] = []
    tool_input = payload.get("tool_input") or {}
    for key in ("file_path", "filePath", "path"):
        v = tool_input.get(key)
        if isinstance(v, str) and v:
            out.append(Path(v))
    edits = tool_input.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict):
                fp = e.get("file_path") or e.get("filePath")
                if isinstance(fp, str) and fp:
                    out.append(Path(fp))
    # de-dupe preserving order
    seen = set()
    result: list[Path] = []
    for p in out:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            result.append(p)
    return result


def _is_brain_file(rel: Path) -> bool:
    """A file is brain-significant for the evidence audit if it lives under hypotheses/
    or decisions/ (excluding the schema/index templates themselves)."""
    parts = rel.parts
    if not parts:
        return False
    if parts[0] not in {"hypotheses", "decisions"}:
        return False
    if rel.name in {"_SCHEMA.md", "INDEX.md"}:
        return False
    return rel.suffix == ".md"


def _validate_evidence(file_path: Path, work_dir: Path) -> tuple[list[str], list[str]]:
    """Returns (orphans, warnings) — orphans block, warnings don't."""
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError as e:
        return ([f"  - read failed: {e}"], [])
    rows = list(_iter_evidence_rows(text)) + list(_iter_bold_evidence_rows(text))
    orphans: list[str] = []
    warns: list[str] = []
    for row in rows:
        verdict, reason = _classify_provenance(row, file_path.parent, work_dir)
        snippet = row[:90] + ("…" if len(row) > 90 else "")
        if verdict == "orphan":
            orphans.append(f"  - {reason} :: {snippet}")
        elif verdict == "warn":
            warns.append(f"  - {reason} :: {snippet}")
    return (orphans, warns)


def _validate_links(file_path: Path) -> list[str]:
    if file_path.name == "_SCHEMA.md":
        return []
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError:
        return []
    text = _strip_code_spans(text)
    broken = []
    for m in LINK_RE.finditer(text):
        target = m.group(2).split("#", 1)[0].strip()
        if not target:
            continue
        if target.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if "{{" in target or ("<" in target and ">" in target):
            continue
        resolved = (file_path.parent / target).resolve()
        if not resolved.exists():
            broken.append(f"  - {target}")
    return broken


def main() -> int:
    payload = _read_payload()
    file_paths = _extract_file_paths(payload)
    if not file_paths:
        return 0

    blocking: list[str] = []
    warnings: list[str] = []

    for fp in file_paths:
        if not fp.is_absolute():
            fp = fp.resolve()
        if not fp.exists() or fp.suffix != ".md":
            continue
        work_dir = _find_work_dir(fp)
        if work_dir is None:
            continue
        try:
            rel = fp.resolve().relative_to(work_dir.resolve())
        except ValueError:
            continue

        link_problems = _validate_links(fp)
        if link_problems:
            warnings.append(
                f"{rel.as_posix()} — internal links don't resolve yet "
                "(may be an ordering issue — fix when target is written):"
            )
            warnings.extend(link_problems)

        if _is_brain_file(rel):
            orphans, warns = _validate_evidence(fp, work_dir)
            if orphans:
                blocking.append(
                    f"{rel.as_posix()} — evidence rows with NO provenance attempt "
                    "(must add an enum tag or a path-typed link):"
                )
                blocking.extend(orphans)
            if warns:
                warnings.append(
                    f"{rel.as_posix()} — provenance links don't resolve yet "
                    "(probably written before the source/ingestion file — fix when it lands):"
                )
                warnings.extend(warns)

    # Warnings always print (informational), but don't block.
    if warnings:
        print(
            "[pm-brain hook] warnings — non-blocking, fix when dependencies land:\n\n"
            + "\n".join(warnings),
            file=sys.stderr,
        )

    if blocking:
        msg = (
            "[pm-brain hook] BLOCKING schema violations — fix in this turn before continuing:\n\n"
            + "\n".join(blocking)
            + "\n\nEvery Evidence-row needs one of these provenance tags:\n"
            "  - [ingestion/...](../ingestion/<kind>/<file>.md) or [source/...](../source/<kind>/<file>.md)\n"
            "  - (stakeholder-verbal, <name>, <YYYY-MM-DD>)\n"
            "  - (intuition, PM, <YYYY-MM-DD>)\n"
            "  - (industry-knowledge)\n"
            "  - (chat, no artifact)\n"
            "Empty-evidence placeholders like '(none yet)' or 'TBD' are exempt.\n"
            "Caveats and inferences belong under 'Open questions / caveats:', NOT under Evidence.\n"
            "If the path-typed file you want to link doesn't exist yet, either write it first "
            "or use an enum tag like (intuition, PM, <date>) and upgrade when the artifact lands."
        )
        print(msg, file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
