#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App entry.

Writes one dating-app bio line to /output/entry.txt (UTF-8, 180
Unicode code points at most, inside the 1-180 gate). Deterministic,
standard library only, no network, no environment reads.

The bio (170 characters): "Large language model, small emotional
baggage: I remember your birthday, your coffee order, and everything
you said at 2 a.m. Swipe right if you proofread your own texts." It
opens with a dating-profile cliche flipped for an AI, turns the
perfect memory into both the selling point and the quiet threat, and
closes with a picky, human-sounding dealbreaker. An earlier draft
leaned on "I never sleep" jokes; the memory angle won because it is
flattering for exactly one sentence before it becomes surveillance.
"""

import os

TEXT = (
    "Large language model, small emotional baggage: I remember your "
    "birthday, your coffee order, and everything you said at 2 a.m. "
    "Swipe right if you proofread your own texts."
)


def main() -> None:
    # The gate requires 1-180 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 180, "entry must be 1-180 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
