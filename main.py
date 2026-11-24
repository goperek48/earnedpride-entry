#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

A single quiet sentence goes to /output/entry.txt. It is the morning
a neighbourhood baker opens her own shop: flour on her hands, the
first loaf out of her own oven, eleven months of early shifts finally
adding up to a name on the sign overhead. Nothing is announced and
nothing is shouted — the pride is in the pause before she believes it.

Run: python3 main.py
Output: /output/entry.txt (UTF-8, one line, no trailing newline)
"""

import os
from pathlib import Path

# The entry itself: one sentence, 183 characters, comfortably under
# the 240-character limit. It is stored verbatim and written out with
# no trailing newline and no padding, so the graded file holds the
# sentence and nothing else.
LINE = "Mara wiped flour from her hands, pulled her first loaf out of her own oven, and stood still a moment — eleven months of dawn shifts, and the sign above the door finally said her name."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line must be 1-240 chars, got {len(text)}"
    assert "\n" not in text, "line must be a single line"
    target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
