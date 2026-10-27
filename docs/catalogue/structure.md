# Structure of the catalogue

Rulebooks and data schemas follow one structure, so that authors know where each artefact lives, reviewers can apply the [definitions of done](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/tree/main/definition_of_done) in the same way, and tools read the tree without per-type configuration.

## Layout

```text
docs/catalogue/
  rulebooks/
    rb-<slug>/
      README.md              the rulebook of the attestation type
      img/                   images and samples of the rulebook, if any
  data-schemas/
    sd-jwt/<slug>-sd-jwt.json    SD-JWT VC payload schema
    mdoc/<slug>-mdoc.json        mdoc schema, if the type has an mdoc encoding
    sd-jwt/sample-data/          optional sample payloads
  assets/
    <slug>/card.svg              card artwork, optional
    <slug>/card-dark.svg         dark variant, optional
    <slug>/logo.svg              logo, optional
  _template/                     skeletons for new types; not published
```

The `<slug>` is lower-case words joined by hyphens. It names the attestation type and is the same in the rulebook folder, in the data schema file names and in the assets folder. A leading `dsNNN-` number is accepted in schema file names and ignored in the slug.

## Rulebooks

- A rulebook is `rulebooks/rb-<slug>/README.md`. The folder holds the images and samples that the rulebook uses.
- The chapters follow the [definition of done for rulebooks](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/definition_of_done/Definition_of_done_Rulebook.md): 1 Introduction, 2 Attestation attributes and metadata, 3 Attestation encoding, 4 Attestation usage, 5 Trust anchors, 6 Revocation, 7 Compliance, 8 References. The skeleton in `_template/rulebook/README.md` has them.
- Every attribute has an `identifier`, a `definition`, a `data type` and an `example value`, and is mandatory, optional or conditional.
- The normative key words are SHALL, SHALL NOT, SHOULD and SHOULD NOT, as in the contributing guide.
- Rulebooks keep their version table and author list in the document.

## Data schemas

- A data schema is JSON Schema 2020-12 and meets the [definition of done for attestation schemas](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/definition_of_done/Definition_of_done_Attestation_schema.md): `$schema`, `title` and `description` at the root, `required` for mandatory attributes, `format`, `pattern`, length bounds and enumerations where they apply, and examples.
- The SD-JWT VC schema describes the payload as flat top-level claims. `properties.vct.const` holds the credential type identifier, and `version` holds the semantic version of the schema.
- The standard claims `iss`, `iat`, `nbf`, `exp`, `cnf` and `status` are optional properties. `status` has the Token Status List shape `{"status_list": {"idx": 0, "uri": "https://..."}}`.
- The `vct` of a new type is `eu.aptitude.<slug>.1`. A type defined by another body keeps its identifier, and a type that exists in another catalogue with the same identifier gets an `aptitude` domain, for example `urn:eudi:pid:aptitude:1`.
- Dates use `format: date` or `format: date-time`, countries are ISO 3166-1 alpha-2 and currencies are ISO 4217, each with a `pattern` that enforces the form.
- Nested objects are allowed. The registry lists one nested level as child claims; deeper levels stay in the schema for validation.

## Assets

A card is an SVG of 400 by 252 units with a title and up to five claims as `{{claim}}` placeholders, where nested claims are `{{parent.child}}`. It is self-contained and consists of shapes and text; scripts, styles, embedded images, `data:` URIs and external references are outside the card format. Text and background have a contrast of at least 4.5:1.

## Ownership

Each rulebook folder has a line in `.github/CODEOWNERS` that names the work package team, for example `/docs/catalogue/rulebooks/rb-<slug>/ @APTITUDE-Consortium/wp<N>-code-owners`. The data schemas and assets of the type have the same owner.

## Adding an attestation type

1. Run `python script/new_catalogue_entry.py <slug> "<Title>"`. It creates the rulebook, the SD-JWT schema and the card from `_template/`.
2. Write the rulebook and the schema together, so that every attribute of the rulebook is a property of the schema and the reverse.
3. Add the CODEOWNERS line.
4. Run `python script/validate_catalogue.py` and fix what it reports.
5. Open a pull request. The `Catalogue` check validates the tree and builds it with registry-cli.

## Checks

`script/validate_catalogue.py` validates the tree: valid JSON; JSON Schema 2020-12; the root keys `$schema`, `title`, `description` and `version`; a string `properties.vct.const` for SD-JWT VC schemas; `required` entries that exist in `properties`; file and folder names; a rulebook for every schema and a schema for every rulebook; and the card rules. It prints warnings for rulebooks without the standard chapters and for schemas without examples, and `--strict` turns warnings into errors.

The `Catalogue` workflow runs the validator and builds the tree with registry-cli, and the site build renders the rulebooks and lists the types on the [catalogue page](index.md).
