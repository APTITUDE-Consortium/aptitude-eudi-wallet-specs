# RB05 — Biometric Profile Attestation Rulebook

**Status:** Draft proposal v0.1 — for discussion, not approved\
**Date:** 3 September 2026\
**Alignment revision:** 8 September 2026 — no partner decision implied\
**Editorial revision:** 11 September 2026 — review-package preparation; technical model unchanged\
**Author:** Hedi Hidouri, IN Groupe\
**Governance:** Formal owner and approvers remain to be confirmed under RB05-D14\
**Intended reviewers:** IN Groupe biometric/security team, Marseille Airport, the Wallet Provider to be confirmed, WP2 trust/protocol leads, WP4/GRNET, WP7/legal and data-protection representatives

| Version | Date | Description |
| --- | --- | --- |
| 0.1 | 2026-09-03 | Structured proposal for review of the APTITUDE UC9 Biometric Profile Attestation |
| 0.1, alignment revision | 2026-09-08 | Align candidate source eligibility and distinguish D4.1's Ready-to-Travel route from the proposed direct-RB05 route; clarify storage and identity-field decisions; semantic schema unchanged |
| 0.1, editorial revision | 2026-09-11 | Prepare the discussion package, supporting-file links and RFC references; semantic schema and proposed behaviour unchanged |

> This version is complete enough for architectural, privacy, security and interoperability review. It deliberately does not claim production readiness. The identifiers, protected-template profile, trust-list location, status-list location and governance approvals listed in Appendix B must be fixed before a production implementation can claim conformance.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook proposes a device-bound, holder-controlled RB05 Biometric Profile Attestation to support voluntary facial verification at airport touchpoints. It specifies a protected facial-reference credential and, for the proposed direct-RB05 route, its presentation to an authorised checkpoint for one-to-one comparison with a live facial sample. Section 1.7 distinguishes that candidate route from the Ready-to-Travel route already described in D4.1.

The attestation addresses a narrow problem: reusing a facial reference generated from a previously verified identity portrait without placing a reusable biometric database under the control of an airport, airline or issuer. In the APTITUDE UC9 pilot, IN Groupe is the proposed Attestation Provider and Marseille Airport is the proposed operational Relying Party. Those legal and technical roles remain subject to formal confirmation.

RB05 attests that:

1. the issuer generated the protected facial reference, or caused an approved processor to generate it within the issuer's controlled issuance process, using a valid trusted source credential containing an authenticated portrait;
2. the protected reference belongs to the named RB05 subject;
3. the attestation is bound to the Wallet Unit key represented in the mdoc Mobile Security Object (MSO); and
4. the protected reference is permitted only for transaction-bound one-to-one facial verification under the controls in this Rulebook.

RB05 is **not**:

- a PID, PhotoID, passport or Digital Travel Credential (DTC);
- a boarding pass, ticket, flight entitlement or boarding authorisation;
- the UC9 “Ready to Travel” object;
- a record of a biometric comparison result;
- a raw portrait or face image;
- permission to perform one-to-many identification, watch-list matching, surveillance, analytics or model training; or
- evidence that every deployment is automatically compliant with data-protection or AI legislation.

Credential validation, biometric verification and travel authorisation are three separate decisions. A valid RB05 proves issuer-signed credential data. A successful one-to-one comparison is a biometric decision under the approved PAD, matcher and threshold, with documented error rates; it does not by itself prove identity or travel entitlement. Validated travel-entitlement evidence and the airport/airline business rules determine whether the traveller may proceed. Separating these decisions does not require two credentials or two presentation interactions at the checkpoint.

This draft adopts a traveller-held Wallet design as a candidate under RB05-D02 and RB05-D12. D4.1 refers both to the EUDI Wallet and to issuance/storage in the Marseille Airport application; it does not establish an unambiguous equivalence between those components. D4.2 must document the agreed component roles and storage model. The candidate does not define an airline-held or airport-held central biometric record, and does not claim that its interpretation of “carrier-held biometrics” has been agreed.

### 1.2 Legal category and document status

RB05 v0.1 is provisionally classified as a **non-qualified EAA**, subject to confirmation by APTITUDE governance and WP7/legal. It is not represented as a QEAA, a PuB-EAA or an official Commission-registered Rulebook.

For the ISO mdoc encoding, the `category` data element SHALL NOT be present. ETSI TS 119 472-1 V1.2.1, requirement EAA-6.2.2.1-01, prohibits `category` for an EU mdoc EAA that is neither a QEAA nor a PuB-EAA. In particular, the non-standard value `eaa:eu:non-qualified` SHALL NOT be encoded.

This conflicts with wording in the EU Attestation Rulebook Template v1.5 and with ARF v3.0.0 requirements ARB_12/ARB_25. The incorporated ETSI rule is followed in this draft, and the upstream inconsistency is recorded as decision RB05-D01. If RB05 is later classified as a QEAA or PuB-EAA, its issuer qualification, trust model, schema and category treatment must be revised before issuance.

### 1.3 Supported format and profiles

RB05 v0.1 supports one credential format and one biometric use profile:

- **Credential format:** ISO/IEC 18013-5 mdoc, with the general non-mDL EAA data elements profiled by ETSI TS 119 472-1 and ISO/IEC 23220-2.
- **Biometric modality:** face.
- **Biometric operation:** one-to-one verification only.
- **Biometric representation:** a protected facial-template payload identified by an approved format, protection and matcher profile. Cancellability, renewability and linkability properties remain subject to profile evidence and RB05-D05/RB05-D17.
- **Storage model:** holder-controlled Wallet Unit; no issuer-, airline- or airport-controlled reusable biometric database.

SD-JWT VC and W3C Verifiable Credentials Data Model encodings are not defined by v0.1. A raw image profile and an indirect pointer to an external biometric database are not defined.

### 1.4 Document structure

- Chapter 2 defines the attributes and metadata.
- Chapter 3 defines the mdoc encoding and schema rules.
- Chapter 4 defines issuance, presentation, verification and lifecycle behaviour.
- Chapter 5 defines trust requirements.
- Chapter 6 defines status and revocation.
- Chapter 7 defines security, privacy and biometric controls.
- Chapter 8 records standards alignment, deviations and traceability.
- Appendix A lists conformance requirements.
- Appendix B lists decisions that block production use.

### 1.5 Key words

The capitalised key words SHALL, SHALL NOT, SHOULD, SHOULD NOT and MAY are to be interpreted as described in RFC 2119 and RFC 8174.

In this v0.1 proposal, those words express the proposed conformance requirements to apply after consortium approval; they do not imply that APTITUDE or any partner has already approved the proposal.

### 1.6 Terminology

- **Attestation Provider / issuer:** the entity that validates the enrolment result and signs RB05.
- **Holder / traveller:** the person to whom RB05 relates and who controls its presentation through a Wallet Unit.
- **Wallet Unit:** the holder-controlled component that receives, stores and presents RB05 and controls the device-bound private key.
- **Relying Party / verifier:** an authorised airport component that requests and validates RB05 for a declared purpose.
- **Biometric reference:** the protected facial representation inside RB05. It remains biometric personal data even when encrypted, transformed or cancellable.
- **Live sample:** a facial sample captured at a checkpoint for presentation-attack detection (PAD) and one-to-one comparison.
- **Protected-template profile:** a versioned specification defining payload syntax, template protection, keys, matching, thresholds, size and failure behaviour.
- **Source credential:** an approved PID with an available authenticated portrait, PhotoID or DTC profile used during enrolment under RB05-D22. The candidate list is not a production allowlist. The source credential is not copied into RB05.
- **Wallet Instance Attestation (WIA):** evidence about the Wallet instance and its provider/lifecycle state used during issuance.
- **Key Attestation (KA):** evidence about a target credential key and its protected key-storage environment.
- **Wallet Unit Attestation (WUA):** the current regulatory set/construct comprising one or more WIAs and one or more KAs; it is not assumed to be one serialized object. For device-bound RB05 issuance, both required artefact types must validate. RB05-D10 must map this current terminology to the endpoint fields in the incorporated ETSI profile, which uses legacy `WUA` terminology differently at the Credential Endpoint.

### 1.7 Relationship with D4.1 and the D4.2 implementation design

This document provides a candidate contribution to D4.2. [D4.1 Annex A.9](https://github.com/APTITUDE-Consortium/wp4-use-cases/blob/dbf7d7a2b1cbe46f1221cf8d14743462695fecab/D4.1/Annex-A.9--UC9-Biometric-Profile-Carrier-Held-Biometrics-for-Seamless-Airport-Travel--INGroupe.md) remains the reference for the existing UC9 scenario. The [D4.2 roadmap](https://github.com/APTITUDE-Consortium/wp4-use-cases/blob/dbf7d7a2b1cbe46f1221cf8d14743462695fecab/D4.1/10.3--Roadmap-Towards-D4.2-Implementation-Manual--GRNET.md) calls for implementation artefacts based on that scenario. Proposed changes require an explicit UC9 decision; D4.2 is not required to adopt this candidate unchanged.

| Topic | D4.1 description | Candidate position and decision |
| --- | --- | --- |
| Portrait source | PID with portrait, PhotoID and/or DTC. | Retain all three as candidate sources; exact accepted profiles, portrait availability/quality and assurance remain under D22. |
| Storage | References to both the EUDI Wallet and the airport application; Ready-to-Travel is described as stored in the airport application. | Holder-controlled Wallet Unit proposed for this RB05 profile; confirm component roles and any required profile revision under D02/D12/D19. |
| Airport flow | Associate the Biometric Profile Attestation with boarding data to issue Ready-to-Travel, then present Ready-to-Travel or the biometric QR option. | Preserve this as route R1; record direct RB05 plus travel-entitlement evidence as alternative R2. Select and specify the integration under D12/D18. |
| Identity fields | Biometric Profile includes names, birth date, nationality and a document/attestation-type indication. | Candidate namespace model retains names and excludes the other source attributes. Justify or revise the field selection under D11; this is not an agreed correction to D4.1. |

**R1 — D4.1 Ready-to-Travel route.** A validated portrait source is used to create the Biometric Profile Attestation. That attestation is subsequently associated with boarding information to issue a separate Ready-to-Travel attestation. The latter carries identity, biometric and travel data in the D4.1 description and is used at the checkpoint, with a biometric QR option also described. D4.1's description does not by itself establish a complete interoperable encoding or validation profile for either mechanism.

If R1 is retained, D12/D18 must specify the authorised association process, evidence linking the biometric profile to the traveller and travel entitlement, derived-credential issuer, storage, protection, disclosure, validity/status dependencies and checkpoint verification. Reuse of a protected RB05 reference in Ready-to-Travel requires the protection/profile owners' approval, including purpose, key domain and retention. It is not automatically permitted or proven by this Rulebook. A Ready-to-Travel credential containing travel data is not an RB05 instance and SHALL NOT be validated against the RB05-only namespace schema.

**R2 — proposed direct-RB05 route.** The traveller presents RB05 to the checkpoint, which validates the attestation and performs the approved one-to-one comparison. The operational decision also uses independently validated travel-entitlement evidence. D12/D18 must define the same-traveller and fresh-transaction binding. An approved combined presentation or other agreed protocol may be used; this proposal does not require two user interactions.

The normative data model in Chapters 2–3 describes the proposed RB05 credential in either case. The detailed checkpoint presentation/matching flow in Sections 4.4–4.7 describes R2. For R1, controls applicable when RB05 is consumed during association and the distinct Ready-to-Travel/QR checkpoint controls must be specified under D12/D18 before that route can claim conformance. Documenting R1 does not silently extend RB05's permitted recipients, storage or reference-reuse policy. A route-specific revision is required wherever the agreed R1 implementation differs from this candidate. Tests for an unselected route are recorded as not applicable, with a decision reference, rather than as passed.

## 2 Attestation attributes and metadata

### 2.1 Data-model requirements

| ID | Requirement |
| --- | --- |
| RB05-AE-01 | RB05 SHALL contain only issuer-signed data that is necessary to identify the attestation subject and perform the approved one-to-one facial verification. |
| RB05-AE-02 | RB05 SHALL contain exactly one `biometric_reference` and its modality SHALL be `face`. |
| RB05-AE-03 | The permitted verification mode SHALL be `one_to_one`. A verifier SHALL reject any other value. |
| RB05-AE-04 | RB05 SHALL NOT contain a raw portrait, live image, video, unprotected template or reversible source image. |
| RB05-AE-05 | RB05 SHALL NOT contain flight number, airline, departure time, seat, booking reference, boarding status or another travel entitlement. |
| RB05-AE-06 | RB05 SHALL NOT contain an audience attribute. Relying-party and purpose restrictions SHALL be enforced through relying-party registration, request policy and reader authentication. |
| RB05-AE-07 | RB05 SHALL NOT contain source-credential evidence, a source-document number, a source portrait hash or a source-expiry copy. Source validation belongs to the issuance process. Any minimal issuer-side dependency record is separate from RB05 and must comply with RB05-D20. |
| RB05-AE-08 | RB05 SHALL NOT contain `category` while it remains a non-qualified EAA. |
| RB05-AE-09 | The tuple (`format_id`, `format_version`, `protection_profile_id`, `matcher_profile_id`) SHALL be immutable, versioned and registered as one approved compatible combination. A verifier SHALL NOT compose a tuple from identifiers that are individually known but not jointly approved. |
| RB05-AE-10 | The protected payload SHALL be disclosed atomically with its modality, verification mode and profile identifiers as one `biometric_reference` map. |

### 2.2 Mandatory attributes

| Data identifier | Definition | Type | Example |
| --- | --- | --- | --- |
| `family_name` | Current family name of the identified holder, derived only from the authenticated source field using the exact D22-approved mapping and Unicode-normalisation rule; no silent truncation, transliteration or lossy change is permitted. | non-empty Unicode text; exact ISO/IEC 23220-2 constraint to be confirmed under D10/D11 | `Durand` |
| `given_name` | Current given name(s) of the identified holder, derived only from the authenticated source field using the exact D22-approved mapping and Unicode-normalisation rule; no silent truncation, transliteration or lossy change is permitted. | non-empty Unicode text; exact ISO/IEC 23220-2 constraint to be confirmed under D10/D11 | `Camille` |
| `biometric_reference` | Atomic protected facial-reference map defined in Section 2.2.1. | map | See Section 3.1.5 |

The combination of `given_name`, `family_name` and the RB05 `document_number` implements the identified-subject profile required for a non-mDL mdoc EAA by ETSI TS 119 472-1. Names SHALL NOT be requested at a checkpoint when the authorised purpose can be achieved by requesting only `biometric_reference` and validating the credential.

#### 2.2.1 Mandatory members of `biometric_reference`

| Member | Definition | Type and constraint | Example |
| --- | --- | --- | --- |
| `modality` | Biometric characteristic represented by the payload. | text; fixed value `face` | `face` |
| `verification_mode` | Only biometric operation permitted by RB05. | text; fixed value `one_to_one` | `one_to_one` |
| `reference_type` | Kind of reference in this profile. | text; fixed value `protected_template` | `protected_template` |
| `format_id` | Immutable URI identifying the exact binary template format. | text URI; 1–512 UTF-8 bytes | `urn:example:aptitude:rb05:format:face-template-v1` |
| `format_version` | Version of the binary format. | text; 1–32 UTF-8 bytes | `1.0` |
| `protection_profile_id` | Immutable URI identifying template protection, encryption, key domain, renewal/cancellation and linkability rules. The identifier does not itself prove those properties. | text URI; 1–512 UTF-8 bytes | `urn:example:aptitude:rb05:protection:cancelable-v1` |
| `matcher_profile_id` | Immutable URI identifying feature extraction, comparison, threshold and score interpretation. | text URI; 1–512 UTF-8 bytes | `urn:example:aptitude:rb05:matcher:face-v1` |
| `payload` | Protected facial-reference bytes. The bytes SHALL conform to all three registered profiles above. | CBOR `bstr`; 1–16,384 bytes in v0.1 | synthetic bytes only in examples |

The proposed 16 KiB limit must be validated using representative payloads from the biometric implementation under RB05-D04 before production. The example URNs use the reserved `example` namespace and identify no real algorithm.

### 2.3 Optional attributes

No optional biometric attribute is defined in v0.1. Implementations SHALL NOT add undeclared members to `biometric_reference`. A precise template-generation timestamp is deliberately not disclosed: no matcher need has been demonstrated, and a stable exact timestamp would add correlation risk. The administrative `issue_date` and MSO validity control credential age.

### 2.4 Conditional attributes

No conditional attribute is defined in the candidate v0.1 schema. Excluding `birth_date`, `nationality` and the source document/attestation type is a minimisation proposal, not an agreed change to the UC9 dataset. Those fields are not inputs to the facial comparison itself, but the pilot may have a separate justified operational need. RB05-D11 must record the decision for each field, whether it belongs in RB05 or another agreed artefact, and its disclosure policy. If the approved dataset changes, the Rulebook, CDDL, JSON Schema, examples and affected tests must be revised together before claiming conformance to it.

| Field | Candidate treatment | Operational question for D11 |
| --- | --- | --- |
| `given_name`, `family_name` | Retained in the proposed identified-subject profile; selectively disclosable. | Confirm why a named subject is needed and when a checkpoint actually requests these fields. |
| `birth_date` | Not encoded in the candidate. | Identify any disambiguation or operational need, its necessity and the credential from which it should be obtained. |
| `nationality` | Not encoded in the candidate. | Identify any justified travel-process need and whether it belongs in the travel or identity evidence rather than RB05. |
| Source document/attestation type | Not encoded in the candidate. | Confirm whether issuance audit suffices or an operational use needs a separately specified attribute. |

Pending that decision, the existing candidate schema and examples remain unchanged. Their successful validation proves consistency with this proposed field selection, not approval of that selection by UC9.

### 2.5 Mandatory metadata

| Data identifier | Definition | Type | Example |
| --- | --- | --- | --- |
| `document_number` | Issuer-assigned serial number of this RB05 instance. It SHALL be collision-checked, unique within the issuing authority's RB05 namespace and never reassigned. It SHOULD be opaque and generated with enough entropy to resist enumeration. It SHALL NOT encode or reuse a passport, PID, PhotoID, DTC, booking, flight or loyalty identifier. | non-empty text; exact ISO/IEC 23220-2 constraint to be confirmed under D10 | `BPA-7XQ4-M9VK-2T6P` |
| `issue_date` | Administrative issue date of RB05. | `full-date` | `2026-09-03` |
| `expiry_date` | Administrative end date. At issuance, it SHALL be no later than the earlier of the validated source credential's expiry date and 30 days after `issue_date`. | `full-date` | `2026-10-03` |
| `issuing_authority_unicode` | Legal name of the RB05 issuing authority. The production value must match the trust registration and certificate policy; the example is fictional. | non-empty Unicode text; exact ISO/IEC 23220-2 constraint to be confirmed under D10 | `Example Issuer SAS` |

The 30-day maximum is a proposal for this draft, subject to validation under RB05-D07. Technical validity is separately encoded in `MSO.validityInfo.validFrom` and `validUntil`. D07/D10 shall also cap technical validity at the applicable WIA/KA validity and status-maintenance horizon, or explicitly document and approve a different current-profile rule and its residual risk. Subsequent withdrawal, account closure, relevant source-credential invalidation or post-issuance Wallet/WIA/KA compromise triggers revocation and deletion under Chapter 6; those future events are not encoded into `expiry_date` at issuance.

### 2.6 Optional metadata

No optional metadata is defined in v0.1.

### 2.7 Conditional metadata

No conditional payload metadata is defined in v0.1. In particular, `cryptographically_bound_to` is not used. RB05 is device-bound to its own Wallet Unit key through the MSO; v0.1 does not require a cross-credential attribute that has not yet been confirmed with the Wallet Provider. The transaction-level same-holder mechanism required by RB05-D18 remains outside the RB05 payload.

The ETSI `oneTime` and `shortLived` data elements SHALL both be omitted in v0.1. RB05 is intended for more than one holder-authorised presentation during its validity period and does not use the ≤24-hour short-lived exception. Their absence does not weaken per-presentation freshness requirements and, under ETSI TS 119 472-1 V1.2.1, means revocation status must be checked. Accordingly, a conformant production RB05 SHALL contain the selected status mechanism in the MSO as specified in Chapter 6.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5 mdoc encoding

#### 3.1.1 Document type and namespaces

The production document type and RB05-specific namespace require allocation by APTITUDE schema governance.

- **Proposed production identifier:** `eu.aptitude-project.biometric-profile.1`
- **Test-only identifier used in this package:** `org.example.aptitude.biometric-profile.1`
- **ISO general namespace:** `org.iso.23220.1`

Until RB05-D03 is approved, implementations SHALL use the test-only identifier only in isolated conformance environments and SHALL NOT issue it as a production credential. The proposed production identifier is a proposal, not an allocation.

An APTITUDE identifier or GitHub index entry is not registration in an EU catalogue of schemes. For an API-mediated flow, D03/D10 must either identify the legally and technically applicable catalogue/registration path for this proposed ordinary non-qualified EAA or provide cross-platform evidence that every target mediating API, operating system and browser can discover and present the explicitly allowlisted pilot type. If neither route is available, API-mediated RB05 is blocked. A proprietary allowlist SHALL be disclosed as a pilot limitation and SHALL NOT be presented as general EUDI interoperability.

The `docType` of each relevant `Document` in `DeviceResponse.documents[]` and the `docType` in its MSO SHALL be identical. All ISO generic data elements SHALL use `org.iso.23220.1`. The `biometric_reference` element SHALL use the approved RB05-specific namespace.

#### 3.1.2 General encoding rules

- RB05 SHALL use the issuer-signed mdoc structures, MSO, device key and device authentication defined by ISO/IEC 18013-5.
- Text strings SHALL be UTF-8 and support the full Unicode range.
- Project-defined text-length ceilings for the custom profile identifiers count UTF-8 encoded bytes, not displayed characters or UTF-16 code units. The 512-byte URI and 32-byte version ceilings are v0.1 interoperability proposals under RB05-D04/D10. This draft does not invent upper bounds for ISO identity elements: the exact ISO/IEC 23220-2 constraints and multilingual boundary behaviour must be confirmed under RB05-D10/D11, and implementations SHALL never silently truncate a valid name or issuer value.
- Administrative dates SHALL use CBOR tag 1004 `full-date` values in `YYYY-MM-DD` form.
- `MSO.validityInfo.validFrom` and `validUntil` SHALL use UTC timestamps with seconds precision, `Z` offset and no fractional seconds.
- CBOR encodings SHALL use deterministic length and integer representations consistent with RFC 8949.
- D10/D21 SHALL define tested ceilings for the complete DeviceRequest, DeviceResponse, mdoc/CBOR object, nesting/container depth, namespace and item counts, text/byte strings, decoded or decompressed output, parsing time and cryptographic work. The receiver SHALL reject indefinite or non-deterministic forms outside the adopted profile, duplicate map keys, duplicate/conflicting items, trailing data and over-budget structures before expensive cryptographic or biometric processing. The 16 KiB `payload` ceiling is not a whole-message resource limit.
- All values in the two namespaces SHALL be carried as digest-protected `IssuerSignedItem` values and covered by `IssuerAuth`.
- In accordance with ETSI TS 119 472-1 V1.2.1 requirements EAA-4.6.1-02, EAA-4.6.1-07 and EAA-6.6.1-01, the ISO mdoc EAA SHALL be signed using at least a CB-AdES-B-B signature under ETSI TS 119 152-1 V1.1.1, and the signing certificate SHALL follow the EAA Provider profile in clause 6 of ETSI TS 119 412-6 V1.1.1. RB05-D10 must resolve the certificate-carriage compatibility issue recorded in Section 8.2 and select the permitted algorithms, digest suite, any higher CB-AdES level and validation policy before an implementation candidate is issued.
- RB05 SHALL be device-bound using `MSO.deviceKeyInfo.deviceKey`. A verifier SHALL validate the device authentication and session transcript, not only `IssuerAuth`.
- For the v0.1 proposal, `expiry_date` is the last UTC calendar date on which the administrative credential may be accepted. `validUntil` SHALL be no later than `00:00:00Z` on the following date and no later than `validFrom` plus 30 × 24 hours. The date-only namespace representation also requires that `expiry_date` is no more than 30 calendar-date increments after `issue_date`; only a full-MSO validator can enforce the exact duration.
- `MSO.validityInfo.signed`, `validFrom` and `validUntil` SHALL satisfy the exact adopted mdoc profile, including `signed` no later than `validFrom` and `validFrom` earlier than `validUntil`. RB05-D10 and RB05-D21 must confirm the boundary interpretation, clock source and permitted skew before an implementation candidate is produced.
- An mdoc with an unknown `docType`, namespace, format profile, protection profile or matcher profile SHALL be rejected safely.

#### 3.1.3 Attribute mapping

| Data identifier | Attribute identifier | Encoding | Namespace | Requirement |
| --- | --- | --- | --- | --- |
| `family_name` | `family_name` | non-empty Unicode `tstr`; exact ISO bound pending D10/D11 | `org.iso.23220.1` | REQUIRED |
| `given_name` | `given_name` | non-empty Unicode `tstr`; exact ISO bound pending D10/D11 | `org.iso.23220.1` | REQUIRED |
| `document_number` | `document_number` | non-empty `tstr`; exact ISO bound pending D10 | `org.iso.23220.1` | REQUIRED |
| `issue_date` | `issue_date` | `full-date` | `org.iso.23220.1` | REQUIRED |
| `expiry_date` | `expiry_date` | `full-date` | `org.iso.23220.1` | REQUIRED |
| `issuing_authority_unicode` | `issuing_authority_unicode` | non-empty Unicode `tstr`; exact ISO bound pending D10 | `org.iso.23220.1` | REQUIRED |
| `biometric_reference` | `biometric_reference` | map defined by CDDL | RB05-specific namespace | REQUIRED |

`category`, `audience`, `oneTime`, `shortLived`, raw portraits, source-evidence fields and travel fields are prohibited in the namespaced v0.1 payload. For this proposed 30-day revocable profile, the selected `status` member SHALL be present in the full mdoc MSO and is not a namespaced RB05 attribute. The structural CDDL and JSON review projection cover namespace values only and therefore do not validate the MSO.

#### 3.1.4 Protected-template profile registry

Before a profile can be used with real biometric data, one registry entry SHALL approve the full (`format_id`, `format_version`, `protection_profile_id`, `matcher_profile_id`) tuple. Registration of the individual identifiers is not sufficient. The entry SHALL define at least:

1. owner, specification location, version and change policy;
2. facial feature extraction and input-image requirements;
3. exact payload syntax and maximum size;
4. template-protection transformation and security claims;
5. irreversibility, cancellation/renewal and the actual linkability properties and mitigations;
6. encryption algorithm, key ownership, key distribution and processing boundary;
7. compatible matcher implementation, comparison direction and score semantics;
8. verification threshold and the validation population used to set it;
9. compatible independently versioned live-capture/PAD policy identifiers and minimum assurance;
10. behaviour for unknown, deprecated or compromised versions; and
11. independent security, privacy, performance and demographic-differential test evidence.

The v0.1 registry intentionally contains no approved production entry. The synthetic `urn:example:` values in the test example SHALL NOT be used with a real person.

Profile identifiers SHALL be compared as exact registered UTF-8 strings. An implementation SHALL NOT normalise, follow, fetch or dereference a URI supplied in a credential. It SHALL resolve a tuple only through the locally available, authenticated registry under RB05-D04. This applies equally to `https:`, `file:`, percent-encoded and visually confusable values and prevents credential input from triggering network or file access.

The PAD profile governs the fresh live sample at the checkpoint; it is not a property of the stored enrolment reference and is not encoded in RB05 v0.1. D4.2 shall select an independently versioned PAD/capture policy approved under RB05-D06/D21 and compatible with the registered matcher tuple. A PAD upgrade that preserves the registered matcher input and approved performance envelope need not reissue RB05; an incompatible change requires a new tuple/version and lifecycle decision.

#### 3.1.5 Illustrative semantic example

The following is a readable projection of the namespaced values, not the binary ISO mdoc itself. The payload is synthetic and represents no face.

```json
{
  "docType": "org.example.aptitude.biometric-profile.1",
  "nameSpaces": {
    "org.iso.23220.1": {
      "family_name": "Durand",
      "given_name": "Camille",
      "document_number": "BPA-7XQ4-M9VK-2T6P",
      "issue_date": "2026-09-03",
      "expiry_date": "2026-10-03",
      "issuing_authority_unicode": "Example Issuer SAS"
    },
    "org.example.aptitude.biometric-profile.1": {
      "biometric_reference": {
        "modality": "face",
        "verification_mode": "one_to_one",
        "reference_type": "protected_template",
        "format_id": "urn:example:aptitude:rb05:format:face-template-v1",
        "format_version": "1.0",
        "protection_profile_id": "urn:example:aptitude:rb05:protection:cancelable-v1",
        "matcher_profile_id": "urn:example:aptitude:rb05:matcher:face-v1",
        "payload": "AAECAwQFBgcICQ=="
      }
    }
  }
}
```

In the JSON review projection, `payload` SHALL use canonical padded Base64. The JSON Schema checks alphabet, padding shape and size. Implementations SHALL also reject non-zero unused pad bits such as `AB==` when checking this JSON projection; schema validation alone does not establish canonical encoding. In the actual mdoc, the payload is a CBOR byte string and this JSON-only representation rule does not apply.

The structural CDDL is provided in [rb05-biometric-profile.cddl](../../schema/wp4/rb05-biometric-profile.cddl). A CBOR diagnostic-notation instance is provided in [rb05-example-semantic.diag](../../schema/wp4/rb05-example-semantic.diag). The [JSON Schema](../../schema/wp4/rb05-biometric-profile.schema.json) and [synthetic JSON example](../../schema/wp4/rb05-example-protected-template.json) support review of the same namespace model. The JSON Schema is non-normative; the Rulebook remains the source of field semantics and every constraint that the structural grammar cannot express. These schemas describe the complete issuance/full-credential set of namespace values; they are not schemas for a selectively disclosed DeviceResponse. The Attestation Provider and Wallet Unit validate the full set during issuance/storage. During presentation, a verifier validates the disclosed items against their individual definitions plus the MSO/digests and disclosure policy; it SHALL NOT reject a legitimate selective disclosure merely because undisclosed mandatory issuance fields are absent.

Neither example is a complete ISO/IEC 18013-5 credential: the package does not yet contain `IssuerSignedItemBytes`, MSO digests, `IssuerAuth`/CB-AdES, device-key material, certificates or test signatures. A complete deterministic CBOR/COSE/MSO vector is required under RB05-D10 before implementation conformance can be claimed.

#### 3.1.6 QR-code rule

An ISO/IEC 18013-5 QR code MAY be used for device engagement. It SHALL contain only engagement information defined by the selected proximity profile; it SHALL NOT be described as carrying the RB05 credential or raw biometric payload.

Any data-bearing biometric QR retained for UC9 is a separate mechanism and requires its own specification. That specification must cover its payload, signature/encryption, audience, freshness, replay protection, expiry, key management and privacy controls. It SHALL NOT be labelled “ISO/IEC 18013-5 compliant” merely because it is displayed as a QR code.

### 3.2 SD-JWT VC encoding

Not supported by RB05 v0.1.

### 3.3 W3C Verifiable Credentials Data Model encoding

Not supported by RB05 v0.1.

## 4 Attestation usage

### 4.1 Actors and responsibilities

| Actor | Proposed UC9 responsibility |
| --- | --- |
| APTITUDE schema-governance function (to be confirmed) | Proposed to allocate the production `docType` and namespace and coordinate technical approval of this Rulebook and schema; its authority remains open under RB05-D14. |
| IN Groupe / proposed legal issuer | Validates enrolment, generates or approves the protected reference, issues and revokes RB05, operates or designates status services, and maintains the profile registry. The exact legal entity remains open under RB05-D02. |
| Wallet Provider | Supplies a conformant Wallet Unit, protects holder keys and RB05 at rest, authenticates the Wallet User before approval, obtains holder approval and performs device authentication. |
| Traveller | Voluntarily enrols, reviews issuance, controls presentations, may withdraw and retains a non-biometric route. |
| Marseille Airport / proposed registered Relying Party | For R2, requests and validates RB05 and performs or commissions PAD and one-to-one comparison inside the approved boundary. For R1, validates the selected Ready-to-Travel/QR artefact under its own agreed profile; direct RB05 checkpoint presentation is not assumed. The exact component/operator and deletion duties remain open under D16; the airline/DCS/airport decision owner remains open under D02/D12/D18. |
| Ready-to-Travel provider, if R1 is retained | Validates the biometric-profile and travel inputs and issues the derived attestation under a separately agreed profile. D12/D18 confirm the legal entity, protected-reference reuse permission, association evidence, storage, lifecycle and checkpoint validation; no approval is inferred from inclusion of this role. |
| Biometric processing component/operator (legal role TBD) | Operates only within the approved purpose, trust boundary and protected-template profile and under its documented legal role. Where it acts as a processor, it acts only on the controller's documented instructions. |
| Status Provider | Publishes signed, privacy-preserving RB05 status information and meets the agreed update service level. |

The same organisation may perform multiple roles, but the legal identity, technical component and responsibility of each role SHALL be documented. An “airport app” SHALL NOT be called a Wallet Unit unless the Wallet Provider and governance process confirm that status.

### 4.2 Preconditions for issuance

The following preconditions apply when RB05 relates to a real person or pilot participant. Isolated non-production conformance vectors may be generated without a traveller only with test-only identifiers and keys, synthetic identities and non-biometric bytes; they SHALL be visibly marked, kept outside production trust/status systems and never imported into a participant Wallet or used for a biometric/travel decision.

The issuer SHALL issue a real-person RB05 only when all of the following are true:

1. the traveller has deliberately initiated enrolment and received clear information about purpose, data, retention, recipients, risks and the non-biometric alternative;
2. the required legal basis and Article 9 GDPR condition have been recorded by the controller, with an approved DPIA for the pilot;
3. the source credential is permitted by the source-acceptance policy approved under RB05-D22 and has been cryptographically validated for its exact `docType`, format/version, signature, issuer trust, device/holder binding where applicable, assurance, validity, status and presentation freshness;
4. the source contains the exact authenticated portrait element permitted by RB05-D22 and it is suitable for the approved feature-extraction profile;
5. the subject data copied to RB05 matches the validated source fields through the exact mapping and normalisation rules approved under RB05-D22;
6. the protected reference was generated within the approved processing boundary and passes the profile's quality checks;
7. the target Wallet Unit proves control of the key placed in `MSO.deviceKeyInfo.deviceKey` and uses the current WUA set/construct comprising the required WIA(s) and, because RB05 is device-bound, KA(s). The authorisation server SHALL validate each WIA and its proof of possession at the applicable pushed-authorisation/token endpoints. The credential issuer SHALL validate each KA and credential-binding proof at the Credential Endpoint. The applicable checks include proofs/signatures, Wallet Provider certificates and trust, status/lifecycle, nonce/freshness, Wallet-instance-to-authorisation-server binding, target-key attestation and WSCD/keystore claims;
8. the issuer can populate an approved production identifier, protected-template profile and status reference; and
9. an integrity-protected transaction context binds the source presentation and its device authentication/user approval, authorised subject values, biometric-processor result, approved profile tuple, target Wallet WIA/KA/key and credential offer/authorisation to the same fresh enrolment session and the same authenticated Wallet User. The source and target SHALL use the same authenticated Wallet Unit with cryptographic session continuity, unless RB05-D19 approves a specific cross-device/re-key ceremony that proves the relationship.

A PID whose portrait is absent, empty, unauthenticated, not disclosed or unsuitable for the approved extraction profile SHALL NOT be treated as a usable biometric source. The candidate source set includes PID with an available authenticated portrait, PhotoID and DTC, consistent with D4.1; each exact type/version/issuer and portrait mapping must be approved under RB05-D22. Inclusion in this candidate set does not imply acceptance of every PID, PhotoID or DTC. The issuer SHALL NOT accept an unlisted type/issuer, lower-assurance substitute or downgrade. If the chosen source cannot supply a usable portrait, enrolment stops before template generation; another approved source may be offered through an explicitly authorised flow, or the traveller uses the non-biometric route. The issuer SHALL NOT encode the source credential, its document number, its portrait or an “attributes evidence” object inside RB05.

Combining identity or portrait evidence from multiple source credentials SHALL NOT be accepted unless RB05-D19 and RB05-D22 approve the exact combination, same-subject mapping and fresh-session continuity for every input. The issuer SHALL reject any combination for which that evidence is missing, inconsistent or invalid; possessing several valid credentials does not establish that they concern the same person.

### 4.3 Issuance flow

Where a Wallet Relying Party requests disclosure of a source `portrait`, the Wallet Provider SHALL ensure that the Wallet Solution warns the Wallet User that the request involves sharing biometric data and requires explicit, specific confirmation, as required by the current Commission Implementing Regulation (EU) 2024/2977, Article 3a. A Relying Party may retain the portrait only to the extent necessary for identification or authentication and in compliance with Union data-protection law, or where another applicable Union or national law that complies with Union data-protection law provides for retention. Transfer to a third country or international organisation is permitted only where Union data-protection law allows it. These portrait-specific safeguards are distinct from this Rulebook's policy for the derived protected reference. Confirmation is a technical safeguard; it is not a substitute for the GDPR legal basis or Article 9 condition.

1. The airport channel creates a single-use enrolment session with a high-entropy nonce and an integrity-protected transaction context.
2. The registered remote Relying Party requests only the necessary source attributes through the APTITUDE presentation profile.
3. The Wallet Unit displays the requester, purpose, attributes and retention information and obtains the traveller's explicit approval.
4. The Relying Party validates the complete source presentation, binds its transcript/digest and authorised values to the enrolment context, and only then forwards the authorised inputs to the biometric processor.
5. The approved biometric processor generates the protected reference and returns an integrity-protected result bound to the same session and approved profile tuple. The result SHALL identify the authorised processor and its authenticated/signing key and, where available, attest the approved software/profile version and security-relevant configuration.
6. Before signing, the issuer SHALL either verify the source presentation itself or authenticate an authorised source verifier and verify an integrity-protected validation result under an approved trust policy. It SHALL also authenticate the authorised biometric processor and validate its result, profile/configuration evidence and freshness. The complete evidence SHALL bind the source transcript/digest and source device/user approval, authorised subject values, processor result, approved profile tuple, target Wallet WIA/KA/key and issuance authorisation to the same fresh context and authenticated Wallet User. A same-Wallet cryptographic continuity proof or a specifically approved cross-device/re-key ceremony SHALL establish that relationship. A forged, untrusted, wrongly configured, cross-user, swapped, stale or replayed session, result, template, subject, Wallet key, credential offer or pre-authorised code SHALL be rejected under RB05-D19.
7. The issuer assigns and collision-checks a fresh, never-reassigned RB05 `document_number`, selects expiry, builds the mdoc and binds it to the validated target Wallet Unit key. If early source invalidation is supported, it creates only the protected minimal dependency record approved under RB05-D20; the source document number, portrait and biometric bytes are excluded.
8. RB05 issuance SHALL follow ETSI TS 119 472-3 V1.1.1, which builds on HAIP 1.0's profile of OpenID4VCI 1.0, with the applicable adaptations in Commission Implementing Regulation (EU) 2024/2982 as amended by (EU) 2026/1731. APTITUDE RFC-01 may add project constraints only where they are consistent with that incorporated EU profile. Before issuing, the provider SHALL publish signed Issuer Metadata whose RB05 credential configuration identifies the exact type and format, applicable provider access/registration information, selected credential-reuse policy, and the unique URI plus data set or preload reference for the Embedded Disclosure Policy (EDP). RB05-D10 must fix those exact metadata values and how the EDP maps the authorised purpose and attributes to Relying Party certificate identities or entitlements.
9. The Wallet Unit shows the issuer, attestation type, purpose, validity and sensitive-data notice before accepting storage.
10. On successful delivery, the source portrait, unprotected features and every issuer/processor working copy of the protected reference SHALL be removed from active memory and normal processing immediately. Any strictly necessary transient copy in a queue or recoverable processing store SHALL be deleted within the approved retention period; v0.1 proposes 24 hours from session creation as the absolute ceiling. The same deletion rules and absolute ceiling apply when issuance fails, is cancelled, is abandoned or times out; active copies SHALL be cleared as soon as they are no longer needed. The approved schedule under RB05-D15 must separately address transaction-context data, caches, logs and backups. Audit records SHALL exclude biometric bytes and source-document numbers.
11. Reuse of the enrolment session, credential offer or pre-authorised code SHALL be rejected.

### 4.4 Presentation profiles

This section specifies candidate direct-RB05 presentation for R2. R1's Ready-to-Travel and data-bearing biometric QR require their own selected presentation, trust and validation profiles under D12/D18. A similar transport or a shared biometric reference does not make those artefacts conformant RB05 credentials.

| Profile | Transport | Permitted use | Mandatory controls |
| --- | --- | --- | --- |
| Remote — API-mediated ISO mdoc | ISO/IEC TS 18013-7:2025 Annex C as profiled by ETSI TS 119 472-2 V1.2.1, with the applicable current adaptations in Commission Implementing Regulation (EU) 2024/2982 as amended | Just-in-time app-mediated transfer during an active UC9 touchpoint/session, if selected under RB05-D10; no pre-arrival staging | authenticated request with mandatory `requestInfo.euWrprc`; RB05 fail-closed certificate validation; verifier/client and nonce/response binding; response protection; Wallet User authentication and explicit approval; least-data request; short D16/D21 transaction TTL |
| Remote — OpenID4VC-HAIP | OpenID4VC-HAIP profile in ETSI TS 119 472-2 V1.2.1 clause 6 with the applicable current Implementing Regulation adaptations, building on HAIP 1.0 and OpenID4VP 1.0; APTITUDE RFC-02 may add consistent project constraints | Just-in-time remote transfer during an active UC9 touchpoint/session, if selected under RB05-D10; no pre-arrival staging | signed Request Object with the Relying Party registration certificate in `verifier_info`; Relying Party access certificate for `x509_hash` client authentication; RB05 fail-closed certificate validation; verifier/client and nonce/response binding; response protection; Wallet User authentication and explicit approval; least-data request; short D16/D21 transaction TTL |
| Proximity | Applicable non-API-mediated ISO/mdoc profile in ETSI TS 119 472-2 V1.2.1 with the current Implementing Regulation adaptations, building on ISO/IEC 18013-5 | Traveller-present checkpoint verification, including approved offline operation with fresh cached trust/status material | reader authentication and mandatory `requestInfo.euWrprc`; RB05 fail-closed certificate validation; session transcript; Wallet User authentication; device authentication; explicit holder action; no data-bearing static QR |

RB05-D10 must select which remote mode or modes UC9 will exercise, and each transaction uses one profile at a time. That UC9 choice does not waive any protocol or mediating-API support obligation independently applicable to the Wallet Solution or Relying Party under the current Implementing Regulation. APTITUDE RFC-02 is a draft remote-presentation profile and does not define the proximity route. Until an APTITUDE proximity RFC is approved, implementations SHALL use the applicable non-API-mediated ISO/mdoc profile in ETSI TS 119 472-2 V1.2.1 with the current Implementing Regulation adaptations, which builds on ISO/IEC 18013-5, plus this Rulebook's reader-authentication and privacy controls.

For OpenID4VP-HAIP, RB05-D10 SHALL identify whether each exercised flow is API-mediated or redirects-based/non-API-mediated. A Wallet SHOULD NOT support a redirects-based cross-device presentation. If UC9 nevertheless retains that route, D10/D21 SHALL define and test Relying Party controls against session fixation, hand-off substitution, replay and incorrect device/session binding before it may carry RB05.

When an API-mediated mode is selected, the mode-specific current Implementing Regulation adaptations also apply. By default, the EUDI Wallet exposes to the mediating API only the presence of the stored RB05 **type**, never RB05 attributes or values. The Wallet SHALL provide the applicable global user control: for ISO/IEC 18013-7 Annex C, disabling it prevents advertising or responding to API-mediated presentation or issuance requests; for OpenID4VP-HAIP, disabling default type disclosure preserves any profile-supported individual-attestation selection. The ISO Annex C route SHALL notify the mediating API when a previously disclosed RB05 is deleted and when Wallet uninstallation removes previously disclosed attestation state. In every API-mediated cross-device flow, the Wallet SHALL verify close physical proximity through a secure, direct and user-mediated local channel. D03/D10 SHALL also prove discovery and presentation of the RB05 type on every target platform; the regulatory minimum for mediating APIs covers catalogue-registered types and does not by itself guarantee support for this unregistered pilot type. Because even the RB05 type reveals participation in a biometric programme, D10 must confirm the selected mode's exact behaviour and D13/D17 must assess the mediating API, operating-system and browser exposure, purposes, retention and correlation risk before real-person testing.

For R2 checkpoint use, RB05 v0.1 prohibits pre-arrival staging of `biometric_reference`. A remote disclosure SHALL belong to one active, fresh, short-lived transaction bound to the later live capture and authorised touchpoint. D16/D21 must define the maximum TTL, volatile-memory/queue and restart behaviour, cancellation/no-show deletion and replay-proof binding. No reusable airport staging database is permitted. This rule does not define or approve R1's pre-travel association step: authorised consumption of RB05, protected-reference reuse and any required policy revision for that step remain under D12/D18. Until the applicable values and controls are approved, the corresponding processing with real biometric data is blocked.

### 4.5 Disclosure policy

- The `biometric_reference` map is an atomic disclosure unit. A verifier that requests it receives the entire protected-reference map and SHALL be authorised for the associated biometric purpose.
- `family_name`, `given_name` and `document_number` SHALL each remain independently selectively disclosable. A later version that adds another identity field must also define its independent disclosure policy.
- At a normal biometric checkpoint, the Relying Party SHOULD request `biometric_reference` only. It SHALL request a name or other identity attribute only when a recorded operational or legal requirement makes it necessary.
- Before allowing the Wallet User to approve or refuse release of any RB05 attribute, the Wallet Unit SHALL authenticate that user in accordance with the applicable EUDI Wallet user-authentication requirements. The authentication method, security level and validity window SHALL follow the adopted Wallet/WSCA/WSCD profile under RB05-D10. User authentication, explicit approval and mdoc device authentication are three distinct controls; successful user authentication never substitutes for a fresh approval to the displayed request.
- Before each `biometric_reference` disclosure, the Wallet Unit SHALL clearly display the verified Relying Party/reader and service identity, touchpoint and stated purpose, the fact that a protected biometric reference will be sent for external matching, the authorised recipient/processing boundary, every requested attribute, the declared transient-retention rule and the available non-biometric route. It SHALL let the Wallet User explicitly confirm or refuse that specific request. This transparency and approval control is not, by itself, GDPR consent or another lawful basis.
- RB05 SHALL NOT be presented silently or continuously. The Wallet Unit SHALL require an explicit holder action for each disclosure transaction.
- Wallet presentation approval is not, by itself, proof that every GDPR requirement or a valid Article 9 consent condition has been met. Legal basis, transparency and withdrawal handling remain controller obligations.

The v0.1 credential and protected reference are stable for their lifetime. A Relying Party may correlate repeat presentations not only by hashing `biometric_reference`, but also through stable full-mdoc material such as `IssuerAuth`/MSO, the device public key, status references and disclosed `IssuerSignedItem` values, as well as protocol metadata. Transport encryption and contractual deletion do not create technical unlinkability, and re-randomising only the biometric payload would not close the whole-presentation risk. This draft does not claim unlinkability between presentations or Relying Parties. Before testing with real people, RB05-D17 must analyse complete presentation transcripts and select and validate a design such as batch/one-time or RP/purpose-specific attestations with distinct cryptographic material, an applicable unlinkable presentation mechanism, or a revised on-device/proof-based flow. Each option changes other lifecycle, status or data-model rules and therefore requires an updated profile. If no technical mitigation is feasible, the pilot scope, residual linkability, Relying-Party restrictions, retention controls, transparency and controller-approved DPIA acceptance must be explicit.

### 4.6 Verification flow and decision separation

The following detailed stages specify R2, the candidate direct-RB05 checkpoint route. Before any disclosure, the Wallet Unit performs the request-side gate defined in Sections 4.4, 4.5 and 5.2: it authenticates the Relying Party/reader and request, validates the applicable registration/access certificate and its purpose/attribute entitlements, applies the EDP and RB05 no-bypass policy, authenticates the Wallet User and obtains fresh explicit approval. This includes validating `requestInfo.euWrprc` and ReaderAuth for the ISO route or the signed Request Object, `verifier_info` registration certificate and Relying Party access certificate for the OpenID4VP-HAIP route. Any failure stops the transaction before RB05 data is released.

After that Wallet-side gate, the RB05 verification/matching boundary performs the response-side credential validation in Stage A and biometric verification in Stage B. Stage C is performed or invoked by the travel-authorisation component assigned in D4.2, which may be operationally separate; RB05 supplies only the minimum transaction-bound outcome required by that component. That outcome SHALL be authenticated and integrity-protected, fresh, and cryptographically bound to the exact RB05 presentation, live-match session, validated travel-entitlement evidence and authorised touchpoint. Stage C SHALL reject a forged, altered, replayed, swapped, stale or unauthorised outcome. D12/D18 select the evidence and binding protocol; these stages do not prescribe two presentation interactions.

For the purposes of this v0.1 data model, an authenticated Marseille checkpoint service receives the protected reference and performs or commissions the comparison inside an authorised transaction boundary, then renders the reference inaccessible. RB05-D16 must still determine whether execution is in the physical gate/reader, another dedicated airport component or a named processor, and must fix the interface and key boundary. On-device matching is a possible privacy-improving redesign under RB05-D17, but it is not the flow specified by v0.1 because the current presentation model discloses `biometric_reference` to the verifier.

#### Stage A — verifier-side response and credential validation

1. validate the expected production `docType` and namespaces;
2. validate the issuer signature and certification path against the authorised RB05 issuer registry;
3. validate MSO digests, technical validity, administrative expiry and the mandatory status member;
4. for remote presentation, validate that the received response is bound to the exact authenticated request, client, nonce and session, and validate the required response protection and Wallet/device proof under the selected remote profile;
5. for proximity presentation, validate that the DeviceResponse is bound to the exact session transcript and validate device authentication under the profiled ISO/IEC 18013-5 route;
6. validate each disclosed item against its field definition and presentation policy, rejecting unknown or prohibited disclosed fields without requiring legitimate undisclosed issuance-mandatory fields; and
7. validate the complete format/version/protection/matcher tuple against one approved registry entry.

#### Stage B — biometric verification

1. activate live capture only after the traveller's deliberate action;
2. avoid capturing uninvolved people and apply the approved PAD profile;
3. generate the live comparison representation inside the approved security boundary;
4. compare one-to-one against the disclosed protected reference using the registered matcher and threshold; and
5. return only the minimum outcome needed by the transaction.

#### Stage C — operational authorisation

1. independently validate the applicable boarding pass or travel entitlement;
2. establish, through a D4.2-approved mechanism, that the authenticated Stage A/B outcome, the RB05 used in those stages and the validated travel-entitlement evidence belong to the same traveller within the same fresh transaction and authorised touchpoint;
3. apply the airport/airline business rules for that touchpoint; and
4. permit or deny the operation without treating RB05 alone as a boarding entitlement.

The R2 same-holder mechanism is blocked by RB05-D18. Co-location in one user interface, matching display names or possession of two otherwise unrelated credentials SHALL NOT be treated as sufficient on their own. Until an approved combined-presentation/session-binding or equivalent evidence-binding mechanism is implemented and tested, the operational owner designated under D16/D18 SHALL direct the traveller to the non-biometric/manual route rather than permit an automated travel decision.

A positive Stage A result does not mean the face matched. A positive Stage B result does not mean the traveller is entitled to board. A biometric mismatch or PAD failure does not mean the issuer signature is invalid and SHALL NOT automatically revoke RB05.

For R1, the same decision separation applies to the credential actually presented, but the checkpoint is not required to receive or revalidate the original RB05 as though R2 had been selected. The Ready-to-Travel/QR specification must establish how validated profile and travel inputs are associated at issuance, how that association is authenticated and bound to the presenting traveller, how source/derived-credential validity and status changes are handled, and how fresh live verification and current operational entitlement are checked. RB05 conformance alone does not demonstrate any of those derived-credential properties. D12/D18 must supply and test the selected R1 controls; a valid issuer signature or successful face match alone is insufficient for the travel decision.

### 4.7 Failure and fallback

For the direct-RB05 route, the biometric fast path SHALL stop, expose no sensitive diagnostic value and offer the approved non-biometric route when any of the following occurs:

- the traveller refuses or withdraws;
- reader authentication or Relying Party registration fails;
- issuer trust, signature, digest, device authentication, validity or status fails;
- trust or status information is unavailable or stale;
- the format, protection or matcher profile is unknown or deprecated;
- PAD fails, the face does not match or capture quality is inadequate;
- the same-holder/transaction binding between RB05 and the travel-entitlement evidence is absent or invalid; or
- the boarding/travel entitlement is absent, invalid or inconsistent.

The fallback SHALL not impose an unjustified penalty or deny a service that is available through an equivalent non-biometric process. Error codes SHALL distinguish credential, status, device, PAD, match and travel-entitlement failures without exposing biometric scores to the traveller or ordinary logs.

If R1 is selected, its specification must map these failure classes to the Ready-to-Travel/QR credential actually used, its association evidence and its lifecycle dependencies. It must not require an R2-only input as a condition of successful R1 operation.

### 4.8 Device binding and lifecycle

RB05 SHALL be device-bound. The private key corresponding to `MSO.deviceKeyInfo.deviceKey` SHALL remain protected by the Wallet Secure Cryptographic Device/Application and SHALL be used during each presentation.

RB05 is renewable but not transferable. A new device, key rotation, material subject-data change, expired source credential, compromised profile or withdrawn participation requires a newly issued RB05. Copying the mdoc or QR representation to another device SHALL NOT produce a valid device-authenticated presentation.

Replacement SHALL NOT leave an uncontrolled second active instance. For loss, suspected compromise or security-driven replacement, the old RB05 SHALL be revoked before a replacement is activated. For planned renewal, device migration or key rotation, the issuer SHALL revoke the superseded RB05 immediately after it has confirmed successful delivery of the new instance; failed or cancelled replacement SHALL leave the existing status unchanged and be safely retryable. RB05-D07 and RB05-D09 must fix the atomicity, recovery and any strictly bounded overlap rule before implementation.

The holder SHALL be able to delete RB05 locally and request issuer-side revocation. Local deletion and issuer-side revocation are distinct operations and the user interface SHALL explain that distinction.

At issuance, the RB05 expiry is capped by the validated source expiry. To react to an earlier source invalidation, the issuer may additionally maintain a protected dependency record only if RB05-D20 approves a privacy-preserving correlation or notification mechanism. That record SHALL contain no source document number, portrait, biometric value or booking data. It may contain the RB05 `document_number`, source type/issuer, source expiry and an issuer-provided opaque status-correlation or subscription handle. Access, encryption, purpose, deletion and incident retention SHALL be documented. If no such mechanism exists, the deployment SHALL state that early source invalidation is not automatically propagated, revalidate the source at renewal and have the residual validity risk approved; it SHALL NOT pretend that the trigger is implemented.

### 4.9 Transactional data

RB05 contains no transactional or travel data. This is consistent with the distinction in D4.1 between creation of the Biometric Profile Attestation and the later association with boarding data to issue Ready-to-Travel. Ready-to-Travel, RB03 and a data-bearing biometric QR are distinct artefacts with their own issuer, lifecycle, rulebook/schema and data-protection decisions; they are not added as fields inside RB05.

Keeping those artefacts distinct does not decide which one is presented at a checkpoint. D12 selects the route described in Section 1.7. For R1, D18 defines trusted association and derivation plus the Ready-to-Travel/QR verification and operational decision. For R2, D18 defines binding between the direct RB05 presentation, live comparison and independently validated travel-entitlement evidence. Both routes must relate the evidence to the same traveller and fresh operation. Any authorised reuse of the protected reference must satisfy the selected format, protection, purpose, recipient and retention policy; the candidate does not silently authorise copying it into another credential.

### 4.10 Environmental and operational constraints

RB05 defines credential behaviour, but a biometric airport result is valid only inside a tested operating envelope. D4.2 and the approved profiles under RB05-D06, D10, D16 and D21 SHALL specify measurable values for:

- supported Wallet, phone, operating-system, reader/gate, camera and biometric-component versions;
- lighting range, camera geometry/distance, background, capture zone and bystander controls;
- capture/PAD/match latency, transaction timeout, throughput and queue targets;
- network-connected and offline modes, maximum trust/status cache age, outage transition and recovery;
- clock source, synchronisation, permitted skew and the interpretation of the end of `expiry_date`;
- retry count, quality guidance, accessible camera/reader placement and assisted/manual fallback;
- power/restart and interrupted-session recovery without replay or residual sensitive data; and
- environmental/security monitoring that does not log biometric or unnecessary identity data.

The v0.1 document does not invent these values. Synthetic functional testing may proceed, but no biometric accuracy, performance, accessibility or operational-readiness claim is valid outside the approved envelope or before RB05-D21 is closed.

## 5 Trust anchors

### 5.1 Issuer trust

An RB05 verifier SHALL trust an issuer only when all of the following hold:

1. the issuer's signing certificate chains to a trust anchor obtained through the APTITUDE pilot trust mechanism approved under RB05-D08;
2. the issuer is authorised in that mechanism for the exact RB05 production `docType`;
3. the certificate and every applicable intermediate are within validity and not revoked;
4. certificate key usage, extended key usage and policy constraints match the adopted mdoc issuer profile; and
5. the `issuing_authority_unicode` value is consistent with the registered legal issuer.

The verifier SHALL verify `IssuerAuth` with the authorised issuer signing public key/certificate and SHALL separately validate that certificate's path and RB05 authorisation to an approved trust anchor or trust source. The Relying Party's own public key is not an issuer-verification key.

The final machine-readable trust-list URL and certificate profile are not yet published in the accessible material. They are production blockers RB05-D08 and RB05-D10; inventing an endpoint here would create false interoperability. RB05-D09 separately governs credential status and revocation.

### 5.2 Relying-party and reader trust

Before releasing `biometric_reference`, the Wallet Unit SHALL authenticate the Relying Party/reader using the adopted EUDI Wallet relying-party registration and reader-authentication mechanisms. For an ISO/mdoc DeviceRequest to an EUDI Wallet, `requestInfo.euWrprc` SHALL be present and contain the CBOR-byte-string serialization of the Relying Party registration certificate required by the current Implementing Regulation profile; it is not replaceable by a project-defined equivalent. For OpenID4VP-HAIP, one element of the signed Request Object's `verifier_info` SHALL contain that registration certificate, and the leaf certificate used with the `x509_hash` client-identifier prefix SHALL be the Relying Party access certificate required by the current profile. The Union-law obligation in Article 3(4) of Implementing Regulation (EU) 2024/2982, as amended, to authenticate and validate a registration certificate applies from 11 August 2028. The accompanying profile allows a warning and explicit user approval after failed validation, subject to the Wallet Provider's risk policy. Because RB05 discloses a protected biometric reference, this Rulebook proposes a stricter pilot rule from the start: the Wallet Unit SHALL validate the registration certificate's trust, status, freshness, intended use and attribute entitlements and SHALL NOT permit that failure to be bypassed by the user. This is an RB05 security policy, not a claim that fail-closed handling is already the Union-law baseline. An adopted equivalent may be used only for a different presentation mode where the applicable law/profile permits it. Authorisation SHALL be limited to the registered organisation, purpose, attribute set, environment and validity period. The Wallet Unit SHALL evaluate the RB05 Embedded Disclosure Policy supplied through the signed Issuer Metadata against the verified Relying Party certificate/registration information and entitlements, inform the user of the result, and refuse a request that does not satisfy the policy.

RB05-D10 must assign the EDP a unique immutable version URI and content hash, fix its exact data set and issuer-metadata credential configuration, map allowed purposes and attributes to the Relying Party certificate/entitlement model, and select the credential-reuse policy consistent with RB05-D17. The EDP content SHALL be authenticated through the signed metadata or an approved trusted preload/distribution mechanism. An unknown, unavailable, stale, tampered, mismatched or rolled-back policy SHALL fail closed; the Wallet Unit SHALL NOT substitute a similarly named policy. D10 must also define EDP cache/refresh/rollback handling and identify the exact Wallet Relying Party access/registration certificates or adopted equivalents, registrar and trust sources, certificate-status/freshness/cache validation, intended-use and attribute-entitlement binding, rollover and emergency removal. The prose in this Rulebook is not, by itself, an executable access-control policy.

An unauthenticated reader or a registered party without a biometric purpose SHALL NOT receive `biometric_reference`. Production deployment SHALL define certificate rollover, emergency removal and compromise notification for both issuers and readers.

### 5.3 Key separation

Issuer-signing keys, status-signing keys, reader-authentication keys, payload-protection keys and matcher/decryption keys SHALL be separate by purpose. The holder's mdoc device key SHALL NOT be used to encrypt the biometric payload. No single shared symmetric key across all pilot readers is acceptable without an approved key-rotation, compromise-containment and hardware-protection design.

## 6 Status and revocation

### 6.1 Revocability

RB05 v0.1 proposes a revocable credential. Its proposed 30-day maximum administrative lifetime does not remove the need to respond to device loss, key compromise, erroneous issuance or compromise of the biometric/protection profile.

For this profile, `shortLived` and `oneTime` are absent and an MSO `status` member is mandatory. A full credential without that member is non-conformant even though the namespace-only CDDL/JSON projection can be validated independently.

Binary “not revoked/revoked” semantics are an RB05 pilot-policy proposal. They are not presented as a status model automatically imposed on an ordinary non-qualified EAA by Commission Implementing Regulation (EU) 2026/1731. WP2 and the issuer SHALL select which permitted current MSO-compatible mechanism RB05 emits, together with its endpoint, signing profile, cache policy and outage behaviour, before implementation. Because the UC9 Relying Party needs to verify RB05 revocation, it SHALL support both current verifier mechanisms: the attestation status-list mechanism and the attestation revocation-list mechanism encoded as an identifier list. This verifier-support rule does not mean that one RB05 MSO must carry both. For an identifier-list reference, the identifier SHALL be unique per MSO. For a status-list reference, the combination of status index and URI SHALL be unique per MSO. APTITUDE RFC-04 may supplement that decision only after it is reconciled with the current Implementing Regulation. For an mdoc, the selected reference belongs in the MSO `status` structure; no RB05 namespace `status` attribute is defined.

The production Rulebook SHALL state the exact status or revocation-list domain, mechanism, encoding version, signer trust, update interval, cache rule and outage policy. These are blocked by RB05-D09. The v0.1 operational proposal is:

- status semantics are binary: not revoked or revoked; no suspension state is used by RB05;
- the status issuer publishes an updated signed list no later than 15 minutes after accepting a revocation event;
- a verifier accepts cached status only while it is within its signed validity interval **and** its signed issue time is no more than 15 minutes old, subject to the clock-skew rule approved under RB05-D09/D21;
- stale, unverifiable or unavailable status fails closed for the biometric fast path and invokes the manual route; and
- status/revocation-list construction SHALL prevent the issuer from learning when or where a particular RB05 is presented;
- `revoked` is irreversible for one RB05 instance; renewed access requires a freshly issued credential with a new `document_number`.

### 6.2 Revocation triggers

The issuer SHALL support revocation for:

- erroneous or fraudulent issuance;
- holder-reported device loss or compromise;
- post-issuance revocation, compromise or end of the approved status-maintenance horizon of a WIA, KA or Wallet Unit, where the adopted D09/D10 mapping identifies affected RB05 instances;
- compromise or unauthorised export of the protected reference;
- issuer or holder key compromise;
- withdrawal requiring the credential to become unusable;
- material change to copied subject data;
- source credential invalidation only when the approved RB05-D20 dependency/notification mechanism identifies an affected RB05;
- protected-template, protection or matcher profile compromise/deprecation; and
- termination of the pilot or holder account where continued use is no longer authorised.

A biometric mismatch, PAD failure, capture-quality failure or invalid boarding pass SHALL NOT by itself revoke RB05.

RB05-D09 SHALL also define the revocation-intake path, not only the published status output. It must specify authenticated request channels and authorisation evidence for the holder, issuer/security team, approved source-status notifier and protected-template profile owner; a device-independent recovery route for loss or compromise; an unambiguous mapping from each accepted event to affected RB05 instances; idempotency, replay protection, rate limiting and abuse/fraud handling; privacy-safe audit and requester notification; emergency escalation; and the hand-off from accepted event to signed-list publication. An unauthenticated, duplicate or malformed request SHALL NOT change status. The issuer SHALL record an accepted or rejected outcome without recording biometric bytes or source-document numbers.

D09/D10 SHALL select an authenticated Wallet Provider status/revocation feed or equivalent mechanism that can map a revoked/compromised WIA, KA or Wallet Unit to all affected live RB05 instances within an approved SLA. If the adopted profile cannot support that propagation, the owner must document the limitation, shorten/cap RB05 validity as necessary and obtain explicit residual-risk approval; the implementation SHALL NOT claim post-issuance Wallet-attestation revocation coverage that it does not provide.

### 6.3 Renewal and deletion

Renewal SHALL generate a new `document_number`, a fresh Wallet Unit binding and a newly protected reference. A compromised or deprecated protection profile SHALL NOT be renewed by copying its old payload.

The Wallet Unit SHALL NOT present an expired RB05 or an RB05 it knows to be revoked. It SHALL clearly mark the credential unusable, inform the holder and provide the approved deletion path. D07, D09, D13 and D20 SHALL define end-of-life handling after expiry, revocation, withdrawal, replacement and pilot termination for the Wallet copy, issuer account/mapping, status entries, dependency records, audits and backups. A revoked-status entry SHALL remain available long enough to prevent stale acceptance under the approved trust/status/cache model, and neither its serial nor status slot may be reused.

Revocation does not erase data already disclosed to a Relying Party. Each participant SHALL separately enforce the deletion and retention rules in Chapter 7.

## 7 Security, privacy and biometric controls

### 7.1 Mandatory security controls

- The profile SHALL implement and evidence confidentiality, integrity, irreversibility and renewal/cancellation properties appropriate to ISO/IEC 24745. It SHALL accurately state linkability across the complete credential and presentation transcript. Neither a protected/re-randomised biometric payload nor encrypted transport SHALL be described as presentation-unlinkable while stable `IssuerAuth`/MSO, device-key, status, disclosed-item or protocol identifiers remain correlatable.
- The protected reference SHALL be encrypted or otherwise protected at application level in addition to Wallet storage and mdoc session protections.
- Wallet keys and cryptographic operations SHALL use the adopted WSCD/WSCA profile.
- Readers and biometric processing components SHALL use hardened, least-privilege execution boundaries and authenticated software/configuration updates.
- Live capture SHALL implement a documented PAD profile evaluated under ISO/IEC 30107-3 or an approved equivalent.
- Matcher accuracy, threshold selection and demographic performance SHALL be evaluated using ISO/IEC 19795-1 and ISO/IEC 19795-10 principles on a population representative of the pilot.
- Unknown, malformed or oversized payloads SHALL be rejected before deserialisation by a biometric library. Whole-message parser and resource limits from Section 3.1.2 SHALL be enforced before expensive cryptographic or biometric work.
- Replay protection SHALL cover presentation requests, session transcripts, credential offers and QR/device-engagement data.
- Ordinary application, analytics and support logs SHALL NOT contain portraits, protected-template bytes, live samples, biometric scores, full credential payloads, holder names, the RB05 `document_number`, source-document numbers or other persistent holder/credential identifiers. Where a revocation or security audit strictly requires the RB05 serial, it may appear only in a separately justified, access-controlled audit record with an approved purpose and retention period under RB05-D09/D13/D15.
- Security events MAY record a short-lived pseudonymous transaction identifier, component/version, broad outcome code and timestamp.

### 7.2 Mandatory privacy controls

- Participation SHALL be optional and a usable non-biometric route SHALL exist.
- The controller SHALL document necessity and proportionality for every touchpoint. A biometric check SHALL NOT be introduced where identity verification is not otherwise necessary.
- Before creating a reusable RB05 credential, the controller SHALL document why that credential is necessary and proportionate compared with direct transaction-specific disclosure from an accepted portrait-bearing source, ephemeral reference derivation, on-device comparison and the non-biometric route. The assessment SHALL identify the operational or security benefit that remains after accounting for RB05's stable special-category payload and whole-presentation correlation risk; D13 and D17 remain open until this alternatives assessment is approved.
- The responsible controller SHALL complete and approve the DPIA, after consulting the DPO as required, before pilot processing of real biometric data. The DPO's independent advisory role SHALL NOT be replaced by assigning the DPO the controller's decision accountability.
- Controller, joint-controller and processor roles, instructions and deletion duties SHALL be documented before integration testing with real people.
- If an API-mediated mode is used, the DPIA and correlation analysis SHALL cover disclosure of the RB05 attestation type to the mediating API, operating system or browser even though no attribute or value is disclosed; the purpose, recipients, retention, user setting, deletion/uninstallation signalling and cross-device proximity control SHALL be documented and tested.
- The traveller SHALL receive clear information in the required languages and be able to withdraw through an accessible channel.
- Cameras SHALL activate only following the traveller's deliberate action; the capture zone SHOULD minimise or mask bystanders.
- Outside an active holder-authorised transaction, the reusable biometric reference SHALL be stored only in the Wallet Unit. An authorised recipient may process it transiently under Section 4.6 and RB05-D16, but the issuer, airport and airline SHALL NOT retain a reusable central copy or an independently usable decryption key that turns a server-side store into a biometric database.
- Source portraits, unprotected features and issuance copies of the protected reference SHALL be deleted under Section 4.3.
- At verification, disclosed payloads, decrypted/intermediate templates and live samples SHALL remain only in volatile transaction processing and SHALL be rendered inaccessible immediately after the match decision or failure. They SHALL NOT be retained for model training, analytics or later matching.
- A protected template remains biometric personal data. It SHALL NOT be treated as anonymous merely because it is encrypted or transformed.
- A verifier SHALL perform one-to-one comparison only. Indexing RB05 payloads, searching them against a gallery or watch list, or deriving a persistent cross-service identifier is prohibited.

### 7.3 Legal-assessment boundary

The Wallet disclosure screen is a technical approval control, not a substitute for the controller's lawful-basis analysis. The controller and WP7/legal must confirm the applicable GDPR Article 6 basis, Article 9 condition, consent/withdrawal model where used, French legal requirements, data-subject rights, retention and international-transfer position.

The one-to-one restriction is consistent with the holder-controlled architecture favoured in CNIL airport guidance and the EDPB's Opinion 11/2024. That alignment does not make a deployment automatically compliant. The controller must still demonstrate necessity, proportionality and effective safeguards.

One-to-one biometric verification is distinct from remote biometric identification under the EU AI Act, but the complete system and its intended use still require a documented AI Act classification and risk assessment.

## 8 Compliance, deviations and traceability

### 8.1 Standards and regulatory alignment

| Source | RB05 treatment |
| --- | --- |
| Regulation (EU) No 910/2014 as amended by Regulation (EU) 2024/1183 | RB05 is provisionally a non-qualified EAA issued to a Wallet Unit; final legal classification is a governance gate. |
| Commission Implementing Regulation (EU) 2024/2979 as amended by (EU) 2026/1731 | Current EAA format/status requirements are treated as controlling for the pilot profile. |
| Commission Implementing Regulations (EU) 2024/2977 and 2024/2982, as amended by (EU) 2026/1731 | Current portrait-disclosure safeguard and EU-pinned issuance/presentation profiles are applied. |
| ARF v3.0.0, Topic 12 | Unique type, namespaces, mdoc format, device binding, usage, trust, status and rulebook traceability are defined; the category conflict is disclosed. |
| ETSI TS 119 472-1 V1.2.1 | Uses `document_number`, `issue_date`, `issuing_authority_unicode`, identified-subject fields and MSO validity/status rules; prohibits non-qualified mdoc `category` and source-evidence data elements. |
| ISO/IEC 18013-5 | mdoc signing, digest protection, device binding, presentation and proximity structures. |
| ISO/IEC 23220-2 | Generic non-mDL identity data elements and `org.iso.23220.1` namespace. |
| OpenID4VCI 1.0 and HAIP 1.0 | Proposed issuance baseline, subject to APTITUDE RFC-01. |
| OpenID4VP 1.0 and HAIP 1.0 | Proposed remote presentation baseline, subject to APTITUDE RFC-02. |
| ETSI TS 119 472-3 V1.1.1; ETSI TS 119 472-2 V1.2.1; ISO/IEC TS 18013-7:2025 Annex C | Incorporated EUDI issuance and remote mdoc presentation layers take precedence where a generic OpenID/HAIP profile differs. |
| ISO/IEC 24745:2022 | Biometric information protection, including confidentiality, integrity and renewability/revocability. |
| ISO/IEC 30107-3:2023 | PAD evaluation and reporting. |
| ISO/IEC 19795-1:2021 and 19795-10:2024 | Biometric performance and demographic-differential testing. |
| GDPR, CNIL guidance and EDPB Opinion 11/2024 | Data minimisation, holder control, retention, alternatives, DPIA and security constraints. |

### 8.2 Explicit deviations and unresolved conflicts

1. **EU template category wording:** Template v1.5 proposes `eaa:eu:non-qualified`; RB05 omits `category` because ETSI EAA-6.2.2.1-01 prohibits it. An upstream clarification should be requested.
2. **Production identifier:** the Rulebook proposes an identifier but uses `org.example...` in tests until APTITUDE allocation.
3. **Protected-template standard:** no public Apple, Google, IATA, ISO or EUDI specification found in the review defines a drop-in interoperable reusable facial-template credential equivalent to RB05. The implementation-specific format, protection and matcher profiles require specification and validation.
4. **APTITUDE RFC status:** RFC-01, RFC-02, RFC-03 and RFC-04 are project profiles referenced for review and integration alignment, not as final external standards. The exact adopted versions and their application to RB05 remain subject to D08–D10.
5. **Proximity:** no approved APTITUDE RFC-05 exists in the reviewed repository. The current baseline is the applicable non-API-mediated profile in ETSI TS 119 472-2 V1.2.1 with current Implementing Regulation adaptations, building on ISO/IEC 18013-5.
6. **CB-AdES certificate carriage:** ISO/IEC 18013-5:2021 clause 9.1.2.4 expects the document-signer `x5chain` directly in `IssuerAuth`'s unprotected header, while ETSI TS 119 152-1 V1.1.1 clauses 4.4 and 5.1.8 require an unsigned `x5chain` to be nested inside the sole `uHeaders` member of the unprotected map. RB05 makes no dual-conformance claim until RB05-D10 records an authoritative EU/ETSI compatibility interpretation and a passing signed vector.
7. **UC9 architecture and dataset:** the holder-controlled Wallet design, R2 direct presentation and identity-field minimisation remain proposals. Section 1.7 records D4.1's R1 Ready-to-Travel route and storage ambiguity. D02/D11/D12/D18 must resolve the implementation choices; this candidate does not amend D4.1 by itself.

### 8.3 Project traceability

| Artefact | Relationship |
| --- | --- |
| WP4 D4.1 UC9 | Reference for the existing Biometric Profile and Ready-to-Travel scenario. Section 1.7 identifies ambiguities and proposed differences for explicit UC9 review; no agreed source requirement is silently replaced. |
| WP4 D4.2 UC9 integration plan | Implements the agreed UC9 architecture through concrete components, APIs, environments, reader locations, controller/processor roles and end-to-end tests. RB05 is a candidate input, subject to source, storage, dataset and route decisions. |
| RB03 Digital Boarding Pass | Separate travel-entitlement credential; not absorbed by RB05. |
| PID with portrait; PhotoID; WP3 DTC | Candidate trusted portrait sources during enrolment, subject to their exact RB05-D22 acceptance profiles and field mappings; no source credential or data group is copied automatically into RB05. |
| APTITUDE RFC-01 | Issuance flow profile. |
| APTITUDE RFC-02 | Remote presentation profile. |
| APTITUDE RFC-03 | Trust Evaluation profile; alignment to be reviewed under D08/D10. |
| APTITUDE RFC-04 | Revocation and artifact-status profile, after reconciliation with current Implementing Regulation. |
| RB05 CDDL and JSON Schema | Machine-readable representation and validation mirror supplied with this draft. |
| RB05 Test Catalogue | Positive, negative, security and privacy acceptance tests supplied with this draft. |

## Appendix A — Normative conformance summary

An **RB05 Attestation Provider** conforms only if it validates a trusted portrait source, uses an approved protected-template profile, issues the required mdoc fields, binds the credential to the Wallet Unit, provides status/revocation, deletes biometric working copies and never encodes prohibited data.

An **RB05 Wallet Unit** conforms only if it validates issuance, protects the device key and credential, authenticates Relying Parties, gives the holder meaningful control, selectively discloses fields and produces valid device authentication.

An **RB05 credential verifier** conforms only if it validates issuer/device/status/validity, disclosure policy and registered profiles and rejects invalid or replayed evidence. An **R2 checkpoint implementation** additionally performs the approved PAD and one-to-one matching, keeps the travel decision distinct, enforces D18 binding, deletes transaction biometrics and offers the approved fallback. An R1 association provider's consumption of RB05 and the Ready-to-Travel/QR checkpoint have additional route-specific requirements under D12/D18; passing RB05 checks does not establish conformance of those separate artefacts.

Conformance SHALL include the tests applicable to the selected route in the [RB05 Test Catalogue](RB05_TEST_CATALOGUE.md); document review alone is insufficient.

## Appendix B — Production approval gates

| Gate | Required decision | Default if unresolved |
| --- | --- | --- |
| RB05-D01 | WP7/WP2 confirm non-qualified EAA classification and raise the ETSI/template category inconsistency. | No category encoded; no production approval. |
| RB05-D02 | Confirm the legal issuer, holder component, Wallet Provider, airport app role, Relying Party and processor/controller allocation. | Treat all named roles as proposals only. |
| RB05-D03 | Allocate final `docType` and custom namespace and decide the applicable catalogue/discovery path; an APTITUDE index alone is not EU registration. | Test-only identifier; no production issuance or general API-discovery claim. |
| RB05-D04 | Approve the binary template format, exact payload size and profile specification, and publish an authenticated tuple registry with owner, canonical machine-readable location/schema, version/cache/deprecation rules and offline behaviour. | Synthetic test payloads only; no production tuple accepted. |
| RB05-D05 | Approve template protection, encryption, key ownership, processing boundary, renewal, compromise response and measurable attack-test criteria. | No real biometric payload. |
| RB05-D06 | Approve matcher, threshold, PAD, accuracy and demographic-differential evidence. | No biometric acceptance decision. |
| RB05-D07 | Confirm maximum credential lifetime, renewal/replacement sequence, atomicity, recovery and bounded-overlap policy. | Use the proposed 30-day lifetime only in isolated pilot design; no production issuance. |
| RB05-D08 | Publish the exact machine-readable issuer trust source and issuer-certificate profile, including certificate-status mechanism/source, responder or CRL-signer trust, freshness/cache/outage rules, rollover and emergency removal. | Reject all production issuers. |
| RB05-D09 | Select the current credential-status mechanism, publish its exact URL/domain, confirm update/outage and end-of-life status-retention policy, define authenticated/idempotent/auditable revocation intake and event mapping, and decide post-issuance WIA/KA/Wallet revocation propagation. | Reject production verification. |
| RB05-D10 | Confirm issuance and presentation versions/modes and, for HAIP, API-mediated versus redirects-based transmission; exact ISO/IEC 23220-2 field constraints and validity boundaries; whole-message CBOR/parser/resource ceilings and deterministic rejection rules; CB-AdES/digest/signature suite and certificate-carriage resolution; user authentication; required WIA and KA validation within the WUA, issuer-side support for verifying both current WIA/KA status-list and identifier-list mechanisms, and post-issuance status horizon/propagation; signed Issuer Metadata and authenticated/version-bound EDP/reuse policy with fail-closed rollback handling; mandatory ISO/mdoc `requestInfo.euWrprc`; Article 3(4)'s 11 August 2028 application date; RB05's stricter no-bypass pilot rule; exact Relying Party registrar/trust/status/entitlement rules; redirects-based cross-device session-fixation controls if that route is retained; Wallet support; and complete signed test vectors. | No encoded-mdoc or cross-vendor conformance claim; no silent truncation of ISO values. |
| RB05-D11 | Approve the purpose and location of each identity field, including names, `birth_date`, `nationality` and source document/attestation type. | Candidate schema remains names-only; no claim that this minimisation is the approved UC9 dataset. |
| RB05-D12 | Select R1 Ready-to-Travel and/or R2 direct-RB05 for explicitly identified pilot flows; confirm storage, association/reference reuse, separate-artefact specifications and owners. | RB05 remains free of travel data; no route or derived-credential compatibility is assumed approved. |
| RB05-D13 | Complete DPIA, lawful-basis/Article 9 analysis, AI Act assessment, accessibility and non-biometric fallback design. | No real-person pilot. |
| RB05-D14 | Name the Rulebook owner, approvers, review channel and change-control process. | v0.1 remains an unapproved proposal for discussion. |
| RB05-D15 | Approve issuer/processor working-data retention, deletion and evidence. | No real portrait or template processing. The proposed 24-hour ceiling is not the ≤24-hour `shortLived` credential option. |
| RB05-D16 | Fix the checkpoint matching location, recipient interface, key boundary, transient retention and fallback responsibility. | Synthetic interface testing only; no real-person biometric comparison. |
| RB05-D17 | Analyse whole-presentation correlation and select a mitigation with distinct cryptographic material/proofs, or formally approve and tightly scope the residual linkability. | Re-randomising only the template is insufficient. No presentation/cross-RP unlinkability claim and no real-person pilot until the complete transcript risk and controls are approved. |
| RB05-D18 | For each D12-selected route, define and test same-traveller evidence, association or presentation binding, validity/status dependencies, live-match freshness and the current travel decision; name the responsible owner/component/interface. | No automated travel authorisation based on an unvalidated R1 derivation or R2 evidence combination; use manual fallback. |
| RB05-D19 | Define and test integrity-protected same-user continuity from the source presentation/device approval and biometric-processor result to the subject, profile tuple, target Wallet WIA/KA/key and issuance authorisation, including trusted source-verifier and processor evidence paths. | Reject issuance; no production credential or real biometric processing. |
| RB05-D20 | Decide whether and how early source invalidation propagates through a minimal protected dependency record or notification. | Cap expiry at source expiry, revalidate at renewal and make no early-propagation claim. |
| RB05-D21 | Define the measurable UC9 airport operating envelope: devices, lighting/geometry, latency/throughput, connectivity/cache, clock skew, complete-message parser/resource budgets, retries, accessibility and recovery. | Synthetic functional tests only; no operational-readiness or real-person performance claim. |
| RB05-D22 | Approve the source-credential eligibility and validation profile: exact types/formats/versions, portrait and subject-field mapping, issuers/trust/status, freshness, holder/device binding and assurance/downgrade rules. | No production RB05 issuance. |

## References

- APTITUDE, [Definition of Done for Rulebooks](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/definition_of_done/Definition_of_done_Rulebook.md) and [Definition of Done for Attestation Schema](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/definition_of_done/Definition_of_done_Attestation_schema.md).
- European Commission, [EUDI Wallet Architecture and Reference Framework, v3.0.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/releases/tag/v3.0.0).
- ETSI, [TS 119 472-1 V1.2.1 (2026-02)](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.02.01_60/ts_11947201v010201p.pdf), *Profiles for Electronic Attestation of Attributes — Part 1: General requirements*.
- [Regulation (EU) No 910/2014, as amended by Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj).
- Commission Implementing Regulations [(EU) 2024/2977](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02024R2977-20260811), [(EU) 2024/2979](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02024R2979-20260811) and [(EU) 2024/2982](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02024R2982-20260811), as amended by [(EU) 2026/1731](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32026R1731).
- ISO/IEC 18013-5, *Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence application*.
- ISO/IEC TS 18013-7:2025, *Personal identification — ISO-compliant driving licence — Part 7: Mobile driving licence add-on functions*.
- ISO/IEC TS 23220-2:2026, *Cards and security devices for personal identification — Building blocks for identity management via mobile devices — Part 2: Data objects and encoding rules for generic eID systems*.
- ETSI, [TS 119 472-2 V1.2.1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.02.01_60/ts_11947202v010201p.pdf) and [TS 119 472-3 V1.1.1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf).
- ETSI, [TS 119 152-1 V1.1.1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11915201/01.01.01_60/ts_11915201v010101p.pdf) and [TS 119 412-6 V1.1.1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf).
- OpenID Foundation, [OpenID4VCI 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html), [OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) and [HAIP 1.0](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-final.html).
- ISO/IEC 24745:2022, ISO/IEC 30107-3:2023, ISO/IEC 19795-1:2021 and ISO/IEC 19795-10:2024.
- European Data Protection Board, [Opinion 11/2024 on facial recognition to streamline airport passenger flows](https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-112024-on-the-use-of-facial-recognition-to-streamline_en).
- CNIL, [*Reconnaissance faciale dans les aéroports : quels enjeux et quels grands principes à respecter ?*](https://www.cnil.fr/fr/reconnaissance-faciale-dans-les-aeroports-quels-enjeux-et-quels-grands-principes-respecter).
- APTITUDE WP4 D4.1, UC9 material; project profiles [RFC-01 Credential Issuance](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/RFCs/RFC001.md), [RFC-02 Presentation](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/RFCs/RFC002.md), [RFC-03 Trust Evaluation](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/RFCs/RFC003.md) and [RFC-04 Revocation](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/RFCs/RFC004.md). Exact adopted versions remain to be confirmed under D08–D10.
