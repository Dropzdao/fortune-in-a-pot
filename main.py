#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant."""

ENTRY = "Soon the sun will choose your newest leaf first, and the whole windowsill will pretend not to be jealous."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
