# Attestation Rulebook for attestations of type Digital Room Key

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab
  - Leonie Taal, IDnow


| Version | Date       | Description                                                                                                      |
| ------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality material and the APTITUDE Attestation Rulebook template.          |
| 0.2     | 26-08-2026 | Demo profile: visual QR pass with `id`, `room_number` and `picture`. Withdrawn by version 0.3.                   |
| 0.3     | 02-11-2026 | Replaces the visual QR pass with an ISO/IEC 18013-5 mdoc. `docType` is `eu.europa.ec.eudi.aptitude.room_key.1`. Presentation uses device engagement and device retrieval, and the door verifies the `DeviceResponse` offline. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the **Digital Room Key**. The Wallet display name is
> **Digital Room Key**. The credential type identifier, mdoc `docType` and
> namespace are `eu.europa.ec.eudi.aptitude.room_key.1`.
>
> The credential is an **ISO/IEC 18013-5 mdoc**. The Wallet presents it with
> that standard's device engagement and device retrieval. The reader verifies
> the `DeviceResponse` offline and uses the result to unlock the assigned room.
>
> Version 0.2, a visual QR image encoded as an SD-JWT, is withdrawn. This
> credential is the room key. It SHALL NOT be implemented as a scannable
> picture of a QR code.
>
> Physical key cards and staff-assisted access remain available as a fallback.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Digital Room Key**, a short-lived Electronic
Attestation of Attributes stored in a guest's EUDI Wallet after successful
identity verification, hotel check-in and room assignment.

The credential type identifier is:

```text
eu.europa.ec.eudi.aptitude.room_key.1
```

The Wallet display name is **Digital Room Key**.

The credential authorises the holder to unlock one assigned room for the
validity period carried in the mdoc. It contains:

- an instance identifier;
- the assigned room number; and
- the legal category of the attestation.

The door reader SHALL treat a successfully verified mdoc for that room, inside
its validity period, as the credential that unlocks the door. The reader
verifies issuer authentication and device authentication as defined in
ISO/IEC 18013-5. The credential SHALL NOT carry a vendor lock secret, a
key-card clone or a biometric.

The Digital Room Key MAY be used to:

- unlock the assigned room at a reader that supports ISO/IEC 18013-5 device
  engagement and device retrieval;
- show the guest the assigned room in the Wallet; and
- give the hotel a revocable, device-bound access credential for the stay.

The credential SHALL NOT be treated as:

- the authoritative reservation record — that remains the Accommodation
  Voucher and the hotel's booking or property system;
- PID;
- a payment credential;
- a proof-of-stay credential; or
- a complete hotel guest profile.

### 1.2 Architectural role

The hotel issues the Digital Room Key only after check-in has assigned a room.

The mdoc is what the door verifies. A reader that has no network connection
SHALL be able to decide using:

- issuer authentication (`issuerAuth` over the Mobile Security Object);
- the digests of the disclosed data elements;
- device authentication bound to the `SessionTranscript`;
- `validityInfo` in the Mobile Security Object; and
- a match between `room_number` and the door.

The hotel's property system remains authoritative for who is checked in and
which room is assigned. A reader with connectivity SHOULD apply revocation and
status. A reader without connectivity relies on the signed validity window and
SHALL NOT refuse an otherwise valid mdoc only because it cannot reach the
property system.

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

### 1.5 Terminology

For this Rulebook:

- **Digital Room Key** means the mdoc whose `docType` is
  `eu.europa.ec.eudi.aptitude.room_key.1`.
- **Accommodation Voucher** means the booking attestation of type
  `booking_reference_credential`.
- **Door reader** means the mdoc reader at the lock. It performs ISO/IEC 18013-5
  device engagement and device retrieval and decides whether to unlock.
- **Primary guest** means the guest whose check-in produced the credential.
- **Delegated guest** means another authorised guest who receives a separate
  Digital Room Key for the same room.
- **PID** means Person Identification Data of type `urn:eu.europa.ec.eudi:pid:1`.

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

1. **Issue after check-in.** The credential SHALL be issued only after
  successful guest verification and check-in, once a room has been assigned.
2. **mdoc room key.** The credential SHALL be an ISO/IEC 18013-5 mdoc.
  Presentation SHALL use device engagement and device retrieval as defined
  in that standard.
3. **Offline verification.** A reader SHALL be able to verify the credential
  without a live call to the booking or property system.
4. **Minimum disclosure.** The data elements SHALL be limited to instance
  identity, room number and legal category.
5. **No vendor lock secret.** The credential SHALL NOT contain a lock-vendor
  secret, cloned key-card payload or biometric.
6. **Device binding.** The Mobile Security Object SHALL contain the Wallet
  `deviceKey`. The reader SHALL verify ISO/IEC 18013-5 device authentication
  bound to the `SessionTranscript`.
7. **Short validity.** `validityInfo.validUntil` SHALL cover the stay,
  including only a limited grace period where hotel policy requires it.
8. **Separate copies.** Each authorised guest SHOULD receive a separate
  Digital Room Key rather than a shared Wallet or a copied credential.
9. **Fallback.** Physical key cards and staff-assisted access SHALL remain
  available.

### 2.3 Credential attributes

| **Data Identifier** | **Definition**                                                                 | **Data type** | **Example value**                      |
| ------------------- | ------------------------------------------------------------------------------ | ------------- | -------------------------------------- |
| `id`                | Unique identifier of this Digital Room Key instance.                           | string        | `c3a91b2e-4d7f-4e18-8b05-9f6a2c1d0e77` |
| `room_number`       | Room this credential authorises the door reader to unlock.                     | string        | `412`                                  |
| `category`          | Legal category. Either `eaa:eu:non-qualified` or `eaa:eu:qualified`.           | string        | `eaa:eu:non-qualified`                 |

`id`, `room_number` and `category` SHALL be present.

The credential SHALL NOT include:

- a visual QR image or a picture of a key card;
- a vendor lock secret, mobile-key blob or access token;
- PID attributes;
- payment data;
- accessibility or medical data; or
- the reservation record.

### 2.4 Mandatory metadata

| **Data Identifier**      | **Definition**                                                              | **Data type**           | **Example value**                                            |
| ------------------------ | --------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------ |
| `category`               | Legal category of the attestation. See §2.3.                               | string                  | `eaa:eu:non-qualified`                                       |
| `issuer`                 | Identifier of the credential issuer, such as the hotel or an authorised issuer. | string or URI       | `https://issuer.examplehotel.example`                        |
| `credential_type`        | Encoding-independent credential type identifier. SHALL equal the `docType`. | string                  | `eu.europa.ec.eudi.aptitude.room_key.1`                                        |
| `issued_at`              | Credential issuance time. Carried as `validityInfo.signed`.                 | date-time               | `2026-06-12T14:52:00+03:00`                                  |
| `valid_from`             | Beginning of validity. Carried as `validityInfo.validFrom`.                 | date-time               | `2026-06-12T15:00:00+03:00`                                  |
| `expires_at`             | End of validity. Carried as `validityInfo.validUntil`.                      | date-time               | `2026-06-15T12:00:00+03:00`                                  |
| `trust_anchor_reference` | Location of issuer trust information provisioned to door readers.           | URI                     | `https://trust.aptitude.example/hospitality-access-issuers`  |

The hotel, the issuer and the operator of the booking and check-in systems MAY
be the same entity. An authorised issuer acting for the accommodation provider
satisfies `issuer`.

### 2.5 Optional metadata

| **Data Identifier**      | **Definition**                                              | **Data type** | **Example value**                                      |
| ------------------------ | ----------------------------------------------------------- | ------------- | ------------------------------------------------------ |
| `credential_name`        | Human-readable credential name. SHALL be `Digital Room Key`. | string       | `Digital Room Key`                                     |
| `credential_description` | Wallet-facing description.                                  | string        | `Room 412, Example Hotel Athens`                       |
| `issuer_name`            | Human-readable hotel or issuer name.                        | string        | `Example Hotel Athens`                                 |
| `issuer_logo_uri`        | Issuer logo URI.                                            | URI           | `https://hotel.example/logo.png`                       |
| `privacy_notice`         | Privacy-notice URI.                                         | URI           | `https://hotel.example/privacy`                        |
| `issuer_policy`          | Digital Room Key policy URI.                                | URI           | `https://hotel.example/room-key-policy`                |
| `display_locale`         | Preferred display language.                                 | string        | `en`                                                   |
| `status_reference`       | Operational status pointer for a reader that can reach the issuer. Not an mdoc data element and not a Mobile Security Object field. | URI or structured value | `https://status.hotel.example/room-key/2026-06/12#412` |

`status_reference` is not carried in the mdoc. ISO/IEC 18013-5:2021 does not
put a status list in the Mobile Security Object. An offline reader SHALL rely
on `validityInfo`.

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

The Digital Room Key SHALL be issued as an ISO/IEC 18013-5 mdoc. The issued
object is an `IssuerSigned` structure as defined in that standard.
ISO/IEC 18013-5 does not define how a credential is issued. Where OpenID4VCI
is used, the credential format SHALL be `mso_mdoc`.

Presentation SHALL use ISO/IEC 18013-5 device engagement and device retrieval.
Those steps are separate. Device engagement SHALL be by QR code or NFC.
Device retrieval SHALL be by BLE or NFC, as the door reader offers. BLE is a
retrieval transport. It is not a device-engagement method.

### 3.1.1 Document type and namespace

The `docType` SHALL be:

```text
eu.europa.ec.eudi.aptitude.room_key.1
```

The namespace for the data elements in §3.1.2 SHALL be:

```text
eu.europa.ec.eudi.aptitude.room_key.1
```

`docType` and the namespace are the same reverse-domain identifier. The
withdrawn version 0.2 issuer-config key `room_key_credential` SHALL NOT be
used as the `docType` or the namespace.

### 3.1.2 Data elements

| **Data Identifier** | **Element identifier** | **Encoding** | **Presence** |
| ------------------- | ---------------------- | ------------ | ------------ |
| `id`                | `id`                   | tstr         | M            |
| `room_number`       | `room_number`          | tstr         | M            |
| `category`          | `category`             | tstr         | M            |

Presence `M` means the element SHALL be present in `issuerSigned.nameSpaces`.

`category` SHALL be `eaa:eu:non-qualified` or `eaa:eu:qualified`.

Each element SHALL be carried as an `IssuerSignedItem` under the namespace in
§3.1.1. The item SHALL be encoded as a CBOR tag 24 byte string, as defined in
ISO/IEC 18013-5, and SHALL contain:

- `digestID`, an unsigned integer unique within the namespace;
- `random`, a byte string of at least 16 bytes;
- `elementIdentifier`; and
- `elementValue`.

The digest in the Mobile Security Object SHALL be computed over the
deterministic CBOR encoding of the `IssuerSignedItem`, as specified in
ISO/IEC 18013-5. For these three elements, `elementValue` SHALL be a UTF-8
text string (`tstr`).

### 3.1.3 Mobile Security Object

`issuerAuth` SHALL be a `COSE_Sign1` whose payload is the Mobile Security
Object, wrapped as a CBOR tag 24 byte string, as defined in ISO/IEC 18013-5.

The Mobile Security Object SHALL include:

- `version` with the value `1.0`;
- `digestAlgorithm` set to `SHA-256`, `SHA-384` or `SHA-512`;
- `docType` equal to `eu.europa.ec.eudi.aptitude.room_key.1`;
- `valueDigests` for the namespace in §3.1.1, with one digest for every issued
  `IssuerSignedItem`;
- `deviceKeyInfo.deviceKey`, a COSE key of the Wallet; and
- `validityInfo.signed`, `validityInfo.validFrom` and `validityInfo.validUntil`,
  each a CBOR tag 0 date-time (`tdate`).

`validityInfo.validFrom` and `validityInfo.validUntil` are the validity window
the door reader checks offline. A reader SHALL reject an mdoc when its clock
is before `validFrom` or after `validUntil`.

The issuer SHALL sign `issuerAuth` with a signature algorithm permitted by
ISO/IEC 18013-5. The example in §3.1.5 uses ES256 (COSE algorithm identifier
-7).

Device authentication is not part of `issuerAuth`. During presentation the
Wallet SHALL authenticate the `DeviceResponse` with a device signature or a
device MAC, as defined in ISO/IEC 18013-5, bound to the `SessionTranscript`.

### 3.1.4 CDDL

```cddl
room_key_elements = {
  "id": tstr,
  "room_number": tstr,
  "category": tstr
}
```

Each entry is issued as an `IssuerSignedItem` per ISO/IEC 18013-5: a CBOR tag
24 byte string of `{ "digestID": uint, "random": bstr, "elementIdentifier": tstr, "elementValue": tstr }`,
with `random` at least 16 bytes long. The `COSE_Sign1` payload is the Mobile
Security Object, also as a CBOR tag 24 byte string. `validityInfo` dates are
CBOR tag 0 date-times.

### 3.1.5 Illustrative issuer-signed structure

The structure below is the issued `issuerSigned` content, shown inside the
`docType` used on a `DeviceResponse` document. `deviceSigned` is produced at
presentation and is omitted here. Digest values, the certificate and the
signature are placeholders. `validityInfo` dates use CBOR tag 0.

```cbor-diag
{
  "docType": "eu.europa.ec.eudi.aptitude.room_key.1",
  "issuerSigned": {
    "nameSpaces": {
      "eu.europa.ec.eudi.aptitude.room_key.1": [
        24(<<{
          "digestID": 0,
          "random": h'7F9C2BA4E88F827D616045507605853E',
          "elementIdentifier": "id",
          "elementValue": "c3a91b2e-4d7f-4e18-8b05-9f6a2c1d0e77"
        }>>),
        24(<<{
          "digestID": 1,
          "random": h'0D61F8370CAD1D412F80B84D143E1257',
          "elementIdentifier": "room_number",
          "elementValue": "412"
        }>>),
        24(<<{
          "digestID": 2,
          "random": h'F1D3FF8443297732862DF21DC4E57262',
          "elementIdentifier": "category",
          "elementValue": "eaa:eu:non-qualified"
        }>>)
      ]
    },
    "issuerAuth": [
      h'A10126',
      { 33: [ h'308201AA...ISSUER_LEAF_CERT_DER...' ] },
      24(<<{
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "docType": "eu.europa.ec.eudi.aptitude.room_key.1",
        "valueDigests": {
          "eu.europa.ec.eudi.aptitude.room_key.1": {
            0: h'1111111111111111111111111111111111111111111111111111111111111111',
            1: h'2222222222222222222222222222222222222222222222222222222222222222',
            2: h'3333333333333333333333333333333333333333333333333333333333333333'
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
          "signed": 0("2026-06-12T14:52:00+03:00"),
          "validFrom": 0("2026-06-12T15:00:00+03:00"),
          "validUntil": 0("2026-06-15T12:00:00+03:00")
        }
      }>>),
      h'5F8D3C2A1B0099EE...SIGNATURE...'
    ]
  }
}
```

### 3.1.6 Wallet display

The Wallet Unit SHOULD display:

```text
Digital Room Key
Hotel: Example Hotel Athens
Room: 412
Valid until: 15 June 2026, 12:00
```

The Wallet Unit SHOULD inform the User that:

- this credential unlocks the assigned room at a compatible door reader;
- presentation uses ISO/IEC 18013-5 device engagement and device retrieval;
- the User can refuse presentation; and
- a physical key card or staff process remains available.

## 3.2 SD-JWT VC-based encoding

This version does not define an SD-JWT VC representation.

The withdrawn version 0.2 profile (`dc+sd-jwt` with a PNG QR in `picture`)
SHALL NOT be issued as a Digital Room Key.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM representation.

# 4 Attestation usage

## 4.1 Issuance trigger

The Digital Room Key SHALL be issued only after:

1. a valid Accommodation Voucher (`booking_reference_credential`) or equivalent
  reservation record exists;
2. the hotel has successfully retrieved the reservation;
3. required PID attributes (`urn:eu.europa.ec.eudi:pid:1`) have been verified;
4. the guest has completed hotel registration requirements;
5. check-in has been completed or approved;
6. a room has been assigned;
7. the hotel has created an active stay record; and
8. the User has consented to receive the credential.

An optional European Disability Card presentation during check-in MAY influence
room assignment. It SHALL NOT add claims to the Digital Room Key.

Issuance is a follow-on step after check-in. It is not part of Accommodation
Voucher issuance.

The same entity MAY operate the booking system, issue this credential and
operate check-in.

## 4.2 Issuer

The credential SHALL be issued by:

- the hotel;
- the hotel group's authorised issuer;
- the hotel's property system acting under hotel authority; or
- an authorised Attestation Provider acting for the hotel.

A qualified trust service provider that operates booking and check-in for the
accommodation provider MAY be that Attestation Provider.

A travel agent or booking platform SHOULD NOT issue a Digital Room Key unless
it has explicit, current authorisation from the hotel.

## 4.3 Device binding

The credential SHALL be device-bound.

The Mobile Security Object SHALL contain `deviceKeyInfo.deviceKey`. During
presentation the Wallet SHALL provide device authentication as defined in
ISO/IEC 18013-5, bound to the `SessionTranscript`. A reader SHALL NOT unlock
the door for an `IssuerSigned` structure that is not carried in a
`DeviceResponse` authenticated for that session.

## 4.4 Wallet disclosure and consent

Before issuance, the Wallet SHOULD display:

- hotel or issuer name;
- room number;
- that the credential is a Digital Room Key for that room;
- that it is presented with ISO/IEC 18013-5 device engagement and device retrieval;
- the validity window;
- issuer; and
- staff fallback information.

The Wallet SHOULD show `room_number` as the primary label.

## 4.5 Presentation at the door

A normal use SHOULD follow these steps:

1. the Wallet and the door reader perform ISO/IEC 18013-5 device engagement
  by QR code or NFC;
2. they establish an encrypted session and retrieve data over BLE or NFC, as
  the reader offers;
3. the reader sends a `DeviceRequest` for `docType`
  `eu.europa.ec.eudi.aptitude.room_key.1`, requesting `room_number` and `id`
  from that same namespace;
4. the Wallet obtains the User's consent and returns a `DeviceResponse`;
5. the reader verifies `issuerAuth`, the `IssuerSignedItem` digests, device
  authentication and `validityInfo`, as specified in §4.9;
6. the reader checks that `room_number` is the room this door controls;
7. the reader unlocks the door or refuses; and
8. a minimal event MAY be recorded when the reader can store or forward one.

The reader SHALL perform verification locally. It SHALL NOT require a live
property-system lookup in order to unlock.

## 4.6 Delegated and additional-guest keys

A primary guest MAY request a key for another registered guest where hotel
policy allows it.

The hotel SHALL issue a separate Digital Room Key to that guest's Wallet.

Each key SHALL:

- have its own `id`;
- authorise the same or an authorised `room_number`;
- be bound to that guest's device key;
- have an independent status and its own `validityInfo`;
- have `validUntil` no later than the primary stay; and
- be individually revocable.

Guests SHALL NOT be expected to share a Wallet or a credential file as the
access method.

## 4.7 Room change

When the room assignment changes, the hotel SHALL:

1. revoke the previous Digital Room Key;
2. update the property system;
3. issue a replacement Digital Room Key with the new `room_number` and a new
  `id`; and
4. cease to treat the previous key as valid for the old room.

A reader that cannot yet see the revocation relies on `validUntil`. The issuer
SHOULD set `validUntil` on the replacement and SHOULD keep the withdrawn key's
remaining validity as short as the stay allows. See §6.3.

## 4.8 Checkout

At checkout, the hotel SHALL:

- set the stay state to checked out;
- revoke the Digital Room Key;
- preserve only required audit events; and
- optionally issue a separate proof-of-stay credential.

The Digital Room Key SHOULD cease to be accepted at the earlier of:

- checkout, for a reader that can apply revocation;
- `validityInfo.validUntil`;
- revocation; or
- replacement.

## 4.9 Verifier obligations

The door reader SHALL:

1. complete ISO/IEC 18013-5 device engagement and encrypted device retrieval;
2. decrypt and parse the `DeviceResponse`;
3. confirm that the document `docType` and the Mobile Security Object
  `docType` are both `eu.europa.ec.eudi.aptitude.room_key.1`;
4. verify the `issuerAuth` `COSE_Sign1` and the issuer certificate chain
  against a trust anchor provisioned for this property;
5. recompute the digest of each disclosed `IssuerSignedItem` and match it to
  `valueDigests` for that `digestID`;
6. verify device authentication, either a device signature or a device MAC,
  against the `SessionTranscript` and the `deviceKey` in the Mobile Security
  Object;
7. verify `validityInfo` against the reader's clock;
8. confirm that the disclosed `room_number` matches the door;
9. where the reader has connectivity and a status source is available, reject
  a revoked or suspended credential; and
10. unlock only when these checks succeed.

A missing requested element, a digest mismatch or a `docType` mismatch SHALL
be a refusal.

A reader SHALL NOT unlock a door for another property because the same vendor
operates both properties.

A typical online decision record, where the reader reports one, is:

```json
{
  "credential_valid": true,
  "issuer_trusted": true,
  "device_auth_valid": true,
  "within_validity": true,
  "room_match": true,
  "revocation_checked": false,
  "decision": "unlock",
  "correlation_id": "door_evt_01JZ..."
}
```

`revocation_checked` is `false` when the reader decided offline.

## 4.10 Access-event logging

A minimal event MAY contain:

- pseudonymous credential reference (`id`);
- timestamp;
- result;
- reason code; and
- reader identifier.

It SHOULD NOT contain:

- PID attributes;
- the device key or the Mobile Security Object;
- booking details unrelated to the event;
- medical or accessibility information;
- payment data; or
- any lock secret.

## 4.11 Failure and fallback

The reader SHALL refuse to unlock when:

- device engagement or device retrieval fails;
- `issuerAuth`, a data-element digest or device authentication fails;
- the reader does not trust the issuer for this property;
- the current time is outside `validityInfo`;
- the credential is revoked or suspended and the reader can determine that;
- `room_number` does not match the door; or
- staff intervention is required.

The hotel SHALL maintain a physical key-card or staff-assisted fallback.

# 5 Trust anchors

The door reader SHALL establish that the issuer:

1. is the hotel or an authorised service acting for it;
2. is authorised to issue Digital Room Keys for this property;
3. uses a certificate chain the reader has been provisioned to trust; and
4. was authorised at issuance, as carried by that chain.

Readers for the APTITUDE pilot SHOULD obtain that trust information through
the WP2 trust framework. An offline reader uses the trust anchors provisioned
to it. It does not fetch them during the presentation.

A Digital Room Key issued for one hotel SHALL NOT be accepted by another
property merely because the same vendor operates both systems.

# 6 Revocation and status

## 6.1 Validity period

The credential SHALL be short-lived and aligned with the active stay.

`validityInfo.validUntil` SHOULD correspond to the authorised checkout time,
plus only a limited operational grace period where hotel policy requires it.

This window is the control an offline reader can enforce. The issuer SHALL set
it at issuance. It cannot be shortened after issuance except by revocation,
which an offline reader applies only after it next receives status.

## 6.2 Revocation and suspension triggers

The credential SHALL be suspended, revoked or replaced when:

- the guest checks out;
- the booking or stay is cancelled;
- the room assignment changes;
- the device is lost or compromised;
- the guest requests replacement;
- the hotel blocks room access;
- a delegated guest loses authorisation;
- the credential was issued in error; or
- the issuer is no longer authorised.

## 6.3 Offline readers and status

An offline reader SHALL enforce `validityInfo` and SHALL NOT depend on a live
status service. ISO/IEC 18013-5:2021 verification does not itself fetch a
status list. Checking status is a profile rule for a reader that has
connectivity and a status source.

A reader that has connectivity SHALL check the issuer's status information and
SHALL reject a suspended or revoked credential even when `validUntil` has not
passed.

The hotel SHOULD assume that, until `validUntil`, a reader which has not
received revocation may still unlock. Lost-device and early-checkout handling
therefore SHOULD combine revocation with as short a `validUntil` as the stay
allows, and the physical fallback in §4.11.

## 6.4 Replacement

Issuing a replacement Digital Room Key SHALL revoke the previous active key
unless the hotel intentionally permits multiple guests or devices.

Each authorised guest SHALL have a separately identifiable key.

# 7 Compliance

This Rulebook is designed to align with:

- Regulation (EU) 2024/1183;
- the EUDI Wallet Architecture and Reference Framework;
- ARF Annex 2 Topic 12;
- ISO/IEC 18013-5 for the mdoc, including `IssuerSigned`, the Mobile Security
  Object, device engagement by QR code or NFC, and device retrieval by BLE or NFC;
- OpenID4VCI where the issuance transport is OpenID4VCI;
- applicable GDPR requirements;
- hotel security and access-control policies; and
- the SEDIT-X Hospitality source material.

The Rulebook enforces:

1. issuance only after verification, check-in and room assignment;
2. separation from the Accommodation Voucher and from PID;
3. Wallet display name **Digital Room Key** and `docType`
  `eu.europa.ec.eudi.aptitude.room_key.1`;
4. the data elements `id`, `room_number` and `category`;
5. ISO/IEC 18013-5 device engagement (QR code or NFC) and device retrieval
  (BLE or NFC), verified at the door;
6. device authentication bound to the `SessionTranscript`;
7. a signed validity window that an offline reader can enforce;
8. independent delegated keys;
9. revocation on room change and checkout, applied by readers that can see status;
10. minimal event logging; and
11. physical or staff-assisted fallback.

The following matters remain open and require technical partner input:

- confirmation of the `docType`, namespace and data elements against the UC10
  room-key profile, where that profile assigns different identifiers;
- how door readers are provisioned with issuer trust anchors;
- the status mechanism an online reader uses, including ISO/IEC 18013-5
  revocation where the reader supports it;
- multi-device policy;
- emergency and staff override;
- room sharing and delegation rules;
- checkout grace periods; and
- separation from a later Proof of Stay Credential.

# 8 References

| **Item Reference**                     | **Standard name/details**                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183                                                                                  |
| [ISO/IEC 18013-5]                      | Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application. mdoc structure, device engagement (QR code, NFC) and device retrieval (BLE, NFC). |
| [SEDIT-X Hospitality Working Paper]    | SEDIT-X Frictionless Hotel Check-in and Guest Verification Using the EUDI Wallet                           |
| [APTITUDE D4.1]                        | APTITUDE D4.1: UC Specifications and Scenarios, final version                                              |
| [ARF]                                  | European Digital Identity Wallet Architecture and Reference Framework                                      |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance                                                                  |
| [RFC 2119]                             | Key words for use in RFCs to Indicate Requirement Levels                                                   |
| [RFC 8610]                             | Concise Data Definition Language (CDDL)                                                                    |
| [RFC 8949]                             | Concise Binary Object Representation (CBOR)                                                                |
| [Topic 7]                              | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking                                      |
| [Topic 10]                             | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit                                      |
| [Topic 12]                             | ARF Annex 2, Topic 12 — Attestation Rulebooks                                                              |
| [ETSI TS 119 472-1]                    | Electronic Attestation of Attributes; building blocks and general requirements                             |
| [Accommodation Voucher Rulebook]       | APTITUDE WP4 Rulebook for `booking_reference_credential`                                                   |
| [European Disability Card Rulebook]    | APTITUDE WP4 Rulebook for `european_disability_card`                                                       |
| [PID Implementing Regulation]          | Commission Implementing Regulation (EU) 2024/2977 — PID                                                    |
