# Attestation Rulebook for attestations of type Digital Boarding Pass

| Version | Date | Description |
| --- | --- | --- |
| 0.1 | 2026-10-27 | Initial proposal. |

Author(s):

- Leye Yang (Amadeus)
- Hugo LOUP RODRIGUES (Amadeus)
- Nitesh Jha (IATA)

Feedback:

- Nitesh Jha ([jhan@iata.org](mailto:jhan@iata.org))
- Leye Yang ([leye.yang@amadeus.com](mailto:leye.yang@amadeus.com))
- Hugo LOUP RODRIGUES ([hugo.rodrigues@amadeus.com](mailto:hugo.rodrigues@amadeus.com))

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines a Digital Boarding Pass as an Electronic Attestation represented by an ISO/IEC 18013-5 mdoc.

The Digital Boarding Pass contains a Bar Coded Boarding Pass (BCBP) value as
defined by IATA Resolution 792. It is intended for use in the European Digital
Identity Wallet ecosystem and with interoperable wallets beyond Europe.

The attestation represents a passenger's checked-in entitlement for one or
more flight legs. It may be issued by an airline or by an authorised party
acting on behalf of an airline. It may be presented to an airline, airport,
ground handler, security checkpoint, boarding gate, lounge operator, or other
authorised Relying Party.

Representing the boarding pass as a verifiable credential allows Relying
Parties to use established issuer-trust and cryptographic-verification
mechanisms. This helps detect forged or altered boarding passes, reduce fraud,
support data minimisation, and provide a consistent verification method. A
standards-based credential format also supports interoperability with EUDIW and
compatible wallets beyond Europe.

The profile preserves the existing BCBP representation so that mdoc-based
verification can coexist with established airline and airport systems. It
supports remote and proximity presentation and may be presented together with
other credentials, including a Photo ID credential when a contactless travel
use case requires face-image matching.

This Rulebook uses a table-based mdoc definition. Only mandatory BCBP elements that are
generally available SHOULD be required in the baseline profile.

### 1.2 Document structure

This Rulebook is structured as follows:

- **Chapter 2 - Attestation attributes and metadata:** defines the boarding pass data
  model, requirements, structure, and contactless-travel considerations.
- **Chapter 3 - Attestation encoding:** defines the ISO/IEC 18013-5 mdoc
  document type, namespace, `bcbp_string` data element, and value rules.
- **Chapter 4 - Attestation Usage:** defines airline remote issuance, remote
  presentation, standalone and combined presentation, proximity presentation, and seamless journeys without a boarding-pass presentation.
- **Chapter 5 - Trust anchors:** defines trust-model dependencies and the
  distinction between test and production environments.
- **Chapter 6 - Validity and status:** defines validity, replacement, status,
  revocation dependencies, and operational fallback.
- **Chapter 7 - Compliance:** defines mdoc-profile compliance, data
  minimisation, interoperability, and future encoding profiles.
- **Chapter 8 - Considerations for issuance:** defines issuer data sources,
  BCBP validation, multi-leg handling, and identity-matching considerations.
- **Chapter 9 - References:** lists the standards and implementation guides
  used by this Rulebook.

### 1.3 Key words

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

### 1.4 Terminology

| Term | Definition |
| --- | --- |
| Digital Boarding Pass | An mdoc containing the BCBP data element `bcbp_string`. |
| BCBP | Bar Coded Boarding Pass defined by IATA Resolution 792. |
| `bcbp_string` | The text-string mdoc data element containing the BCBP value. |
| Issuer | An airline or authorised party issuing the attestation. |
| Wallet Unit | An EUDI Wallet or another compatible wallet holding and presenting the attestation. |
| Relying Party | An authorised verifier receiving and validating the attestation. |
| Flight leg | One flight coupon represented in the BCBP. |
| DCS | Departure Control System managing check-in and boarding data. |
| mdoc reader | A device or software component requesting and validating an mdoc. |

### 1.5 Out of scope

The following topics are outside the scope of this Rulebook:

- detailed trust-list governance and certificate-policy definition;
- normative wallet user-interface and user-experience requirements;
- airline booking, payment, baggage, immigration, and border-control business
  processes;
- a separate SD-JWT encoding profile. Although the attestation rules defined in this rulebook can be used for creating SD JWT based boarding pass.
- derived credential issuance, including the issuance or self-derivation of a biometric boarding-pass VC after advance biometric verification.
- physical barcode-reader and airport-gate implementation.
- the complete wallet provisioning protocol used to deliver the attestation.

This Rulebook describes dependencies on these topics where necessary for
interoperability, but does not prescribe their implementation.

## 2 Attestation attributes and metadata

### 2.1 Introduction

The Digital Boarding Pass SHALL represent the BCBP data model defined by IATA
Resolution 792. The BCBP multiple-leg format uses format code `M` and supports
one to four flight legs.

The BCBP payload consists of a mandatory fixed-length section followed by an
optional variable-length section. The value may contain conditional fields,
airline individual-use data, structured messages, length indicators, padding,
and security data defined by the BCBP standard.

The baseline profile does not require every optional BCBP field. It requires
the BCBP value to contain the mandatory elements that are generally available
and to preserve the original BCBP encoding and structure.

### 2.2 Requirements on the data model

| ID | Requirement |
| --- | --- |
| DBP-AE-01 | The Digital Boarding Pass SHALL use an ISO/IEC 18013-5-compatible mdoc representation. |
| DBP-AE-02 | The mdoc SHALL use the document type and namespace defined in Chapter 3. |
| DBP-AE-03 | The issuer-signed namespace SHALL contain the mandatory `bcbp_string` data element. |
| DBP-AE-04 | The `bcbp_string` value SHALL follow IATA Resolution 792. |
| DBP-AE-05 | The `bcbp_string` value SHALL preserve BCBP field ordering, padding, length indicators, and required structural sections. |
| DBP-AE-06 | Only mandatory BCBP elements that are generally available SHOULD be required by the baseline profile. |
| DBP-AE-07 | The issuer-signed data SHALL be protected by issuer authentication. |
| DBP-AE-08 | A verifier SHALL reject a value that cannot be parsed or validated as a BCBP. |
| DBP-AE-09 | The BCBP value SHALL NOT be replaced by a second proprietary semantic model. |

### 2.3 BCBP structure

IATA Resolution 792, Version 6, defines the BCBP standard. It specifies:

- format code `M` for the multiple-leg format;
- one to four flight legs;
- mandatory passenger, flight, and check-in data;
- conditional and airline individual-use data; and
- security sections for signing and verification data.

The BCBP variable-size field uses ASCII-printed hexadecimal length indicators.
Where present, the BCBP version header identifies the version marker and
version number. Unique and repeated structured-message fields identify the
lengths of their respective data areas. These values are required for robust
parsing and lossless reconstruction of the BCBP value.

The BCBP may be carried in PDF417, Aztec, QR Code, DataMatrix, or Code 128
representations.

This Rulebook does not prescribe a physical barcode
symbology; `bcbp_string` preserves the BCBP data independent of the storage and rendering
technology.

### 2.4 Contactless travel requirements

For contactless travel, the Relying Party airport touchpoint MAY request the
Digital Boarding Pass together with additional identity related data such as epassport portrait image stored in a Photo ID (ISO 23220-4 Annex C) attestation.

The combined presentation (photoID + digital boarding pass) MAY support identity matching, biometric comparison,
or another airport policy. The Relying Party SHALL request only the minimum
identity and boarding data needed for the decision.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

The Digital Boarding Pass SHALL be encoded as an ISO/IEC 18013-5 mdoc.

The document type is:

```text
org.iata.boardingpass.1
```

The issuer-signed namespace is:

```text
org.iata.bcbp.1
```

The namespace contains the following data element:

```text
bcbp_string
```

The data element SHALL be encoded as a CBOR text string (`tstr`). The string
value SHALL follow IATA Resolution 792.

### 3.2 mdoc profile table

The following table is normative for this profile.

| Field | Value | Description |
| --- | --- | --- |
| `docType` | `org.iata.boardingpass.1` | mdoc document type. It SHALL be present in the mdoc structure. The `.1` suffix identifies version 1 of the document type. |
| Namespace | `org.iata.bcbp.1` | Required issuer-signed namespace holding the BCBP data element. |
| Data-element identifier | `bcbp_string` | Mandatory `tstr` text string as defined by CBOR. It contains the Bar Coded Boarding Pass string encoded as text. The string value SHALL explicitly follow IATA Resolution 792 BCBP. |

The mdoc envelope SHALL use the issuer-authentication and device-authentication
structures required by the applicable ISO/IEC 18013-5 profile.

## 4 Attestation Usage

This section describes how Digital Boarding Pass attestations are intended to
be issued and used. Requested attributes are examples; a Relying Party MAY
request other data required by an approved use case.

### 4.1 Airline remote issuance

At online check-in, the airline or an authorised issuer creates the BCBP value,
validates the booking and DCS data, passenger admissibility for international travel and issues the mdoc to the Wallet Unit. For passenger admissibility during international travel(non-schengen area) airline MAY request additional information which may include APTITUDE DTC and optionally APTITUDE DTA (only for non-existent Interactive Advance Passenger Information System). On successful admissibility check it SHALL issue the boarding pass into the wallet as per the attestation encoding defined in §3.

### 4.2 Proximity presentation at airport touchpoint(s)

It is REQUIRED for on-demand 1:1 biometric matching when the portrait image is not shared in advance.
Other on-demand or offline presentations SHOULD use this profile.

At the day of travel, an airport touchpoint reader MAY present QR code for device engagement. The presentation request MAY include noarding pass to verify the journy details together with travel credential such as APTITUDE DTC to esverifytablish the passenger identity. The proximity flow SHALL follow the [ISO/IEC 18013-5:2021] specification.

Validation will include

- Issuer data authentication of credentials
- Validation of certificate chain
- Mobile security object validation for mdoc
- Check if its not revoked
- If selective disclosure was used then verifying integrity and authenticity of the disclosed data
- Matching portrait image with the face capture by biometric gates. How this is done is out of scope for the rulebook.
- Validating passenger travel data from boarding pass and travel credential to the DCS and other required systems

mdoc validation shall be done as per [ISO/IEC 18013-5:2021] together with [ISO/IEC 18013.2] for revocation checks.

### 4.3 Seamless journey without a boarding-pass presentation

A Digital Boarding Pass is not required in every passenger journey. In a
seamless tap-and-go or similar proximity experience, the passenger may present
an identity attestation alone. The airline or airport system may use the
verified subject or authorised identifier to retrieve booking and boarding
state from the DCS and perform the admissibility decision.

The Digital Boarding Pass MAY be requested as a fallback when the operational
record cannot be retrieved or reconciled.

## 5 Trust anchors

This Rulebook does not define trust-list governance, certificate policy, or
trust-anchor distribution. The issuer and Relying Party SHALL use the recognised trust framework for establishing and validating issuer.

## 6 Validity and status

The mdoc validity information SHALL set `validUntil` to the last-leg journey
departure time or shortly thereafter. The Relying Party SHALL reject an expired
credential or one that does not apply to the current flight and operational
context.

## 7 Compliance

### 7.1 mdoc profile compliance

An implementation claiming compliance with this Rulebook SHALL:

- use `docType` `org.iata.boardingpass.1`;
- use namespace `org.iata.bcbp.1`;
- contain `bcbp_string` encoded as a CBOR text string (`tstr`);
- format `bcbp_string` according to IATA Resolution 792;
- preserve mandatory BCBP structure, ordering, padding, and length indicators;
- protect issuer-signed data using the applicable mdoc authentication; and
- support the required presentation and validation checks.

### 7.2 Data minimisation and interoperability

Only mandatory BCBP elements SHOULD be required by the baseline profile.

The profile supports EUDI Wallets and compatible wallets when the
participating systems implement the same mdoc data model, IATA BCBP value
rules, issuer authentication, and presentation mechanisms.

### 7.3 Other encodings

This Rulebook does not define an SD-JWT profile. A future companion profile
MAY define another SD JWT version based one existing rulebook specifications for mdoc.

## 8 Considerations for issuance

The issuer SHOULD derive `bcbp_string` from an authoritative airline or DCS
record and SHOULD validate it before signing. The issuer SHOULD ensure that
the generally available mandatory BCBP elements are present and SHOULD avoid
making carrier-specific optional data a requirement.

For multi-leg journeys, the issuer SHALL preserve the original BCBP leg order,
length indicators, padding, and all required structural fields.

If the issuer performs identity matching, it SHOULD request only the minimum
PID or Photo ID data needed for that purpose.

Boarding pass data may change before departure several times. The issuer SHALL consider sending the updates and notification to user for re-issuance or refreshing of the existing boarding pass credential and keep this upto date. How to handle the boarding pass update is out of scope for this rulebook.

## 9 References

| Reference | Description |
| --- | --- |
| IATA Resolution 792, Version 6 | Bar Coded Boarding Pass specification, effective June 2016. |
| IATA BCBP Implementation Guide | Technical implementation details for the BCBP standard. |
| ISO/IEC 18013-5:2021 | Mobile document data model, issuer authentication, device engagement, session data, and proximity presentation. |
| ISO/IEC 18013-5.2 |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, second edition|
| ISO/IEC 18013-7 | Complementary online presentation functions for mobile documents. |
