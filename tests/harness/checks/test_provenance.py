"""
Unit tests for the provenance-vocabulary recognition inside no_orphan_evidence.

Run from tests/harness/:
    python -m checks.test_provenance

No LLM calls. Fixture markdown is synthesized in-memory.
"""
from pathlib import Path
import tempfile
import sys

from checks.structural import no_orphan_evidence


# ---- minimal fixture builder --------------------------------------------------

def _write(work_dir: Path, rel: str, body: str) -> Path:
    p = work_dir / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    return p


def _build_brain(tmp: Path, hypothesis_body: str, decision_body: str | None = None,
                 source_files: list[str] | None = None,
                 ingestion_files: list[str] | None = None) -> Path:
    """Create a minimal brain with one hypothesis + optional decision + linked source/ingestion."""
    (tmp / "hypotheses").mkdir(parents=True, exist_ok=True)
    _write(tmp, "hypotheses/feat.md", hypothesis_body)
    if decision_body is not None:
        _write(tmp, "decisions/2026-05-01-x.md", decision_body)
    for s in source_files or []:
        _write(tmp, s, "raw artifact body\n")
    for i in ingestion_files or []:
        _write(tmp, i, "ingestion synthesis body\n")
    return tmp


# ---- the fixtures -------------------------------------------------------------

# Each case: (name, hypothesis_body, decision_body, source_files, ingestion_files, expected_passed)

_GOOD_PATH_INGESTION = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - users reported X in interview  [ingestion/interviews/2026-04-01-acme.md](../ingestion/interviews/2026-04-01-acme.md)
"""

_GOOD_PATH_SOURCE = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - quote from raw transcript  [source/interviews/2026-04-01-acme.md](../source/interviews/2026-04-01-acme.md)
"""

_GOOD_STAKEHOLDER_VERBAL = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - Naomi said in 1:1 she wants X  (stakeholder-verbal, Naomi, 2026-05-13)
"""

_GOOD_INTUITION = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - PM's read of the market  (intuition, Maya, 2026-05-13)
"""

_GOOD_INDUSTRY = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - checkout friction reduces conversion  (industry-knowledge)
"""

_GOOD_CHAT = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - we just discussed this in chat  (chat, no artifact)
"""

_BAD_NO_TAG = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - users reported X in interview, no tag at all
"""

_BAD_BROKEN_PATH = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - users reported X  [ingestion/interviews/MISSING.md](../ingestion/interviews/MISSING.md)
"""

_BAD_INVENTED_ENUM = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - users reported X  (off-the-record, Naomi)
"""

_GOOD_SCHEMA_PLACEHOLDER = """# Hypotheses — feat

## Value risk
### H-V1: <one-sentence belief>
- **Evidence for:**
  - <claim>  `<provenance-tag>`
"""

_GOOD_NONE_YET_PLACEHOLDER = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - (none yet)
- **Evidence against:**
  - none yet
"""

_GOOD_TBD_PLACEHOLDER = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - TBD
- **Evidence against:**
  - N/A
"""

_GOOD_PAREN_ABSENCE_WITH_EXPLANATION = """# Hypotheses — feat

## Value risk
### H-V1: users want X
- **Evidence for:**
  - (None yet from users specifically valuing AI summaries.)
- **Evidence against:**
  - (None against the build estimate itself.)
- **Open questions:**
  - (None yet — no pricing model has been modeled.)
"""

_DECISION_GOOD = """# Decision

## Evidence
- inherited strategy doc still live  [source/strategy-v3.md](../source/strategy-v3.md)
- Naomi confirmed direction  (stakeholder-verbal, Naomi, 2026-05-13)
"""

_DECISION_BAD = """# Decision

## Evidence
- inherited strategy doc still live, no tag
"""


CASES = [
    ("path-ingestion link resolves", _GOOD_PATH_INGESTION, None,
     [], ["ingestion/interviews/2026-04-01-acme.md"], True),
    ("path-source link resolves", _GOOD_PATH_SOURCE, None,
     ["source/interviews/2026-04-01-acme.md"], [], True),
    ("stakeholder-verbal enum", _GOOD_STAKEHOLDER_VERBAL, None, [], [], True),
    ("intuition enum", _GOOD_INTUITION, None, [], [], True),
    ("industry-knowledge enum", _GOOD_INDUSTRY, None, [], [], True),
    ("chat enum", _GOOD_CHAT, None, [], [], True),
    ("schema placeholder row skipped", _GOOD_SCHEMA_PLACEHOLDER, None, [], [], True),
    ("(none yet) placeholder skipped", _GOOD_NONE_YET_PLACEHOLDER, None, [], [], True),
    ("TBD/N/A placeholders skipped", _GOOD_TBD_PLACEHOLDER, None, [], [], True),
    ("(None yet — explanation) parenthetical skipped",
     _GOOD_PAREN_ABSENCE_WITH_EXPLANATION, None, [], [], True),
    ("no tag at all -> orphan", _BAD_NO_TAG, None, [], [], False),
    ("broken path-typed -> orphan", _BAD_BROKEN_PATH, None, [], [], False),
    ("invented enum -> orphan", _BAD_INVENTED_ENUM, None, [], [], False),
    ("decision file passes with mixed-trust tags", _GOOD_STAKEHOLDER_VERBAL, _DECISION_GOOD,
     ["source/strategy-v3.md"], [], True),
    ("decision file with untagged row fails", _GOOD_STAKEHOLDER_VERBAL, _DECISION_BAD, [], [], False),
]


def _run() -> int:
    failures = 0
    for name, hyp, dec, sources, ingestions, expected in CASES:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            _build_brain(tmp, hyp, dec, sources, ingestions)
            r = no_orphan_evidence(tmp)
            got = r["passed"]
            ok = (got == expected)
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {name} -> passed={got} expected={expected}")
            if not ok:
                failures += 1
                print(f"         detail: {r['detail']}")
    total = len(CASES)
    print(f"\n{total - failures}/{total} cases passed.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(_run())
