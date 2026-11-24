"""make.fun make-the-judge-smile entry.

Writes a single line about a small good thing that happened today:
an unexpected kindness from the last person you'd expect it from.
"""

import os

LINE = (
    "The grumpiest man on my street left a warm loaf on my doorstep "
    "this morning with a note \u2014 'You looked tired yesterday' "
    "\u2014 and I hadn't told a soul I was tired."
)


def main() -> None:
    # Guard the competition rules at runtime: one line, 1-200 chars.
    # Fail loudly instead of silently writing an invalid entry.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"entry line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry line must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
