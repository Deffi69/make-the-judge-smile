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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
