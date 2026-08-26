# Attestation Rulebook for attestations of type Accommodation Voucher

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                                  |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality working paper and the APTITUDE Attestation Rulebook template. |
| 0.2     | 24-07-2026 | Aligned data model and `vct` with the APTITUDE issuer configuration (`booking_reference_credential`).        |
| 0.3     | 26-08-2026 | Aligned display name, nested claim set and check-in composition with the issuer schema for Accommodation Voucher (`booking_reference_credential`), PID and optional European Disability Card. |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The attribute model below SHALL
> match the APTITUDE issuer configuration for `booking_reference_credential`
> (Wallet display name: **Accommodation Voucher**).



## 1 Introduction



### 1.1 Document scope and purpose

This Rulebook defines the **Accommodation Voucher**, a hotel-booking attestation
issued to a traveller's EUDI Wallet after a reservation has been successfully
created or confirmed.

The issuer-configuration identifier and Verifiable Credential Type (`vct`) is:

```text
booking_reference_credential
```

The Wallet display name is **Accommodation Voucher**.

The credential enables a hotel, Property Management System (PMS), booking platform,
travel agent or authorised intermediary to:

- retrieve the correct reservation;
- confirm that the credential applies to the target property and stay period;
- bind the presented reservation to verified guest identity where required;
- support self-service or staff-assisted check-in;
- support reservation-state progression;
- reduce manual entry of booking details; and
- return a structured booking-validation result.

The credential is not a PID and SHALL NOT duplicate the traveller's full identity.
A minimal guest name MAY be included so that the voucher can be matched to the
reservation. Identity attributes needed for legal hotel registration SHALL be
requested separately from PID (`urn:eu.europa.ec.eudi:pid:1`) according to the
applicable jurisdiction and hotel policy.

Where the guest optionally requests accessibility-related assistance (for example
an easier-access room or assistance with the room), the European Disability Card
(`urn:eu.europa.ec.eudi:edc:1`) MAY be presented in the same check-in transaction.
That presentation is optional and is defined in the European Disability Card
Rulebook.

The credential is also distinct from:

- a payment confirmation or eReceipt;
- the **Hotel Pass** (`room_key_credential`), which is a visual QR pass issued
  after check-in and is not a cryptographic room-key credential;
- a proof-of-stay credential; and
- the authoritative reservation record held by the hotel, DMC, booking platform or PMS.



### 1.2 Architectural role

The credential acts primarily as a trusted **reservation lookup and binding artefact**.

The authoritative reservation state remains in the booking or hotel infrastructure.
`reservationStatus` in the credential is the issuer-known status at issuance. Where
reservation details may change after issuance, the verifier SHALL retrieve current
operational state from the authorised booking or PMS system rather than treating
the voucher as the live reservation record.

Typical back-end states include:

```text
reserved
confirmed
pre_check_in_available
checked_in
room_assigned
checked_out
cancelled
no_show
```



### 1.3 Document structure

- Chapter 2 defines attributes and metadata.
- Chapter 3 defines the SD-JWT VC encoding.
- Chapter 4 defines issuance, presentation and verification.
- Chapter 5 defines trust anchors.
- Chapter 6 defines validity, status and revocation.
- Chapter 7 defines compliance and privacy requirements.
- Chapter 8 lists references.



### 1.4 Key words

The capitalised words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119].

### 1.5 Terminology

- **Reservation reference** means the reservation identifier used to retrieve the
booking (`reservationReference`).
- **Supplier reference** means the identifier assigned by the supplier, DMC or
booking platform (`supplierReference`).
- **Voucher reference** means the issuer-assigned voucher identifier
(`voucherReference`).
- **Property identifier** means a stable identifier of the target hotel or
accommodation in the pilot or production environment (`property.id`).
- **PMS** means the hotel's Property Management System.
- **Primary guest** means the traveller to whom the credential was issued and whose
wallet presentation is used for booking retrieval or check-in.
- **Hotel Pass** means the follow-on visual QR pass (`room_key_credential`) issued
after successful check-in.
- **PID** means Person Identification Data of type `urn:eu.europa.ec.eudi:pid:1`.



## 2 Attestation attributes and metadata



### 2.1 Legal category

For the SEDIT-X pilot, the credential is a **non-qualified EAA**:

```text
eaa:eu:non-qualified
```



### 2.2 Design principles

1. The credential SHALL identify the reservation without reproducing the complete
  booking record.
2. The booking or PMS back end SHALL remain authoritative for mutable state.
3. Full civil identity SHALL remain in PID. The voucher MAY contain a minimal
  guest name for reservation matching.
4. The verifier SHALL request only the fields needed for reservation retrieval and
  the applicable hotel-registration process.
5. Payment data SHALL remain separate.
6. Presentation SHALL require User consent.
7. Raw PID attributes SHOULD be retained only for the short operational period needed
  for verification and delivery to the authorised hotel system.
8. Accessibility assistance SHALL be requested from the European Disability Card
  where the guest opts in, not from this voucher.
9. A manual or staff-assisted lookup process SHALL remain available.



### 2.3 Credential attributes

The credential attribute set SHALL match the APTITUDE issuer configuration for
`booking_reference_credential`. Nested objects SHALL be preserved as issued.


| **Data Identifier**      | **Definition**                                                                                          | **Data type** | **Example value**            |
| ------------------------ | ------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------- |
| `id`                     | Unique identifier of this voucher instance.                                                             | string        | `8f2c1e4a-6b9d-4c21-9a0e-2d7f5b8c1a90` |
| `reservationReference`   | Reservation or booking reference. Primary lookup value for hotel check-in.                              | string        | `BR-2026-00042`              |
| `supplierReference`      | Supplier, DMC or booking-platform reference associated with the reservation.                            | string        | `SUP-2026-00001`             |
| `property.id`            | Stable identifier of the target hotel or property.                                                      | string        | `hotel-123`                  |
| `property.name`          | Human-readable property name for Wallet display and verifier confirmation.                              | string        | `Example Hotel Athens`       |
| `stay.checkInDate`       | Arrival or check-in date.                                                                               | date          | `2026-06-12`                 |
| `stay.checkOutDate`      | Departure or check-out date.                                                                            | date          | `2026-06-15`                 |
| `room.type`              | Booked room type or product description.                                                                | string        | `Standard Double`            |
| `ratePlanCode`           | Rate-plan or tariff code associated with the reservation.                                               | string        | `BAR`                        |
| `reservationStatus`      | Issuer-known reservation status at issuance. Live state remains in the booking or PMS system.           | string        | `Confirmed`                  |
| `voucherReference`       | Issuer-assigned voucher identifier.                                                                     | string        | `VCH-2026-00042`             |
| `guest.givenName`        | Given name of the primary guest as recorded on the reservation.                                         | string        | `Hanna`                      |
| `guest.familyName`       | Family name of the primary guest as recorded on the reservation.                                        | string        | `Matkalainen`                |


The credential SHALL NOT include PAN, IBAN, payment tokens, cryptograms or other
sensitive payment-instrument data.

The credential SHALL NOT include PID attributes other than the minimal guest name
needed for reservation matching.

### 2.4 Mandatory metadata


| **Data Identifier**      | **Definition**                                                                        | **Data type**           | **Example value**                                    |
| ------------------------ | ------------------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------- |
| `category`               | Legal category.                                                                       | string                  | `eaa:eu:non-qualified`                               |
| `issuer`                 | Identifier of the booking platform, DMC, hotel or authorised issuer.                  | string or URI           | `https://issuer.avratours.example`                   |
| `credential_type`        | Encoding-independent credential type identifier. SHALL equal the issuer-config `vct`. | string                  | `booking_reference_credential`                       |
| `issued_at`              | Credential issuance timestamp.                                                        | date-time               | `2026-06-12T11:30:00Z`                               |
| `status_reference`       | Status or revocation reference.                                                       | URI or structured value | `https://status.booking.example/atl/2026-06/12#4821` |
| `trust_anchor_reference` | Location of issuer trust information.                                                 | URI                     | `https://trust.aptitude.example/hospitality-issuers` |




### 2.5 Optional metadata


| **Data Identifier**      | **Definition**                                                                        | **Data type** | **Example value**                                          |
| ------------------------ | ------------------------------------------------------------------------------------- | ------------- | ---------------------------------------------------------- |
| `expires_at`             | Credential expiry. Recommended to align with stay window plus a limited grace period. | date-time     | `2026-06-16T12:00:00+03:00`                                |
| `valid_from`             | Beginning of credential validity.                                                     | date-time     | `2026-06-12T11:30:00Z`                                     |
| `credential_name`        | Wallet display name. SHALL be `Accommodation Voucher`.                                | string        | `Accommodation Voucher`                                    |
| `credential_description` | Human-readable description.                                                           | string        | `Stay at Example Hotel Athens, 12–15 June 2026`            |
| `issuer_name`            | Human-readable issuer name.                                                           | string        | `AVRA Tours`                                               |
| `issuer_logo_uri`        | URI of issuer logo.                                                                   | URI           | `https://issuer.example/logo.png`                          |
| `privacy_notice`         | URI of privacy information.                                                           | URI           | `https://issuer.example/privacy`                           |
| `issuer_policy`          | URI of issuance and verification policy.                                              | URI           | `https://issuer.example/policy`                            |
| `display_locale`         | Preferred display language.                                                           | string        | `en`                                                       |




# 3 Attestation encoding



## 3.1 ISO/IEC 18013-5-compliant encoding

This version does not define an mdoc representation.

A future profile MAY define mdoc for on-premises proximity check-in, provided the same
semantic model, status checks and selective-disclosure rules are preserved.

## 3.2 SD-JWT VC-based encoding

The Accommodation Voucher SHALL be issued as `dc+sd-jwt`.

### 3.2.1 Verifiable Credential Type

The `vct` value SHALL be:

```text
booking_reference_credential
```

This matches the APTITUDE issuer configuration identifier and scope
`booking_reference_credential`. The Wallet display name for this type is
**Accommodation Voucher**.

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
| `reservationReference`   | `reservationReference`   | string     | MUST            |
| `supplierReference`      | `supplierReference`      | string     | MUST            |
| `property`               | `property`               | object     | MUST NOT        |
| `property.id`            | `id`                     | string     | MUST            |
| `property.name`          | `name`                   | string     | MUST            |
| `stay`                   | `stay`                   | object     | MUST NOT        |
| `stay.checkInDate`       | `checkInDate`            | string     | MUST            |
| `stay.checkOutDate`      | `checkOutDate`           | string     | MUST            |
| `room`                   | `room`                   | object     | MUST NOT        |
| `room.type`              | `type`                   | string     | MUST            |
| `ratePlanCode`           | `ratePlanCode`           | string     | MUST            |
| `reservationStatus`      | `reservationStatus`      | string     | MUST            |
| `voucherReference`       | `voucherReference`       | string     | MUST            |
| `guest`                  | `guest`                  | object     | MUST NOT        |
| `guest.givenName`        | `givenName`              | string     | MUST            |
| `guest.familyName`       | `familyName`             | string     | MUST            |
| `trust_anchor_reference` | `trust_anchor_reference` | string     | MUST NOT        |


Nested objects SHALL be selectively disclosable at the smallest practical semantic
unit. A verifier SHALL be able to request `reservationReference` and `property.id`
without receiving the full guest name where that name is not required.

### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://issuer.avratours.example",
  "iat": 1781263800,
  "nbf": 1781263800,
  "exp": 1781607600,
  "vct": "booking_reference_credential",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 4821,
      "uri": "https://status.booking.example/atl/2026-06/12"
    }
  },
  "category": "eaa:eu:non-qualified",
  "id": "8f2c1e4a-6b9d-4c21-9a0e-2d7f5b8c1a90",
  "reservationReference": "BR-2026-00042",
  "supplierReference": "SUP-2026-00001",
  "property": {
    "id": "hotel-123",
    "name": "Example Hotel Athens"
  },
  "stay": {
    "checkInDate": "2026-06-12",
    "checkOutDate": "2026-06-15"
  },
  "room": {
    "type": "Standard Double"
  },
  "ratePlanCode": "BAR",
  "reservationStatus": "Confirmed",
  "voucherReference": "VCH-2026-00042",
  "guest": {
    "givenName": "Hanna",
    "familyName": "Matkalainen"
  },
  "trust_anchor_reference": "https://trust.aptitude.example/hospitality-issuers"
}
```



## 3.3 W3C Verifiable Credentials Data Model-based encoding

This version does not define a W3C VCDM representation.

# 4 Attestation usage



## 4.1 Issuance trigger

The Accommodation Voucher SHALL be issued only after:

1. the reservation has been successfully created or confirmed;
2. a reservation reference has been returned;
3. the target property and stay dates are known;
4. the issuer is authorised to issue for the reservation;
5. any required guest-to-booking binding has been established; and
6. the User has consented to receive the credential.

The source-defined flow is:

1. the reservation is created through the existing booking, DMC or hotel process;
2. the Booking Platform creates an issuance session for
  `booking_reference_credential`;
3. the Intermediary Service creates a credential offer;
4. the Wallet receives and displays the offer as **Accommodation Voucher**;
5. the User accepts it;
6. the Wallet completes OpenID4VCI issuance; and
7. the credential is stored in the Wallet.



## 4.2 Holder binding

The credential **SHOULD be device-bound**.

The issuer SHOULD associate it with the primary guest using:

- verified identity data collected during booking;
- a holder-binding key; or
- a PID binding where required.

The credential SHALL NOT contain full PID data merely to support binding.

## 4.3 Hotel check-in presentation

Hotel check-in is a composed presentation. The verifier SHALL treat the following
credentials as distinct request objects.

### 4.3.1 Accommodation Voucher

The verifier SHOULD request:

- `reservationReference`;
- `property.id`;
- `stay.checkInDate`;
- `stay.checkOutDate`; and
- optionally `property.name`, `reservationStatus`, `room.type`, `voucherReference`
  and `guest` names where useful for confirmation or display.

### 4.3.2 PID

PID claims SHALL be requested separately from this voucher, using
`vct` `urn:eu.europa.ec.eudi:pid:1` (`dc+sd-jwt`), and only according to hotel,
jurisdictional and pilot requirements.

The issued PID claim set used in the hospitality pilot includes:

- `given_name`, `family_name`;
- `birthdate`;
- `place_of_birth` (`country`, `region`, `locality`);
- `nationalities`;
- `picture`;
- `address` (`formatted`, `country`, `region`, `locality`, `postal_code`,
  `street_address`, `house_number`);
- `personal_administrative_number`;
- `birth_family_name`, `birth_given_name`;
- `sex`;
- `email`, `phone_number`;
- `issuing_authority`, `issuing_country`, `issuing_jurisdiction`;
- `date_of_issuance`, `date_of_expiry`;
- `document_number`;
- `trust_anchor`; and
- `attestation_legal_category` (`PID`).

A hotel check-in verifier SHOULD request only the subset required for reservation
matching and legal guest registration, typically:

- `family_name` and `given_name`;
- `birthdate`, where jurisdiction-dependent;
- `nationalities`, where jurisdiction-dependent;
- `address`, only where hotel-registration law requires it;
- `document_number`, only where legally required; and
- `picture`, only where staff visual confirmation is part of the check-in process.

The verifier SHALL NOT routinely request `email`, `phone_number`,
`personal_administrative_number`, birth names, `sex` or other PID claims that are
not required for the current registration process.

`guest.givenName` / `guest.familyName` from the voucher SHOULD be compared with
PID `given_name` / `family_name` where guest-to-booking binding is required.

### 4.3.3 Optional European Disability Card

After or together with voucher and PID verification, the guest MAY present a
European Disability Card (`european_disability_card`,
`vct` `urn:eu.europa.ec.eudi:edc:1`) to request assistance with the room, an
easier-access room, or related hospitality accommodations.

That presentation is optional. The hotel SHALL NOT treat absence of the card as
absence of an accessibility need. The requested EDC claims and verifier
obligations are defined in the European Disability Card Rulebook.



## 4.4 Verification obligations

The hotel, PMS or Intermediary Service SHALL:

1. verify credential signature and integrity;
2. verify issuer trust and authority;
3. verify credential validity and status;
4. verify holder binding where required;
5. confirm `property.id` matches the target property;
6. confirm the stay dates are relevant to the check-in request;
7. retrieve the reservation using `reservationReference`;
8. compare required PID attributes with the booking or registration record;
9. verify the current reservation state from the booking or PMS system;
10. process an optional European Disability Card presentation where offered;
11. return a structured result; and
12. retain only the minimum operational information.

Example:

```json
{
  "credential_valid": true,
  "booking_found": true,
  "hotel_match": true,
  "stay_window_valid": true,
  "guest_binding_valid": true,
  "booking_status": "Confirmed",
  "check_in_allowed": true,
  "accessibility_assistance_requested": false,
  "decision": "proceed",
  "correlation_id": "hci_01JZ..."
}
```



## 4.5 Reservation-state progression

The credential MAY include `reservationStatus` as known at issuance.

The verifier SHALL retrieve current state from the authorised booking or PMS
system. A mismatch between `reservationStatus` and live PMS state SHALL be
resolved in favour of the PMS.

The credential SHOULD NOT be reissued for every PMS state change unless required by
the chosen implementation model.

Successful check-in MAY trigger issuance of a **Hotel Pass**
(`room_key_credential`) as defined in the Hotel Pass Rulebook.

## 4.6 PMS integration

Where PMS integration exists, the verified reservation reference and PID attributes MAY be
used to:

- retrieve the reservation;
- update the guest registration record;
- record successful identity verification;
- complete check-in;
- assign a room;
- record an optional accessibility-assistance request;
- trigger Hotel Pass issuance; and
- support check-out.

Where PMS integration does not exist, the verified result MAY be displayed to hotel
staff for manual processing.

## 4.7 Data minimisation and retention

The Intermediary Service SHOULD NOT act as a long-term store of traveller identity.

Raw PID attributes SHOULD be retained only for the short period required to:

- validate the presentation;
- deliver the result;
- support controlled retries;
- handle troubleshooting; and
- satisfy an agreed audit requirement.

European Disability Card attributes, where presented, are special-category data and
SHALL follow the retention rules in the European Disability Card Rulebook.

The verifier SHOULD retain only:

- reservation reference or pseudonymous transaction reference;
- property identifier;
- verification timestamp;
- check-in outcome; and
- minimum legal-registration data where applicable.



## 4.8 Failure and fallback

The verifier SHALL return `denied`, `not_found` or `manual_review` where:

- signature, trust, validity or status verification fails;
- the booking cannot be found;
- the property does not match;
- the booking is cancelled or expired;
- the stay dates are not relevant;
- guest binding cannot be established;
- current reservation state cannot be retrieved where required; or
- applicable legal-registration claims are unavailable.

A staff-assisted reservation lookup SHALL remain possible.

Absence or failure of an optional European Disability Card presentation SHALL NOT
by itself deny check-in.

# 5 Trust anchors

The credential may be issued by:

- a hotel;
- a hotel group;
- a booking platform;
- a travel agent or tour operator;
- a Destination Management Company;
- a reservation back-office service; or
- an Attestation Provider acting for one of these entities.

The verifier SHALL determine:

1. the issuer's identity;
2. the issuer's authority over the reservation;
3. the hotel or booking-system scope covered by that authority;
4. the accepted credential type (`booking_reference_credential`);
5. applicable signing certificates or trust anchors; and
6. whether the issuer remains authorised.

For the APTITUDE pilot, trust SHOULD be obtained through the WP2 trust framework.

# 6 Revocation and status



## 6.1 Validity

The credential expiry SHOULD align with:

- the stay window; and
- a limited post-departure grace period.

It SHOULD NOT remain valid indefinitely.

## 6.2 Revocation triggers

The credential SHALL be revocable or status-checkable when:

- the reservation is cancelled;
- the booking is refunded or voided;
- the booking is transferred where transfer is permitted;
- stay dates or property change materially;
- a replacement credential is issued;
- fraud or erroneous issuance is detected;
- the Wallet or credential is compromised; or
- the issuer is no longer authorised.



## 6.3 Mutable state versus revocation

Live reservation-state checks in the booking or PMS system do not eliminate the need
for credential status checking.

The verifier SHOULD check both:

1. credential validity and status; and
2. current reservation state.

The final APTITUDE status-list endpoint remains to be defined.

# 7 Compliance

This Rulebook is designed to align with:

- Regulation (EU) 2024/1183;
- the EUDI Wallet Architecture and Reference Framework;
- ARF Annex 2 Topic 12;
- OpenID4VCI;
- OpenID4VP;
- SD-JWT VC and HAIP;
- GDPR data-minimisation and storage-limitation principles;
- the SEDIT-X Hospitality working paper; and
- the APTITUDE issuer configuration for `booking_reference_credential`.

The Rulebook enforces:

1. the issuer-config claim set (`id`, `reservationReference`, `supplierReference`,
  `property`, `stay`, `room`, `ratePlanCode`, `reservationStatus`,
  `voucherReference`, `guest`);
2. Wallet display name **Accommodation Voucher**;
3. separation of the voucher from PID
  (`urn:eu.europa.ec.eudi:pid:1`);
4. optional, separate European Disability Card presentation for hospitality
  assistance;
5. separate handling of legal hotel-registration data;
6. authoritative PMS or booking-system state;
7. user consent;
8. status and revocation;
9. minimal intermediary retention; and
10. staff-assisted fallback.

Open matters include:

- final issuer governance model;
- guest-to-PID binding mechanism;
- group-booking and delegation rules;
- final status-list infrastructure;
- whether an mdoc representation is required;
- country-specific hotel-registration profiles; and
- Hotel Pass issuance after check-in.



# 8 References


| **Item Reference**                     | **Standard name/details**                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183                                                                                  |
| [APTITUDE issuer-config]               | NXD-Foundation / nxd-wallet-conformance-backend, `data/issuer-config.json`, `booking_reference_credential` |
| [SEDIT-X Hospitality Working Paper]    | SEDIT-X Frictionless Hotel Check-in and Guest Verification Using the EUDI Wallet                           |
| [APTITUDE D4.1]                        | APTITUDE D4.1: UC Specifications and Scenarios, final version                                              |
| [ARF]                                  | European Digital Identity Wallet Architecture and Reference Framework                                      |
| [OpenID4VCI]                           | OpenID for Verifiable Credential Issuance                                                                  |
| [OpenID4VP]                            | OpenID for Verifiable Presentations                                                                        |
| [HAIP]                                 | OpenID4VC High Assurance Interoperability Profile                                                          |
| [SD-JWT VC]                            | SD-JWT-based Verifiable Credentials                                                                        |
| [RFC 2119]                             | Key words for use in RFCs to Indicate Requirement Levels                                                   |
| [Topic 7]                              | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking                                      |
| [Topic 10]                             | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit                                      |
| [Topic 12]                             | ARF Annex 2, Topic 12 — Attestation Rulebooks                                                              |
| [ETSI TS 119 472-1]                    | Electronic Attestation of Attributes; building blocks and general requirements                             |
| [PID Implementing Regulation]          | Commission Implementing Regulation (EU) 2024/2977 — PID                                                    |
| [European Disability Card Rulebook]    | APTITUDE WP4 Rulebook for `european_disability_card` (`urn:eu.europa.ec.eudi:edc:1`)                       |
| [Hotel Pass Rulebook]                  | APTITUDE WP4 Rulebook for `room_key_credential`                                                            |

