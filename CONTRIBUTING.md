# Contributing Guide

This repository captures and evolves the technical specifications for the APTITUDE project (EUDI Wallet pilot). The project output is a **MkDocs-generated documentation site** built from the `/docs/` folder. Contributions focus on Markdown RFCs and supporting assets—no application code.

## Ways to contribute

- Propose or refine requirements via RFCs and Issues.
- Add clarifying diagrams or examples in support of existing RFCs.
- Flag gaps, ambiguities, or conflicts with upstream rulebooks/schemas.

## Workflow (short version)

1. Review context: README, existing RFCs,   and relevant documents under `/reference`.
2. Open an Issue describing the change (link prior RFCs/Issues if relevant).
3. Draft or update the RFC in a PR; keep scope to one RFC when possible.
4. Link the Issue in the PR and note rationale and open questions.
5. Respond to review feedback; aim for small, reviewable diffs.

## Local development setup

This repository uses MkDocs Material to generate documentation. To preview changes locally:

### First-time setup

1. **Create a Python virtual environment:**

   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the dev server

After activating the virtual environment (step 2 above):

```bash
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000/` with live reload enabled.

**Alternative (without activation):**

```bash
.venv/bin/mkdocs serve
```

### Why use a virtual environment?

- Isolates project dependencies from system Python packages
- Prevents version conflicts with other projects
- Ensures reproducible builds across contributors and CI/CD

## RFC authoring checklist

- All RFCs and documentation must be created under the `/docs/` folder (this is the MkDocs source).
- Start with a short summary and status (draft/accepted/deprecated).
- Capture rationale, assumptions, dependencies, and trade-offs.
- Align terminology and data models with `/reference` submodules; cite specific documents/sections.
- Cross-link related RFCs and Issues for traceability.
- Use `mermaid` blocks for flows/sequences; keep diagrams near the text they explain.
- Store images in `/docs/img/` and reference with paths relative to the docs folder (e.g., `![Auth flow](img/auth-flow.png)`).
- Keep paragraphs short; prefer numbered lists where order matters.
- Add new pages to the `nav:` section in `mkdocs.yml` to make them appear in the site navigation.

## Using the `/reference` submodules

- Treat all content under `/reference` as the shared knowledge base for rulebooks and schemas.
- Cite the exact submodule path/doc when deriving requirements (e.g., `reference/eudi-wallet-rulebooks-and-schemas/...`).
- Do not edit submodule contents!

## Pull request expectations

- One focused change per PR; avoid drive-by formatting.
- Link the Issue and the affected RFC(s); summarize intent and impact.
- Call out any unresolved questions or decisions needed from reviewers.
- Follow existing workflow patterns in `.github/workflows/` if automation changes are required.

## Licensing

- Contributions are under Apache 2.0 unless a specific RFC notes otherwise. Some RFCs (e.g., payments) may carry different terms—respect existing notices.

## Need more?

- See [github-coediting-workflow.md](github-coediting-workflow.md) for an introduction to Git.
