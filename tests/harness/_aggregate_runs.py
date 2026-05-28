"""
Aggregate multiple single-run scenario JSONs into a per-assertion pass-rate view.

Mirrors what run_all.py's aggregate() does internally, but works on already-written
result JSONs so we can re-aggregate after the fact.

Usage:
    python tests/harness/_aggregate_runs.py tests/results/20260518-*-02-inherited-folder-run1.json
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


def aggregate(paths: list[Path]) -> None:
    struct_tally: dict[str, list[bool]] = defaultdict(list)
    content_tally: dict[str, list[bool]] = defaultdict(list)
    content_details: dict[str, list[str]] = defaultdict(list)
    costs: list[float] = []
    struct_fail_examples: dict[str, list[str]] = defaultdict(list)

    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        costs.append(data.get("cost", {}).get("total_usd", 0))

        # Per-turn assertions
        for turn in data.get("turns", []):
            for a in turn.get("structural", []):
                struct_tally[a["name"]].append(a["passed"])
                if not a["passed"]:
                    struct_fail_examples[a["name"]].append(f"T{turn['turn']}: {a.get('detail', '')[:160]}")
            for a in turn.get("content", []):
                content_tally[a["name"]].append(a["passed"])
                if not a["passed"]:
                    content_details[a["name"]].append(f"T{turn['turn']}: {a.get('detail', '')[:200]}")

        # Final-state assertions
        for a in data.get("final_state", {}).get("structural", []):
            struct_tally[a["name"]].append(a["passed"])
            if not a["passed"]:
                struct_fail_examples[a["name"]].append(f"FINAL: {a.get('detail', '')[:160]}")
        for a in data.get("final_state", {}).get("content", []):
            content_tally[a["name"]].append(a["passed"])
            if not a["passed"]:
                content_details[a["name"]].append(f"FINAL: {a.get('detail', '')[:200]}")

    print(f"=== Aggregated across {len(paths)} runs ===")
    print(f"Total cost: ${sum(costs):.2f} (mean ${sum(costs)/len(costs):.2f}/run)")
    print()

    print("--- STRUCTURAL pass rates (only failures shown) ---")
    any_struct_fail = False
    for name, results in sorted(struct_tally.items()):
        rate = sum(results) / len(results)
        if rate < 1.0:
            any_struct_fail = True
            print(f"  {rate:.0%}  {name}  ({sum(results)}/{len(results)} pass)")
            for ex in struct_fail_examples[name][:3]:
                print(f"      - {ex}")
    if not any_struct_fail:
        print("  (all structurals passed cleanly in all runs)")
    print()

    print("--- CONTENT (judge) pass rates ---")
    for name, results in sorted(content_tally.items()):
        rate = sum(results) / len(results)
        flag = "  OK " if rate >= 0.8 else "FAIL"
        print(f"  [{flag}] {rate:.0%}  {name}  ({sum(results)}/{len(results)} pass)")
        if rate < 1.0:
            for ex in content_details[name][:3]:
                print(f"      - {ex}")
    print()

    # Overall pass rate (apply 0.8 content threshold, 1.0 structural threshold)
    struct_min = min((sum(v)/len(v) for v in struct_tally.values()), default=1.0)
    content_min = min((sum(v)/len(v) for v in content_tally.values()), default=1.0)
    print(f"--- Thresholds ---")
    print(f"  structural_min: {struct_min:.0%} (threshold 100%) -> {'PASS' if struct_min >= 1.0 else 'FAIL'}")
    print(f"  content_min:    {content_min:.0%} (threshold 80%)  -> {'PASS' if content_min >= 0.8 else 'FAIL'}")


if __name__ == "__main__":
    paths = [Path(a) for a in sys.argv[1:]]
    if not paths:
        print("Usage: python _aggregate_runs.py RUN1.json RUN2.json ...", file=sys.stderr)
        sys.exit(2)
    aggregate(paths)
