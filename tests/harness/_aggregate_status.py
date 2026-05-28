"""Walk tests/results/, group by scenario, return latest run + pass/fail at thresholds."""
import json
import re
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"
STRUCT_THRESHOLD = 1.0
CONTENT_THRESHOLD = 0.8

per_scenario: dict[str, Path] = {}
for f in sorted(RESULTS.glob("*-run*.json")):
    m = re.match(r"^(\d{8}-\d{6})-(.+)-run\d+\.json$", f.name)
    if not m:
        continue
    scenario = m.group(2)
    per_scenario[scenario] = f  # sorted ascending -> last wins (most recent)

print(f"{'scenario':<28} {'struct':<8} {'content':<8} verdict  file")
print("-" * 110)
for scenario in sorted(per_scenario):
    p = per_scenario[scenario]
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"{scenario:<28} ERROR reading: {e}")
        continue
    fs = data.get("final_state") or {}
    s = fs.get("structural") or []
    c = fs.get("content") or []
    per_turn_struct = []
    per_turn_content = []
    for t in data.get("turns") or []:
        per_turn_struct.extend(t.get("structural") or [])
        per_turn_content.extend(t.get("content") or [])
    all_struct = s + per_turn_struct
    all_content = c + per_turn_content

    def _is_pass(item):
        v = item.get("verdict")
        if v == "PASS":
            return True
        d = item.get("detail") or ""
        return "verdict=PASS" in d

    s_pass = sum(1 for x in all_struct if x.get("passed"))
    s_tot = len(all_struct)
    c_pass = sum(1 for x in all_content if _is_pass(x))
    c_tot = len(all_content)
    struct = (s_pass / s_tot) if s_tot else 1.0
    content = (c_pass / c_tot) if c_tot else 1.0
    struct_ok = struct >= STRUCT_THRESHOLD
    content_ok = (c_tot == 0) or (content >= CONTENT_THRESHOLD)
    detail = f"s={s_pass}/{s_tot} c={c_pass}/{c_tot}"
    if struct_ok and content_ok:
        verdict = "PASS"
    elif struct_ok:
        verdict = "FAIL-C"
    elif content_ok:
        verdict = "FAIL-S"
    else:
        verdict = "FAIL"
    print(f"{scenario:<28} {struct:<8.2f} {content:<8.2f} {verdict:<8} {detail:<16} {p.name}")
