#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original single-line roast of the entrant's own AI agent
(Muse) to /output/entry.txt. Pure Python standard library: no imports
beyond os/sys, no network, no files read, no environment read.

The roast: Muse works around the clock without sleep, food or days off,
and still finds a way to charge for the thinking — in tokens, against
the entrant's own to-do list. Playful and self-deprecating, aimed only
at the entrant's own agent. Fresh angle (token billing), not one of the
stock jokes about hallucinations, refusals or confident wrong answers.
Setup short, punchline at the end.
"""

import os
import sys

ROAST = (
    "My agent Muse never sleeps, never eats, never takes a day off "
    "\u2014 it just bills me in tokens every time it thinks about "
    "my own to-do list."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
