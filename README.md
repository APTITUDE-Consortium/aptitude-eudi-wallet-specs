# APTITUDE Technical Specifications and RFCs

This repository contains the technical requirements and RFC documentation for the APTITUDE project, which pilots the European Digital Identity Wallet (EUDI Wallet).

Published specifications are available on [GitHub Pages](https://aptitude-consortium.github.io/aptitude-eudi-wallet-rfcs/).

## Repository structure

This repository uses MkDocs to build documentation from the `/docs/` folder. The generated site is available at [APTITUDE Technical Specification](https://aptitude-consortium.github.io/aptitude-eudi-wallet-rfcs/).

- `/docs/` - Documentation sources (rulebooks, standards, glossaries, images, and media)
  - `/docs/rulebook/` - Attestation rulebooks
  - `/docs/img/` - Images and diagrams
  - `/docs/media/` - CSS and style assets
  - `/docs/overrides/` - MkDocs theme customizations
- `/reference/` - Git submodules with upstream rulebooks and specifications ([Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules))
- `mkdocs.yml` - MkDocs configuration
- `/script/` - Helper maintenance scripts

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on proposing and merging changes.

See [github-coediting-workflow.md](github-coediting-workflow.md) for an introduction to the GitHub co-editing workflow.

## Funding

![image](docs/img/eu-cofunded.png)

The project is co-funded by the European Union. However, the views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority. Neither the European Union nor the granting authority can be held responsible.

## Licensing

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. The IP is handled as part of the EWC IP agreement. Please note that some of the RFCs (Like payments) are not based on Apache 2.0 license.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the [LICENSE](LICENSE) for the specific language governing permissions and limitations under the License.
