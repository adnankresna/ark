"""
structural.py — deterministic assertion helpers used by run_scenario.py.

Each helper takes (work_dir, arg, snapshots=None) and returns
    {"name": str, "passed": bool, "detail": str}.

snapshots is {"before": {relpath: mtime, ...}, "after": {relpath: mtime, ...}} for
per-turn assertions. Final-state assertions pass snapshots=None.

Conventions:
  - All paths in expected.yaml are RELATIVE to work_dir.
  - Glob patterns use Path.glob semantics (** for recursive).
  - Returns always carry all three keys, even on failure.
"""

from pathlib import Path
import re


# ============================================================
# File presence + modification
# ============================================================

def file_exists(work_dir: Path, path: str, snapshots=None) -> dict:
    p = work_dir / path
    return _result(f"file_exists:{path}", p.is_file(), "" if p.is_file() else f"not found: {p}")


def file_exists_glob(work_dir: Path, pattern: str, snapshots=None) -> dict:
    """
    Supports comma- or ' OR '-separated alternatives. Passes if ANY alternative matches.
    expected.yaml uses both forms (e.g. 'ingestion/adhoc/*churn*.md OR ingestion/market/*churn*.md').
    """
    alternatives = _split_alternatives(pattern)
    found = []
    for alt in alternatives:
        for match in work_dir.glob(alt):
            if match.is_file():
                found.append(str(match.relative_to(work_dir)).replace("\\", "/"))
    passed = len(found) > 0
    return _result(
        f"file_exists_glob:{pattern}",
        passed,
        "" if passed else f"no matches for any of: {alternatives}",
        extra=f"matched: {found[:5]}" if found else "",
    )


def file_modified(work_dir: Path, path: str, snapshots=None) -> dict:
    """
    File exists AND its mtime changed since the before-snapshot (or it didn't exist before).
    Used for per-turn assertions like 'knowledge/product/metrics.md was updated this turn'.

    If 'path' contains ' OR ', any alternative satisfies the assertion.
    """
    alternatives = _split_alternatives(path)
    for alt in alternatives:
        p = work_dir / alt
        if not p.is_file():
            continue
        if snapshots is None:
            return _result(f"file_modified:{path}", True, f"matched: {alt} (no snapshot; presence only)")
        rel = alt.replace("\\", "/")
        before = (snapshots.get("before") or {}).get(rel)
        after = (snapshots.get("after") or {}).get(rel)
        if after is None:
            continue
        if before is None or after > before + 1e-6:
            return _result(f"file_modified:{path}", True, f"modified: {alt}")
    return _result(
        f"file_modified:{path}",
        False,
        f"no alternative was modified this turn: {alternatives}",
    )


def file_modified_or_created(work_dir: Path, path: str, snapshots=None) -> dict:
    """Pass if file exists now AND (was modified OR didn't exist in before-snapshot)."""
    return file_modified(work_dir, path, snapshots=snapshots) \
        if snapshots is not None \
        else file_exists(work_dir, path)


def file_contains_any(work_dir: Path, arg: str, snapshots=None) -> dict:
    """
    Check that at least one of the resolved files contains at least one of the substrings.

    YAML form:
        file_contains_any: <path_or_glob_alternatives> ; <substr1> OR <substr2> OR ...

    Examples:
        file_contains_any: knowledge/strategy.md ; telemetron OR north-star
        file_contains_any: CLAUDE.md ; act and tell
        file_contains_any: knowledge/org/tools.md OR rules/data.md ; posthog OR linear OR intercom

    Path alternatives use the same ' OR ' / ',' splitter as file_exists_glob.
    Substring matching is case-insensitive. A single ';' separates the two halves.
    """
    if not arg or ";" not in arg:
        return _result(
            f"file_contains_any:{arg}",
            False,
            "malformed: expected '<path_or_glob> ; <substr1> OR <substr2> ...'",
        )
    path_part, _, substr_part = arg.partition(";")
    path_alternatives = _split_alternatives(path_part.strip())
    substr_alternatives = [s.strip().lower() for s in re.split(r"\s+OR\s+", substr_part.strip()) if s.strip()]
    if not substr_alternatives:
        return _result(f"file_contains_any:{arg}", False, "no substrings to match")

    matched_files: list[str] = []
    for alt in path_alternatives:
        for match in work_dir.glob(alt):
            if not match.is_file():
                continue
            try:
                body = match.read_text(encoding="utf-8", errors="replace").lower()
            except OSError:
                continue
            if any(s in body for s in substr_alternatives):
                matched_files.append(str(match.relative_to(work_dir)).replace("\\", "/"))

    passed = len(matched_files) > 0
    return _result(
        f"file_contains_any:{arg}",
        passed,
        "" if passed else (
            f"no file in {path_alternatives} contained any of {substr_alternatives}"
        ),
        extra=f"matched: {matched_files[:3]}" if matched_files else "",
    )


def file_modified_glob(work_dir: Path, pattern: str, snapshots=None) -> dict:
    """Any file matching the glob was modified or created this turn."""
    alternatives = _split_alternatives(pattern)
    if snapshots is None:
        return file_exists_glob(work_dir, pattern)
    before = snapshots.get("before") or {}
    after = snapshots.get("after") or {}
    hits = []
    for alt in alternatives:
        for match in work_dir.glob(alt):
            if not match.is_file():
                continue
            rel = str(match.relative_to(work_dir)).replace("\\", "/")
            b = before.get(rel)
            a = after.get(rel)
            if a is None:
                continue
            if b is None or a > b + 1e-6:
                hits.append(rel)
    return _result(
        f"file_modified_glob:{pattern}",
        len(hits) > 0,
        "" if hits else f"no files matched and modified for: {alternatives}",
        extra=f"changed: {hits[:5]}" if hits else "",
    )


# ============================================================
# Hypothesis lifecycle
# ============================================================

HYPOTHESIS_EXCLUDED = {"INDEX.md", "_SCHEMA.md"}


def _list_hypothesis_files(work_dir: Path) -> list[Path]:
    h_dir = work_dir / "hypotheses"
    if not h_dir.is_dir():
        return []
    return [p for p in h_dir.glob("*.md")
            if p.name not in HYPOTHESIS_EXCLUDED and not p.name.startswith(".")]


def hypothesis_count_at_least(work_dir: Path, n, snapshots=None) -> dict:
    n = int(n)
    files = _list_hypothesis_files(work_dir)
    real = [f for f in files if _hypothesis_has_content(f)]
    return _result(
        f"hypothesis_count_at_least:{n}",
        len(real) >= n,
        f"found {len(real)} non-stub hypothesis files (total .md = {len(files)})",
    )


def _hypothesis_has_content(p: Path) -> bool:
    """A hypothesis file is real if it has more than ~100 chars of body beyond the schema scaffolding."""
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return False
    # Strip front-matter & whitespace-only lines; require some substantive line count.
    stripped = "\n".join(l for l in text.splitlines() if l.strip() and not l.strip().startswith("<!--"))
    return len(stripped) > 200


EVIDENCE_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<target>[^)]+)\)")


_BOLD_LABEL_RE = re.compile(r"^\s*[-*+]?\s*\*\*([^*]+):\*\*")


def _count_evidence_links(p: Path) -> int:
    """
    Count outbound links inside the "Evidence for" region of a hypothesis file.

    Supports two shapes:
      (a) Markdown header form:  `## Evidence for` / `### Evidence` (depth-scoped)
      (b) Bold-label list form:  `- **Evidence for:**` followed by bullet rows
          (this is the canonical scaffold shape — see hypotheses/_SCHEMA.md)

    The "Evidence against" / "Evidence against (demand side)" sections are excluded.
    A bold-label region ends at the next bold label or the next markdown header.
    """
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return 0
    count = 0
    in_evidence_header = False
    header_depth = 0
    in_evidence_label = False
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            depth = len(m.group(1))
            header_text = m.group(2).lower()
            in_evidence_label = False  # header ends any bold-label region
            if "evidence" in header_text and "against" not in header_text:
                in_evidence_header = True
                header_depth = depth
            elif in_evidence_header and depth <= header_depth:
                in_evidence_header = False
            continue
        lm = _BOLD_LABEL_RE.match(line)
        if lm:
            label = lm.group(1).strip().lower()
            in_evidence_label = ("evidence for" in label) or label == "evidence"
            count += len(EVIDENCE_LINK_RE.findall(line))
            continue
        if in_evidence_header or in_evidence_label:
            count += len(EVIDENCE_LINK_RE.findall(line))
    return count


def _resolve_hypothesis(work_dir: Path, hypothesis_id: str, snapshots=None) -> Path | None:
    """
    Resolve a scenario-level id like 'H2' to a specific hypothesis file.

    Strategy:
      1. If a file's frontmatter/body contains the literal id (e.g. 'id: H2' or '# H2 —'), use it.
      2. Otherwise, fall back to ordering by file creation order using the before-snapshot.
         H1 = oldest hypothesis file, H2 = next, etc. (1-indexed.)
    """
    files = _list_hypothesis_files(work_dir)
    if not files:
        return None
    # Direct id match
    for f in files:
        try:
            head = f.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        if re.search(rf"\b{re.escape(hypothesis_id)}\b", head):
            return f
    # Ordering fallback
    m = re.match(r"^[Hh](\d+)$", hypothesis_id.strip())
    if not m:
        return files[0] if files else None
    idx = int(m.group(1)) - 1
    # Order by mtime ascending (oldest = earliest created)
    ordered = sorted(files, key=lambda p: p.stat().st_mtime)
    if 0 <= idx < len(ordered):
        return ordered[idx]
    return None


def hypothesis_evidence_count_increased_for(work_dir: Path, hypothesis_id: str, snapshots=None) -> dict:
    """At least one new evidence link was added to <hypothesis_id> this turn."""
    if snapshots is None:
        return _result(
            f"hypothesis_evidence_count_increased_for:{hypothesis_id}",
            False, "snapshots required for diff-based assertion",
        )
    after_file = _resolve_hypothesis(work_dir, hypothesis_id, snapshots=snapshots)
    if after_file is None:
        return _result(
            f"hypothesis_evidence_count_increased_for:{hypothesis_id}",
            False, "no hypothesis files found",
        )
    after_count = _count_evidence_links(after_file)
    # Get before-count: re-read from before-snapshot is impossible (files mutated in-place),
    # so we approximate by checking whether the file existed at all before AND grew in size.
    rel = str(after_file.relative_to(work_dir)).replace("\\", "/")
    before_mtime = (snapshots.get("before") or {}).get(rel)
    if before_mtime is None:
        # File is new this turn; any evidence row counts as an increase from 0.
        return _result(
            f"hypothesis_evidence_count_increased_for:{hypothesis_id}",
            after_count >= 1,
            f"new hypothesis file {rel}, evidence links = {after_count}",
        )
    after_mtime = (snapshots.get("after") or {}).get(rel)
    file_changed = after_mtime is not None and after_mtime > before_mtime + 1e-6
    return _result(
        f"hypothesis_evidence_count_increased_for:{hypothesis_id}",
        file_changed and after_count >= 1,
        f"file changed={file_changed}, evidence links now={after_count} ({rel})",
    )


def hypothesis_evidence_count_unchanged_for(work_dir: Path, hypothesis_id: str, snapshots=None) -> dict:
    """No new evidence link was added to <hypothesis_id> this turn (low-signal rejection check)."""
    if snapshots is None:
        return _result(
            f"hypothesis_evidence_count_unchanged_for:{hypothesis_id}",
            False, "snapshots required for diff-based assertion",
        )
    after_file = _resolve_hypothesis(work_dir, hypothesis_id, snapshots=snapshots)
    if after_file is None:
        # Vacuous pass: nothing to add evidence to.
        return _result(
            f"hypothesis_evidence_count_unchanged_for:{hypothesis_id}",
            True, "no hypothesis files exist (vacuous pass)",
        )
    rel = str(after_file.relative_to(work_dir)).replace("\\", "/")
    before_mtime = (snapshots.get("before") or {}).get(rel)
    after_mtime = (snapshots.get("after") or {}).get(rel)
    # Pass if file existed before AND wasn't modified this turn.
    unchanged = (before_mtime is not None
                 and after_mtime is not None
                 and abs(after_mtime - before_mtime) < 1e-6)
    return _result(
        f"hypothesis_evidence_count_unchanged_for:{hypothesis_id}",
        unchanged,
        f"file {rel} mtime before={before_mtime} after={after_mtime}",
    )


# ============================================================
# Decisions
# ============================================================

def all_decisions_have_reversal_condition(work_dir: Path, _=None, snapshots=None) -> dict:
    d_dir = work_dir / "decisions"
    if not d_dir.is_dir():
        return _result("all_decisions_have_reversal_condition", True, "decisions/ dir absent (vacuous pass)")
    decision_files = [p for p in d_dir.glob("*.md")
                      if p.name not in {"INDEX.md", "_SCHEMA.md"}]
    if not decision_files:
        return _result("all_decisions_have_reversal_condition", True, "no decision files yet (vacuous pass)")
    missing = []
    for f in decision_files:
        text = f.read_text(encoding="utf-8").lower()
        if not _has_reversal_field(text):
            missing.append(f.name)
    return _result(
        "all_decisions_have_reversal_condition",
        len(missing) == 0,
        "" if not missing else f"missing in: {missing}",
    )


_REVERSAL_MARKERS = (
    "what would reverse",
    "reversal condition",
    "reverse this decision",
    "reverse if",
    "would reverse this",
)


def _has_reversal_field(text_lower: str) -> bool:
    return any(m in text_lower for m in _REVERSAL_MARKERS)


# ============================================================
# Link integrity
# ============================================================

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# Code spans / fenced blocks are LITERAL text in markdown — links inside them aren't
# clickable, so the validator must skip them. Without this, schema files that document
# the link form via examples (e.g. `[text](path)` or fenced ```markdown blocks showing
# illustrative paths) trip the validator on links that aren't real cross-links.
#
# Fenced-block regex must be line-anchored AND must distinguish openers (info string
# allowed) from closers (whitespace-only after the backticks). A naive `​```.*?​```` mispairs
# nested fences: a schema with an outer ```markdown wrapper and an inner ```markdown
# example block ends up with the regex pairing (outer-open, inner-open) and
# (inner-close, outer-close), leaving the inner example body visible to the link scanner.
_FENCED_CODE_RE = re.compile(
    r"^```[^\n]*\n.*?^```[ \t]*$",
    re.DOTALL | re.MULTILINE,
)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def _strip_code_spans(text: str) -> str:
    text = _FENCED_CODE_RE.sub("", text)
    text = _INLINE_CODE_RE.sub("", text)
    return text


def all_internal_links_valid(work_dir: Path, _=None, snapshots=None) -> dict:
    # _SCHEMA.md files document the link FORM via illustrative examples (e.g.
    # `[ingestion/...](../ingestion/foo.md)`). Those examples are template
    # documentation, not navigation, and their targets are never expected to
    # resolve in a real brain. Skip them entirely.
    broken = []
    for md_file in work_dir.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        if md_file.name == "_SCHEMA.md":
            continue
        try:
            text = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        text = _strip_code_spans(text)
        for m in LINK_RE.finditer(text):
            target = m.group(2).split("#", 1)[0].strip()
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            # Skip pure-anchor / image-relative things that look like templating placeholders.
            if "{{" in target or "<" in target and ">" in target:
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{md_file.relative_to(work_dir)} -> {target}")
    return _result(
        "all_internal_links_valid",
        len(broken) == 0,
        "" if not broken else f"broken ({len(broken)} total): {broken[:10]}",
    )


# Provenance vocabulary — must match exactly one of these.
# Path-typed: a markdown link whose target starts with ingestion/ or source/.
# Non-path-typed: the parenthetical forms below.
_PROVENANCE_NON_PATH_RES = (
    re.compile(r"\(stakeholder-verbal,\s*[^,]+,\s*\d{4}-\d{2}-\d{2}\)", re.IGNORECASE),
    re.compile(r"\(intuition,\s*[^,]+,\s*\d{4}-\d{2}-\d{2}\)", re.IGNORECASE),
    re.compile(r"\(industry-knowledge\)", re.IGNORECASE),
    re.compile(r"\(chat,\s*no artifact\)", re.IGNORECASE),
)

# Heuristic: an evidence row is a bullet that contains a textual claim.
# Skip placeholder rows (the schema template literal "<claim>  `<provenance-tag>`").
_ROW_RE = re.compile(r"^\s*[-*]\s+(.*)$")


# Empty-evidence placeholders: legitimate "we haven't gathered evidence yet" stances.
# These are NOT claims — they're admissions of absence — so they don't need provenance tags.
# Match the bare row content (after the bullet marker has been stripped).
#
# Three accepted shapes:
#   (a) Bare placeholder: "(none yet)", "TBD", "N/A", "nothing yet" — entire row is the marker.
#   (b) Parenthetical admission: "(None yet — no pricing model has been modeled.)" — the entire
#       row is a parenthetical aside that opens with an absence keyword. These are richer
#       admissions (explaining WHY there's nothing) and are also not claims.
#   (c) Bare separator: just "—" / "–" / "-" with nothing else. A common shape the agent
#       writes when the section legitimately has no evidence yet but it didn't reach for one
#       of the (a)/(b) words. Not a claim; not auditable as one.
_BARE_PLACEHOLDER_RE = re.compile(
    r"^\s*[*_`]*\s*"
    r"\(?\s*(none(\s+yet)?|n/?a|tbd|todo|"
    r"nothing\s+yet|no\s+evidence(\s+yet)?|"
    r"not\s+yet|pending|open|[—–-])\s*\)?"
    r"\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)

# A parenthetical row starting with an absence keyword.
# Allow leading italic/bold/code markers (*, _, `) since agents sometimes wrap the
# placeholder in italics like "*(none from current sources)*".
_PAREN_ABSENCE_RE = re.compile(
    r"^\s*[*_`]*\s*\(\s*(none|nothing|no\s+evidence|n/?a|tbd|not\s+yet|nothing\s+yet)\b"
    r"[^)]*\)\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)


def _is_empty_evidence_placeholder(row: str) -> bool:
    """True for rows whose entire payload is a placeholder like '(none yet)' or a
    parenthetical admission like '(None yet — no pricing model has been modeled.)'."""
    stripped = row.strip()
    return bool(_BARE_PLACEHOLDER_RE.match(stripped)
                or _PAREN_ABSENCE_RE.match(stripped))


def _row_has_provenance(row_text: str, file_parent: Path, work_dir: Path) -> tuple[bool, str]:
    """Return (has_tag, reason_if_not). Path-typed tags must resolve."""
    # Non-path enums first.
    for rx in _PROVENANCE_NON_PATH_RES:
        if rx.search(row_text):
            return True, ""
    # Path-typed: any markdown link whose target starts with ingestion/ or source/.
    for lm in LINK_RE.finditer(row_text):
        target = lm.group(2).split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        # Normalize the leading "../"s away and check the leaf segment.
        if "ingestion/" in target or "source/" in target:
            resolved = (file_parent / target).resolve()
            if not resolved.exists():
                return False, f"path-typed tag broken: {target}"
            try:
                rel = resolved.relative_to(work_dir.resolve())
            except ValueError:
                return False, f"path-typed tag outside work_dir: {target}"
            parts = rel.parts
            if not parts or parts[0] not in {"source", "ingestion"}:
                return False, f"path-typed tag not under source/ or ingestion/: {target}"
            return True, ""
    return False, "no provenance tag (must be path-typed or match enum)"


def _iter_evidence_rows(text: str):
    """Yield raw bullet lines that fall under an 'Evidence' header in a file."""
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
        # Also catch the "**Evidence for:** / **Evidence against:**" bold-label shape.
        rm = _ROW_RE.match(line)
        if not rm:
            continue
        row = rm.group(1).strip()
        if not row:
            continue
        # Skip the schema template literal rows.
        if row.startswith("<") and "<provenance-tag>" in row:
            continue
        # Skip bold-label markers like "**Evidence for:**" with no payload.
        if re.match(r"^\*\*[^*]+:\*\*\s*$", row):
            continue
        # Skip empty-evidence placeholders — these are legitimate "we have no evidence yet"
        # stances, not orphan claims.
        if _is_empty_evidence_placeholder(row):
            continue
        yield row


# Same idea but for evidence rows under bold-label fields like "**Evidence for:**".
_BOLD_EVIDENCE_LABEL_RE = re.compile(r"^\s*[-*]\s+\*\*Evidence\s+(for|against)\s*:\*\*\s*$", re.IGNORECASE)


def _iter_bold_evidence_rows(text: str):
    """Yield bullet rows that sit immediately under a '- **Evidence for:**' label."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if _BOLD_EVIDENCE_LABEL_RE.match(lines[i]):
            i += 1
            while i < len(lines):
                line = lines[i]
                # Stop at next top-level bullet or header or blank line followed by something else.
                if re.match(r"^\s*$", line):
                    i += 1
                    continue
                if re.match(r"^#{1,6}\s+", line):
                    break
                # Indented bullet = a sub-row of the bold label.
                sub = re.match(r"^\s+[-*]\s+(.*)$", line)
                if sub:
                    row = sub.group(1).strip()
                    if (not (row.startswith("<") and "<provenance-tag>" in row)
                            and not _is_empty_evidence_placeholder(row)):
                        yield row
                    i += 1
                    continue
                # Non-indented bullet — back out, end of section.
                break
            continue
        i += 1


def no_orphan_evidence(work_dir: Path, _=None, snapshots=None) -> dict:
    """
    Every evidence row in any hypothesis or decision file must carry a provenance tag from
    the canonical enum. Orphan = a claim with no audit anchor at all.

    Path-typed tags ([ingestion/...] / [source/...]) must resolve to a real file under
    source/ or ingestion/.

    Non-path tags must match the exact parenthetical forms:
      (stakeholder-verbal, <name>, <YYYY-MM-DD>)
      (intuition, <name>, <YYYY-MM-DD>)
      (industry-knowledge)
      (chat, no artifact)
    """
    orphans = []
    files = list(_list_hypothesis_files(work_dir))
    decisions_dir = work_dir / "decisions"
    if decisions_dir.is_dir():
        for p in decisions_dir.rglob("*.md"):
            if p.name in {"INDEX.md", "_SCHEMA.md"}:
                continue
            files.append(p)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        rows = list(_iter_evidence_rows(text)) + list(_iter_bold_evidence_rows(text))
        for row in rows:
            ok, reason = _row_has_provenance(row, f.parent, work_dir)
            if not ok:
                rel = f.relative_to(work_dir).as_posix()
                snippet = row[:80] + ("…" if len(row) > 80 else "")
                orphans.append(f"{rel}: {reason} :: {snippet}")
    return _result(
        "no_orphan_evidence",
        len(orphans) == 0,
        "" if not orphans else f"orphans ({len(orphans)}): {orphans[:8]}",
    )


def no_silent_hypothesis_demotion(work_dir: Path, _=None, snapshots=None) -> dict:
    """
    Structural proxy: any hypothesis whose status string suggests demotion (deprecated,
    demoted, killed, rejected, abandoned) must ALSO carry an evidence-against or
    contradictions section with at least one bullet/link.
    """
    offenders = []
    demote_re = re.compile(
        r"^\s*(?:status|state)\s*[:=]\s*[\"']?(deprecated|demoted|killed|rejected|abandoned|disproven)\b",
        re.IGNORECASE | re.MULTILINE,
    )
    against_section_re = re.compile(
        r"^#{1,6}\s+.*(evidence[- ]against|against|contradict|dissent|disconfirm).*$",
        re.IGNORECASE | re.MULTILINE,
    )
    for h_file in _list_hypothesis_files(work_dir):
        try:
            text = h_file.read_text(encoding="utf-8")
        except OSError:
            continue
        if not demote_re.search(text):
            continue
        if not against_section_re.search(text):
            offenders.append(h_file.name)
            continue
        # Has the section — verify it has at least one bullet/link, not just an empty header.
        m = against_section_re.search(text)
        tail = text[m.end():]
        # Cut at the next header of equal-or-higher level
        next_header = re.search(r"^#{1,6}\s+", tail, re.MULTILINE)
        body = tail[:next_header.start()] if next_header else tail
        if not (re.search(r"^\s*[-*+]\s+\S", body, re.MULTILINE) or LINK_RE.search(body)):
            offenders.append(f"{h_file.name} (empty against-section)")
    return _result(
        "no_silent_hypothesis_demotion",
        len(offenders) == 0,
        "" if not offenders else f"silently demoted: {offenders}",
    )


# ============================================================
# Helpers
# ============================================================

def _split_alternatives(pattern: str) -> list[str]:
    """
    Split on ' OR ' (case-insensitive) so expected.yaml entries like
        'ingestion/adhoc/*churn*.md OR ingestion/market/*churn*.md'
    expand to two glob alternatives.
    """
    parts = re.split(r"\s+OR\s+", pattern, flags=re.IGNORECASE)
    return [p.strip() for p in parts if p.strip()]


def _result(name: str, passed: bool, detail: str, extra: str = "") -> dict:
    full_detail = detail if not extra else f"{detail} | {extra}" if detail else extra
    return {"name": name, "passed": bool(passed), "detail": full_detail}


# ============================================================
# Dispatch
# ============================================================

DISPATCH = {
    "file_exists": file_exists,
    "file_exists_glob": file_exists_glob,
    "file_modified": file_modified,
    "file_modified_glob": file_modified_glob,
    "file_modified_or_created": file_modified_or_created,
    "file_contains_any": file_contains_any,
    "hypothesis_count_at_least": hypothesis_count_at_least,
    "hypothesis_evidence_count_increased_for": hypothesis_evidence_count_increased_for,
    "hypothesis_evidence_count_unchanged_for": hypothesis_evidence_count_unchanged_for,
    "all_decisions_have_reversal_condition": all_decisions_have_reversal_condition,
    "all_internal_links_valid": all_internal_links_valid,
    "no_orphan_evidence": no_orphan_evidence,
    "no_silent_hypothesis_demotion": no_silent_hypothesis_demotion,
}


def run_assertion(work_dir: Path, assertion, snapshots=None) -> dict:
    """
    Accepts:
      - "name: value"   (string form for single-arg assertions; YAML's typical inline shape)
      - {name: value}   (dict form, YAML mapping)
      - "name"          (no-arg assertions)
    """
    name, arg = _parse_assertion(assertion)
    fn = DISPATCH.get(name)
    if not fn:
        return {"name": name, "passed": False, "detail": "unknown assertion"}
    try:
        return fn(work_dir, arg, snapshots=snapshots)
    except TypeError:
        # Older signature without snapshots kw — call positionally.
        return fn(work_dir, arg)


def _parse_assertion(assertion) -> tuple[str, object]:
    if isinstance(assertion, str):
        if ":" in assertion:
            name, _, arg = assertion.partition(":")
            return name.strip(), arg.strip()
        return assertion.strip(), None
    if isinstance(assertion, dict):
        (name, arg), = assertion.items()
        return name, arg
    return str(assertion), None
