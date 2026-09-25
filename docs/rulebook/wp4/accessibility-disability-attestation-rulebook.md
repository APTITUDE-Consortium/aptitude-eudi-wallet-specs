# Attestation Rulebook for attestations of type European Disability Card

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                                        |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X use case, APTITUDE UC7 material and the APTITUDE Attestation Rulebook template. |
| 0.2     | 26-08-2026 | Aligned with the issuer schema for European Disability Card (`european_disability_card`, `vct` `urn:eu.europa.ec.eudi:edc:1`) and optional hospitality check-in use. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the **European Disability Card** for the APTITUDE /
> SEDIT-X pilot. The issuer-configuration identifier is `european_disability_card`.
> The Verifiable Credential Type (`vct`) is `urn:eu.europa.ec.eudi:edc:1`.
>
> The attribute model below SHALL match the APTITUDE issuer configuration. Domain-
> specific service outcomes (for example an easier-access hotel room) are produced
> by the Relying Party after verification; they are not encoded as additional
> claims in this credential.



## 1 Introduction



### 1.1 Document scope and purpose

This Rulebook defines the **European Disability Card**, an Electronic Attestation
of Attributes stored in a User's EUDI Wallet and used to prove recognised
disability status and, where applicable, assistant entitlement.

The issuer-configuration identifier is:

```text
european_disability_card
```

The Verifiable Credential Type (`vct`) is:

```text
urn:eu.europa.ec.eudi:edc:1
```

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

The attestation SHALL express verified **status or entitlement**, not medical
diagnosis. It SHALL disclose only the minimum information needed for the current
service decision.

In the hospitality check-in flow, presentation is **optional**. The hotel
verifies the Accommodation Voucher and PID regardless. Where the guest offers
this card, the hotel MAY use `disability_status_recognised` and
`assistant_entitlement` to trigger its assistance process (for example room
type, access arrangements or staff support). Those operational outcomes SHALL
NOT be written back into this credential.

The primary objectives are to:

1. enable trusted verification of recognised disability status;
2. enable selective disclosure of assistant entitlement where relevant;
3. reduce repeated presentation of paper disability cards or supporting documents;
4. avoid disclosure of health information not needed by the service provider;
5. support cross-border use where the issuer and verifier participate in a recognised
  trust framework; and
6. allow operational service systems to receive a clear eligibility outcome.



### 1.2 Document structure

This Rulebook is structured as follows:

- Chapter 2 defines attributes and metadata in an encoding-independent manner.
- Chapter 3 defines the SD-JWT VC encoding and discusses optional mdoc support.
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

- **European Disability Card** means the attestation of type
  `european_disability_card` with `vct` `urn:eu.europa.ec.eudi:edc:1`.
- **Recognised disability status** means confirmation that the holder is
  recognised under the applicable disability-card scheme
  (`disability_status_recognised`).
- **Assistant entitlement** means the verified right to be accompanied or
  assisted by another person under the applicable scheme
  (`assistant_entitlement`).
- **Service provider** means an authorised transport, hospitality, mobility,
  education or other organisation acting as Relying Party.
- **Accommodation Voucher** means the hotel-booking attestation of type
  `booking_reference_credential`.
- **PID** means Person Identification Data of type `urn:eu.europa.ec.eudi:pid:1`.



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
the relevant status and entitlements.

The credential attribute set SHALL match the APTITUDE issuer configuration for
`european_disability_card`.

### 2.1 Design principles

The following design principles apply:

1. **Entitlement, not diagnosis:** the credential SHALL represent recognised
  status and assistant entitlement rather than diagnostic or clinical data.
2. **Selective disclosure:** each claim SHOULD be independently disclosable.
3. **Minimum identity disclosure:** name, birth date, serial number and portrait
  SHALL be requested only where needed for fraud prevention, visual inspection
  or legal rules.
4. **Portrait is a card image, not a biometric template:** the credential MAY
  contain `portrait` as a data-URL image consistent with the card scheme. It
  SHALL NOT contain a biometric template, biometric reference, fingerprint,
  iris data or any other biometric sample. A verifier SHALL NOT extract a
  biometric template from `portrait` unless a specific legal basis exists.
5. **No inferred diagnosis:** a verifier SHALL NOT infer a diagnosis from
  recognised status or assistant entitlement.
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


| **Data Identifier**              | **Definition**                                                                                          | **Data type** | **Example value**                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------------- |
| `id`                             | Unique identifier of this card instance.                                                                | string        | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `family_name`                    | Holder's family name as recorded on the card.                                                           | string        | `Matkalainen`                          |
| `given_name`                     | Holder's given name as recorded on the card.                                                            | string        | `Hanna`                                |
| `birth_date`                     | Holder's date of birth as recorded on the card.                                                         | date          | `1990-05-23`                           |
| `serial_number`                  | Serial number of the European Disability Card.                                                          | string        | `EDC-FI-2026-0001234`                  |
| `issue_date`                     | Date of issue of the card.                                                                              | date          | `2026-01-15`                           |
| `expiry_date`                    | Date of expiry of the card.                                                                             | date          | `2031-01-14`                           |
| `issuing_country`                | ISO 3166-1 alpha-2 country code of the issuing jurisdiction.                                            | string        | `FI`                                   |
| `portrait`                       | Facial image of the holder as a data URL, for visual inspection where required.                         | string        | `data:image/jpeg;base64,...`           |
| `assistant_entitlement`          | Indicates that the holder is entitled to an assistant or accompanying person under the scheme.          | boolean       | `true`                                 |
| `disability_status_recognised`   | Indicates that the holder is recognised under the applicable disability-card scheme.                    | boolean       | `true`                                 |


`issuing_country` SHALL use ISO 3166-1 alpha-2 codes.

`portrait` SHALL be a `data:` URL image. It is a card photograph for visual
comparison. It SHALL NOT be treated as authorisation to perform automated
biometric matching unless a specific legal basis exists.

`disability_status_recognised` is the primary status claim. A Relying Party
SHALL NOT request diagnostic detail in addition to this boolean in order to
accept the card.

`assistant_entitlement` is the primary entitlement claim for companion or
assistant-related service decisions.

### 2.3 Optional attributes

This issuer profile does not define additional optional attribute claims beyond
the set in section 2.2. Wallet display metadata MAY still be provided as in
section 2.6.

PID remains a separate credential. Where stronger identity matching is required,
the Relying Party SHALL request PID (`urn:eu.europa.ec.eudi:pid:1`) rather than
extending this card.

### 2.4 Conditional attributes


| **Data Identifier**          | **Definition**                                                                 | **Data type** | **Example value**             |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------- | ----------------------------- |
| `cryptographically_bound_to` | Attestation type to which this credential is cryptographically bound. Present where formal binding to PID is required. | string        | `urn:eu.europa.ec.eudi:pid:1` |


Where `cryptographically_bound_to` is present, its value SHOULD identify the PID type
used to bind the holder to the attestation:

```text
urn:eu.europa.ec.eudi:pid:1
```



### 2.5 Mandatory metadata


| **Data Identifier**      | **Definition**                                                           | **Data type**           | **Example value**                                      |
| ------------------------ | ------------------------------------------------------------------------ | ----------------------- | ------------------------------------------------------ |
| `category`               | Legal category of the attestation.                                       | string                  | `eaa:eu:non-qualified`                                 |
| `issuer`                 | Identifier of the competent authority or trusted Attestation Provider.   | string or URI           | `https://issuer.dvv.example`                           |
| `credential_type`        | Encoding-independent credential type identifier. SHALL equal the `vct`.  | string                  | `urn:eu.europa.ec.eudi:edc:1`                          |
| `issued_at`              | Time of credential issuance.                                             | date-time               | `2026-01-15T09:30:00Z`                                 |
| `status_reference`       | Reference used for status or revocation checking. Credential identification for status purposes SHALL be expressed only through this status metadata (for example status-list URI and index), not through a separate attestation identifier claim beyond `id`. | URI or structured value | `https://status.example/edc/atl/2026-01/15#1234` |
| `trust_anchor_reference` | Location from which applicable issuer trust information can be obtained. | URI                     | `https://trust.aptitude.example/accessibility-issuers` |




### 2.6 Optional metadata


| **Data Identifier**      | **Definition**                                | **Data type** | **Example value**                                   |
| ------------------------ | --------------------------------------------- | ------------- | --------------------------------------------------- |
| `credential_name`        | Human-readable wallet display name.           | string        | `European Disability Card`                          |
| `credential_description` | Human-readable explanation of the credential. | string        | `Recognised disability status and assistant entitlement` |
| `issuer_name`            | Human-readable issuer name.                   | string        | `Digital and Population Data Services Agency`       |
| `issuer_logo_uri`        | URI of the issuer logo.                       | URI           | `https://issuer.example/logo.png`                   |
| `privacy_notice`         | URI of the applicable privacy notice.         | URI           | `https://issuer.example/privacy`                    |
| `issuer_policy`          | URI of the issuance and verification policy.  | URI           | `https://issuer.example/policy`                     |
| `terms_of_use`           | URI of terms governing credential use.        | URI           | `https://issuer.example/terms`                      |
| `display_locale`         | Preferred language for wallet display.        | string        | `en`                                                |




### 2.7 Conditional metadata


| **Data Identifier**   | **Definition**                                                                                         | **Data type** | **Example value**                         |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ------------- | ----------------------------------------- |
| `status_list_index`   | Entry index in an applicable Attestation Status List. Mandatory when a list-based mechanism is used.   | integer       | `1234`                                    |
| `status_list_uri`     | URI of the applicable Attestation Status List. Mandatory when list-based status is used.               | URI           | `https://status.example/edc/atl/2026-01/15` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI           | `https://status.example/edc/arl/2026-01`  |




# 3 Attestation encoding



## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not mandate mdoc as the primary encoding.

A future deployment MAY define an ISO/IEC 18013-5-compliant representation where:

- offline or proximity presentation is a core requirement;
- the applicable accessibility scheme supports mdoc issuance;
- a unique document type and namespace are approved; and
- the same selective-disclosure and minimisation principles are preserved.

Until an mdoc profile is approved, an issuer SHALL NOT advertise an mdoc document type
for this attestation.

## 3.2 SD-JWT VC-based encoding



### 3.2.1 Verifiable Credential Type

The Verifiable Credential Type SHALL be:

```text
urn:eu.europa.ec.eudi:edc:1
```

This matches the APTITUDE issuer configuration identifier `european_disability_card`.

The credential SHALL be issued as `dc+sd-jwt` and SHALL comply with the SD-JWT VC
and HAIP profiles selected by APTITUDE WP2.

### 3.2.2 Registered JWT claims


| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes**                          | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | -------------------------------------------- | --------------- |
| `issuer`            | `iss`                    | string              | JWT issuer identifier                        | MUST NOT        |
| `issued_at`         | `iat`                    | integer             | NumericDate                                  | MUST NOT        |
| `valid_from`        | `nbf`                    | integer             | NumericDate where used. Distinct from card `issue_date`. | MUST NOT        |
| `expires_at`        | `exp`                    | integer             | NumericDate where used. Distinct from card `expiry_date`. | MUST NOT        |
| `credential_type`   | `vct`                    | string              | SD-JWT VC type. SHALL be `urn:eu.europa.ec.eudi:edc:1`. | MUST NOT        |
| `holder_binding`    | `cnf`                    | object              | Holder-binding confirmation key, where used  | MUST NOT        |
| `status_reference`  | `status`                 | object              | Credential status metadata.                  | MUST NOT        |




### 3.2.3 Private claims specific to this attestation


| **Data Identifier**            | **Attribute identifier**       | **Encoding format** | **Notes**                             | **Disclosable** |
| ------------------------------ | ------------------------------ | ------------------- | ------------------------------------- | --------------- |
| `category`                     | `category`                     | string              | ETSI EAA category                     | MUST NOT        |
| `id`                           | `id`                           | string              | Card instance identifier              | MUST NOT        |
| `family_name`                  | `family_name`                  | string              | Card family name                      | MUST            |
| `given_name`                   | `given_name`                   | string              | Card given name                       | MUST            |
| `birth_date`                   | `birth_date`                   | string              | ISO 8601 date                         | MUST            |
| `serial_number`                | `serial_number`                | string              | Card serial number                    | MUST            |
| `issue_date`                   | `issue_date`                   | string              | ISO 8601 date                         | MUST            |
| `expiry_date`                  | `expiry_date`                  | string              | ISO 8601 date                         | MUST            |
| `issuing_country`              | `issuing_country`              | string              | ISO 3166-1 alpha-2                    | MUST            |
| `portrait`                     | `portrait`                     | string              | Data-URL card photograph              | MUST            |
| `assistant_entitlement`        | `assistant_entitlement`        | boolean             | Assistant / accompanying-person right | MUST            |
| `disability_status_recognised` | `disability_status_recognised` | boolean             | Recognised status under the scheme    | MUST            |
| `cryptographically_bound_to`   | `cryptographically_bound_to`   | string              | PID type where bound                  | MUST NOT        |
| `trust_anchor_reference`       | `trust_anchor_reference`       | string              | Trust-anchor lookup                   | MUST NOT        |
| `privacy_notice`               | `privacy_notice`               | string              | Privacy information                   | MAY             |


A verifier SHALL be able to request `disability_status_recognised` and
`assistant_entitlement` without also receiving `portrait`, `serial_number` or
name claims.

### 3.2.4 Illustrative JWT claim set

```json
{
  "iss": "https://issuer.dvv.example",
  "iat": 1768464000,
  "nbf": 1768464000,
  "exp": 1926288000,
  "vct": "urn:eu.europa.ec.eudi:edc:1",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 1234,
      "uri": "https://status.example/edc/atl/2026-01/15"
    }
  },
  "category": "eaa:eu:non-qualified",
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "family_name": "Matkalainen",
  "given_name": "Hanna",
  "birth_date": "1990-05-23",
  "serial_number": "EDC-FI-2026-0001234",
  "issue_date": "2026-01-15",
  "expiry_date": "2031-01-14",
  "issuing_country": "FI",
  "portrait": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...",
  "assistant_entitlement": true,
  "disability_status_recognised": true,
  "trust_anchor_reference": "https://trust.aptitude.example/accessibility-issuers",
  "privacy_notice": "https://issuer.example/privacy"
}
```

The example includes more attributes than a normal presentation should disclose. An
actual service request SHALL select only the relevant claims.

### 3.2.5 Human-readable wallet representation

The Wallet Unit SHOULD display:

```text
European Disability Card
Holder: Hanna Matkalainen
Serial number: EDC-FI-2026-0001234
Issuing country: FI
Recognised status: Yes
Assistant entitlement: Yes
Valid until: 14 January 2031
```

The Wallet Unit SHOULD inform the User that:

- only selected claims will be disclosed;
- diagnosis and clinical information are not part of the credential;
- `portrait` is requested only where visual inspection is needed;
- the verifier will use the disclosed claims for the stated service purpose;
- the User can refuse the presentation; and
- a manual or staff-assisted process should remain available.



## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C VCDM representation.

## 4 Attestation usage



### 4.1 Issuance prerequisites

Before issuance, the Attestation Provider SHALL:

1. verify that the applicant is recognised under the applicable scheme;
2. determine whether assistant entitlement applies;
3. verify identity to the level required by the scheme;
4. confirm the card validity period;
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
- other health information not needed to express recognised status and assistant
  entitlement.

`portrait` MAY be included as the card photograph.

### 4.2 Device and holder binding

The attestation **SHOULD be device-bound** to a key controlled by the Wallet Unit.

Where the scheme requires strong anti-fraud protection, the credential SHOULD also be
bound to the holder through:

- PID-based issuance;
- holder-binding key material; or
- another approved scheme mechanism.

A Relying Party SHOULD request PID only where necessary to prevent misuse, satisfy
legal requirements or resolve ambiguity. It SHOULD NOT routinely request PID when
recognised status or assistant entitlement alone is sufficient.

Where both this card and PID are presented, `family_name`, `given_name` and
`birth_date` SHOULD be compared with PID `family_name`, `given_name` and
`birthdate`.

### 4.3 Presentation contexts

The attestation may be presented remotely or in proximity.

Relevant SEDIT-X contexts include:

#### Airport

A verifier MAY request:

- `disability_status_recognised`;
- `assistant_entitlement`, where companion or assistant processing is offered; and
- name, `serial_number` or `portrait` only where staff visual inspection or
  anti-fraud checks require them.

#### Ferry transport

A verifier or booking portal MAY request:

- `disability_status_recognised`;
- `assistant_entitlement`, where a companion or assistant fare or boarding
  process is offered; and
- identity claims only where required to bind the entitlement to the ticket.

#### Hospitality check-in

Presentation at hotel check-in is **optional** and occurs after or together with
the Accommodation Voucher (`booking_reference_credential`) and PID
(`urn:eu.europa.ec.eudi:pid:1`).

A hotel MAY request:

- `disability_status_recognised`, to confirm that accessibility assistance may
  be offered;
- `assistant_entitlement`, where an accompanying person or in-room assistance
  is requested; and
- name claims only where needed to bind the request to the checked-in guest.

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

A university MAY request `disability_status_recognised` and, where relevant,
`assistant_entitlement`, plus identity claims only where required by
institution policy.

### 4.4 Relying Party obligations

The Relying Party or EUDIW Intermediary Service SHALL:

1. verify signature and cryptographic integrity;
2. verify issuer trust and authorisation;
3. verify validity and status, including `issue_date` and `expiry_date`;
4. verify holder binding where required;
5. verify that `disability_status_recognised` is `true` where recognition is
  required for the service;
6. verify `assistant_entitlement` only where an assistant-related service is
  requested;
7. avoid requesting diagnosis or unrelated attributes;
8. avoid inferring disability type from the disclosed claims;
9. provide the service outcome or route the request to staff;
10. retain only the minimum operational result; and
11. provide a non-digital or staff-assisted alternative where appropriate.

A typical hospitality result SHOULD be limited to:

```json
{
  "credential_valid": true,
  "disability_status_recognised": true,
  "assistant_entitlement": true,
  "decision": "assistance_offered",
  "correlation_id": "acc_01JZ..."
}
```


### 4.5 Identity attributes

Name, birth date, serial number and portrait MAY be present in the issued
credential. A verifier SHALL request them only where needed.

Examples:

- a ticket portal generally SHOULD request `disability_status_recognised` and
  `assistant_entitlement`, not name or portrait;
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

A transport or service discount MAY be applied based on verified recognition or
assistant entitlement. Payment authorisation and payment confirmation SHALL remain
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
- `disability_status_recognised` is not `true` where recognition is required;
- `assistant_entitlement` is required for the requested service and is not
  `true`;
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
trusted issuer list selected by WP2.

A verifier SHALL verify both:

- the cryptographic trust chain; and
- the issuer's authority to issue `urn:eu.europa.ec.eudi:edc:1`.

The illustrative endpoints in this draft are not operational.

## 6 Revocation



### 6.1 Validity model

The attestation MAY be medium- or long-lived, depending on the issuing scheme.

The issuer SHALL specify `issue_date` and `expiry_date`.

The validity period SHOULD reflect:

- the period of recognition under the scheme;
- review or reassessment requirements;
- expiry of the physical or digital disability card;
- age-related or temporary entitlement conditions; and
- the issuer's status-management capability.



### 6.2 Revocation and status

The attestation SHALL be status-checkable where it is not strictly short-lived.

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
selected by APTITUDE WP2.

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
- the APTITUDE issuer configuration for `european_disability_card`; and
- the European Disability Card example in APTITUDE UC7.

The Rulebook enforces these properties:

1. `vct` is `urn:eu.europa.ec.eudi:edc:1` and the configuration id is
  `european_disability_card`;
2. the issuer-config claim set is used
  (`id`, `family_name`, `given_name`, `birth_date`, `serial_number`,
  `issue_date`, `expiry_date`, `issuing_country`, `portrait`,
  `assistant_entitlement`, `disability_status_recognised`);
3. the attestation expresses recognised status and assistant entitlement rather
  than diagnosis;
4. claims are selectively disclosable;
5. identity data and portrait are requested only where operationally needed;
6. no biometric template is issued;
7. the credential may support transport, hospitality and academic services;
8. hospitality check-in use is optional;
9. user consent is required for presentation;
10. special-category data receives enhanced protection;
11. status and revocation are supported;
12. credential copies are not routinely retained; and
13. manual fallback remains available.

The following matters remain open:

- legal category by issuer and Member State (including possible PuB-EAA issuance);
- whether mdoc is required for proximity scenarios;
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
| [APTITUDE issuer-config]               | NXD-Foundation / nxd-wallet-conformance-backend, `data/issuer-config.json`, `european_disability_card`                                                                                        |
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

