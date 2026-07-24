# Attestation Rulebook for attestations of type Passenger Ferry Boarding Pass

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
> This Rulebook is an implementation-oriented draft. The SEDIT-X Ferry Transport
> working paper defines the credential's purpose, issuer, principal claim set,
> issuance trigger, mdoc format, proximity-presentation mode and verifier checks.
> It does not yet define a final EU-wide document type, namespace, controlled
> vocabularies, status-list endpoint, trust-list endpoint or complete CDDL schema.
> Values identified below as **proposed** or **pilot profile** require confirmation
> through the APTITUDE WP2/WP4 governance process before production use.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Passenger Ferry Boarding Pass**, a ferry-operator-issued
Electronic Attestation of Attributes stored in a passenger's EUDI Wallet.

The attestation represents the passenger-specific right to board a particular ferry
sailing. It is issued after the relevant ferry-booking process has been completed,
including:

1. passenger identity verification;
2. verification of any selected discount or loyalty entitlement;
3. vehicle verification where a vehicle forms part of the booking; and
4. successful payment or another accepted booking-completion condition.

The Passenger Ferry Boarding Pass is intended primarily for rapid proximity
presentation at a port boarding lane, handheld verifier, tablet or other authorised
ferry-boarding terminal. It enables the ferry operator to verify that:

* the credential was issued by an authorised ferry operator or issuer acting for it;
* the credential is cryptographically valid and has not expired or been revoked;
* it relates to the current sailing, route, vessel, departure time and boarding window;
* the passenger presenting it is consistent with the passenger identity or booking
  reference associated with the credential; and
* the passenger is currently entitled to board.

The attestation does not replace the Person Identification Data (PID) credential.
Where passenger-to-ticket binding must be checked at the port, the Passenger Ferry
Boarding Pass is presented together with the minimum required PID attributes.

The credential is distinct from:

* the **Vehicle Ferry Boarding Pass**, which represents a vehicle-specific boarding right;
* the **mVRC**, which provides authoritative vehicle registration attributes;
* a **payment confirmation or eReceipt**, which proves payment completion; and
* a student, loyalty or accessibility attestation used to establish a fare or service
  entitlement during booking.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 defines the attestation attributes and metadata in an
  encoding-independent manner.
* Chapter 3 defines the ISO/IEC 18013-5-compliant mdoc encoding.
* Chapter 4 specifies issuance, presentation and verification usage.
* Chapter 5 defines how trust anchors are obtained.
* Chapter 6 specifies validity, status and revocation.
* Chapter 7 describes compliance with the EUDI Wallet framework and SEDIT-X
  privacy requirements.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119].

In addition, *must* in lower case indicates an external constraint that is not
established by this Rulebook. The word *can* indicates a capability. Other words,
such as *will*, *is* and *are*, are statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the EUDI Wallet
Architecture and Reference Framework.

For this Rulebook:

* **Passenger Ferry Boarding Pass** means the wallet-held attestation defined here.
* **Sailing** means a specific ferry departure operated on a route at a stated date
  and time, normally identified by a sailing or voyage identifier.
* **Boarding window** means the interval during which the credential may be used
  for port boarding.
* **Passenger reference** means a ferry-specific, booking-specific or pairwise
  pseudonymous identifier used to link the boarding entitlement to the passenger.
* **Port verifier** means a ferry employee's verifier application, lane terminal,
  handheld device or other authorised Relying Party Instance used for boarding.
* **Intermediary Service** means the EUDIW Intermediary Service acting on behalf of
  the ferry operator for issuance, verification, trust, status and integration operations.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines all attributes and metadata of the Passenger Ferry Boarding Pass
in an encoding-independent manner.

For the SEDIT-X pilot, the credential is defined as a **non-qualified EAA**. Its
category value is therefore:

```text
eaa:eu:non-qualified
```

The credential SHALL contain the minimum information needed to prove a
passenger-specific right to board a particular sailing. It SHOULD NOT duplicate the
passenger's full civil identity, payment instrument data, discount credential or complete
booking record.

### 2.1 Design principles

The following design principles apply:

1. **Passenger-specific entitlement:** the credential represents the boarding right of
   one passenger for one sailing or an explicitly defined set of connected sailing
   segments.
2. **Separation from identity:** civil identity remains in the PID. The boarding pass
   contains a pseudonymous passenger reference and, where needed, a binding reference.
3. **Separation from payment:** the credential MAY be issued only after payment is
   confirmed, but it SHALL NOT contain sensitive card, bank-account or cryptogram data.
4. **Separation from vehicle entitlement:** a vehicle's right to board is represented by
   a separate Vehicle Ferry Boarding Pass.
5. **Proximity-first design:** the credential SHALL support rapid ISO/IEC 18013-5
   proximity presentation at the port.
6. **Context validation:** cryptographic validation SHALL be combined with checks
   against the current sailing and ferry operational systems.
7. **Data minimisation:** relying parties SHALL request and retain only the minimum
   data necessary for boarding.
8. **Fallback:** failed automated verification SHALL produce a clear denied or
   staff-assisted-review outcome.

### 2.2 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_id` | Unique identifier of the Passenger Ferry Boarding Pass. It SHALL NOT be a civil identity number. | string | `pfbp_01JYRFN7B42W6X8Q9D3K` |
| `passenger_reference` | Pairwise, booking-specific or ferry-specific reference linking the boarding pass to the passenger. | string | `psg_7f2a91c4d3` |
| `booking_reference` | Booking or reservation reference used by the ferry systems to locate the passenger journey. | string | `BOOK-2026-000991` |
| `sailing_id` | Unique identifier of the specific ferry sailing. | string | `rafina-andros-2026-06-15-0730` |
| `route_id` | Identifier of the ferry route. | string | `RFN-AND` |
| `departure_port` | Code or identifier of the departure port. | string | `RFN` |
| `arrival_port` | Code or identifier of the arrival port. | string | `AND` |
| `vessel_id` | Stable identifier of the vessel where available. | string | `IMO-9507891` |
| `vessel_name` | Human-readable vessel name. | string | `Fast Ferries Andros` |
| `departure_datetime` | Scheduled departure date and time, including time-zone offset or UTC representation. | date-time | `2026-06-15T07:30:00+03:00` |
| `boarding_window_start` | Start of the period during which the credential may be used for boarding. | date-time | `2026-06-15T05:45:00+03:00` |
| `boarding_window_end` | End of the period during which the credential may be used for boarding. | date-time | `2026-06-15T07:15:00+03:00` |
| `accommodation_category` | Passenger seat, deck, cabin or accommodation category associated with the ticket. | string | `numbered_seat` |
| `boarding_status` | Current issuer-known state of the passenger boarding entitlement. | string enum | `ready_to_board` |

Permitted values for `boarding_status` SHOULD include:

* `issued`;
* `checked_in`;
* `ready_to_board`;
* `boarded`;
* `cancelled`;
* `suspended`; and
* `expired`.

An issuer SHALL NOT use `boarding_status` as the sole source of truth where a live
ferry operational-system check is available. The verifier SHALL still confirm the
current sailing and booking status.

### 2.3 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `ticket_number` | Ferry ticket number or operator ticket identifier. | string | `TKT-FF-882710` |
| `fare_category` | Fare or tariff category applied to the passenger. | string | `student_discount` |
| `seat_number` | Assigned numbered seat, where applicable. | string | `18A` |
| `cabin_number` | Assigned cabin reference, where applicable. | string | `C-204` |
| `deck` | Assigned passenger deck or boarding area. | string | `Deck 6` |
| `embarkation_area` | Port gate, terminal or boarding area where the passenger should report. | string | `RFN-GATE-02` |
| `check_in_required` | Indicates whether an additional ferry check-in step is required before boarding. | boolean | `false` |
| `boarding_group` | Boarding group, sequence or priority category. | string | `Group B` |
| `carrier_code` | Code identifying the ferry operator. | string | `CFF` |
| `route_description` | Human-readable route description. | string | `Rafina – Andros` |
| `scheduled_arrival_datetime` | Scheduled arrival date and time. | date-time | `2026-06-15T09:25:00+03:00` |
| `discount_basis` | Minimal code indicating the tariff basis, without embedding the underlying entitlement credential. | string | `verified_student_status` |
| `service_entitlements` | Service-related passenger entitlements associated with the ticket. | array of strings | `["priority_boarding"]` |
| `accessibility_service_reference` | Pseudonymous reference indicating that an operational accessibility request exists. | string | `ssr_01JYR9...` |
| `display_qr_payload` | Optional operator QR/barcode payload for compatibility with existing port scanners. | binary or string | `M1FF...` |
| `terms_and_conditions_uri` | URI for the applicable ferry carriage terms. | URI | `https://ferry.example/terms` |

The `discount_basis` attribute SHALL NOT disclose a full Student Credential, Loyalty
Credential or Disability Attestation. It MAY state only the tariff basis that was applied
and verified during booking.

The `display_qr_payload` is not a substitute for mdoc verification. Where included, it
MAY support backward compatibility with legacy ferry scanning infrastructure.

### 2.4 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `subject_binding_reference` | Reference used to compare the Passenger Ferry Boarding Pass to a PID presentation. Mandatory where the ferry boarding policy requires explicit passenger-to-PID binding at the port. | string | `pid-bind:8a71...` |
| `guardian_booking_reference` | Booking reference of the responsible adult. Present where a child passenger is represented under an approved dependent-travel policy. | string | `BOOK-2026-000990` |
| `group_booking_reference` | Identifier of a group booking where the credential forms part of a group-travel arrangement. | string | `GRP-2026-0715-22` |
| `connected_sailings` | Additional ferry sailing segments explicitly covered by the same credential. | array of objects | `[{"sailing_id":"myk-nax-2026-06-16-1100"}]` |
| `cryptographically_bound_to` | Attestation type to which this credential is cryptographically bound. Present where the deployment applies formal cross-credential binding. | string | `urn:eu.europa.ec.eudi:pid:1` |

Where `cryptographically_bound_to` is present, its value SHALL identify the PID type
used for passenger binding:

```text
urn:eu.europa.ec.eudi:pid:1
```

The source material requires consistency between the PID subject and the passenger
boarding pass subject or booking reference. The exact cryptographic cross-credential
binding mechanism remains to be confirmed by the APTITUDE profile.

### 2.5 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the ferry operator or Attestation Provider acting for it. | string or URI | `https://issuer.fastferries.example` |
| `credential_type` | Encoding-independent credential type identifier. | string | `urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1` |
| `issued_at` | Date and time at which the credential was issued. | date-time | `2026-06-12T10:35:22Z` |
| `valid_from` | Start of the credential-validity period. | date-time | `2026-06-12T10:35:22Z` |
| `valid_until` | End of the credential-validity period. | date-time | `2026-06-15T09:00:00+03:00` |
| `schema_version` | Version of the credential schema. | string | `0.1` |
| `status_reference` | Reference used to check credential status or revocation. | URI or structured value | `https://status.fastferries.example/atl/2026-06/12#991` |
| `trust_anchor_reference` | Location from which applicable issuer trust information can be obtained. | URI | `https://trust.aptitude.example/ferry-issuers` |

The identifiers and URLs above are illustrative and SHALL be replaced by values approved
through APTITUDE governance.

### 2.6 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_name` | Human-readable wallet display name. | string | `Passenger Ferry Boarding Pass` |
| `credential_description` | Human-readable explanation of the credential. | string | `Boarding pass for Rafina to Andros` |
| `issuer_name` | Human-readable ferry operator or issuing service name. | string | `Cyclades Fast Ferries` |
| `issuer_logo_uri` | URI of the issuer logo displayed by the Wallet Unit. | URI | `https://issuer.example/logo.png` |
| `privacy_notice` | Reference to the relevant privacy information. | URI | `https://ferry.example/eudi/privacy` |
| `issuer_policy` | Reference to the credential issuance and verification policy. | URI | `https://ferry.example/eudi/issuer-policy` |
| `display_locale` | Preferred language for wallet display. | string | `en` |

### 2.7 Conditional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `status_list_index` | Entry index in an applicable Attestation Status List. Mandatory when list-based status is used. | integer | `991` |
| `status_list_uri` | URI of the applicable Attestation Status List. Mandatory when list-based status is used. | URI | `https://status.fastferries.example/atl/2026-06/12` |
| `revocation_list_uri` | URI of the applicable Attestation Revocation List. Mandatory when a revocation-list mechanism is used. | URI | `https://status.fastferries.example/arl/2026-06` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

### 3.1.1 Document type

The proposed mdoc document type is:

```text
urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1
```

This is a pilot identifier and requires confirmation by the APTITUDE
schema-governance process.

### 3.1.2 Namespace

The proposed attribute namespace is:

```text
urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1
```

The `category` metadata SHALL use the applicable ETSI namespace:

```text
org.etsi.01947201.010101
```

### 3.1.3 Encoding conventions

The following encoding conventions apply:

* `tstr`, `uint`, `bstr`, `bool` and `tdate` are CDDL representation types defined
  in [RFC 8610] and [RFC 8949].
* A `tstr` SHALL be UTF-8 encoded.
* Unless an attribute definition specifies otherwise, a `tstr` SHALL have a maximum
  length of 150 characters.
* A `tdate` SHALL contain an RFC 3339 date-time value.
* Fractions of seconds SHOULD NOT be used.
* Date-time values SHALL include either `Z` or an explicit local offset.
* CBOR deterministic-encoding rules SHALL be applied.
* Indefinite-length CBOR items SHALL NOT be used.
* Port and carrier codes SHOULD use established operator, IATA, UN/LOCODE or
  nationally recognised codes where available.
* Controlled vocabulary values SHALL be lower-case ASCII strings unless another
  profile explicitly defines a different representation.

### 3.1.4 Attribute mapping

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace** |
|---------------------|--------------------------|---------------------|---------------|
| `credential_id` | `credential_id` | tstr | `urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1` |
| `passenger_reference` | `passenger_reference` | tstr | same |
| `booking_reference` | `booking_reference` | tstr | same |
| `sailing_id` | `sailing_id` | tstr | same |
| `route_id` | `route_id` | tstr | same |
| `departure_port` | `departure_port` | tstr | same |
| `arrival_port` | `arrival_port` | tstr | same |
| `vessel_id` | `vessel_id` | tstr | same |
| `vessel_name` | `vessel_name` | tstr | same |
| `departure_datetime` | `departure_datetime` | tdate | same |
| `boarding_window_start` | `boarding_window_start` | tdate | same |
| `boarding_window_end` | `boarding_window_end` | tdate | same |
| `accommodation_category` | `accommodation_category` | tstr | same |
| `boarding_status` | `boarding_status` | tstr | same |
| `ticket_number` | `ticket_number` | tstr | same |
| `fare_category` | `fare_category` | tstr | same |
| `seat_number` | `seat_number` | tstr | same |
| `cabin_number` | `cabin_number` | tstr | same |
| `deck` | `deck` | tstr | same |
| `embarkation_area` | `embarkation_area` | tstr | same |
| `check_in_required` | `check_in_required` | bool | same |
| `boarding_group` | `boarding_group` | tstr | same |
| `carrier_code` | `carrier_code` | tstr | same |
| `route_description` | `route_description` | tstr | same |
| `scheduled_arrival_datetime` | `scheduled_arrival_datetime` | tdate | same |
| `discount_basis` | `discount_basis` | tstr | same |
| `service_entitlements` | `service_entitlements` | array of tstr | same |
| `accessibility_service_reference` | `accessibility_service_reference` | tstr | same |
| `display_qr_payload` | `display_qr_payload` | bstr or tstr | same |
| `subject_binding_reference` | `subject_binding_reference` | tstr | same |
| `guardian_booking_reference` | `guardian_booking_reference` | tstr | same |
| `group_booking_reference` | `group_booking_reference` | tstr | same |
| `connected_sailings` | `connected_sailings` | array of maps | same |
| `cryptographically_bound_to` | `cryptographically_bound_to` | tstr | same |
| `issued_at` | `issued_at` | tdate | same |
| `valid_from` | `valid_from` | tdate | same |
| `valid_until` | `valid_until` | tdate | same |
| `schema_version` | `schema_version` | tstr | same |
| `status_reference` | `status_reference` | tstr or map | same |
| `trust_anchor_reference` | `trust_anchor_reference` | tstr | same |
| `category` | `category` | tstr | `org.etsi.01947201.010101` |

In the table above, `same` means:

```text
urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1
```

### 3.1.5 Selective disclosure policy

For ISO/IEC 18013-5 presentation requests, the Relying Party SHALL request only the
attributes needed for the current boarding decision.

A normal port-boarding request SHOULD request:

* `credential_id`;
* `passenger_reference`;
* `booking_reference`;
* `sailing_id`;
* `departure_port`;
* `arrival_port`;
* `vessel_id` or `vessel_name`;
* `departure_datetime`;
* `boarding_window_start`;
* `boarding_window_end`;
* `boarding_status`;
* `valid_until`; and
* `status_reference`.

The following SHOULD be requested only where operationally needed:

* seat, cabin or deck allocation;
* fare category or discount basis;
* accessibility service reference;
* ticket number;
* group or guardian references; and
* legacy QR payload.

### 3.1.6 Illustrative mdoc data set

The following example is a human-readable representation of the attributes contained
in an illustrative mdoc. It is not a complete CBOR or COSE serialisation.

```json
{
  "docType": "urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1",
  "nameSpaces": {
    "urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1": {
      "credential_id": "pfbp_01JYRFN7B42W6X8Q9D3K",
      "passenger_reference": "psg_7f2a91c4d3",
      "booking_reference": "BOOK-2026-000991",
      "sailing_id": "rafina-andros-2026-06-15-0730",
      "route_id": "RFN-AND",
      "departure_port": "RFN",
      "arrival_port": "AND",
      "vessel_id": "IMO-9507891",
      "vessel_name": "Fast Ferries Andros",
      "departure_datetime": "2026-06-15T07:30:00+03:00",
      "boarding_window_start": "2026-06-15T05:45:00+03:00",
      "boarding_window_end": "2026-06-15T07:15:00+03:00",
      "accommodation_category": "numbered_seat",
      "seat_number": "18A",
      "boarding_status": "ready_to_board",
      "carrier_code": "CFF",
      "issued_at": "2026-06-12T10:35:22Z",
      "valid_from": "2026-06-12T10:35:22Z",
      "valid_until": "2026-06-15T09:00:00+03:00",
      "schema_version": "0.1",
      "status_reference": "https://status.fastferries.example/atl/2026-06/12#991",
      "trust_anchor_reference": "https://trust.aptitude.example/ferry-issuers"
    },
    "org.etsi.01947201.010101": {
      "category": "eaa:eu:non-qualified"
    }
  }
}
```

The actual mdoc SHALL additionally contain the issuer-signed and device-signed
structures, validity information, issuer authentication and other elements required by
the applicable ISO/IEC 18013-5 and EUDI Wallet profiles.

## 3.2 SD-JWT VC-based encoding

Version 0.1 of this Rulebook does not define an SD-JWT VC representation for the
Passenger Ferry Boarding Pass.

The SEDIT-X Ferry Transport working paper explicitly selects mdoc because the
credential must support rapid ISO/IEC 18013-5 proximity presentation at the port.

A future version MAY add SD-JWT VC as an additional remote-presentation format only
if:

* the APTITUDE profile requires it;
* the same semantic claim model is preserved;
* status and passenger-binding semantics remain equivalent; and
* use of SD-JWT VC does not replace the mandatory mdoc capability for the target port flow.

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 of this Rulebook does not define a W3C Verifiable Credentials Data Model
representation.

## 4 Attestation usage

### 4.1 Issuance trigger and prerequisites

The ferry company or an authorised Attestation Provider acting for it SHALL issue the
Passenger Ferry Boarding Pass only after the booking process has reached an accepted
issuance state.

Before issuance, the issuer SHALL confirm:

1. the ferry booking exists;
2. the passenger identity attributes required for booking have been verified;
3. the passenger reference has been bound to the booking;
4. any selected student, loyalty, disability or other discount entitlement has been
   verified according to the applicable tariff rules;
5. where a vehicle is booked, the required vehicle verification has completed;
6. payment has succeeded or another accepted settlement condition has been met;
7. the sailing, route, vessel and departure details are available; and
8. the credential validity and boarding window have been calculated.

The issuer SHALL display to the User:

* the credential type;
* the issuer;
* the sailing and route;
* the departure date and time;
* the passenger or booking reference;
* the validity period;
* the purpose of the credential; and
* the main attributes that will be included.

The credential SHALL be issued using OpenID4VCI or another issuer-mediated wallet
issuance flow approved by APTITUDE.

The User SHALL consent to receiving and storing the credential in the Wallet Unit.

### 4.2 Device and holder binding

The Passenger Ferry Boarding Pass **SHOULD be device-bound** to a key controlled by
the Wallet Unit.

Where the selected EUDI Wallet mdoc profile requires device authentication, the issuer
SHALL provision the credential so that the Wallet Unit can produce the required
device-signed response during proximity presentation.

The credential SHALL be associated with the passenger through
`passenger_reference`, `booking_reference` and, where required,
`subject_binding_reference`.

The source material requires the verifier to confirm that the PID subject is consistent
with the Passenger Ferry Boarding Pass subject or booking reference. Accordingly, the
port policy SHOULD request a PID presentation whenever the ferry operator needs to
confirm that the person presenting the boarding pass is the booked passenger.

The credential SHALL NOT be freely transferable to another Wallet Unit or passenger.

### 4.3 Presentation mode

The primary presentation mode is an ISO/IEC 18013-5 proximity exchange between the
Wallet Unit and a port verifier.

The flow SHOULD follow these steps:

1. the ferry employee or lane terminal selects the current sailing or boarding-lane context;
2. the verifier creates or obtains the applicable presentation policy;
3. the Wallet Unit and verifier perform device engagement, for example through NFC;
4. the Wallet Unit authenticates or evaluates the Relying Party where applicable;
5. the Wallet Unit displays the requested credentials, attributes and purpose;
6. the User authenticates locally and approves or refuses the presentation;
7. the Wallet Unit returns the mdoc response over the negotiated proximity channel;
8. the verifier or Intermediary Service validates the response; and
9. the ferry system returns `granted`, `denied` or `manual_review`.

For a passenger-only booking, a normal presentation SHOULD include:

* Passenger Ferry Boarding Pass; and
* PID attributes required for passenger-to-ticket binding, where required by policy.

For a booking with a vehicle, the combined presentation SHOULD additionally include:

* Vehicle Ferry Boarding Pass; and
* mVRC attributes required for vehicle-to-ticket binding.

### 4.4 Relying Party obligations

The port verifier or EUDIW Intermediary Service SHALL:

1. verify the issuer signature and credential integrity;
2. verify that the issuer is trusted and authorised to issue the credential type;
3. verify the credential validity period;
4. verify status or revocation information;
5. verify mdoc device authentication and session binding;
6. verify that the credential is valid for the selected sailing;
7. verify the vessel, route, departure port, arrival port and departure date/time;
8. verify that the current time falls within the permitted boarding window;
9. verify that `boarding_status` and the current ferry operational record permit boarding;
10. where PID is requested, verify that the PID subject or disclosed binding data is
    consistent with the passenger reference or booking record;
11. reject replay, duplicate-use or already-boarded presentations according to the
    ferry operator's policy;
12. return a clear access decision; and
13. record only the minimum operational event needed for boarding control and audit.

A successful verification result SHOULD be limited to data such as:

```json
{
  "boarding_pass_valid": true,
  "passenger_binding_valid": true,
  "sailing_valid": true,
  "boarding_window_valid": true,
  "decision": "granted",
  "correlation_id": "pvs_01HY2B8MMQ21"
}
```

The relying party SHALL NOT retain full copies of the presented mdoc or PID unless
there is a clearly defined legal or operational requirement.

### 4.5 Operational boarding event

After successful verification, the ferry system MAY record a minimal boarding event
containing:

* sailing identifier;
* boarding lane or verifier-device identifier;
* timestamp;
* booking reference or pseudonymous transaction identifier;
* event type;
* verification outcome; and
* operator identifier where staff accountability requires it.

The event SHOULD NOT contain:

* a complete credential copy;
* unnecessary PID attributes;
* the underlying student, loyalty or disability credential;
* sensitive payment data; or
* unrelated vehicle-registration data.

### 4.6 Offline and degraded operation

The proximity exchange itself SHALL be capable of operating locally according to the
selected ISO/IEC 18013-5 profile.

The deployment profile SHALL define whether a verifier may make a boarding decision
when it cannot reach:

* credential status infrastructure;
* the ferry booking or ticketing system;
* the sailing manifest; or
* the EUDIW Intermediary Service.

Any offline acceptance policy SHALL define:

* maximum cache age;
* accepted issuer and certificate cache;
* permitted credential-validity margin;
* duplicate-use controls;
* reconciliation behaviour; and
* conditions requiring staff-assisted review.

The credential's cryptographic validity alone does not prove that the booking has not
been cancelled or that the passenger has not already boarded.

### 4.7 Transactional data

This attestation is not a payment credential.

The credential MAY be issued only after a payment-completion result is received, but it
SHALL NOT contain:

* card PAN;
* IBAN;
* payment cryptogram;
* payment access token;
* account credentials; or
* other sensitive payment-instrument data.

A transaction reference or eReceipt SHALL be handled as a separate attestation or
operational record.

### 4.8 Failure and fallback

The verifier SHALL return `denied` or `manual_review` when:

* signature, trust, status or validity verification fails;
* the credential is not valid for the selected sailing;
* the boarding window is not open;
* the booking has been cancelled, replaced or already consumed;
* the PID-to-passenger binding cannot be established where required;
* the verifier cannot validate a necessary current operational condition;
* the mdoc response is malformed or replayed; or
* ferry policy requires a staff check.

The ferry employee or lane terminal SHALL receive a clear outcome without unnecessary
exposure of credential claims.

## 5 Trust anchors

The Passenger Ferry Boarding Pass is a non-qualified EAA issued by:

* a ferry operator;
* an authorised ticketing or travel-agency issuer acting for the ferry operator; or
* an EUDIW Intermediary Service acting on behalf of the ferry operator.

For the APTITUDE pilot, the Relying Party SHALL obtain issuer trust information through
the APTITUDE trust framework and the applicable trusted issuer list established by WP2.

The `trust_anchor_reference` metadata SHALL identify the machine-readable location
from which applicable issuer trust information can be obtained.

The production trust model SHALL define:

1. the entity authorised to register ferry boarding-pass issuers;
2. the trusted-list or List of Trusted Entities structure;
3. the service type used for authorised ferry-ticket issuers;
4. whether a travel agency may issue directly or only under delegation from the ferry operator;
5. certificate and mdoc issuer-authentication profiles;
6. permitted issuer scope, including ferry operator, route or service constraints;
7. key rollover and compromise handling; and
8. Wallet Unit and verifier behaviour where trust information cannot be retrieved.

A verifier SHALL verify both:

* that the issuer authentication chain terminates in an accepted trust anchor; and
* that the issuer is authorised to issue
  `urn:aptitude.eu:seditx:passenger-ferry-boarding-pass:1`.

The illustrative domain names in this Rulebook are not operational trust endpoints.

## 6 Revocation

### 6.1 Validity model

The credential SHALL be journey-specific.

Its `valid_until` value SHALL NOT extend beyond the operational period required for the
sailing plus a limited post-departure grace period.

The issuer SHOULD align the validity period with:

* the booking-confirmation time;
* the boarding-window opening and closing times;
* the scheduled departure;
* possible operational delays; and
* the maximum period during which the ticket may legitimately be presented.

A sailing delay MAY extend operational acceptance only where:

* the ferry system confirms the delay;
* the credential remains otherwise valid; and
* the verifier's policy explicitly allows the extension.

### 6.2 Revocation and status

The Passenger Ferry Boarding Pass SHALL be status-checkable.

The issuer SHALL invalidate or update the status of the credential when, for example:

* the booking is cancelled;
* the ticket is refunded;
* the passenger is rebooked to another sailing;
* the sailing is cancelled and the credential is no longer applicable;
* a replacement boarding pass is issued;
* fraud or erroneous issuance is detected;
* the Wallet Unit or credential is reported compromised; or
* the passenger has boarded and the operator uses consumed-ticket status.

The verifier SHALL check both:

1. the credential status mechanism; and
2. the ferry operator's current booking and boarding state, where available.

### 6.3 Status-list mechanism

The target APTITUDE implementation SHOULD use the status-list mechanism selected by
APTITUDE WP2 and aligned with the applicable EUDI Wallet Technical Specification.

The final production URL for the relevant Attestation Status List or Attestation
Revocation List has not yet been defined.

The issuer policy SHALL publish at least the domain from which applicable status data
can be retrieved. The individual credential SHALL contain the specific status reference
required by the selected mechanism.

Illustrative pilot value:

```text
https://status.fastferries.example/
```

This value SHALL NOT be treated as an operational endpoint.

## 7 Compliance

This Rulebook is designed to align with:

* Regulation (EU) 2024/1183 establishing the European Digital Identity Framework;
* the EUDI Wallet Architecture and Reference Framework;
* the Attestation Rulebook requirements in Topic 12 of ARF Annex 2;
* the issuance and presentation profiles selected by APTITUDE;
* ISO/IEC 18013-5 proximity presentation;
* the SEDIT-X Ferry Transport working paper;
* GDPR principles of purpose limitation, data minimisation, storage limitation,
  integrity and confidentiality; and
* ferry operational requirements for booking, ticketing, boarding and audit.

The Rulebook enforces the following properties:

1. the attestation is a purpose-bound, non-qualified EAA;
2. it represents a passenger-specific boarding entitlement;
3. it is issued only after the required booking checks;
4. it is designed for mdoc proximity presentation;
5. it is associated with the passenger without unnecessarily duplicating civil identity;
6. it remains separate from vehicle, payment and discount credentials;
7. user authentication and consent are required for presentation;
8. cryptographic checks are combined with sailing-context checks;
9. status and revocation checks are required;
10. only minimal operational logs are retained; and
11. a staff-assisted fallback is available.

The following matters remain open and SHALL be resolved before a final production
version is published:

* final mdoc document type and namespace;
* final CDDL and maximum-length constraints;
* final port, vessel, route and carrier code systems;
* final passenger-to-PID binding mechanism;
* final holder/device-binding profile;
* final trust-list service type and endpoint;
* final status-list or revocation-list mechanism and endpoint;
* offline acceptance and cache policy;
* duplicate-use and consumed-ticket semantics;
* legacy QR/barcode compatibility profile; and
* legal retention requirements for boarding events.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
| [SEDIT-X Ferry Working Paper] | APTITUDE WP4, SEDIT-X Ferry Transport, “Ferry Transport using the EUDI Wallet for booking, vehicle entitlement verification, wallet-based payment, and proximity boarding”, Version 0.1, May 2026 |
| [ARF] | European Digital Identity Wallet Architecture and Reference Framework |
| [ISO/IEC 18013-5] | ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence application |
| [OpenID4VCI] | OpenID for Verifiable Credential Issuance |
| [OpenID4VP] | OpenID for Verifiable Presentations |
| [RFC 2119] | Key words for use in RFCs to Indicate Requirement Levels |
| [RFC 3339] | Date and Time on the Internet: Timestamps |
| [RFC 8610] | Concise Data Definition Language |
| [RFC 8949] | Concise Binary Object Representation |
| [Topic 7] | ARF Annex 2, Topic 7 — Attestation revocation and revocation checking |
| [Topic 10] | ARF Annex 2, Topic 10 — Issuing a PID or attestation to a Wallet Unit |
| [Topic 12] | ARF Annex 2, Topic 12 — Attestation Rulebooks |
| [ETSI TS 119 472-1] | Electronic Signatures and Trust Infrastructures; Electronic Attestation of Attributes; Part 1: Building blocks and general requirements |
