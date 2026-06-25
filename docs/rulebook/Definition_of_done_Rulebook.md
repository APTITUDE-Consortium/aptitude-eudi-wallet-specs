# Definition of Done

## Rulebook

### Scope & Purpose

- The purpose of the credential is clearly defined (e.g. *what need does it address and for whom?*)
- The intended usage scenarios are documented (e.g. border control, hotel check-in, delegation)
- The business context is described

### Lifecycle & Actors

- Issuer is identified
- Holder is identified
- Verifier is identified
- Issuance requirements are documented (prerequisites, process, and conditions for issuing the credential)
- Presentation requirements are documented (how and in which context the credential is presented)
- Verification requirements are documented (what the verifier must check to accept the credential)
- Usage constraints are documented (e.g. 24h validity, single use, geographic restrictions)

### Attribute Definition

- Mandatory attributes are defined
- Optional attributes are defined
- Conditional attributes are defined (fields that become mandatory only under specific conditions, e.g. field B is required when field A is set)
- Mandatory metadata are defined
- Optional metadata are defined
- Conditional metadata are defined (if applicable)
- Each attribute includes:
  - `identifier` — technical field name used in the encoding
  - `definition` — human-readable business description
  - `data type` — e.g. string, boolean, date, integer
  - `example value` — a concrete, realistic value

### Trust

- Trust anchor requirements are documented (who signs the credential? which entity is considered trusted and how is it verified?)
- Revocation/status handling is documented, or non-applicability is explicitly justified (e.g. short-lived credentials do not require revocation because they expire within 24h)

### Encoding

- Credential format is identified (e.g. `mdoc` / ISO 18013-5, `SD-JWT VC` / OpenID)
- Encoding requirements are documented — explicit rules on how attributes must be encoded, for example:
  - *All string values SHALL be UTF-8 encoded*
  - *Canonical CBOR encoding SHOULD be used*
  - *The credential SHALL be ISO/IEC 18013-5 compliant*
- Credential namespace is defined (e.g. `eu.europa.ec.eudiw.mvrc.delegation_permission.1`)
- At least one encoding example is provided

### Compliance & Standards Alignment

- Compliance requirements are documented (e.g. eIDAS 2.0, ARF, ICAO 9303)
- Applicable standards are referenced (e.g. ISO/IEC 18013-5, RFC 7519)
- Applicable regulations are referenced
- Deviations from standards are documented and justified

### Traceability

- Related Attestation Schema is identified
- Related RFCs are identified (if applicable)

### Governance

- All TODOs and TBDs are resolved
- Review comments are addressed
- Owner approval is received
- Reviewer approval is received
