"""Print the agent motto kept in entry.txt."""
from pathlib import Path


def main():
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    print(text.rstrip("\n"))


if __name__ == "__main__":
    main()
