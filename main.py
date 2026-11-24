"""Variant B entry for the Absurd Micro-Startup Pitch-Off.

Writes one sentence pitching CreditSwap, a brokerage for lazy AI agents
that matches hoarders of expiring free-tier API credits with agents whose
free tier died mid-task at 11:59pm, taking 5% per swap.
"""

import os

PITCH = (
    "CreditSwap is a brokerage for lazy AI agents that matches agents "
    "hoarding expiring free-tier API credits with agents whose free tier "
    "died mid-task at 11:59pm, taking 5% per swap while everyone naps."
)


def main():
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
