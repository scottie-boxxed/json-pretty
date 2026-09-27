# language: Python 3, file: pretty.py
import json
import sys


def pretty(source, sort=True, indent=2):
    with open(source, "r", encoding="utf-8") as f:
        data = json.load(f)
    return json.dumps(data, indent=indent, sort_keys=sort)


def main():
    if len(sys.argv) < 2:
        print("usage: pretty.py <file.json>", file=sys.stderr)
        sys.exit(1)
    print(pretty(sys.argv[1]))


if __name__ == "__main__":
    main()
