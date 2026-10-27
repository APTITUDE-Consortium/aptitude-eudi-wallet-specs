#!/usr/bin/env python3
"""Create the rulebook, the SD-JWT schema and the card of a new attestation type from the templates."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalogue  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="lower-case words joined by hyphens, for example 'ferry-boarding-pass'")
    parser.add_argument("title", help="display title, for example 'Ferry Boarding Pass'")
    args = parser.parse_args()
    if not catalogue.SLUG_RE.match(args.slug):
        sys.exit(f"slug '{args.slug}' must be lower-case words joined by hyphens")

    root = catalogue.CATALOGUE
    tpl = root / "_template"
    targets = {
        tpl / "rulebook" / "README.md": root / "rulebooks" / f"rb-{args.slug}" / "README.md",
        tpl / "data-schemas" / "sd-jwt" / "template-sd-jwt.json": root / "data-schemas" / "sd-jwt" / f"{args.slug}-sd-jwt.json",
        tpl / "assets" / "card.svg": root / "assets" / args.slug / "card.svg",
    }
    for dst in targets.values():
        if dst.exists():
            sys.exit(f"{dst} exists")
    for src, dst in targets.items():
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8").replace("{{slug}}", args.slug).replace("{{title}}", args.title)
        dst.write_text(text, encoding="utf-8")
        print(f"created {dst.relative_to(root.parent.parent)}")
    print("Next: write the rulebook and the schema together, add a CODEOWNERS line, run script/validate_catalogue.py")


if __name__ == "__main__":
    main()
