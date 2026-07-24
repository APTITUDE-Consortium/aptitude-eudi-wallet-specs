# Attestation Rulebook for attestations of type Accessibility / Disability Attestation

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                                        |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X use case, APTITUDE UC7 material and the APTITUDE Attestation Rulebook template. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The SEDIT-X material defines the
> Accessibility / Disability Attestation at a high level as a wallet credential supporting
> selective disclosure of accessibility-related entitlements across transport, hospitality
> and academic services. It does not yet define a complete SEDIT-X-specific claim set.



## 1 Introduction



### 1.1 Document scope and purpose

This Rulebook defines the **Accessibility / Disability Attestation**, an Electronic
Attestation of Attributes stored in a User's EUDI Wallet and used to prove one or more
verified accessibility-related entitlements.

The attestation is intended to enable inclusive and equal access to services without
requiring the User to repeatedly disclose medical records, diagnostic details or a complete
disability profile.

Within SEDIT-X, the attestation may support:

- airport assistance and accessible passenger processing;
- ferry or other transport discounts and companion entitlements;
- priority or assisted boarding;
- accessible hotel services;
- mobility-related assistance;
- university and campus accessibility services; and
- other service accommodations accepted by an authorised Relying Party.

The attestation SHALL express verified **status or entitlement**, not medical diagnosis.
It SHALL disclose only the minimum information needed for the current service decision.

The primary objectives are to:

1. enable trusted verification of accessibility-related rights;
2. support selective disclosure of only the applicable entitlement;
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

- **Accessibility entitlement** means a verified right, benefit, accommodation or
service condition available to the holder.
- **Companion entitlement** means the verified right to be accompanied by another
person under the applicable scheme.
- **Support need** means an operational accommodation that may be requested by the
User. It does not itself reveal diagnosis or clinical details.
- **Disability status** means confirmation that the holder is recognised under an
applicable disability or accessibility scheme.
- **Service provider** means an authorised transport, hospitality, mobility, education
or other organisation acting as Relying Party.
- **European Disability Card** means the disability-card profile referenced by the
APTITUDE UC7 source material.



## 2 Attestation attributes and metadata



### Chapter overview and requirements

This chapter defines the attributes and metadata of the Accessibility / Disability
Attestation in an encoding-independent manner.

For the SEDIT-X pilot, the attestation is defined as a **non-qualified EAA** unless it is
issued under a legal and trust framework that qualifies it as a QEAA or PuB-EAA.

The pilot category value is therefore:

```text
eaa:eu:non-qualified
```

The attestation SHALL be based on data from a competent public authority, public issuer,
recognised disability-card scheme, or another trusted organisation authorised to attest
the relevant accessibility rights.

### 2.1 Design principles

The following design principles apply:

1. **Entitlement, not diagnosis:** the credential SHALL represent rights and service
  entitlements rather than diagnostic or clinical data.
2. **Selective disclosure:** each entitlement SHOULD be independently disclosable.
3. **Minimum identity disclosure:** name, birth date and card number SHALL
  be requested only where needed for fraud prevention, visual inspection or legal rules.
4. **No biometrics:** the credential SHALL NOT contain a portrait, biometric template,
  biometric reference or any other biometric data.
5. **No inferred diagnosis:** a verifier SHALL NOT infer a diagnosis from an entitlement.
6. **Context-specific requests:** a ferry operator, airport, hotel or university SHALL
  request only claims needed for the specific service.
7. **User control:** presentation SHALL require informed User approval.
8. **No unnecessary retention:** verifiers SHOULD retain only the decision and minimum
  operational reference.
9. **Cross-domain reuse:** one credential MAY support multiple service domains where
  the entitlement semantics are accepted by each relevant service policy.
10. **Fallback:** a User who cannot or does not present the credential SHALL retain access
  to an appropriate manual or assisted process.



### 2.2 Mandatory attributes


| **Data Identifier** | **Definition**                                                                                   | **Data type**     | **Example value**                                 |
| ------------------- | ------------------------------------------------------------------------------------------------ | ----------------- | ------------------------------------------------- |
| `recognised_status` | Indicates that the holder is recognised under the applicable accessibility or disability scheme. | boolean           | `true`                                            |
| `scheme_id`         | Identifier of the applicable national, European or organisational scheme.                        | string            | `eu_disability_card`                              |
| `issuing_country`   | Country code of the issuing jurisdiction or scheme authority.                                    | string            | `ITA`                                             |
| `entitlements`      | Set of verified accessibility-related entitlements associated with the holder.                   | array of strings  | `["companion_entitlement","priority_assistance"]` |
| `valid_from`        | Start date of the attestation's validity.                                                        | date or date-time | `2026-01-01`                                      |
| `valid_until`       | End date of the attestation's validity.                                                          | date or date-time | `2028-12-31`                                      |


The `entitlements` array SHALL contain one or more values from an approved controlled
vocabulary.

The controlled vocabulary proposed by this Rulebook includes:

- `companion_entitlement`;
- `additional_support`;
- `priority_assistance`;
- `assisted_boarding`;
- `priority_boarding`;
- `reduced_fare`;
- `free_companion_fare`;
- `accessible_seating`;
- `wheelchair_assistance`;
- `step_free_access`;
- `accessible_room`;
- `accessible_transport`;
- `campus_accessibility_support`;
- `communication_assistance`; and
- `other_verified_entitlement`.

A deployment SHALL use only the values relevant to its service and legal context.

### 2.3 Optional attributes


| **Data Identifier**              | **Definition**                                                                                    | **Data type**    | **Example value**                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------- |
| `family_name`                    | Holder's family name. Included only where necessary for identity binding or visual inspection.    | string           | `Rossi`                                              |
| `given_name`                     | Holder's given name. Included only where necessary for identity binding or visual inspection.     | string           | `Giulia`                                             |
| `birth_date`                     | Holder's date of birth. Included only where required for identity binding or policy checks.       | date             | `1994-05-18`                                         |
| `card_serial_number`             | Serial number of the physical or digital disability card.                                         | string           | `EDC-IT-2026-0048921`                                |
| `subject_reference`              | Pairwise or scheme-specific pseudonymous reference to the holder.                                 | string           | `subj_74b18fd0`                                      |
| `entitlement_level`              | Scheme-defined level relevant to a particular benefit.                                            | string           | `level_2`                                            |
| `entitlement_scope`              | Geographic, organisational or service-domain scope of the entitlement.                            | array of strings | `["EU","transport"]`                                 |
| `support_categories`             | Categories of operational support that may be requested.                                          | array of strings | `["mobility_assistance","communication_assistance"]` |
| `companion_count`                | Maximum number of companions covered by the entitlement.                                          | integer          | `1`                                                  |
| `discount_percentage`            | Verified discount percentage, where the issuing scheme directly defines it.                       | integer          | `50`                                                 |
| `free_companion`                 | Indicates that one eligible companion is entitled to a free ticket or service.                    | boolean          | `true`                                               |
| `wheelchair_user`                | Indicates eligibility for wheelchair-specific services. SHOULD be disclosed only where necessary. | boolean          | `true`                                               |
| `service_animal_entitlement`     | Indicates entitlement to travel or enter with an assistance animal.                               | boolean          | `true`                                               |
| `communication_preference`       | Operational communication mode requested by the User.                                             | string           | `sign_language`                                      |
| `emergency_assistance_reference` | Optional reference to an approved emergency-assistance profile without exposing medical details.  | string           | `ear_01JZ...`                                        |


The optional attributes above SHALL NOT be interpreted as a recommendation that every
Accessibility / Disability Attestation contain them.

### 2.4 Conditional attributes


| **Data Identifier**              | **Definition**                                                                                                                                 | **Data type**    | **Example value**                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------ |
| `companion_entitlement`          | Indicates entitlement to an accompanying person. Mandatory where the scheme explicitly grants this right and the User chooses to disclose it.  | boolean          | `true`                                                 |
| `additional_support_entitlement` | Indicates entitlement to additional support. Mandatory where the scheme explicitly grants this right and the User chooses to disclose it.      | boolean          | `true`                                                 |
| `support_validity_context`       | Conditions or service domains in which a disclosed support entitlement is valid. Mandatory where an entitlement is not universally applicable. | array of strings | `["rail","ferry","airport"]`                           |
| `cryptographically_bound_to`     | Attestation type to which this credential is cryptographically bound. Present where formal binding to PID is required.                         | string           | `urn:eu.europa.ec.eudi:pid:1`                          |


Where `cryptographically_bound_to` is present, its value SHOULD identify the PID type
used to bind the holder to the attestation:

```text
urn:eu.europa.ec.eudi:pid:1
```



### 2.5 Mandatory metadata


| **Data Identifier**      | **Definition**                                                           | **Data type**           | **Example value**                                               |
| ------------------------ | ------------------------------------------------------------------------ | ----------------------- | --------------------------------------------------------------- |
| `category`               | Legal category of the attestation.                                       | string                  | `eaa:eu:non-qualified`                                          |
| `issuer`                 | Identifier of the competent authority or trusted Attestation Provider.   | string or URI           | `https://issuer.ipzs.example`                                   |
| `credential_type`        | Encoding-independent credential type identifier.                         | string                  | `urn:aptitude.eu:seditx:accessibility-disability-attestation:1` |
| `issued_at`              | Time of credential issuance.                                             | date-time               | `2026-07-23T09:30:00Z`                                          |
| `schema_version`         | Version of the credential schema.                                        | string                  | `0.1`                                                           |
| `status_reference`       | Reference used for status or revocation checking. Credential identification for status purposes SHALL be expressed only through this status metadata (for example status-list URI and index), not through a separate attestation identifier claim. | URI or structured value | `https://status.example/atl/2026-07/42#812` |
| `trust_anchor_reference` | Location from which applicable issuer trust information can be obtained. | URI                     | `https://trust.aptitude.example/accessibility-issuers`          |




### 2.6 Optional metadata


| **Data Identifier**      | **Definition**                                | **Data type** | **Example value**                                   |
| ------------------------ | --------------------------------------------- | ------------- | --------------------------------------------------- |
| `credential_name`        | Human-readable wallet display name.           | string        | `Accessibility Attestation`                         |
| `credential_description` | Human-readable explanation of the credential. | string        | `Verified accessibility and companion entitlements` |
| `issuer_name`            | Human-readable issuer name.                   | string        | `National Disability Card Authority`                |
| `issuer_logo_uri`        | URI of the issuer logo.                       | URI           | `https://issuer.example/logo.png`                   |
| `privacy_notice`         | URI of the applicable privacy notice.         | URI           | `https://issuer.example/privacy`                    |
| `issuer_policy`          | URI of the issuance and verification policy.  | URI           | `https://issuer.example/policy`                     |
| `terms_of_use`           | URI of terms governing credential use.        | URI           | `https://issuer.example/terms`                      |
| `display_locale`         | Preferred language for wallet display.        | string        | `en`                                                |




### 2.7 Conditional metadata


| **Data Identifier**   | **Definition**                                                                                         | **Data type** | **Example value**                       |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ------------- | --------------------------------------- |
| `status_list_index`   | Entry index in an applicable Attestation Status List. Mandatory when a list-based mechanism is used.   | integer       | `812`                                   |
| `status_list_uri`     | URI of the applicable Attestation Status List. Mandatory when list-based status is used.               | URI           | `https://status.example/atl/2026-07/42` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI           | `https://status.example/arl/2026-07`    |




# 3 Attestation encoding



## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 of this Rulebook does not mandate mdoc as the primary encoding.

A future deployment MAY define an ISO/IEC 18013-5-compliant representation where:

- offline or proximity presentation is a core requirement;
- the applicable accessibility scheme supports mdoc issuance;
- a unique document type and namespace are approved; and
- the same selective-disclosure and minimisation principles are preserved.

Until an mdoc profile is approved, an issuer SHALL NOT advertise an mdoc document type
for this attestation.

## 3.2 SD-JWT VC-based encoding



### 3.2.1 Verifiable Credential Type

The proposed Verifiable Credential Type is:

```text
urn:aptitude.eu:seditx:accessibility-disability-attestation:1
```

This is a pilot identifier and requires confirmation by APTITUDE governance.

The credential SHALL comply with the SD-JWT VC and HAIP profiles selected by
APTITUDE WP2.

### 3.2.2 Registered JWT claims


| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes**                          | **Disclosable** |
| ------------------- | ------------------------ | ------------------- | -------------------------------------------- | --------------- |
| `issuer`            | `iss`                    | string              | JWT issuer identifier                        | MUST NOT        |
| `issued_at`         | `iat`                    | integer             | NumericDate                                  | MUST NOT        |
| `valid_until`       | `exp`                    | integer             | NumericDate where date-time expiry is used   | MUST NOT        |
| `valid_from`        | `nbf`                    | integer             | NumericDate where date-time validity is used | MUST NOT        |
| `credential_type`   | `vct`                    | string              | SD-JWT VC type                               | MUST NOT        |
| `holder_binding`    | `cnf`                    | object              | Holder-binding confirmation key, where used  | MUST NOT        |
| `status_reference`  | `status`                 | object              | Credential status metadata. This is the only credential-instance identifier used for status and revocation; a separate `attestation_id` claim SHALL NOT be issued. | MUST NOT        |
| `family_name`       | `family_name`            | string              | OIDC registered claim                        | MUST            |
| `given_name`        | `given_name`             | string              | OIDC registered claim                        | MUST            |
| `birth_date`        | `birthdate`              | string              | OIDC registered claim                        | MUST            |




### 3.2.3 Private claims specific to this attestation


| **Data Identifier**              | **Attribute identifier**         | **Encoding format** | **Notes**                             | **Disclosable** |
| -------------------------------- | -------------------------------- | ------------------- | ------------------------------------- | --------------- |
| `category`                       | `category`                       | string              | ETSI EAA category                     | MUST NOT        |
| `recognised_status`              | `recognised_status`              | boolean             | Recognition under the scheme          | MUST            |
| `scheme_id`                      | `scheme_id`                      | string              | Disability/accessibility scheme       | MUST            |
| `issuing_country`                | `issuing_country`                | string              | ISO 3166-1 alpha-3 code               | MUST            |
| `entitlements`                   | `entitlements`                   | array of strings    | Verified rights and benefits          | MUST            |
| `card_serial_number`             | `card_serial_number`             | string              | Scheme card number                    | MUST            |
| `subject_reference`              | `subject_reference`              | string              | Pairwise or scheme-specific reference | MUST            |
| `entitlement_level`              | `entitlement_level`              | string              | Scheme-defined level                  | MUST            |
| `entitlement_scope`              | `entitlement_scope`              | array of strings    | Geographic/domain scope               | MUST            |
| `support_categories`             | `support_categories`             | array of strings    | Operational support categories        | MUST            |
| `companion_count`                | `companion_count`                | integer             | Permitted companions                  | MUST            |
| `discount_percentage`            | `discount_percentage`            | integer             | Issuer-defined discount               | MUST            |
| `free_companion`                 | `free_companion`                 | boolean             | Free companion entitlement            | MUST            |
| `wheelchair_user`                | `wheelchair_user`                | boolean             | Wheelchair-service entitlement        | MUST            |
| `service_animal_entitlement`     | `service_animal_entitlement`     | boolean             | Assistance animal entitlement         | MUST            |
| `communication_preference`       | `communication_preference`       | string              | Operational communication preference  | MUST            |
| `emergency_assistance_reference` | `emergency_assistance_reference` | string              | Protected operational reference       | MUST            |
| `companion_entitlement`          | `companion_entitlement`          | boolean             | Explicit companion right              | MUST            |
| `additional_support_entitlement` | `additional_support_entitlement` | boolean             | Explicit support right                | MUST            |
| `support_validity_context`       | `support_validity_context`       | array of strings    | Valid service contexts                | MUST            |
| `cryptographically_bound_to`     | `cryptographically_bound_to`     | string              | PID type where bound                  | MUST NOT        |
| `schema_version`                 | `schema_version`                 | string              | Rulebook/schema version               | MUST NOT        |
| `trust_anchor_reference`         | `trust_anchor_reference`         | string              | Trust-anchor lookup                   | MUST NOT        |
| `privacy_notice`                 | `privacy_notice`                 | string              | Privacy information                   | MAY             |


All entitlement entries and nested objects SHALL be selectively disclosable at the
smallest practical semantic unit. A verifier SHALL be able to request
`companion_entitlement` without also receiving unrelated assistance categories.

### 3.2.4 Illustrative JWT claim set

```json
{
  "iss": "https://issuer.ipzs.example",
  "iat": 1784799000,
  "nbf": 1767225600,
  "exp": 1861833599,
  "vct": "urn:aptitude.eu:seditx:accessibility-disability-attestation:1",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 812,
      "uri": "https://status.example/atl/2026-07/42"
    }
  },
  "category": "eaa:eu:non-qualified",
  "recognised_status": true,
  "scheme_id": "eu_disability_card",
  "issuing_country": "ITA",
  "family_name": "Rossi",
  "given_name": "Giulia",
  "birthdate": "1994-05-18",
  "card_serial_number": "EDC-IT-2026-0048921",
  "entitlements": [
    "companion_entitlement",
    "priority_assistance",
    "reduced_fare"
  ],
  "companion_entitlement": true,
  "companion_count": 1,
  "free_companion": true,
  "additional_support_entitlement": true,
  "support_categories": [
    "mobility_assistance"
  ],
  "support_validity_context": [
    "rail",
    "ferry",
    "airport"
  ],
  "valid_from": "2026-01-01",
  "valid_until": "2028-12-31",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.aptitude.example/accessibility-issuers",
  "privacy_notice": "https://issuer.example/privacy"
}
```

The example includes more attributes than a normal presentation should disclose. An
actual service request SHALL select only the relevant claims.

### 3.2.5 Human-readable wallet representation

The Wallet Unit SHOULD display:

```text
Accessibility Attestation
Scheme: European Disability Card
Issuer: National Disability Card Authority
Recognised status: Valid
Available entitlements:
- Companion entitlement
- Additional support
- Reduced fare
Valid until: 31 December 2028
```

The Wallet Unit SHOULD inform the User that:

- only selected entitlements will be disclosed;
- diagnosis, clinical information and biometric data are not part of the credential;
- the verifier will use the disclosed claims for the stated service purpose;
- the User can refuse the presentation; and
- a manual or staff-assisted process should remain available.



## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 of this Rulebook does not define a W3C VCDM representation.

## 4 Attestation usage



### 4.1 Issuance prerequisites

Before issuance, the Attestation Provider SHALL:

1. verify that the applicant is recognised under the applicable scheme;
2. determine the valid accessibility-related entitlements;
3. verify identity to the level required by the scheme;
4. confirm the credential validity period;
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
- portrait, biometric template, biometric reference or any other biometric data; or
- other health information not needed to express a verified entitlement.



### 4.2 Device and holder binding

The attestation **SHOULD be device-bound** to a key controlled by the Wallet Unit.

Where the scheme requires strong anti-fraud protection, the credential SHOULD also be
bound to the holder through:

- PID-based issuance;
- a pairwise subject reference;
- holder-binding key material; or
- another approved scheme mechanism.

A Relying Party SHOULD request PID only where necessary to prevent misuse, satisfy
legal requirements or resolve ambiguity. It SHOULD NOT routinely request PID when the
accessibility entitlement alone is sufficient.

### 4.3 Presentation contexts

The attestation may be presented remotely or in proximity.

Relevant SEDIT-X contexts include:

#### Airport

A verifier MAY request only the entitlement needed to arrange assistance, such as:

- `priority_assistance`;
- `wheelchair_assistance`;
- `assisted_boarding`;
- `communication_assistance`; or
- `companion_entitlement`.



#### Ferry transport

A verifier or booking portal MAY request:

- `reduced_fare`;
- `free_companion_fare`;
- `companion_entitlement`;
- `assisted_boarding`; or
- another applicable ferry entitlement.



#### Hospitality

A hotel MAY request:

- `accessible_room`;
- `step_free_access`;
- `communication_assistance`; or
- another accommodation-related entitlement.



#### University or campus

A university MAY request:

- `campus_accessibility_support`;
- `communication_assistance`;
- `step_free_access`; or
- another institution-approved service entitlement.

The verifier SHALL NOT request the full `entitlements` set where one specific entitlement
is sufficient.

### 4.4 Relying Party obligations

The Relying Party or EUDIW Intermediary Service SHALL:

1. verify signature and cryptographic integrity;
2. verify issuer trust and authorisation;
3. verify validity and status;
4. verify holder binding where required;
5. verify that the disclosed entitlement is valid for the requested service context;
6. avoid requesting diagnosis or unrelated attributes;
7. avoid inferring disability type from the disclosed entitlement;
8. provide the service outcome or route the request to staff;
9. retain only the minimum operational result; and
10. provide a non-digital or staff-assisted alternative where appropriate.

A typical result SHOULD be limited to:

```json
{
  "credential_valid": true,
  "requested_entitlement": "companion_entitlement",
  "entitlement_valid": true,
  "companion_count": 1,
  "decision": "eligible",
  "correlation_id": "acc_01JZ..."
}
```



### 4.5 Identity attributes

The UC7 source-defined European Disability Card includes family name, given name,
birth date and card serial number. Under this Rulebook those attributes MAY be present
in the issued credential, but a verifier SHALL request them only where needed.

This attestation SHALL NOT include a portrait or any biometric data. Where visual
identity confirmation is required, the Relying Party SHALL use a separate approved
mechanism (for example a PID presentation or staff-assisted process), not this credential.

Examples:

- a ticket portal generally SHOULD request the entitlement and scheme validity, not name;
- a staff member verifying identity MAY request minimal name data or a subject-binding
reference, but SHALL NOT expect a portrait from this attestation;
- a ferry or airport verifier MAY request a subject-binding reference rather than full name;
- a remote service SHOULD avoid requesting identity attributes unless a justified
anti-fraud process requires them.



### 4.6 Special-category data

Accessibility and disability information may constitute sensitive or special-category
personal data under applicable law.

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

A transport or service discount MAY be applied based on a verified entitlement. Payment
authorisation and payment confirmation SHALL remain separate.

The Relying Party MAY retain:

- the applied fare basis;
- entitlement verification outcome;
- transaction reference; and
- minimum evidence needed for audit.

It SHOULD NOT retain the complete attestation.

### 4.8 Failure and fallback

The verifier SHALL return `not_verified` or `manual_review` when:

- signature, trust, validity or status verification fails;
- the requested entitlement is not present;
- the entitlement is not valid in the service context;
- holder binding cannot be established where required;
- the credential cannot be read; or
- the User declines presentation.

Failure to complete wallet verification SHALL NOT automatically establish that the User
has no disability or accessibility entitlement.

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
3. which entitlement claims the issuer may attest;
4. the geographic and service scope of that authority;
5. the applicable signing certificate or trust anchor; and
6. whether the issuer's authorisation remains valid.

For the APTITUDE pilot, issuer trust SHOULD be obtained through the trust framework and
trusted issuer list selected by WP2.

A verifier SHALL verify both:

- the cryptographic trust chain; and
- the issuer's authority to issue the claimed scheme and entitlement set.

The illustrative endpoints in this draft are not operational.

## 6 Revocation



### 6.1 Validity model

The attestation MAY be medium- or long-lived, depending on the issuing scheme.

The issuer SHALL specify `valid_from` and `valid_until`.

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

A change to one entitlement SHOULD, where technically feasible, invalidate or update
only the affected entitlement rather than unnecessarily exposing other information.

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
- SEDIT-X's inclusive-by-design approach; and
- the source-defined European Disability Card example in APTITUDE UC7.

The Rulebook enforces these properties:

1. the attestation expresses entitlement rather than diagnosis;
2. claims are selectively disclosable;
3. identity data is optional unless operationally needed;
4. the credential contains no portrait or other biometric data;
5. the credential may support transport, hospitality and academic services;
6. user consent is required for presentation;
7. verifiers request only context-relevant entitlements;
8. special-category data receives enhanced protection;
9. status and revocation are supported;
10. credential copies are not routinely retained; and
11. manual fallback remains available.

The following matters remain open:

- final credential type identifier;
- final approved entitlement vocabulary;
- mapping to the final European Disability Card data model;
- legal category by issuer and Member State;
- whether mdoc is required for proximity scenarios;
- final PID-binding policy;
- final trust-list service types and endpoints;
- final status-list mechanism;
- national and cross-border entitlement-recognition rules;
- accommodation-request workflows;
- handling of temporary entitlements; and
- retention rules for transport and hospitality operators.



## 8 References


| **Item Reference**                     | **Standard name/details**                                                                                                                                                                     |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [APTITUDE D4.1]                        | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026                                                                                                                    |
| [APTITUDE UC7]                         | Accessing Discounted Train Fares via EUDIW — European Disability Card example and candidate data model                                                                                        |
| [SEDIT-X Airport Working Paper]        | APTITUDE WP4, SEDIT-X at the Airport, Version 4.1, May 2026                                                                                                                                   |
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


