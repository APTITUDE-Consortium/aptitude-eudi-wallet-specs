# Attestation Rulebook for attestations of type Vehicle Ferry Boarding Credential

* Author(s):
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X Ferry Transport working paper and the APTITUDE Attestation Rulebook template. |
| 0.2 | 24-07-2026 | Simplified structure aligned with the passenger Ferry Boarding Pass model. |
| 0.3 | 24-07-2026 | Aligned claim model with the Vehicle Ferry Boarding Credential JSON Schema. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the Vehicle Ferry Boarding Credential for the APTITUDE /
> SEDIT-X ferry pilot. The SD-JWT claim model below is aligned with the Vehicle
> Boarding Credential JSON Schema (`credentialType`: `VehicleBoardingCredential`).

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Vehicle Ferry Boarding Credential** for use in the
European Digital Identity Wallet ecosystem.

The credential expresses the real-world fact that a specific vehicle is entitled to
board a specific ferry journey at a given departure date and time.

The attestation is intended to be issued by an authentic source, such as a ferry
operator or an authorised ticketing system acting on behalf of the ferry operator. The
Holder is typically the passenger who booked the vehicle. Relying Parties include ferry
operators, port boarding gates, vehicle-lane terminals, authorised boarding control
staff, and other authorised systems that need to verify vehicle boarding entitlement.

In practical terms, the attestation enables a passenger to present proof that a named
vehicle may embark on a specific sailing. It can reduce reliance on paper vehicle tickets
and can reduce the need for real-time backend lookups during boarding, provided that the
Relying Party can verify the issuer, the signature, the validity period, the journey
details, and the vehicle attributes needed for embarkation.

The attestation does not replace:

* the passenger **Ferry Boarding Pass**, which represents the passenger's boarding right;
* the **mVRC**, which provides authoritative vehicle-registration attributes;
* the **PID** credential; or
* a payment confirmation or eReceipt.

Where vehicle-to-ticket binding must be checked at the port, the Vehicle Ferry Boarding
Credential SHOULD be presented together with the minimum required mVRC attributes and,
where required by policy, the passenger Ferry Boarding Pass and PID.

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
| Vehicle Ferry Boarding Credential | A Verifiable Credential representing a vehicle's entitlement to board a specific ferry journey. |
| Ferry operator | The organisation operating the ferry journey or acting as the authentic source for the boarding entitlement. |
| Authorised ticketing system | A system authorised by the ferry operator to issue or manage boarding passes. |
| mVRC | Mobile Vehicle Registration Credential providing authoritative vehicle-registration attributes. |
| Boarding gate / vehicle lane | A physical or digital checkpoint where vehicle boarding entitlement is verified. |
| Journey | A specific ferry trip between a departure port and an arrival port at a scheduled date and time. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a Vehicle Ferry Boarding Credential
may contain. The attributes are defined in an encoding-independent manner. Each
attribute is classified as mandatory, optional, or conditional.

The credential is journey-specific and time-bound. It contains only the information
necessary to verify that a specific vehicle is entitled to board a specific ferry
service. The claim model is nested under `departure`, `arrival`, `vehicle` and
`ticket` objects as defined by the Vehicle Boarding Credential schema.

### 2.1 Introduction

The Vehicle Ferry Boarding Credential is defined as a non-qualified Electronic
Attestation of Attributes unless a future version of this Rulebook explicitly defines a
qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value
`non-qualified-EAA`.

The attestation model consists of the following logical groups:

* credential type;
* departure port-call details;
* arrival details;
* vehicle identification and category data;
* ticket identifiers;
* optional vessel and reservation information;
* credential metadata.

The attestation is bound to a single vehicle and a single ferry journey. It SHALL NOT
be treated as a reusable credential after the scheduled departure time.

The mVRC remains the authoritative source of vehicle-registration attributes. This
credential SHOULD NOT duplicate the complete mVRC.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `credentialType` | Schema const | Credential type discriminator. SHALL be `VehicleBoardingCredential`. | string | `VehicleBoardingCredential` |
| `departure.date` | ISO 8601 date | Scheduled departure date. | date | `2026-06-15` |
| `departure.time` | Local time `HH:MM` or `HH:MM:SS` | Scheduled departure time at the departure port. | string | `07:30` |
| `departure.port` | Port identifier | Departure port. | string | `GRRFN` |
| `arrival.date` | ISO 8601 date | Scheduled arrival date. | date | `2026-06-15` |
| `arrival.time` | Local time `HH:MM` or `HH:MM:SS` | Scheduled arrival time at the arrival port. | string | `12:45` |
| `arrival.port` | Port identifier | Arrival port. | string | `GRMLO` |
| `vehicle.vehicleType` | Ferry tariff / vehicle category | Human-readable ferry-relevant vehicle type. | string | `Passenger Car` |
| `vehicle.vehicleTypeCode` | Ferry tariff code | Operator or tariff code for the vehicle type. | string | `PC` |
| `ticket.ticketLet` | N/A | Ticket letter, class code, or other operator-specific classification. | string | `V` |
| `ticket.ticketNumber` | N/A | Ferry vehicle-ticket number. | string | `000123456` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vesselDescription` | N/A | Description or name of the ferry vessel. | string | `Fast Ferries Andros` |
| `reservationNumber` | N/A | Booking or reservation number associated with the vehicle ticket. | string | `RES-2026-000991` |
| `departure.gate` | N/A | Departure gate, lane or boarding area. | string | `RFN-LANE-02` |
| `vehicle.plateNumber` | Vehicle registration mark | Registration / plate number of the vehicle entitled to board. | string | `NIK-1234` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vehicle.plateNumber` | Vehicle registration mark | SHOULD be present where the boarding process requires clear-text plate matching against the mVRC or physical vehicle. MAY be omitted where vehicle binding is established by other means under ferry policy. | string | `NIK-1234` |
| `departure.gate` | N/A | SHOULD be present where gate or lane assignment is known at issuance and needed for embarkation guidance. | string | `RFN-LANE-02` |
| `reservationNumber` | N/A | SHOULD be present where the ferry system uses a reservation number distinct from `ticket.ticketNumber`. | string | `RES-2026-000991` |

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `VehicleBoardingCredential` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-ferry.gr` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1780315200` |
| `exp` | JWT | Expiration time of the credential. For this attestation it SHALL NOT be later than the scheduled departure time unless operational rules explicitly require a short post-departure grace period. | integer | `1781508600` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks, where revocation is supported. | object | `{ "status_list": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1780315200` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:2aacf8dc-3f0b-4b30-987d-5eacb9dba222` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/ferry/operators/fast-ferries` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:vehicle-registration:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `status` | SD-JWT VC status mechanism, where used | SHALL be present if the issuer supports revocation or suspension for the boarding credential. MAY be omitted where the attestation is short-lived and expires at or before departure time. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the vehicle boarding credential is required to be presented together with an mVRC or another accepted vehicle-registration attestation. | string | `urn:eudi:vehicle-registration:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `credentialType` | `VehicleBoardingCredential` | Credential type discriminator. | Vehicle Boarding Credential schema | Const value; additional values SHALL NOT be used. |
| `departure.date` / `arrival.date` | ISO 8601 date | Scheduled date. | ISO 8601 | Date-only format `YYYY-MM-DD` SHALL be used. |
| `departure.time` / `arrival.time` | `HH:MM` or `HH:MM:SS` | Scheduled local time. | Schema time pattern | Time-zone handling SHALL be clear to the verifier as local port time. |
| `departure.port` / `arrival.port` | Valid port identifiers | Identifies the port. | UN/LOCODE recommended | Operator-specific port identifiers MAY be used during pilots. |
| `vehicle.vehicleTypeCode` | Issuer-defined tariff codes | Identifies the fare/loading category code. | Ferry operator tariff vocabulary | Examples include `PC`, `MC`, `VAN`, `BUS`. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `VBP-IR-01` | `arrival.date` SHALL NOT precede `departure.date`. | Prevents temporally inconsistent journey information. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject inconsistent journey data. Verifier SHALL reject the attestation for boarding if this rule fails. |
| `VBP-IR-02` | The credential SHALL be bound to a single journey and a single vehicle. | Prevents reuse across different services, vessels, dates, or vehicles. | Issuer business rules and verifier business validation. | Verifier SHALL reject the attestation if it cannot determine the specific journey or vehicle. |
| `VBP-IR-03` | The attestation SHALL NOT be reusable after the scheduled departure time. | Boarding entitlement is time-bound and journey-specific. | Issuer validity period and verifier freshness checks. | Verifier SHALL reject the attestation after expiry, unless a locally defined operational grace period applies. |
| `VBP-IR-04` | `credentialType` SHALL equal `VehicleBoardingCredential`. | Ensures type-safe interpretation of the claim set. | Schema validation and verifier business validation. | Verifier SHALL reject credentials with an unexpected `credentialType`. |
| `VBP-IR-05` | `ticket.ticketLet` and `ticket.ticketNumber` SHALL be non-empty. | Ensures a usable ticket identifier for embarkation and audit. | Schema validation and issuer business rules. | Issuer SHALL reject empty ticket identifiers. Verifier SHALL reject incomplete ticket data. |
| `VBP-IR-06` | Where vehicle matching is required, `vehicle.plateNumber` SHOULD be compared with the mVRC and the physical vehicle. | Ensures that the vehicle presented for embarkation is the vehicle entitled to board. | Relying Party business validation. | Verifier SHOULD reject the boarding transaction where required vehicle matching fails. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the
Vehicle Ferry Boarding Credential.

The credential defined in this Rulebook is specified for SD-JWT VC-based issuance and
presentation. If a future version defines an ISO/IEC 18013-5-compliant mdoc
representation, that version SHALL define a unique document type, namespaces, attribute
identifiers, CBOR encoding rules, and illustrative mdoc examples.

## 3.2 SD-JWT VC-based encoding

The Vehicle Ferry Boarding Credential SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
VehicleBoardingCredential
```

This value SHALL match the claim `credentialType`.

The credential claims defined in this section SHALL follow SD-JWT VC and HAIP
conventions where applicable. Claim names are either IANA-registered JWT claims,
public names, or private names specific to this attestation type.

For all claims, this Rulebook specifies whether an Attestation Provider MUST, MAY, or
MUST NOT make the claim selectively disclosable.

### 3.2.1 IANA-registered and standard JWT / SD-JWT VC claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `iss` | `iss` | string | JWT issuer identifier. | MUST NOT |
| `iat` | `iat` | integer | Issued-at timestamp. | MUST NOT |
| `nbf` | `nbf` | integer | Not-before timestamp, where used. | MUST NOT |
| `exp` | `exp` | integer | Expiration timestamp. SHALL NOT be later than the scheduled departure time unless operational rules define a short grace period. | MUST NOT |
| `jti` | `jti` | string | Unique credential instance identifier, where used. | MUST NOT |
| `cnf` | `cnf` | object | Holder binding confirmation claim, where used. | MUST NOT |
| `status` | `status` | object | Status or revocation information, where used. | MUST NOT |
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `VehicleBoardingCredential`. | MUST NOT |

### 3.2.2 Private claims specific to the Vehicle Ferry Boarding Credential

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `credentialType` | `credentialType` | string | SHALL be `VehicleBoardingCredential`. | MUST NOT |
| `departure` | `departure` | object | Departure port-call object. | MUST NOT |
| `departure.date` | `date` | string | ISO 8601 date. | MUST |
| `departure.time` | `time` | string | Local time `HH:MM` or `HH:MM:SS`. | MUST |
| `departure.port` | `port` | string | Departure port identifier. | MUST |
| `departure.gate` | `gate` | string | Gate or lane, where present. | MAY |
| `arrival` | `arrival` | object | Arrival object. | MUST NOT |
| `arrival.date` | `date` | string | ISO 8601 date. | MUST |
| `arrival.time` | `time` | string | Local time `HH:MM` or `HH:MM:SS`. | MUST |
| `arrival.port` | `port` | string | Arrival port identifier. | MUST |
| `vesselDescription` | `vesselDescription` | string | Vessel name or description, where present. | MAY |
| `reservationNumber` | `reservationNumber` | string | Reservation number, where present. | MAY |
| `vehicle` | `vehicle` | object | Vehicle object. | MUST NOT |
| `vehicle.vehicleType` | `vehicleType` | string | Human-readable vehicle type. | MUST |
| `vehicle.vehicleTypeCode` | `vehicleTypeCode` | string | Vehicle type / tariff code. | MUST |
| `vehicle.plateNumber` | `plateNumber` | string | Plate / registration number, where present. | MAY |
| `ticket` | `ticket` | object | Ticket object. | MUST NOT |
| `ticket.ticketLet` | `ticketLet` | string | Ticket letter or class code. | MUST |
| `ticket.ticketNumber` | `ticketNumber` | string | Ticket number. | MUST |
| `trust_anchor` | `trust_anchor` | string | Trust-anchor reference, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Bound attestation type, where used. | MUST NOT |

### 3.2.3 Example JWT claim set

```json
{
  "iss": "https://issuer.example-ferry.gr",
  "iat": 1780315200,
  "nbf": 1780315200,
  "exp": 1781508600,
  "jti": "urn:uuid:2aacf8dc-3f0b-4b30-987d-5eacb9dba222",
  "vct": "VehicleBoardingCredential",
  "attestation_legal_category": "non-qualified-EAA",
  "credentialType": "VehicleBoardingCredential",
  "departure": {
    "date": "2026-06-15",
    "time": "07:30",
    "port": "GRRFN",
    "gate": "RFN-LANE-02"
  },
  "arrival": {
    "date": "2026-06-15",
    "time": "12:45",
    "port": "GRMLO"
  },
  "vesselDescription": "Fast Ferries Andros",
  "reservationNumber": "RES-2026-000991",
  "vehicle": {
    "vehicleType": "Passenger Car",
    "vehicleTypeCode": "PC",
    "plateNumber": "NIK-1234"
  },
  "ticket": {
    "ticketLet": "V",
    "ticketNumber": "000123456"
  },
  "trust_anchor": "https://trust.example.eu/ferry/operators/fast-ferries",
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

### 3.2.4 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be
generated by the issuer using the applicable signing algorithm, disclosure
construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

### 3.2.5 Example human-readable disclosed payload

A verifier that requests the minimum data needed for vehicle boarding may receive a
presentation disclosing the following claims:

```json
{
  "vct": "VehicleBoardingCredential",
  "credentialType": "VehicleBoardingCredential",
  "departure": {
    "date": "2026-06-15",
    "time": "07:30",
    "port": "GRRFN"
  },
  "arrival": {
    "date": "2026-06-15",
    "time": "12:45",
    "port": "GRMLO"
  },
  "vehicle": {
    "vehicleType": "Passenger Car",
    "vehicleTypeCode": "PC",
    "plateNumber": "NIK-1234"
  },
  "ticket": {
    "ticketLet": "V",
    "ticketNumber": "000123456"
  }
}
```

The issuer identity, credential type metadata, expiry time, signature, holder binding
proof, and trust anchor information are not treated as selectively disclosable vehicle
attributes and SHALL remain available to the verifier for technical validation.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model
encoding for the Vehicle Ferry Boarding Credential.

If a future version defines a W3C VCDM representation, that version SHALL define the
credential context, type, credential subject structure, proof type, selective
disclosure mechanism, and presentation requirements.

## 4 Attestation usage

The Vehicle Ferry Boarding Credential is intended for verifying vehicle boarding
entitlement for a specific ferry journey.

Typical usage scenarios include:

* presentation by the passenger at a vehicle boarding lane or port gate;
* scanning or digital verification by authorised boarding staff;
* online verification by a ferry operator system;
* offline or low-connectivity verification where the verifier can validate the
  credential signature, issuer, validity period, disclosed journey data, and vehicle
  attributes without relying on a real-time ticketing backend.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`) and `credentialType`;
* the issuer authorisation to issue Vehicle Ferry Boarding Credentials;
* the credential validity period;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the journey and vehicle details match the boarding context.

The Relying Party SHOULD request and verify an mVRC or another accepted
vehicle-registration credential when the boarding process requires vehicle matching. In
such cases, the Relying Party SHOULD compare relevant vehicle attributes, such as
`vehicle.plateNumber` and `vehicle.vehicleTypeCode`, with the Vehicle Ferry Boarding
Credential. The Relying Party SHALL apply data minimisation and SHALL request only the
attributes required for the boarding decision.

Where passenger identity matching is also required, the Relying Party SHOULD request
the passenger Ferry Boarding Pass and PID according to ferry policy.

The attestation SHOULD be device-bound through holder binding where supported by the
EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be
cryptographically bound to an mVRC or another accepted vehicle-registration attestation
where stronger vehicle matching is required. Where this binding is used, the metadata
attribute `cryptographically_bound_to` SHOULD identify the relevant vehicle-registration
attestation type.

No payment-specific transactional data is defined by this Rulebook. If the Vehicle
Ferry Boarding Credential is used as part of a transaction that also involves payment,
payment-related requirements SHALL be defined in a separate payment attestation,
payment profile, or transaction-specific rulebook.

Failure of wallet verification SHALL NOT by itself deny access to a staff-assisted
boarding process where ferry policy allows it.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer of the Vehicle Ferry Boarding Credential
is authorised to issue this attestation type.

For non-qualified EAA deployments, the Relying Party SHOULD obtain trust anchor
information through one or more of the following mechanisms:

* a machine-readable trust list or trust registry used by the relevant ecosystem;
* an issuer metadata endpoint published by the ferry operator or authorised ticketing
  operator;
* a trust framework entry managed by APTITUDE WP2 or by another authorised governance
  body;
* a pilot trust list used for controlled interoperability testing.

Where the metadata attribute `trust_anchor` is present, it SHOULD identify the
location or registry entry from which the Relying Party can obtain the issuer trust
anchor or issuer authorisation information.

The Relying Party SHALL use the trust anchor to verify that:

* the issuer signing key or certificate chains to a trusted authority or registered
  trust anchor;
* the issuer is authorised to issue the `VehicleBoardingCredential` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the
  trust framework.

Wallet Units MAY also use the same trust framework information during issuance to
determine whether the provider is authorised to issue this attestation type.

## 6 Revocation

The Vehicle Ferry Boarding Credential is typically short-lived and journey-specific.

The preferred validity model for this attestation is short validity. The credential
expiration time (`exp`) SHALL be set no later than the scheduled departure time unless
a clearly defined operational grace period is required by the ferry operator or port
boarding process.

After departure, the attestation SHALL be considered expired and SHALL NOT be accepted
for boarding.

Revocation MAY be handled by one or more of the following mechanisms:

* short validity, where the attestation expires at or before departure time;
* backend verification by the ferry operator or authorised boarding system;
* an attestation status list mechanism, where supported;
* an attestation revocation list mechanism, where supported.

If a status or revocation mechanism is included in the credential, the Relying Party
SHALL check the status before accepting the attestation, unless offline operating
rules explicitly allow deferred status checking.

If a vehicle ticket is cancelled, refunded, exchanged, duplicated, or otherwise
invalidated before departure, or if the vehicle is removed or replaced on the booking,
the issuer SHOULD either revoke or suspend the attestation, or ensure that backend
verification detects the invalid state.

## 7 Compliance

This Rulebook is designed to align with the EUDI Wallet architectural approach for
Electronic Attestations of Attributes and with the Attestation Rulebook structure
defined in the ARF.

The Rulebook supports the following compliance objectives:

* it defines the attestation purpose and scope;
* it defines mandatory, optional, and conditional attributes in an encoding-independent manner;
* it defines a legal category indication through `attestation_legal_category`;
* it defines an SD-JWT VC `vct` value and `credentialType` for the attestation type;
* it defines issuer, validity, and status metadata needed for verification;
* it defines code lists and integrity rules required for consistent interpretation;
* it defines how trust anchors can be obtained and used;
* it defines expiry and revocation expectations;
* it supports selective disclosure and data minimisation;
* it keeps vehicle entitlement separate from passenger, payment and registration credentials.

This Rulebook does not define a qualified EAA or public-sector EAA profile. It also
does not define ISO/IEC 18013-5 mdoc or W3C VCDM encodings in this version.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X Ferry Working Paper] | APTITUDE WP4, SEDIT-X Ferry Transport, Version 0.1, May 2026 |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes; building blocks and general requirements |
