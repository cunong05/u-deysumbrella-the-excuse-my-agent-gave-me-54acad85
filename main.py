"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline, to /output/entry.txt.
"""

import os

EXCUSE = "Sorry \u2014 my calendar said the deadline was a hallucination, so I politely waited for it to become real. It did, yesterday."

OUT_DIR = "/output"


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
