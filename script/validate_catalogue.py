#!/usr/bin/env python3
"""Validate the attestation catalogue under docs/catalogue.

Errors fail the run; warnings fail it only with --strict.
"""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalogue  # noqa: E402

try:
    from jsonschema import Draft202012Validator
except ImportError:  # the validator reports this as an error below
    Draft202012Validator = None

CHAPTERS = [
    "Introduction",
    "Attestation attributes and metadata",
    "Attestation encoding",
    "Attestation usage",
    "Trust anchors",
    "Revocation",
    "Compliance",
    "References",
]
FORBIDDEN_SVG = {"script", "image", "foreignObject", "style", "iframe", "a", "object", "embed"}
SCHEMA_URI = "https://json-schema.org/draft/2020-12/schema"


def check_schema(path, kind, errors, warnings):
    rel = path.relative_to(catalogue.CATALOGUE)
    try:
        schema = catalogue.load_json(path)
    except ValueError as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
        return None
    if Draft202012Validator is not None:
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema.SchemaError
            errors.append(f"{rel}: not a valid JSON Schema 2020-12: {getattr(exc, 'message', exc)}")
    if schema.get("$schema") != SCHEMA_URI:
        errors.append(f"{rel}: $schema must be {SCHEMA_URI}")
    for key in ("title", "description", "version"):
        if not schema.get(key):
            errors.append(f"{rel}: the root needs {key}")
    props = schema.get("properties", {})
    for name in schema.get("required", []):
        if name not in props:
            errors.append(f"{rel}: required entry '{name}' is not a property")
    if "required" not in schema:
        errors.append(f"{rel}: the root needs required")
    if kind == "sd-jwt":
        if not isinstance(props.get("vct", {}).get("const"), str):
            errors.append(f"{rel}: properties.vct.const must be a string")
        if "examples" not in schema and not any("examples" in p for p in props.values() if isinstance(p, dict)):
            warnings.append(f"{rel}: no examples")
    return schema


def check_rulebook(path, errors, warnings):
    rel = path.relative_to(catalogue.CATALOGUE)
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^# \S", text, re.M):
        errors.append(f"{rel}: the rulebook needs a level-1 title")
    headings = [re.sub(r"^\d+(\.\d+)*\s*", "", h).strip() for h in re.findall(r"^#{2}\s+(.+)$", text, re.M)]
    for chapter in CHAPTERS:
        if chapter not in headings:
            warnings.append(f"{rel}: chapter '{chapter}' is missing")
    if "{{" in text:
        errors.append(f"{rel}: template placeholder '{{{{' is still present")


def check_card(path, slug_schemas, errors):
    rel = path.relative_to(catalogue.CATALOGUE)
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        errors.append(f"{rel}: invalid XML: {exc}")
        return
    for bad in sorted({e.tag.split("}")[-1] for e in root.iter()} & FORBIDDEN_SVG):
        errors.append(f"{rel}: <{bad}> is outside the card format")
    text = path.read_text(encoding="utf-8")
    if "data:" in text or re.search(r'(href|src)\s*=\s*"(?!#)', text) or re.search(r'on[a-z]+\s*=\s*"', text):
        errors.append(f"{rel}: external references, data: URIs and event handlers are outside the card format")
    if not root.get("viewBox"):
        errors.append(f"{rel}: viewBox is required")
    if path.parent.name not in slug_schemas:
        errors.append(f"{rel}: no data schema with the slug {path.parent.name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = parser.parse_args()
    errors, warnings = [], []
    if Draft202012Validator is None:
        errors.append("the jsonschema package is required (pip install jsonschema)")

    root = catalogue.CATALOGUE
    sdjwt = {}
    for path in catalogue.sdjwt_schemas(root):
        slug = catalogue.slug_of(path, catalogue.SDJWT_SUFFIX)
        sdjwt[slug] = path
        if not catalogue.NAME_RE.match(path.name[: -len(catalogue.SDJWT_SUFFIX)]):
            errors.append(f"{path.relative_to(root)}: name must be [dsNNN-]<slug>{catalogue.SDJWT_SUFFIX}")
        check_schema(path, "sd-jwt", errors, warnings)
    mdoc = {}
    for path in catalogue.mdoc_schemas(root):
        mdoc[catalogue.slug_of(path, catalogue.MDOC_SUFFIX)] = path
        check_schema(path, "mdoc", errors, warnings)

    rb = {}
    for path in catalogue.rulebooks(root):
        slug = path.parent.name[len("rb-"):]
        rb[slug] = path
        if not catalogue.SLUG_RE.match(slug):
            errors.append(f"{path.parent.relative_to(root)}: slug must be lower-case words joined by hyphens")
        check_rulebook(path, errors, warnings)
    for d in (root / "rulebooks").glob("rb-*") if (root / "rulebooks").exists() else []:
        if not (d / "README.md").is_file():
            errors.append(f"{d.relative_to(root)}: README.md is missing")

    for slug in sorted(set(sdjwt) | set(mdoc)):
        if slug not in rb:
            warnings.append(f"{slug}: data schema without a rulebook")
    for slug in sorted(rb):
        if slug not in sdjwt and slug not in mdoc:
            errors.append(f"{slug}: rulebook without a data schema")

    for path in sorted((root / "assets").glob("*/*.svg")) if (root / "assets").exists() else []:
        check_card(path, set(sdjwt) | set(mdoc), errors)

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(sdjwt)} SD-JWT VC schemas, {len(mdoc)} mdoc schemas, {len(rb)} rulebooks; {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors or (args.strict and warnings) else 0)


if __name__ == "__main__":
    main()
