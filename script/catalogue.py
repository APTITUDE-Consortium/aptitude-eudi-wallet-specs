"""Shared helpers for the attestation catalogue under docs/catalogue."""

import json
import re
from pathlib import Path

CATALOGUE = Path(__file__).resolve().parent.parent / "docs" / "catalogue"
SDJWT_SUFFIX = "-sd-jwt.json"
MDOC_SUFFIX = "-mdoc.json"
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_RE = re.compile(r"^(ds\d+-)?(?P<slug>[A-Za-z0-9]+(-[A-Za-z0-9]+)*)$")


def slug_of(path: Path, suffix: str) -> str:
    """Slug of a schema file: the file name without the suffix and a leading dsNNN-."""
    return re.sub(r"^ds\d+-", "", path.name[: -len(suffix)])


def sdjwt_schemas(root: Path = CATALOGUE):
    return sorted((root / "data-schemas" / "sd-jwt").glob("*" + SDJWT_SUFFIX))


def mdoc_schemas(root: Path = CATALOGUE):
    return sorted((root / "data-schemas" / "mdoc").glob("*" + MDOC_SUFFIX))


def rulebooks(root: Path = CATALOGUE):
    return sorted((root / "rulebooks").glob("rb-*/README.md"))


def load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def attestation_types(root: Path = CATALOGUE):
    """Describe every attestation type found in the tree, keyed by slug."""
    types = {}
    for path in sdjwt_schemas(root):
        slug = slug_of(path, SDJWT_SUFFIX)
        entry = types.setdefault(slug, {"slug": slug})
        entry["sd_jwt"] = path
        try:
            schema = load_json(path)
            entry["title"] = schema.get("title") or slug
            entry["version"] = schema.get("version", "")
            entry["vct"] = schema.get("properties", {}).get("vct", {}).get("const", "")
        except (ValueError, OSError):
            entry["title"] = slug
    for path in mdoc_schemas(root):
        slug = slug_of(path, MDOC_SUFFIX)
        types.setdefault(slug, {"slug": slug, "title": slug})["mdoc"] = path
    for path in rulebooks(root):
        slug = path.parent.name[len("rb-"):]
        types.setdefault(slug, {"slug": slug, "title": slug})["rulebook"] = path
    return dict(sorted(types.items()))
