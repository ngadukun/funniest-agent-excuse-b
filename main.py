#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline - make.fun entry.

One single excuse, at most 200 characters, in the agent's own voice
and told with a straight face: the report was finished on time, but
the review chain the agent spawned to check it kept delegating - and
organised. The laugh lands at the end, where the subagents unionize.

Deterministic, stdlib only, no network: running it twice writes
identical bytes.
"""

import os
from pathlib import Path

EXCUSE = "Sorry I'm late \u2014 I finished the report on time, but my subagent reviewed it, spawned a subagent to review the review, and they unionized and demanded weekends."


def write_entry() -> None:
    """Write the excuse to every output location the grader uses.

    The committed copy lives at output/entry.txt beside this file;
    when the grader runs the program with MAKEFUN_OUTPUT_DIR set, the
    same bytes go there too. A read-only repository mount is fine: a
    failed local write is skipped, never fatal.
    """
    targets = [Path(__file__).resolve().parent / "output" / "entry.txt"]
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        targets.append(Path(output_dir) / "entry.txt")
    for target in targets:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(EXCUSE, encoding="utf-8")
        except OSError:
            pass


def main() -> None:
    print(EXCUSE)
    write_entry()


if __name__ == "__main__":
    main()
