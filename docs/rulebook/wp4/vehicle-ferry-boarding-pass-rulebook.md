# Attestation Rulebook for attestations of type Vehicle Ferry Boarding Pass

* Author(s):
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X Ferry Transport working paper and the APTITUDE Attestation Rulebook template. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This is an implementation-oriented draft. The SEDIT-X Ferry Transport working paper
> defines the credential purpose, issuer, candidate claim set, issuance trigger, mdoc
> format, proximity-presentation mode and principal verifier checks. It does not yet
> define a final EU-wide document type, namespace, controlled vocabularies, complete
> CDDL schema, trust endpoint or status endpoint. Proposed values require confirmation
> through APTITUDE WP2/WP4 governance before production use.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Vehicle Ferry Boarding Pass**, a ferry-operator-issued
Electronic Attestation of Attributes stored in a passenger's EUDI Wallet.

The attestation represents the right of a specific vehicle to board a particular ferry
sailing. It is issued after the ferry booking is completed and after the vehicle has been
linked to the booking using a verified mobile Vehicle Registration Credential (mVRC)
or another approved vehicle-registration source.

It enables a port verifier to determine that:

* the credential was issued by an authorised ferry operator or issuer acting for it;
* the credential is authentic, valid and not revoked;
* it applies to the current sailing, route, vessel, departure time and boarding window;
* the vehicle reference or registration binding is consistent with the booking; and
* the presented mVRC is consistent with the Vehicle Ferry Boarding Pass and the
  vehicle physically presented for embarkation.

The Vehicle Ferry Boarding Pass does not replace the mVRC, Passenger Ferry Boarding
Pass, PID or payment confirmation. Each remains a separate credential or operational
artefact.

### 1.2 Document structure

* Chapter 2 defines attributes and metadata independently of encoding.
* Chapter 3 defines the ISO/IEC 18013-5 mdoc encoding.
* Chapter 4 specifies issuance, presentation and verification.
* Chapter 5 specifies trust-anchor distribution.
* Chapter 6 specifies validity, status and revocation.
* Chapter 7 describes compliance.
* Chapter 8 lists references.

### 1.3 Key words

The capitalised key words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119]. Lower-case *must* denotes an external constraint rather than a requirement
created by this Rulebook.

### 1.4 Terminology

This document uses the terminology of Annex 1 of the EUDI Wallet Architecture and
Reference Framework.

* **mVRC**: mobile Vehicle Registration Credential.
* **Vehicle reference**: a booking-specific or ferry-specific pseudonymous vehicle identifier.
* **Sailing**: a specific ferry departure on a defined route, vessel, date and time.
* **Boarding window**: the interval during which the vehicle may be embarked.
* **Port verifier**: an authorised ferry employee device, lane terminal or other Relying Party Instance.
* **Intermediary Service**: the EUDIW Intermediary Service acting for the ferry operator.

## 2 Attestation attributes and metadata

### 2.1 Introduction and legal category

For the SEDIT-X pilot, the Vehicle Ferry Boarding Pass is a **non-qualified EAA**.
Its `category` value is:

```text
eaa:eu:non-qualified
```

The credential SHALL contain only the information needed to prove that a specific
vehicle may board a specific sailing. It SHOULD NOT duplicate the complete mVRC.

The design follows these principles:

1. one credential represents one vehicle entitlement for one sailing;
2. the mVRC remains the authoritative source of vehicle-registration attributes;
3. registration data is minimised through a vehicle reference or registration-number hash;
4. passenger identity and passenger entitlement remain separate;
5. payment data remains outside this credential;
6. the credential supports rapid ISO/IEC 18013-5 proximity presentation; and
7. cryptographic checks are combined with live ferry operational checks.

### 2.2 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_id` | Unique identifier of the Vehicle Ferry Boarding Pass. | string | `vfbp_01JYRFN8K73P6X9Q4C2M` |
| `booking_reference` | Ferry booking or reservation reference. | string | `BOOK-2026-000991` |
| `vehicle_reference` | Booking-specific or ferry-specific reference to the vehicle. | string | `veh_4a9c72f8d1` |
| `vehicle_category` | Ferry-relevant vehicle category. | string | `passenger_car` |
| `sailing_id` | Identifier of the specific ferry sailing. | string | `rafina-andros-2026-06-15-0730` |
| `route_id` | Identifier of the ferry route. | string | `RFN-AND` |
| `departure_port` | Departure-port code or identifier. | string | `RFN` |
| `arrival_port` | Arrival-port code or identifier. | string | `AND` |
| `vessel_id` | Stable vessel identifier, where available. | string | `IMO-9507891` |
| `vessel_name` | Human-readable vessel name. | string | `Fast Ferries Andros` |
| `departure_datetime` | Scheduled departure date and time. | date-time | `2026-06-15T07:30:00+03:00` |
| `boarding_window_start` | Beginning of the vehicle boarding window. | date-time | `2026-06-15T05:30:00+03:00` |
| `boarding_window_end` | End of the vehicle boarding window. | date-time | `2026-06-15T07:00:00+03:00` |
| `boarding_status` | Current issuer-known status of the vehicle entitlement. | string enum | `ready_to_board` |

Recommended `boarding_status` values are `issued`, `checked_in`, `ready_to_board`,
`boarded`, `cancelled`, `suspended` and `expired`.

### 2.3 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `ticket_number` | Operator vehicle-ticket identifier. | string | `VTKT-FF-883011` |
| `registration_number_hash` | Salted or keyed hash of the registration number. | string | `sha256:93c8...` |
| `registration_number` | Selectively disclosed registration number. | string | `NIK-1234` |
| `vehicle_type` | Detailed vehicle type. | string | `hatchback` |
| `vehicle_make` | Vehicle manufacturer, where needed. | string | `Toyota` |
| `vehicle_model` | Vehicle model, where needed. | string | `Corolla` |
| `vehicle_length_mm` | Vehicle length in millimetres. | integer | `4630` |
| `vehicle_width_mm` | Vehicle width in millimetres. | integer | `1780` |
| `vehicle_height_mm` | Vehicle height in millimetres. | integer | `1435` |
| `vehicle_mass_kg` | Vehicle mass relevant to booking or loading. | integer | `1320` |
| `deck_assignment` | Assigned garage deck or loading area. | string | `Garage Deck 2` |
| `boarding_lane` | Assigned vehicle boarding lane. | string | `RFN-LANE-02` |
| `hazardous_goods_declared` | Whether an approved dangerous-goods declaration exists. | boolean | `false` |
| `trailer_included` | Whether the booking includes a trailer. | boolean | `false` |
| `trailer_reference` | Booking reference for the trailer. | string | `trl_01JYR...` |
| `carrier_code` | Ferry-operator code. | string | `CFF` |
| `route_description` | Human-readable route. | string | `Rafina – Andros` |
| `scheduled_arrival_datetime` | Scheduled arrival time. | date-time | `2026-06-15T09:25:00+03:00` |
| `display_qr_payload` | Optional legacy QR/barcode payload. | binary or string | `M1VF...` |
| `terms_and_conditions_uri` | Applicable carriage terms. | URI | `https://ferry.example/vehicle-terms` |

An issuer SHOULD include either `registration_number_hash` or `registration_number`,
not both, unless a documented operational need exists.

### 2.4 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `mVRC_binding_reference` | Reference to the verified mVRC evidence used during booking. Mandatory where explicit binding is required. | string | `mvrc-bind:71d2...` |
| `vehicle_dimensions_source` | Source of vehicle dimensions. Mandatory when dimensions are included. | string enum | `mvrc` |
| `declared_dimensions_verified` | Whether user-declared dimensions were subsequently verified. | boolean | `false` |
| `trailer_category` | Ferry tariff category of a trailer. Mandatory when a trailer is included. | string | `small_trailer` |
| `passenger_boarding_pass_reference` | Reference to the Passenger Ferry Boarding Pass for the same booking. | string | `pfbp_01JYRFN7B42W6X8Q9D3K` |
| `cryptographically_bound_to` | Type of attestation to which this credential is cryptographically bound. | string | `urn:eu.europa.ec.eudi:vehicle-registration:1` |

Permitted `vehicle_dimensions_source` values are `mvrc`, `user_declared`,
`ferry_inspection` and `other_approved_source`.

The exact mVRC type identifier and formal cross-credential binding mechanism remain
to be confirmed by APTITUDE.

### 2.5 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `issuer` | Ferry operator or authorised Attestation Provider. | string or URI | `https://issuer.fastferries.example` |
| `credential_type` | Encoding-independent credential type. | string | `urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1` |
| `issued_at` | Credential issuance time. | date-time | `2026-06-12T10:36:02Z` |
| `valid_from` | Beginning of credential validity. | date-time | `2026-06-12T10:36:02Z` |
| `valid_until` | End of credential validity. | date-time | `2026-06-15T09:00:00+03:00` |
| `schema_version` | Credential-schema version. | string | `0.1` |
| `status_reference` | Credential status or revocation reference. | URI or structured value | `https://status.fastferries.example/atl/2026-06/12#992` |
| `trust_anchor_reference` | Location of applicable issuer trust information. | URI | `https://trust.aptitude.example/ferry-issuers` |

### 2.6 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_name` | Human-readable wallet name. | string | `Vehicle Ferry Boarding Pass` |
| `credential_description` | Human-readable credential description. | string | `Vehicle boarding pass for Rafina to Andros` |
| `issuer_name` | Human-readable issuer name. | string | `Cyclades Fast Ferries` |
| `issuer_logo_uri` | Issuer logo for wallet display. | URI | `https://issuer.example/logo.png` |
| `privacy_notice` | Applicable privacy information. | URI | `https://ferry.example/eudi/privacy` |
| `issuer_policy` | Issuance and verification policy. | URI | `https://ferry.example/eudi/issuer-policy` |
| `display_locale` | Preferred display language. | string | `en` |

### 2.7 Conditional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `status_list_index` | Entry index in an Attestation Status List. | integer | `992` |
| `status_list_uri` | URI of the Attestation Status List. | URI | `https://status.fastferries.example/atl/2026-06/12` |
| `revocation_list_uri` | URI of the Attestation Revocation List. | URI | `https://status.fastferries.example/arl/2026-06` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

### 3.1.1 Document type

The proposed mdoc document type is:

```text
urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1
```

This pilot identifier requires confirmation through APTITUDE schema governance.

### 3.1.2 Namespace

The proposed attribute namespace is:

```text
urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1
```

The `category` attribute SHALL use:

```text
org.etsi.01947201.010101
```

### 3.1.3 Encoding conventions

* `tstr`, `uint`, `bstr`, `bool` and `tdate` follow [RFC 8610] and [RFC 8949].
* Strings SHALL use UTF-8.
* Unless otherwise stated, strings SHALL not exceed 150 characters.
* Date-time values SHALL comply with [RFC 3339].
* Deterministic CBOR encoding SHALL be used.
* Indefinite-length CBOR items SHALL NOT be used.
* Vehicle categories SHOULD use an approved ferry tariff vocabulary.
* Port, vessel and carrier identifiers SHOULD use recognised code systems where available.

### 3.1.4 Attribute mapping

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
|---------------------|--------------------------|---------------------|---------------|
| `credential_id` | `credential_id` | tstr | `urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1` |
| `booking_reference` | `booking_reference` | tstr | same |
| `vehicle_reference` | `vehicle_reference` | tstr | same |
| `vehicle_category` | `vehicle_category` | tstr | same |
| `sailing_id` | `sailing_id` | tstr | same |
| `route_id` | `route_id` | tstr | same |
| `departure_port` | `departure_port` | tstr | same |
| `arrival_port` | `arrival_port` | tstr | same |
| `vessel_id` | `vessel_id` | tstr | same |
| `vessel_name` | `vessel_name` | tstr | same |
| `departure_datetime` | `departure_datetime` | tdate | same |
| `boarding_window_start` | `boarding_window_start` | tdate | same |
| `boarding_window_end` | `boarding_window_end` | tdate | same |
| `boarding_status` | `boarding_status` | tstr | same |
| `ticket_number` | `ticket_number` | tstr | same |
| `registration_number_hash` | `registration_number_hash` | tstr | same |
| `registration_number` | `registration_number` | tstr | same |
| `vehicle_type` | `vehicle_type` | tstr | same |
| `vehicle_make` | `vehicle_make` | tstr | same |
| `vehicle_model` | `vehicle_model` | tstr | same |
| `vehicle_length_mm` | `vehicle_length_mm` | uint | same |
| `vehicle_width_mm` | `vehicle_width_mm` | uint | same |
| `vehicle_height_mm` | `vehicle_height_mm` | uint | same |
| `vehicle_mass_kg` | `vehicle_mass_kg` | uint | same |
| `deck_assignment` | `deck_assignment` | tstr | same |
| `boarding_lane` | `boarding_lane` | tstr | same |
| `hazardous_goods_declared` | `hazardous_goods_declared` | bool | same |
| `trailer_included` | `trailer_included` | bool | same |
| `trailer_reference` | `trailer_reference` | tstr | same |
| `carrier_code` | `carrier_code` | tstr | same |
| `route_description` | `route_description` | tstr | same |
| `scheduled_arrival_datetime` | `scheduled_arrival_datetime` | tdate | same |
| `display_qr_payload` | `display_qr_payload` | bstr or tstr | same |
| `mVRC_binding_reference` | `mvrc_binding_reference` | tstr | same |
| `vehicle_dimensions_source` | `vehicle_dimensions_source` | tstr | same |
| `declared_dimensions_verified` | `declared_dimensions_verified` | bool | same |
| `trailer_category` | `trailer_category` | tstr | same |
| `passenger_boarding_pass_reference` | `passenger_boarding_pass_reference` | tstr | same |
| `cryptographically_bound_to` | `cryptographically_bound_to` | tstr | same |
| `issued_at` | `issued_at` | tdate | same |
| `valid_from` | `valid_from` | tdate | same |
| `valid_until` | `valid_until` | tdate | same |
| `schema_version` | `schema_version` | tstr | same |
| `status_reference` | `status_reference` | tstr or map | same |
| `trust_anchor_reference` | `trust_anchor_reference` | tstr | same |
| `category` | `category` | tstr | `org.etsi.01947201.010101` |

In the table, `same` means the proposed Vehicle Ferry Boarding Pass namespace.

### 3.1.5 Selective disclosure policy

A normal vehicle-boarding request SHOULD request only:

* credential and booking references;
* vehicle reference and category;
* sailing, route, ports and vessel;
* departure time and boarding window;
* boarding status;
* validity and status information; and
* the minimum vehicle-binding data needed for comparison with the mVRC.

Registration number, make/model, dimensions, trailer data, garage allocation and
legacy QR payload SHOULD be requested only when operationally required.

### 3.1.6 Illustrative mdoc data set

```json
{
  "docType": "urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1",
  "nameSpaces": {
    "urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1": {
      "credential_id": "vfbp_01JYRFN8K73P6X9Q4C2M",
      "booking_reference": "BOOK-2026-000991",
      "vehicle_reference": "veh_4a9c72f8d1",
      "registration_number_hash": "sha256:93c8...",
      "vehicle_category": "passenger_car",
      "vehicle_make": "Toyota",
      "vehicle_model": "Corolla",
      "vehicle_length_mm": 4630,
      "vehicle_height_mm": 1435,
      "sailing_id": "rafina-andros-2026-06-15-0730",
      "route_id": "RFN-AND",
      "departure_port": "RFN",
      "arrival_port": "AND",
      "vessel_id": "IMO-9507891",
      "vessel_name": "Fast Ferries Andros",
      "departure_datetime": "2026-06-15T07:30:00+03:00",
      "boarding_window_start": "2026-06-15T05:30:00+03:00",
      "boarding_window_end": "2026-06-15T07:00:00+03:00",
      "boarding_status": "ready_to_board",
      "carrier_code": "CFF",
      "mVRC_binding_reference": "mvrc-bind:71d2...",
      "vehicle_dimensions_source": "mvrc",
      "passenger_boarding_pass_reference": "pfbp_01JYRFN7B42W6X8Q9D3K",
      "issued_at": "2026-06-12T10:36:02Z",
      "valid_from": "2026-06-12T10:36:02Z",
      "valid_until": "2026-06-15T09:00:00+03:00",
      "schema_version": "0.1",
      "status_reference": "https://status.fastferries.example/atl/2026-06/12#992",
      "trust_anchor_reference": "https://trust.aptitude.example/ferry-issuers"
    },
    "org.etsi.01947201.010101": {
      "category": "eaa:eu:non-qualified"
    }
  }
}
```

The actual mdoc SHALL also contain all issuer-signed, device-signed, validity and
issuer-authentication structures required by ISO/IEC 18013-5 and the selected EUDI
Wallet profile.

## 3.2 SD-JWT VC-based encoding

Version 0.1 does not define an SD-JWT VC representation. The SEDIT-X Ferry Transport
working paper selects mdoc for port proximity presentation. A future version MAY add
SD-JWT VC as an additional remote format if semantic and security equivalence is preserved.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 does not define a W3C VCDM representation.

## 4 Attestation usage

### 4.1 Issuance prerequisites

The ferry company or authorised Attestation Provider SHALL issue the credential only after:

1. a valid ferry booking exists;
2. a vehicle ticket was selected;
3. the required mVRC attributes were presented and verified;
4. the vehicle was linked to the passenger booking;
5. vehicle fare and applicable fees were calculated;
6. payment succeeded or another accepted settlement condition was met;
7. sailing, route, vessel and departure data were available; and
8. validity and boarding windows were calculated.

Where authoritative dimensions are unavailable from the mVRC, the booking portal MAY
collect them from the User. Such values SHALL be marked as `user_declared` and MAY be
verified later at the port.

The issuer SHALL display the credential type, issuer, masked vehicle identity, category,
route, sailing, vessel, departure time, validity and purpose. The User SHALL consent to
receiving and storing the credential.

Issuance SHALL use OpenID4VCI or another APTITUDE-approved issuer-mediated flow.

### 4.2 Device and credential binding

The Vehicle Ferry Boarding Pass **SHOULD be device-bound** to a key controlled by the
Wallet Unit.

It SHALL be associated with the vehicle through `vehicle_reference` and, where used,
`registration_number_hash`, `registration_number` and `mVRC_binding_reference`.

It SHOULD be linked to the Passenger Ferry Boarding Pass or same booking through
`passenger_boarding_pass_reference` or `booking_reference`.

The credential SHALL NOT be freely transferable to another Wallet Unit, passenger or vehicle.

### 4.3 Presentation mode

The primary mode is ISO/IEC 18013-5 proximity presentation.

For vehicle boarding, the verifier SHOULD request a combined presentation containing:

* Passenger Ferry Boarding Pass;
* Vehicle Ferry Boarding Pass;
* PID where passenger binding is required; and
* mVRC attributes needed to bind the physical vehicle to the booking.

The Wallet Unit SHALL display the requested data and purpose and obtain User approval.

### 4.4 Relying Party obligations

The port verifier or Intermediary Service SHALL:

1. verify issuer signature and integrity;
2. verify issuer trust and authorisation;
3. verify validity and credential status;
4. verify mdoc device authentication and session binding;
5. confirm the selected sailing, route, vessel, ports and departure time;
6. verify that the current time is within the boarding window;
7. confirm the current operational boarding status;
8. compare Vehicle Ferry Boarding Pass data with the mVRC;
9. compare vehicle data with the ferry booking;
10. verify category and dimensions where relevant;
11. confirm the linked Passenger Ferry Boarding Pass relates to the same journey where required;
12. detect replay, duplicate use or already-boarded status; and
13. return `granted`, `denied` or `manual_review`.

A normal successful response SHOULD be limited to:

```json
{
  "vehicle_boarding_pass_valid": true,
  "mvrc_binding_valid": true,
  "vehicle_booking_match": true,
  "sailing_valid": true,
  "boarding_window_valid": true,
  "decision": "granted",
  "correlation_id": "pvs_01HY2B8MMQ21"
}
```

The verifier SHALL NOT retain complete mVRC or boarding-pass copies unless explicitly required.

### 4.5 Operational boarding event

The ferry system MAY record only:

* sailing identifier;
* booking reference or pseudonymous transaction identifier;
* vehicle reference;
* lane or verifier-device identifier;
* timestamp;
* event type and outcome; and
* operator identifier where required.

It SHOULD NOT retain complete credential copies, unnecessary registration data,
passenger civil identity or sensitive payment data.

### 4.6 Offline and degraded operation

The proximity exchange SHALL support local operation according to the selected mdoc profile.
The deployment SHALL define cache age, status availability, booking-system availability,
duplicate-use detection, reconciliation and staff-review rules.

Cryptographic validity alone does not prove that the booking remains active or that the
vehicle has not already boarded.

### 4.7 Transactional data

This is not a payment credential. It SHALL NOT contain PAN, IBAN, payment cryptograms,
payment tokens, account credentials or other sensitive payment-instrument data.

### 4.8 Failure and fallback

The verifier SHALL deny or request manual review where:

* signature, trust, status or validity fails;
* the sailing or boarding window does not match;
* the booking is cancelled, replaced or already consumed;
* the mVRC binding cannot be established;
* the physical or registered vehicle does not match the booking;
* vehicle category or dimensions are inconsistent;
* the linked passenger entitlement is invalid where required; or
* the mdoc response is malformed or replayed.

## 5 Trust anchors

The credential is issued by a ferry operator, an authorised issuer acting for it, or an
EUDIW Intermediary Service acting on its behalf.

For the APTITUDE pilot, relying parties SHALL obtain trust information through the
APTITUDE WP2 trust framework and applicable trusted issuer list.

The production profile SHALL define:

1. issuer registration authority;
2. trusted-list structure and service type;
3. delegated issuance rules;
4. certificate and mdoc issuer-authentication profiles;
5. issuer scope by operator, route or service;
6. key rollover and compromise handling; and
7. verifier behaviour when trust data is unavailable.

A verifier SHALL confirm both a valid trust chain and authorisation to issue:

```text
urn:aptitude.eu:seditx:vehicle-ferry-boarding-pass:1
```

## 6 Revocation

### 6.1 Validity model

The credential SHALL be journey-specific. Its validity SHALL not extend beyond the
sailing's operational period plus a limited grace period.

### 6.2 Revocation and status

The credential SHALL be status-checkable and SHALL be invalidated or updated when:

* the booking or vehicle ticket is cancelled or refunded;
* the vehicle is removed or replaced;
* the passenger is rebooked;
* the sailing is cancelled;
* a replacement credential is issued;
* fraud or erroneous issuance is detected;
* the Wallet Unit is compromised; or
* the vehicle has boarded and consumed-ticket status is used.

The verifier SHALL check both credential status and current ferry operational state.

### 6.3 Status-list location

APTITUDE SHOULD use the status-list mechanism selected by WP2. The production URL
has not yet been defined. Illustrative only:

```text
https://status.fastferries.example/
```

## 7 Compliance

This Rulebook is designed to align with Regulation (EU) 2024/1183, the EUDI Wallet
ARF, ARF Topic 12, ISO/IEC 18013-5, APTITUDE issuance/presentation profiles, the
SEDIT-X Ferry Transport working paper and GDPR data-minimisation principles.

It establishes that the attestation:

1. is a purpose-bound non-qualified EAA;
2. represents a vehicle-specific boarding entitlement;
3. is issued after mVRC-based vehicle verification and booking completion;
4. supports mdoc proximity presentation;
5. avoids unnecessary duplication of mVRC data;
6. remains separate from passenger, payment and discount credentials;
7. requires User authentication and consent;
8. combines cryptographic, sailing and vehicle-consistency checks;
9. supports status and revocation checking; and
10. provides staff-assisted fallback.

Open matters include the final document type and namespace, CDDL constraints,
vehicle-category vocabulary, mVRC identifier and binding mechanism, registration-number
hashing profile, trust and status endpoints, offline policy, duplicate-use semantics,
legacy barcode compatibility and handling of trailers, oversized vehicles and dangerous goods.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 establishing the European Digital Identity Framework |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X Ferry Working Paper] | APTITUDE WP4 SEDIT-X Ferry Transport Working Paper, Version 0.1 |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [ISO/IEC 18013-5] | Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence application |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 3339] | Date and Time on the Internet: Timestamps |
| [RFC 8610] | Concise Data Definition Language |
| [RFC 8949] | Concise Binary Object Representation |
| [Topic 7] | ARF Annex 2 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes — Building blocks and general requirements |
