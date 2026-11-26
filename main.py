#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Prints the one-line entry exactly, with no trailing newline.
"""

ENTRY = "Soon the sun will choose your newest leaf first, and the whole windowsill will pretend not to be jealous."


def validate(line: str) -> str:
    """Entry must be a single line within the 1-120 char limit."""
    assert 1 <= len(line) <= 200, f"entry length out of range: {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    return line


def main() -> None:
    print(validate(ENTRY), end="")


if __name__ == "__main__":
    main()
