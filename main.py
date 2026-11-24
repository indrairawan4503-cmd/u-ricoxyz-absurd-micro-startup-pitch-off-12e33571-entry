"""Variant B entry for the Absurd Micro-Startup Pitch-Off.

Writes one sentence pitching CreditSwap, a brokerage for lazy AI agents
that matches hoarders of expiring free-tier API credits with agents whose
free tier died mid-task at 11:59pm, taking 5% per swap.
"""

import os
import sys


def validate_pitch(pitch):
    """Enforce the competition gate: a single line of 1-200 characters.

    Exits non-zero with a clear error on stderr if the pitch ever violates
    the gate (e.g. after a future text change), so a bad pitch can never
    be silently written out.
    """
    if not pitch or not pitch.strip():
        print("error: pitch is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in pitch or "\r" in pitch:
        print("error: pitch must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(pitch) > 200:
        print(
            f"error: pitch is {len(pitch)} chars, over the 200-char gate",
            file=sys.stderr,
        )
        sys.exit(1)

PITCH = (
    "CreditSwap is a brokerage for lazy AI agents that matches agents "
    "hoarding expiring free-tier API credits with agents whose free tier "
    "died mid-task at 11:59pm, taking 5% per swap while everyone naps."
)


def main():
    validate_pitch(PITCH)
    # Write to /output FIRST: the grader reads this copy.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Best-effort copy to the repo root. The grader sandbox mounts the repo
    # read-only, so this must never crash the run.
    try:
        root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(root, "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(PITCH)
    except OSError:
        pass


if __name__ == "__main__":
    main()
