# Attestation Rulebook for attestations of type Passenger Ferry Boarding Credential

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date       | Description                                                                                                                                                                                                 |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Ferry Transport working paper and the APTITUDE Attestation Rulebook template.                                                                                            |
| 0.2     | 24-07-2026 | Aligned data model and SD-JWT VC encoding with the Ferry Boarding Pass Attestation model.                                                                                                                   |
| 0.3     | 24-07-2026 | SD-JWT claim model aligned with the Passenger Ferry Boarding Credential JSON Schema. Withdrawn as the encoding by version 0.4.                                                                              |
| 0.4     | 02-11-2026 | Replaces the SD-JWT encoding with an ISO/IEC 18013-5 mdoc. `docType` is `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`. The gate verifies the `DeviceResponse` offline.                            |

**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the **Passenger Ferry Boarding Credential**. The Wallet
> display name is **Passenger Ferry Boarding Credential**. The credential type
> identifier, mdoc `docType` and namespace are
> `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`.
>
> The credential is an **ISO/IEC 18013-5 mdoc**. The Wallet presents it with
> that standard's device engagement and device retrieval. The boarding-gate
> reader verifies the `DeviceResponse` offline and uses the result to decide
> whether the passenger may embark.
>
> Version 0.3, an SD-JWT VC with `vct` `PassengerBoardingCredential` and nested
> `departure`, `arrival`, `passenger`, `ticket` and `accommodation` objects, is
> withdrawn as the encoding. This credential SHALL NOT be issued as an SD-JWT VC.
>
> Cabin elements are optional, so the model supports passengers with or without
> cabin accommodation.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Passenger Ferry Boarding Credential**, a short-lived
Electronic Attestation of Attributes for the European Digital Identity Wallet.

The credential type identifier is:

```text
eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1
```

The Wallet display name is **Passenger Ferry Boarding Credential**.

The credential expresses the fact that one passenger is entitled to board one
ferry journey at a scheduled departure. A journey is one sailing: one
departure port, one arrival port, and one scheduled departure date and time.

The attestation is issued by an authentic source, such as a ferry operator or
an authorised ticketing system acting for that operator. The Holder is the
passenger named on the ticket. The verifier is the boarding-gate reader, or
boarding staff using such a reader, at the departure port.

The credential MAY be used to:

- present passenger boarding entitlement at a gate reader that supports
  ISO/IEC 18013-5 device engagement and device retrieval;
- show the holder the sailing, ticket and seat or cabin in the Wallet; and
- let the operator accept the passenger without a live ticketing lookup, when
  the reader can verify the mdoc from provisioned trust anchors.

The names in this credential are the names on the ticket. They are not PID,
and this credential is not a combined identity-and-boarding document. Where
the gate must match the person to the ticket, this credential SHOULD be
presented together with the minimum required PID attributes. That is a
separate presentation.

The credential SHALL NOT be treated as:

- the **Vehicle Ferry Boarding Credential**, which is a vehicle's boarding
  right;
- the **mVRC**, which provides the vehicle-registration attributes;
- **PID**; or
- a payment confirmation or eReceipt.

A student, loyalty or accessibility attestation used to choose a fare remains
a separate credential. A discount code MAY be copied onto this ticket. The
entitlement attestation itself is not embedded here.

### 1.2 Architectural role

The mdoc is what the gate verifies. A reader that has no network connection
SHALL be able to decide using:

- issuer authentication (`issuerAuth` over the Mobile Security Object);
- the digests of the disclosed data elements;
- device authentication bound to the `SessionTranscript`;
- `validityInfo` in the Mobile Security Object; and
- a match between the disclosed journey and passenger elements and the sailing
  this gate is boarding.

The operator's ticketing system remains authoritative for the booking. A
reader with connectivity SHOULD apply revocation and status. A reader without
connectivity relies on the signed validity window and the disclosed journey
elements, and SHALL NOT refuse an otherwise valid mdoc only because it cannot
reach the ticketing system.

`validityInfo` is the acceptance window. It does not by itself identify the
sailing. The reader SHALL still match `departure_port`, `departure_date` and
`departure_time` to the sailing it is boarding.

Presenting the credential does not consume it. A passenger MAY be checked at
more than one point before departure. Invalidation before `validUntil` is
revocation, which an offline reader applies only after it has received status.

### 1.3 Document structure

- Chapter 2 defines attributes and metadata.
- Chapter 3 defines the ISO/IEC 18013-5 mdoc encoding.
- Chapter 4 defines issuance, presentation and verification.
- Chapter 5 defines trust anchors.
- Chapter 6 defines validity, suspension and revocation.
- Chapter 7 defines compliance, privacy and security requirements.
- Chapter 8 lists references.

### 1.4 Key words

The capitalised words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119].

In addition, 'must' (non-capitalised) indicates an external constraint, not a
requirement created by this document. 'can' indicates a capability.

### 1.5 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

For this Rulebook:

- **Passenger Ferry Boarding Credential** means the mdoc whose `docType` is
  `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`.
- **Journey** means one ferry sailing between a departure port and an arrival
  port at a scheduled date and time.
- **Ferry operator** means the organisation operating that sailing, or the
  authentic source for the passenger boarding entitlement.
- **Authorised ticketing system** means a system the ferry operator authorises
  to issue this credential.
- **Passenger** means the natural person named on this credential.
- **Gate reader** means the mdoc reader at the passenger boarding gate. It
  performs ISO/IEC 18013-5 device engagement and device retrieval and decides
  whether the passenger may embark.
- **PID** means Person Identification Data of type
  `urn:eu.europa.ec.eudi:pid:1`.

## 2 Attestation attributes and metadata

### 2.1 Legal category

For the SEDIT-X pilot, the credential is a **non-qualified EAA**:

```text
eaa:eu:non-qualified
```

A deployment MAY issue the credential as a qualified EAA when the issuer is a
qualified trust service provider and the attestation meets the requirements
for a qualified electronic attestation of attributes:

```text
eaa:eu:qualified
```

The issued credential SHALL use exactly one of these category values.

### 2.2 Design principles

1. **One passenger, one journey.** The credential SHALL describe a single
   passenger and a single sailing. It SHALL NOT be reused for another sailing,
   vessel, date or passenger.
2. **mdoc boarding credential.** The credential SHALL be an ISO/IEC 18013-5
   mdoc. Presentation SHALL use device engagement and device retrieval as
   defined in that standard.
3. **Offline verification.** A gate reader SHALL be able to verify the
   credential without a live call to the ticketing system.
4. **Minimum disclosure.** The data elements SHALL be limited to the sailing,
   the ticketed name, the ticket identifier, the seat and, where booked, the
   cabin.
5. **No payment data.** The credential SHALL NOT carry a payment confirmation,
   card number or eReceipt.
6. **Device binding.** The Mobile Security Object SHALL contain the Wallet
   `deviceKey`. The reader SHALL verify ISO/IEC 18013-5 device authentication
   bound to the `SessionTranscript`.
7. **Short validity.** `validityInfo.validUntil` SHALL be no later than the
   scheduled departure, plus only a limited grace period where the operator
   defines one.
8. **Separate credentials.** Vehicle boarding, vehicle registration, PID and
   payment remain other attestations.
9. **Fallback.** Staff-assisted boarding SHALL remain available where ferry
   policy allows it. Failure of wallet verification SHALL NOT by itself remove
   that path.

### 2.3 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `id` | Unique identifier of this credential instance. | string | `1ddcf8dc-3f0b-4b30-987d-5eacb9dba111` |
| `category` | Legal category. Either `eaa:eu:non-qualified` or `eaa:eu:qualified`. | string | `eaa:eu:non-qualified` |
| `departure_date` | Scheduled departure date at the departure port. | date | `2026-06-15` |
| `departure_time` | Scheduled departure time at the departure port, local port time, `HH:MM` or `HH:MM:SS`. | string | `07:30` |
| `departure_port` | Departure port identifier. UN/LOCODE is recommended. | string | `GRRFN` |
| `arrival_date` | Scheduled arrival date at the arrival port. | date | `2026-06-15` |
| `arrival_time` | Scheduled arrival time at the arrival port, local port time, `HH:MM` or `HH:MM:SS`. | string | `12:45` |
| `arrival_port` | Arrival port identifier. UN/LOCODE is recommended. | string | `GRMLO` |
| `first_name` | Given name of the passenger on the ticket. | string | `Nikos` |
| `last_name` | Family name of the passenger on the ticket. | string | `Triantafyllou` |
| `ticket_let` | Ticket letter, class code or other operator classification. | string | `A` |
| `ticket_number` | Ferry ticket number. | string | `000123456` |
| `seat_type` | Seat or accommodation product. | string | `AIR_SEAT` |
| `seat_number` | Assigned seat, or an operator placeholder where seating is free. | string | `12A` |

These attributes SHALL be present.

`departure_date` and `arrival_date` SHALL use `YYYY-MM-DD`. The times are
local port time, not an instant with a numeric offset. The acceptance window
the reader enforces is `validityInfo`, which does carry a date-time.

`first_name` and `last_name` are the names printed for this ticket. They are
not PID claims. When the gate matches identity, it compares these values with
PID `given_name` and `family_name` in a separate presentation.

Where free seating applies and no fixed seat is allocated, `seat_number` MAY
contain an operator-defined placeholder, provided the issuer documents the
convention.

### 2.4 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `departure_gate` | Departure gate or boarding area, when known at issuance. | string | `RFN-GATE-02` |
| `vessel_description` | Name or description of the ferry vessel. | string | `Fast Ferries Andros` |
| `reservation_number` | Booking number, when the operator uses one distinct from `ticket_number`. | string | `RES-2026-000991` |
| `discount` | Discount or fare-basis code, when one was applied. | string | `student` |
| `cabin_number` | Assigned cabin number. | string | `C-204` |
| `cabin_class_description` | Human-readable cabin class. | string | `Outside twin` |
| `cabin_class_code` | Operator cabin class code. | string | `OA2` |
| `class_type` | Class type associated with the cabin. | string | `outside` |
| `number_of_beds` | Number of beds in the cabin. | unsigned integer | `2` |
| `bed_position` | Assigned bed position within the cabin. | string | `lower` |
| `male_beds` | Number of male beds allocated, where the operator uses that split. | unsigned integer | `1` |
| `female_beds` | Number of female beds allocated, where the operator uses that split. | unsigned integer | `1` |

A change of gate after issuance SHALL NOT by itself invalidate the credential.
The operator SHOULD communicate a new gate outside this mdoc. The reader
SHALL NOT refuse a credential only because `departure_gate` is absent or no
longer matches the gate where the passenger presents it.

### 2.5 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `departure_gate` | SHOULD be present when a gate is assigned at issuance and the holder needs it to find the gate. | string | `RFN-GATE-02` |
| `reservation_number` | SHOULD be present when the operator's reservation number is not the same value as `ticket_number`. | string | `RES-2026-000991` |
| `discount` | SHOULD be present only when a verified discount or fare basis was applied. | string | `student` |
| Cabin elements | `cabin_number`, `cabin_class_description`, `cabin_class_code`, `class_type`, `number_of_beds`, `bed_position`, `male_beds` and `female_beds` SHALL be omitted when no cabin is allocated. Any of them MAY be present when a cabin is booked. An absent cabin element means that value was not issued. It SHALL NOT be encoded as null. | string or unsigned integer | `C-204` |

The credential SHALL NOT include:

- PID attributes other than the ticketed name in `first_name` and `last_name`;
- a portrait or other biometric;
- payment data; or
- the Vehicle Ferry Boarding Credential.

### 2.6 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `category` | Legal category of the attestation. See §2.3. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the credential issuer, such as the ferry operator or an authorised ticketing system. | string or URI | `https://issuer.example-ferry.gr` |
| `credential_type` | Encoding-independent credential type identifier. SHALL equal the `docType`. | string | `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1` |
| `issued_at` | Credential issuance time. Carried as `validityInfo.signed`. | date-time | `2026-06-01T10:00:00+03:00` |
| `valid_from` | Beginning of the acceptance window. Carried as `validityInfo.validFrom`. | date-time | `2026-06-01T10:00:00+03:00` |
| `expires_at` | End of the acceptance window. Carried as `validityInfo.validUntil`. | date-time | `2026-06-15T07:30:00+03:00` |
| `trust_anchor_reference` | Location of issuer trust information provisioned to gate readers. | URI | `https://trust.example.eu/ferry/operators/fast-ferries` |

The ferry operator and the authorised ticketing system MAY be the same entity.
An authorised issuer acting for the operator satisfies `issuer`.

### 2.7 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `credential_name` | Human-readable credential name. SHALL be `Passenger Ferry Boarding Credential`. | string | `Passenger Ferry Boarding Credential` |
| `credential_description` | Wallet-facing description. | string | `Rafina–Milos, 15 June 2026, 07:30` |
| `issuer_name` | Human-readable operator or issuer name. | string | `Fast Ferries` |
| `issuer_logo_uri` | Issuer logo URI. | URI | `https://issuer.example-ferry.gr/logo.png` |
| `privacy_notice` | Privacy-notice URI. | URI | `https://issuer.example-ferry.gr/privacy` |
| `display_locale` | Preferred display language. | string | `en` |
| `status_reference` | Operational status pointer for a reader that can reach the issuer. Not an mdoc data element and not a Mobile Security Object field. | URI or structured value | `https://status.example-ferry.gr/passenger-boarding/000123456` |

`status_reference` is not carried in the mdoc. ISO/IEC 18013-5:2021 does not
put a status list in the Mobile Security Object. An offline reader SHALL rely
on `validityInfo` and the disclosed journey elements.

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes** |
| -------------- | ------------------ | ----------- | ----------------------- | --------- |
| `credential_type` | `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1` | Credential type identifier. | This Rulebook | SHALL equal the `docType`. |
| `category` | `eaa:eu:non-qualified`, `eaa:eu:qualified` | Legal category. | This Rulebook | The pilot value is `eaa:eu:non-qualified`. |
| `departure_date` / `arrival_date` | ISO 8601 date | Scheduled local date. | ISO 8601 | `YYYY-MM-DD`. |
| `departure_time` / `arrival_time` | `HH:MM` or `HH:MM:SS` | Scheduled local port time. | This Rulebook | Not a zoned instant. |
| `departure_port` / `arrival_port` | Port identifier | Port. | UN/LOCODE recommended | An operator code MAY be used in the pilot. |
| `seat_type` | Issuer-defined seating code | Seat or product type. | Ferry operator vocabulary | Examples include `AIR_SEAT`, `DECK`, `CABIN`. |
| `discount` | Issuer-defined discount code | Applied fare basis or discount. | Ferry operator tariff vocabulary | Examples include `student`, `loyalty`, `child`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Behaviour on failure** |
| ----------- | ------------------ | ----------------- | ------------------ | ------------------------ |
| `PBP-IR-01` | `arrival_date` SHALL NOT precede `departure_date`. | Prevents a journey that runs backwards. | Issuer, before signing. | Issuer SHALL NOT issue the mdoc. |
| `PBP-IR-02` | The credential SHALL describe one journey and one passenger. | Prevents reuse across sailings or passengers. | Issuer. The reader checks the disclosed sailing against the gate. | Reader SHALL refuse when it cannot determine that sailing or passenger. |
| `PBP-IR-03` | The credential SHALL NOT be accepted after `validityInfo.validUntil`. | Boarding entitlement ends at departure, plus only a defined grace period. | Reader, against its clock. | Reader SHALL refuse. |
| `PBP-IR-04` | `docType` SHALL equal `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`. | Identifies this attestation type. | Reader. | Reader SHALL refuse any other `docType`. |
| `PBP-IR-05` | `ticket_let` and `ticket_number` SHALL be non-empty. | The gate needs a ticket identifier. | Issuer, before signing. | Issuer SHALL NOT issue the mdoc. |
| `PBP-IR-06` | Cabin elements SHALL be omitted when no cabin is allocated. | A seat-only ticket must not imply a cabin. | Issuer, before signing. | Issuer SHALL omit them. A reader SHOULD refuse a cabin element that contradicts a non-cabin `seat_type` where the operator defines that contradiction. |
| `PBP-IR-07` | Where the gate matches identity, `first_name` and `last_name` SHOULD be compared with PID. | The person at the gate is the passenger on the ticket. | Reader, as a separate check from mdoc verification. | Reader SHOULD refuse embarkation when that match fails. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The Passenger Ferry Boarding Credential SHALL be issued as an ISO/IEC 18013-5
mdoc. The issued object is an `IssuerSigned` structure as defined in that
standard. ISO/IEC 18013-5 does not define how a credential is issued. Where
OpenID4VCI is used, the credential format SHALL be `mso_mdoc`.

Presentation SHALL use ISO/IEC 18013-5 device engagement and device retrieval.
Those steps are separate. Device engagement SHALL be by QR code or NFC.
Device retrieval SHALL be by BLE or NFC, as the gate reader offers. BLE is a
retrieval transport. It is not a device-engagement method.

#### 3.1.1 Document type and namespace

The `docType` SHALL be:

```text
eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1
```

The namespace for the data elements in §3.1.2 SHALL be:

```text
eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1
```

`docType` and the namespace are the same reverse-domain identifier. The
withdrawn version 0.3 type `PassengerBoardingCredential` SHALL NOT be used as
the `docType`, the namespace, or an SD-JWT `vct` for this credential.

#### 3.1.2 Data elements

| **Data Identifier** | **Element identifier** | **Encoding** | **Presence** |
| ------------------- | ---------------------- | ------------ | ------------ |
| `id` | `id` | tstr | M |
| `category` | `category` | tstr | M |
| `departure_date` | `departure_date` | tstr | M |
| `departure_time` | `departure_time` | tstr | M |
| `departure_port` | `departure_port` | tstr | M |
| `arrival_date` | `arrival_date` | tstr | M |
| `arrival_time` | `arrival_time` | tstr | M |
| `arrival_port` | `arrival_port` | tstr | M |
| `first_name` | `first_name` | tstr | M |
| `last_name` | `last_name` | tstr | M |
| `ticket_let` | `ticket_let` | tstr | M |
| `ticket_number` | `ticket_number` | tstr | M |
| `seat_type` | `seat_type` | tstr | M |
| `seat_number` | `seat_number` | tstr | M |
| `departure_gate` | `departure_gate` | tstr | O |
| `vessel_description` | `vessel_description` | tstr | O |
| `reservation_number` | `reservation_number` | tstr | O |
| `discount` | `discount` | tstr | O |
| `cabin_number` | `cabin_number` | tstr | C |
| `cabin_class_description` | `cabin_class_description` | tstr | C |
| `cabin_class_code` | `cabin_class_code` | tstr | C |
| `class_type` | `class_type` | tstr | C |
| `number_of_beds` | `number_of_beds` | uint | C |
| `bed_position` | `bed_position` | tstr | C |
| `male_beds` | `male_beds` | uint | C |
| `female_beds` | `female_beds` | uint | C |

Presence `M` means the element SHALL be present in `issuerSigned.nameSpaces`.
Presence `O` means the element MAY be present. Presence `C` means the element
SHALL be omitted when no cabin is allocated, and MAY be present when a cabin
is booked.

`category` SHALL be `eaa:eu:non-qualified` or `eaa:eu:qualified`.

Version 0.3 nested JSON paths map to these element identifiers as follows.
The nested paths are not used in the mdoc.

| **Version 0.3 path** | **Element identifier** |
| -------------------- | ---------------------- |
| `attestation_legal_category` | `category` |
| `departure.date` | `departure_date` |
| `departure.time` | `departure_time` |
| `departure.port` | `departure_port` |
| `departure.gate` | `departure_gate` |
| `arrival.date` | `arrival_date` |
| `arrival.time` | `arrival_time` |
| `arrival.port` | `arrival_port` |
| `passenger.firstName` | `first_name` |
| `passenger.lastName` | `last_name` |
| `ticket.ticketLet` | `ticket_let` |
| `ticket.ticketNumber` | `ticket_number` |
| `ticket.discount` | `discount` |
| `accommodation.seatType` | `seat_type` |
| `accommodation.seatNumber` | `seat_number` |
| `accommodation.cabinNumber` | `cabin_number` |
| `accommodation.cabinClassDescription` | `cabin_class_description` |
| `accommodation.cabinClassCode` | `cabin_class_code` |
| `accommodation.classType` | `class_type` |
| `accommodation.numberOfBeds` | `number_of_beds` |
| `accommodation.bedPosition` | `bed_position` |
| `accommodation.maleBeds` | `male_beds` |
| `accommodation.femaleBeds` | `female_beds` |
| `vesselDescription` | `vessel_description` |
| `reservationNumber` | `reservation_number` |

Each issued element SHALL be carried as an `IssuerSignedItem` under the
namespace in §3.1.1. The item SHALL be encoded as a CBOR tag 24 byte string,
as defined in ISO/IEC 18013-5, and SHALL contain:

- `digestID`, an unsigned integer unique within the namespace;
- `random`, a byte string of at least 16 bytes;
- `elementIdentifier`; and
- `elementValue`.

The digest in the Mobile Security Object SHALL be computed over the
deterministic CBOR encoding of the `IssuerSignedItem`, as specified in
ISO/IEC 18013-5. `elementValue` SHALL be a UTF-8 text string (`tstr`), except
`number_of_beds`, `male_beds` and `female_beds`, whose `elementValue` SHALL be
an unsigned integer (`uint`).

The reader requests the elements it needs. Elements the reader does not
request are not disclosed in the `DeviceResponse`. The reader SHALL request
only the elements required for the boarding decision. A boarding decision
SHALL request the mandatory journey, name, ticket and seat elements. It
SHALL NOT request cabin elements when the passenger has no cabin, and it
SHALL NOT request `discount` unless the decision uses the fare basis.

#### 3.1.3 Mobile Security Object

`issuerAuth` SHALL be a `COSE_Sign1` whose payload is the Mobile Security
Object, wrapped as a CBOR tag 24 byte string, as defined in ISO/IEC 18013-5.

The Mobile Security Object SHALL include:

- `version` with the value `1.0`;
- `digestAlgorithm` set to `SHA-256`, `SHA-384` or `SHA-512`;
- `docType` equal to `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`;
- `valueDigests` for the namespace in §3.1.1, with one digest for every issued
  `IssuerSignedItem`;
- `deviceKeyInfo.deviceKey`, a COSE key of the Wallet; and
- `validityInfo.signed`, `validityInfo.validFrom` and `validityInfo.validUntil`,
  each a CBOR tag 0 date-time (`tdate`).

`validityInfo.validFrom` and `validityInfo.validUntil` are the acceptance
window the gate reader checks offline. A reader SHALL reject an mdoc when its
clock is before `validFrom` or after `validUntil`.

`validUntil` SHALL NOT be later than the scheduled departure unless the
operator defines a short grace period. That grace period SHALL be reflected
in `validUntil` at issuance. The reader does not invent a grace period of
its own.

The issuer SHALL sign `issuerAuth` with a signature algorithm permitted by
ISO/IEC 18013-5. The example in §3.1.5 uses ES256 (COSE algorithm identifier
-7).

Device authentication is not part of `issuerAuth`. During presentation the
Wallet SHALL authenticate the `DeviceResponse` with a device signature or a
device MAC, as defined in ISO/IEC 18013-5, bound to the `SessionTranscript`.

#### 3.1.4 CDDL

```cddl
passenger_ferry_boarding_elements = {
  "id": tstr,
  "category": tstr,
  "departure_date": tstr,
  "departure_time": tstr,
  "departure_port": tstr,
  "arrival_date": tstr,
  "arrival_time": tstr,
  "arrival_port": tstr,
  "first_name": tstr,
  "last_name": tstr,
  "ticket_let": tstr,
  "ticket_number": tstr,
  "seat_type": tstr,
  "seat_number": tstr,
  ? "departure_gate": tstr,
  ? "vessel_description": tstr,
  ? "reservation_number": tstr,
  ? "discount": tstr,
  ? "cabin_number": tstr,
  ? "cabin_class_description": tstr,
  ? "cabin_class_code": tstr,
  ? "class_type": tstr,
  ? "number_of_beds": uint,
  ? "bed_position": tstr,
  ? "male_beds": uint,
  ? "female_beds": uint
}
```

Each entry is issued as an `IssuerSignedItem` per ISO/IEC 18013-5: a CBOR tag
24 byte string of `{ "digestID": uint, "random": bstr, "elementIdentifier": tstr, "elementValue": tstr / uint }`,
with `random` at least 16 bytes long. The `COSE_Sign1` payload is the Mobile
Security Object, also as a CBOR tag 24 byte string. `validityInfo` dates are
CBOR tag 0 date-times.

#### 3.1.5 Illustrative issuer-signed structure

The structure below is the issued `issuerSigned` content for a seat-only
ticket, shown inside the `docType` used on a `DeviceResponse` document.
`deviceSigned` is produced at presentation and is omitted here. Digest
values, the certificate and the signature are placeholders. `validityInfo`
dates use CBOR tag 0. Optional and cabin elements are absent from this
example. A cabin booking adds those `IssuerSignedItem` values and their
digests in the same namespace.

```cbor-diag
{
  "docType": "eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1",
  "issuerSigned": {
    "nameSpaces": {
      "eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1": [
        24(<<{
          "digestID": 0,
          "random": h'7F9C2BA4E88F827D616045507605853E',
          "elementIdentifier": "id",
          "elementValue": "1ddcf8dc-3f0b-4b30-987d-5eacb9dba111"
        }>>),
        24(<<{
          "digestID": 1,
          "random": h'0D61F8370CAD1D412F80B84D143E1257',
          "elementIdentifier": "category",
          "elementValue": "eaa:eu:non-qualified"
        }>>),
        24(<<{
          "digestID": 2,
          "random": h'F1D3FF8443297732862DF21DC4E57262',
          "elementIdentifier": "departure_date",
          "elementValue": "2026-06-15"
        }>>),
        24(<<{
          "digestID": 3,
          "random": h'A1B2C3D4E5F60718293A4B5C6D7E8F90',
          "elementIdentifier": "departure_time",
          "elementValue": "07:30"
        }>>),
        24(<<{
          "digestID": 4,
          "random": h'00112233445566778899AABBCCDDEEFF',
          "elementIdentifier": "departure_port",
          "elementValue": "GRRFN"
        }>>),
        24(<<{
          "digestID": 5,
          "random": h'FFEEDDCCBBAA99887766554433221100',
          "elementIdentifier": "arrival_date",
          "elementValue": "2026-06-15"
        }>>),
        24(<<{
          "digestID": 6,
          "random": h'0123456789ABCDEFFEDCBA9876543210',
          "elementIdentifier": "arrival_time",
          "elementValue": "12:45"
        }>>),
        24(<<{
          "digestID": 7,
          "random": h'89ABCDEF0123456789ABCDEF01234567',
          "elementIdentifier": "arrival_port",
          "elementValue": "GRMLO"
        }>>),
        24(<<{
          "digestID": 8,
          "random": h'1112131415161718191A1B1C1D1E1F20',
          "elementIdentifier": "first_name",
          "elementValue": "Nikos"
        }>>),
        24(<<{
          "digestID": 9,
          "random": h'2122232425262728292A2B2C2D2E2F30',
          "elementIdentifier": "last_name",
          "elementValue": "Triantafyllou"
        }>>),
        24(<<{
          "digestID": 10,
          "random": h'3132333435363738393A3B3C3D3E3F40',
          "elementIdentifier": "ticket_let",
          "elementValue": "A"
        }>>),
        24(<<{
          "digestID": 11,
          "random": h'4142434445464748494A4B4C4D4E4F50',
          "elementIdentifier": "ticket_number",
          "elementValue": "000123456"
        }>>),
        24(<<{
          "digestID": 12,
          "random": h'5152535455565758595A5B5C5D5E5F60',
          "elementIdentifier": "seat_type",
          "elementValue": "AIR_SEAT"
        }>>),
        24(<<{
          "digestID": 13,
          "random": h'6162636465666768696A6B6C6D6E6F70',
          "elementIdentifier": "seat_number",
          "elementValue": "12A"
        }>>)
      ]
    },
    "issuerAuth": [
      h'A10126',
      { 33: [ h'308201AA...ISSUER_LEAF_CERT_DER...' ] },
      24(<<{
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "docType": "eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1",
        "valueDigests": {
          "eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1": {
            0: h'1111111111111111111111111111111111111111111111111111111111111111',
            1: h'2222222222222222222222222222222222222222222222222222222222222222',
            2: h'3333333333333333333333333333333333333333333333333333333333333333',
            3: h'4444444444444444444444444444444444444444444444444444444444444444',
            4: h'5555555555555555555555555555555555555555555555555555555555555555',
            5: h'6666666666666666666666666666666666666666666666666666666666666666',
            6: h'7777777777777777777777777777777777777777777777777777777777777777',
            7: h'8888888888888888888888888888888888888888888888888888888888888888',
            8: h'9999999999999999999999999999999999999999999999999999999999999999',
            9: h'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            10: h'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
            11: h'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
            12: h'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
            13: h'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
          }
        },
        "deviceKeyInfo": {
          "deviceKey": {
            1: 2,
            -1: 1,
            -2: h'6C8F25B6C9A7B3E4F19D2A5C7E9B11223344556677889900AABBCCDDEEFF0011',
            -3: h'7D9E36C7DA8BC4F20A1B2C3D4E5F60718293A4B5C6D7E8F90123456789ABCDEF'
          }
        },
        "validityInfo": {
          "signed": 0("2026-06-01T10:00:00+03:00"),
          "validFrom": 0("2026-06-01T10:00:00+03:00"),
          "validUntil": 0("2026-06-15T07:30:00+03:00")
        }
      }>>),
      h'5F8D3C2A1B0099EE...SIGNATURE...'
    ]
  }
}
```

#### 3.1.6 Wallet display

The Wallet Unit SHOULD display:

```text
Passenger Ferry Boarding Credential
Rafina (GRRFN) – Milos (GRMLO)
15 June 2026, 07:30
Nikos Triantafyllou
Seat: 12A
Ticket: A 000123456
Valid until: 15 June 2026, 07:30
```

When a cabin is issued, the Wallet Unit SHOULD also display `cabin_number`.

The Wallet Unit SHOULD inform the User that:

- this credential is presented at the boarding gate with ISO/IEC 18013-5
  device engagement and device retrieval;
- the User can refuse presentation; and
- a staff-assisted boarding process remains available where ferry policy
  allows it.

### 3.2 SD-JWT VC-based encoding

This version does not define an SD-JWT VC representation.

The withdrawn version 0.3 profile (`vct` `PassengerBoardingCredential`, with
nested `departure`, `arrival`, `passenger`, `ticket` and `accommodation`
objects) SHALL NOT be issued as a Passenger Ferry Boarding Credential.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM representation.

## 4 Attestation usage

### 4.1 Issuance trigger

The Passenger Ferry Boarding Credential SHALL be issued only after:

1. a passenger booking exists for one sailing;
2. the ticketed name, ticket identifier and seat information are known; and
3. the User has consented to receive the credential.

Issuance MAY happen at booking time. It does not require the passenger to be
at the port.

The same entity MAY operate ticketing and issue this credential.

### 4.2 Issuer

The credential SHALL be issued by:

- the ferry operator; or
- an authorised ticketing system acting for that operator.

The issuer is the authentic source for this boarding entitlement. A party
that only resells the ticket SHOULD NOT issue the credential unless the
operator has explicitly authorised it to do so.

### 4.3 Device binding

The credential SHALL be device-bound.

The Mobile Security Object SHALL contain `deviceKeyInfo.deviceKey`. During
presentation the Wallet SHALL provide device authentication as defined in
ISO/IEC 18013-5, bound to the `SessionTranscript`. A reader SHALL NOT accept
an `IssuerSigned` structure that is not carried in a `DeviceResponse`
authenticated for that session.

### 4.4 Wallet disclosure and consent

Before issuance, the Wallet SHOULD display:

- operator or issuer name;
- departure and arrival ports;
- departure date and time;
- the ticketed passenger name;
- ticket identifier and seat, and cabin where issued;
- that the credential is presented with ISO/IEC 18013-5 device engagement and
  device retrieval; and
- the validity window.

### 4.5 Presentation at the boarding gate

A normal use SHOULD follow these steps:

1. the Wallet and the gate reader perform ISO/IEC 18013-5 device engagement
   by QR code or NFC;
2. they establish an encrypted session and retrieve data over BLE or NFC, as
   the reader offers;
3. the reader sends a `DeviceRequest` for `docType`
   `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`, requesting the
   elements required for the boarding decision from that same namespace;
4. the Wallet obtains the User's consent and returns a `DeviceResponse`;
5. the reader verifies `issuerAuth`, the `IssuerSignedItem` digests, device
   authentication and `validityInfo`, as specified in §4.7;
6. the reader checks that `departure_port`, `departure_date` and
   `departure_time` are the sailing this gate is boarding;
7. where identity matching applies, the reader compares `first_name` and
   `last_name` with PID as specified in §4.6;
8. the reader allows embarkation or refuses; and
9. a minimal event MAY be recorded when the reader can store or forward one.

The reader SHALL perform mdoc verification locally. It SHALL NOT require a
live ticketing lookup in order to accept the credential.

The boarding context is the sailing this gate is operating: its departure
port, date and time. Passenger matching, when policy requires it, is a
comparison of the disclosed ticketed name with PID. It is not a field inside
this mdoc.

A minimal event MAY contain a pseudonymous credential reference (`id`), a
timestamp, a result, a reason code and a reader identifier. It SHOULD NOT
contain PID attributes beyond what the event already needs, the device key,
the Mobile Security Object, or payment data.

### 4.6 Identity matching

mdoc verification and identity matching are separate.

When the gate matches the person to the ticket, the reader SHOULD request
`first_name` and `last_name` from this credential and the minimum PID
attributes needed for the comparison. The reader SHALL request only those
attributes.

This Rulebook does not define a cryptographic binding between this credential
and PID. The gate compares the disclosed values. The names are not taken from
a travel document at presentation time.

### 4.7 Verifier obligations

The gate reader SHALL:

1. complete ISO/IEC 18013-5 device engagement and encrypted device retrieval;
2. decrypt and parse the `DeviceResponse`;
3. confirm that the document `docType` and the Mobile Security Object
   `docType` are both `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`;
4. verify the `issuerAuth` `COSE_Sign1` and the issuer certificate chain
   against a trust anchor provisioned for this operator;
5. recompute the digest of each disclosed `IssuerSignedItem` and match it to
   `valueDigests` for that `digestID`;
6. verify device authentication, either a device signature or a device MAC,
   against the `SessionTranscript` and the `deviceKey` in the Mobile Security
   Object;
7. verify `validityInfo` against the reader's clock;
8. confirm that the disclosed `departure_port`, `departure_date` and
   `departure_time` match the sailing this gate is boarding;
9. confirm that a requested mandatory element was disclosed;
10. apply `PBP-IR-01` to the disclosed dates;
11. where the reader has connectivity and a status source is available, reject
    a revoked or suspended credential; and
12. allow embarkation only when these checks succeed.

A missing requested element, a digest mismatch or a `docType` mismatch SHALL
be a refusal.

A reader SHALL NOT accept a credential for another operator only because the
same vendor operates both gates.

A reader SHALL NOT treat a missing status list as a failure. Status is not a
field of this mdoc.

### 4.8 Failure and fallback

The reader SHALL refuse embarkation on the strength of this credential when:

- device engagement or device retrieval fails;
- `issuerAuth`, a data-element digest or device authentication fails;
- the reader does not trust the issuer for this operator;
- the current time is outside `validityInfo`;
- the credential is revoked or suspended and the reader can determine that;
- the disclosed sailing is not the sailing this gate is boarding;
- a requested mandatory element is missing; or
- required identity matching fails.

The operator SHALL keep a staff-assisted boarding path where ferry policy
allows it. Refusal of the mdoc SHALL NOT by itself close that path.

## 5 Trust anchors

The gate reader SHALL establish that the issuer:

1. is the ferry operator or an authorised ticketing system acting for it;
2. is authorised to issue Passenger Ferry Boarding Credentials for this
   operator;
3. uses a certificate chain the reader has been provisioned to trust; and
4. was authorised at issuance, as carried by that chain.

Readers for the APTITUDE pilot SHOULD obtain that trust information through
the WP2 trust framework. An offline reader uses the trust anchors provisioned
to it. It does not fetch them during the presentation.

A credential issued for one operator SHALL NOT be accepted by another
operator merely because the same vendor operates both systems.

## 6 Revocation and status

### 6.1 Validity period

The credential SHALL be short-lived and limited to one journey.

`validityInfo.validFrom` SHOULD be no earlier than issuance. It MAY be the
start of the boarding window where the operator wants the credential refused
before that window.

`validityInfo.validUntil` SHALL be no later than the scheduled departure,
plus only a limited grace period where the operator defines one. The grace
period is set at issuance. A reader SHALL NOT add one.

This window is the time control an offline reader can enforce. After
`validUntil`, the reader SHALL NOT accept the credential for boarding.

### 6.2 Revocation and suspension triggers

The issuer SHOULD revoke, suspend or replace the credential when:

- the ticket is cancelled, refunded or exchanged;
- the passenger on the booking is replaced;
- the sailing, ports or departure time change;
- the device is lost or compromised;
- the credential was issued in error; or
- the issuer is no longer authorised.

A successful presentation SHALL NOT by itself revoke the credential. The
passenger may be checked again before departure. Revocation on first use is
not this profile.

A gate change SHALL NOT by itself be a revocation trigger.

### 6.3 Offline readers and status

An offline reader SHALL enforce `validityInfo` and the disclosed journey
elements, and SHALL NOT depend on a live status service. ISO/IEC 18013-5:2021
verification does not itself fetch a status list. Checking status is a
profile rule for a reader that has connectivity and a status source.

A reader that has connectivity SHALL check the issuer's status information
and SHALL reject a suspended or revoked credential even when `validUntil` has
not passed.

Until `validUntil`, a reader which has not received revocation may still
accept the credential. Cancellation handling therefore SHOULD combine
revocation with as short a `validUntil` as the sailing allows, and with the
staff path in §4.8.

## 7 Compliance

This Rulebook is designed to align with:

- Regulation (EU) 2024/1183;
- the EUDI Wallet Architecture and Reference Framework;
- ARF Annex 2 Topic 12;
- ISO/IEC 18013-5 for the mdoc, including `IssuerSigned`, the Mobile Security
  Object, device engagement by QR code or NFC, and device retrieval by BLE or
  NFC;
- OpenID4VCI where the issuance transport is OpenID4VCI;
- applicable GDPR requirements; and
- the SEDIT-X Ferry Transport source material.

The Rulebook enforces:

1. one passenger and one journey per credential;
2. separation from the Vehicle Ferry Boarding Credential, the mVRC, PID and
   payment;
3. Wallet display name **Passenger Ferry Boarding Credential** and `docType`
   `eu.europa.ec.eudi.aptitude.passenger_ferry_boarding.1`;
4. the data elements in §3.1.2, with cabin elements omitted when no cabin is
   booked;
5. ISO/IEC 18013-5 device engagement (QR code or NFC) and device retrieval
   (BLE or NFC), verified at the gate;
6. device authentication bound to the `SessionTranscript`;
7. a signed validity window that an offline reader can enforce, together with
   a match of the disclosed sailing to the gate;
8. revocation on cancellation or passenger change, applied by readers that can
   see status, and no revocation merely because the credential was presented;
9. minimal event logging; and
10. a staff-assisted fallback where ferry policy allows it.

The following matters remain open and require operator input:

- confirmation of the `docType`, namespace and data elements against the
  operator's ticketing profile, where that profile assigns different
  identifiers;
- how gate readers are provisioned with issuer trust anchors;
- the status mechanism an online reader uses;
- the length of any post-departure grace period; and
- whether a ferry boarding-pass data standard, analogous to an IATA boarding
  pass, should replace these element identifiers.

This version does not define an SD-JWT VC or a W3C VCDM encoding. No IATA
boarding-pass standard is adopted here.

## 8 References

| **Item Reference** | **Standard name/details** |
| ------------------ | ------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [ISO/IEC 18013-5] | Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application. mdoc structure, device engagement (QR code, NFC) and device retrieval (BLE, NFC). |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X Ferry Working Paper] | APTITUDE WP4, SEDIT-X Ferry Transport, Version 0.1, May 2026 |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 8610] | Concise Data Definition Language (CDDL) |
| [RFC 8949] | Concise Binary Object Representation (CBOR) |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes; building blocks and general requirements |
