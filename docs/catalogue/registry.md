# Publishing in the registry

The tree under `docs/catalogue` is the input of the `rulebook-catalog` layout of registry-cli. The registry builds every attestation type of the tree and publishes its metadata, rulebook and card.

## Source entry

```yaml
sources:
  - url: "git:https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs.git"
    organization: "aptitude-consortium"
    layout: "rulebook-catalog"
    path: "docs/catalogue"
    options:
      attestation_los: "iso_18045_high"   # TS11 level of security for the whole catalogue
      binding_type: "key"                 # TS11 binding type for the whole catalogue
```

The entry goes into `sources.yaml` of [registry.siros.org](https://github.com/sirosfoundation/registry.siros.org). The registry rebuilds every six hours.

## What is published

| Input | Output |
| --- | --- |
| `data-schemas/sd-jwt/<slug>-sd-jwt.json` | `/<org>/<slug>.vctm.json` (SD-JWT VC type metadata), the catalogue entry and its claims |
| `data-schemas/mdoc/<slug>-mdoc.json` | `/<org>/<slug>.mdoc.json` |
| `rulebooks/rb-<slug>/README.md` | `/<org>/<slug>/rulebook.html` and the TS11 `rulebookURI` |
| `assets/<slug>/card.svg`, `card-dark.svg`, `logo.svg` | `svg_templates` and the logo in the display metadata |

The TS11 API lists the attestation types that have a rulebook. An attestation type needs an SD-JWT VC schema to appear in the registry.

## Checking a build

```bash
go install github.com/sirosfoundation/registry-cli/cmd/registry-cli@v0.18.0
cp -r docs/catalogue /tmp/aptitude-catalogue
printf 'sources:\n  - url: "file:///tmp/aptitude-catalogue"\n    organization: "aptitude-consortium"\n    layout: "rulebook-catalog"\n' > /tmp/sources.yaml
registry-cli build --sources /tmp/sources.yaml --output /tmp/aptitude-out
```

registry-cli writes generated files next to a local source, so the build runs on a copy.
