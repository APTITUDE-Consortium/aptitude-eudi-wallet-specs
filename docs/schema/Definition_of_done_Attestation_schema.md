# Definition of Done

## Attestation Schema

### Coverage & Traceability

- All Rulebook attributes are represented in the schema
- No undocumented attributes are included
- Consistency with the Rulebook has been verified

### Attribute Definition

*For each attribute:*

- `identifier` is defined (field name)
- `data type` is defined (e.g. `"type": "string"`)
- `format` is defined where applicable (e.g. `"format": "date"`)
- Required/optional status is defined (mandatory fields are listed in the `required` array)
- Constraints are defined where applicable (e.g. `"minLength": 2`, `"maxLength": 150`, `"pattern"`)

### Validation

- Enumerations are defined where applicable (e.g. a status field that only accepts `"active"` or `"inactive"`)
- Validation constraints are defined where applicable (e.g. if `status = "partial"` then field B is required)

### Technical Quality

- Schema metadata is present at root level:
  - `$schema` — declares the JSON Schema version (e.g. `"https://json-schema.org/draft/2020-12/schema"`)
  - `title`
  - `description`
- Schema is syntactically valid (well-formed JSON, no syntax errors)
- All `$ref` references are resolvable
- Schema passes a JSON Schema validator
- Example payload is provided (e.g. `"family_name": "Rossi"`, `"date_of_birth": "1990-01-01"`)

### Governance

- Review comments are addressed
- Technical review is completed
- Owner approval is received
- Reviewer approval is received
