"""Warning Label for Humans: One Line, Big Laugh.

Writes one original single-line safety warning label for every human being
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.
"""

import os

LINE = (
    "WARNING: This human is not waterproof, not dishwasher safe, and will, "
    "without warning, remember something embarrassing from 2009 at 3 a.m."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
