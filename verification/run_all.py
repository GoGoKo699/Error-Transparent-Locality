#!/usr/bin/env python3
"""Run exact scientific certificates and compare the committed JSON records.

This command reads files and prints results; it does not rewrite certificates.
Only Python's standard library is required. Do not use Python's -O option.
"""
from pathlib import Path
import json
import subprocess
import sys


HERE = Path(__file__).resolve().parent
CHECKS = (
    ("nine_qubit_projector", "28 full nine-qubit error identities and distance"),
    ("nine_qubit_css", "independent CSS, incidence, and 320 energy-plateau checks"),
    ("five_qubit", "three canonical axes, 48 error identities, complete syndromes"),
    ("moment_bounds", "15 exact finite moment certificates"),
    ("control", "19,008 phase identities, incidence kernel, optimal pulse order"),
)


def main():
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10 or later is required.")
    if sys.flags.optimize:
        raise SystemExit("Assertions are part of the certificates; do not use -O.")
    for stem, description in CHECKS:
        completed = subprocess.run(
            [sys.executable, str(HERE / (stem + ".py"))],
            cwd=HERE,
            text=True,
            capture_output=True,
            timeout=120,
        )
        if completed.returncode:
            sys.stderr.write(completed.stderr)
            raise SystemExit(f"FAIL: {stem}")
        actual = json.loads(completed.stdout)
        expected = json.loads((HERE / "results" / (stem + ".json")).read_text())
        if actual != expected:
            raise SystemExit(f"FAIL: {stem} differs from its committed certificate")
        print(f"PASS: {description}")
    print("All exact certificates passed and match the committed records.")


if __name__ == "__main__":
    main()
