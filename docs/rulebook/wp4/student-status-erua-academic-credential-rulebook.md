# Attestation Rulebook for attestations of type Student Status / ERUA Academic Credential

* Author(s):
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X use case, ERUA-iD materials, the European Student Card VC pilot context and the APTITUDE Attestation Rulebook template. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X and ERUA governance processes.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The available SEDIT-X material
> defines the credential at a high level as a Student Status Credential issued by a
> participating university or alliance authority and used for verified discounts,
> university access and federated campus services. ERUA materials additionally
> distinguish an Educational ID, proving institutional affiliation, from an Alliance ID,
> proving ERUA membership.
>
> This draft defines a unified **Student Status / ERUA Academic Credential** pilot profile
> that can carry both institutional student status and ERUA alliance affiliation. This
> unification is a proposed harmonisation, not yet a formally approved ERUA or APTITUDE
> data model. A deployment MAY instead issue Educational ID and Alliance ID as separate
> attestations, provided equivalent semantics and verification outcomes are preserved.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Student Status / ERUA Academic Credential**, an Electronic
Attestation of Attributes stored in a student's EUDI Wallet.

The credential provides portable proof that its holder:

1. has a current student relationship with a recognised Higher Education Institution;
2. belongs to, or is eligible to participate in, the European Reform University Alliance
   (ERUA), where applicable; and
3. may exercise explicitly stated student or alliance service entitlements during the
   credential's validity period.

The credential is intended to support privacy-preserving verification in contexts such as:

* student discounts for ferry or other transport services;
* access to ERUA and university online services;
* campus, library, laboratory, event or facility access;
* event and course registration;
* attendance and Tap2Enter-style services;
* student meal or cafeteria eligibility;
* participation in alliance activities;
* mobility and visiting-student scenarios; and
* other services requiring proof of current student status or ERUA affiliation.

The credential is an **identity and affiliation credential**. It SHALL NOT be interpreted
as proof of:

* completion of a course or programme;
* academic grades or credit achievement;
* award of a diploma, degree or micro-credential;
* payment completion; or
* entitlement to every service offered by the issuing institution or alliance.

Academic achievements SHALL be represented through separate credentials such as a
Transcript of Records, diploma, diploma supplement, micro-credential, badge or other
achievement credential.

### 1.2 Relationship to Educational ID, Alliance ID and European Student Card

ERUA-iD materials define two core credential concepts:

* **Educational ID**, confirming affiliation with the holder's Higher Education Institution;
* **Alliance ID**, confirming membership or participation in ERUA.

The European Student Card Verifiable Credential provides another portable proof of
student status and may be issued through an ESC Router-based or decentralised flow.

This Rulebook defines a common semantic profile that can be implemented in either of
these deployment patterns:

1. **Unified credential:** one Student Status / ERUA Academic Credential contains both
   institutional student status and ERUA affiliation.
2. **Separate credentials:** an Educational ID or ESC VC proves student status, while an
   Alliance ID separately proves ERUA affiliation.
3. **Student-status-only credential:** a participating university issues student status
   without ERUA affiliation for services where alliance membership is irrelevant.

A Relying Party SHALL request only the credential or attributes required for the service.
It SHALL NOT require ERUA affiliation where proof of ordinary student status is sufficient.

### 1.3 Document structure

This Rulebook is structured as follows:

* Chapter 2 defines the attestation attributes and metadata in an
  encoding-independent manner.
* Chapter 3 defines the SD-JWT VC encoding and discusses optional mdoc support.
* Chapter 4 specifies issuance, presentation and verification usage.
* Chapter 5 defines how trust anchors are obtained.
* Chapter 6 specifies validity, status and revocation.
* Chapter 7 describes compliance with the EUDI Wallet framework and ERUA/SEDIT-X
  privacy requirements.
* Chapter 8 lists references.

### 1.4 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119].

In addition, *must* in lower case indicates an external constraint that is not established
by this Rulebook. The word *can* indicates a capability. Other words such as *will*,
*is* and *are* are statements of fact.

### 1.5 Terminology

This document uses the terminology specified in Annex 1 of the EUDI Wallet Architecture
and Reference Framework.

For this Rulebook:

* **Home institution** means the recognised Higher Education Institution at which the
  student holds the relevant student relationship.
* **ERUA affiliation** means a verified relationship with ERUA derived from membership
  in a participating institution or from an approved alliance-participation arrangement.
* **Student status** means the current institutional status defined by the issuer, such as
  active, temporarily suspended or otherwise valid for a defined period.
* **Educational ID** means an institutional affiliation credential in the ERUA-iD model.
* **Alliance ID** means an ERUA membership or alliance-affiliation credential.
* **ESC VC** means a European Student Card represented as a Verifiable Credential.
* **Service entitlement** means an explicitly stated eligibility outcome, not a general
  permission to access every institutional or alliance service.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata in an encoding-independent manner.

For the SEDIT-X and ERUA pilot, the credential is defined as a **non-qualified EAA**.
Its category value is:

```text
eaa:eu:non-qualified
```

The credential SHALL be designed around affiliation, status and service eligibility.
It SHOULD use pseudonymous identifiers and SHALL avoid unnecessary replication of PID
attributes.

### 2.1 Design principles

The following design principles apply:

1. **Authoritative institutional status:** the home institution or another authorised
   academic issuer remains authoritative for the student's institutional relationship.
2. **Alliance affiliation:** ERUA affiliation SHALL be based on a recognised institutional
   or alliance source.
3. **Data minimisation:** a service SHOULD normally request only a status indicator,
   issuing institution and validity period.
4. **Separation from civil identity:** legal name, date of birth, nationality and document
   identifiers SHOULD remain in the PID unless indispensable for a service.
5. **Separation from achievement:** course completion, grades and credits SHALL use
   dedicated learning or achievement credentials.
6. **Selective disclosure:** programme, study level, campus and entitlements SHALL be
   disclosed only when needed.
7. **Cross-border usability:** institution, programme and level identifiers SHOULD use
   stable European or nationally recognised identifiers where available.
8. **Current-status verification:** status and validity SHALL be checked at presentation.
9. **Service-specific decisions:** the verifier SHALL apply its own service policy after
   verifying the credential.
10. **Non-discrimination:** absence of optional alliance or programme information SHALL
    not be treated as lack of student status where the mandatory student-status claims are valid.

### 2.2 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_id` | Unique identifier of the credential. It SHALL NOT be a national civil identity number. | string | `erua_student_01K0V7...` |
| `student_reference` | Pairwise or issuer-specific pseudonymous reference for the student. | string | `stu_8f2a91c4d3` |
| `student_status` | Current student relationship asserted by the issuer. | string enum | `active` |
| `home_institution_id` | Stable identifier of the home Higher Education Institution. | string or URI | `https://ror.org/04qmmjx98` |
| `home_institution_name` | Human-readable name of the home institution. | string | `University of the Aegean` |
| `affiliation_type` | Type of institutional relationship. | string enum | `student` |
| `status_valid_from` | Date from which the asserted student status is valid. | date | `2026-09-01` |
| `status_valid_until` | Date until which the asserted student status is valid. | date | `2027-08-31` |

Permitted values for `student_status` SHOULD include:

* `active`;
* `enrolled`;
* `exchange_student`;
* `visiting_student`;
* `doctoral_candidate`;
* `temporarily_suspended`;
* `completed_pending_expiry`; and
* `inactive`.

A credential with `student_status` equal to `inactive` SHALL NOT be accepted as proof of
current student status unless a service policy explicitly supports former-student use.

Permitted values for `affiliation_type` SHOULD include:

* `student`;
* `doctoral_candidate`;
* `exchange_student`;
* `visiting_student`; and
* another value approved by the academic-governance profile.

### 2.3 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `given_name` | Student's given name. SHOULD be omitted when a pseudonymous status proof is sufficient. | string | `Alexandra` |
| `family_name` | Student's family name. SHOULD be omitted when a pseudonymous status proof is sufficient. | string | `Papadopoulou` |
| `display_name` | Human-readable name for wallet display. | string | `Alexandra Papadopoulou` |
| `institutional_email` | Institutional email address. | string | `alexandra@example.aegean.gr` |
| `institutional_person_identifier` | Institution-controlled student identifier. Disclosure SHOULD be limited. | string | `aegean:student:20261234` |
| `european_student_identifier` | European Student Identifier where available. | string | `urn:schac:personalUniqueCode:int:esi:example.edu:12345` |
| `education_identifier` | Identifier corresponding to the ERUA Educational ID deployment. | string | `edu-id:aegean:8f2a...` |
| `alliance_identifier` | Identifier corresponding to the ERUA Alliance ID deployment. | string | `erua-id:7a91...` |
| `erua_affiliation` | Indicates current affiliation with ERUA. | boolean | `true` |
| `alliance_name` | Name of the university alliance. | string | `European Reform University Alliance` |
| `alliance_code` | Short alliance code. | string | `ERUA` |
| `programme_name` | Name of the programme of study. | string | `MSc Information and Communication Systems` |
| `programme_identifier` | Stable identifier of the programme. | string or URI | `urn:aegean:programme:ics-msc` |
| `study_level` | Study-cycle or qualification-framework level. | string | `EQF7` |
| `study_field` | Study field or classification code. | string | `061` |
| `academic_year` | Academic year for which status is asserted. | string | `2026/2027` |
| `semester` | Current semester or term, when needed. | string | `winter` |
| `campus` | Campus or study location. | string | `Samos` |
| `mobility_status` | Mobility or exchange relationship. | string enum | `erua_exchange` |
| `host_institution_id` | Identifier of a host institution during mobility. | string or URI | `https://ror.org/012tb2g32` |
| `student_card_number` | European or institutional student-card number where the deployment uses one. | string | `ESC-GR-2026-12345` |
| `service_entitlements` | Explicit service eligibility values. | array of strings | `["student_discount","library_access"]` |
| `assurance_level` | Assurance or verification level of the academic source and issuance process. | string | `institutionally_verified` |
| `portrait` | Student portrait where specifically required for supervised visual identification. | binary or URI | `data:image/jpeg;base64,...` |

The `portrait` attribute SHOULD NOT be present in the normal ERUA status profile. It MAY
be included only under a documented policy where visual identification is necessary and
where the issuer has a lawful and authoritative source.

### 2.4 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `erua_membership_basis` | Basis for ERUA affiliation. Mandatory when `erua_affiliation` is `true`. | string enum | `member_institution_student` |
| `host_institution_name` | Human-readable host institution. Present when `host_institution_id` is present. | string | `University of Konstanz` |
| `mobility_valid_from` | Start of mobility period. Mandatory when mobility status is asserted. | date | `2026-10-01` |
| `mobility_valid_until` | End of mobility period. Mandatory when mobility status is asserted. | date | `2027-02-28` |
| `programme_level` | Programme or qualification level used for tariff or service policy. Present only when required. | string | `master` |
| `discount_eligibility` | Minimal verified discount eligibility result. Present only for a profile that embeds a specific entitlement. | boolean | `true` |
| `cryptographically_bound_to` | Attestation type to which this credential is cryptographically bound. Present where formal binding to PID is required. | string | `urn:eu.europa.ec.eudi:pid:1` |

Permitted values for `erua_membership_basis` SHOULD include:

* `member_institution_student`;
* `approved_exchange_participant`;
* `joint_programme_student`;
* `alliance_activity_participant`; and
* another governance-approved value.

### 2.5 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the issuing university or authorised academic Attestation Provider. | string or URI | `https://issuer.aegean.gr` |
| `credential_type` | Encoding-independent credential type identifier. | string | `urn:aptitude.eu:seditx:erua-student-status:1` |
| `issued_at` | Date and time of credential issuance. | date-time | `2026-09-02T08:30:00Z` |
| `valid_from` | Start of credential cryptographic validity. | date-time | `2026-09-02T08:30:00Z` |
| `valid_until` | End of credential cryptographic validity. | date-time | `2027-09-01T00:00:00Z` |
| `schema_version` | Version of the credential schema. | string | `0.1` |
| `status_reference` | Reference used for credential status or revocation checking. | URI or structured value | `https://status.aegean.gr/atl/2026/09#3812` |
| `trust_anchor_reference` | Location from which issuer trust information can be obtained. | URI | `https://trust.erua-eui.eu/academic-issuers` |

All identifiers and URLs above are illustrative and SHALL be replaced by governance-approved
values.

### 2.6 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_name` | Human-readable wallet display name. | string | `ERUA Student Status` |
| `credential_description` | Human-readable explanation of the credential. | string | `Proof of current student status and ERUA affiliation` |
| `issuer_name` | Human-readable issuer name. | string | `University of the Aegean` |
| `issuer_logo_uri` | URI of the issuer logo. | URI | `https://issuer.aegean.gr/logo.png` |
| `alliance_logo_uri` | URI of the alliance logo. | URI | `https://erua-eui.eu/logo.png` |
| `privacy_notice` | Reference to privacy information. | URI | `https://issuer.aegean.gr/privacy/student-status` |
| `issuer_policy` | Reference to issuance and verification policy. | URI | `https://issuer.aegean.gr/policy/student-status` |
| `display_locale` | Preferred language for wallet display. | string | `en` |
| `source_system_reference` | Pseudonymous reference to the authoritative SIS or ESC Router record. | string | `sis-ref:81af...` |

### 2.7 Conditional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `status_list_index` | Entry index in an applicable Attestation Status List. Mandatory when list-based status is used. | integer | `3812` |
| `status_list_uri` | URI of the applicable Attestation Status List. Mandatory when list-based status is used. | URI | `https://status.aegean.gr/atl/2026/09` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI | `https://status.aegean.gr/arl/2026` |
| `esc_router_reference` | Reference to the ESC Router record or transaction. Present only in an ESC Router-based issuance profile. | string | `esc-router:txn:72f...` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 of this Rulebook does not mandate an ISO/IEC 18013-5 mdoc representation.

The SEDIT-X campus and ERUA services include both online and proximity verification.
SD-JWT VC is selected as the primary pilot encoding because it supports remote
OpenID4VP/DC API-style interactions and selective disclosure across alliance services.

A future deployment MAY define an mdoc encoding where offline or unsupervised proximity
access is required. Such a profile SHALL define:

* a unique mdoc document type;
* a unique attribute namespace;
* CDDL encodings;
* reader authentication requirements;
* offline status and trust-cache rules; and
* equivalence with the semantic model in Chapter 2.

Until that profile is approved, an issuer SHALL NOT advertise mdoc support for this
attestation solely on the basis of this Rulebook.

## 3.2 SD-JWT VC-based encoding

### 3.2.1 Verifiable Credential Type

The proposed Verifiable Credential Type is:

```text
urn:aptitude.eu:seditx:erua-student-status:1
```

This is a pilot identifier and requires confirmation through APTITUDE and ERUA governance.

### 3.2.2 Registered JWT claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `issuer` | `iss` | string | JWT issuer identifier | MUST NOT |
| `issued_at` | `iat` | integer | NumericDate | MUST NOT |
| `valid_until` | `exp` | integer | NumericDate | MUST NOT |
| `valid_from` | `nbf` | integer | NumericDate | MUST NOT |
| `credential_type` | `vct` | string | SD-JWT VC type | MUST NOT |
| `holder_binding` | `cnf` | object | Holder-binding confirmation key | MUST NOT |
| `status_reference` | `status` | object | Credential status metadata | MUST NOT |
| `given_name` | `given_name` | string | OpenID Connect claim | MUST |
| `family_name` | `family_name` | string | OpenID Connect claim | MUST |
| `institutional_email` | `email` | string | OpenID Connect claim | MUST |

### 3.2.3 Private claims specific to this attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `category` | `category` | string | EAA legal category | MUST NOT |
| `credential_id` | `credential_id` | string | Credential identifier | MUST NOT |
| `student_reference` | `student_reference` | string | Pseudonymous student reference | MUST |
| `student_status` | `student_status` | string | Current student status | MUST |
| `home_institution_id` | `home_institution_id` | string | Stable HEI identifier | MUST |
| `home_institution_name` | `home_institution_name` | string | Human-readable HEI name | MUST |
| `affiliation_type` | `affiliation_type` | string | Institutional relationship | MUST |
| `status_valid_from` | `status_valid_from` | string | ISO date | MUST |
| `status_valid_until` | `status_valid_until` | string | ISO date | MUST |
| `display_name` | `display_name` | string | Wallet/service display value | MUST |
| `institutional_person_identifier` | `institutional_person_identifier` | string | Institution-specific ID | MUST |
| `european_student_identifier` | `european_student_identifier` | string | European Student Identifier | MUST |
| `education_identifier` | `education_identifier` | string | ERUA Educational ID | MUST |
| `alliance_identifier` | `alliance_identifier` | string | ERUA Alliance ID | MUST |
| `erua_affiliation` | `erua_affiliation` | boolean | ERUA relationship | MUST |
| `alliance_name` | `alliance_name` | string | Alliance name | MUST |
| `alliance_code` | `alliance_code` | string | Alliance short code | MUST |
| `programme_name` | `programme_name` | string | Programme name | MUST |
| `programme_identifier` | `programme_identifier` | string | Programme identifier | MUST |
| `study_level` | `study_level` | string | EQF/NQF or cycle | MUST |
| `study_field` | `study_field` | string | Study-field code | MUST |
| `academic_year` | `academic_year` | string | Academic year | MUST |
| `semester` | `semester` | string | Term or semester | MUST |
| `campus` | `campus` | string | Campus/location | MUST |
| `mobility_status` | `mobility_status` | string | Mobility relationship | MUST |
| `host_institution_id` | `host_institution_id` | string | Host HEI identifier | MUST |
| `host_institution_name` | `host_institution_name` | string | Host HEI name | MUST |
| `mobility_valid_from` | `mobility_valid_from` | string | ISO date | MUST |
| `mobility_valid_until` | `mobility_valid_until` | string | ISO date | MUST |
| `student_card_number` | `student_card_number` | string | Student-card identifier | MUST |
| `service_entitlements` | `service_entitlements` | array of strings | Explicit entitlements | MUST |
| `assurance_level` | `assurance_level` | string | Issuance/source assurance | MUST |
| `portrait` | `portrait` | string | Protected image or URI | MUST |
| `erua_membership_basis` | `erua_membership_basis` | string | Basis of ERUA affiliation | MUST |
| `programme_level` | `programme_level` | string | Programme level | MUST |
| `discount_eligibility` | `discount_eligibility` | boolean | Specific discount outcome | MUST |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | PID type binding | MUST NOT |
| `schema_version` | `schema_version` | string | Schema version | MUST NOT |
| `trust_anchor_reference` | `trust_anchor_reference` | string | Trust lookup location | MUST NOT |
| `privacy_notice` | `privacy_notice` | string | Privacy information | MAY |
| `source_system_reference` | `source_system_reference` | string | Pseudonymous source reference | MUST NOT |
| `esc_router_reference` | `esc_router_reference` | string | ESC Router reference | MUST NOT |

### 3.2.4 Illustrative JWT claim set

```json
{
  "iss": "https://issuer.aegean.gr",
  "iat": 1788337800,
  "nbf": 1788337800,
  "exp": 1819756800,
  "vct": "urn:aptitude.eu:seditx:erua-student-status:1",
  "cnf": {
    "jkt": "m4F0...wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 3812,
      "uri": "https://status.aegean.gr/atl/2026/09"
    }
  },
  "category": "eaa:eu:non-qualified",
  "credential_id": "erua_student_01K0V7M2P9",
  "student_reference": "stu_8f2a91c4d3",
  "student_status": "active",
  "home_institution_id": "https://ror.org/04qmmjx98",
  "home_institution_name": "University of the Aegean",
  "affiliation_type": "student",
  "status_valid_from": "2026-09-01",
  "status_valid_until": "2027-08-31",
  "european_student_identifier": "urn:schac:personalUniqueCode:int:esi:example.edu:12345",
  "education_identifier": "edu-id:aegean:8f2a91c4d3",
  "alliance_identifier": "erua-id:7a91e5f8",
  "erua_affiliation": true,
  "alliance_name": "European Reform University Alliance",
  "alliance_code": "ERUA",
  "erua_membership_basis": "member_institution_student",
  "programme_name": "MSc Information and Communication Systems",
  "programme_identifier": "urn:aegean:programme:ics-msc",
  "study_level": "EQF7",
  "academic_year": "2026/2027",
  "campus": "Samos",
  "service_entitlements": [
    "student_discount",
    "library_access",
    "erua_event_registration"
  ],
  "assurance_level": "institutionally_verified",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.erua-eui.eu/academic-issuers",
  "privacy_notice": "https://issuer.aegean.gr/privacy/student-status"
}
```

An actual compact SD-JWT serialisation SHALL be generated using the final issuer keys,
salts, status infrastructure and selective-disclosure policy. This Rulebook does not
provide a fabricated base64 token.

### 3.2.5 Human-readable wallet representation

A Wallet Unit SHOULD display at least:

```text
ERUA Student Status
Status: Active student
Institution: University of the Aegean
ERUA affiliation: Active
Academic year: 2026/2027
Valid until: 31 August 2027
Issuer: University of the Aegean
```

Programme, study level, student identifier and service entitlements SHOULD be displayed
only where present and relevant.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 of this Rulebook does not define a W3C VCDM representation.

ERUA's earlier pilots and EBSI-aligned implementations may use W3C VC structures, but
this Rulebook selects SD-JWT VC as the target EUDI Wallet pilot encoding. A future
version MAY add a formally mapped W3C VCDM profile if required.

## 4 Attestation usage

### 4.1 Issuance prerequisites

The issuer SHALL be a recognised Higher Education Institution or an authorised academic
Attestation Provider acting on its behalf.

Before issuance, the issuer SHALL:

1. authenticate the student through the institutional identity infrastructure;
2. retrieve or verify current status from an authoritative Student Information System,
   ESC Router or equivalent academic source;
3. confirm the student's institutional affiliation and validity period;
4. where ERUA affiliation is asserted, verify the applicable alliance-membership basis;
5. determine the minimum attributes required for the selected credential profile;
6. bind the credential to the Wallet Unit;
7. present the credential purpose, issuer, data and validity to the User; and
8. obtain User consent to receive and store the credential.

An ESC Router-based issuance profile MAY follow:

```text
Institutional IdP → Student Information System → ESC Router →
Issuer Service → EUDI Wallet
```

A decentralised profile MAY issue directly from institutionally verified SIS data without
using the ESC Router, subject to the approved governance model.

### 4.2 Device and holder binding

The credential **SHOULD be device-bound** to a key controlled by the Wallet Unit.

The issuer SHALL ensure that the credential is delivered to the Wallet Unit used by the
authenticated student and that issuance is protected against misdirection and replay.

The credential MAY be cryptographically bound to PID using:

```text
cryptographically_bound_to = "urn:eu.europa.ec.eudi:pid:1"
```

PID binding SHOULD be used where a service requires high-assurance civil identity in
addition to academic status. It SHOULD NOT be required for pseudonymous services where
student status alone is sufficient.

### 4.3 Presentation contexts

The credential MAY be presented remotely or in proximity.

Remote presentation MAY use OpenID4VP or the Digital Credentials API for:

* online registration;
* authentication to ERUA services;
* course or event enrolment;
* transport discount verification;
* remote library or academic-service access; and
* other web-based services.

Proximity presentation MAY be used for:

* Tap2Enter attendance;
* event check-in;
* campus and facility access;
* cafeteria or free-meal verification;
* library desk verification;
* ferry or mobility discount verification; and
* another face-to-face service.

The Wallet Unit SHALL display the requested attributes and purpose and SHALL obtain User
authentication and approval before disclosure.

### 4.4 Typical disclosure profiles

#### 4.4.1 Basic student-status proof

A verifier SHOULD request only:

* `student_status`;
* `home_institution_id` or `home_institution_name`;
* `status_valid_until`; and
* credential validity and status metadata.

#### 4.4.2 ERUA service access

A verifier MAY additionally request:

* `erua_affiliation`;
* `alliance_code`;
* `alliance_identifier` or a pairwise alternative; and
* a required `service_entitlements` value.

#### 4.4.3 Transport discount

A ferry or transport verifier SHOULD request only:

* `student_status` or `discount_eligibility`;
* `home_institution_id`;
* `status_valid_until`; and
* `programme_level` only where required by the tariff rules.

The SEDIT-X ferry profile identifies student status, issuing institution, validity period
and programme/level only where needed as the appropriate disclosure subset.

#### 4.4.4 Attendance or event registration

A service MAY request:

* `student_reference` or a service-specific pseudonym;
* `erua_affiliation` where the event is alliance-restricted;
* `home_institution_id`; and
* the minimum display name only where the attendance record must identify the person.

#### 4.4.5 Meal or cafeteria eligibility

A service SHOULD request a verified eligibility result and a pseudonymous subject or
service-specific identifier. It SHOULD avoid collecting programme, grades, full date of
birth or civil identity document data.

### 4.5 Relying Party obligations

A Relying Party SHALL:

1. verify the issuer signature and credential integrity;
2. verify that the issuer is trusted and authorised to assert student status;
3. verify credential validity and status;
4. verify key binding, nonce, audience and presentation freshness as applicable;
5. verify that `student_status` is acceptable for the requested service;
6. check the status-validity interval;
7. apply service-specific eligibility rules;
8. request only attributes necessary for the service;
9. avoid retaining the complete credential or unrelated attributes;
10. return a clear decision such as granted, denied or manual review; and
11. provide an alternative procedure where automated verification cannot complete.

A typical result SHOULD contain only:

```json
{
  "student_status_valid": true,
  "erua_affiliation_valid": true,
  "requested_entitlement_valid": true,
  "decision": "granted",
  "correlation_id": "erua-vfy-01K0..."
}
```

### 4.6 Identity verification and PID

A Relying Party SHALL NOT request PID by default merely because it verifies student status.

PID MAY be requested when:

* the service has a legal requirement to identify the individual;
* the service grants a high-value, personal or non-transferable entitlement;
* an examination or supervised academic process requires identity confirmation;
* a mismatch or fraud indicator requires staff-assisted verification; or
* the applicable service policy documents another proportionate need.

Where PID is requested, the verifier SHALL request only the minimum identity attributes
needed for the stated purpose.

### 4.7 Service entitlements

The `service_entitlements` attribute MAY simplify decisions for well-defined services.
However:

* it SHALL contain only explicitly issued entitlements;
* it SHALL NOT be interpreted as a general access-control list;
* the verifier SHALL still check validity and status;
* sensitive information SHALL not be inferred from entitlement labels; and
* frequently changing service state SHOULD remain in the service backend rather than
  require constant credential re-issuance.

### 4.8 Operational logging

A verifier MAY record a minimal event containing:

* service or event identifier;
* timestamp;
* pseudonymous transaction or student reference;
* issuer or institution identifier;
* requested eligibility outcome; and
* decision.

The log SHOULD NOT contain:

* complete credential copies;
* unnecessary PID attributes;
* programme or study-level data unrelated to the decision;
* portrait images; or
* other academic records.

### 4.9 Transactional data

This credential is not a payment attestation and SHALL NOT carry payment transaction data.

Where the credential is used to obtain a discount or free service, the payment, tariff or
redemption transaction SHALL be processed separately. A verifier MAY record that a
student-status eligibility check succeeded, but SHALL NOT use the credential as payment
authorisation evidence.

### 4.10 Failure and fallback

The automated flow SHALL return denied or manual review when:

* signature, trust, validity or status verification fails;
* student status is inactive or outside its validity period;
* ERUA affiliation is required but cannot be verified;
* the requested entitlement is absent;
* holder binding or presentation freshness fails;
* the authoritative source reports that the status has changed; or
* the service policy requires additional staff verification.

## 5 Trust anchors

The credential is a non-qualified EAA issued by a participating Higher Education
Institution or an authorised academic Attestation Provider.

For the pilot, trust SHOULD be established through the APTITUDE trust framework and/or
an ERUA academic issuer registry.

The production trust model SHALL define:

1. which institutions are authorised to issue student status;
2. whether ERUA itself may issue alliance affiliation or only provide technical infrastructure;
3. whether a shared ERUA Issuer acts as technical provider, issuer of record or both;
4. how delegated issuance is represented;
5. the trusted-list service type for academic issuers;
6. certificate and signing-key profiles;
7. issuer scope by institution, credential type and alliance role;
8. key rollover and compromise handling; and
9. verifier behaviour when trust information is unavailable.

A verifier SHALL establish both:

* cryptographic trust in the issuer; and
* semantic authorisation of that issuer to assert the relevant institution and student status.

Where ERUA affiliation is asserted by a university, the trust framework SHALL establish
that the university is an ERUA member and is authorised to issue that affiliation.

## 6 Revocation

### 6.1 Validity model

The credential SHALL have a bounded validity period aligned with the academic source.

The issuer SHOULD set validity based on:

* enrolment or registration period;
* academic year or semester;
* mobility period;
* expected SIS revalidation cycle; and
* maximum risk acceptable for status changes.

A one-year validity period MAY be used where supported by regular status checking and
prompt revocation. Shorter periods SHOULD be used for exchange or visiting-student status
that ends on a defined date.

### 6.2 Revocation and status updates

The credential SHALL be status-checkable.

The issuer SHALL revoke, suspend, supersede or otherwise invalidate the credential when:

* the student's status ends;
* enrolment is cancelled;
* a mobility or visiting period ends early;
* the credential was issued using erroneous source data;
* a replacement credential is issued under a one-active-credential policy;
* the Wallet Unit or credential is reported compromised; or
* fraud is detected.

The issuer SHOULD support a **one active credential per profile and student** policy,
where operationally feasible, so that re-issuance supersedes the previous credential.

### 6.3 Status-list mechanism

The target implementation SHOULD use the status-list mechanism selected by APTITUDE WP2
and aligned with the applicable EUDI Wallet Technical Specification.

The final production endpoint has not yet been defined.

Illustrative value:

```text
https://status.aegean.gr/
```

This value SHALL NOT be treated as an operational endpoint.

## 7 Compliance

This Rulebook is designed to align with:

* Regulation (EU) 2024/1183 establishing the European Digital Identity Framework;
* the EUDI Wallet Architecture and Reference Framework;
* ARF Annex 2 Topic 12 requirements;
* SD-JWT VC and the APTITUDE-selected HAIP profile;
* OpenID4VCI and OpenID4VP;
* the SEDIT-X Student Status Credential use cases;
* the ERUA-iD Educational ID and Alliance ID concepts;
* the European Student Card VC pilot context;
* GDPR principles of purpose limitation, data minimisation, storage limitation,
  integrity and confidentiality; and
* higher-education requirements for authoritative affiliation and status verification.

The Rulebook enforces these properties:

1. the attestation is a purpose-bound non-qualified EAA;
2. the home institution remains authoritative for student status;
3. ERUA affiliation is represented separately and disclosed only when needed;
4. civil identity and academic achievement data are not unnecessarily duplicated;
5. SD-JWT selective disclosure is used for service-specific proofs;
6. the credential is bound to the Wallet Unit;
7. presentation requires User authentication and approval;
8. status and revocation checks are required;
9. verifiers request and retain only minimum data;
10. PID is not required by default; and
11. staff-assisted fallback remains available.

The following matters remain open and SHALL be resolved before final publication:

* whether the final profile is unified or split into Educational ID and Alliance ID;
* relationship to the final European Student Card VC data model;
* final `vct` identifier;
* approved HEI, programme and study-level code systems;
* final ERUA governance and issuer-of-record model;
* final PID-binding policy;
* final trust-list service type and endpoint;
* final status-list or revocation-list mechanism and endpoint;
* mdoc support for offline campus proximity services;
* service-entitlement vocabulary; and
* cross-institutional data-retention and audit rules.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X] | APTITUDE WP4, Seamless Digital Traveller Experience use case materials |
| [ERUA-iD] | ERUA digital identity and verifiable credential infrastructure materials developed by the University of the Aegean |
| [ESC VC Pilot] | European Student Card Verifiable Credential pilot architecture and implementation materials |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [OIDC] | OpenID Connect Core 1.0 |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 3339] | Date and Time on the Internet: Timestamps |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Signatures and Trust Infrastructures; Electronic Attestation of Attributes; Part 1: Building blocks and general requirements |
