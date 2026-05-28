#!/usr/bin/env python3
"""
run_all.py — run every scenario under tests/scenarios/, N runs each.

USAGE
    python tests/harness/run_all.py
    python tests/harness/run_all.py --runs 5
    python tests/harness/run_all.py --runs 5 --max-cost 100

STATUS
    Skeleton. Delegates to run_scenario.py.
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCENARIOS_DIR = REPO_ROOT / "tests" / "scenarios"
RUN_SCENARIO = REPO_ROOT / "tests" / "harness" / "run_scenario.py"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--max-cost", type=float, default=None)
    args = ap.parse_args()

    scenarios = sorted([p for p in SCENARIOS_DIR.iterdir() if p.is_dir()])
    if not scenarios:
        sys.exit("No scenarios found under tests/scenarios/")

    overall = {"pass": [], "fail": []}
    for s in scenarios:
        print(f"\n========== {s.name} ==========", file=sys.stderr)
        cmd = ["python", str(RUN_SCENARIO), str(s), "--runs", str(args.runs)]
        if args.max_cost is not None:
            cmd += ["--max-cost", str(args.max_cost)]
        result = subprocess.run(cmd)
        (overall["pass"] if result.returncode == 0 else overall["fail"]).append(s.name)

    print(f"\nPassed: {overall['pass']}")
    print(f"Failed: {overall['fail']}")
    sys.exit(0 if not overall["fail"] else 1)


if __name__ == "__main__":
    main()
