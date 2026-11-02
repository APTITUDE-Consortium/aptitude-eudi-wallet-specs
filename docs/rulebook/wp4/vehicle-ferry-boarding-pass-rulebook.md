# Attestation Rulebook for attestations of type Vehicle Ferry Boarding Credential

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date       | Description                                                                                                                                                                                                 |
| ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Ferry Transport working paper and the APTITUDE Attestation Rulebook template.                                                                                            |
| 0.2     | 24-07-2026 | Simplified structure aligned with the passenger Ferry Boarding Pass model.                                                                                                                                  |
| 0.3     | 24-07-2026 | SD-JWT claim model aligned with the Vehicle Boarding Credential JSON Schema. Withdrawn as the encoding by version 0.4.                                                                                      |
| 0.4     | 02-11-2026 | Replaces the SD-JWT encoding with an ISO/IEC 18013-5 mdoc. `docType` is `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`. The lane verifies the `DeviceResponse` offline.                             |

**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the **Vehicle Ferry Boarding Credential**. The Wallet
> display name is **Vehicle Ferry Boarding Credential**. The credential type
> identifier, mdoc `docType` and namespace are
> `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`.
>
> The credential is an **ISO/IEC 18013-5 mdoc**. The Wallet presents it with
> that standard's device engagement and device retrieval. The vehicle-lane
> reader verifies the `DeviceResponse` offline and uses the result to decide
> whether the vehicle may embark.
>
> Version 0.3, an SD-JWT VC with `vct` `VehicleBoardingCredential` and nested
> `departure`, `arrival`, `vehicle` and `ticket` objects, is withdrawn as the
> encoding. This credential SHALL NOT be issued as an SD-JWT VC.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Vehicle Ferry Boarding Credential**, a short-lived
Electronic Attestation of Attributes for the European Digital Identity Wallet.

The credential type identifier is:

```text
eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1
```

The Wallet display name is **Vehicle Ferry Boarding Credential**.

The credential expresses the fact that one vehicle is entitled to board one
ferry journey at a scheduled departure. A journey is one sailing: one
departure port, one arrival port, and one scheduled departure date and time.

The attestation is issued by an authentic source, such as a ferry operator or
an authorised ticketing system acting for that operator. The Holder is the
passenger who holds the vehicle booking. The verifier is the vehicle-lane
reader, or boarding staff using such a reader, at the departure port.

The credential MAY be used to:

- present vehicle boarding entitlement at a lane reader that supports
  ISO/IEC 18013-5 device engagement and device retrieval;
- show the holder the sailing, vehicle and ticket in the Wallet; and
- let the operator accept the vehicle without a live ticketing lookup, when
  the reader can verify the mdoc from provisioned trust anchors.

The credential SHALL NOT be treated as:

- the passenger **Ferry Boarding Pass**, which is the passenger's own boarding
  right;
- the **mVRC**, which provides the vehicle-registration attributes;
- **PID**; or
- a payment confirmation or eReceipt.

Where the lane must match the vehicle to the ticket, this credential SHOULD be
presented together with the minimum required mVRC attributes. Where policy
also requires the person, the lane SHOULD request the passenger Ferry Boarding
Pass and PID. Those are separate presentations. This mdoc does not embed them.

### 1.2 Architectural role

The mdoc is what the lane verifies. A reader that has no network connection
SHALL be able to decide using:

- issuer authentication (`issuerAuth` over the Mobile Security Object);
- the digests of the disclosed data elements;
- device authentication bound to the `SessionTranscript`;
- `validityInfo` in the Mobile Security Object; and
- a match between the disclosed journey and vehicle elements and the sailing
  this lane is boarding.

The operator's ticketing system remains authoritative for the booking. A
reader with connectivity SHOULD apply revocation and status. A reader without
connectivity relies on the signed validity window and the disclosed journey
elements, and SHALL NOT refuse an otherwise valid mdoc only because it cannot
reach the ticketing system.

`validityInfo` is the acceptance window. It does not by itself identify the
sailing. The reader SHALL still match `departure_port`, `departure_date` and
`departure_time` to the sailing it is boarding.

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

- **Vehicle Ferry Boarding Credential** means the mdoc whose `docType` is
  `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`.
- **Journey** means one ferry sailing between a departure port and an arrival
  port at a scheduled date and time.
- **Ferry operator** means the organisation operating that sailing, or the
  authentic source for the vehicle boarding entitlement.
- **Authorised ticketing system** means a system the ferry operator authorises
  to issue this credential.
- **mVRC** means the Mobile Vehicle Registration Credential. It provides
  vehicle-registration attributes. This credential does not replace it.
- **Lane reader** means the mdoc reader at the vehicle boarding lane or port
  gate. It performs ISO/IEC 18013-5 device engagement and device retrieval and
  decides whether the vehicle may embark.
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

1. **One vehicle, one journey.** The credential SHALL describe a single
   vehicle and a single sailing. It SHALL NOT be reused for another sailing,
   vessel, date or vehicle.
2. **mdoc boarding credential.** The credential SHALL be an ISO/IEC 18013-5
   mdoc. Presentation SHALL use device engagement and device retrieval as
   defined in that standard.
3. **Offline verification.** A lane reader SHALL be able to verify the
   credential without a live call to the ticketing system.
4. **Minimum disclosure.** The data elements SHALL be limited to the sailing,
   the vehicle category, the ticket identifier and, where the lane matches the
   vehicle, the plate number.
5. **No payment data.** The credential SHALL NOT carry a payment confirmation,
   card number or eReceipt.
6. **Device binding.** The Mobile Security Object SHALL contain the Wallet
   `deviceKey`. The reader SHALL verify ISO/IEC 18013-5 device authentication
   bound to the `SessionTranscript`.
7. **Short validity.** `validityInfo.validUntil` SHALL be no later than the
   scheduled departure, plus only a limited grace period where the operator
   defines one.
8. **Separate credentials.** Passenger boarding, vehicle registration and
   payment remain other attestations. This credential SHOULD NOT duplicate the
   mVRC.
9. **Fallback.** Staff-assisted boarding SHALL remain available where ferry
   policy allows it. Failure of wallet verification SHALL NOT by itself remove
   that path.

### 2.3 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `id` | Unique identifier of this credential instance. | string | `2aacf8dc-3f0b-4b30-987d-5eacb9dba222` |
| `category` | Legal category. Either `eaa:eu:non-qualified` or `eaa:eu:qualified`. | string | `eaa:eu:non-qualified` |
| `departure_date` | Scheduled departure date at the departure port. | date | `2026-06-15` |
| `departure_time` | Scheduled departure time at the departure port, local port time, `HH:MM` or `HH:MM:SS`. | string | `07:30` |
| `departure_port` | Departure port identifier. UN/LOCODE is recommended. | string | `GRRFN` |
| `arrival_date` | Scheduled arrival date at the arrival port. | date | `2026-06-15` |
| `arrival_time` | Scheduled arrival time at the arrival port, local port time, `HH:MM` or `HH:MM:SS`. | string | `12:45` |
| `arrival_port` | Arrival port identifier. UN/LOCODE is recommended. | string | `GRMLO` |
| `vehicle_type` | Human-readable ferry vehicle category. | string | `Passenger Car` |
| `vehicle_type_code` | Operator or tariff code for that category. | string | `PC` |
| `ticket_let` | Ticket letter, class code or other operator classification. | string | `V` |
| `ticket_number` | Ferry vehicle-ticket number. | string | `000123456` |

These attributes SHALL be present.

`departure_date` and `arrival_date` SHALL use `YYYY-MM-DD`. The times are
local port time, not an instant with a numeric offset. The acceptance window
the reader enforces is `validityInfo`, which does carry a date-time.

### 2.4 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `departure_gate` | Departure gate, lane or boarding area, when known at issuance. | string | `RFN-LANE-02` |
| `vessel_description` | Name or description of the ferry vessel. | string | `Fast Ferries Andros` |
| `reservation_number` | Booking number, when the operator uses one distinct from `ticket_number`. | string | `RES-2026-000991` |
| `plate_number` | Registration mark of the vehicle entitled to board. | string | `NIK-1234` |

### 2.5 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `plate_number` | SHALL be present when the lane matches the vehicle to the ticket by plate. MAY be omitted when vehicle binding is established by other means under ferry policy. | string | `NIK-1234` |
| `departure_gate` | SHOULD be present when a gate or lane is assigned at issuance and the holder needs it to find the lane. | string | `RFN-LANE-02` |
| `reservation_number` | SHOULD be present when the operator's reservation number is not the same value as `ticket_number`. | string | `RES-2026-000991` |

The credential SHALL NOT include:

- PID attributes;
- a full copy of the mVRC;
- payment data; or
- the passenger Ferry Boarding Pass.

### 2.6 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `category` | Legal category of the attestation. See §2.3. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the credential issuer, such as the ferry operator or an authorised ticketing system. | string or URI | `https://issuer.example-ferry.gr` |
| `credential_type` | Encoding-independent credential type identifier. SHALL equal the `docType`. | string | `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1` |
| `issued_at` | Credential issuance time. Carried as `validityInfo.signed`. | date-time | `2026-06-01T10:00:00+03:00` |
| `valid_from` | Beginning of the acceptance window. Carried as `validityInfo.validFrom`. | date-time | `2026-06-01T10:00:00+03:00` |
| `expires_at` | End of the acceptance window. Carried as `validityInfo.validUntil`. | date-time | `2026-06-15T07:30:00+03:00` |
| `trust_anchor_reference` | Location of issuer trust information provisioned to lane readers. | URI | `https://trust.example.eu/ferry/operators/fast-ferries` |

The ferry operator and the authorised ticketing system MAY be the same entity.
An authorised issuer acting for the operator satisfies `issuer`.

### 2.7 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
| ------------------- | -------------- | ------------- | ----------------- |
| `credential_name` | Human-readable credential name. SHALL be `Vehicle Ferry Boarding Credential`. | string | `Vehicle Ferry Boarding Credential` |
| `credential_description` | Wallet-facing description. | string | `Rafina–Milos, 15 June 2026, 07:30` |
| `issuer_name` | Human-readable operator or issuer name. | string | `Fast Ferries` |
| `issuer_logo_uri` | Issuer logo URI. | URI | `https://issuer.example-ferry.gr/logo.png` |
| `privacy_notice` | Privacy-notice URI. | URI | `https://issuer.example-ferry.gr/privacy` |
| `display_locale` | Preferred display language. | string | `en` |
| `status_reference` | Operational status pointer for a reader that can reach the issuer. Not an mdoc data element and not a Mobile Security Object field. | URI or structured value | `https://status.example-ferry.gr/vehicle-boarding/000123456` |

`status_reference` is not carried in the mdoc. ISO/IEC 18013-5:2021 does not
put a status list in the Mobile Security Object. An offline reader SHALL rely
on `validityInfo` and the disclosed journey elements.

### 2.8 Code lists

| **Field name** | **Allowed values** | **Meaning** | **Source / vocabulary** | **Notes** |
| -------------- | ------------------ | ----------- | ----------------------- | --------- |
| `credential_type` | `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1` | Credential type identifier. | This Rulebook | SHALL equal the `docType`. |
| `category` | `eaa:eu:non-qualified`, `eaa:eu:qualified` | Legal category. | This Rulebook | The pilot value is `eaa:eu:non-qualified`. |
| `departure_date` / `arrival_date` | ISO 8601 date | Scheduled local date. | ISO 8601 | `YYYY-MM-DD`. |
| `departure_time` / `arrival_time` | `HH:MM` or `HH:MM:SS` | Scheduled local port time. | This Rulebook | Not a zoned instant. |
| `departure_port` / `arrival_port` | Port identifier | Port. | UN/LOCODE recommended | An operator code MAY be used in the pilot. |
| `vehicle_type_code` | Issuer-defined tariff code | Fare or loading category. | Ferry operator tariff vocabulary | Examples include `PC`, `MC`, `VAN`, `BUS`. |

### 2.9 Integrity rules

| **Rule ID** | **Rule statement** | **Why it exists** | **Where enforced** | **Behaviour on failure** |
| ----------- | ------------------ | ----------------- | ------------------ | ------------------------ |
| `VBP-IR-01` | `arrival_date` SHALL NOT precede `departure_date`. | Prevents a journey that runs backwards. | Issuer, before signing. | Issuer SHALL NOT issue the mdoc. |
| `VBP-IR-02` | The credential SHALL describe one journey and one vehicle. | Prevents reuse across sailings or vehicles. | Issuer. The reader checks the disclosed sailing against the lane. | Reader SHALL refuse when it cannot determine that sailing or vehicle. |
| `VBP-IR-03` | The credential SHALL NOT be accepted after `validityInfo.validUntil`. | Boarding entitlement ends at departure, plus only a defined grace period. | Reader, against its clock. | Reader SHALL refuse. |
| `VBP-IR-04` | `docType` SHALL equal `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`. | Identifies this attestation type. | Reader. | Reader SHALL refuse any other `docType`. |
| `VBP-IR-05` | `ticket_let` and `ticket_number` SHALL be non-empty. | The lane needs a ticket identifier. | Issuer, before signing. | Issuer SHALL NOT issue the mdoc. |
| `VBP-IR-06` | Where the lane matches the vehicle by plate, `plate_number` SHOULD be compared with the mVRC and with the vehicle at the lane. | The vehicle in the lane is the vehicle on the ticket. | Reader, as a separate check from mdoc verification. | Reader SHOULD refuse embarkation when that match fails. |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The Vehicle Ferry Boarding Credential SHALL be issued as an ISO/IEC 18013-5
mdoc. The issued object is an `IssuerSigned` structure as defined in that
standard. ISO/IEC 18013-5 does not define how a credential is issued. Where
OpenID4VCI is used, the credential format SHALL be `mso_mdoc`.

Presentation SHALL use ISO/IEC 18013-5 device engagement and device retrieval.
Those steps are separate. Device engagement SHALL be by QR code or NFC.
Device retrieval SHALL be by BLE or NFC, as the lane reader offers. BLE is a
retrieval transport. It is not a device-engagement method.

#### 3.1.1 Document type and namespace

The `docType` SHALL be:

```text
eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1
```

The namespace for the data elements in §3.1.2 SHALL be:

```text
eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1
```

`docType` and the namespace are the same reverse-domain identifier. The
withdrawn version 0.3 type `VehicleBoardingCredential` SHALL NOT be used as
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
| `vehicle_type` | `vehicle_type` | tstr | M |
| `vehicle_type_code` | `vehicle_type_code` | tstr | M |
| `ticket_let` | `ticket_let` | tstr | M |
| `ticket_number` | `ticket_number` | tstr | M |
| `plate_number` | `plate_number` | tstr | C |
| `departure_gate` | `departure_gate` | tstr | O |
| `vessel_description` | `vessel_description` | tstr | O |
| `reservation_number` | `reservation_number` | tstr | O |

Presence `M` means the element SHALL be present in `issuerSigned.nameSpaces`.
Presence `O` means the element MAY be present. Presence `C` means the element
SHALL be present when §2.5 requires it.

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
| `vehicle.vehicleType` | `vehicle_type` |
| `vehicle.vehicleTypeCode` | `vehicle_type_code` |
| `vehicle.plateNumber` | `plate_number` |
| `ticket.ticketLet` | `ticket_let` |
| `ticket.ticketNumber` | `ticket_number` |
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
ISO/IEC 18013-5. For every element in this section, `elementValue` SHALL be a
UTF-8 text string (`tstr`).

The reader requests the elements it needs. Elements the reader does not
request are not disclosed in the `DeviceResponse`. The reader SHALL request
only the elements required for the boarding decision. A boarding decision
SHALL request the mandatory journey, vehicle-category and ticket elements.
It SHALL also request `plate_number` when §2.5 requires that element.

#### 3.1.3 Mobile Security Object

`issuerAuth` SHALL be a `COSE_Sign1` whose payload is the Mobile Security
Object, wrapped as a CBOR tag 24 byte string, as defined in ISO/IEC 18013-5.

The Mobile Security Object SHALL include:

- `version` with the value `1.0`;
- `digestAlgorithm` set to `SHA-256`, `SHA-384` or `SHA-512`;
- `docType` equal to `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`;
- `valueDigests` for the namespace in §3.1.1, with one digest for every issued
  `IssuerSignedItem`;
- `deviceKeyInfo.deviceKey`, a COSE key of the Wallet; and
- `validityInfo.signed`, `validityInfo.validFrom` and `validityInfo.validUntil`,
  each a CBOR tag 0 date-time (`tdate`).

`validityInfo.validFrom` and `validityInfo.validUntil` are the acceptance
window the lane reader checks offline. A reader SHALL reject an mdoc when its
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
vehicle_ferry_boarding_elements = {
  "id": tstr,
  "category": tstr,
  "departure_date": tstr,
  "departure_time": tstr,
  "departure_port": tstr,
  "arrival_date": tstr,
  "arrival_time": tstr,
  "arrival_port": tstr,
  "vehicle_type": tstr,
  "vehicle_type_code": tstr,
  "ticket_let": tstr,
  "ticket_number": tstr,
  ? "plate_number": tstr,
  ? "departure_gate": tstr,
  ? "vessel_description": tstr,
  ? "reservation_number": tstr
}
```

Each entry is issued as an `IssuerSignedItem` per ISO/IEC 18013-5: a CBOR tag
24 byte string of `{ "digestID": uint, "random": bstr, "elementIdentifier": tstr, "elementValue": tstr }`,
with `random` at least 16 bytes long. The `COSE_Sign1` payload is the Mobile
Security Object, also as a CBOR tag 24 byte string. `validityInfo` dates are
CBOR tag 0 date-times.

#### 3.1.5 Illustrative issuer-signed structure

The structure below is the issued `issuerSigned` content, shown inside the
`docType` used on a `DeviceResponse` document. `deviceSigned` is produced at
presentation and is omitted here. Digest values, the certificate and the
signature are placeholders. `validityInfo` dates use CBOR tag 0. Optional
elements that this issuance did not include are absent. `plate_number` is
included because this example is a lane that matches the vehicle by plate.

```cbor-diag
{
  "docType": "eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1",
  "issuerSigned": {
    "nameSpaces": {
      "eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1": [
        24(<<{
          "digestID": 0,
          "random": h'7F9C2BA4E88F827D616045507605853E',
          "elementIdentifier": "id",
          "elementValue": "2aacf8dc-3f0b-4b30-987d-5eacb9dba222"
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
          "elementIdentifier": "vehicle_type",
          "elementValue": "Passenger Car"
        }>>),
        24(<<{
          "digestID": 9,
          "random": h'2122232425262728292A2B2C2D2E2F30',
          "elementIdentifier": "vehicle_type_code",
          "elementValue": "PC"
        }>>),
        24(<<{
          "digestID": 10,
          "random": h'3132333435363738393A3B3C3D3E3F40',
          "elementIdentifier": "ticket_let",
          "elementValue": "V"
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
          "elementIdentifier": "plate_number",
          "elementValue": "NIK-1234"
        }>>)
      ]
    },
    "issuerAuth": [
      h'A10126',
      { 33: [ h'308201AA...ISSUER_LEAF_CERT_DER...' ] },
      24(<<{
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "docType": "eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1",
        "valueDigests": {
          "eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1": {
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
            12: h'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
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
Vehicle Ferry Boarding Credential
Rafina (GRRFN) – Milos (GRMLO)
15 June 2026, 07:30
Vehicle: Passenger Car, NIK-1234
Ticket: V 000123456
Valid until: 15 June 2026, 07:30
```

The Wallet Unit SHOULD inform the User that:

- this credential is presented at the vehicle lane with ISO/IEC 18013-5
  device engagement and device retrieval;
- the User can refuse presentation; and
- a staff-assisted boarding process remains available where ferry policy
  allows it.

### 3.2 SD-JWT VC-based encoding

This version does not define an SD-JWT VC representation.

The withdrawn version 0.3 profile (`vct` `VehicleBoardingCredential`, with
nested `departure`, `arrival`, `vehicle` and `ticket` objects) SHALL NOT be
issued as a Vehicle Ferry Boarding Credential.

### 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM representation.

## 4 Attestation usage

### 4.1 Issuance trigger

The Vehicle Ferry Boarding Credential SHALL be issued only after:

1. a vehicle booking exists for one sailing;
2. the vehicle category and ticket identifier are known;
3. where §2.5 requires it, the plate number is known; and
4. the User has consented to receive the credential.

Issuance MAY happen at booking time. It does not require the vehicle to be at
the port.

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
- vehicle category and, where present, plate number;
- ticket identifier;
- that the credential is presented with ISO/IEC 18013-5 device engagement and
  device retrieval; and
- the validity window.

### 4.5 Presentation at the vehicle lane

A normal use SHOULD follow these steps:

1. the Wallet and the lane reader perform ISO/IEC 18013-5 device engagement
   by QR code or NFC;
2. they establish an encrypted session and retrieve data over BLE or NFC, as
   the reader offers;
3. the reader sends a `DeviceRequest` for `docType`
   `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`, requesting the
   elements required for the boarding decision from that same namespace;
4. the Wallet obtains the User's consent and returns a `DeviceResponse`;
5. the reader verifies `issuerAuth`, the `IssuerSignedItem` digests, device
   authentication and `validityInfo`, as specified in §4.7;
6. the reader checks that `departure_port`, `departure_date` and
   `departure_time` are the sailing this lane is boarding;
7. where vehicle matching applies, the reader compares `plate_number` and
   `vehicle_type_code` as specified in §4.6;
8. the reader allows embarkation or refuses; and
9. a minimal event MAY be recorded when the reader can store or forward one.

The reader SHALL perform mdoc verification locally. It SHALL NOT require a
live ticketing lookup in order to accept the credential.

A minimal event MAY contain a pseudonymous credential reference (`id`), a
timestamp, a result, a reason code and a reader identifier. It SHOULD NOT
contain PID attributes, the device key, the Mobile Security Object, or
payment data.

### 4.6 Vehicle, passenger and registration checks

mdoc verification and vehicle matching are separate.

When the lane matches the vehicle by plate, the reader SHOULD request this
credential's `plate_number` and the minimum mVRC attributes needed for the
comparison, and SHOULD compare them with the vehicle at the lane. The reader
SHALL request only those attributes.

Where policy also identifies the driver or passengers, the reader SHOULD
request the passenger Ferry Boarding Pass and PID. Those presentations are
not claims of this mdoc.

This Rulebook does not define a cryptographic binding between this credential
and the mVRC. The lane compares the disclosed values.

### 4.7 Verifier obligations

The lane reader SHALL:

1. complete ISO/IEC 18013-5 device engagement and encrypted device retrieval;
2. decrypt and parse the `DeviceResponse`;
3. confirm that the document `docType` and the Mobile Security Object
   `docType` are both `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`;
4. verify the `issuerAuth` `COSE_Sign1` and the issuer certificate chain
   against a trust anchor provisioned for this operator;
5. recompute the digest of each disclosed `IssuerSignedItem` and match it to
   `valueDigests` for that `digestID`;
6. verify device authentication, either a device signature or a device MAC,
   against the `SessionTranscript` and the `deviceKey` in the Mobile Security
   Object;
7. verify `validityInfo` against the reader's clock;
8. confirm that the disclosed `departure_port`, `departure_date` and
   `departure_time` match the sailing this lane is boarding;
9. confirm that a requested mandatory element was disclosed;
10. apply `VBP-IR-01` to the disclosed dates;
11. where the reader has connectivity and a status source is available, reject
    a revoked or suspended credential; and
12. allow embarkation only when these checks succeed.

A missing requested element, a digest mismatch or a `docType` mismatch SHALL
be a refusal.

A reader SHALL NOT accept a credential for another operator only because the
same vendor operates both lanes.

### 4.8 Failure and fallback

The reader SHALL refuse embarkation on the strength of this credential when:

- device engagement or device retrieval fails;
- `issuerAuth`, a data-element digest or device authentication fails;
- the reader does not trust the issuer for this operator;
- the current time is outside `validityInfo`;
- the credential is revoked or suspended and the reader can determine that;
- the disclosed sailing is not the sailing this lane is boarding;
- a requested mandatory element is missing; or
- required vehicle matching fails.

The operator SHALL keep a staff-assisted boarding path where ferry policy
allows it. Refusal of the mdoc SHALL NOT by itself close that path.

## 5 Trust anchors

The lane reader SHALL establish that the issuer:

1. is the ferry operator or an authorised ticketing system acting for it;
2. is authorised to issue Vehicle Ferry Boarding Credentials for this
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

- the vehicle ticket is cancelled, refunded or exchanged;
- the vehicle is removed or replaced on the booking;
- the sailing, ports or departure time change;
- the device is lost or compromised;
- the credential was issued in error; or
- the issuer is no longer authorised.

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

1. one vehicle and one journey per credential;
2. separation from the passenger Ferry Boarding Pass, the mVRC, PID and
   payment;
3. Wallet display name **Vehicle Ferry Boarding Credential** and `docType`
   `eu.europa.ec.eudi.aptitude.vehicle_ferry_boarding.1`;
4. the data elements in §3.1.2;
5. ISO/IEC 18013-5 device engagement (QR code or NFC) and device retrieval
   (BLE or NFC), verified at the lane;
6. device authentication bound to the `SessionTranscript`;
7. a signed validity window that an offline reader can enforce, together with
   a match of the disclosed sailing to the lane;
8. revocation on cancellation or vehicle change, applied by readers that can
   see status;
9. minimal event logging; and
10. a staff-assisted fallback where ferry policy allows it.

The following matters remain open and require operator input:

- confirmation of the `docType`, namespace and data elements against the
  operator's ticketing profile, where that profile assigns different
  identifiers;
- how lane readers are provisioned with issuer trust anchors;
- the status mechanism an online reader uses;
- the length of any post-departure grace period; and
- when `plate_number` is mandatory for a given operator.

This version does not define an SD-JWT VC or a W3C VCDM encoding.

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
