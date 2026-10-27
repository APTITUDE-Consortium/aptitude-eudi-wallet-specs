# Attestation Rulebook for attestations of type Passenger Ferry Boarding Credential

* Author(s):
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X Ferry Transport working paper and the APTITUDE Attestation Rulebook template. |
| 0.2 | 24-07-2026 | Aligned data model and SD-JWT VC encoding with the Ferry Boarding Pass Attestation model. |
| 0.3 | 24-07-2026 | Aligned claim model with the Passenger Ferry Boarding Credential JSON Schema. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the Passenger Ferry Boarding Credential for the APTITUDE /
> SEDIT-X ferry pilot. The SD-JWT claim model below is aligned with the Passenger
> Boarding Credential JSON Schema (`credentialType`: `PassengerBoardingCredential`).
> Cabin-related claims are optional, so the model supports passengers with or without
> cabin accommodation.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Passenger Ferry Boarding Credential** for use in the
European Digital Identity Wallet ecosystem.

The credential expresses the real-world fact that a natural person holds a valid
boarding entitlement for a specific ferry journey and is entitled to board a specific
vessel at a given departure date and time.

The attestation is intended to be issued by an authentic source, such as a ferry
operator or an authorised ticketing system acting on behalf of the ferry operator. The
Holder is the passenger to whom the boarding entitlement applies. Relying Parties
include ferry operators, port boarding gates, authorised boarding control staff, and
other authorised systems that need to verify boarding entitlement.

In practical terms, the attestation enables a passenger to present proof of boarding
entitlement through an EUDI Wallet. It can reduce reliance on paper tickets and can
reduce the need for real-time backend lookups during boarding, provided that the
Relying Party can verify the issuer, the signature, the validity period, and the
relevant journey details.

The attestation supports ferry boarding use cases, including online or offline
verification at ports and boarding gates. It contains journey-specific and
passenger-specific information strictly related to the boarding process, including
passenger name, ticket identifiers, departure and arrival information, vessel
information, seat allocation and optional cabin details.

The attestation does not replace the Person Identification Data (PID) credential.
Where passenger-to-ticket binding must be checked at the port, the Passenger Ferry
Boarding Credential is presented together with the minimum required PID attributes.

The credential is distinct from:

* the **Vehicle Ferry Boarding Credential**, which represents a vehicle-specific boarding right;
* the **mVRC**, which provides authoritative vehicle registration attributes;
* a **payment confirmation or eReceipt**, which proves payment completion; and
* a student, loyalty or accessibility attestation used to establish a fare or service
  entitlement during booking.

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
| Passenger Ferry Boarding Credential | A Verifiable Credential representing a passenger's entitlement to board a specific ferry journey. |
| Ferry operator | The organisation operating the ferry journey or acting as the authentic source for the boarding entitlement. |
| Authorised ticketing system | A system authorised by the ferry operator to issue or manage boarding passes. |
| Passenger | The natural person to whom the boarding entitlement applies. |
| Boarding gate | A physical or digital checkpoint where the boarding entitlement is verified. |
| Journey | A specific ferry trip between a departure port and an arrival port at a scheduled date and time. |

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that a Passenger Ferry Boarding
Credential may contain. The attributes are defined in an encoding-independent manner.
Each attribute is classified as mandatory, optional, or conditional.

The credential is journey-specific and time-bound. It contains only the information
necessary to verify that the Holder is entitled to board a specific ferry service. The
claim model is nested under `departure`, `arrival`, `passenger`, `ticket` and
`accommodation` objects as defined by the Passenger Boarding Credential schema.

### 2.1 Introduction

The Passenger Ferry Boarding Credential is defined as a non-qualified Electronic
Attestation of Attributes unless a future version of this Rulebook explicitly defines a
qualified or public-sector legal category.

The attribute `attestation_legal_category` SHALL be included and SHALL have the value
`non-qualified-EAA`.

The attestation model consists of the following logical groups:

* credential type;
* departure port-call details;
* arrival details;
* passenger identification;
* ticket identifiers;
* accommodation details (seat mandatory; cabin optional);
* optional vessel and reservation information;
* credential metadata.

The attestation is bound to a single passenger and a single ferry journey. It SHALL NOT
be treated as a reusable credential after the scheduled departure time.

Cabin-related claims under `accommodation` are optional. The credential therefore
supports passengers with or without cabin accommodation. Seat-related claims
(`seatType`, `seatNumber`) remain required within the `accommodation` object.

### 2.2 Mandatory attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `attestation_legal_category` | ARF Topic 12 / Rulebook legal category indication | Indicates the legal category of the attestation. | string | `non-qualified-EAA` |
| `credentialType` | Schema const | Credential type discriminator. SHALL be `PassengerBoardingCredential`. | string | `PassengerBoardingCredential` |
| `departure.date` | ISO 8601 date | Scheduled departure date. | date | `2026-06-15` |
| `departure.time` | Local time `HH:MM` or `HH:MM:SS` | Scheduled departure time at the departure port. | string | `07:30` |
| `departure.port` | Port identifier | Departure port. | string | `GRRFN` |
| `arrival.date` | ISO 8601 date | Scheduled arrival date. | date | `2026-06-15` |
| `arrival.time` | Local time `HH:MM` or `HH:MM:SS` | Scheduled arrival time at the arrival port. | string | `12:45` |
| `arrival.port` | Port identifier | Arrival port. | string | `GRMLO` |
| `passenger.firstName` | OIDC `given_name` where applicable | Passenger given name. | string | `Nikos` |
| `passenger.lastName` | OIDC `family_name` where applicable | Passenger family name. | string | `Triantafyllou` |
| `ticket.ticketLet` | N/A | Ticket letter, class code, or other operator-specific classification. | string | `A` |
| `ticket.ticketNumber` | N/A | Ferry ticket number. | string | `000123456` |
| `accommodation.seatType` | N/A | Type of seat or accommodation product. | string | `AIR_SEAT` |
| `accommodation.seatNumber` | N/A | Assigned seat number or seating identifier. | string | `12A` |

### 2.3 Optional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vesselDescription` | N/A | Description or name of the ferry vessel. | string | `Fast Ferries Andros` |
| `reservationNumber` | N/A | Booking or reservation number associated with the ticket. | string | `RES-2026-000991` |
| `departure.gate` | N/A | Departure gate, terminal or boarding area. | string | `RFN-GATE-02` |
| `ticket.discount` | N/A | Discount or fare-basis code applied to the ticket. | string | `student` |
| `accommodation.cabinNumber` | N/A | Assigned cabin number, where cabin accommodation is booked. | string | `C-204` |
| `accommodation.cabinClassDescription` | N/A | Human-readable cabin class description. | string | `Outside twin` |
| `accommodation.cabinClassCode` | N/A | Operator cabin class code. | string | `OA2` |
| `accommodation.classType` | N/A | Class type associated with the accommodation. | string | `outside` |
| `accommodation.numberOfBeds` | N/A | Number of beds in the cabin. | integer | `2` |
| `accommodation.bedPosition` | N/A | Assigned bed position within the cabin. | string | `lower` |
| `accommodation.maleBeds` | N/A | Number of male beds allocated, where used by the operator. | integer or null | `1` |
| `accommodation.femaleBeds` | N/A | Number of female beds allocated, where used by the operator. | integer or null | `1` |

### 2.4 Conditional attributes

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `departure.gate` | N/A | SHOULD be present where gate or boarding-area assignment is known at issuance. | string | `RFN-GATE-02` |
| `reservationNumber` | N/A | SHOULD be present where the ferry system uses a reservation number distinct from `ticket.ticketNumber`. | string | `RES-2026-000991` |
| `ticket.discount` | N/A | SHOULD be present only where a verified discount or fare basis was applied. | string | `student` |
| Cabin claims under `accommodation` | N/A | `cabinNumber`, `cabinClassDescription`, `cabinClassCode`, `classType`, `numberOfBeds`, `bedPosition`, `maleBeds` and `femaleBeds` SHALL be present only where cabin accommodation is booked. MUST be omitted for seat-only or free-seating products that do not allocate a cabin. | string / integer / null | `C-204` |

Where free seating applies and no fixed seat is allocated, `accommodation.seatNumber`
MAY contain an operator-defined placeholder or seating-product identifier, provided the
issuer documents the convention.

### 2.5 Mandatory metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `vct` | SD-JWT VC | Verifiable Credential Type identifying this attestation type. | string | `PassengerBoardingCredential` |
| `iss` | SD-JWT VC / JWT | Identifier of the issuer of the credential. | string | `https://issuer.example-ferry.gr` |
| `iat` | JWT | Time at which the credential was issued. | integer | `1780315200` |
| `exp` | JWT | Expiration time of the credential. For this attestation it SHALL NOT be later than the scheduled departure time unless operational rules explicitly require a short post-departure grace period. | integer | `1781508600` |
| `cnf` | SD-JWT VC / JOSE | Confirmation claim binding the credential to key material controlled by the Holder or Wallet Unit, where holder binding is used. | object | `{ "jwk": { ... } }` |
| `status` | SD-JWT VC status mechanism, where used | Status information enabling revocation or suspension checks, where revocation is supported. | object | `{ "status_list": { ... } }` |

### 2.6 Optional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `nbf` | JWT | Time before which the credential MUST NOT be accepted. | integer | `1780315200` |
| `jti` | JWT | Unique identifier of the credential instance. | string | `urn:uuid:1ddcf8dc-3f0b-4b30-987d-5eacb9dba111` |
| `trust_anchor` | ARF Topic 12 | Location or identifier of the machine-readable trust anchor or trust framework entry used to verify issuer authorisation. | string | `https://trust.example.eu/ferry/operators/fast-ferries` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | Identifier of another attestation type to which this attestation is cryptographically bound, where such binding is used. | string | `urn:eudi:pid:1` |

### 2.7 Conditional metadata

| **Data Identifier** | **Semantic Reference** | **Definition** | **Data type** | **Example value** |
|---------------------|------------------------|----------------|---------------|-------------------|
| `status` | SD-JWT VC status mechanism, where used | SHALL be present if the issuer supports revocation or suspension for the boarding credential. MAY be omitted where the attestation is short-lived and expires at or before departure time. | object | `{ "status_list": { ... } }` |
| `cryptographically_bound_to` | ARF Topic 12 / ARB_28 | SHOULD be present where the boarding credential is required to be presented together with PID or another identity attestation for passenger identity matching. | string | `urn:eudi:pid:1` |

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes / extensibility** |
|----------------|--------------------|-------------|--------------------------|---------------------------|
| `credentialType` | `PassengerBoardingCredential` | Credential type discriminator. | Passenger Boarding Credential schema | Const value; additional values SHALL NOT be used. |
| `departure.date` / `arrival.date` | ISO 8601 date | Scheduled date. | ISO 8601 | Date-only format `YYYY-MM-DD` SHALL be used. |
| `departure.time` / `arrival.time` | `HH:MM` or `HH:MM:SS` | Scheduled local time. | Schema time pattern | Time-zone handling SHALL be clear to the verifier as local port time. |
| `departure.port` / `arrival.port` | Valid port identifiers | Identifies the port. | UN/LOCODE recommended | Operator-specific port identifiers MAY be used during pilots. |
| `accommodation.seatType` | Issuer-defined seating / accommodation codes | Identifies the seat or product type. | Ferry operator vocabulary | Examples include `AIR_SEAT`, `DECK`, `CABIN`. |
| `ticket.discount` | Issuer-defined discount codes | Identifies an applied fare basis or discount. | Ferry operator tariff vocabulary | Examples include `student`, `loyalty`, `child`. |
| `attestation_legal_category` | `non-qualified-EAA`, `QEAA`, `PuB-EAA` | Indicates the legal category of the attestation. | ARF Topic 12 / Rulebook template | This Rulebook uses `non-qualified-EAA`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Verifier / issuer behavior on failure** |
|-------------|--------------------|-------------------|--------------------|-------------------------------------------|
| `PBP-IR-01` | `arrival.date` SHALL NOT precede `departure.date`. | Prevents temporally inconsistent journey information. | Issuer business rules, schema validation, verifier business validation. | Issuer SHALL reject inconsistent journey data. Verifier SHALL reject the attestation for boarding if this rule fails. |
| `PBP-IR-02` | The credential SHALL be bound to a single journey and a single passenger. | Prevents reuse across different services, vessels, dates, or passengers. | Issuer business rules and verifier business validation. | Verifier SHALL reject the attestation if it cannot determine the specific journey or passenger. |
| `PBP-IR-03` | The attestation SHALL NOT be reusable after the scheduled departure time. | Boarding entitlement is time-bound and journey-specific. | Issuer validity period and verifier freshness checks. | Verifier SHALL reject the attestation after expiry, unless a locally defined operational grace period applies. |
| `PBP-IR-04` | `credentialType` SHALL equal `PassengerBoardingCredential`. | Ensures type-safe interpretation of the claim set. | Schema validation and verifier business validation. | Verifier SHALL reject credentials with an unexpected `credentialType`. |
| `PBP-IR-05` | `ticket.ticketLet` and `ticket.ticketNumber` SHALL be non-empty. | Ensures a usable ticket identifier for embarkation and audit. | Schema validation and issuer business rules. | Issuer SHALL reject empty ticket identifiers. Verifier SHALL reject incomplete ticket data. |
| `PBP-IR-06` | Cabin claims under `accommodation` MUST be omitted if no cabin is allocated. | Prevents misleading cabin allocation information for seat-only tickets. | Issuer business rules and schema validation. | Issuer SHALL omit cabin claims for non-cabin products. Verifier SHOULD ignore or reject inconsistent cabin data. |
| `PBP-IR-07` | Passenger name attributes SHOULD be compared with PID or another accepted identity source when the boarding process requires identity matching. | Ensures that the person presenting the boarding credential is the intended passenger. | Relying Party business validation. | Verifier SHOULD reject the boarding transaction where required identity matching fails. |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version of the Rulebook does not define an ISO/IEC 18013-5 mdoc encoding for the
Passenger Ferry Boarding Credential.

The credential defined in this Rulebook is specified for SD-JWT VC-based issuance and
presentation. If a future version defines an ISO/IEC 18013-5-compliant mdoc
representation, that version SHALL define a unique document type, namespaces, attribute
identifiers, CBOR encoding rules, and illustrative mdoc examples.

## 3.2 SD-JWT VC-based encoding

The Passenger Ferry Boarding Credential SHALL be issued as an SD-JWT VC.

The Verifiable Credential Type (`vct`) for this attestation type is:

```text
PassengerBoardingCredential
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
| `vct` | `vct` | string | SD-JWT VC type. Value SHALL be `PassengerBoardingCredential`. | MUST NOT |

### 3.2.2 Public or reusable claims

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Reference/Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|---------------------|-----------------|
| `passenger.firstName` | `firstName` | string | Passenger given name. May be mapped to OIDC `given_name` where applicable. | MUST |
| `passenger.lastName` | `lastName` | string | Passenger family name. May be mapped to OIDC `family_name` where applicable. | MUST |

### 3.2.3 Private claims specific to the Passenger Ferry Boarding Credential

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Notes** | **Disclosable** |
|---------------------|--------------------------|---------------------|-----------|-----------------|
| `attestation_legal_category` | `attestation_legal_category` | string | SHALL be `non-qualified-EAA`. | MUST NOT |
| `credentialType` | `credentialType` | string | SHALL be `PassengerBoardingCredential`. | MUST NOT |
| `departure` | `departure` | object | Departure port-call object. | MUST NOT |
| `departure.date` | `date` | string | ISO 8601 date. | MUST |
| `departure.time` | `time` | string | Local time `HH:MM` or `HH:MM:SS`. | MUST |
| `departure.port` | `port` | string | Departure port identifier. | MUST |
| `departure.gate` | `gate` | string | Gate or boarding area, where present. | MAY |
| `arrival` | `arrival` | object | Arrival object. | MUST NOT |
| `arrival.date` | `date` | string | ISO 8601 date. | MUST |
| `arrival.time` | `time` | string | Local time `HH:MM` or `HH:MM:SS`. | MUST |
| `arrival.port` | `port` | string | Arrival port identifier. | MUST |
| `vesselDescription` | `vesselDescription` | string | Vessel name or description, where present. | MAY |
| `reservationNumber` | `reservationNumber` | string | Reservation number, where present. | MAY |
| `passenger` | `passenger` | object | Passenger object. | MUST NOT |
| `ticket` | `ticket` | object | Ticket object. | MUST NOT |
| `ticket.ticketLet` | `ticketLet` | string | Ticket letter or class code. | MUST |
| `ticket.ticketNumber` | `ticketNumber` | string | Ticket number. | MUST |
| `ticket.discount` | `discount` | string | Discount or fare-basis code, where present. | MAY |
| `accommodation` | `accommodation` | object | Accommodation object. | MUST NOT |
| `accommodation.seatType` | `seatType` | string | Seat or product type. | MUST |
| `accommodation.seatNumber` | `seatNumber` | string | Seat number or seating identifier. | MUST |
| `accommodation.cabinNumber` | `cabinNumber` | string | Cabin number, where present. | MAY |
| `accommodation.cabinClassDescription` | `cabinClassDescription` | string | Cabin class description, where present. | MAY |
| `accommodation.cabinClassCode` | `cabinClassCode` | string | Cabin class code, where present. | MAY |
| `accommodation.classType` | `classType` | string | Class type, where present. | MAY |
| `accommodation.numberOfBeds` | `numberOfBeds` | integer | Number of beds, where present. | MAY |
| `accommodation.bedPosition` | `bedPosition` | string | Bed position, where present. | MAY |
| `accommodation.maleBeds` | `maleBeds` | integer or null | Male beds, where present. | MAY |
| `accommodation.femaleBeds` | `femaleBeds` | integer or null | Female beds, where present. | MAY |
| `trust_anchor` | `trust_anchor` | string | Trust-anchor reference, where used. | MUST NOT |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | Bound attestation type, where used. | MUST NOT |

### 3.2.4 Example JWT claim set

```json
{
  "iss": "https://issuer.example-ferry.gr",
  "iat": 1780315200,
  "nbf": 1780315200,
  "exp": 1781508600,
  "jti": "urn:uuid:1ddcf8dc-3f0b-4b30-987d-5eacb9dba111",
  "vct": "PassengerBoardingCredential",
  "attestation_legal_category": "non-qualified-EAA",
  "credentialType": "PassengerBoardingCredential",
  "departure": {
    "date": "2026-06-15",
    "time": "07:30",
    "port": "GRRFN",
    "gate": "RFN-GATE-02"
  },
  "arrival": {
    "date": "2026-06-15",
    "time": "12:45",
    "port": "GRMLO"
  },
  "vesselDescription": "Fast Ferries Andros",
  "reservationNumber": "RES-2026-000991",
  "passenger": {
    "firstName": "Nikos",
    "lastName": "Triantafyllou"
  },
  "ticket": {
    "ticketLet": "A",
    "ticketNumber": "000123456",
    "discount": "student"
  },
  "accommodation": {
    "seatType": "AIR_SEAT",
    "seatNumber": "12A",
    "cabinNumber": "C-204",
    "cabinClassDescription": "Outside twin",
    "cabinClassCode": "OA2",
    "classType": "outside",
    "numberOfBeds": 2,
    "bedPosition": "lower",
    "maleBeds": 1,
    "femaleBeds": 1
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

### 3.2.5 Example issued SD-JWT

The following is a non-normative placeholder example. A production SD-JWT SHALL be
generated by the issuer using the applicable signing algorithm, disclosure
construction, holder binding, and SD-JWT VC rules.

```text
<issuer-signed-sd-jwt>~<disclosure-1>~<disclosure-2>~<disclosure-n>~<holder-binding-jwt>
```

### 3.2.6 Example human-readable disclosed payload

A verifier that requests the minimum data needed for boarding may receive a
presentation disclosing the following claims:

```json
{
  "vct": "PassengerBoardingCredential",
  "credentialType": "PassengerBoardingCredential",
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
  "passenger": {
    "firstName": "Nikos",
    "lastName": "Triantafyllou"
  },
  "ticket": {
    "ticketLet": "A",
    "ticketNumber": "000123456"
  },
  "accommodation": {
    "seatType": "AIR_SEAT",
    "seatNumber": "12A"
  }
}
```

The issuer identity, credential type metadata, expiry time, signature, holder binding
proof, and trust anchor information are not treated as selectively disclosable
passenger attributes and SHALL remain available to the verifier for technical
validation.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version of the Rulebook does not define a W3C Verifiable Credentials Data Model
encoding for the Passenger Ferry Boarding Credential.

If a future version defines a W3C VCDM representation, that version SHALL define the
credential context, type, credential subject structure, proof type, selective
disclosure mechanism, and presentation requirements.

## 4 Attestation usage

The Passenger Ferry Boarding Credential is intended for verifying passenger boarding
entitlement for a specific ferry journey.

Typical usage scenarios include:

* presentation by the passenger at a port or boarding gate;
* scanning or digital verification by authorised boarding staff;
* online verification by a ferry operator system;
* offline or low-connectivity verification where the verifier can validate the
  credential signature, issuer, validity period, and disclosed journey data without
  relying on a real-time ticketing backend.

A Relying Party receiving the attestation SHALL verify:

* the issuer signature;
* the SD-JWT VC type (`vct`) and `credentialType`;
* the issuer authorisation to issue Passenger Ferry Boarding Credentials;
* the credential validity period;
* the credential status, where a status mechanism is present;
* holder binding, where used;
* the integrity rules defined in Section 2.9;
* that the journey and passenger details match the boarding context.

The Relying Party SHOULD request and verify PID or another accepted identity
credential when the boarding process requires passenger identity matching. In such
cases, the Relying Party SHOULD compare the relevant identity attributes, such as
`passenger.firstName` and `passenger.lastName`, with the boarding credential. The
Relying Party SHALL apply data minimisation and SHALL request only the attributes
required for the boarding decision.

The attestation SHOULD be device-bound through holder binding where supported by the
EUDI Wallet and the applicable SD-JWT VC profile. The attestation MAY be
cryptographically bound to a PID or another accepted identity attestation where the
boarding process requires stronger passenger identity matching. Where this binding is
used, the metadata attribute `cryptographically_bound_to` SHOULD contain:

```text
urn:eudi:pid:1
```

No payment-specific transactional data is defined by this Rulebook. If the Passenger
Ferry Boarding Credential is used as part of a transaction that also involves payment,
payment-related requirements SHALL be defined in a separate payment attestation,
payment profile, or transaction-specific rulebook.

Failure of wallet verification SHALL NOT by itself deny the passenger access to a
staff-assisted boarding process where ferry policy allows it.

## 5 Trust anchors

A Relying Party SHALL verify that the issuer of the Passenger Ferry Boarding Credential
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
* the issuer is authorised to issue the `PassengerBoardingCredential` attestation type;
* the issuer metadata or trust framework entry has not expired or been revoked;
* the issuer identity in the credential is consistent with the issuer identity in the
  trust framework.

Wallet Units MAY also use the same trust framework information during issuance to
determine whether the provider is authorised to issue this attestation type.

## 6 Revocation

The Passenger Ferry Boarding Credential is typically short-lived and journey-specific.

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

If a ticket is cancelled, refunded, exchanged, duplicated, or otherwise invalidated
before departure, the issuer SHOULD either revoke or suspend the attestation, or ensure
that backend verification detects the invalid state.

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
* it supports seat-only and cabin accommodations through optional cabin claims.

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
| [OIDC] | OpenID Connect Core 1.0 |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes; building blocks and general requirements |
