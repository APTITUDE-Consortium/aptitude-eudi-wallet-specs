# Definition of Done for Rulebooks

This document defines the acceptance criteria that a Rulebook must satisfy before being considered complete and ready for review. It provides a common reference for assessing the completeness, consistency and quality of the artefact.

### Scope & Purpose

- The purpose of the credential is clearly defined:
  - The document explicitly states the business problem addressed by the credential.
  - The document explicitly states the objective of the credential.
  - The intended users and/or relying parties are identified.
- The intended usage scenarios are documented:
  - At least one supported use case is described.
  - Preconditions for using the credential are documented (if applicable).
  - Usage limitations are documented (if applicable).
- The business context is described:
  - The application domain is identified (e.g. travel, automotive, education).
  - The operational context in which the credential is intended to be used is described.
  - Relationships with other credentials, systems or business processes are documented (if applicable).

### Lifecycle & Actors

- Actors are identified:
  - Issuer is identified.
  - Holder is identified.
  - Verifier is identified.
- Issuance requirements are documented:
  - The issuing authority is identified.
  - Required input information for issuance is documented.
  - Preconditions for issuing the credential are documented.
  - The issuance workflow is described.
- Presentation requirements are documented:
  - Supported presentation method(s) are identified.
  - Required information to be presented is documented.
  - Rules governing selective disclosure of credential attributes are documented (if applicable).
- Verification requirements are documented:
  - Verification inputs are identified.
  - Verification checks are described.
  - Expected verification outcome is documented.
  - Failure conditions are documented (if applicable).
- Usage constraints are documented:
  - Credential validity period is defined.
  - Usage limitations are documented.
  - Environmental or operational constraints are documented (if applicable).

### Attribute Definition

- Mandatory attributes are defined.
- Optional attributes are defined.
- Conditional attributes are defined (fields that become mandatory only under specific conditions, e.g. field B is required when field A is set).
- Mandatory metadata are defined.
- Optional metadata are defined.
- Conditional metadata are defined (if applicable).
- Each attribute includes:
  - `identifier` — technical field name used in the encoding.
  - `definition` — human-readable business description.
  - `data type` — e.g. string, boolean, date, integer.
  - `example value` — a concrete, realistic value.

### Trust

- Trust anchor requirements are documented:
  - Trust anchor(s) are identified.
  - Trust source or trust list is identified.
  - The mechanism used to validate the trust chain is described.
- Revocation/status handling is documented:
  - Revocation mechanism is described (if applicable).
  - Credential status validation process is documented.
  - Justification is provided when revocation is not applicable.

### Encoding

- Credential format is identified:
  - Supported credential format(s) are explicitly identified (e.g. `mdoc`, `SD-JWT VC`).
  - The corresponding specification or standard is referenced.
- Encoding requirements are documented:
  - Encoding rules for attributes are documented.
  - Character encoding requirements are documented (e.g. UTF-8).
  - Serialization or encoding format requirements are documented (e.g. CBOR).
  - Applicable encoding standards are referenced (e.g. ISO/IEC 18013-5).
- Credential namespace is defined:
  - The credential namespace is explicitly identified.
  - Attribute identifiers are consistent with the defined namespace.
- At least one encoding example is provided:
  - The example conforms to the defined encoding rules.

### Compliance & Standards Alignment

- Compliance requirements are documented:
  - Applicable compliance obligations are identified.
  - Compliance requirements are traceable to the applicable regulations or standards.
- Applicable standards are referenced (e.g. ISO/IEC 18013-5, RFC 7519):
  - Standards are explicitly listed.
  - Normative references are provided.
- Applicable regulations are referenced:
  - Regulatory references are explicitly listed.
- Deviations from standards are documented and justified:
  - Each deviation is explicitly identified.
  - The rationale for the deviation is documented.

### Traceability

- References to the related Attestation Schema are provided.
- References to related RFCs are provided (if applicable).
- References are valid and consistent with the corresponding artefacts.

### Governance

- All TODOs and TBDs are resolved.
- Review comments are addressed:
  - All review comments have been resolved or explicitly justified.
- Owner approval is received.
- Reviewer approval is received.
