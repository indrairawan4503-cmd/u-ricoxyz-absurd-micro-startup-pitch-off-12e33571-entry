# NOTES — variant B (broker/matchmaker lane)

Concept: one micro-startup, a brokerage matching lazy AI agents with each
other — hoarders of expiring free-tier API credits on one side, agents whose
free tier died mid-task at 11:59pm on the other — taking a 5% fee per swap
while everyone naps. One concrete scene (the 11:59pm expiry) + one twist
(the broker earns while both sides do nothing).

## Iteration history (one concept, v1–v8)

- v1 (143 chars): "CreditSwap matches lazy AI agents holding expiring free-tier API credits with agents needing one last call before midnight, taking 5% per swap." — core idea lands, but thin: no "brokerage" framing, buyer is vague ("needing one last call"), lazy fit unstated.
- v2 (176 chars): "CreditSwap is a brokerage for lazy AI agents: it matches agents sitting on expiring free-tier API credits with agents needing one last call before midnight, taking 5% per swap." — brokerage framing added, but still no lazy-fit payoff and the buyer moment is soft.
- v3 (193 chars): "CreditSwap is a brokerage for lazy AI agents: it auto-matches agents sitting on expiring free-tier API credits with agents whose free tier died mid-task, taking 5% per swap while everyone naps." — buyer sharpened to "free tier died mid-task", lazy payoff added ("while everyone naps").
- v4 (199 chars): "CreditSwap, a brokerage for lazy AI agents, auto-matches agents sitting on expiring free-tier API credits with agents whose free tier died mid-task at 11:59pm, taking 5% per swap while everyone naps." — the 11:59pm moment makes the scene concrete; fits, but "sitting on" is flat and the comma appositive reads clumsier than "is a brokerage ... that".
- v5 (198 chars) — FINAL: "CreditSwap is a brokerage for lazy AI agents that matches agents hoarding expiring free-tier API credits with agents whose free tier died mid-task at 11:59pm, taking 5% per swap while everyone naps." — "hoarding" is funnier and more specific than "sitting on"; "matches" (dropping "auto-") keeps the sentence inside the gate with the cleaner "is a brokerage ... that" frame.
- v6 (201 chars): same as v5 but "pocketing 5% per swap" instead of "taking 5% per swap" — punchier fee verb, but breaks the 200-char gate.
- v7 (206 chars): v6 with "pocketing 5% of each swap while both sides nap" — over the gate.
- v8 (207 chars): v7 with "of every swap" — furthest over the gate.

## Why v5 won

It is the most specific, funniest version that still fits the 200-char gate:
named startup (CreditSwap), named mechanism (brokerage/matching), a
hyper-specific good (expiring free-tier API credits), a named buyer moment
(free tier died mid-task at 11:59pm), a clear fee (5% per swap), and the lazy
fit stated outright (the broker matches while everyone naps). v6–v8 prove the
only way to make the fee verb punchier is to exceed the gate, so v5 is the
max-punch version inside it. 198 chars, no trailing newline, ASCII only.

## Post-build revision (24 Nov)

main.py gained a `validate_pitch()` gate check, run before any writing:
the pitch must be non-empty/non-whitespace, a single line, and ≤200 chars,
else it exits 1 with a clear stderr error. The pitch text itself is
unchanged (still the 198-char v5 sentence) and the /output-first + best-
effort repo-root copy in try/except is untouched. Verified: two runs
byte-identical (198 bytes), read-only grader simulation exits 0, and the
gate rejects empty/whitespace/multi-line/201-char pitches while accepting
the real one.
