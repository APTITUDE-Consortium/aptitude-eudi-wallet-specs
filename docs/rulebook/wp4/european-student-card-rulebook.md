# Attestation Rulebook for attestations of type European Student Card

* Author(s):
  * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  * Petros Kavassalis, University of the Aegean, UAegean i4m Lab
* Reviewer(s):
  * Andrijana Todosijevic, SIROS Foundation

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X use case, ERUA-iD materials and the APTITUDE Attestation Rulebook template. |
| 0.2 | 24-07-2026 | Aligned data model and SD-JWT VC encoding with the European Student Card Attestation model. |
| 0.3 | 02-10-2026 | Renamed credential from Student ID / StudentID Attestation to European Student Card Attestation. |
| 0.4 | 18-10-2026 | Clarified that one attestation is one current student affiliation for one validity period, including short enrolments and mobility periods. Recorded the European Student Identifier in `schacPersonalUniqueCode`. Excluded lifelong, alumni, and post-enrolment use. |
| 0.5 | 09-11-2026 | Aligned the legal category, SD-JWT format and type, encoding-independent metadata, presentation checks, status lists, and revocation with the attestation rulebook template and the review of 3 November 2026. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X and ERUA governance processes.

> **Draft status**
>
> This Rulebook defines the European Student Card Attestation for the APTITUDE / SEDIT-X education
> and student-service pilot context. The attribute model, metadata, integrity rules and
> SD-JWT VC encoding below are the normative claim set for this attestation type.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **European Student Card Attestation** for use in the European Digital
Identity Wallet ecosystem.

The European Student Card Attestation expresses the real-world fact that a natural person
holds a student affiliation with an educational organisation during the credential validity
period. It enables relying parties to verify current student status and selected
identity or affiliation attributes using the EUDI Wallet.

The attestation is intended to be issued by an authentic source, such as a university,
higher-education institution, or authorised academic identity provider. The Holder is the
natural person to whom the student status applies. Relying Parties may include campus
service providers, libraries, laboratories, access-control systems, mobility services,
student-discount service providers, ferry or other transport operators accepting student
status, public or private service providers accepting student status, and other
authorised verifiers.

In practical terms, the attestation enables a student to present proof of student status
through an EUDI Wallet using selective disclosure. It can reduce reliance on physical
student cards, manual checks, or real-time backend lookups, provided that the relying
party can verify the issuer, credential signature, validity period, credential status
where applicable, and the disclosed attributes needed for the transaction.

The attestation supports education and student-service use cases, including remote
presentation and local verification without a call to the issuer, for campus services,
discounted services, access control, mobility scenarios, academic services, and other
scenarios where proof of student affiliation is required. Section 1.5 defines the
boundary with person identity, later enrolments, and lifelong-learning records.
Section 3.1 records that internet-free proximity presentation is not supported in this
version.

The credential is an **identity and affiliation credential**. It SHALL NOT be interpreted
as proof of:

* completion of a course or programme;
* academic grades or credit achievement;
* award of a diploma, degree or micro-credential;
* payment completion; or
* entitlement to every service offered by the issuing institution.

Academic achievements SHALL be represented through separate credentials such as a
Transcript of Records, diploma, diploma supplement, micro-credential, badge or other
achievement credential.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 describes the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 specifies how the attestation attributes and metadata are encoded using SD-JWT VC. ISO/IEC 18013-5 and W3C VCDM encodings are not defined in this version of the Rulebook.
* Chapter 4 specifies attestation usage, including presentation and verification expectations.
* Chapter 5 defines how trust anchors for attestation verification can be obtained.
* Chapter 6 defines revocation and expiry mechanisms.
* Chapter 7 provides compliance information.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and options
specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e.,
a requirement that is not mandated by this document, but, for instance, by an external
document. The word 'can' indicates a capability, whereas other words, such as 'will',
and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

In addition, the following domain-specific terms are used:

| Term | Meaning |
|------|---------|
| European Student Card Attestation | A Verifiable Credential representing one current student affiliation with one educational organisation, for one validity period, together with selected student identity attributes. |
| Educational organisation | A university, higher-education institution, or other authorised academic organisation acting as the authentic source for student status. |
| Authorised academic identity provider | A system or organisation authorised by an educational organisation to issue or manage student identity attestations. |
| Student | The natural person who holds a current student affiliation with the issuing educational organisation for the validity period of the attestation. |
| European Student Identifier | A higher-education student identifier carried as a SCHAC `schacPersonalUniqueCode` URN of the form `urn:schac:personalUniqueCode:int:esi:<scope>:<code>`. It identifies the same student across institutions for mobility and related higher-education services. It is not a lifelong identity, and it does not by itself prove that an enrolment is still current. |
| Relying Party | An organisation or system that verifies the European Student Card Attestation to make an access, eligibility, discount, or service decision. |
| SCHAC | Schema for Academia, a set of attributes commonly used in research and education identity federations. |
| eduPerson | A set of attributes commonly used to represent persons and affiliations in education and research identity federations. |

### 1.5 Scope boundaries

One European Student Card Attestation represents one current student affiliation with one
educational organisation for one validity period. A later enrolment, or an enrolment at
another organisation, is a separate attestation. Where a person holds several current
affiliations, the Holder may hold several attestations and present the one a transaction
requires.

The Holder's persistent identity is a PID or another accepted identity attestation. This
attestation does not replace that identity. Where strong holder matching is required, this
attestation SHOULD be cryptographically bound to it, as specified in Sections 2.6 and 4.
The Holder controls whether to present an attestation and which selectively disclosable
claims to release. The educational organisation remains the authentic source of the
affiliation.

The following are out of scope:

* lifelong validity, or any use as proof of student status after the attested affiliation has ended;
* alumni, professional, or other post-enrolment status;
* persons with no current student affiliation at an issuing educational organisation, including prospective students who have not been admitted and learners with no institutional enrolment;
* identification before enrolment, other than presentation of an attestation already issued by the student's home organisation;
* diplomas, grades, micro-credentials, and other achievement or qualification records, which are separate attestations and bind to the Holder through the wallet identity;
* individual learning accounts and training entitlements.

Employers, informal-learning providers, and organisations that are not the authentic source
of the subject's student status SHALL NOT issue this attestation type. Only the applicable
trust framework MAY authorise an additional provider type. This Rulebook does not create
that authorisation, and it does not define a provider-independent learner identity.

Council Recommendation 2022/C 243/02, Council Recommendation 2022/C 243/03, and the
proposed Skills Portability Act concern learning achievements, training entitlements, and
digital qualification attestations across a person's life. Those instruments sit beside
this attestation in the wallet. They do not extend the validity of a student affiliation
beyond the enrolment it attests.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a European Student Card Attestation may
contain. The attributes are defined in an encoding-independent manner. Each attribute is
classified as mandatory, optional, or conditional.

The European Student Card Attestation is valid for the affiliation it attests. That period
MAY be an academic year, a mobility period, or a shorter enrolment. During that period it
is intended for repeated presentation with selective disclosure. The attribute set is
designed to support data minimisation by allowing a Holder to disclose only the student
attributes required for a specific transaction.

### 2.1 Introduction

The European Student Card Attestation is defined as a non-qualified Electronic Attestation of
Attributes unless a future version of this Rulebook explicitly defines a qualified or
public-sector legal category.

The attribute `category` SHALL be included and SHALL have the value
`eaa:eu:non-qualified`.

The attestation model consists of the following logical groups:

* student identification attributes;
* organisation attributes;
* core identity attributes for holder matching;
* contact attributes;
* affiliation and status attributes;
* credential metadata.

The attestation is issued as a Verifiable Credential compatible with the EUDI Wallet
using SD-JWT VC. The model aligns with the following issuer metadata parameters:

* `scope`: `EuropeanStudentCard`;
* `format`: `dc+sd-jwt`;
* `vct`: `urn:eudi:aptitude:european-student-card:1`;
* `claims`: the claims defined in this Rulebook;
* `proof_types_supported`: issuer-defined, including `jwt` where supported;
* `cryptographic_binding_methods_supported`: issuer-defined, for example `jwk` or
  `cose_key`.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `category` | ETSI TS 119 472-1 / Rulebook template | Indicates the legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `identifier` | Institutional student identifier | Unique student identifier, such as an institutional student number or equivalent. | string | `STU-2026-000123` |
| `schacHomeOrganization` | SCHAC `schacHomeOrganization` | Home organisation or institution domain or identifier. | string | `aegean.gr` |
| `firstName` | OIDC `given_name` where applicable | Student given name. | string | `Nikos` |
| `familyName` | OIDC `family_name` where applicable | Student family name. | string | `Triantafyllou` |
| `eduPersonPrincipalName` | eduPerson `eduPersonPrincipalName` | Principal name of the student, often expressed in `user@realm` format. | string | `ntriantafyllou@aegean.gr` |
| `eduPersonPrimaryAffiliation` | eduPerson `eduPersonPrimaryAffiliation` | Primary affiliation of the subject with the educational organisation. | string | `student` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `schacPersonalUniqueID` | SCHAC `schacPersonalUniqueID` | One or more unique identifiers for the student. | array of strings | `["urn:schac:personalUniqueID:gr:student:123456"]` |
| `displayName` | OIDC `name` or education profile display name | Display name formatted for user interfaces. | string | `Nikos Triantafyllou` |
| `commonName` | Common name / CN | Alternate display or preferred name. | string | `Nikos Triantafyllou` |
| `eduPersonAffiliation` | eduPerson `eduPersonAffiliation` | One or more affiliations, such as `student`, `member`, or `affiliate`. | array of strings | `["student", "member"]` |
| `eduPersonScopedAffiliation` | eduPerson `eduPersonScopedAffiliation` | One or more scoped affiliation values. | array of strings | `["student@aegean.gr"]` |
| `eduPersonAssurance` | eduPerson `eduPersonAssurance` | One or more assurance values for the subject or attributes. | array of strings | `["https://refeds.org/assurance"]` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `schacPersonalUniqueCode` | SCHAC `schacPersonalUniqueCode` / European Student Identifier | SHALL be included when the issuer has assigned a European Student Identifier to the subject. The value SHALL be that ESI as a SCHAC URN. An issuer that assigns an ESI SHOULD reuse the same value on later attestations of the same student. | string | `urn:schac:personalUniqueCode:int:esi:example.edu:123456` |
| `dateOfBirth` | ISO 8601 date / OIDC `birthdate` where applicable | The issuer SHALL include `dateOfBirth` only when it is required for holder matching or for an age-related eligibility rule known at issuance. If included, it SHALL represent the subject's birth date and SHALL NOT be in the future. Section 4 defines when a Relying Party may request it. | date | `1990-04-12` |
| `mail` | RFC 5322 mailbox | The issuer MAY include `mail` as a contact address. Section 4 defines when a Relying Party may request it. | string | `ntriantafyllou@aegean.gr` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| credential type | SD-JWT VC `vct` | Verifiable Credential Type identifying this attestation type. Section 3.2 maps this attribute to `vct`. | string | `urn:eudi:aptitude:european-student-card:1` |
| issuer | SD-JWT VC / JWT `iss` | Identifier of the issuer of the credential. Section 3.2 maps this attribute to `iss`. | string | `https://issuer.example-university.edu` |
| issue time | JWT `iat` | Time at which the credential was issued. Section 3.2 maps this attribute to `iat`. | integer | `1772366400` |
| expiry time | JWT `exp` | Expiration time of the credential. For this attestation it SHOULD reflect the end of the applicable student-status validity period, such as an academic year, a mobility period, or a shorter enrolment. Section 3.2 maps this attribute to `exp`. | integer | `1798761600` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| not before | JWT `nbf` | Time before which the credential MUST NOT be accepted. Section 3.2 maps this attribute to `nbf`. | integer | `1772366400` |
| credential instance identifier | JWT `jti` | Unique identifier of the credential instance. Section 3.2 maps this attribute to `jti`. | string | `urn:uuid:4f6a8e9a-40c2-4d21-96f8-7b85cc3f6c20` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/education/institutions/example-university` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `status_list_index` | Token Status List `status.status_list.idx` | SHALL be present when the credential is valid for more than 24 hours. Non-negative integer index of this credential in the issuer's Token Status List. The issuer SHALL assign the index at random. | integer | `4127` |
| `status_list_uri` | Token Status List `status.status_list.uri` | SHALL be present when `status_list_index` is present. HTTPS URI of the Token Status List, on a domain the issuer controls or a domain the trust framework operates for the issuer. | string | `https://status.example-university.edu/esc/1` |
| holder binding | SD-JWT VC / JOSE `cnf` | SHALL be present when the attestation is bound to key material controlled by the Holder or Wallet Unit. Section 3.2 maps this attribute to `cnf`. The attestation SHOULD be holder-bound where the wallet and the SD-JWT VC profile support it, as specified in Section 4. | object | `{ "jwk": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the European Student Card Attestation must be presented together with PID or another identity attestation for strong holder matching. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `dateOfBirth` | ISO 8601 date values | Subject's date of birth. | ISO 8601 | Date-only format `YYYY-MM-DD` SHALL be used where possible. |
| `mail` | RFC 5322-compliant mailbox strings | Email address. | RFC 5322 | Implementations SHOULD apply practical email validation appropriate for the issuing context. |
| `schacPersonalUniqueCode` | SCHAC URN; European Student Identifier values use `urn:schac:personalUniqueCode:int:esi:<scope>:<code>` | Cross-institutional student identifier, where assigned. | SCHAC / European Student Identifier | `<scope>` is a country code or the `schacHomeOrganization` domain, as required for the identifier to be globally unique. The value identifies the student. Current enrolment is expressed by `eduPersonPrimaryAffiliation` together with the credential validity period. |
| `schacHomeOrganization` | Issuer-defined organisation identifiers, commonly domain-style values | Identifies the home educational organisation. | SCHAC / issuer-defined controlled values | Values SHOULD be stable and consistently interpreted across issuers and relying parties. |
| `eduPersonPrimaryAffiliation` | Issuer-defined controlled vocabulary; the value for this attestation is `student` or an issuer-defined student-equivalent | Primary affiliation of the subject. | eduPerson / issuer-defined controlled values | The value SHALL indicate current student status. A former-affiliation value, including `alum`, SHALL NOT be used. |
| `eduPersonAffiliation` | Issuer-defined controlled vocabulary; examples include `student`, `member`, `affiliate` | One or more affiliations of the subject. | eduPerson / issuer-defined controlled values | Values SHOULD be consistent with `eduPersonPrimaryAffiliation`. |
| `eduPersonScopedAffiliation` | Scoped affiliation strings, commonly `affiliation@scope` | Affiliation value scoped to an organisation or domain. | eduPerson / SCHAC context | Scope SHOULD be consistent with `schacHomeOrganization`. |
| `eduPersonAssurance` | Assurance URIs or issuer-defined assurance values | Assurance information for the subject or attributes. | eduPerson / REFEDS or issuer-defined assurance framework | Additional values SHOULD only be used if documented by the issuer or trust framework. |
| `category` | `eaa:eu:non-qualified`, `urn:etsi:esi:eaa:eu:qualified`, `urn:etsi:esi:eaa:eu:pub` | Indicates the legal category of the attestation. | ETSI TS 119 472-1 / Rulebook template | This Rulebook uses `eaa:eu:non-qualified`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `ESC-IR-01` | `identifier`, `firstName`, `familyName`, `schacHomeOrganization`, `eduPersonPrincipalName`, and `eduPersonPrimaryAffiliation` SHALL be present in the issued credential. | Ensures that the issued credential contains the mandatory student identification, organisation, identity, and affiliation data. | Issuer business rules and schema validation. | Issuer SHALL reject incomplete credential data. |
| `ESC-IR-02` | If `dateOfBirth` is included, it SHALL represent the subject's birth date and SHALL NOT be in the future. | Prevents invalid identity data and supports correct age-related or matching checks. | Issuer business rules and verifier business validation. | Issuer SHALL reject invalid dates. Verifier SHALL reject or ignore an invalid `dateOfBirth` claim depending on the transaction. |
| `ESC-IR-03` | If `eduPersonScopedAffiliation` values are included, they SHOULD be consistent with `schacHomeOrganization`, for example by using a matching scoping domain. | Ensures that scoped affiliation can be interpreted consistently. | Issuer business rules and verifier business validation. | Issuer SHOULD prevent inconsistent scoped affiliations. Verifier MAY reject or downgrade confidence in inconsistent values. |
| `ESC-IR-04` | If `eduPersonAffiliation` is present, it SHOULD include the value of `eduPersonPrimaryAffiliation`. | Ensures that the primary affiliation is consistent with the broader affiliation list. | Issuer business rules and verifier business validation. | Issuer SHOULD align the values. Verifier MAY treat inconsistent affiliation data as insufficient. |
| `ESC-IR-05` | If `schacPersonalUniqueID` is multi-valued, each entry SHOULD be unique within the array. | Prevents duplicate identifiers and ambiguity. | Issuer business rules and schema validation. | Issuer SHOULD remove duplicates. Verifier MAY ignore duplicate entries. |
| `ESC-IR-06` | Selective disclosure SHALL allow the Holder to reveal only the attributes required for the transaction. | Supports privacy and data minimisation. | Issuer credential construction and Wallet presentation logic. | Verifier SHALL request only necessary claims. Wallet SHOULD allow the Holder to review the disclosed claims. |
| `ESC-IR-07` | `eduPersonPrimaryAffiliation` SHALL be `student` or an issuer-defined student-equivalent value. A value that indicates a former affiliation, including `alum`, SHALL NOT be used. | Ensures that the attestation represents current student status and cannot be kept as an alumni or post-enrolment credential. | Issuer business rules and verifier business validation. | Issuer SHALL NOT issue this attestation type with a primary affiliation that does not indicate current student status. Verifier SHALL reject the credential for student-status decisions if the affiliation does not indicate current student status. |
| `ESC-IR-08` | When the issuer has assigned a European Student Identifier, `schacPersonalUniqueCode` SHALL contain that identifier as a SCHAC ESI URN, and the issuer SHOULD reuse the same value on later attestations of the same student. | Gives mobility and alliance verifiers a stable student identifier without treating that identifier as lifelong identity or as proof of current enrolment. | Issuer business rules and verifier business validation. | Issuer SHALL include the assigned ESI. Verifier SHALL NOT treat a missing ESI as a failed enrolment check. Verifier SHALL NOT treat the ESI alone as proof that the affiliation is current. |
| `ESC-IR-09` | The verifier SHALL treat a presentation as insufficient when a claim it requested, and that its decision requires, is absent or invalid. Absence of a selectively disclosable claim that the verifier did not request SHALL NOT by itself make the presentation invalid. A student-status or discount decision SHALL accept a presentation of `eduPersonPrimaryAffiliation` and `schacHomeOrganization`, together with the non-disclosable validation data: issuer, credential type, validity, signature, and status and holder binding where those mechanisms are used. | Selective disclosure allows the Holder to withhold claims the verifier did not request. The discount example in Section 4 depends on this. | Verifier business validation. | Verifier SHALL reject the presentation when a requested decision-critical claim is missing or invalid. Verifier SHALL NOT reject it solely because an unrequested selectively disclosable claim is absent. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the
European Student Card Attestation.

This version does not support presentation when the Wallet Unit and the Relying Party
are in proximity and no internet connection is available. The attestation is issued
only as an SD-JWT VC and is presented with OpenID4VP. That protocol needs internet
connectivity between the Wallet Unit and the Relying Party. An ISO/IEC 18013-5 mdoc
profile would be required before internet-free proximity presentation could be
supported. This is the outcome of the analysis required by ARB_02. Verification
without a real-time call to the issuer remains in scope when the verifier can
validate the signature and issuer from a trust anchor it already holds, and can
apply the status rules in Section 6.

If a future version of this Rulebook defines an
ISO/IEC 18013-5-compliant mdoc representation, that version SHALL define a unique
document type, namespaces, attribute identifiers, CBOR encoding rules, and
illustrative mdoc examples.

### 3.2 SD-JWT VC-based encoding

The European Student Card Attestation SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
urn:eudi:aptitude:european-student-card:1
```

This value is a collision-resistant name under the APTITUDE scheme provider's control.
An incompatible change to the claim set, claim semantics, or integrity rules SHALL use
a new `vct`. A compatible clarification MAY keep this value. The scheme provider MAY
replace this value with another URI under its control; that replacement SHALL be
recorded in this Rulebook.

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP
conventions where applicable. Claim names are either IANA-registered JWT claims,
public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or
MUST NOT make the claim selectively disclosable.

#### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| issuer | `iss` | string | JWT issuer identifier. | MUST NOT |
| issue time | `iat` | integer | Issued-at timestamp. | MUST NOT |
| not before | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| expiry time | `exp` | integer | Expiration timestamp. SHOULD reflect the end of the applicable student-status validity period. | MUST NOT |
| credential instance identifier | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| holder binding | `cnf` | object | Holder binding confirmation claim. SHALL be present when the attestation is bound to Holder key material. | MUST NOT |
| `status_list_index` | `status.status_list.idx` | integer | Entry index in the Token Status List. SHALL be present when the credential is valid for more than 24 hours. The issuer SHALL assign it at random. | MUST NOT |
| `status_list_uri` | `status.status_list.uri` | string | HTTPS URI of the Token Status List. SHALL be present when `status_list_index` is present. | MUST NOT |
| credential type | `vct` | string | SD-JWT VC type. Value SHALL be `urn:eudi:aptitude:european-student-card:1`. | MUST NOT |

#### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `firstName` | `firstName` | string | Student given name. May be mapped to OIDC `given_name` in implementations that use OIDC naming conventions. | MUST |
| `familyName` | `familyName` | string | Student family name. May be mapped to OIDC `family_name` in implementations that use OIDC naming conventions. | MUST |
| `displayName` | `displayName` | string | Display name formatted for user interfaces. | MAY |
| `commonName` | `commonName` | string | Alternate display or preferred name. | MAY |
| `dateOfBirth` | `dateOfBirth` | string | Date of birth formatted as ISO 8601 date, where disclosed. | MAY |
| `mail` | `mail` | string | Email address. | MAY |

#### 3.2.3 Private claims specific to the European Student Card Attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `category` | `category` | string | SHALL be `eaa:eu:non-qualified`. | MUST NOT |
| `identifier` | `identifier` | string | Unique student identifier, such as institutional student number or equivalent. | MUST |
| `schacPersonalUniqueCode` | `schacPersonalUniqueCode` | string | European Student Identifier, where assigned, as a SCHAC ESI URN. | MUST |
| `schacPersonalUniqueID` | `schacPersonalUniqueID` | array of strings | One or more unique identifiers for the student. | MAY |
| `schacHomeOrganization` | `schacHomeOrganization` | string | Home organisation or institution domain or identifier. | MUST |
| `eduPersonPrincipalName` | `eduPersonPrincipalName` | string | Principal name, often in `user@realm` format. | MAY |
| `eduPersonPrimaryAffiliation` | `eduPersonPrimaryAffiliation` | string | Primary affiliation, expected to indicate student status. | MUST |
| `eduPersonAffiliation` | `eduPersonAffiliation` | array of strings | One or more affiliations. | MAY |
| `eduPersonScopedAffiliation` | `eduPersonScopedAffiliation` | array of strings | One or more scoped affiliation values. | MAY |
| `eduPersonAssurance` | `eduPersonAssurance` | array of strings | One or more assurance values for the subject or attributes. | MAY |
| `trust_anchor` | `trust_anchor` | string | Location or identifier of the trust anchor or trust framework entry used to verify issuer authorisation, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Identifier of another attestation type to which this attestation is bound, where used. | MUST NOT |

#### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-university.edu",
  "iat": 1772366400,
  "nbf": 1772366400,
  "exp": 1798761600,
  "jti": "urn:uuid:4f6a8e9a-40c2-4d21-96f8-7b85cc3f6c20",
  "vct": "urn:eudi:aptitude:european-student-card:1",
  "category": "eaa:eu:non-qualified",
  "identifier": "STU-2026-000123",
  "schacPersonalUniqueCode": "urn:schac:personalUniqueCode:int:esi:example.edu:123456",
  "schacPersonalUniqueID": [
    "urn:schac:personalUniqueID:gr:student:123456"
  ],
  "schacHomeOrganization": "aegean.gr",
  "firstName": "Nikos",
  "familyName": "Triantafyllou",
  "displayName": "Nikos Triantafyllou",
  "commonName": "Nikos Triantafyllou",
  "dateOfBirth": "1990-04-12",
  "mail": "ntriantafyllou@aegean.gr",
  "eduPersonPrincipalName": "ntriantafyllou@aegean.gr",
  "eduPersonPrimaryAffiliation": "student",
  "eduPersonAffiliation": [
    "student",
    "member"
  ],
  "eduPersonScopedAffiliation": [
    "student@aegean.gr"
  ],
  "eduPersonAssurance": [
    "https://refeds.org/assurance"
  ],
  "trust_anchor": "https://trust.example.eu/education/institutions/example-university",
  "status": {
    "status_list": {
      "idx": 4127,
      "uri": "https://status.example-university.edu/esc/1"
    }
  },
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  }
}
```

#### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be
generated by the issuer using the applicable signing algorithm, disclosure
construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

#### 3.2.6 Example human-readable disclosed payload

A verifier that requests only proof of student status for a discounted service may
receive a presentation disclosing the following claims:

```json
{
  "vct": "urn:eudi:aptitude:european-student-card:1",
  "identifier": "STU-2026-000123",
  "schacHomeOrganization": "aegean.gr",
  "firstName": "Nikos",
  "familyName": "Triantafyllou",
  "eduPersonPrimaryAffiliation": "student",
  "eduPersonScopedAffiliation": [
    "student@aegean.gr"
  ]
}
```

The example above is one possible presentation. A verifier that only needs to know
whether the Holder has student status SHALL accept `eduPersonPrimaryAffiliation` and
`schacHomeOrganization`, and SHOULD NOT request `dateOfBirth`, `mail`, unique
identifiers, `eduPersonScopedAffiliation`, or `eduPersonAssurance` unless the
transaction requires them.

The issuer identity, credential type, expiry time, signature, holder binding proof,
status list index and URI where present, and trust anchor information are not treated
as selectively disclosable student attributes and SHALL remain available to the
verifier for technical validation.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model
encoding for the European Student Card Attestation.

If a future version defines a W3C VCDM representation, that version SHALL define the
credential context, type, credential subject structure, proof type, selective disclosure
mechanism, and presentation requirements.

## 4 Attestation usage

The European Student Card Attestation is intended for verifying student status and selected student
identity or affiliation attributes.

Typical usage scenarios include:

* presentation by the student for campus services such as libraries, laboratories,
  rooms, buildings, or academic platforms;
* presentation for student discounts or eligibility checks, including ferry or other
  transport discounts where student status is accepted;
* presentation for mobility scenarios involving another educational organisation or
  service provider;
* online verification by a service provider using remote presentation protocols;
* local verification without a call to the issuer, where the verifier already holds
  the trust anchor and a status list that is still within its cache period, and can
  validate the credential signature, issuer, validity period, status, and disclosed
  attributes.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`);
* the issuer authorisation to issue European Student Card Attestations;
* the credential validity period;
* the credential status, as specified in Section 6, when the attestation is valid for more than 24 hours;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the disclosed student attributes are sufficient for the relying-party decision.

The Relying Party SHOULD request and verify PID or another accepted identity credential
where the transaction requires strong identity matching. For low-risk student-status
checks, the Relying Party MAY rely on the European Student Card Attestation alone, provided that the
issuer, signature, validity, status, and holder binding checks are successful and this
is consistent with the relying party's policy.

The Relying Party SHALL apply data minimisation and SHALL request only the attributes
required for the transaction. A discount or eligibility check that only needs current
student status and the home organisation SHALL accept a presentation of
`eduPersonPrimaryAffiliation` and `schacHomeOrganization`. An account-linking process
may require `eduPersonPrincipalName` or `mail`. A mobility or alliance verifier
SHALL request `schacPersonalUniqueCode` only where the transaction requires the European
Student Identifier. The Relying Party SHALL request `dateOfBirth` only where the
transaction requires holder matching or an age check, and SHALL request `mail` only
where it requires a contact address or account matching. The Relying Party SHOULD
request `eduPersonScopedAffiliation` only where it needs both the affiliation value
and the organisational scope, and SHOULD request `eduPersonAssurance` only where it
needs assurance information to decide whether the credential is sufficient for the
service.

A successful verification proves the disclosed affiliation for the credential validity
period. It does not prove lifelong student status, eligibility to enrol at another
organisation, or a qualification. A person who is not yet enrolled is identified with a
PID or another accepted identity attestation. A later enrolment, including enrolment after
a previous affiliation has ended, is issued as a new attestation.

The attestation SHOULD be device-bound through holder binding where supported by the
EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be
cryptographically bound to a PID or another accepted identity attestation where strong
identity matching is required. Where this binding is used, the metadata attribute
`cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the European Student Card
Attestation is used as part of a transaction that also involves payment,
payment-related requirements SHALL be defined in a separate payment attestation,
payment profile, or transaction-specific rulebook.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer of the European Student Card Attestation is authorised
to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor
information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant education or
  EUDI Wallet ecosystem;
* an issuer metadata endpoint published by the educational organisation or authorised
  academic identity provider;
* a trust framework entry managed by APTITUDE WP2 or by another authorised governance
  body;
* a pilot trust list used for controlled interoperability testing;
* a federation or sectoral trust framework used by research and education identity
  providers, where applicable.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the location
or registry entry from which the Relying Party can obtain the issuer trust anchor or
issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered
  trust anchor;
* the issuer is authorised to issue the `urn:eudi:aptitude:european-student-card:1` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the
  trust framework;
* the issuer is an educational organisation or authorised academic identity provider for
  the relevant student population.

Employers, informal-learning providers, and other organisations that are not the authentic
source of the subject's student status SHALL NOT be accepted as issuers of this
attestation type. A trust framework MAY authorise a further provider type. This Rulebook
does not grant that authorisation.

Wallet Units MAY also use the same trust framework information during issuance to
determine whether the provider is authorised to issue this attestation type.

## 6 Revocation

The European Student Card Attestation is intended for repeated presentation during the
affiliation it attests, whether that is an academic year, a mobility period, or a shorter
enrolment.

The credential expiration time (`exp`) SHOULD be aligned with the end of the applicable
student-status validity period, such as the end of an academic year, enrolment period,
mobility period, or other issuer-defined validity period.

An attestation whose validity period is 24 hours or less MAY omit status information
and rely on expiry. An attestation that is valid for more than 24 hours SHALL be
revocable. The issuer SHALL then include `status_list_index` and `status_list_uri`,
encoded as `status.status_list.idx` and `status.status_list.uri`, and SHALL implement
the Token Status List mechanism. The issuer SHALL assign `status.status_list.idx` at
random. The issuer SHALL publish each Token Status List at an HTTPS URI on a domain
it controls, or on a domain the trust framework operates for it. That URI is
`status.status_list.uri`. Retrieving the list SHALL NOT require authentication.
If APTITUDE WP2 later operates a shared status service, this Rulebook will name that
domain.

A verifier SHOULD download each new list once, outside the presentation, cache it,
and set a maximum cache period by risk analysis. It MAY rely on that cache while the
cache is still within the list validity and within that period. It SHOULD NOT fetch
the list during the presentation itself. If the cache is missing or stale, the status
check has not succeeded. The verifier SHALL then accept or refuse only under a
documented risk analysis. For a decision that the Holder is currently a student, a
stale or missing list SHOULD lead to refusal.

If the attestation is revocable, the issuer SHALL revoke it when its compromise is
confirmed, and when the value of an attribute is added, removed, or changed while at
least 24 hours of validity remain. A report that the credential may be compromised
SHALL start an investigation and MAY lead to suspension. Confirmation of compromise
is what requires revocation.

The issuer SHALL also revoke or suspend the attestation when the student is no longer
enrolled, the credential was issued incorrectly, or the student identifier is no
longer valid for presentation. Where at least 24 hours of validity remain, that
action SHALL be revocation. Where the Holder's contact details are known, the issuer
SHOULD tell the Holder, out of band, about the revocation and SHOULD ask the Holder
to request a new attestation when the affiliation is still current. A later enrolment
is a new attestation. Where the issuer previously assigned a European Student
Identifier, the new attestation SHOULD carry the same `schacPersonalUniqueCode`.

The issuer SHALL NOT extend this attestation, and SHALL NOT issue this attestation
type, to represent lifelong, alumni, or post-enrolment status.

## 7 Compliance

This Rulebook is designed to align with the EUDI Wallet architectural approach for
Electronic Attestations of Attributes and with the Attestation Rulebook structure
defined in the ARF.

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope;
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner;
* it defines a legal category indication through `category`;
* it defines an SD-JWT VC `vct` value for the attestation type;
* it defines issuer, validity, and status metadata needed for verification;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors can be obtained and used;
* it defines expiry and revocation expectations, including the Token Status List location and the rule for a stale cache;
* it supports selective disclosure and data minimisation;
* it records that internet-free proximity presentation is not supported in this version.

This Rulebook does not define a qualified EAA or public-sector EAA profile. It also does
not define ISO/IEC 18013-5 mdoc or W3C VCDM encodings in this version.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X] | APTITUDE WP4 SEDIT-X education and student-service materials |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [OIDC] | OpenID Connect Core 1.0 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [Token Status List] | IETF OAuth Token Status List, `draft-ietf-oauth-status-list`. Attestation Status List mechanism for SD-JWT VC. |
| [SCHAC] | Schema for Academia attributes used in research and education identity contexts |
| [eduPerson] | eduPerson schema attributes used in research and education identity contexts |
| [European Student Identifier] | European Student Identifier, carried as SCHAC `schacPersonalUniqueCode`, `urn:schac:personalUniqueCode:int:esi:<scope>:<code>` |
| [Council Recommendation 2022/C 243/02] | Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability |
| [Council Recommendation 2022/C 243/03] | Council Recommendation of 16 June 2022 on individual learning accounts |
| [COM(2026) 992] | Proposal for a Regulation on portability of qualifications and skills (Skills Portability Act), 15 September 2026. Informative only: digital qualification attestations are a separate attestation type. |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 5322] | Internet Message Format |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes; building blocks and general requirements |
