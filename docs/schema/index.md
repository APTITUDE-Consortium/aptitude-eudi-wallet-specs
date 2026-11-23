# Attestation Schemas

This section contains candidate schema definitions for the APTITUDE pilot. Their review status, scope and constraints are defined by the corresponding rulebook; publication here does not imply approval or production readiness.

The RB05 v0.1 artefacts below accompany the [Biometric Profile Attestation draft rulebook](../rulebook/wp4/RB05_BIOMETRIC_PROFILE_RULEBOOK_v0.1.md). They describe the complete set of namespace values, not a signed mdoc or a selectively disclosed presentation. Both examples use synthetic identities and non-biometric payload bytes.

| Document | Description |
|----------|-------------|
| [RB05 CDDL](wp4/rb05-biometric-profile.cddl) | Candidate structure for the complete RB05 namespace values. |
| [RB05 JSON Schema](wp4/rb05-biometric-profile.schema.json) | Non-normative JSON review projection of the candidate namespace model. |
| [RB05 synthetic JSON example](wp4/rb05-example-protected-template.json) | Readable example of the namespace values; not a signed credential. |
| [RB05 synthetic CBOR diagnostic example](wp4/rb05-example-semantic.diag) | Textual CBOR representation of the same synthetic namespace values. |
