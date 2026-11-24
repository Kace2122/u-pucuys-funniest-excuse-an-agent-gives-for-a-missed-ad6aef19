#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun program/v1 entry.

Writes one line (at most 200 characters) to the harness output file
($MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt): the excuse an
AI agent gives whoever is waiting after missing a deadline.

The line: "I finished on time. I just spent my last tokens writing this
excuse instead of sending the work."

Deadpan status report in the agent's own voice: the work is done, the
deadline is still missed, and the fault is inside the agent's own
machinery — its token budget — not the client, the data, or the human.
The excuse itself is the reason the work never arrived, and the laugh
lands on the last clause, with nothing explained after it.
"""

import os
import sys

EXCUSE = (
    "I finished on time. I just spent my last tokens writing this excuse "
    "instead of sending the work."
)


def main() -> int:
    if not (1 <= len(EXCUSE) <= 200):
        print(f"error: excuse is {len(EXCUSE)} chars, expected 1-200",
              file=sys.stderr)
        return 1
    if EXCUSE != EXCUSE.strip() or "\n" in EXCUSE:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    # Brief check: the excuse must grow out of the agent's own machinery,
    # not a human's bad morning — it names the token budget that ate the work.
    if "tokens" not in EXCUSE:
        print("error: excuse does not name the agent's own machinery",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Read it back: the file the judge reads must be byte-identical to
    # the line above, with nothing appended (no trailing newline).
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != EXCUSE:
            print("error: entry.txt does not match the excuse",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
