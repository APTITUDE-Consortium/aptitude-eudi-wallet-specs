# APTITUDE Technical Specifications and RFCs

This repository contains the technical requirements and RFC documentation for the APTITUDE project, which pilots the European Digital Identity Wallet (EUDI Wallet).

Published specifications are available on [GitHub Pages](https://aptitude-consortium.github.io/aptitude-eudi-wallet-specs/).

## Repository structure

This repository uses MkDocs to build documentation from the `/docs/` folder. The generated site is available at [APTITUDE Technical Specification](https://aptitude-consortium.github.io/aptitude-eudi-wallet-specs/).

- `/docs/` - Documentation sources included in the published site
  - `/docs/horizontal-RFCs/` - RFC documents and index pages
  - `/docs/rulebook/` - Rulebooks, including `/docs/rulebook/wp2-trust-specifications/`
  - `/docs/img/` - Images and diagrams
  - `/docs/media/` - CSS and frontend assets
  - `/docs/overrides/` - MkDocs theme customizations
- `/reference/` - Git submodules with upstream rulebooks and specifications ([Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules))
  - `/reference/eid-wallet-it-docs/`
  - `/reference/eudi-doc-architecture-and-reference-framework/`
  - `/reference/eudi-doc-attestation-rulebooks-catalog/`
  - `/reference/eudi-doc-standards-and-technical-specifications/`
  - `/reference/ewc-eudi-wallet-rulebooks-and-schemas/`
  - `/reference/webuild-wp4-architecture/`
- `/script/` - Helper maintenance scripts
- `/.github/workflows/` - CI jobs for linting, pages publishing, and submodule updates
- `mkdocs.yml` - MkDocs configuration
- `/site/` - Generated static output (build artifact)

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on proposing and merging changes.

See [github-coediting-workflow.md](github-coediting-workflow.md) for an introduction to the GitHub co-editing workflow.

## Difference Between Rulebook, RFCs, and Schemas

To keep this repository maintainable and avoid unnecessary document proliferation, the following distinction applies.

### Rulebook

The Rulebook is the human-readable and descriptive source of truth for an attestation profile.
It describes content and form of the attestation and typically includes:

1. ARF-related topics and profile context.
2. Level of assurance.
3. Applicable legal, sector, and technical standards.
4. References to the relevant data schema and, when needed, use case manuals.

If the required protocols are already covered by horizontal RFCs, credential profiling should be documented directly in the Rulebook.
Primary audience: business and service designers integrating attestations into application processes.

### Attestation Schema (Schema)

The Attestation Schema is the machine-readable counterpart of the Rulebook.
It is expressed as a JSON Schema that defines the credential attribute structure so software components, wallets, and test beds can process it automatically.
Primary audience: software developers, conformance test tools integrators.

### RFCs

An RFC is a technical specification focused on implementation for the APTITUDE pilot.
Primary audience: developers and teams configuring interoperability and conformance testing platforms.
Horizontal RFCs define protocol profiles that apply across all APTITUDE use cases and attestation types.
Vertical RFCs should exist only when a credential needs protocol mechanisms that are not already covered by horizontal RFCs and that may be reusable across other use cases.

Typical RFC objectives in this repository:

1. Define technical implementation specifications, either cross-cutting or specific to a work package or domain use case.
2. Clarify pilot reference choices (for example selected protocol versions and implementation profiles).
3. Define what must be verified for interoperability and conformance, including expected inputs and outputs.
4. Document pilot-specific compromises and explicit exclusions compared with ARF or other technical specifications.

Examples of topics that may require RFC treatment:

1. Issuance and presentation implementation details for pilot scope.
2. Credential revocation handling.
3. Proximity presentation and related conformance checks.
4. Transaction authorization and payment-related integrations.
5. Trust evaluation implementation by wallet, issuer, or verifier, including mandatory versus optional controls.

## Funding

![image](docs/img/eu-cofunded.png)

The project is co-funded by the European Union. However, the views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority. Neither the European Union nor the granting authority can be held responsible.

## Licensing

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. The IP is handled as part of the EWC IP agreement. Please note that some of the RFCs (Like payments) are not based on Apache 2.0 license.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the [LICENSE](LICENSE) for the specific language governing permissions and limitations under the License.
