# Contributing Guide

This repository contains the technical documentation for the APTITUDE EUDI Wallet pilot.

Most contributions are text updates (requirements, RFC content, clarifications, diagrams). This is not an application code repository.

## What You Can Contribute

- Propose a new requirement.
- Improve or clarify an existing RFC.
- Add examples or diagrams.
- Report gaps, unclear wording, or conflicts with rulebooks/schemas.

## Recommended Workflow

1. Read the context first: `README.md`, related RFC pages, and relevant files under `reference/`.
2. Open a GitHub Issue describing what you want to change and why.
3. Create a pull request with a focused update (ideally one RFC/topic at a time).
4. Link the Issue in the pull request and explain rationale and open questions.
5. Address review comments and keep changes small and easy to review.

## If You Want To Preview Locally

This documentation site is built with MkDocs.

You do not need to run MkDocs locally to suggest or submit documentation changes. A pull request with clear text updates is enough. Local preview is optional and useful when you want to check formatting before review.

### First-Time Setup

1. Create a Python virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. Activate it:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Start The Preview Server

After activation, run:

```bash
mkdocs serve
```

Open: `http://127.0.0.1:8000/`

The page updates automatically when files change.

Alternative without activation:

```bash
.venv/bin/mkdocs serve
```

### Why The Virtual Environment Matters

- Isolates project dependencies from system Python packages
- Prevents version conflicts with other projects
- Ensures reproducible builds across contributors and CI/CD

## Writing Checklist

- Create and edit documentation under `docs/`.
- Start each RFC with a short summary and status (`draft`, `accepted`, `deprecated`).
- Explain assumptions, dependencies, and trade-offs.
- Use consistent terms aligned with the content in `reference/`.
- Link related RFCs and Issues.
- Keep text short and clear.
- Put images in `docs/img/` and link with relative paths.
- Add new pages to `nav:` in `mkdocs.yml` so they appear in the site menu.

### Glossary Terms

Use glossary links for terms that need a consistent meaning across documents.

- To reference an existing term in a page, use:
  `<section:term|text shown to readers>`
  Example: `<components:EUDI Wallet|European Digital Identity Wallet (EUDI Wallet)>`
- To add a new term, edit `docs/glossary-definitions.md`:
  add `section:term` on one line and the definition on the next line.
  Then use that term in pages with the reference format above.

If you are unsure which section to use, pick one of: `roles`, `components`, `credentials`.

## About The `reference/` Folder

- Treat `reference/` as read-only source material for rulebooks and schemas.
- Cite the exact source path when deriving requirements.
- Do not edit files inside `reference/` unless explicitly requested.

## Pull Request Expectations

- One focused change per PR; avoid drive-by formatting.
- Link the Issue and affected RFC(s); summarize intent and impact.
- Clearly list open questions for reviewers.
- Follow existing workflow patterns in `.github/workflows/` if automation changes are required.

## Licensing

- Contributions are under Apache 2.0 unless a specific RFC says otherwise.
- Some RFCs (for example payments) may have different terms. Respect existing notices.

## Need more?

- See `github-coediting-workflow.md` for a Git introduction.
