# Attestation Rulebook for attestations of type Ferry Loyalty Credential

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
> working paper defines the Ferry Loyalty Credential at a high level as an optional
> credential issued by a ferry company or loyalty programme and used during remote
> booking to prove eligibility for loyalty benefits, points, tier benefits or discounts.
>
> The source material identifies the principal presentation subset as a loyalty identifier
> or pseudonymous member reference, tier or benefit entitlement, and validity period.
> It does not define a final credential type identifier, complete claim model, encoding,
> controlled vocabularies, trust-list endpoint or status-list endpoint. Values marked as
> **proposed** or **pilot profile** require confirmation through APTITUDE governance.

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the **Ferry Loyalty Credential**, a ferry-operator or loyalty-
programme-issued Electronic Attestation of Attributes stored in a User's EUDI Wallet.

The credential represents the User's membership in a ferry loyalty programme and,
where applicable, one or more verified loyalty benefits.

It may be used during ferry booking to:

* identify the User as a loyalty-programme member;
* prove a loyalty tier;
* prove eligibility for a fare discount;
* prove eligibility for priority or enhanced services;
* associate a booking with the loyalty account;
* accrue or redeem points, where supported; and
* reduce repeated manual entry of loyalty account details.

The credential is optional. It SHALL be requested only where the User selects or expects
a loyalty-related benefit.

The credential does not replace:

* PID, which provides civil identity;
* a Passenger Ferry Boarding Pass, which proves the right to board a sailing;
* a payment credential or payment confirmation;
* a Student Status Credential or other independent discount entitlement; or
* the loyalty programme's back-end account and ledger.

The credential SHOULD function primarily as portable proof of membership and
entitlement. The loyalty programme back end remains authoritative for mutable balances,
redemption history and account state unless the selected profile explicitly supports
those attributes.

### 1.2 Document structure

This Rulebook is structured as follows:

* Chapter 2 defines attributes and metadata in an encoding-independent manner.
* Chapter 3 defines the proposed SD-JWT VC encoding.
* Chapter 4 specifies issuance, presentation and verifier obligations.
* Chapter 5 defines trust-anchor requirements.
* Chapter 6 specifies validity, suspension and revocation.
* Chapter 7 describes compliance and privacy requirements.
* Chapter 8 lists references.

### 1.3 Key words

This document uses the capitalised key words **SHALL**, **SHOULD** and **MAY** as
specified in [RFC 2119].

### 1.4 Terminology

For this Rulebook:

* **Loyalty programme** means a ferry-operator or multi-operator programme that grants
  benefits based on membership, tier, activity or another approved rule.
* **Loyalty member reference** means a programme-specific or pairwise pseudonymous
  identifier for the holder.
* **Tier** means the programme level assigned to the member.
* **Benefit entitlement** means a verified right to a discount, priority service, points
  multiplier or another loyalty-programme benefit.
* **Points balance** means the mutable number of loyalty points associated with the
  member's account.
* **Ferry operator** means the company providing the ferry service and acting as issuer,
  verifier or both.
* **Intermediary Service** means the EUDIW integration layer acting for the ferry operator.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

For the SEDIT-X pilot, the credential is defined as a **non-qualified EAA**.

```text
eaa:eu:non-qualified
```

The credential SHALL contain only the information needed to prove loyalty membership
and applicable benefits.

### 2.1 Design principles

1. **Pseudonymous membership:** the credential SHOULD use a programme-specific or
   pairwise member reference rather than a civil identity identifier.
2. **Minimum disclosure:** a verifier SHOULD request only the membership, tier or
   benefit needed for the booking.
3. **Separation from identity:** PID SHALL be requested separately only where required.
4. **Separation from payment:** the credential SHALL NOT contain payment-instrument data.
5. **Separation from ticketing:** the credential does not itself grant a right to travel.
6. **Mutable data caution:** balances and redemption state SHOULD remain authoritative
   in the loyalty back end unless a freshness mechanism is defined.
7. **User control:** presentation SHALL require User approval.
8. **No default request:** the credential SHALL NOT be requested where no loyalty benefit
   is relevant to the transaction.

### 2.2 Mandatory attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_id` | Unique identifier of the Ferry Loyalty Credential. | string | `flc_01JZ5L8M2A7P9Q4R6T3V` |
| `member_reference` | Loyalty-programme identifier or pseudonymous member reference. | string | `member_f8a72c91` |
| `programme_id` | Identifier of the loyalty programme. | string | `fast_ferries_rewards` |
| `programme_name` | Human-readable programme name. | string | `Fast Ferries Rewards` |
| `membership_status` | Current membership state. | string enum | `active` |
| `valid_from` | Start date or time of validity. | date or date-time | `2026-01-01` |
| `valid_until` | End date or time of validity. | date or date-time | `2027-12-31` |

Permitted values for `membership_status` SHOULD include:

* `active`;
* `suspended`;
* `closed`;
* `expired`; and
* `pending_review`.

### 2.3 Optional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `tier` | Current loyalty tier. | string | `gold` |
| `tier_valid_from` | Start date of the current tier. | date | `2026-04-01` |
| `tier_valid_until` | End date of the current tier. | date | `2027-03-31` |
| `benefit_entitlements` | Verified benefits associated with membership or tier. | array of strings | `["fare_discount","priority_boarding"]` |
| `discount_percentage` | Discount directly granted by the programme. | integer | `10` |
| `points_multiplier` | Multiplier applied to point accrual. | number | `1.5` |
| `priority_boarding` | Indicates entitlement to priority boarding. | boolean | `true` |
| `priority_support` | Indicates entitlement to priority customer support. | boolean | `true` |
| `lounge_access` | Indicates access to an applicable ferry lounge or premium area. | boolean | `false` |
| `free_change_entitlement` | Indicates eligibility for free or discounted booking changes. | boolean | `true` |
| `free_baggage_entitlement` | Indicates an additional baggage entitlement where relevant. | boolean | `false` |
| `partner_benefits` | Benefits recognised by partner organisations. | array of strings | `["hotel_partner_discount"]` |
| `issuing_operator_id` | Identifier of the ferry operator responsible for the programme. | string | `fast-ferries-gr` |
| `issuing_operator_name` | Human-readable ferry operator name. | string | `Fast Ferries` |
| `account_created_at` | Date when loyalty membership was created. | date | `2023-06-15` |
| `display_member_number` | Masked or display-friendly loyalty number. | string | `FFR-••••-4821` |
| `programme_terms_uri` | URI of loyalty programme terms. | URI | `https://ferry.example/loyalty/terms` |

### 2.4 Conditional attributes

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `points_balance` | Current points balance. Present only where the profile defines freshness and ledger synchronisation. | integer | `1840` |
| `points_balance_as_of` | Time at which the disclosed points balance was authoritative. Mandatory when `points_balance` is present. | date-time | `2026-07-23T08:45:00Z` |
| `redeemable_points` | Points available for redemption. Conditional where redemption is supported through the credential flow. | integer | `1500` |
| `benefit_scope` | Routes, operators, fare classes or services to which a benefit applies. Mandatory where a benefit is restricted. | array of strings | `["domestic_routes","economy_fare"]` |
| `subject_binding_reference` | Reference used to bind the loyalty member to PID or another identity credential. Present where strong identity binding is required. | string | `pid-bind:2f81...` |
| `cryptographically_bound_to` | Credential type to which formal binding is applied. | string | `urn:eu.europa.ec.eudi:pid:1` |

`points_balance` SHOULD NOT be included in a long-lived credential unless:

* the issuer can refresh or reissue it;
* the timestamp is clearly visible;
* the verifier checks freshness; and
* the loyalty back end remains authoritative.

### 2.5 Mandatory metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `category` | Legal category of the attestation. | string | `eaa:eu:non-qualified` |
| `issuer` | Identifier of the ferry operator or loyalty Attestation Provider. | string or URI | `https://loyalty.fastferries.example` |
| `credential_type` | Encoding-independent credential type identifier. | string | `urn:aptitude.eu:seditx:ferry-loyalty-credential:1` |
| `issued_at` | Date and time of issuance. | date-time | `2026-07-23T08:45:00Z` |
| `schema_version` | Version of the credential schema. | string | `0.1` |
| `status_reference` | Reference for status or revocation checking. | URI or structured value | `https://status.fastferries.example/loyalty/atl/42#812` |
| `trust_anchor_reference` | Location of applicable trust information. | URI | `https://trust.aptitude.example/ferry-loyalty-issuers` |

### 2.6 Optional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `credential_name` | Human-readable wallet name. | string | `Ferry Loyalty Credential` |
| `credential_description` | Human-readable explanation. | string | `Fast Ferries Rewards membership and benefits` |
| `issuer_name` | Human-readable issuer name. | string | `Fast Ferries` |
| `issuer_logo_uri` | URI of issuer logo. | URI | `https://ferry.example/logo.png` |
| `privacy_notice` | URI of the privacy notice. | URI | `https://ferry.example/loyalty/privacy` |
| `issuer_policy` | URI of issuance and verification policy. | URI | `https://ferry.example/loyalty/policy` |
| `display_locale` | Preferred display language. | string | `en` |

### 2.7 Conditional metadata

| **Data Identifier** | **Definition** | **Data type** | **Example value** |
|---------------------|----------------|---------------|-------------------|
| `status_list_index` | Status-list entry index. | integer | `812` |
| `status_list_uri` | Status-list URI. | URI | `https://status.fastferries.example/loyalty/atl/42` |
| `revocation_list_uri` | Revocation-list URI where used. | URI | `https://status.fastferries.example/loyalty/arl/2026-07` |

# 3 Attestation encoding

## 3.1 ISO/IEC 18013-5-compliant encoding

Version 0.1 does not define mdoc as the primary format.

A future profile MAY define mdoc where loyalty presentation at a physical port or ferry
facility requires proximity and offline capability.

## 3.2 SD-JWT VC-based encoding

### 3.2.1 Verifiable Credential Type

The proposed Verifiable Credential Type is:

```text
urn:aptitude.eu:seditx:ferry-loyalty-credential:1
```

### 3.2.2 Registered JWT claims

| **Data Identifier** | **Claim** | **Format** | **Disclosable** |
|---------------------|-----------|------------|-----------------|
| `issuer` | `iss` | string | MUST NOT |
| `issued_at` | `iat` | integer | MUST NOT |
| `valid_from` | `nbf` | integer | MUST NOT |
| `valid_until` | `exp` | integer | MUST NOT |
| `credential_type` | `vct` | string | MUST NOT |
| `holder_binding` | `cnf` | object | MUST NOT |
| `status_reference` | `status` | object | MUST NOT |

### 3.2.3 Private claims

| **Data Identifier** | **Claim** | **Format** | **Disclosable** |
|---------------------|-----------|------------|-----------------|
| `category` | `category` | string | MUST NOT |
| `credential_id` | `credential_id` | string | MUST NOT |
| `member_reference` | `member_reference` | string | MUST |
| `programme_id` | `programme_id` | string | MUST |
| `programme_name` | `programme_name` | string | MUST |
| `membership_status` | `membership_status` | string | MUST |
| `tier` | `tier` | string | MUST |
| `tier_valid_from` | `tier_valid_from` | string | MUST |
| `tier_valid_until` | `tier_valid_until` | string | MUST |
| `benefit_entitlements` | `benefit_entitlements` | array | MUST |
| `discount_percentage` | `discount_percentage` | integer | MUST |
| `points_multiplier` | `points_multiplier` | number | MUST |
| `priority_boarding` | `priority_boarding` | boolean | MUST |
| `priority_support` | `priority_support` | boolean | MUST |
| `lounge_access` | `lounge_access` | boolean | MUST |
| `free_change_entitlement` | `free_change_entitlement` | boolean | MUST |
| `free_baggage_entitlement` | `free_baggage_entitlement` | boolean | MUST |
| `partner_benefits` | `partner_benefits` | array | MUST |
| `issuing_operator_id` | `issuing_operator_id` | string | MUST |
| `issuing_operator_name` | `issuing_operator_name` | string | MUST |
| `account_created_at` | `account_created_at` | string | MUST |
| `display_member_number` | `display_member_number` | string | MUST |
| `points_balance` | `points_balance` | integer | MUST |
| `points_balance_as_of` | `points_balance_as_of` | string | MUST |
| `redeemable_points` | `redeemable_points` | integer | MUST |
| `benefit_scope` | `benefit_scope` | array | MUST |
| `subject_binding_reference` | `subject_binding_reference` | string | MUST |
| `cryptographically_bound_to` | `cryptographically_bound_to` | string | MUST NOT |
| `schema_version` | `schema_version` | string | MUST NOT |
| `trust_anchor_reference` | `trust_anchor_reference` | string | MUST NOT |

Each benefit SHOULD be independently disclosable where technically possible.

### 3.2.4 Illustrative claim set

```json
{
  "iss": "https://loyalty.fastferries.example",
  "iat": 1784796300,
  "nbf": 1767225600,
  "exp": 1830211199,
  "vct": "urn:aptitude.eu:seditx:ferry-loyalty-credential:1",
  "cnf": {
    "jkt": "wallet-key-thumbprint"
  },
  "status": {
    "status_list": {
      "idx": 812,
      "uri": "https://status.fastferries.example/loyalty/atl/42"
    }
  },
  "category": "eaa:eu:non-qualified",
  "credential_id": "flc_01JZ5L8M2A7P9Q4R6T3V",
  "member_reference": "member_f8a72c91",
  "programme_id": "fast_ferries_rewards",
  "programme_name": "Fast Ferries Rewards",
  "membership_status": "active",
  "tier": "gold",
  "benefit_entitlements": [
    "fare_discount",
    "priority_boarding",
    "priority_support"
  ],
  "discount_percentage": 10,
  "priority_boarding": true,
  "priority_support": true,
  "issuing_operator_id": "fast-ferries-gr",
  "issuing_operator_name": "Fast Ferries",
  "valid_from": "2026-01-01",
  "valid_until": "2027-12-31",
  "schema_version": "0.1",
  "trust_anchor_reference": "https://trust.aptitude.example/ferry-loyalty-issuers"
}
```

## 3.3 W3C Verifiable Credentials Data Model-based encoding

Version 0.1 does not define a W3C VCDM representation.

## 4 Attestation usage

### 4.1 Issuance prerequisites

The issuer SHALL issue the credential only after:

1. the loyalty account exists;
2. the User has authenticated to the loyalty programme;
3. the member reference has been established;
4. the current membership status has been checked;
5. any tier or benefit claims have been calculated;
6. the validity period has been determined; and
7. the User has consented to receive the credential.

The credential SHALL be issued through OpenID4VCI or another APTITUDE-approved
issuance flow.

### 4.2 Device and holder binding

The credential **SHOULD be device-bound**.

Strong PID binding is not mandatory for every loyalty use case. It MAY be required where:

* the account is strictly personal;
* high-value benefits are involved;
* account transfer or fraud risk is significant; or
* the fare policy requires identity matching.

### 4.3 Presentation during booking

A normal ferry booking flow SHOULD request only the subset needed for the selected
benefit.

Examples:

#### Membership recognition

```text
member_reference
programme_id
membership_status
valid_until
```

#### Tier-based discount

```text
programme_id
membership_status
tier
discount_percentage
valid_until
```

#### Priority boarding

```text
programme_id
membership_status
priority_boarding
valid_until
```

The booking portal SHALL NOT request points balance, account-creation date or unrelated
benefits when they are not required.

### 4.4 Relying Party obligations

The ferry portal or Intermediary Service SHALL:

1. verify signature and integrity;
2. verify issuer trust and programme authority;
3. verify validity and status;
4. verify membership status;
5. confirm that the disclosed benefit applies to the selected operator, route, fare or date;
6. check freshness where mutable claims are used;
7. apply the benefit according to current tariff rules;
8. return a structured verification result;
9. avoid retaining the full credential; and
10. prevent duplicate or unauthorised redemption where relevant.

A typical result SHOULD be:

```json
{
  "credential_valid": true,
  "programme_id": "fast_ferries_rewards",
  "membership_valid": true,
  "tier": "gold",
  "benefit": "fare_discount",
  "discount_percentage": 10,
  "decision": "eligible",
  "correlation_id": "loy_01JZ..."
}
```

### 4.5 Points accrual and redemption

Points accrual and redemption are not automatically implemented by credential
presentation.

The loyalty back end remains authoritative.

Where a presentation triggers accrual or redemption:

* the verifier SHALL authenticate to the loyalty system;
* a transaction-specific reference SHALL be used;
* replay and duplicate redemption SHALL be prevented;
* the User SHALL be shown the effect of the transaction;
* points changes SHALL be recorded in the loyalty ledger; and
* the credential SHOULD be refreshed or reissued where it carries mutable balance data.

### 4.6 Data minimisation and privacy

The verifier SHOULD retain only:

* programme identifier;
* benefit applied;
* tariff basis;
* transaction reference;
* timestamp; and
* verification outcome.

It SHOULD NOT retain:

* the complete credential;
* unrelated benefits;
* full loyalty history;
* unnecessary member identifiers;
* points balance where not needed; or
* PID attributes unless required.

### 4.7 Failure and fallback

The verifier SHALL return `not_eligible` or `manual_review` when:

* signature, trust, validity or status verification fails;
* membership is inactive;
* the benefit does not apply;
* a mutable claim is stale;
* the account has been suspended;
* a redemption is duplicated; or
* the loyalty service is unavailable.

Failure of wallet verification SHALL NOT affect the User's underlying right to purchase
a standard fare without loyalty benefits.

## 5 Trust anchors

The Ferry Loyalty Credential may be issued by:

* a ferry operator;
* a ferry loyalty programme operator;
* a consortium of ferry operators;
* an authorised travel programme administrator; or
* an Attestation Provider acting for one of these entities.

The trust framework SHALL allow the verifier to determine:

1. the issuer's legal or contractual authority;
2. the loyalty programme operated by the issuer;
3. the ferry operators that recognise the credential;
4. the benefits the issuer may attest;
5. the issuer's signing certificates or trust anchors; and
6. whether the issuer remains authorised.

For the APTITUDE pilot, trust SHOULD be obtained through the applicable WP2 trusted
issuer framework.

## 6 Revocation

### 6.1 Validity model

The credential MAY be medium-lived.

Tier and benefit validity MAY be shorter than membership validity.

The issuer SHOULD avoid embedding mutable values for longer than their reliable
freshness period.

### 6.2 Revocation and suspension

The credential SHALL be revocable or suspendable when:

* the account is closed;
* membership is suspended;
* fraud or account takeover is detected;
* the credential is reported compromised;
* a replacement credential is issued;
* the issuer is no longer authorised;
* the programme ends; or
* the credential was issued in error.

### 6.3 Status-list mechanism

The final APTITUDE status-list mechanism and endpoint remain to be defined.

Illustrative value:

```text
https://status.fastferries.example/loyalty/
```

This is not an operational endpoint.

## 7 Compliance

This Rulebook is designed to align with:

* Regulation (EU) 2024/1183;
* the EUDI Wallet Architecture and Reference Framework;
* ARF Annex 2 Topic 12;
* OpenID4VCI;
* OpenID4VP;
* SD-JWT VC and HAIP;
* GDPR principles of purpose limitation, data minimisation and storage limitation; and
* the SEDIT-X Ferry Transport working paper.

The Rulebook enforces:

1. optional, context-based presentation;
2. pseudonymous member references;
3. selective disclosure of tier and benefits;
4. separation from PID, payment and boarding credentials;
5. back-end authority for mutable loyalty state;
6. status and revocation;
7. minimal verifier retention; and
8. fallback to normal fare purchase.

Open matters include:

* final credential type identifier;
* final loyalty benefit vocabulary;
* operator and programme identifiers;
* support for multi-operator programmes;
* points-balance freshness;
* redemption transaction binding;
* whether mdoc is required;
* final trust-list endpoint;
* final status-list endpoint; and
* cross-programme interoperability.

## 8 References

| **Item Reference** | **Standard name/details** |
|--------------------|---------------------------|
| [European Digital Identity Regulation] | Regulation (EU) 2024/1183 |
| [SEDIT-X Ferry Working Paper] | APTITUDE WP4, SEDIT-X Ferry Transport, Version 0.1, May 2026 |
| [APTITUDE D4.1] | APTITUDE D4.1: UC Specifications and Scenarios, final version, 29 May 2026 |
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
