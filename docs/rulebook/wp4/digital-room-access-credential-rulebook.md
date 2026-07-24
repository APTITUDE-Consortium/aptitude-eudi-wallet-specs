# Attestation Rulebook for attestations of type Digital Room Access Credential

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                             |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------- |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality material and the APTITUDE Attestation Rulebook template. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented proposal for an optional, follow-on
> hospitality credential.
>
> This credential is **MVP+ / optional**. It SHALL NOT be treated as a mandatory component
> of the initial SEDIT-X Hospitality MVP, whose primary credential is the Hotel Booking
> Reference Credential.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Digital Room Access Credential**, a short-lived,
hotel-issued Electronic Attestation of Attributes stored in a guest's EUDI Wallet after
successful identity verification and hotel check-in.

The credential represents a time-bounded and scope-bounded right to access:

- an assigned hotel room;
- a defined set of common hotel facilities;
- an assigned accommodation area;
- another hotel-controlled access point associated with the guest's stay; or
- a combination of the above.

The credential MAY also support controlled integration with:

- room-lock systems;
- mobile key platforms;
- lifts and floor-access controls;
- hotel lounges;
- parking areas;
- spa, gym or pool facilities;
- business centres;
- meal areas;
- self-service kiosks; and
- later stay, checkout or expense-related processes.

The credential SHALL NOT be treated as the authoritative reservation record. The Hotel
Booking Reference Credential and the hotel's PMS remain responsible for reservation
identification and current stay state.

The Digital Room Access Credential is distinct from:

- PID;
- the Hotel Booking Reference Credential;
- a physical or proprietary mobile key;
- a payment credential;
- a proof-of-stay credential;
- a hotel loyalty credential; and
- a complete hotel guest profile.

### 1.2 Source-supported role

The SEDIT-X source material supports the following baseline:

1. room-access or stay-related credentials are optional follow-on credentials;
2. they may be issued after successful identity verification and check-in;
3. they may support access to the room and hotel facilities; and
4. they may later support checkout or expense-related processes.

The source material also states that operational data for room-key issuance and hotel
services may be generated after the hotel or PMS has retrieved the reservation and
updated the guest or check-in record.

All detailed claims and cryptographic access mechanisms below are proposed extensions
to that baseline.

### 1.3 Credential versus door key

This Rulebook distinguishes between:

- the **access credential**, which proves the scope and validity of the guest's access
rights; and
- the **door-key material**, which is the lock-system-specific secret, token or derived
cryptographic capability used to operate a particular lock.

The access credential SHOULD NOT directly contain a long-lived reusable lock secret.

A preferred implementation is:

1. the Wallet presents or proves the access credential to an authorised lock gateway,
  hotel application or reader;
2. the verifier confirms the credential, access scope, time window and status;
3. the system derives, retrieves or validates a short-lived lock capability; and
4. access is granted or denied.

Where a lock platform requires key material to be provisioned into the Wallet, it SHALL be:

- device-bound;
- encrypted;
- scoped to the authorised lock or lock group;
- time-bounded;
- revocable or replaceable;
- protected against replay and extraction; and
- separated from human-readable credential claims.

### 1.4 Document structure

- Chapter 2 defines attributes and metadata.
- Chapter 3 defines the proposed SD-JWT VC encoding and lock-system binding models.
- Chapter 4 defines issuance, activation, use and verification.
- Chapter 5 defines trust anchors.
- Chapter 6 defines validity, suspension and revocation.
- Chapter 7 defines compliance, privacy and security requirements.
- Chapter 8 lists references.

### 1.5 Key words

The capitalised words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119].

### 1.6 Terminology

For this Rulebook:

- **Access zone** means a hotel-controlled room, facility, floor, lift, parking area or
other physical area.
- **Access point** means a door, gate, reader, turnstile, lift controller or similar
enforcement component.
- **Lock gateway** means the system that validates or converts wallet-held access rights
into a lock-system decision.
- **Primary guest** means the guest whose check-in produced the credential.
- **Delegated guest** means another authorised guest who receives a separate access
credential for the same room or stay.

## 2 Attestation attributes and metadata

### 2.1 Legal category

For the SEDIT-X pilot, the credential is a **non-qualified EAA**:

```text
eaa:eu:non-qualified
```

### 2.2 Design principles

1. **Issue after check-in:** the credential SHALL be issued only after successful guest
  verification and check-in.
2. **Short-lived access:** validity SHALL be limited to the relevant stay and operational
  access window.
3. **Minimum disclosure:** the credential SHALL NOT contain unnecessary civil identity.
4. **Device binding:** the credential SHOULD be bound to the Wallet Unit.
5. **Separate access secrets:** reusable door-key secrets SHALL NOT be exposed as ordinary
  selectively disclosable claims.
6. **Current hotel state:** the PMS or access-control system remains authoritative for room
  assignment, checkout, access suspension and lock state.
7. **Independent delegation:** each guest SHOULD receive a separate credential rather
  than sharing one wallet credential or key.
8. **Immediate suspension:** hotel staff SHALL be able to suspend access when required.
9. **Legacy scanner compatibility:** where existing readers require a QR or barcode, the
  credential MAY include a display payload carrying the room number or equivalent
   operational code.
10. **Fallback:** physical key cards and staff-assisted access SHALL remain available.

### 2.3 Mandatory attributes


| **Data Identifier**    | **Definition**                                                     | **Data type**               | **Example value**                                 |
| ---------------------- | ------------------------------------------------------------------ | --------------------------- | ------------------------------------------------- |
| `access_credential_id` | Unique identifier of the Digital Room Access Credential.           | string                      | `drac_01JZ7R4M9P2K6T8V3Q5D`                       |
| `hotel_id`             | Stable identifier of the hotel or property.                        | string                      | `hotel_gr_skg_001`                                |
| `booking_reference`    | Booking reference associated with the checked-in stay.             | string                      | `AVRA-HTL-2026-004821`                            |
| `display_room_number`  | Human-readable room number for Wallet display and operational use. | string                      | `504`                                             |
| `access_scope`         | Set of access zones authorised by the credential.                  | array of strings or objects | `["assigned_room","guest_lift","breakfast_area"]` |
| `access_valid_from`    | Beginning of the access period.                                    | date-time                   | `2026-08-04T15:00:00+03:00`                       |
| `access_valid_until`   | End of the access period.                                          | date-time                   | `2026-08-08T11:00:00+03:00`                       |
| `access_status`        | Current issuer-known access state.                                 | string enum                 | `active`                                          |


Permitted values for `access_status` SHOULD include:

- `issued`;
- `active`;
- `temporarily_suspended`;
- `revoked`;
- `expired`;
- `checked_out`; and
- `replaced`.

### 2.4 Optional attributes


| **Data Identifier**        | **Definition**                                                                                                                                      | **Data type**    | **Example value**                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------- |
| `hotel_name`               | Human-readable hotel name.                                                                                                                          | string           | `Aegean City Hotel`                               |
| `floor`                    | Authorised floor for display or lift control.                                                                                                       | string           | `5`                                               |
| `guest_role`               | Role of the holder in the stay.                                                                                                                     | string enum      | `primary_guest`                                   |
| `access_zone_details`      | Structured list of authorised access zones and conditions.                                                                                          | array of objects | `[{"zone":"spa","from":"08:00","until":"20:00"}]` |
| `facility_entitlements`    | Hotel facilities available to the guest.                                                                                                            | array of strings | `["breakfast_area","gym"]`                        |
| `parking_access`           | Indicates access to the hotel parking facility.                                                                                                     | boolean          | `true`                                            |
| `lift_access`              | Indicates use of guest lifts or specified floors.                                                                                                   | boolean          | `true`                                            |
| `late_checkout_access`     | Indicates that access extends beyond the standard checkout time.                                                                                    | boolean          | `false`                                           |
| `access_method`            | Supported access interaction method.                                                                                                                | array of strings | `["nfc","ble","qr"]`                              |
| `display_qr_payload`       | Optional QR or barcode payload for compatibility with existing hotel scanners. MAY encode the room number or an equivalent operational access code. | binary or string | `ROOM:504`                                        |
| `credential_display_label` | Wallet-facing label.                                                                                                                                | string           | `Room 504 Access`                                 |


Permitted values for `guest_role` SHOULD include:

- `primary_guest`;
- `additional_guest`;
- `delegated_guest`; and
- `staff_authorised_guest`.

### 2.5 Mandatory metadata


| **Data Identifier**      | **Definition**                                            | **Data type**           | **Example value**                                           |
| ------------------------ | --------------------------------------------------------- | ----------------------- | ----------------------------------------------------------- |
| `category`               | Legal category of the attestation.                        | string                  | `eaa:eu:non-qualified`                                      |
| `issuer`                 | Identifier of the hotel or authorised room-access issuer. | string or URI           | `https://issuer.aegeancityhotel.example`                    |
| `credential_type`        | Encoding-independent credential type identifier.          | string                  | `urn:aptitude.eu:seditx:digital-room-access:1`              |
| `issued_at`              | Credential issuance timestamp.                            | date-time               | `2026-08-04T14:52:00+03:00`                                 |
| `schema_version`         | Credential schema version.                                | string                  | `0.1`                                                       |
| `status_reference`       | Credential status or revocation reference.                | URI or structured value | `https://status.hotel.example/access/atl/2026-08/04#5042`   |
| `trust_anchor_reference` | Location of issuer trust information.                     | URI                     | `https://trust.aptitude.example/hospitality-access-issuers` |


### 2.6 Optional metadata


| **Data Identifier**      | **Definition**                       | **Data type** | **Example value**                                    |
| ------------------------ | ------------------------------------ | ------------- | ---------------------------------------------------- |
| `credential_name`        | Human-readable credential name.      | string        | `Digital Room Access Credential`                     |
| `credential_description` | Wallet-facing description.           | string        | `Access to Room 504 and authorised hotel facilities` |
| `issuer_name`            | Human-readable hotel or issuer name. | string        | `Aegean City Hotel`                                  |
| `issuer_logo_uri`        | Issuer logo URI.                     | URI           | `https://hotel.example/logo.png`                     |
| `privacy_notice`         | Privacy-notice URI.                  | URI           | `https://hotel.example/privacy`                      |
| `issuer_policy`          | Access-credential policy URI.        | URI           | `https://hotel.example/digital-key-policy`           |
| `display_locale`         | Preferred display language.          | string        | `en`                                                 |


# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 does not define a complete mdoc representation.

A future proximity profile MAY use mdoc where:

- the lock or access reader acts as an authorised proximity verifier;
- the requested data is minimal;
- verifier authentication is available;
- offline verification is required; and
- the access-control protocol remains separate from the ordinary attribute namespace.

A proposed future document type could be:

```text
urn:aptitude.eu:seditx:digital-room-access:1
```

This value is not yet normative.

## 3.2 SD-JWT VC-based encoding

### 3.2.1 Verifiable Credential Type

The proposed `vct` value is:

```text
urn:aptitude.eu:seditx:digital-room-access:1
```

### 3.2.2 Registered JWT claims


| **Data Identifier**  | **Claim** | **Format** | **Disclosable** |
| -------------------- | --------- | ---------- | --------------- |
| `issuer`             | `iss`     | string     | MUST NOT        |
| `issued_at`          | `iat`     | integer    | MUST NOT        |
| `access_valid_from`  | `nbf`     | integer    | MUST NOT        |
| `access_valid_until` | `exp`     | integer    | MUST NOT        |
| `credential_type`    | `vct`     | string     | MUST NOT        |
| `holder_binding`     | `cnf`     | object     | MUST NOT        |
| `status_reference`   | `status`  | object     | MUST NOT        |


### 3.2.3 Private claims


| **Data Identifier**      | **Claim**                | **Format** | **Disclosable** |
| ------------------------ | ------------------------ | ---------- | --------------- |
| `category`               | `category`               | string     | MUST NOT        |
| `access_credential_id`   | `access_credential_id`   | string     | MUST NOT        |
| `hotel_id`               | `hotel_id`               | string     | MUST            |
| `hotel_name`             | `hotel_name`             | string     | MUST            |
| `booking_reference`      | `booking_reference`      | string     | MUST            |
| `display_room_number`    | `display_room_number`    | string     | MUST            |
| `floor`                  | `floor`                  | string     | MUST            |
| `guest_role`             | `guest_role`             | string     | MUST            |
| `access_scope`           | `access_scope`           | array      | MUST            |
| `access_zone_details`    | `access_zone_details`    | array      | MUST            |
| `facility_entitlements`  | `facility_entitlements`  | array      | MUST            |
| `access_status`          | `access_status`          | string     | MUST            |
| `parking_access`         | `parking_access`         | boolean    | MUST            |
| `lift_access`            | `lift_access`            | boolean    | MUST            |
| `late_checkout_access`   | `late_checkout_access`   | boolean    | MUST            |
| `access_method`          | `access_method`          | array      | MUST            |
| `display_qr_payload`     | `display_qr_payload`     | string     | MUST            |
| `schema_version`         | `schema_version`         | string     | MUST NOT        |
| `trust_anchor_reference` | `trust_anchor_reference` | string     | MUST NOT        |


Door-key or lock-provider material SHALL NOT appear as a normal SD-JWT disclosure.

### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://issuer.aegeancityhotel.example",
  "iat": 1785851520,
  "nbf": 1785852000,
  "exp": 1786176000,
  "vct": "urn:aptitude.eu:seditx:digital-room-access:1",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 5042,
      "uri": "https://status.hotel.example/access/atl/2026-08/04"
    }
  },
  "category": "eaa:eu:non-qualified",
  "access_credential_id": "drac_01JZ7R4M9P2K6T8V3Q5D",
  "hotel_id": "hotel_gr_skg_001",
  "hotel_name": "Aegean City Hotel",
  "booking_reference": "AVRA-HTL-2026-004821",
  "display_room_number": "504",
  "guest_role": "primary_guest",
  "access_scope": [
    "assigned_room",
    "guest_lift",
    "breakfast_area",
    "gym"
  ],
  "access_status": "active",
  "access_method": [
    "nfc",
    "ble",
    "qr"
  ],
  "display_qr_payload": "ROOM:504",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.aptitude.example/hospitality-access-issuers"
}
```

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 does not define a W3C VCDM representation.

## 3.4 Lock-system binding

The access credential MAY be integrated with a lock platform using one of three
proposed models. This Rulebook does not define the lock-provider cryptographic
protocol. The final profile SHALL specify whether access uses presentation to a
connected verifier, NFC, Bluetooth Low Energy, a Wallet-to-lock reader protocol, a
display QR for existing scanners, a hotel mobile-key SDK, secure hardware, or a
combination of these.

### Model A — Online credential verification

1. the Wallet presents the credential to a lock gateway or hotel reader;
2. the gateway validates the credential and live access state;
3. the gateway instructs the lock to open.

This model avoids provisioning a reusable lock secret into the credential.

### Model B — Protected mobile-key provisioning

1. the hotel validates the stay and Wallet Unit;
2. the lock platform provisions encrypted device-bound key material separately from
  the credential claims;
3. the Wallet or secure hardware uses the material through NFC or BLE;
4. the key expires or is revoked at checkout.

### Model C — Display QR for existing scanners

1. the Wallet displays `display_qr_payload`, which MAY encode the room number or an
  equivalent operational code;
2. an existing hotel scanner or reader processes the QR or barcode;
3. the hotel access system validates the stay and room assignment against live state;
4. access is granted or denied.

A display QR used for legacy scanners SHALL NOT embed a long-lived reusable lock secret.

# 4 Attestation usage

## 4.1 Issuance trigger

The credential SHALL be issued only after:

1. a valid Hotel Booking Reference Credential or equivalent reservation record exists;
2. the hotel has successfully retrieved the reservation;
3. required PID attributes have been verified;
4. the guest has completed hotel registration requirements;
5. check-in has been completed or approved;
6. a room has been assigned;
7. the hotel or PMS has created an active stay record;
8. the access scope and time window have been determined; and
9. the User has consented to receive the credential.

This is a follow-on issuance step after check-in, not part of the initial booking-
reference issuance flow.

## 4.2 Issuer

The credential SHALL be issued by:

- the hotel;
- the hotel group's authorised access issuer;
- the hotel's PMS or digital-key service acting under hotel authority; or
- an authorised Attestation Provider acting for the hotel.

A travel agent or booking platform SHOULD NOT issue room-access rights unless it has
explicit, current authorisation from the hotel and access-control system.

## 4.3 Device binding

The credential **SHALL be device-bound** where it is used to operate a physical lock.

The binding SHOULD use a key held by the Wallet Unit or device secure hardware.

The issuer SHALL ensure that:

- the credential cannot be copied to another device without authorisation;
- access-key material is not exportable as clear text;
- replacement on a new device invalidates or suspends the previous credential; and
- device loss can trigger immediate suspension.

## 4.4 Wallet display and consent

Before issuance, the Wallet SHOULD display:

- hotel name;
- room or accommodation label;
- access-validity period;
- authorised facility access;
- issuer;
- device-binding notice;
- conditions of use; and
- emergency or staff fallback information.

The Wallet SHOULD avoid displaying internal lock identifiers or cryptographic material.

## 4.5 Room access transaction

A normal access transaction SHOULD follow these steps:

1. the guest approaches the access point;
2. the Wallet is unlocked or authorises background use according to Wallet policy;
3. the access point and Wallet establish the supported channel;
4. the Wallet proves possession of the credential or protected capability;
5. the verifier checks time, scope, device binding and status;
6. the hotel access system confirms that the stay remains active;
7. access is granted or denied; and
8. a minimal access event may be recorded.

Repeated explicit consent for every room-door operation MAY be replaced by a prior
time-bounded authorisation where allowed by the Wallet and hotel policy.

High-risk or exceptional access operations MAY require explicit User authentication.

## 4.6 Facility access

The credential MAY authorise facilities in addition to the room.

The verifier SHALL check that:

- the facility appears in `access_scope`;
- the current time is within any facility-specific interval;
- the guest role permits access;
- the stay is active; and
- the credential has not been suspended.

Facility access SHALL NOT imply permission to charge the guest. Payment or charge
authorisation SHALL be handled separately.

## 4.7 Delegated and additional-guest access

A primary guest MAY request access for another registered guest where hotel policy
allows it.

The hotel SHALL issue a separate credential to the delegated or additional guest.

The delegated credential SHALL:

- have its own identifier;
- be bound to the recipient's Wallet Unit;
- identify the permitted access scope;
- cover the same stay or room;
- have an independent status;
- have a validity period no longer than the primary stay; and
- be individually revocable.

Guests SHALL NOT be expected to share a Wallet, QR code, secret or credential file.

## 4.8 Room change

When the room assignment changes, the hotel SHALL:

1. suspend or revoke the old room-access scope;
2. update the PMS and access-control system;
3. issue or refresh the credential for the new room;
4. replace any protected key material or display QR payload; and
5. prevent the old credential from opening the previous room.

The lock authorisation SHALL reflect the new room assignment immediately.

## 4.9 Checkout

At checkout, the hotel SHALL:

- set the stay state to `checked_out`;
- revoke, expire or disable access;
- invalidate protected key material;
- stop facility access unless a post-checkout entitlement exists;
- preserve only required audit events; and
- optionally issue a separate proof-of-stay credential.

The access credential SHOULD cease functioning at the earlier of:

- checkout completion;
- `access_valid_until`;
- revocation; or
- replacement.

## 4.10 Verifier obligations

The lock gateway, reader or hotel access system SHALL:

1. verify issuer signature and integrity;
2. verify issuer trust and authority for the hotel;
3. verify device binding;
4. verify validity and current time;
5. verify credential status;
6. verify the requested access point against `access_scope`;
7. verify current stay or access state where connectivity exists;
8. prevent replay and credential cloning;
9. apply room changes and checkout promptly;
10. return a clear grant or denial decision; and
11. log only the minimum event required for security and operations.

A typical decision result is:

```json
{
  "credential_valid": true,
  "device_binding_valid": true,
  "stay_active": true,
  "access_point_authorised": true,
  "time_valid": true,
  "decision": "granted",
  "correlation_id": "access_evt_01JZ..."
}
```

## 4.11 Offline use

Offline use MAY be supported, but the deployment SHALL define:

- maximum offline duration;
- trusted clock requirements;
- lock and key scope;
- cached revocation age;
- replay detection;
- duplicate credential handling;
- room-change behaviour;
- checkout reconciliation; and
- emergency override.

Offline access SHALL NOT continue indefinitely merely because the credential's original
expiry has not yet been reached.

## 4.12 Access-event logging

A minimal access event MAY contain:

- pseudonymous credential or booking reference;
- access-point identifier;
- timestamp;
- result;
- reason code;
- verifier or lock identifier; and
- security-event indicator.

It SHOULD NOT contain:

- PID attributes;
- complete credential data;
- booking details unrelated to access;
- medical or accessibility information;
- payment data; or
- the reusable lock secret.

## 4.13 Failure and fallback

Access SHALL be denied or routed to staff when:

- signature or trust verification fails;
- the credential is expired, suspended or revoked;
- the Wallet Unit binding is invalid;
- the access point is outside the scope;
- the stay is no longer active;
- the room assignment has changed;
- the capability is replayed or malformed;
- the reader cannot establish required freshness; or
- the lock system requires staff intervention.

The hotel SHALL maintain a physical key-card or staff-assisted fallback.

# 5 Trust anchors

The verifier SHALL establish that the issuer:

1. is the hotel or an authorised service acting for it;
2. controls or is authorised to configure access for the relevant property;
3. is authorised to issue the Digital Room Access Credential;
4. uses accepted signing keys and certificates; and
5. remains authorised at verification time.

For the APTITUDE pilot, trust SHOULD be obtained through the WP2 trust framework.

The trust model SHOULD distinguish:

- hotel identity;
- property identity;
- PMS or access-platform identity;
- delegated issuer identity; and
- verifier or lock-reader identity.

A credential issued for one hotel SHALL NOT be accepted by another property merely
because the same vendor operates both lock systems.

# 6 Revocation and status

## 6.1 Validity period

The credential SHALL be short-lived and aligned with the active stay.

`access_valid_until` SHOULD normally correspond to the authorised checkout time,
including only a limited operational grace period where hotel policy requires it.

## 6.2 Revocation and suspension triggers

The credential SHALL be suspended, revoked or replaced when:

- the guest checks out;
- the booking or stay is cancelled;
- the room assignment changes;
- the device is lost or compromised;
- the credential is suspected of being copied;
- the guest requests replacement;
- the hotel blocks room access;
- a delegated guest loses authorisation;
- payment or security policy lawfully requires access suspension;
- the issuer or lock platform is compromised; or
- the credential was issued in error.

## 6.3 Immediate access-state checks

Status-list propagation alone may be insufficient for room access.

Where feasible, the verifier SHOULD also check a live hotel access-control or PMS
service for current stay and room assignment.

The final profile SHALL define the maximum delay between hotel suspension and lock
enforcement.

## 6.4 Replacement

Issuing a replacement credential SHALL invalidate the previous active credential unless
the hotel intentionally permits multiple guests or devices.

Each authorised guest or device SHALL have a separately identifiable credential.

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
2. separation from the Hotel Booking Reference Credential;
3. short-lived room and facility access;
4. device binding;
5. separation of access claims from cryptographic door-key material;
6. live or near-live access-state checks;
7. independent delegated credentials;
8. immediate room-change and checkout handling;
9. minimal access-event logging; and
10. physical or staff-assisted fallback.

The following matters remain open and require technical partner input:

- final credential type identifier;
- lock-provider integration protocol;
- NFC, BLE, QR and OS-wallet support;
- display QR payload format for existing scanners;
- secure-element or hardware-key requirements;
- online versus offline access model;
- final access-scope vocabulary;
- verifier authentication for door readers;
- final status and live-state endpoints;
- key rotation and recovery;
- multi-device policy;
- emergency and staff override;
- room sharing and delegation rules;
- checkout grace periods; and
- separation from a later Proof of Stay Credential.

# 8 References


| **Item Reference**                     | **Standard name/details**                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183                                                        |
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


