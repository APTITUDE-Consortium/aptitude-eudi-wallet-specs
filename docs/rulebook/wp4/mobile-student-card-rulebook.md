# Mobile Student Card (mSC) Attestation Rulebook

| Version | Date | Description |
|---|---|---|
| 0.1.0 | October 2026 | Initial draft. |
| 0.5.0 | November 2026 | Generic mSC model. Attribute set, use cases, issuance, presentation, trust, technical requirements and conformance. |
| 0.6.0 | November 2026 | Adds design principles, encoding details, verifier obligations, lifecycle, security considerations and references. |
| 0.7.0 | November 2026 | Proximity presentation under ISO/IEC 18013-5 is supported. |

| | |
|---|---|
| Status | Draft for discussion |
| Credential name | Mobile Student Card (mSC) |
| Credential format | ISO/IEC 18013-5 mdoc |
| Issuance protocol | OpenID for Verifiable Credential Issuance (OID4VCI) |
| Presentation | Remote: OpenID for Verifiable Presentations (OID4VP). Proximity: ISO/IEC 18013-5 |
| docType / namespace | Open issue (see §12) |

> **Draft status.** This Rulebook is a draft for discussion. Items marked *open issue* are not yet decided and are listed in §12. Until they are decided, implementations SHALL NOT treat placeholder values in this document as final.

## 1 Introduction

### 1.1 Purpose

This Rulebook defines the **Mobile Student Card (mSC)**, an Electronic Attestation of Attributes (EAA) for the European Digital Identity Wallet (EUDI Wallet).

The mSC expresses one fact: the Holder holds a valid student card issued in relation to an educational establishment, for the stated validity period. It lets the Holder prove that fact, and disclose the cardholder attributes a Relying Party needs, using the selective disclosure built into the mdoc format.

### 1.2 Scope

This Rulebook defines:

* the use cases of the mSC;
* the attributes and their encoding;
* issuance and presentation requirements;
* trust, holder binding, validity and revocation principles;
* privacy, data protection and security requirements;
* conformance criteria.

The following are out of scope:

* diplomas, grades, transcripts, micro-credentials and other achievement records, which are separate attestations;
* alumni or other post-study status;
* the Holder's legal identity, which is provided by the PID.

### 1.3 What the mSC does not prove

The mSC SHALL NOT be interpreted as:

* a Person Identification Data (PID) attestation, or a substitute for one;
* proof of student status after the validity period of the card;
* an entitlement to any benefit. Entitlement depends on the Relying Party's own terms and conditions.

### 1.4 Relationship with other attestations

The mSC sits beside other attestations in the Wallet:

* **PID.** The mSC is bound to the Holder's PID (§7.3). The PID remains the source of the Holder's legal identity. Where a Relying Party needs identity assurance beyond the cardholder attributes, it SHOULD request the relevant PID attributes in a separate presentation.
* **Academic attestations.** Diplomas and other qualifications are separate attestations. The mSC does not carry or replace them.

### 1.5 Key words

The key words SHALL, SHALL NOT, SHOULD, SHOULD NOT and MAY are to be interpreted as described in RFC 2119.

### 1.6 Terms

This document uses the terminology of the EUDI Wallet Architecture and Reference Framework (ARF). In addition:

| Term | Meaning |
|---|---|
| mSC | Mobile Student Card: the attestation defined in this Rulebook. |
| Holder | The natural person to whom the student card was issued, and who holds the mSC in their Wallet. |
| Establishment | The educational establishment the student card relates to. |
| Issuer | An organisation authorised to issue the mSC, as set out in §7.1. |
| Relying Party | An organisation that verifies the mSC to make an access, eligibility, discount or service decision. |
| Mobile Security Object (MSO) | The issuer-signed structure of an mdoc that contains the digests of the data elements, the device key and the validity information, as defined in ISO/IEC 18013-5. |

## 2 Use cases

### 2.1 Student-status verification

The Holder proves that they hold a valid student card at an establishment. The Relying Party verifies the authenticity of the mSC, the trustworthiness of its Issuer and the card's validity, without needing to learn the Holder's identity.

*Example:* an online service offers a student price. It requests `establishment` and `validity` only.

### 2.2 Access to student benefits and services

The Holder presents the mSC to an organisation that grants a service or benefit to students, such as a discount, a campus service, library access or access control. The Relying Party establishes that the mSC was issued by an authorised Issuer, that the card is currently valid and, where necessary, who the cardholder is.

*Example:* a campus library checks that the borrower is a current student and records their name. It requests `establishment`, `validity`, `given_name` and `family_name`.

### 2.3 Student identification

The mSC helps identify the student associated with a student card, for example at an exam or an event reserved for students. The Relying Party requests the identification attributes it needs, as set out in §6.4. Where a visual check is required, it MAY request `portrait`.

### 2.4 Verification of a specific card

Where a Relying Party manages its own records against a card number, for example a registration system, it MAY request `card_number` to identify the specific card.

## 3 Design principles

1. **One card, one attestation.** An mSC SHALL represent one student card, relating to one establishment, for one validity period. A renewed or replaced card is a new mSC.
2. **Minimal mandatory set.** Only the attributes needed in every use case are mandatory. Everything else is optional and issued only where the Issuer holds the data.
3. **Selective disclosure.** Each attribute is a separate mdoc data element. The Holder discloses only the attributes a Relying Party requests and the Holder approves.
4. **Authentic data.** Every attribute SHALL come from the Issuer's records. The Wallet SHALL NOT supply or modify attribute values.
5. **Bound to the Holder.** The mSC is bound to the Wallet device key and to the Holder's PID.
6. **No identity substitute.** The mSC SHALL NOT be used as a substitute for the PID.

## 4 Attributes

> **Subject to change.** The attribute set below is a draft. Attributes, their presence (M/O) and their encodings may change in later versions of this Rulebook.

### 4.1 Attribute table

Each attribute is a separate mdoc data element in the mSC namespace. M = mandatory, O = optional.

| Identifier | M/O | Encoding | Definition |
|---|---|---|---|
| `family_name` | M | tstr | Family name of the cardholder. |
| `given_name` | M | tstr | Given name(s) of the cardholder. |
| `establishment` | M | tstr | Name of the educational establishment the student card relates to. |
| `validity` | M | tstr | Validity period of the student card. |
| `full_name` | O | tstr | Full name of the cardholder. |
| `birth_date` | O | tdate | Date of birth of the cardholder. |
| `card_number` | O | tstr | Number identifying the student card. |
| `student_status` | O | bool | Whether the cardholder has student status. |
| `portrait` | O | bstr | Facial image of the cardholder, provided by the Issuer from its own records. |
| `address` | O | tstr | Postal address of the cardholder. |
| `postal_code` | O | uint | Postal code of the cardholder's address. |
| `city` | O | tstr | City of the cardholder's address. |
| `country` | O | tstr | Country of the cardholder's address. |
| `email` | O | tstr | Email address of the cardholder. |

### 4.2 Attribute rules

* **Mandatory attributes** SHALL be present in every mSC.
* **Optional attributes** MAY be present. The Issuer SHALL include an optional attribute only where it holds a verified value for it.
* `family_name` and `given_name` SHALL match the names held by the Issuer for the cardholder.
* `full_name`, where present, SHALL be consistent with `family_name` and `given_name`.
* `validity` SHALL describe the validity period of the student card. Its exact value format is an open issue.
* `card_number` SHOULD NOT contain directly identifiable personal information, such as a name or date of birth.
* `portrait`, where present, SHALL come from the Issuer's records and SHALL NOT be captured by the Wallet.
* `address`, `postal_code`, `city` and `country` describe the cardholder's address, not the establishment's.

### 4.3 Metadata

The following information is carried by the mdoc structure, not as data elements in the mSC namespace:

| Information | Carried in | Notes |
|---|---|---|
| Credential type | `docType` | Value is an open issue. |
| Issuer | Issuer certificate in `issuerAuth` | Identifies the Issuer and anchors trust (§7.1). |
| Issuance time | MSO `validityInfo.signed` | |
| Credential validity window | MSO `validityInfo.validFrom` / `validUntil` | Checked by every Relying Party (§7.4). |
| Device key | MSO `deviceKeyInfo.deviceKey` | Used for device authentication (§7.3). |

## 5 Issuance

### 5.1 Issuance protocol

The mSC SHALL be issued using OID4VCI, with credential format `mso_mdoc`.

### 5.2 Issuance requirements

Before issuing an mSC, the Issuer SHALL establish:

* the identity of the cardholder;
* the cardholder's given name and family name;
* the establishment the student card relates to;
* the student's status with that establishment;
* the validity of the student card;
* every optional attribute it includes in the mSC.

The Issuer SHALL ensure that every attribute corresponds to the person and the student card for which the mSC is issued.

### 5.3 Issuance flow

A typical issuance follows these steps:

1. the Issuer offers the mSC to the Holder through an OID4VCI credential offer;
2. the Holder's Wallet authenticates to the Issuer and authorises the issuance;
3. the Issuer authenticates the Holder and matches them to its student records;
4. the Issuer establishes the binding to the Holder's PID (mechanism: open issue);
5. the Wallet provides a device public key, which the Issuer places in the MSO;
6. the Issuer signs the MSO and delivers the mSC to the Wallet.

### 5.4 Wallet display and consent

Before accepting the mSC, the Wallet SHOULD display to the Holder:

* the Issuer's name;
* the establishment;
* the cardholder's name;
* the validity period;
* the list of attributes the mSC contains.

## 6 Presentation

### 6.1 Presentation channels

The mSC SHALL support two presentation channels:

* **Remote presentation** using OID4VP, for online services;
* **Proximity presentation** using ISO/IEC 18013-5 device engagement and device retrieval, for in-person checks such as campus access, libraries or ticket desks.

Both channels present the same issued mdoc, with the same `docType`, namespace, data elements, `issuerAuth` and device binding.

### 6.2 Proximity presentation

In proximity presentation:

1. the Wallet and the reader perform device engagement as defined in ISO/IEC 18013-5;
2. they establish an encrypted session and perform device retrieval as defined in ISO/IEC 18013-5;
3. the reader sends a request for the mSC `docType` and the attributes it needs;
4. the Wallet obtains the Holder's approval and returns a response containing only the approved attributes;
5. the reader performs the checks in §6.6.

A reader SHALL be able to verify the issuer signature, the data-element digests, device authentication and `validityInfo` from trust anchors already provisioned to it, without a network connection. Where the reader is offline, it cannot check revocation status at presentation time; how a reader applies status when offline depends on the revocation mechanism (open issue).

### 6.3 Presentation format

The mSC SHALL be presented in the ISO/IEC 18013-5 mdoc format. Only the data elements the Relying Party requests and the Holder approves are disclosed.

### 6.4 Attribute presentation

A Relying Party SHALL request only the attributes necessary for the intended use case.

| Use case | Attributes requested |
|---|---|
| Student-status verification | `establishment`, `validity`, and where present `student_status` |
| Student identification | + `given_name`, `family_name`, and where needed `birth_date` or `portrait` |
| Verification of a specific card | + `card_number` |

A Relying Party SHOULD NOT request `given_name`, `family_name` or `birth_date` where student-status verification can be performed without them.

### 6.5 Holder consent

Before each presentation, the Wallet SHALL show the Holder which Relying Party is requesting which attributes, and SHALL obtain the Holder's approval. The Holder MAY refuse the presentation.

### 6.6 Relying Party obligations

On receiving an mSC presentation, the Relying Party SHALL:

1. confirm that the `docType` is the mSC `docType`;
2. verify the `issuerAuth` signature and the Issuer's certificate chain against a trusted Issuer list (§7.1);
3. recompute the digest of each disclosed data element and match it to the MSO;
4. verify device authentication against the `deviceKey` in the MSO (§7.3);
5. check the MSO `validityInfo` and the disclosed `validity` against the current time (§7.4);
6. where it can, check the status of the mSC (§7.5);
7. confirm that every attribute it requested and requires was disclosed.

### 6.7 Failure handling

The Relying Party SHALL refuse the mSC when:

* the `docType` is not the mSC `docType`;
* the issuer signature, a digest or device authentication fails;
* the Issuer is not on a trusted Issuer list;
* the current time is outside the MSO `validityInfo` or the disclosed `validity`;
* the mSC is known to be revoked or suspended;
* a required attribute is missing.

A refusal of the mSC SHALL NOT by itself prevent the Relying Party from offering another way to prove student status.

## 7 Trust and verification

### 7.1 Issuer trust

Issuers SHALL be authorised and listed according to national priorities, registrars and acceptance processes. A Relying Party SHALL be able to establish that the mSC was issued by an authorised Issuer.

### 7.2 Credential authenticity

The mSC SHALL be cryptographically protected against modification. A Relying Party SHALL verify the issuer signature (`issuerAuth`) and the digests of the disclosed data elements, as defined in ISO/IEC 18013-5.

### 7.3 Holder binding

As required by ISO/IEC 18013-5, the MSO contains the Wallet `deviceKey`, and every presentation includes device authentication. A Relying Party SHALL NOT accept issuer-signed data that is not authenticated by the device for that session.

The mSC SHALL also be bound to the Holder's PID. The binding mechanism is an open issue.

### 7.4 Validity

A Relying Party SHALL NOT accept the mSC outside the `validityInfo` period of its MSO, or outside the period stated in `validity`. The MSO `validUntil` SHOULD NOT be later than the end of the card's validity period.

### 7.5 Revocation and suspension

The Issuer SHOULD revoke or suspend the mSC when:

* the student card is cancelled, lost, stolen or replaced;
* the cardholder no longer has student status with the establishment;
* the Holder's device is lost or compromised;
* the mSC was issued in error;
* the Issuer is no longer authorised.

The revocation and status mechanism is an open issue (Token Status List to be decided).

### 7.6 Lifecycle

* **Renewal.** At the end of the validity period, a new mSC is issued for the new period. The previous mSC is not extended.
* **Update.** Where an attribute changes, the Issuer SHOULD issue a new mSC and revoke the previous one.
* **Deletion.** The Holder MAY delete the mSC from their Wallet at any time.

## 8 Privacy and data protection

The mSC contains personal data about the cardholder. The scheme SHALL follow the principle of data minimisation. In particular:

* identification attributes (`family_name`, `given_name`, `full_name`, `birth_date`, `portrait`) SHOULD be disclosed only when the cardholder must be identified;
* address and contact attributes (`address`, `postal_code`, `city`, `country`, `email`) SHALL NOT be requested for student-status verification;
* `card_number` is a stable identifier, so presentations that disclose it can be linked to each other. It SHOULD be requested only to verify a specific card;
* a Relying Party SHALL NOT request an attribute only because it is available;
* a Relying Party SHOULD NOT store disclosed attributes longer than its purpose requires.

The processing of personal data SHALL comply with applicable data protection legislation, including the GDPR.

## 9 Security considerations

* The Issuer SHALL protect its signing keys and SHALL use signature algorithms permitted by ISO/IEC 18013-5.
* Each data element SHALL be salted as defined in ISO/IEC 18013-5, so that undisclosed values cannot be guessed from their digests.
* Device authentication prevents an mSC copied from one device from being presented from another.
* A Relying Party SHOULD keep its trusted Issuer list up to date.

## 10 Technical requirements

### 10.1 Standards

The mSC SHALL use:

| | |
|---|---|
| Credential format | ISO/IEC 18013-5 mdoc |
| Issuance protocol | OID4VCI, credential format `mso_mdoc` |
| Presentation | OID4VP (remote); ISO/IEC 18013-5 device engagement and device retrieval (proximity) |
| Data elements | As defined in §4, one namespace for all elements |

The mSC SHALL comply with the applicable requirements of these standards.

### 10.2 mdoc structure

Each attribute SHALL be carried as an `IssuerSignedItem` in the mSC namespace, containing a `digestID`, a random salt, the `elementIdentifier` and the `elementValue`, as defined in ISO/IEC 18013-5.

The MSO SHALL contain:

* the `docType`;
* the digest algorithm;
* `valueDigests`, with one digest for every issued data element;
* `deviceKeyInfo.deviceKey`;
* `validityInfo`, with `signed`, `validFrom` and `validUntil`.

The MSO SHALL be signed by the Issuer as a `COSE_Sign1` structure (`issuerAuth`).

### 10.3 CDDL

The CDDL below describes the mSC data elements. The namespace identifier is an open issue.

```cddl
msc_elements = {
  "family_name": tstr,
  "given_name": tstr,
  "establishment": tstr,
  "validity": tstr,
  ? "full_name": tstr,
  ? "birth_date": tdate,
  ? "card_number": tstr,
  ? "student_status": bool,
  ? "portrait": bstr,
  ? "address": tstr,
  ? "postal_code": uint,
  ? "city": tstr,
  ? "country": tstr,
  ? "email": tstr
}
```

## 11 References

* Regulation (EU) 2024/1183 (European Digital Identity Framework).
* EUDI Wallet Architecture and Reference Framework (ARF).
* ISO/IEC 18013-5, Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application.
* OpenID for Verifiable Credential Issuance (OID4VCI).
* OpenID for Verifiable Presentations (OID4VP).
* Regulation (EU) 2016/679 (GDPR).
* RFC 2119, Key words for use in RFCs to Indicate Requirement Levels.

## 12 Open issues

1. docType and namespace identifier.
2. Format of the `validity` value.
3. Mechanism for binding the mSC to the Holder's PID.
4. Revocation and status mechanism (Token Status List to be decided).

## 13 Conformance

An implementation conforms to this Rulebook if:

1. the credential is an ISO/IEC 18013-5 mdoc, issued using OID4VCI, and presentable remotely using OID4VP and in proximity using ISO/IEC 18013-5;
2. the credential contains every mandatory attribute in §4, with the encoding stated there;
3. the Issuer is authorised as set out in §7.1, and meets the issuance requirements in §5.2;
4. the credential is device-bound and bound to the Holder's PID, as set out in §7.3;
5. Relying Parties verify authenticity and validity as set out in §6.6, §7.2 and §7.4;
6. the scheme follows the data-minimisation requirements in §6.4 and §8;
7. the processing of personal data complies with applicable data protection legislation.
