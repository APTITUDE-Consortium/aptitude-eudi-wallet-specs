# Attestation Rulebook for attestations of type Biometric QR Credential / Airport Journey Token

* Author(s):
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Christos Raptis, Fraport Greece
    * Angeliki Gkalimaridou, Fraport Greece
    * Isidoros Antonakos, Fraport Greece
    * Anastasios Symeonidis, Fraport Greece
* Reviewer(s):
    * Nicolas Portolleau, IN Groupe

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 22-07-2026 | Initial draft based on the SEDIT-X Smart Airport working paper and the APTITUDE Attestation Rulebook template. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The SEDIT-X source material defines the
> purpose, issuance prerequisites, airport usage, biometric-processing principles and principal
> verification obligations of the attestation. It does not yet define a final normative claim set,
> credential identifier, QR payload profile, trust-list endpoint or status-list endpoint.
> Values and requirements explicitly identified below as **pilot profile** or **proposed** require
> confirmation through the APTITUDE WP2/WP4 governance process before production use.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Biometric QR Credential / Airport Journey Token**, a
journey-specific, airport-issued Electronic Attestation of Attributes intended to support
secure and privacy-preserving passenger processing at airport operational touchpoints.

The attestation is issued after an airport-side issuer has verified:

1. a valid Person Identification Data (PID) credential or equivalent high-assurance identity evidence;
2. a valid Boarding Pass Credential; and
3. the binding between the passenger identity and the relevant flight journey.

Where the PID does not contain a usable portrait image, issuance may additionally involve
a dedicated identity-proofing, liveness and biometric-enrolment step.

The primary objective of the attestation is to provide a compact, cryptographically protected,
checkpoint-readable journey token that confirms that the passenger identity and flight
entitlement were previously verified and bound. In biometric-enhanced operation, the token
also carries or enables controlled derivation of a protected biometric reference used solely
for one-to-one (1:1) verification against a live facial capture.

The attestation is intended for use at airport touchpoints such as:

* self-service check-in and baggage drop;
* security screening;
* final boarding gates; and
* other explicitly authorised airport journey checkpoints.

The attestation SHALL NOT be used for one-to-many (1:N) biometric identification,
general-purpose identity verification, surveillance, or the creation of a central biometric
database.

The attestation does not replace the PID or the Boarding Pass Credential. It is a derived,
purpose-bound airport attestation representing a previously established identity-to-journey
binding.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 defines the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 defines the SD-JWT VC encoding and the pilot QR presentation representation.
* Chapter 4 specifies issuance, presentation and verification usage.
* Chapter 5 defines how trust anchors are obtained.
* Chapter 6 specifies validity and revocation requirements.
* Chapter 7 describes compliance with the EUDI Wallet framework and the SEDIT-X privacy model.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119].

In addition, *must* in lower case indicates an external constraint that is not established
by this Rulebook. The word *can* indicates a capability. Other words such as *will*,
*is* and *are* are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the EUDI Wallet Architecture
and Reference Framework.

For this Rulebook:

* **Airport Journey Token** and **Biometric QR Credential** refer to the same attestation type.
* **Biometric reference** means a portrait image or biometric template used exclusively as
  the reference side of a 1:1 biometric comparison.
* **Journey context** means the flight, passenger, validity period and authorised airport
  processing steps to which the attestation applies.
* **Checkpoint** means an airport operational touchpoint authorised to verify the attestation.
* **DCS** means an airline Departure Control System or equivalent operational system.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata of the Biometric QR Credential / Airport
Journey Token in an encoding-independent manner.

The credential is defined as a **non-qualified EAA** for the SEDIT-X pilot. Its category
value is therefore:

```text
eaa:eu:non-qualified
```

The credential SHALL be purpose-bound, journey-specific and short-lived. It SHALL contain
only the data needed to verify the airport journey context and, where applicable, perform
a one-off 1:1 biometric comparison.

Civil identity attributes such as full name, nationality, address or document number SHOULD
remain in the PID and SHOULD NOT be duplicated in this attestation unless an airport policy,
legal requirement or operational constraint makes a specific attribute indispensable.

### 2.1 Design principles

The following design principles apply:

1. **Derived attestation:** issuance depends on prior verification of PID and Boarding Pass Credential.
2. **Journey specificity:** one attestation relates to one passenger journey or a tightly defined set
   of flight segments.
3. **Data minimisation:** the attestation uses pseudonymous binding references instead of repeating
   civil identity attributes.
4. **Biometric limitation:** biometric information is used solely for 1:1 comparison.
5. **Holder control:** the credential is held under the passenger's control and access is protected
   by local user authentication.
6. **No central biometric database:** live captures and matching artefacts SHALL NOT be persistently
   stored by airport or airline systems.
7. **Operational verification:** cryptographic verification is combined with real-time or appropriately
   cached journey-eligibility checks against airport or airline systems.
8. **Fallback:** unsuccessful credential or biometric verification SHALL result in staff-assisted
   handling rather than automatic adverse decision-making beyond the immediate airport process.

### 2.2 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `journey_token_id` | Unique identifier of the airport journey token. It SHALL NOT be a civil identity number. | string | `ajt_01K0SKG7M3R9V6NQ2F4A` |
| `passenger_reference` | Pairwise or journey-specific pseudonymous reference linking the token to the verified passenger context. | string | `psg_7f2a91c4d3` |
| `boarding_pass_reference` | Reference to the Boarding Pass Credential or verified boarding entitlement used during issuance. | string | `bp_220726_A3123_018A` |
| `flight_number` | Marketing or operating flight number to which the token applies. | string | `A3123` |
| `operating_carrier` | IATA or ICAO code of the operating carrier. | string | `A3` |
| `departure_airport` | IATA airport code of the departure airport. | string | `SKG` |
| `arrival_airport` | IATA airport code of the destination airport. | string | `ATH` |
| `scheduled_departure` | Scheduled departure date and time in UTC. | date-time | `2026-07-22T16:30:00Z` |
| `identity_binding_verified` | Indicates that the issuer verified the binding between the passenger identity evidence and boarding entitlement. | boolean | `true` |
| `flight_entitlement_verified` | Indicates that the issuer verified a valid flight entitlement at issuance time. | boolean | `true` |
| `verification_time` | Time at which the identity and flight-entitlement binding was verified for issuance. | date-time | `2026-07-22T09:15:20Z` |
| `biometric_binding_type` | Type of biometric reference associated with the credential. | string enum | `protected_portrait_reference` |
| `biometric_reference` | Protected portrait, protected template, or cryptographic reference enabling the authorised 1:1 comparison. | binary or string | `urn:aptitude:bio-ref:9f5c...` |
| `biometric_use` | Permitted biometric processing mode. The value SHALL be `one_to_one_verification`. | string enum | `one_to_one_verification` |
| `authorised_checkpoints` | Airport processing steps at which the token may be used. | array of strings | `["bag_drop","security","boarding_gate"]` |

Permitted values for `biometric_binding_type` are:

* `protected_portrait`;
* `protected_portrait_reference`;
* `protected_template`; or
* `protected_template_reference`.

An implementation SHALL select one binding model in its deployment profile. A relying party
SHALL reject a credential containing an unsupported binding type.

Permitted values for entries in `authorised_checkpoints` are:

* `check_in`;
* `bag_drop`;
* `security`;
* `lounge`;
* `boarding_gate`; and
* another value defined by an approved airport deployment profile.

### 2.3 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `journey_reference` | Issuer-generated reference to the complete airport journey context. | string | `jrn_SKG_A3123_20260722` |
| `booking_reference_hash` | Salted or keyed hash of the booking/PNR reference, where operational correlation is required without disclosure of the PNR. | string | `sha256:68e3...` |
| `airline_passenger_reference` | Airline-specific pseudonymous identifier created when the PID was verified. | string | `air_psg_88271` |
| `seat_number` | Assigned passenger seat, where needed by a checkpoint. | string | `18A` |
| `boarding_group` | Boarding group or zone. | string | `3` |
| `boarding_gate` | Assigned gate known at issuance or update time. | string | `B12` |
| `boarding_window_start` | Start of the boarding-validity window. | date-time | `2026-07-22T15:45:00Z` |
| `boarding_window_end` | End of the boarding-validity window. | date-time | `2026-07-22T16:20:00Z` |
| `journey_status` | Last issuer-known journey status. | string enum | `ready_to_travel` |
| `biometric_algorithm` | Identifier of the biometric representation or matching profile. | string | `ISO_39794_5_PROFILE_TBD` |
| `biometric_quality` | Issuer-generated quality result for the biometric reference, without exposing matching thresholds. | string enum | `sufficient` |
| `enrolment_method` | Method used to obtain the biometric reference. | string enum | `pid_portrait` |
| `issuing_airport` | IATA code of the airport-side issuer context. | string | `SKG` |
| `display_name` | Human-readable wallet display name. | string | `SKG Airport Journey Token` |

Permitted values for `journey_status` SHOULD include:

* `issued`;
* `ready_to_travel`;
* `checked_in`;
* `security_cleared`;
* `boarding_open`;
* `boarded`;
* `cancelled`; and
* `expired`.

Permitted values for `enrolment_method` are:

* `pid_portrait`;
* `identity_proofing_and_liveness`; or
* `approved_external_photo_identity`.

### 2.4 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `liveness_verified` | Indicates successful liveness verification. Mandatory when `enrolment_method` is `identity_proofing_and_liveness`. | boolean | `true` |
| `identity_proofing_reference` | Pseudonymous reference to the completed identity-proofing session. Mandatory when a dedicated proofing process was used. | string | `idv_01K0S8...` |
| `document_type` | Type of verified identity document. MAY be included only when required by the deployment profile. | string | `national_id` |
| `document_issuing_country` | Country that issued the identity evidence. MAY be included only where necessary for journey eligibility. | string | `GRC` |
| `additional_flight_segments` | Additional segments covered by the same journey token. Present only when explicitly permitted by the deployment profile. | array of objects | `[{"flight_number":"A3982","departure_airport":"ATH","arrival_airport":"JTR"}]` |
| `cryptographically_bound_to` | Attestation type to which this credential is cryptographically bound. Mandatory under this Rulebook. | string | `urn:eu.europa.ec.eudi:pid:1` |

The credential SHALL be cryptographically bound to the Wallet Unit and to the verified
journey context. The `cryptographically_bound_to` value SHALL identify the PID type used
during issuance:

```text
urn:eu.europa.ec.eudi:pid:1
```

The binding to the Boarding Pass Credential SHALL be expressed using
`boarding_pass_reference` and the issuer's issuance evidence. A future approved Boarding Pass
Rulebook MAY define an additional formal cross-credential binding mechanism.

### 2.5 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the airport-side Attestation Provider. | string or URI | `https://issuer.skg.example` |
| `credential_type` | Encoding-independent credential type identifier. | string | `urn:aptitude.eu:seditx:airport-journey-token:1` |
| `issued_at` | Time of credential issuance. | date-time | `2026-07-22T09:16:00Z` |
| `valid_from` | Start of credential validity. | date-time | `2026-07-22T09:16:00Z` |
| `valid_until` | End of credential validity. | date-time | `2026-07-22T18:30:00Z` |
| `schema_version` | Version of the credential schema. | string | `0.1` |
| `holder_binding` | Indicates that the credential is bound to a key controlled by the Wallet Unit. | string | `jwk_thumbprint` |
| `status_reference` | Reference used for status or revocation checking. | URI or structured value | `https://status.skg.example/atl/2026-07/42#9182` |
| `trust_anchor_reference` | Location from which the applicable issuer trust information can be obtained. | URI | `https://trust.aptitude.example/airport-issuers` |

The identifiers and URLs above are illustrative and SHALL be replaced by values approved
through APTITUDE governance.

### 2.6 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_name` | Human-readable name displayed by the Wallet Unit. | string | `Biometric QR Credential` |
| `credential_description` | Human-readable explanation of the credential purpose. | string | `Airport journey token for SKG flight A3123` |
| `terms_of_use` | Reference to the applicable passenger terms and privacy information. | URI | `https://airport.example/eudi/terms` |
| `privacy_notice` | Reference to the biometric-processing privacy notice. | URI | `https://airport.example/eudi/biometrics/privacy` |
| `issuer_policy` | Reference to the issuer policy governing issuance and verification. | URI | `https://airport.example/eudi/issuer-policy` |
| `display_locale` | Preferred language for wallet display. | string | `en` |

### 2.7 Conditional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `status_list_index` | Entry index in an applicable Attestation Status List. Mandatory when a list-based status mechanism is used. | integer | `9182` |
| `status_list_uri` | URI of the applicable Attestation Status List. Mandatory when list-based status is used. | URI | `https://status.skg.example/atl/2026-07/42` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI | `https://status.skg.example/arl/2026-07` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 of this Rulebook does not define an ISO/IEC 18013-5 mdoc representation for
the Biometric QR Credential / Airport Journey Token.

The operational BioQRCode path is based on optical presentation of a protected QR
representation. The parallel SEDIT-X proximity path uses a direct ISO/IEC 18013-5-style
presentation of the underlying PID and Boarding Pass Credential and is therefore outside
the scope of this attestation type.

A future version MAY define an mdoc representation if offline NFC presentation of this
derived airport token becomes an approved requirement. Until such a profile is defined,
an issuer SHALL NOT advertise an mdoc document type for this attestation.

## 3.2 SD-JWT VC-based encoding

### 3.2.1 Verifiable Credential Type

The proposed Verifiable Credential Type is:

```text
urn:aptitude.eu:seditx:airport-journey-token:1
```

This value is a pilot identifier and requires confirmation by the APTITUDE schema-governance
process before production use.

The attestation SHALL comply with the SD-JWT VC profile selected by APTITUDE WP2 and
the applicable HAIP profile.

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

### 3.2.3 Private claims specific to this attestation

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `category` | `category` | string | Defined according to ETSI EAA category conventions | MUST NOT |
| `journey_token_id` | `journey_token_id` | string | Token identifier | MUST NOT |
| `passenger_reference` | `passenger_reference` | string | Pseudonymous passenger binding | MUST |
| `boarding_pass_reference` | `boarding_pass_reference` | string | Boarding Pass Credential reference | MUST |
| `journey_reference` | `journey_reference` | string | Optional journey correlation reference | MUST |
| `booking_reference_hash` | `booking_reference_hash` | string | Optional protected PNR correlation | MUST |
| `airline_passenger_reference` | `airline_passenger_reference` | string | Optional airline pseudonym | MUST |
| `flight_number` | `flight_number` | string | Flight number | MUST |
| `operating_carrier` | `operating_carrier` | string | Carrier code | MUST |
| `departure_airport` | `departure_airport` | string | IATA airport code | MUST |
| `arrival_airport` | `arrival_airport` | string | IATA airport code | MUST |
| `scheduled_departure` | `scheduled_departure` | string | RFC 3339 timestamp | MUST |
| `seat_number` | `seat_number` | string | Optional assigned seat | MUST |
| `boarding_group` | `boarding_group` | string | Optional boarding group | MUST |
| `boarding_gate` | `boarding_gate` | string | Optional gate | MUST |
| `boarding_window_start` | `boarding_window_start` | string | RFC 3339 timestamp | MUST |
| `boarding_window_end` | `boarding_window_end` | string | RFC 3339 timestamp | MUST |
| `journey_status` | `journey_status` | string | Issuer-known operational state | MUST |
| `identity_binding_verified` | `identity_binding_verified` | boolean | Prior identity binding result | MUST NOT |
| `flight_entitlement_verified` | `flight_entitlement_verified` | boolean | Prior entitlement verification result | MUST NOT |
| `verification_time` | `verification_time` | string | RFC 3339 timestamp | MUST NOT |
| `biometric_binding_type` | `biometric_binding_type` | string | Protected biometric representation type | MUST NOT |
| `biometric_reference` | `biometric_reference` | string or object | Protected reference or protected biometric material | MUST |
| `biometric_use` | `biometric_use` | string | Fixed to `one_to_one_verification` | MUST NOT |
| `biometric_algorithm` | `biometric_algorithm` | string | Optional representation/profile identifier | MUST NOT |
| `biometric_quality` | `biometric_quality` | string | Optional quality classification | MUST |
| `enrolment_method` | `enrolment_method` | string | Biometric enrolment method | MUST |
| `liveness_verified` | `liveness_verified` | boolean | Conditional liveness result | MUST NOT |
| `identity_proofing_reference` | `identity_proofing_reference` | string | Conditional proofing session reference | MUST |
| `authorised_checkpoints` | `authorised_checkpoints` | array of strings | Permitted use contexts | MUST |
| `issuing_airport` | `issuing_airport` | string | Airport code | MUST |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | PID type to which this credential is bound | MUST NOT |
| `schema_version` | `schema_version` | string | Rulebook/schema version | MUST NOT |
| `trust_anchor_reference` | `trust_anchor_reference` | string | Trust-anchor lookup location | MUST NOT |
| `privacy_notice` | `privacy_notice` | string | Privacy information | MAY |

`biometric_reference` is highly sensitive. It SHALL be selectively disclosable as a single
claim or protected object, but an Attestation Provider SHALL structure the credential so that
a verifier cannot independently disclose nested elements that are not required for the
authorised comparison.

### 3.2.4 Illustrative JWT claim set

```json
{
  "iss": "https://issuer.skg.example",
  "iat": 1784702160,
  "nbf": 1784702160,
  "exp": 1784735400,
  "vct": "urn:aptitude.eu:seditx:airport-journey-token:1",
  "cnf": {
    "jkt": "g3JfQ2...wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 9182,
      "uri": "https://status.skg.example/atl/2026-07/42"
    }
  },
  "category": "eaa:eu:non-qualified",
  "journey_token_id": "ajt_01K0SKG7M3R9V6NQ2F4A",
  "passenger_reference": "psg_7f2a91c4d3",
  "boarding_pass_reference": "bp_220726_A3123_018A",
  "journey_reference": "jrn_SKG_A3123_20260722",
  "flight_number": "A3123",
  "operating_carrier": "A3",
  "departure_airport": "SKG",
  "arrival_airport": "ATH",
  "scheduled_departure": "2026-07-22T16:30:00Z",
  "boarding_gate": "B12",
  "boarding_window_start": "2026-07-22T15:45:00Z",
  "boarding_window_end": "2026-07-22T16:20:00Z",
  "identity_binding_verified": true,
  "flight_entitlement_verified": true,
  "verification_time": "2026-07-22T09:15:20Z",
  "biometric_binding_type": "protected_portrait_reference",
  "biometric_reference": {
    "ref": "urn:aptitude:bio-ref:9f5c14584f31",
    "protection_profile": "APTITUDE-BIOQR-01"
  },
  "biometric_use": "one_to_one_verification",
  "enrolment_method": "pid_portrait",
  "authorised_checkpoints": [
    "bag_drop",
    "security",
    "boarding_gate"
  ],
  "issuing_airport": "SKG",
  "cryptographically_bound_to": "urn:eu.europa.ec.eudi:pid:1",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.aptitude.example/airport-issuers",
  "privacy_notice": "https://airport.example/eudi/biometrics/privacy"
}
```

An actual compact SD-JWT serialisation and disclosure set SHALL be generated from the
selected APTITUDE SD-JWT VC implementation profile. This draft does not provide a
fabricated base64-encoded token because issuer keys, salts, status infrastructure and the
final disclosure policy have not yet been defined.

### 3.2.5 Human-readable wallet representation

A Wallet Unit SHOULD display at least:

```text
SKG Airport Journey Token
Flight: A3123
Route: Thessaloniki (SKG) to Athens (ATH)
Departure: 22 July 2026, 16:30 UTC
Valid for: Bag drop, security and boarding gate
Biometric use: One-to-one verification only
Issuer: SKG Airport pilot issuer
Valid until: 22 July 2026, 18:30 UTC
```

The Wallet Unit SHOULD prominently inform the User that:

* the credential links verified identity evidence to a specific flight;
* the biometric reference will be used only for a one-off 1:1 comparison;
* airport systems must not retain the live image or biometric comparison artefacts;
* presentation requires local User authentication; and
* the User can refuse presentation and use the staff-assisted process.

### 3.2.6 Protected QR presentation representation

The QR code displayed by the Wallet Unit is a presentation representation of the
Biometric QR Credential. It is not a separate legal attestation type.

The final binary/QR encoding profile is not specified in the current SEDIT-X source
material. The APTITUDE pilot profile SHALL define:

* whether the QR carries a self-contained signed object or a short-lived protected reference;
* maximum payload size and QR error-correction level;
* cryptographic protection and reader-validation rules;
* anti-replay and freshness controls;
* biometric-reference protection;
* behaviour when a checkpoint is temporarily offline; and
* compatibility with existing airport optical scanners.

At minimum, the protected QR representation SHALL:

1. be cryptographically bound to the issued credential or to a fresh wallet-generated
   presentation of that credential;
2. identify the journey token and issuer;
3. be time-limited or dynamically refreshed;
4. prevent undetected modification;
5. prevent a static screenshot from being reusable outside the authorised validity and
   journey context;
6. expose no raw civil identity attributes unless expressly required;
7. expose the biometric reference only in protected form; and
8. be verifiable by the EUDIW Intermediary Service or an authorised airport verifier.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 of this Rulebook does not define a W3C Verifiable Credentials Data Model
representation.

A future version MAY add such an encoding only if it is permitted by the applicable EUDI
Wallet framework and accompanied by an approved selective-disclosure and presentation
profile.

## 4 Attestation usage

### 4.1 Issuance prerequisites

Before issuing the attestation, the Attestation Provider SHALL:

1. obtain a User-authorised presentation of a valid PID or equivalent approved identity credential;
2. obtain a valid Boarding Pass Credential;
3. verify issuer signatures, trust anchors, validity and status of both credentials;
4. confirm that the identity subject and boarding-pass subject or pseudonymous binding refer
   to the same passenger;
5. confirm the passenger's current entitlement for the stated flight;
6. obtain or derive the protected biometric reference according to one of the approved methods;
7. display the credential type, issuer, purpose, intended airport use, attributes and biometric
   processing notice to the User; and
8. obtain explicit User consent before issuance.

Where the PID does not contain a usable portrait image, issuance SHALL include:

* PID verification;
* liveness verification;
* binding of the live enrolment subject to the verified identity; and
* confirmation of a valid Boarding Pass Credential.

### 4.2 Device and holder binding

The attestation **SHALL be device-bound** to a key controlled by the Wallet Unit.

The Wallet Unit SHALL require local User authentication, such as biometric authentication
or PIN, before displaying or presenting the protected QR representation.

The attestation SHALL be cryptographically bound to the PID type indicated by
`cryptographically_bound_to`. It SHALL also be bound to the Boarding Pass Credential
through the journey-specific `boarding_pass_reference` and issuer evidence.

The credential SHALL NOT be transferable between Wallet Units without re-issuance.

### 4.3 Presentation contexts

The primary presentation mode is visual presentation of a protected QR representation from
the Wallet Unit to an authorised optical reader.

The attestation MAY be used at:

* baggage-drop equipment;
* airport security checkpoints;
* boarding gates; and
* another checkpoint explicitly included in `authorised_checkpoints`.

A verifier SHALL NOT accept the token for a checkpoint type that is not authorised by the
credential.

The User SHALL unlock the credential through local authentication before presentation.
The Wallet Unit SHALL provide a clear indication that the token is being displayed for an
airport operational decision.

### 4.4 Relying Party obligations

A Relying Party receiving the Biometric QR Credential does not normally need to request
the PID again because the token represents a previously verified identity-to-flight binding.
However:

* the Relying Party MAY request the PID through the parallel proximity flow where required
  by law, airport policy or fallback procedures;
* the Relying Party SHALL NOT infer that the token is a general-purpose identity credential;
* the Relying Party SHALL verify the token only for the stated journey and checkpoint context.

The Relying Party or EUDIW Intermediary Service SHALL:

1. verify the credential signature and cryptographic integrity;
2. validate the Attestation Provider against the applicable trust framework;
3. verify validity times and credential status;
4. verify holder/device binding and presentation freshness;
5. verify that the token corresponds to the current airport, flight, date and checkpoint;
6. consult the relevant airline/airport operational system to confirm current eligibility;
7. enforce `authorised_checkpoints`;
8. ensure that a cancelled, rebooked, completed or otherwise invalid journey token is rejected;
9. where biometric-enhanced mode is used, perform only 1:1 comparison against the protected
   reference associated with the token;
10. discard live captures, derived templates and reference data from processing memory
    immediately after the matching decision; and
11. return only the minimum operational outcome needed by the touchpoint.

The normal operational result SHOULD be limited to:

```json
{
  "journey_token_valid": true,
  "flight_eligible": true,
  "biometric_match": "pass",
  "decision": "allow",
  "correlation_id": "evt_01K0..."
}
```

The relying party SHALL NOT store a copy of the credential, portrait, biometric template
or QR payload merely because presentation occurred.

### 4.5 Biometric verification

Biometric-enhanced usage SHALL follow these requirements:

* comparison SHALL be 1:1 and SHALL NOT be 1:N;
* the live capture SHALL be compared only against the reference associated with the
  presented token;
* no central gallery of passenger biometric templates SHALL be created;
* biometric data SHALL be processed ephemerally;
* matching thresholds and quality policies SHALL be controlled by the authorised deployment;
* a low-confidence or failed result SHALL trigger staff-assisted handling;
* the biometric result SHALL NOT be reused for unrelated purposes; and
* operational logging SHALL exclude facial images and biometric templates.

### 4.6 Freshness, replay prevention and QR display

The final QR freshness profile remains to be defined. The implementation SHALL nevertheless
ensure that:

* a copied screenshot cannot remain valid indefinitely;
* the presentation is bound to a short validity window, verifier challenge, dynamic display,
  or equivalent anti-replay mechanism;
* the verifier detects expired or previously consumed single-use presentations where the
  deployment uses one-time semantics; and
* acceptance of a fresh QR does not replace the current DCS eligibility check.

### 4.7 Transactional data

This attestation is not a payment attestation and does not carry payment transaction data.

Airport payment operations, such as excess-baggage payment, SHALL use a separate payment
authorisation flow and any resulting payment confirmation or e-receipt credential. A payment
outcome MAY update the operational journey state but SHALL NOT modify the biometric purpose
of this attestation.

### 4.8 Failure and fallback

The automated flow SHALL stop and route the passenger to staff-assisted processing when:

* credential integrity, trust, status or validity verification fails;
* the QR presentation is stale, replayed or unreadable;
* the token does not match the current flight or checkpoint;
* the airline operational system does not confirm eligibility;
* biometric matching fails or produces insufficient confidence;
* the biometric reference is unavailable or unsupported; or
* legal or operational policy requires manual verification.

## 5 Trust anchors

The Biometric QR Credential is a non-qualified EAA issued by an airport-side Attestation
Provider or an authorised provider acting for the airport.

For the APTITUDE pilot, the Relying Party SHALL obtain issuer trust information through the
APTITUDE trust framework and the applicable trusted issuer list established by WP2.

The `trust_anchor_reference` metadata SHALL identify the machine-readable location from
which the applicable issuer trust information can be obtained.

The production trust model SHALL define:

1. the entity authorised to register airport journey-token issuers;
2. the trusted-list or List of Trusted Entities structure;
3. the service type used to identify authorised Airport Journey Token providers;
4. certificate profiles and signing-key requirements;
5. key rollover and compromise handling;
6. issuer authorisation scope, including authorised airports and credential types; and
7. Wallet Unit and verifier behaviour when trust information cannot be retrieved.

A verifier SHALL verify both:

* that the signature chain terminates in an accepted trust anchor; and
* that the issuer is authorised to issue
  `urn:aptitude.eu:seditx:airport-journey-token:1`.

The illustrative domain names in this Rulebook are not operational trust endpoints.

## 6 Revocation

### 6.1 Validity model

The attestation SHALL be short-lived and journey-specific. Its validity SHALL NOT extend
beyond the operational journey window required for the covered flight.

The issuer SHOULD set `valid_until` no later than the earliest of:

* completion of boarding plus an operational grace period;
* cancellation of the flight;
* cancellation or replacement of the boarding pass;
* rebooking of the passenger to a different flight;
* end of the airport-defined journey-token validity period; or
* expiry or invalidation of required underlying evidence.

Short validity alone does not remove the need for real-time journey-context validation.

### 6.2 Revocation and status

The attestation SHALL be status-checkable.

The target APTITUDE implementation SHOULD use the status-list mechanism selected by
APTITUDE WP2 and aligned with the applicable EUDI Wallet Technical Specification.

The issuer SHALL invalidate the attestation when, for example:

* the associated boarding pass is cancelled or replaced;
* the passenger is rebooked;
* the flight is cancelled and the token is no longer applicable;
* the Wallet Unit or credential is reported compromised;
* the identity-to-journey binding is found to be incorrect;
* the User revokes consent where the applicable service model supports it; or
* the Attestation Provider detects fraudulent issuance or use.

A Relying Party SHALL check both credential status and current journey eligibility.

### 6.3 Status-list location

The final production URL for the applicable Attestation Status List or Attestation
Revocation List has not yet been defined.

The deployment Rulebook or issuer policy SHALL publish at least the domain from which
the applicable status data can be retrieved. The individual credential SHALL contain the
specific status reference required by the selected mechanism.

Illustrative pilot value:

```text
https://status.skg.example/
```

This value SHALL NOT be treated as an operational endpoint.

## 7 Compliance

This Rulebook is designed to align with:

* Regulation (EU) 2024/1183 establishing the European Digital Identity Framework;
* the EUDI Wallet Architecture and Reference Framework;
* the Attestation Rulebook requirements in Topic 12 of ARF Annex 2;
* the EUDI Wallet issuance and presentation profiles selected by APTITUDE;
* the SD-JWT VC and HAIP profiles selected by APTITUDE WP2;
* the SEDIT-X Smart Airport 1:1 biometric-verification model;
* GDPR principles of purpose limitation, data minimisation, storage limitation,
  integrity, confidentiality and data protection by design and by default; and
* the EDPB position favouring passenger-controlled biometric references and avoiding
  central 1:N identification architectures in airport passenger-flow use cases.

The Rulebook enforces the following compliance properties:

1. the attestation is a non-qualified, purpose-bound EAA;
2. issuance requires explicit User participation and consent;
3. presentation requires local User authentication;
4. the credential is bound to the Wallet Unit;
5. only authorised checkpoint uses are permitted;
6. biometric processing is limited to 1:1 verification;
7. live and transient biometric data are deleted immediately after comparison;
8. cryptographic validation is combined with current operational eligibility;
9. status and revocation checks are required;
10. data disclosed and retained by airport systems are minimised; and
11. a manual fallback is available when automated verification cannot safely complete.

The following matters remain open and SHALL be resolved before a final compliant version
is published:

* final credential type identifier;
* final claim catalogue and controlled vocabularies;
* exact protected QR encoding and freshness profile;
* biometric-reference protection profile;
* final trust-list service type and endpoint;
* final status-list or revocation-list mechanism and endpoint;
* approved Boarding Pass Credential binding mechanism;
* permitted offline operation and cache policy; and
* final data-controller and processor responsibilities for each airport touchpoint.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X Airport Working Paper] | APTITUDE WP4, SEDIT-X at the Airport, “Smart airport: Using the EUDI Wallet for biometric boarding without pre-enrollment (biometric 1:1 verification)”, Version 4.1, May 2026 |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence application |
| [ISO/IEC 19794-5] | Information technology — Biometric data interchange formats — Part 5: Face image data |
| [ISO/IEC 39794-5] | Information technology — Extensible biometric data interchange formats — Part 5: Face image data |
| [OIDC] | OpenID Connect Core 1.0 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 3339] | Date and Time on the Internet: Timestamps |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [Topic 20] | ARF Annex 2, Topic 20 — Strong User authentication for electronic payments |
| [EDPB Opinion 11/2024] | Opinion 11/2024 on the use of facial recognition to streamline airport passengers' flow |
| [ETSI TS 119 472-1] | Electronic Signatures and Trust Infrastructures; Electronic Attestation of Attributes; Part 1: Building blocks and general requirements |
