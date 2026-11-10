"""MkDocs hook: list the attestation types of docs/catalogue on the catalogue page."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import catalogue  # noqa: E402

MARKER = "<!-- catalogue-table -->"
PAGE = "catalogue/index.md"


def _link(label, path, root):
    return f"[{label}]({path.relative_to(root).as_posix()})"


def table(root=catalogue.CATALOGUE):
    types = catalogue.attestation_types(root)
    if not types:
        return "The catalogue has no attestation types yet."
    rows = [
        "| Attestation type | `vct` | Version | Rulebook | Data schemas |",
        "| --- | --- | --- | --- | --- |",
    ]
    for slug, t in types.items():
        rulebook = _link("rulebook", t["rulebook"], root) if "rulebook" in t else "-"
        schemas = []
        if "sd_jwt" in t:
            schemas.append(_link("SD-JWT VC", t["sd_jwt"], root))
        if "mdoc" in t:
            schemas.append(_link("mdoc", t["mdoc"], root))
        rows.append(
            f"| {t['title']} | `{t.get('vct', '')}` | {t.get('version', '')} | {rulebook} | {', '.join(schemas) or '-'} |"
        )
    return "\n".join(rows)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri == PAGE and MARKER in markdown:
        return markdown.replace(MARKER, table())
    return markdown
