#!/usr/bin/env python3
"""Agent Motto Battle entry runner.

Reads the motto from entry.txt next to this script and prints it.
Standard library only — no third-party dependencies.
"""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    motto = entry_path.read_text(encoding="utf-8").strip()
    print(motto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
