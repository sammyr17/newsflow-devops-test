import json
import sys
from typing import Dict


def parse_article(raw: str) -> Dict[str, str]:
    """Simple article parser.

    First non-empty line is treated as the title.
    Remaining non-empty lines form the body.
    """
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        raise ValueError("Empty article")

    title = lines[0]
    body = "\n".join(lines[1:]) if len(lines) > 1 else ""
    return {"title": title, "body": body}


def main(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    article = parse_article(raw)
    print(json.dumps(article))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python article_parser.py <file>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
