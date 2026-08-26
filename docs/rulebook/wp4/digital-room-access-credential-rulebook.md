# Attestation Rulebook for attestations of type Hotel Pass

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                             |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------- |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality material and the APTITUDE Attestation Rulebook template. |
| 0.2     | 26-08-2026 | Aligned with the issuer schema for Hotel Pass (`room_key_credential`): visual QR pass with `id`, `room_number` and `picture`; not a cryptographic room-key credential. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook defines the **Hotel Pass** for the APTITUDE / SEDIT-X hospitality
> pilot. The Wallet display name is **Hotel Pass**. The issuer-configuration
> identifier and `vct` is `room_key_credential`.
>
> The Hotel Pass is a **visual QR pass**. It is **not** a cryptographic room-key
> credential. It SHALL NOT be treated as lock-system key material.
>
> This credential is **MVP+ / optional**. It SHALL NOT be treated as a mandatory
> component of the initial SEDIT-X Hospitality MVP, whose primary credential is the
> Accommodation Voucher (`booking_reference_credential`).

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Hotel Pass**, a short-lived, hotel-issued Electronic
Attestation of Attributes stored in a guest's EUDI Wallet after successful identity
verification and hotel check-in.

The issuer-configuration identifier and Verifiable Credential Type (`vct`) is:

```text
room_key_credential
```

The Wallet display name is **Hotel Pass**.

The credential is a visual pass for the assigned room. It contains:

- an instance identifier;
- the assigned room number for Wallet display and staff confirmation; and
- a PNG QR image, as a data URL, encoding the reservation reference.

The Hotel Pass MAY be used to:

- display the assigned room to the guest;
- present a scannable QR to hotel staff or an existing scanner;
- correlate the checked-in stay with the reservation used at check-in; and
- support later stay, checkout or staff-assisted processes.

The credential SHALL NOT be treated as:

- the authoritative reservation record — that remains the Accommodation Voucher
  and the hotel's PMS;
- a cryptographic room-key, mobile-key, lock secret or derived lock capability;
- PID;
- a payment credential;
- a proof-of-stay credential; or
- a complete hotel guest profile.

Cryptographic integration with room-lock systems, NFC or BLE mobile-key
provisioning is out of scope for this version.

### 1.2 Source-supported role

The SEDIT-X source material supports the following baseline:

1. a follow-on hospitality credential MAY be issued after successful identity
  verification and check-in;
2. it MAY support guest display of the assigned room and staff or scanner
  recognition of the stay; and
3. physical key cards and staff-assisted access SHALL remain available.

Operational room assignment is generated after the hotel or PMS has retrieved
the reservation (from the Accommodation Voucher), verified PID, completed
check-in and assigned a room.

### 1.3 Visual QR pass, not a door key

This Rulebook distinguishes between:

- the **Hotel Pass**, which is a wallet-held visual QR pass for the assigned
  room and reservation; and
- **door-key material**, which is the lock-system-specific secret, token or
  derived cryptographic capability used to operate a particular lock.

The Hotel Pass SHALL NOT contain a lock secret, cryptographic key, access token
or other material capable of operating a lock.

The intended use is:

1. the Wallet displays `room_number` and `picture`;
2. hotel staff or an existing scanner reads the QR image, which encodes the
  reservation reference;
3. the hotel access or PMS system validates the stay and room assignment
  against live state; and
4. access or service is granted, denied, or handled by staff, including by
  issuing or using a physical key card.

A display QR SHALL NOT embed a long-lived reusable lock secret. The QR payload
SHALL encode the reservation reference used at check-in, not lock-system
credentials.

### 1.4 Document structure

- Chapter 2 defines attributes and metadata.
- Chapter 3 defines the SD-JWT VC encoding.
- Chapter 4 defines issuance, display, use and verification.
- Chapter 5 defines trust anchors.
- Chapter 6 defines validity, suspension and revocation.
- Chapter 7 defines compliance, privacy and security requirements.
- Chapter 8 lists references.

### 1.5 Key words

The capitalised words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119].

### 1.6 Terminology

For this Rulebook:

- **Hotel Pass** means the visual QR pass of type `room_key_credential`.
- **Accommodation Voucher** means the booking attestation of type
  `booking_reference_credential`.
- **Reservation reference** means the reservation identifier encoded in the QR
  image and used to retrieve the stay. It is the same identifier as
  `reservationReference` on the Accommodation Voucher.
- **Primary guest** means the guest whose check-in produced the credential.
- **Delegated guest** means another authorised guest who receives a separate
  Hotel Pass for the same room or stay.

## 2 Attestation attributes and metadata

### 2.1 Legal category

For the SEDIT-X pilot, the credential is a **non-qualified EAA**:

```text
eaa:eu:non-qualified
```

### 2.2 Design principles

1. **Issue after check-in:** the credential SHALL be issued only after successful
  guest verification and check-in, once a room has been assigned.
2. **Visual QR pass:** the credential SHALL be a displayable pass, not a
  cryptographic room-key.
3. **Minimum disclosure:** the claim set SHALL be limited to instance identity,
  room number and the QR image.
4. **No lock secrets:** reusable door-key secrets SHALL NOT appear in the
  credential.
5. **Current hotel state:** the PMS remains authoritative for room assignment,
  checkout and access suspension.
6. **Independent copies:** each authorised guest SHOULD receive a separate
  Hotel Pass rather than sharing one Wallet credential or screenshot.
7. **Immediate invalidation:** hotel staff SHALL be able to revoke or replace
  the pass when the room assignment changes or the stay ends.
8. **Legacy scanner compatibility:** `picture` SHALL be a PNG QR image that
  existing staff or scanners can read.
9. **Fallback:** physical key cards and staff-assisted access SHALL remain
  available.

### 2.3 Credential attributes

The credential attribute set SHALL match the APTITUDE issuer configuration for
`room_key_credential`.


| **Data Identifier** | **Definition**                                                                                         | **Data type** | **Example value**                          |
| ------------------- | ------------------------------------------------------------------------------------------------------ | ------------- | ------------------------------------------ |
| `id`                | Unique identifier of this Hotel Pass instance.                                                         | string        | `c3a91b2e-4d7f-4e18-8b05-9f6a2c1d0e77`     |
| `room_number`       | Human-readable assigned room number for Wallet display and operational confirmation.                   | string        | `412`                                      |
| `picture`           | PNG QR image as a data URL, encoding the reservation reference associated with the checked-in stay.    | string        | `data:image/png;base64,...`                |


`picture` SHALL be a `data:` URL with media type `image/png`. The QR symbol
encoded in that image SHALL represent the reservation reference, not lock-system
key material and not a biometric portrait.

`picture` is an operational QR image. It SHALL NOT be interpreted as a PID
portrait or as a facial image.

The credential SHALL NOT include:

- lock secrets, mobile-key material or access tokens;
- PID attributes;
- payment data;
- accessibility or medical data; or
- the full reservation record.

### 2.4 Mandatory metadata


| **Data Identifier**      | **Definition**                                            | **Data type**           | **Example value**                                           |
| ------------------------ | --------------------------------------------------------- | ----------------------- | ----------------------------------------------------------- |
| `category`               | Legal category of the attestation.                        | string                  | `eaa:eu:non-qualified`                                      |
| `issuer`                 | Identifier of the hotel or authorised Hotel Pass issuer.  | string or URI           | `https://issuer.examplehotel.example`                       |
| `credential_type`        | Encoding-independent credential type identifier.          | string                  | `room_key_credential`                                       |
| `issued_at`              | Credential issuance timestamp.                            | date-time               | `2026-06-12T14:52:00+03:00`                                 |
| `status_reference`       | Credential status or revocation reference.                | URI or structured value | `https://status.hotel.example/pass/atl/2026-06/12#412`      |
| `trust_anchor_reference` | Location of issuer trust information.                     | URI                     | `https://trust.aptitude.example/hospitality-access-issuers` |


### 2.5 Optional metadata


| **Data Identifier**      | **Definition**                       | **Data type** | **Example value**                                    |
| ------------------------ | ------------------------------------ | ------------- | ---------------------------------------------------- |
| `expires_at`             | Credential expiry. SHOULD align with checkout plus a limited grace period. | date-time     | `2026-06-15T12:00:00+03:00`                          |
| `valid_from`             | Beginning of credential validity.    | date-time     | `2026-06-12T15:00:00+03:00`                          |
| `credential_name`        | Human-readable credential name. SHALL be `Hotel Pass`. | string        | `Hotel Pass`                                         |
| `credential_description` | Wallet-facing description.           | string        | `Visual pass for Room 412, Example Hotel Athens`     |
| `issuer_name`            | Human-readable hotel or issuer name. | string        | `Example Hotel Athens`                               |
| `issuer_logo_uri`        | Issuer logo URI.                     | URI           | `https://hotel.example/logo.png`                     |
| `privacy_notice`         | Privacy-notice URI.                  | URI           | `https://hotel.example/privacy`                      |
| `issuer_policy`          | Hotel Pass policy URI.               | URI           | `https://hotel.example/hotel-pass-policy`            |
| `display_locale`         | Preferred display language.          | string        | `en`                                                 |


# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

This version does not define an mdoc representation.

A future proximity profile MAY use mdoc where the same semantic model is
preserved: instance identifier, room number and visual QR image, with no
cryptographic lock secret in the attribute namespace.

## 3.2 SD-JWT VC-based encoding

The Hotel Pass SHALL be issued as `dc+sd-jwt`.

### 3.2.1 Verifiable Credential Type

The `vct` value SHALL be:

```text
room_key_credential
```

This matches the APTITUDE issuer configuration identifier and scope
`room_key_credential`. The Wallet display name for this type is **Hotel Pass**.

### 3.2.2 Registered JWT claims


| **Data Identifier** | **Claim** | **Format** | **Disclosable** |
| ------------------- | --------- | ---------- | --------------- |
| `issuer`            | `iss`     | string     | MUST NOT        |
| `issued_at`         | `iat`     | integer    | MUST NOT        |
| `valid_from`        | `nbf`     | integer    | MUST NOT        |
| `expires_at`        | `exp`     | integer    | MUST NOT        |
| `credential_type`   | `vct`     | string     | MUST NOT        |
| `holder_binding`    | `cnf`     | object     | MUST NOT        |
| `status_reference`  | `status`  | object     | MUST NOT        |


### 3.2.3 Private claims


| **Data Identifier**      | **Claim**                | **Format** | **Disclosable** |
| ------------------------ | ------------------------ | ---------- | --------------- |
| `category`               | `category`               | string     | MUST NOT        |
| `id`                     | `id`                     | string     | MUST NOT        |
| `room_number`            | `room_number`            | string     | MUST            |
| `picture`                | `picture`                | string     | MUST            |
| `trust_anchor_reference` | `trust_anchor_reference` | string     | MUST NOT        |


Door-key or lock-provider material SHALL NOT appear as a claim or disclosure.

### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://issuer.examplehotel.example",
  "iat": 1781267520,
  "nbf": 1781268000,
  "exp": 1781524800,
  "vct": "room_key_credential",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 412,
      "uri": "https://status.hotel.example/pass/atl/2026-06/12"
    }
  },
  "category": "eaa:eu:non-qualified",
  "id": "c3a91b2e-4d7f-4e18-8b05-9f6a2c1d0e77",
  "room_number": "412",
  "picture": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "trust_anchor_reference": "https://trust.aptitude.example/hospitality-access-issuers"
}
```

The `picture` value in the example is truncated. A production credential SHALL
contain a complete PNG data URL whose QR payload encodes the reservation
reference (for example `BR-2026-00042`).

### 3.2.5 Human-readable wallet representation

The Wallet Unit SHOULD display:

```text
Hotel Pass
Hotel: Example Hotel Athens
Room: 412
[QR image]
```

The Wallet Unit SHOULD inform the User that:

- this is a visual pass for the assigned room;
- the QR encodes the reservation reference;
- the pass does not cryptographically unlock the door;
- a physical key card or staff process remains available; and
- the User can refuse presentation.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM representation.

# 4 Attestation usage

## 4.1 Issuance trigger

The Hotel Pass SHALL be issued only after:

1. a valid Accommodation Voucher (`booking_reference_credential`) or equivalent
  reservation record exists;
2. the hotel has successfully retrieved the reservation;
3. required PID attributes (`urn:eu.europa.ec.eudi:pid:1`) have been verified;
4. the guest has completed hotel registration requirements;
5. check-in has been completed or approved;
6. a room has been assigned;
7. the hotel or PMS has created an active stay record;
8. a PNG QR image encoding the reservation reference has been generated; and
9. the User has consented to receive the credential.

An optional European Disability Card presentation during check-in MAY influence
room assignment (for example an easier-access room). It SHALL NOT add claims to
the Hotel Pass.

This is a follow-on issuance step after check-in, not part of the initial
Accommodation Voucher issuance flow.

## 4.2 Issuer

The credential SHALL be issued by:

- the hotel;
- the hotel group's authorised issuer;
- the hotel's PMS acting under hotel authority; or
- an authorised Attestation Provider acting for the hotel.

A travel agent or booking platform SHOULD NOT issue a Hotel Pass unless it has
explicit, current authorisation from the hotel.

## 4.3 Device binding

The credential **SHOULD be device-bound**.

Device binding of the SD-JWT does not prevent a screenshot of the displayed QR
image. The hotel access process SHALL therefore validate the encoded reservation
reference and live stay state, and SHALL NOT treat possession of a QR image as
sufficient proof of an active stay.

## 4.4 Wallet display and consent

Before issuance, the Wallet SHOULD display:

- hotel or issuer name;
- room number;
- that the credential is a visual QR pass;
- that it does not cryptographically unlock the door;
- issuer;
- conditions of use; and
- staff fallback information.

The Wallet SHOULD render `picture` as the scannable QR image and `room_number`
as the primary label.

## 4.5 Use at the hotel

A normal use SHOULD follow these steps:

1. the guest opens the Hotel Pass in the Wallet;
2. the Wallet displays `room_number` and the QR image;
3. hotel staff or a scanner reads the QR, recovering the reservation reference;
4. the hotel system looks up the stay and current room assignment;
5. the system confirms that the stay remains active and the room matches
  `room_number`;
6. service or access is granted, denied, or handled by staff; and
7. a minimal event MAY be recorded.

OpenID4VP presentation MAY disclose `room_number` (and, where required, support
verification of the signed credential) without relying only on the visual QR.

The Hotel Pass SHALL NOT be used as a cryptographic command to a lock.

## 4.6 Delegated and additional-guest passes

A primary guest MAY request a pass for another registered guest where hotel
policy allows it.

The hotel SHALL issue a separate Hotel Pass to the delegated or additional
guest.

Each pass SHALL:

- have its own `id`;
- identify the same or an authorised `room_number`;
- encode the applicable reservation reference in `picture`;
- have an independent status;
- have a validity period no longer than the primary stay; and
- be individually revocable.

Guests SHALL NOT be expected to share a Wallet, screenshot, QR image or
credential file as the sole access method.

## 4.7 Room change

When the room assignment changes, the hotel SHALL:

1. suspend or revoke the previous Hotel Pass;
2. update the PMS;
3. issue a replacement Hotel Pass with the new `room_number` and a new QR
  image; and
4. prevent the previous pass from being treated as valid for the old room.

## 4.8 Checkout

At checkout, the hotel SHALL:

- set the stay state to checked out;
- revoke, expire or disable the Hotel Pass;
- preserve only required audit events; and
- optionally issue a separate proof-of-stay credential.

The Hotel Pass SHOULD cease to be accepted at the earlier of:

- checkout completion;
- credential expiry;
- revocation; or
- replacement.

## 4.9 Verifier obligations

The hotel staff application, scanner or Intermediary Service SHALL:

1. recover the reservation reference from the QR image, or verify the presented
  SD-JWT;
2. verify issuer signature and integrity where the SD-JWT is presented;
3. verify issuer trust and authority for the hotel;
4. verify validity and current time;
5. verify credential status where the SD-JWT is presented;
6. retrieve current stay and room assignment from the PMS;
7. confirm that `room_number` matches the live assignment;
8. return a clear accept or deny decision; and
9. log only the minimum event required for security and operations.

A typical decision result is:

```json
{
  "credential_valid": true,
  "reservation_found": true,
  "stay_active": true,
  "room_match": true,
  "decision": "accepted",
  "correlation_id": "pass_evt_01JZ..."
}
```

## 4.10 Access-event logging

A minimal event MAY contain:

- pseudonymous credential or reservation reference;
- timestamp;
- result;
- reason code; and
- verifier or scanner identifier.

It SHOULD NOT contain:

- PID attributes;
- the QR image or complete credential;
- booking details unrelated to the event;
- medical or accessibility information;
- payment data; or
- any lock secret.

## 4.11 Failure and fallback

The pass SHALL be rejected or routed to staff when:

- the QR cannot be read;
- the reservation cannot be found;
- signature or trust verification fails where the SD-JWT is presented;
- the credential is expired, suspended or revoked;
- the stay is no longer active;
- the room assignment has changed; or
- staff intervention is required.

The hotel SHALL maintain a physical key-card or staff-assisted fallback.

# 5 Trust anchors

The verifier SHALL establish that the issuer:

1. is the hotel or an authorised service acting for it;
2. controls or is authorised to issue Hotel Passes for the relevant property;
3. uses accepted signing keys and certificates; and
4. remains authorised at verification time.

For the APTITUDE pilot, trust SHOULD be obtained through the WP2 trust framework.

A Hotel Pass issued for one hotel SHALL NOT be accepted by another property
merely because the same vendor operates both systems.

# 6 Revocation and status

## 6.1 Validity period

The credential SHALL be short-lived and aligned with the active stay.

Expiry SHOULD normally correspond to the authorised checkout time, including
only a limited operational grace period where hotel policy requires it.

## 6.2 Revocation and suspension triggers

The credential SHALL be suspended, revoked or replaced when:

- the guest checks out;
- the booking or stay is cancelled;
- the room assignment changes;
- the device is lost or compromised;
- the QR image is suspected of being copied and misused;
- the guest requests replacement;
- the hotel blocks room access;
- a delegated guest loses authorisation;
- the credential was issued in error; or
- the issuer is no longer authorised.

## 6.3 Live stay-state checks

Because the Hotel Pass is a visual QR encoding a reservation reference,
status-list propagation alone may be insufficient.

Where feasible, the verifier SHOULD also check a live PMS service for current
stay and room assignment. A scanned QR for a checked-out or reassigned stay
SHALL be rejected even if the original image is still displayed in a Wallet.

## 6.4 Replacement

Issuing a replacement Hotel Pass SHALL invalidate the previous active pass
unless the hotel intentionally permits multiple guests or devices.

Each authorised guest SHALL have a separately identifiable pass.

# 7 Compliance

This Rulebook is designed to align with:

- Regulation (EU) 2024/1183;
- the EUDI Wallet Architecture and Reference Framework;
- ARF Annex 2 Topic 12;
- OpenID4VCI;
- OpenID4VP;
- SD-JWT VC and HAIP;
- applicable GDPR requirements;
- hotel security and access-control policies; and
- the SEDIT-X Hospitality source material.

The Rulebook enforces:

1. issuance only after verification and check-in;
2. separation from the Accommodation Voucher;
3. Wallet display name **Hotel Pass** and `vct` `room_key_credential`;
4. the issuer-config claim set (`id`, `room_number`, `picture`);
5. visual QR pass semantics, not cryptographic room-key semantics;
6. live or near-live stay-state checks;
7. independent delegated passes;
8. immediate room-change and checkout handling;
9. minimal event logging; and
10. physical or staff-assisted fallback.

The following matters remain open and require technical partner input:

- QR payload encoding convention for the reservation reference;
- scanner and Wallet rendering profiles for the PNG data URL;
- whether a future cryptographic mobile-key profile is required;
- final status and live-state endpoints;
- multi-device policy;
- emergency and staff override;
- room sharing and delegation rules;
- checkout grace periods; and
- separation from a later Proof of Stay Credential.

# 8 References


| **Item Reference**                     | **Standard name/details**                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183                                                        |
| [APTITUDE issuer-config]               | NXD-Foundation / nxd-wallet-conformance-backend, `data/issuer-config.json`, `room_key_credential` |
| [SEDIT-X Hospitality Working Paper]    | SEDIT-X Frictionless Hotel Check-in and Guest Verification Using the EUDI Wallet |
| [APTITUDE D4.1]                        | APTITUDE D4.1: UC Specifications and Scenarios, final version                    |
| [ARF]                                  | European Digital Identity Wallet Architecture and Reference Framework            |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance                                        |
| [OpenID4VP]                            | OpenID for Verifiable Presentations                                              |
| [HAIP]                                 | OpenID4VC High Assurance Interoperability Profile                                |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials                                              |
| [RFC 2119]                             | Key words for use in RFCs to Indicate Requirement Levels                         |
| [Topic 7]                              | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking            |
| [Topic 10]                             | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit            |
| [Topic 12]                             | ARF Annex 2, Topic 12 — Attestation Rulebooks                                    |
| [ETSI TS 119 472-1]                    | Electronic Attestation of Attributes; building blocks and general requirements   |
| [Accommodation Voucher Rulebook]       | APTITUDE WP4 Rulebook for `booking_reference_credential`                         |
| [European Disability Card Rulebook]    | APTITUDE WP4 Rulebook for `european_disability_card`                             |
| [PID Implementing Regulation]          | Commission Implementing Regulation (EU) 2024/2977 — PID                          |

