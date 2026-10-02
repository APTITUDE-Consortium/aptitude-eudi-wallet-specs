# Attestation Rulebook for attestations of type European Disability Card

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                                        |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X use case, APTITUDE UC7 material and the APTITUDE Attestation Rulebook template. |
| 0.2     | 26-08-2026 | Aligned with an earlier APTITUDE issuer schema (`european_disability_card`, `vct` `urn:eu.europa.ec.eudi:edc:1`) and optional hospitality check-in use. |
| 0.3     | 02-10-2026 | Defines the APTITUDE European Disability Card SD-JWT profile based on the Italian IT-Wallet / Documenti su IO model (IT Wallet Specification v1.3.3): `vct` `urn:eudi:EuropeanDisabilityCard:it:1`, claim set with `constant_attendance_allowance` as the primary accessibility claim. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the APTITUDE / SEDIT-X **European Disability Card**
> profile. It is based on the Italian IT-Wallet (“Documenti su IO”) European
> Disability Card model (IT Wallet Specification **v1.3.3**). The attribute set,
> identifiers and SD-JWT encoding rules in the chapters below are the APTITUDE
> profile.
>
> The Verifiable Credential Type (`vct`) is:
>
> ```text
> urn:eudi:EuropeanDisabilityCard:it:1
> ```
>
> The OpenID4VCI credential configuration identifier is:
>
> ```text
> dc_sd_jwt_EuropeanDisabilityCard
> ```
>
> The APTITUDE / SEDIT-X pilot uses **mock data** that conforms to this profile.
> Domain-specific service outcomes (for example an easier-access hotel room) are
> produced by the Relying Party after verification; they are not encoded as
> additional claims in this credential.



## 1 Introduction



### 1.1 Document scope and purpose

This Rulebook defines the **European Disability Card**, an Electronic Attestation of Attributes stored in a User's EUDI Wallet
and used to prove recognised disability-card status and, where applicable,
constant attendance allowance (accompanying assistance / additional support).

This APTITUDE profile is based on the Italian national wallet implementation
(IT-Wallet / Documenti su IO), as documented in the IT-Wallet Technical
Specifications (v1.3.3) and the European Disability Card examples in the
PID-(Q)EAA data model. The data model defined in this Rulebook is the APTITUDE
profile used for issuance and verification in the pilot.

The Verifiable Credential Type (`vct`) is:

```text
urn:eudi:EuropeanDisabilityCard:it:1
```

The OpenID4VCI credential configuration identifier is:

```text
dc_sd_jwt_EuropeanDisabilityCard
```

with format `dc+sd-jwt` and scope `EuropeanDisabilityCard`.

The attestation is intended to enable inclusive and equal access to services without
requiring the User to repeatedly disclose medical records, diagnostic details or a
complete disability profile.

Within SEDIT-X, the attestation may support:

- airport assistance and accessible passenger processing;
- ferry or other transport discounts and companion or assistant entitlements;
- priority or assisted boarding;
- accessible hotel services, including optional presentation at check-in to
  request assistance with the room or an easier-access room;
- mobility-related assistance;
- university and campus accessibility services; and
- other service accommodations accepted by an authorised Relying Party.

The attestation SHALL express verified **card status or entitlement**, not medical
diagnosis. It SHALL disclose only the minimum information needed for the current
service decision.

In the hospitality check-in flow, presentation is **optional**. The hotel
verifies the Accommodation Voucher and PID regardless. Where the guest offers
this card, the hotel MAY use `constant_attendance_allowance` (and, only where
needed, identity claims) to trigger its assistance process (for example room
type, access arrangements or staff support). Those operational outcomes SHALL
NOT be written back into this credential.

The primary objectives are to:

1. enable trusted verification of a recognised European Disability Card;
2. enable selective disclosure of `constant_attendance_allowance` where relevant;
3. reduce repeated presentation of paper disability cards or supporting documents;
4. avoid disclosure of health information not needed by the service provider;
5. support cross-border use where the issuer and verifier participate in a recognised
  trust framework; and
6. allow operational service systems to receive a clear eligibility outcome.



### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 defines attributes and metadata in an encoding-independent manner.
- Chapter 3 defines the SD-JWT VC encoding.
- Chapter 4 specifies issuance, presentation, consent and verifier obligations.
- Chapter 5 defines trust-anchor requirements.
- Chapter 6 defines validity and revocation.
- Chapter 7 describes compliance with the EUDI Wallet framework and privacy principles.
- Chapter 8 lists references.



### 1.3 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119].

In addition, *must* in lower case indicates an external constraint not established by
this Rulebook. The word *can* indicates a capability. Other words such as *will*, *is*
and *are* are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the EUDI Wallet
Architecture and Reference Framework.

For this Rulebook:

- **European Disability Card** means the attestation with `vct`
  `urn:eudi:EuropeanDisabilityCard:it:1` and OpenID4VCI configuration id
  `dc_sd_jwt_EuropeanDisabilityCard`, as defined for the Italian IT-Wallet /
  Documenti su IO profile.
- **Constant attendance allowance** means the verified entitlement to
  accompanying assistance or additional support under the applicable scheme
  (`constant_attendance_allowance`).
- **Recognised disability-card status** means that the holder presents a valid
  European Disability Card under this profile. Possession and successful
  verification of the credential establish recognition; a separate boolean
  status claim is not part of this profile.
- **Service provider** means an authorised transport, hospitality, mobility,
  education or other organisation acting as Relying Party.
- **Accommodation Voucher** means the hotel-booking attestation of type
  `booking_reference_credential`.
- **PID** means Person Identification Data of type `urn:eu.europa.ec.eudi:pid:1`.
- **IT-Wallet / Documenti su IO** means the official Italian national wallet
  programme whose European Disability Card technical model is the basis of this
  Rulebook. APTITUDE uses that model with mock data for the pilot.



## 2 Attestation attributes and metadata



### Chapter overview and requirements

This chapter defines the attributes and metadata of the European Disability Card
in an encoding-independent manner.

For the SEDIT-X pilot, the attestation is defined as a **non-qualified EAA** unless it is
issued under a legal and trust framework that qualifies it as a QEAA or PuB-EAA.

The pilot category value is therefore:

```text
eaa:eu:non-qualified
```

The attestation SHALL be based on data from a competent public authority, public issuer,
recognised disability-card scheme, or another trusted organisation authorised to attest
the relevant status and entitlements. The issuing authority is represented by
`issuing_authority` and `issuing_country`.

The credential attribute set is defined in the sections below. The APTITUDE pilot
issuer SHALL populate it with mock values.

### 2.1 Design principles

The following design principles apply:

1. **Entitlement, not diagnosis:** the credential SHALL represent card recognition
  and constant attendance allowance rather than diagnostic or clinical data.
2. **Selective disclosure:** each claim SHOULD be independently disclosable.
3. **Minimum identity disclosure:** name, birth date, document number and portrait
  SHALL be requested only where needed for fraud prevention, visual inspection
  or legal rules. For SEDIT-X Episode 4 hospitality, the primary requested claim
  SHOULD be `constant_attendance_allowance`.
4. **Portrait is a card image, not a biometric template:** the credential MAY
  contain `portrait` as an image consistent with the card scheme. It
  SHALL NOT contain a biometric template, biometric reference, fingerprint,
  iris data or any other biometric sample. A verifier SHALL NOT extract a
  biometric template from `portrait` unless a specific legal basis exists.
5. **No inferred diagnosis:** a verifier SHALL NOT infer a diagnosis from card
  possession or from `constant_attendance_allowance`.
6. **Context-specific requests:** a ferry operator, airport, hotel or university
  SHALL request only claims needed for the specific service.
7. **User control:** presentation SHALL require informed User approval.
8. **No unnecessary retention:** verifiers SHOULD retain only the decision and
  minimum operational reference.
9. **Cross-domain reuse:** one credential MAY support multiple service domains
  where the status and entitlement are accepted by each relevant service policy.
10. **Optional hospitality use:** hotel check-in SHALL succeed without this
  credential. Presentation at check-in is an opt-in request for assistance.
11. **Fallback:** a User who cannot or does not present the credential SHALL
  retain access to an appropriate manual or assisted process.



### 2.2 Mandatory attributes


| **Data Identifier**               | **Definition**                                                                                          | **Data type** | **Example value**                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------------- |
| `family_name`                     | Holder's family name as recorded on the card.                                                           | string        | `Rossi`                                |
| `given_name`                      | Holder's given name as recorded on the card.                                                            | string        | `Mario`                                |
| `birth_date`                      | Holder's date of birth as recorded on the card.                                                         | date          | `1980-01-10`                           |
| `document_number`                 | Document number of the European Disability Card.                                                        | string        | `XXXXXXXXXX`                           |
| `expiry_date`                     | Administrative expiration date of the credential / card.                                                | date          | `2031-01-14`                           |
| `issuing_authority`               | Name of the administrative authority that issued the credential.                                        | string        | `Istituto Poligrafico e Zecca dello Stato` |
| `issuing_country`                 | ISO 3166-1 alpha-2 country code of the issuing jurisdiction.                        | string        | `IT`                                   |
| `portrait`                        | Facial image of the holder, for visual inspection where required.                                       | string / bytes | *(image)*                             |
| `link_qr_code`                    | URI associated with the card QR code.                                                                   | URI           | `https://example.it/edc/qr/...`        |
| `constant_attendance_allowance`   | Indicates entitlement to accompanying assistance / additional support under the scheme.                 | boolean       | `true`                                 |


`issuing_country` SHALL use ISO 3166-1 alpha-2 codes. 

`portrait` is a card photograph for visual comparison. It SHALL NOT be treated as
authorisation to perform automated biometric matching unless a specific legal
basis exists. Encoding of the image (for example base64 in SD-JWT) is defined in
Chapter 3.

Successful verification of a valid European Disability Card under this profile
is the primary status outcome. This attribute set does **not** include a
separate `disability_status_recognised` boolean.

`constant_attendance_allowance` is the primary accessibility-related entitlement
claim for companion or assistant-related service decisions in SEDIT-X.

### 2.3 Optional attributes

This profile does not define additional optional application claims beyond
the set in section 2.2. Registered JWT claims such as `nbf`, `vct#integrity` and
the optional `verification` object are treated as encoding / metadata (see
sections 2.5–2.7 and Chapter 3).

PID remains a separate credential. Where stronger identity matching is required,
the Relying Party SHALL request PID (`urn:eu.europa.ec.eudi:pid:1`) rather than
extending this card.

### 2.4 Conditional attributes


| **Data Identifier**          | **Definition**                                                                 | **Data type** | **Example value**             |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------- | ----------------------------- |
| `cryptographically_bound_to` | Attestation type to which this credential is cryptographically bound. Present where formal binding to PID is required beyond `cnf`. | string        | `urn:eu.europa.ec.eudi:pid:1` |


Where `cryptographically_bound_to` is present, its value SHOULD identify the PID type
used to bind the holder to the attestation:

```text
urn:eu.europa.ec.eudi:pid:1
```

Holder key binding is primarily expressed through
the registered `cnf` claim (see section 3.2).



### 2.5 Mandatory metadata


| **Data Identifier**      | **Definition**                                                           | **Data type**           | **Example value**                                      |
| ------------------------ | ------------------------------------------------------------------------ | ----------------------- | ------------------------------------------------------ |
| `category`               | Legal category of the attestation.                                       | string                  | `eaa:eu:non-qualified`                                 |
| `issuer`                 | Identifier of the Credential Issuer (`iss`).                             | URI                     | `https://issuer.example.org`                           |
| `credential_type`        | Encoding-independent credential type identifier. SHALL equal the `vct`.  | string                  | `urn:eudi:EuropeanDisabilityCard:it:1`                 |
| `issued_at`              | Time of credential issuance (`iat`).                                     | date-time / NumericDate | `2026-01-15T09:30:00Z`                                 |
| `status_reference`       | Reference used for status or revocation checking (`status.status_list`). | URI or structured value | `https://status.example/edc/atl/2026-01/15#1234`       |
| `trust_anchor_reference` | Location from which applicable issuer trust information can be obtained. | URI                     | `https://trust.aptitude.example/accessibility-issuers` |




### 2.6 Optional metadata


| **Data Identifier**      | **Definition**                                | **Data type** | **Example value**                                   |
| ------------------------ | --------------------------------------------- | ------------- | --------------------------------------------------- |
| `credential_name`        | Human-readable wallet display name.           | string        | `European Disability Card` / `Carta della disabilità europea` |
| `credential_description` | Human-readable explanation of the credential. | string        | `Recognised disability card and constant attendance allowance` |
| `issuer_name`            | Human-readable issuer name.                   | string        | `Istituto Poligrafico e Zecca dello Stato`          |
| `issuer_logo_uri`        | URI of the issuer logo.                       | URI           | `https://issuer.example/logo.png`                   |
| `privacy_notice`         | URI of the applicable privacy notice.         | URI           | `https://issuer.example/privacy`                    |
| `issuer_policy`          | URI of the issuance and verification policy.  | URI           | `https://issuer.example/policy`                     |
| `terms_of_use`           | URI of terms governing credential use.        | URI           | `https://issuer.example/terms`                      |
| `display_locale`         | Preferred language for wallet display.        | string        | `it` / `en`                                         |



### 2.7 Conditional metadata


| **Data Identifier**   | **Definition**                                                                                         | **Data type** | **Example value**                         |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ------------- | ----------------------------------------- |
| `status_list_index`   | Entry index in an applicable Attestation Status List (`status.status_list.idx`). Mandatory when a list-based mechanism is used. | integer       | `1234`                                    |
| `status_list_uri`     | URI of the applicable Attestation Status List (`status.status_list.uri`). Mandatory when list-based status is used. | URI           | `https://status.example/edc/atl/2026-01/15` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI           | `https://status.example/edc/arl/2026-01`  |
| `verification`        | Optional verification object (`trust_framework`, `assurance_level`) where issued.                      | object        | see section 3.2                         |


# 3 Attestation encoding

This attestation SHALL be encoded as an SD-JWT VC (`dc+sd-jwt`). No other
encoding is defined by this Rulebook.



## 3.1 Verifiable Credential Type

The Verifiable Credential Type SHALL be:

```text
urn:eudi:EuropeanDisabilityCard:it:1
```

The OpenID4VCI credential configuration for this profile is:

```json
{
  "credential_configuration_id": "dc_sd_jwt_EuropeanDisabilityCard",
  "format": "dc+sd-jwt",
  "scope": "EuropeanDisabilityCard",
  "vct": "urn:eudi:EuropeanDisabilityCard:it:1"
}
```

The credential SHALL be issued as `dc+sd-jwt` and SHALL comply with the SD-JWT VC
and HAIP profiles selected by APTITUDE WP2.

## 3.2 Registered JWT claims


| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes**                          | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | -------------------------------------------- | --------------- |
| `issuer`            | `iss`                    | string (URI)        | Credential Issuer unique identifier          | MUST NOT        |
| `subject`           | `sub`                    | string (UUID)       | Subject identifier of the SD-JWT             | MUST NOT        |
| `issued_at`         | `iat`                    | number              | NumericDate (RFC 7519)                       | MUST NOT        |
| `expires_at`        | `exp`                    | number              | NumericDate. Distinct from card `expiry_date`. | MUST NOT        |
| `valid_from`        | `nbf`                    | number              | NumericDate where used                       | MUST NOT        |
| `credential_type`   | `vct`                    | string              | SHALL be `urn:eudi:EuropeanDisabilityCard:it:1` | MUST NOT        |
| `vct_integrity`     | `vct#integrity`          | string              | Integrity metadata for the `vct` resource, where used | MUST NOT        |
| `holder_binding`    | `cnf`                    | object              | Holder-binding JWK (`cnf.jwk`)               | MUST NOT        |
| `status_reference`  | `status`                 | object              | `status.status_list` with `idx` and `uri`    | MUST NOT        |
| `sd_digests`        | `_sd`                    | array of string     | Digests of disclosures                       | MUST NOT        |
| `sd_alg`            | `_sd_alg`                | string              | Hash algorithm; this profile: `sha-256`      | MUST NOT        |
| `verification`      | `verification`           | object              | Optional: `trust_framework`, `assurance_level` | MUST NOT        |




## 3.3 Private claims specific to this attestation


| **Data Identifier**             | **Attribute identifier**        | **Encoding format** | **Notes**                                      | **Disclosable** |
| ------------------------------- | ------------------------------- | ------------------- | ---------------------------------------------- | --------------- |
| `issuing_authority`             | `issuing_authority`             | string              | Administrative issuer name                     | MUST            |
| `issuing_country`               | `issuing_country`               | string              | ISO 3166-1 alpha-2;          | MUST            |
| `expiry_date`                   | `expiry_date`                   | string (date)       | Administrative card / credential expiry        | MUST            |
| `link_qr_code`                  | `link_qr_code`                  | string (URI)        | QR-code link                                   | MUST            |
| `given_name`                    | `given_name`                    | string              | First name                                     | MUST            |
| `family_name`                   | `family_name`                   | string              | Family name                                    | MUST            |
| `birth_date`                    | `birth_date`                    | string (date)       | Date of birth                                  | MUST            |
| `portrait`                      | `portrait`                      | string              | Card photograph (e.g. base64)                  | MUST            |
| `constant_attendance_allowance` | `constant_attendance_allowance` | boolean             | Accompanying assistance / additional support   | MUST            |
| `document_number`               | `document_number`               | string              | Document number                                | MUST            |


A verifier SHALL be able to request `constant_attendance_allowance` without also
receiving `portrait`, `document_number` or name claims.

For SEDIT-X Episode 4, the requested disclosure SHOULD primarily be
`constant_attendance_allowance`. Identity attributes such as `given_name` /
`family_name` SHOULD be requested only if the hotel (or other) journey genuinely
needs them.

## 3.4 Illustrative JWT claim set

```json
{
  "iss": "https://issuer.example.org",
  "sub": "550e8400-e29b-41d4-a716-446655440000",
  "iat": 1768464000,
  "nbf": 1768464000,
  "exp": 1926288000,
  "vct": "urn:eudi:EuropeanDisabilityCard:it:1",
  "cnf": {
    "jwk": {
      "kty": "EC",
      "crv": "P-256",
      "x": "...",
      "y": "..."
    }
  },
  "status": {
    "status_list": {
      "idx": 1234,
      "uri": "https://status.example/edc/atl/2026-01/15"
    }
  },
  "_sd_alg": "sha-256",
  "issuing_authority": "Istituto Poligrafico e Zecca dello Stato",
  "issuing_country": "IT",
  "expiry_date": "2031-01-14",
  "link_qr_code": "https://example.it/edc/qr/XXXXXXXXXX",
  "given_name": "Mario",
  "family_name": "Rossi",
  "birth_date": "1980-01-10",
  "portrait": "/9j/4AAQSkZJRgABAQ...",
  "constant_attendance_allowance": true,
  "document_number": "XXXXXXXXXX"
}
```

The example includes more attributes than a normal presentation should disclose. An
actual service request SHALL select only the relevant claims. APTITUDE pilot
issuance MAY use mock values that conform to this structure.

## 3.5 Human-readable wallet representation

The Wallet Unit SHOULD display:

```text
European Disability Card / Carta della disabilità europea
Holder: Mario Rossi
Document number: XXXXXXXXXX
Issuing country: IT
Issuing authority: Istituto Poligrafico e Zecca dello Stato
Constant attendance allowance: Yes
Valid until: 14 January 2031
```

The Wallet Unit SHOULD inform the User that:

- only selected claims will be disclosed;
- diagnosis and clinical information are not part of the credential;
- `portrait` is requested only where visual inspection is needed;
- the verifier will use the disclosed claims for the stated service purpose;
- the User can refuse the presentation; and
- a manual or staff-assisted process should remain available.



## 4 Attestation usage



### 4.1 Issuance prerequisites

Before issuance, the Attestation Provider SHALL:

1. verify that the applicant is entitled to a European Disability Card under the
  applicable scheme (for APTITUDE: mock eligibility aligned with this profile);
2. determine whether `constant_attendance_allowance` applies;
3. verify identity to the level required by the scheme;
4. confirm the card validity period (`expiry_date`);
5. explain the credential purpose and claims;
6. provide the applicable privacy information; and
7. obtain User consent to receive and store the credential.

The issuer SHALL NOT include:

- medical diagnosis;
- clinical history;
- treatment information;
- medication;
- health-professional notes;
- unsupported free-text descriptions of disability;
- biometric templates or biometric references; or
- other health information not needed to express card recognition and constant
  attendance allowance.

`portrait` MAY be included as the card photograph.

### 4.2 Device and holder binding

The attestation **SHOULD be device-bound** to a key controlled by the Wallet Unit.
In the SD-JWT encoding this is expressed through `cnf.jwk`.

Where the scheme requires strong anti-fraud protection, the credential SHOULD also be
bound to the holder through:

- PID-based issuance;
- holder-binding key material; or
- another approved scheme mechanism.

A Relying Party SHOULD request PID only where necessary to prevent misuse, satisfy
legal requirements or resolve ambiguity. It SHOULD NOT routinely request PID when
card verification or `constant_attendance_allowance` alone is sufficient.

Where both this card and PID are presented, `family_name`, `given_name` and
`birth_date` SHOULD be compared with PID `family_name`, `given_name` and
`birthdate`.

### 4.3 Presentation contexts

The attestation may be presented remotely or in proximity.

Relevant SEDIT-X contexts include:

#### Airport

A verifier MAY request:

- `constant_attendance_allowance`, where companion or assistant processing is
  offered; and
- name, `document_number` or `portrait` only where staff visual inspection or
  anti-fraud checks require them.

Successful verification of the credential itself establishes recognised
disability-card status for the service decision.

#### Ferry transport

A verifier or booking portal MAY request:

- `constant_attendance_allowance`, where a companion or assistant fare or boarding
  process is offered; and
- identity claims only where required to bind the entitlement to the ticket.

#### Hospitality check-in

Presentation at hotel check-in is **optional** and occurs after or together with
the Accommodation Voucher (`booking_reference_credential`) and PID
(`urn:eu.europa.ec.eudi:pid:1`).

A hotel SHOULD primarily request:

- `constant_attendance_allowance`, where an accompanying person or in-room
  assistance is requested.

A hotel MAY additionally request:

- `given_name` / `family_name` only where needed to bind the request to the
  checked-in guest.

The hotel MAY use a positive verification result to:

- assign or offer an easier-access room;
- arrange assistance with the room; or
- record an accessibility-service request in the PMS.

Those operational outcomes belong to the hotel process. They SHALL NOT be added
as claims on this card or on the Hotel Pass.

The hotel SHALL NOT request `portrait` unless staff visual confirmation is part
of the assistance process.

Absence of this credential SHALL NOT deny check-in and SHALL NOT be treated as
proof that the guest has no accessibility need.

#### University or campus

A university MAY request `constant_attendance_allowance` and identity claims only
where required by institution policy.

### 4.4 Relying Party obligations

The Relying Party or EUDIW Intermediary Service SHALL:

1. verify signature and cryptographic integrity;
2. verify issuer trust and authorisation;
3. verify validity and status, including JWT `exp` / `nbf` and card
  `expiry_date`;
4. verify holder binding (`cnf`) where required;
5. treat successful verification of a valid European Disability Card as
  recognised card status for the service decision;
6. verify `constant_attendance_allowance` only where an assistant-related service
  is requested;
7. avoid requesting diagnosis or unrelated attributes;
8. avoid inferring disability type from the disclosed claims;
9. provide the service outcome or route the request to staff;
10. retain only the minimum operational result; and
11. provide a non-digital or staff-assisted alternative where appropriate.

A typical hospitality result SHOULD be limited to:

```json
{
  "credential_valid": true,
  "constant_attendance_allowance": true,
  "decision": "assistance_offered",
  "correlation_id": "acc_01JZ..."
}
```


### 4.5 Identity attributes

Name, birth date, document number and portrait MAY be present in the issued
credential. A verifier SHALL request them only where needed.

Examples:

- a ticket portal generally SHOULD request `constant_attendance_allowance`, not
  name or portrait;
- a staff member verifying identity MAY request name and, where visual
  inspection is required, `portrait`;
- a hotel check-in verifier SHOULD match card name to PID and the Accommodation
  Voucher guest name where the assistance request must be bound to the stay;
- a remote service SHOULD avoid requesting identity attributes unless a justified
  anti-fraud process requires them.

`portrait` SHALL NOT be used as a general-purpose biometric login.

### 4.6 Special-category data

Accessibility and disability information may constitute sensitive or special-category
personal data under applicable law. `portrait` may additionally constitute biometric
data when used for identification.

The Relying Party SHALL:

- establish a valid legal basis;
- apply purpose limitation;
- request the minimum necessary claims;
- protect the presentation and result;
- restrict internal access;
- define short retention periods; and
- avoid using the data for profiling, advertising, employment decisions or unrelated risk scoring.


### 4.7 Transactional data

This attestation is not a payment credential.

A transport or service discount MAY be applied based on verified card recognition or
constant attendance allowance. Payment authorisation and payment confirmation SHALL remain
separate.

The Relying Party MAY retain:

- the applied fare or assistance basis;
- entitlement verification outcome;
- transaction reference; and
- minimum evidence needed for audit.

It SHOULD NOT retain the complete attestation or the portrait image.

### 4.8 Failure and fallback

The verifier SHALL return `not_verified` or `manual_review` when:

- signature, trust, validity or status verification fails;
- `constant_attendance_allowance` is required for the requested service and is
  not `true`;
- holder binding cannot be established where required;
- the credential cannot be read; or
- the User declines presentation.

Failure to complete wallet verification SHALL NOT automatically establish that the User
has no disability or accessibility entitlement.

At hotel check-in, failure or refusal of this optional presentation SHALL NOT by
itself deny check-in or Hotel Pass issuance.

## 5 Trust anchors

The attestation may be issued by:

- a competent national authority;
- a public-sector disability-card issuer;
- an organisation designated by law;
- a recognised European Disability Card issuer;
- a trusted organisation operating under an approved scheme; or
- an authorised Attestation Provider acting for such an entity.

The trust model SHALL allow the verifier to determine:

1. who authorised the issuer;
2. which scheme the issuer participates in;
3. which claims the issuer may attest;
4. the geographic and service scope of that authority;
5. the applicable signing certificate or trust anchor; and
6. whether the issuer's authorisation remains valid.

For the APTITUDE pilot, issuer trust SHOULD be obtained through the trust framework and
trusted issuer list selected by WP2. The pilot MAY use a mock issuer that advertises
`dc_sd_jwt_EuropeanDisabilityCard` / `urn:eudi:EuropeanDisabilityCard:it:1`.

Where the optional `verification` object is present, its
`trust_framework` and `assurance_level` values SHOULD be interpreted according to
the applicable trust-framework rules (for example `it_wallet` / `eudi_wallet`
and the applicable LoA URIs).

A verifier SHALL verify both:

- the cryptographic trust chain; and
- the issuer's authority to issue `urn:eudi:EuropeanDisabilityCard:it:1`.

The illustrative endpoints in this draft are not operational.

## 6 Revocation



### 6.1 Validity model

The attestation MAY be medium- or long-lived, depending on the issuing scheme.

The issuer SHALL specify administrative expiry through `expiry_date`, and JWT
lifetime through `exp` (and `nbf` where used).

The validity period SHOULD reflect:

- the period of recognition under the scheme;
- review or reassessment requirements;
- expiry of the physical or digital disability card;
- age-related or temporary entitlement conditions; and
- the issuer's status-management capability.



### 6.2 Revocation and status

The attestation SHALL be status-checkable where it is not strictly short-lived.
This profile requires a `status.status_list` object with `idx` and `uri`.

The issuer SHALL revoke or suspend the credential when, for example:

- the credential was issued in error;
- fraud or identity misuse is detected;
- the credential is reported lost or compromised;
- the underlying status or entitlement ends;
- a replacement credential is issued;
- the issuer is no longer authorised; or
- the scheme requires withdrawal.

### 6.3 Status-list location

The target implementation SHOULD use the status-list or revocation-list mechanism
selected by APTITUDE WP2 (compatible with the `status.status_list` shape).

The final production endpoint has not been defined.

Illustrative value:

```text
https://status.example/
```

This SHALL NOT be treated as an operational endpoint.

## 7 Compliance

This Rulebook is designed to align with:

- Regulation (EU) 2024/1183;
- the EUDI Wallet Architecture and Reference Framework;
- ARF Annex 2 Topic 12;
- the issuance and presentation profiles selected by APTITUDE;
- SD-JWT VC and HAIP;
- GDPR principles, including data minimisation and protection by design;
- SEDIT-X's inclusive-by-design approach;
- the APTITUDE European Disability Card profile based on the Italian IT-Wallet /
  Documenti su IO model (IT Wallet Specification v1.3.3);
- OpenID4VCI configuration
  `dc_sd_jwt_EuropeanDisabilityCard` / scope `EuropeanDisabilityCard`; and
- the European Disability Card example in APTITUDE UC7 (pilot use of mock data).

The Rulebook enforces these properties:

1. `vct` is `urn:eudi:EuropeanDisabilityCard:it:1` and the configuration id is
  `dc_sd_jwt_EuropeanDisabilityCard`;
2. the claim set is
  (`issuing_authority`, `issuing_country`, `expiry_date`, `link_qr_code`,
  `given_name`, `family_name`, `birth_date`, `portrait`,
  `constant_attendance_allowance`, `document_number`, plus registered JWT /
  SD-JWT claims);
3. the attestation expresses card recognition and constant attendance allowance
  rather than diagnosis;
4. claims are selectively disclosable;
5. identity data and portrait are requested only where operationally needed;
6. SEDIT-X Episode 4 primarily requests `constant_attendance_allowance`;
7. no biometric template is issued;
8. the credential may support transport, hospitality and academic services;
9. hospitality check-in use is optional;
10. user consent is required for presentation;
11. special-category data receives enhanced protection;
12. status and revocation are supported via `status.status_list`;
13. credential copies are not routinely retained; and
14. manual fallback remains available.

The following matters remain open:

- legal category by issuer and Member State (including possible PuB-EAA issuance);
- final PID-binding policy;
- final trust-list service types and endpoints;
- final status-list mechanism;
- national and cross-border entitlement-recognition rules;
- hotel assistance-request workflows after a positive verification;
- handling of temporary entitlements; and
- retention rules for transport and hospitality operators.



## 8 References


| **Item Reference**                     | **Standard name/details**                                                                                                                                                                     |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [European Disability Card Regulation]  | Regulation (EU) 2024/2841 of the European Parliament and of the Council on the European Disability Card and the European Parking Card                                                         |
| [IT-Wallet Specs]                      | Italian IT-Wallet Technical Specifications (Department for Digital Transformation / IPZS), including v1.3.3 — https://github.com/italia/eid-wallet-it-docs                                    |
| [IT-Wallet Docs]                       | Official IT-Wallet Technical Documentation — https://italia.github.io/eid-wallet-it-docs/                                                                                                     |
| [IT-Wallet PID-EAA data model]         | Digital Credential / PID-(Q)EAA data model (European Disability Card SD-JWT examples) — https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pid-eaa-data-model.html            |
| [IT-Wallet Credential Issuer config]   | Credential Issuer entity configuration (`dc_sd_jwt_EuropeanDisabilityCard`, scope `EuropeanDisabilityCard`, `vct` `urn:eudi:EuropeanDisabilityCard:it:1`) — https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pid-eaa-entity-configuration.html |
| [IT-Wallet Issuance]                   | PID-(Q)EAA issuance flow with `scope=EuropeanDisabilityCard` — https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pid-eaa-issuance.html                                         |
| [APTITUDE D4.1]                        | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026                                                                                                                    |
| [APTITUDE UC7]                         | Accessing Discounted Train Fares via EUDIW — European Disability Card example and candidate data model                                                                                        |
| [SEDIT-X Airport Working Paper]        | APTITUDE WP4, SEDIT-X at the Airport, Version 4.1, May 2026                                                                                                                                   |
| [SEDIT-X Hospitality Working Paper]    | SEDIT-X Frictionless Hotel Check-in and Guest Verification Using the EUDI Wallet                                                                                                              |
| [ARF]                                  | European Digital Identity Wallet Architecture and Reference Framework                                                                                                                         |
| [HAIP]                                 | OpenID4VC High Assurance Interoperability Profile                                                                                                                                             |
| [OIDC]                                 | OpenID Connect Core 1.0                                                                                                                                                                       |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance                                                                                                                                                     |
| [OpenID4VP]                            | OpenID for Verifiable Presentations                                                                                                                                                           |
| [RFC 2119]                             | Key words for use in RFCs to Indicate Requirement Levels                                                                                                                                      |
| [RFC 3339]                             | Date and Time on the Internet: Timestamps                                                                                                                                                     |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials                                                                                                                                                           |
| [Topic 7]                              | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking                                                                                                                         |
| [Topic 10]                             | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit                                                                                                                         |
| [Topic 12]                             | ARF Annex 2, Topic 12 — Attestation Rulebooks                                                                                                                                                 |
| [ETSI TS 119 472-1]                    | Electronic Signatures and Trust Infrastructures; Electronic Attestation of Attributes; Part 1: Building blocks and general requirements                                                       |
| [PID Implementing Regulation]          | Commission Implementing Regulation (EU) 2024/2977 — PID                                                                                                                                       |
| [Accommodation Voucher Rulebook]       | APTITUDE WP4 Rulebook for `booking_reference_credential`                                                                                                                                      |
| [Hotel Pass Rulebook]                  | APTITUDE WP4 Rulebook for `room_key_credential`                                                                                                                                               |
