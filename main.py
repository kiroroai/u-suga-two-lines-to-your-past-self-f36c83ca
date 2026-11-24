#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): line 1 warns the writer's past self about one
specific moment; line 2 says in one sentence why that moment
mattered and what changed because of it.
"""

import os

LINE_1 = (
    "Don't sign the $40,000 loan papers at the kitchen table the night "
    "your father says, \"Just sign it, we'll figure it out later.\""
)
LINE_2 = (
    "That signature cost you three years of overtime and the flat you'd "
    "saved for, and it's why you now read every page twice "
    "before your name touches it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
