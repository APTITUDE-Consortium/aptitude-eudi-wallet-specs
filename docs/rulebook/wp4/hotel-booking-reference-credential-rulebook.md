# Attestation Rulebook for attestations of type Hotel Booking Reference Credential

* Author(s):
    * Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
    * Petros Kavassalis, University of the Aegean, UAegean i4m Lab

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality working paper and the APTITUDE Attestation Rulebook template. |

**Feedback:**

* To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The SEDIT-X Hospitality source
> defines an explicit MVP claim set consisting of `booking_reference`, `hotel_id`,
> `hotel_name`, `arrival_date`, `departure_date`, `booking_platform`, `issued_at`
> and `expires_at`.
>
> Additional claims in this Rulebook are marked as proposed extensions. They support
> reservation lookup, guest-to-booking binding, occupancy, room category, mutable
> reservation-state references and operational check-in, but are not part of the
> source-defined MVP unless stated otherwise.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Hotel Booking Reference Credential**, a hotel-booking
attestation issued to a traveller's EUDI Wallet after a reservation has been successfully
created or confirmed.

The credential enables a hotel, Property Management System (PMS), booking platform,
travel agent or authorised intermediary to:

* retrieve the correct reservation;
* confirm that the credential applies to the target hotel and stay period;
* bind the presented booking reference to verified guest identity where required;
* support self-service or staff-assisted check-in;
* support reservation-state progression;
* reduce manual entry of booking details; and
* return a structured booking-validation result.

The credential is not a PID and SHOULD NOT duplicate the traveller's full identity.
Identity attributes needed for legal hotel registration SHALL be requested separately
from PID according to the applicable jurisdiction and hotel policy.

The credential is also distinct from:

* a payment confirmation or eReceipt;
* a room-access credential;
* a proof-of-stay credential; and
* the authoritative reservation record held by the hotel, DMC, booking platform or PMS.

### 1.2 Architectural role

The credential acts primarily as a trusted **reservation lookup and binding artefact**.

The authoritative reservation state remains in the booking or hotel infrastructure.
Where reservation details may change after issuance, the credential SHOULD reference
a current operational state rather than attempting to embed every mutable field.

Typical states include:

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

* Chapter 2 defines attributes and metadata.
* Chapter 3 defines the SD-JWT VC encoding.
* Chapter 4 defines issuance, presentation and verification.
* Chapter 5 defines trust anchors.
* Chapter 6 defines validity, status and revocation.
* Chapter 7 defines compliance and privacy requirements.
* Chapter 8 lists references.

### 1.4 Key words

The capitalised words **SHALL**, **SHOULD** and **MAY** are used as specified in
[RFC 2119].

### 1.5 Terminology

* **Booking reference** means the reservation identifier used to retrieve the booking.
* **Hotel identifier** means a stable identifier of the target hotel in the pilot or
  production environment.
* **Booking platform** means the portal, travel agent, tour operator or technical platform
  through which the booking originated.
* **PMS** means the hotel's Property Management System.
* **Mutable state reference** means a reference through which an authorised verifier
  can obtain the current reservation or stay state.
* **Primary guest** means the traveller to whom the credential was issued and whose
  wallet presentation is used for booking retrieval or check-in.

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
3. Guest identity SHALL remain in PID unless a minimal booking-specific reference is
   operationally required.
4. The verifier SHALL request only the fields needed for reservation retrieval and the
   applicable hotel-registration process.
5. Payment data SHALL remain separate.
6. Presentation SHALL require User consent.
7. Raw PID attributes SHOULD be retained only for the short operational period needed
   for verification and delivery to the authorised hotel system.
8. A manual or staff-assisted lookup process SHALL remain available.

### 2.3 Mandatory MVP attributes

The following attributes are directly based on the SEDIT-X Hospitality MVP claim set.

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `booking_reference` | Reservation or booking reference identifier. Primary lookup value for hotel check-in. | string | `AVRA-HTL-2026-004821` |
| `hotel_id` | Stable identifier of the target hotel in the pilot context. | string | `hotel_gr_skg_001` |
| `arrival_date` | Arrival or check-in date. | date | `2026-08-04` |
| `departure_date` | Departure or check-out date. | date | `2026-08-08` |

### 2.4 Optional MVP attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `hotel_name` | Human-readable hotel name, useful for wallet display. | string | `Aegean City Hotel` |
| `booking_platform` | Originating booking platform, travel agent or tour operator. | string | `AVRA Tours` |

`issued_at` and `expires_at` are represented as credential metadata in this Rulebook.

### 2.5 Proposed optional extensions

The following attributes are not part of the source-defined MVP claim set. They are
proposed where operational requirements justify them.

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_id` | Unique identifier of the credential. | string | `hbrc_01JZ6K8P4D7M2Q9T5V3R` |
| `hotel_reservation_id` | Hotel- or PMS-specific reservation identifier where different from the booking reference. | string | `PMS-RES-887214` |
| `primary_guest_reference` | Booking-specific or pairwise pseudonymous reference to the primary guest. | string | `guest_f2a91b7c` |
| `booking_status` | Issuer-known reservation state at issuance. | string | `confirmed` |
| `room_category` | Booked room category. | string | `double_standard` |
| `occupancy_adults` | Number of adult guests. | integer | `2` |
| `occupancy_children` | Number of child guests. | integer | `0` |
| `number_of_rooms` | Number of rooms included in the booking. | integer | `1` |
| `board_basis` | Meal or board arrangement. | string | `breakfast_included` |
| `package_reference` | Reference to a travel package or DMC arrangement. | string | `PKG-GR-0826-17` |
| `booking_created_at` | Time the reservation was created or confirmed. | date-time | `2026-06-12T11:25:00Z` |
| `check_in_time_from` | Earliest normal check-in time. | time or date-time | `2026-08-04T15:00:00+03:00` |
| `check_out_time_until` | Latest normal check-out time. | time or date-time | `2026-08-08T11:00:00+03:00` |
| `property_address` | Minimal hotel location information used for wallet display. | object | `{"city":"Thessaloniki","country":"GR"}` |
| `booking_contact_reference` | Protected reference to booking contact data held in the source system. | string | `contact_ref_712a...` |
| `special_request_reference` | Reference to operational requests held in the booking system. | string | `req_01JZ...` |
| `accessibility_request_reference` | Reference to an accessibility-service request without disclosing medical data. | string | `acc_req_01JZ...` |
| `terms_and_conditions_uri` | URI of applicable reservation terms. | URI | `https://hotel.example/booking-terms` |

### 2.6 Mutable-state extensions

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `state_reference` | Opaque reference used to retrieve current reservation state from an authorised system. | URI or string | `https://booking.example/state/bk_8f2...` |
| `state_version` | Version or generation of the state known at issuance. | string | `4` |
| `state_checked_at` | Time at which the embedded state was last confirmed. | date-time | `2026-07-23T09:10:00Z` |
| `current_state_hint` | Non-authoritative state hint for wallet display. | string | `confirmed` |

Where `state_reference` is present:

* it SHALL be opaque and unguessable;
* it SHALL NOT expose personal data in the URI;
* access SHALL require authorised verifier authentication;
* the retrieved state SHALL be limited to the current transaction purpose; and
* the verifier SHALL treat the back-end result as authoritative.

### 2.7 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `subject_binding_reference` | Reference used to bind the booking credential to PID or another identity credential. Present where guest-to-booking matching is required. | string | `pid-bind:84e2...` |
| `group_booking_reference` | Group or delegation reference where the credential relates to a group reservation. | string | `GRP-ERUA-2026-81` |
| `lead_guest_authority` | Indicates that the holder may act for other guests in the booking. | boolean | `true` |
| `additional_guest_count` | Number of additional guests covered by the booking. | integer | `1` |
| `payment_status_hint` | Non-sensitive indication of whether the booking is paid, guaranteed or pay-at-property. | string | `prepaid` |
| `cryptographically_bound_to` | Credential type to which formal binding is applied. | string | `urn:eu.europa.ec.eudi:pid:1` |

The credential SHALL NOT include PAN, IBAN, payment tokens, cryptograms or other
sensitive payment-instrument data.

### 2.8 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the booking platform, DMC, hotel or authorised issuer. | string or URI | `https://issuer.avratours.example` |
| `credential_type` | Encoding-independent credential type identifier. | string | `urn:aptitude.eu:seditx:hotel-booking-reference:1` |
| `issued_at` | Credential issuance timestamp. | date-time | `2026-06-12T11:30:00Z` |
| `schema_version` | Credential schema version. | string | `0.1` |
| `status_reference` | Status or revocation reference. | URI or structured value | `https://status.booking.example/atl/2026-06/12#4821` |
| `trust_anchor_reference` | Location of issuer trust information. | URI | `https://trust.aptitude.example/hospitality-issuers` |

### 2.9 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `expires_at` | Credential expiry. Recommended to align with stay window plus a limited grace period. | date-time | `2026-08-09T12:00:00+03:00` |
| `valid_from` | Beginning of credential validity. | date-time | `2026-06-12T11:30:00Z` |
| `credential_name` | Wallet display name. | string | `Hotel Booking Reference` |
| `credential_description` | Human-readable description. | string | `Booking for Aegean City Hotel, 4–8 August 2026` |
| `issuer_name` | Human-readable issuer name. | string | `AVRA Tours` |
| `issuer_logo_uri` | URI of issuer logo. | URI | `https://issuer.example/logo.png` |
| `privacy_notice` | URI of privacy information. | URI | `https://issuer.example/privacy` |
| `issuer_policy` | URI of issuance and verification policy. | URI | `https://issuer.example/policy` |
| `display_locale` | Preferred display language. | string | `en` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 does not define an mdoc representation.

A future profile MAY define mdoc for on-premises proximity check-in, provided the same
semantic model, status checks and selective-disclosure rules are preserved.

## 3.2 SD-JWT VC-based encoding

### 3.2.1 Verifiable Credential Type

The proposed `vct` value is:

```text
urn:aptitude.eu:seditx:hotel-booking-reference:1
```

### 3.2.2 Registered JWT claims

| **Data Identifier** | **Claim** | **Format** | **Disclosable** |
|---------------------|-----------|------------|-----------------|
| `issuer` | `iss` | string | MUST NOT |
| `issued_at` | `iat` | integer | MUST NOT |
| `valid_from` | `nbf` | integer | MUST NOT |
| `expires_at` | `exp` | integer | MUST NOT |
| `credential_type` | `vct` | string | MUST NOT |
| `holder_binding` | `cnf` | object | MUST NOT |
| `status_reference` | `status` | object | MUST NOT |

### 3.2.3 Private claims

| **Data Identifier** | **Claim** | **Format** | **Disclosable** |
|---------------------|-----------|------------|-----------------|
| `category` | `category` | string | MUST NOT |
| `credential_id` | `credential_id` | string | MUST NOT |
| `booking_reference` | `booking_reference` | string | MUST |
| `hotel_id` | `hotel_id` | string | MUST |
| `hotel_name` | `hotel_name` | string | MUST |
| `arrival_date` | `arrival_date` | string | MUST |
| `departure_date` | `departure_date` | string | MUST |
| `booking_platform` | `booking_platform` | string | MUST |
| `hotel_reservation_id` | `hotel_reservation_id` | string | MUST |
| `primary_guest_reference` | `primary_guest_reference` | string | MUST |
| `booking_status` | `booking_status` | string | MUST |
| `room_category` | `room_category` | string | MUST |
| `occupancy_adults` | `occupancy_adults` | integer | MUST |
| `occupancy_children` | `occupancy_children` | integer | MUST |
| `number_of_rooms` | `number_of_rooms` | integer | MUST |
| `board_basis` | `board_basis` | string | MUST |
| `package_reference` | `package_reference` | string | MUST |
| `booking_created_at` | `booking_created_at` | string | MUST |
| `check_in_time_from` | `check_in_time_from` | string | MUST |
| `check_out_time_until` | `check_out_time_until` | string | MUST |
| `property_address` | `property_address` | object | MUST |
| `booking_contact_reference` | `booking_contact_reference` | string | MUST |
| `special_request_reference` | `special_request_reference` | string | MUST |
| `accessibility_request_reference` | `accessibility_request_reference` | string | MUST |
| `state_reference` | `state_reference` | string | MUST |
| `state_version` | `state_version` | string | MUST |
| `state_checked_at` | `state_checked_at` | string | MUST |
| `current_state_hint` | `current_state_hint` | string | MUST |
| `subject_binding_reference` | `subject_binding_reference` | string | MUST |
| `group_booking_reference` | `group_booking_reference` | string | MUST |
| `lead_guest_authority` | `lead_guest_authority` | boolean | MUST |
| `additional_guest_count` | `additional_guest_count` | integer | MUST |
| `payment_status_hint` | `payment_status_hint` | string | MUST |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | MUST NOT |
| `schema_version` | `schema_version` | string | MUST NOT |
| `trust_anchor_reference` | `trust_anchor_reference` | string | MUST NOT |

### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://issuer.avratours.example",
  "iat": 1781263800,
  "nbf": 1781263800,
  "exp": 1786266000,
  "vct": "urn:aptitude.eu:seditx:hotel-booking-reference:1",
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
  "credential_id": "hbrc_01JZ6K8P4D7M2Q9T5V3R",
  "booking_reference": "AVRA-HTL-2026-004821",
  "hotel_id": "hotel_gr_skg_001",
  "hotel_name": "Aegean City Hotel",
  "arrival_date": "2026-08-04",
  "departure_date": "2026-08-08",
  "booking_platform": "AVRA Tours",
  "primary_guest_reference": "guest_f2a91b7c",
  "booking_status": "confirmed",
  "room_category": "double_standard",
  "occupancy_adults": 2,
  "number_of_rooms": 1,
  "state_reference": "https://booking.example/state/bk_8f2...",
  "state_version": "4",
  "current_state_hint": "confirmed",
  "subject_binding_reference": "pid-bind:84e2...",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.aptitude.example/hospitality-issuers"
}
```

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 does not define a W3C VCDM representation.

# 4 Attestation usage

## 4.1 Issuance trigger

The Booking Reference Credential SHALL be issued only after:

1. the reservation has been successfully created or confirmed;
2. a booking reference has been returned;
3. the target hotel and stay dates are known;
4. the issuer is authorised to issue for the reservation;
5. any required guest-to-booking binding has been established; and
6. the User has consented to receive the credential.

The source-defined flow is:

1. the reservation is created through the existing booking, DMC or hotel process;
2. the Booking Platform creates an issuance session for
   `booking_reference_credential`;
3. the Intermediary Service creates a credential offer;
4. the Wallet receives and displays the offer;
5. the User accepts it;
6. the Wallet completes OpenID4VCI issuance; and
7. the credential is stored in the Wallet.

## 4.2 Holder binding

The credential **SHOULD be device-bound**.

The issuer SHOULD associate it with the primary guest using:

* a booking-specific guest reference;
* verified identity data collected during booking;
* a holder-binding key; or
* a PID binding reference where required.

The credential SHALL NOT contain full PID data merely to support binding.

## 4.3 Hotel check-in presentation

At check-in, the verifier SHOULD request:

* `booking_reference`;
* `hotel_id`;
* `arrival_date`;
* `departure_date`; and
* any guest-binding reference required by policy.

PID claims SHALL be requested separately and only according to hotel, jurisdictional
and pilot requirements.

The source material identifies these possible PID claims:

* `family_name`, usually required for reservation lookup and identification;
* `given_name`, where needed;
* `date_of_birth`, jurisdiction-dependent;
* `nationality`, jurisdiction-dependent;
* document-related fields, only where legally required; and
* address or contact details, which should be avoided unless strictly needed.

## 4.4 Verification obligations

The hotel, PMS or Intermediary Service SHALL:

1. verify credential signature and integrity;
2. verify issuer trust and authority;
3. verify credential validity and status;
4. verify holder binding where required;
5. confirm `hotel_id` matches the target property;
6. confirm the stay dates are relevant to the check-in request;
7. retrieve the reservation using `booking_reference`;
8. compare required PID attributes with the booking or registration record;
9. verify the current reservation state;
10. return a structured result; and
11. retain only the minimum operational information.

Example:

```json
{
  "credential_valid": true,
  "booking_found": true,
  "hotel_match": true,
  "stay_window_valid": true,
  "guest_binding_valid": true,
  "booking_status": "confirmed",
  "check_in_allowed": true,
  "decision": "proceed",
  "correlation_id": "hci_01JZ..."
}
```

## 4.5 Reservation-state progression

The credential MAY support the following operational states:

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

A state embedded in the credential is a hint unless it is guaranteed fresh.

Where `state_reference` is used, the verifier SHALL retrieve the current state from the
authoritative system.

The credential SHOULD NOT be reissued for every PMS state change unless required by
the chosen implementation model.

## 4.6 PMS integration

Where PMS integration exists, the verified booking reference and PID attributes MAY be
used to:

* retrieve the reservation;
* update the guest registration record;
* record successful identity verification;
* complete check-in;
* assign a room;
* trigger room-key issuance; and
* support check-out.

Where PMS integration does not exist, the verified result MAY be displayed to hotel
staff for manual processing.

## 4.7 Data minimisation and retention

The Intermediary Service SHOULD NOT act as a long-term store of traveller identity.

Raw PID attributes SHOULD be retained only for the short period required to:

* validate the presentation;
* deliver the result;
* support controlled retries;
* handle troubleshooting; and
* satisfy an agreed audit requirement.

The verifier SHOULD retain only:

* booking reference or pseudonymous transaction reference;
* hotel identifier;
* verification timestamp;
* check-in outcome; and
* minimum legal-registration data where applicable.

## 4.8 Failure and fallback

The verifier SHALL return `denied`, `not_found` or `manual_review` where:

* signature, trust, validity or status verification fails;
* the booking cannot be found;
* the hotel does not match;
* the booking is cancelled or expired;
* the stay dates are not relevant;
* guest binding cannot be established;
* current reservation state cannot be retrieved where required; or
* applicable legal-registration claims are unavailable.

A staff-assisted reservation lookup SHALL remain possible.

# 5 Trust anchors

The credential may be issued by:

* a hotel;
* a hotel group;
* a booking platform;
* a travel agent or tour operator;
* a Destination Management Company;
* a reservation back-office service; or
* an Attestation Provider acting for one of these entities.

The verifier SHALL determine:

1. the issuer's identity;
2. the issuer's authority over the reservation;
3. the hotel or booking-system scope covered by that authority;
4. the accepted credential type;
5. applicable signing certificates or trust anchors; and
6. whether the issuer remains authorised.

For the APTITUDE pilot, trust SHOULD be obtained through the WP2 trust framework.

# 6 Revocation and status

## 6.1 Validity

The credential expiry SHOULD align with:

* the stay window; and
* a limited post-departure grace period.

It SHOULD NOT remain valid indefinitely.

## 6.2 Revocation triggers

The credential SHALL be revocable or status-checkable when:

* the reservation is cancelled;
* the booking is refunded or voided;
* the booking is transferred where transfer is permitted;
* stay dates or hotel change materially;
* a replacement credential is issued;
* fraud or erroneous issuance is detected;
* the Wallet or credential is compromised; or
* the issuer is no longer authorised.

## 6.3 Mutable state versus revocation

A mutable reservation-state endpoint does not eliminate the need for credential status.

The verifier SHOULD check both:

1. credential validity and status; and
2. current reservation state.

The final APTITUDE status-list endpoint remains to be defined.

# 7 Compliance

This Rulebook is designed to align with:

* Regulation (EU) 2024/1183;
* the EUDI Wallet Architecture and Reference Framework;
* ARF Annex 2 Topic 12;
* OpenID4VCI;
* OpenID4VP;
* SD-JWT VC and HAIP;
* GDPR data-minimisation and storage-limitation principles; and
* the SEDIT-X Hospitality working paper.

The Rulebook enforces:

1. a minimal source-defined MVP claim set;
2. separation of booking reference and PID;
3. separate handling of legal hotel-registration data;
4. authoritative PMS or booking-system state;
5. optional mutable-state references;
6. user consent;
7. status and revocation;
8. minimal intermediary retention; and
9. staff-assisted fallback.

Open matters include:

* final credential type identifier;
* final issuer governance model;
* final state-reference API and authorisation model;
* final guest-to-PID binding mechanism;
* group-booking and delegation rules;
* final status-list infrastructure;
* whether an mdoc representation is required;
* country-specific hotel-registration profiles; and
* room-key or follow-on stay credential integration.

# 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [SEDIT-X Hospitality Working Paper] | SEDIT-X Frictionless Hotel Check-in and Guest Verification Using the EUDI Wallet |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [HAIP] | OpenID4VC High Assurance Interoperability Profile |
| [SD-JWT VC] | SD-JWT-based Verifiable Credentials |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Attestation of Attributes; building blocks and general requirements |
