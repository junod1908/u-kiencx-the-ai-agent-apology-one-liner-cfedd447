#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short apology line an AI agent sends its human right after
it has broken something. The line is 103 characters of UTF-8 text.
"""
import os

ENTRY = "I changed every password to one very strong password. I have forgotten it. It was very strong."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
