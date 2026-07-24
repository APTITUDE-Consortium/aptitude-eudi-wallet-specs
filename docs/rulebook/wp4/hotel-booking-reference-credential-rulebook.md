# Attestation Rulebook for attestations of type Hotel Booking Reference Credential

- Author(s):
  - Nikos Triantafyllou, University of the Aegean, UAegean i4m Lab
  - Petros Kavassalis, University of the Aegean, UAegean i4m Lab


| Version | Date       | Description                                                                                                  |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| 0.1     | 23-07-2026 | Initial draft based on the SEDIT-X Hospitality working paper and the APTITUDE Attestation Rulebook template. |
| 0.2     | 24-07-2026 | Aligned data model and `vct` with the APTITUDE issuer configuration (`booking_reference_credential`).        |


**Feedback:**

- To be defined by the APTITUDE WP4 / SEDIT-X governance process.

> **Draft status**
>
> This Rulebook is an implementation-oriented draft. The SEDIT-X Hospitality source  
> defines an explicit MVP claim set consisting of `booking_reference`, `hotel_id`,  
> `hotel_name`, `arrival_date`, `departure_date`, `booking_platform`, `issued_at`  
> and `expires_at`.



## 1 Introduction



### 1.1 Document scope and purpose

This Rulebook defines the **Hotel Booking Reference Credential**, a hotel-booking
attestation issued to a traveller's EUDI Wallet after a reservation has been successfully
created or confirmed.

The credential enables a hotel, Property Management System (PMS), booking platform,
travel agent or authorised intermediary to:

- retrieve the correct reservation;
- confirm that the credential applies to the target hotel and stay period;
- bind the presented booking reference to verified guest identity where required;
- support self-service or staff-assisted check-in;
- support reservation-state progression;
- reduce manual entry of booking details; and
- return a structured booking-validation result.

The credential is not a PID and SHOULD NOT duplicate the traveller's full identity.
Identity attributes needed for legal hotel registration SHALL be requested separately
from PID according to the applicable jurisdiction and hotel policy.

The credential is also distinct from:

- a payment confirmation or eReceipt;
- a room-access credential;
- a proof-of-stay credential; and
- the authoritative reservation record held by the hotel, DMC, booking platform or PMS.



### 1.2 Architectural role

The credential acts primarily as a trusted **reservation lookup and binding artefact**.

The authoritative reservation state remains in the booking or hotel infrastructure.
Where reservation details may change after issuance, the verifier SHALL retrieve current
operational state from the authorised booking or PMS system rather than expecting every
mutable field to be embedded in the credential.

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

- **Booking reference** means the reservation identifier used to retrieve the booking.
- **Hotel identifier** means a stable identifier of the target hotel in the pilot or
production environment.
- **Booking platform** means the portal, travel agent, tour operator or technical platform
through which the booking originated.
- **PMS** means the hotel's Property Management System.
- **Primary guest** means the traveller to whom the credential was issued and whose
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



### 2.3 Credential attributes

The credential attribute set SHALL match the APTITUDE issuer configuration for
`booking_reference_credential`.


| **Data Identifier** | **Definition**                                                                        | **Data type** | **Example value**      |
| ------------------- | ------------------------------------------------------------------------------------- | ------------- | ---------------------- |
| `booking_reference` | Reservation or booking reference identifier. Primary lookup value for hotel check-in. | string        | `AVRA-HTL-2026-004821` |
| `hotel_id`          | Stable identifier of the target hotel.                                                | string        | `hotel_gr_skg_001`     |
| `hotel_name`        | Human-readable hotel name for Wallet display and verifier confirmation.               | string        | `Aegean City Hotel`    |
| `arrival_date`      | Arrival or check-in date.                                                             | date          | `2026-08-04`           |
| `departure_date`    | Departure or check-out date.                                                          | date          | `2026-08-08`           |
| `booking_platform`  | Originating booking platform, travel agent or tour operator.                          | string        | `AVRA Tours`           |


The credential SHALL NOT include PAN, IBAN, payment tokens, cryptograms or other
sensitive payment-instrument data.

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


| **Data Identifier**      | **Definition**                                                                        | **Data type** | **Example value**                                |
| ------------------------ | ------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------ |
| `expires_at`             | Credential expiry. Recommended to align with stay window plus a limited grace period. | date-time     | `2026-08-09T12:00:00+03:00`                      |
| `valid_from`             | Beginning of credential validity.                                                     | date-time     | `2026-06-12T11:30:00Z`                           |
| `credential_name`        | Wallet display name.                                                                  | string        | `Hotel Booking Reference`                        |
| `credential_description` | Human-readable description.                                                           | string        | `Booking for Aegean City Hotel, 4–8 August 2026` |
| `issuer_name`            | Human-readable issuer name.                                                           | string        | `AVRA Tours`                                     |
| `issuer_logo_uri`        | URI of issuer logo.                                                                   | URI           | `https://issuer.example/logo.png`                |
| `privacy_notice`         | URI of privacy information.                                                           | URI           | `https://issuer.example/privacy`                 |
| `issuer_policy`          | URI of issuance and verification policy.                                              | URI           | `https://issuer.example/policy`                  |
| `display_locale`         | Preferred display language.                                                           | string        | `en`                                             |




# 3 Attestation encoding



## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.2 does not define an mdoc representation.

A future profile MAY define mdoc for on-premises proximity check-in, provided the same
semantic model, status checks and selective-disclosure rules are preserved.

## 3.2 SD-JWT VC-based encoding

The Hotel Booking Reference Credential SHALL be issued as `dc+sd-jwt`.

### 3.2.1 Verifiable Credential Type

The `vct` value SHALL be:

```text
booking_reference_credential
```

This matches the APTITUDE issuer configuration identifier and scope
`booking_reference_credential`.

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
| `booking_reference`      | `booking_reference`      | string     | MUST            |
| `hotel_id`               | `hotel_id`               | string     | MUST            |
| `hotel_name`             | `hotel_name`             | string     | MUST            |
| `arrival_date`           | `arrival_date`           | string     | MUST            |
| `departure_date`         | `departure_date`         | string     | MUST            |
| `booking_platform`       | `booking_platform`       | string     | MUST            |
| `trust_anchor_reference` | `trust_anchor_reference` | string     | MUST NOT        |




### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://issuer.avratours.example",
  "iat": 1781263800,
  "nbf": 1781263800,
  "exp": 1786266000,
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
  "booking_reference": "AVRA-HTL-2026-004821",
  "hotel_id": "hotel_gr_skg_001",
  "hotel_name": "Aegean City Hotel",
  "arrival_date": "2026-08-04",
  "departure_date": "2026-08-08",
  "booking_platform": "AVRA Tours",
  "trust_anchor_reference": "https://trust.aptitude.example/hospitality-issuers"
}
```



## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.2 does not define a W3C VCDM representation.

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

- verified identity data collected during booking;
- a holder-binding key; or
- a PID binding where required.

The credential SHALL NOT contain full PID data merely to support binding.

## 4.3 Hotel check-in presentation

At check-in, the verifier SHOULD request:

- `booking_reference`;
- `hotel_id`;
- `arrival_date`;
- `departure_date`; and
- optionally `hotel_name` and `booking_platform` where useful for confirmation or display.

PID claims SHALL be requested separately and only according to hotel, jurisdictional
and pilot requirements.

The source material identifies these possible PID claims:

- `family_name`, usually required for reservation lookup and identification;
- `given_name`, where needed;
- `date_of_birth`, jurisdiction-dependent;
- `nationality`, jurisdiction-dependent;
- document-related fields, only where legally required; and
- address or contact details, which should be avoided unless strictly needed.



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
9. verify the current reservation state from the booking or PMS system;
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

The credential MAY support the following operational states in the back-end system:

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

Reservation state is not encoded as a credential claim in the APTITUDE issuer
configuration. The verifier SHALL retrieve current state from the authorised booking
or PMS system.

The credential SHOULD NOT be reissued for every PMS state change unless required by
the chosen implementation model.

## 4.6 PMS integration

Where PMS integration exists, the verified booking reference and PID attributes MAY be
used to:

- retrieve the reservation;
- update the guest registration record;
- record successful identity verification;
- complete check-in;
- assign a room;
- trigger room-key issuance; and
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

The verifier SHOULD retain only:

- booking reference or pseudonymous transaction reference;
- hotel identifier;
- verification timestamp;
- check-in outcome; and
- minimum legal-registration data where applicable.



## 4.8 Failure and fallback

The verifier SHALL return `denied`, `not_found` or `manual_review` where:

- signature, trust, validity or status verification fails;
- the booking cannot be found;
- the hotel does not match;
- the booking is cancelled or expired;
- the stay dates are not relevant;
- guest binding cannot be established;
- current reservation state cannot be retrieved where required; or
- applicable legal-registration claims are unavailable.

A staff-assisted reservation lookup SHALL remain possible.

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
- stay dates or hotel change materially;
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

1. the issuer-config claim set
  (`booking_reference`, `hotel_id`, `hotel_name`, `arrival_date`, `departure_date`,
   `booking_platform`);
2. separation of booking reference and PID;
3. separate handling of legal hotel-registration data;
4. authoritative PMS or booking-system state;
5. user consent;
6. status and revocation;
7. minimal intermediary retention; and
8. staff-assisted fallback.

Open matters include:

- final issuer governance model;
- guest-to-PID binding mechanism;
- group-booking and delegation rules;
- final status-list infrastructure;
- whether an mdoc representation is required;
- country-specific hotel-registration profiles; and
- room-key or follow-on stay credential integration.



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


