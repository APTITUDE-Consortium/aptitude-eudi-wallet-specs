# Release Process

This repository publishes versioned documentation to GitHub Pages. This document describes how a new version is cut, who can do it, and what happens as a result.

## Table of Contents

* [Overview](#overview)
* [Version Numbering](#version-numbering)
* [Who Can Run a Release](#who-can-run-a-release)
* [How to Run a Release](#how-to-run-a-release)
* [What the Release Process Does](#what-the-release-process-does)
* [Where to Find a Released Version](#where-to-find-a-released-version)
* [Running Two Releases in the Same Month](#running-two-releases-in-the-same-month)
* [Troubleshooting](#troubleshooting)

## Overview

Publishing is entirely manual and deliberate: there is no workflow that deploys on every push to `main`. The only way the live site changes is by running [`.github/workflows/release.yml`](.github/workflows/release.yml) ("Release documentation") from the Actions tab.

Each run:

* Mints a new version number and tags it.
* Builds the documentation site from the current `main` branch.
* Publishes a [GitHub Release](../../releases) for that tag, with the built site attached as a downloadable zip.
* Publishes the built site to the live GitHub Pages site as a new, selectable version, and points `latest` at it.

This keeps published versions as deliberate, citable checkpoints rather than one per commit — appropriate for a specification document that implementers may pin to.

## Version Numbering

Versions follow `v<yyyymm>.<n>`:

* `yyyy` — four-digit year.
* `mm` — two-digit month, zero-padded.
* `n` — a progressive number starting at `1`, reset at the beginning of each month.

Examples: `v202607.1`, `v202607.2`, then `v202608.1` at the start of the next month.

The workflow computes `n` automatically by looking at existing tags for the current month — you don't need to (and shouldn't) specify a version manually.

## Who Can Run a Release

Any repository collaborator with write access can *trigger* the workflow, but the job will not actually run until it is approved by a member of the **wp2-leads** team. This is enforced by the `release` GitHub Environment (Settings → Environments → `release`), which lists `wp2-leads` as a required reviewer.

When you trigger the workflow, it will sit in a "Waiting" state in the Actions run until someone from `wp2-leads` approves it from the run's page.

## How to Run a Release

1. Make sure `main` has everything you want in the release — the workflow always builds from the tip of `main`.
2. Go to the repository's **Actions** tab → **Release documentation** workflow → **Run workflow** → confirm on the `main` branch.
   Alternatively, with the [GitHub CLI](https://cli.github.com/): `gh workflow run release.yml`.
3. Wait for a `wp2-leads` member to approve the run (or, if you are one, approve it yourself from the run's page).
4. Once approved, the workflow runs automatically end-to-end — no further action needed.

## What the Release Process Does

In order:

1. Computes the next `v<yyyymm>.<n>` version number.
2. Creates and pushes a git tag for that version.
3. Builds the site with `mkdocs build --clean`.
4. Zips the built site and attaches it to a new GitHub Release for that tag (with auto-generated release notes).
5. Publishes the built site via [`mike`](https://github.com/jimporter/mike), which:
   * Adds the new version to the version dropdown on the live site.
   * Updates the `latest` alias to point at this new version.

## Where to Find a Released Version

* **Live site**: the version dropdown in the site header lets you switch between all published versions. `latest` (the default) always points at the most recently released version.
* **GitHub Releases**: each version has a corresponding [release](../../releases) with a `documentation-v<yyyymm>.<n>.zip` asset — a self-contained, downloadable copy of that version's built site for offline browsing.
* **Git tags**: each version is also a plain git tag (`git tag -l`), pointing at the exact commit on `main` it was built from.

## Running Two Releases in the Same Month

Just run the workflow again. The version number automatically increments (`v202607.1` → `v202607.2`, etc.); both versions remain available in the dropdown and as separate GitHub Releases.

## Troubleshooting

* **The workflow run is stuck on "Waiting"**: it needs approval from a `wp2-leads` member — see [Who Can Run a Release](#who-can-run-a-release).
* **The new version doesn't appear on the live site right after the run finishes**: GitHub Pages can take a minute or two to rebuild and its CDN to refresh; a hard refresh usually resolves it.
* **You need to change who can approve releases**: update the required reviewers on the `release` environment under Settings → Environments → `release`.
