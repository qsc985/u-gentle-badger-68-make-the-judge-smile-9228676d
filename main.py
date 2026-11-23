#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line about a small good thing
that happened today to /output/entry.txt (at most 200 characters)."""

import os

LINE = (
    "At 6:40 this morning Rosa at the bakery slid my coffee across before "
    "I'd said a word \u2014 two sugars, exactly how I take it \u2014 then "
    "winked like we'd just pulled off a heist together."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
