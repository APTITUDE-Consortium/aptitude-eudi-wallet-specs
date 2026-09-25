Author(s):

- 

# Attestation Rulebook for attestations of type *Digital Travel Authorizations (DTA)*

| Version | Date       | Description                                                                 |
| ------- | ---------- | ---------------------------------------------------------------------------- |
| 0.1     | 2026-09-15 | First draft of APTITUDE DTA to be managed inside EUDI wallet in accordance with [ICAO DTA TR] version 2.15 published on 2021. |

Feedback:

* <jhan@iata.org>

## 1 Introduction

### 1.1 Document scope and purpose

Within the European context and in accordance with the EUDI Wallet Architecture and Reference Framework, the Digital Travel Authorization (DTA) can be managed by an EUDI Wallet following the format of an electronic attestation of attributes. The DTA enables travelers to hold a digitally issued and verifiable travel authorization in their Wallet Unit for pre-travel admissibility's check and border-control use cases, in place of or alongside a printed or emailed authorization.
 
The primary objective of the DTA is to support pre-travel authorization checks and border verification, pre-clearance and the port of entry. The DTA complements the authorization record held by the issuing State and uses EUDI Wallet presentation mechanisms to support remote and proximity presentation and, where permitted by the credential format and protocol, selective disclosure and strong cryptographic verification.
 
Within this context, the target model builds on the ICAO DTA as defined in [ICAO-DTA-TR] and linked to the holder's passport. This rulebook therefore draws on the ICAO DTA data model as its baseline while adapting the encoding and presentation layer to EUDI Wallet mechanisms. Divergence from the strict ICAO specification is expected in data content (EUDI Wallet-specific extensions) and presentation protocols (EUDI Wallet remote/proximity presentation). For details see §7.
 
The present rulebook specifies the following listed items for APTITUDE DTA: 
- The attributes and metadata 
- Encoding and its mapping to the data elements. 
- The issuance, presentation and verification requirements. 
- The trust anchor, revocation and compliance requirements that apply to the attestation.

### 1.2 Document structure

- Chapter 2 — Requirements on the APTITUDE DTA and its attributes/metadata
- Chapter 3 — Encoding and its associated attributes
- Chapter 4 — Attestation usage
- Chapter 5 — Trust anchors
- Chapter 6 — Revocation
- Chapter 7 — Compliance with the ICAO DTA specification
- Chapter 8 — Issuance considerations
- Chapter 9 — References

### 1.3 Key words

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

### 1.4 Terminology

- **DTA**: Digital Travel Authorization, as defined in [ICAO-DTA-TR] §2.2: "an electronically enabled travel authorization".
- **VDS-NC**: Visible Digital Seal for Non-Constrained Environments, the mandatory barcode verification feature of a DTA per [ICAO-DTA-TR] §2.5.4 and §3.
- **Notification**: the DTA Notification of Result issued to the applicant, per [ICAO-DTA-TR] §2.5.4 and Appendix B.

## 2 Attestation attributes and metadata

### 2.1 Introduction

The ICAO DTA data model is specified under [ICAO-DTA-TR]: the mandatory content of a DTA Notification (§2.5.4) and the mandatory VDS-NC schema (§3.3) together define the full set of data elements. The objective of this section is to:

- Reference every data element mandated by the [ICAO-DTA-TR] Notification table and VDS-NC schema in the APTITUDE DTA mdoc.
- Specify field-length and format constraints given in [ICAO-DTA-TR] §3.3 (e.g. `dtan` ≤ 13 chars, ISO 8601 dates).
- Carry the mandatory VDS-NC verification feature ([ICAO-DTA-TR] §2.5.3, §2.5.4) as an embedded data element rather than requiring a separate physical/printed artefact.

#### Table 1 — Requirements on data model

| Index      | Requirement specification                                                                                                                                                                        |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DTA\_AE\_01 | The APTITUDE DTA SHALL use ISO/IEC 18013-5 mdoc-cbor encoding. [Ref: this rulebook §3]                                                                                                                |
| DTA\_AE\_02 | The APTITUDE DTA SHALL carry all data elements mandated for the DTA Notification of Result in [ICAO-DTA-TR] §2.5.4.4.                                                                                  |
| DTA\_AE\_03 | The APTITUDE DTA SHALL carry all data elements marked `required` in the [ICAO-DTA-TR] §3.3 VDS-NC message schema.       |
| DTA\_AE\_04 | The APTITUDE DTA SHALL embed a valid VDS-NC (or VDS) object as defined in [ICAO-DTA-TR] §3, in accordance with §2.5.4 which mandates a digitally signed barcode as the verification feature.          |
| DTA\_AE\_05 | The APTITUDE DTA SHALL support a trust architecture enabling verification via the same CSCA/DS PKI used for eMRTDs, per [ICAO-DTA-TR] §3.1–3.2.                                                       |
| DTA\_AE\_06 | The APTITUDE DTA SHALL support Selective Disclosure allowing a Relying Party (e.g. an airline at check-in) to request only the subset of elements it needs.                       |
| DTA\_AE\_07 | The APTITUDE DTA mdoc SHALL include a portrait data element where the issuing State chooses to use a photo per [ICAO-DTA-TR] §2.5.3.                       |

#### Table 2 — Requirements on issuing

| Index      | Requirement specification                                                                                                                                                                        |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DTA\_IS\_01 | The APTITUDE DTA SHALL be issued exclusively by the DTA Issuing Authority of the State that grants the travel authorization, per [ICAO-DTA-TR] §2.9. |
| DTA\_IS\_02 | The APTITUDE DTA in mdoc format SHALL be issued only after a successful application steps per [ICAO-DTA-TR] §2.5.1–2.5.3. This rulebook governs only the resulting Notification artefact. |
| DTA\_IS\_03 | The APTITUDE DTA SHALL be linked to exactly one official travel document (passport) identified by `travel_doc_number` and `travel_doc_issuer`, per [ICAO-DTA-TR] §2.5.4. |
| DTA\_IS\_04 | The issuing system SHALL support revocation/invalidation of an issued APTITUDE DTA. |
| DTA\_IS\_05 | The issuing system SHALL notify of unsuccessful APTITUDE DTA issuance through the issuing authority's existing Notification of Result process per [ICAO-DTA-TR] §2.5.4. It is outside the scope of this rulebook to define the process for same. |
| DTA\_IS\_06 | The issuing system SHALL put length constraints of issued data elements in accordance to [ICAO-DTA-TR] §3.3. |

#### Table 3 — Requirements on data elements

| Index      | Requirement specification                                                                                                                                                                        |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DTA\_DM\_01 | The APTITUDE DTA SHALL contain the mandatory data elements listed in Table 4 (§2.2), whose content SHALL be consistent with the corresponding VDS-NC `msg` object embedded per DTA\_AE\_04. |
| DTA\_DM\_02 | The APTITUDE DTA MAY contain the optional data elements listed in Table 5 (§2.3), where used by the issuing State (ex. `duration_of_stay`, `additional_information`). |
| DTA\_DM\_03 | Where a data element is present both as a discrete element and inside the embedded VDS-NC object, the two values SHALL be identical. The discrete element exists for selective disclosure and structured querying, the VDS-NC object exists for additional verification outside of proximity and remote online verification flow. |

### 2.2 Mandatory attributes

Table 4

| Identifier                     | Description                                                                                                   | Example                     |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `dta_number`                    | Identifying number of APTITUDE DTA instance. [ICAO-DTA-TR] §2.5.4 "DTA Number", VDS-NC `dtan`. SHALL be ≤13 characters     | `123889546`                   |
| `authority_doc_name`             | Word(s), in the language of the issuing State, naming the APTITUDE DTA document. [ICAO-DTA-TR] §2.5.4 "Document".         | `Digital Travel Authorization` |
| `travel_doc_holder_name`                    | Family name and given name(s) of the holder as on the official travel document or passport. [ICAO-DTA-TR] §2.5.4 "Name", VDS-NC `pi.n`. SHALL be ≤39 characters | `Anna Maria Eriksson`   |
| `birth_date`                     | Date of birth of the holder. [ICAO-DTA-TR] §2.7.1, VDS-NC `pi.dob`.                                                | `1952-03-11`                 |
| `sex`                            | Sex of the holder. [ICAO-DTA-TR] §2.7.1, VDS-NC `pi.sex`. SHALL be enum F/M/<                                      | `F`                           |
| `nationality`                    | Nationality of the holder, ISO 3166-1 alpha-3. [ICAO-DTA-TR] §2.7.1, VDS-NC `pi.nl`.                               | `USA`                         |
| `travel_doc_number`              | Number of the passport or travel document to which the  APTITUDE DTA is linked. [ICAO-DTA-TR] §2.5.4 "Passport Number", VDS-NC `pi.pn`.       | `L8988901C`                  |
| `place_of_issue`                 | Post/location where the APTITUDE DTA is issued. [ICAO-DTA-TR] §2.5.4 "Place of issue", VDS-NC `dta.poi`. SHALL be ≤15 characters              | `Peacetown`                   |
| `valid_from_date`                | First date from which the APTITUDE DTA can be used to seek entry. [ICAO-DTA-TR] §2.5.4 "Valid from (date)", VDS-NC `dta.vf`. | `2026-06-06`               |
| `valid_until_date`               | Last date on which the APTITUDE DTA can be used to seek entry. [ICAO-DTA-TR] §2.5.4 "Valid until (date)", VDS-NC `dta.vu`.  | `2030-06-06`                 |
| `number_of_entries`              | Number of entries for which the APTITUDE DTA is valid; `M` = multiple, `1` = Single entry, `2` = 2 entries etc. [ICAO-DTA-TR] §2.5.4 "Number of entries", VDS-NC `dta.noe`. | `M`                    |
| `type_class_category`            | Type-classpcategory of APTITUDE DTA granted (e.g. visitor, resident, diplmat) and any territorial limitation. [ICAO-DTA-TR] §2.5.4 "Type/class/category", VDS-NC `dta.tcc`. SHALL be ≤46 character | `Tourist`    |
| `visible_digital_seal`           | The embedded, digitally signed VDS or VDS-NC object constituting the mandatory verification feature. [ICAO-DTA-TR] §2.5.4 "Verification feature", §3. | `(binary VDS-NC object)` |

### 2.3 Optional and conditional attributes

Table 5

| Identifier               | Description                                                                                                              | Example              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `duration_of_stay`         | Number of days/months/years the holder may stay. [ICAO-DTA-TR] §2.5.4 "Duration of Stay", VDS-NC `dta.dos` (optional in VDS-NC schema). SHALL be 6 character following YYMMDD) | `050000` (YYMMDD)      |
| `portrait`              | Photo of the holder per issuing-State discretion. [ICAO-DTA-TR] §2.5.3                                          | JPEG or JPEG2000 encoded data                         |
| `travel_doc_issuer`              | State/Organization that issued the linked passport. [ICAO-DTA-TR] §2.7.1.                                          | `USA`                         |
| `travel_doc_expiry_date`         | Expiry date of the linked passport. [ICAO-DTA-TR] §2.5.4 "Passport Date of Expiry".                                | `2030-01-01`                 |
| `additional_information`   | Necessary endorsements/entitlements (ex. max stay, conditions, fee record). [ICAO-DTA-TR] §2.5.4 "Additional information", VDS-NC `dta.ai` (optional). SHALL be ≤100 characters. | `Employment Prohibited` |

### 2.4 Mandatory metadata

Table 6

| Identifier          | Description                                                                                   | Example         |
| -------------------- | ------------------------------------------------------------------------------------------------- | ------------------ |
| `issuing_country`    | ISO 3166-1 alpha-3 code of the issuing State. [ICAO-DTA-TR] §3.1 header `is`.  Country code as alpha 2 and alpha 3 code, defined in ISO 3166-1                    | `UTO`             |
| `version`             | Profile version which mirrors VDS-NC version number. [ICAO-DTA-TR] §3. SHALL be set to 1.              | `1`               |

### 2.5 Optional metadata

Table 7

| Identifier       | Description                                                                                     | Example      |
| ------------------ | ----------------------------------------------------------------------------------------------- | -------------- |
| `issuing_authority`  | Authority issuing the APTITUDE DTA. [ICAO-DTA-TR] §2.5.4.    | `Demo DTA Authority` |
| `issue_date`        | Date the DTA record was created, where the issuing State distinguishes it from `valid_from_date` per [ICAO-DTA-TR] §2.5.4 note. | `2021-06-01` |

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5 compliant encoding

This Rulebook defines an ISO/IEC 18013-5:2021-compliant mdoc encoding for the **APTITUDE DTA**.

The attestation is intended to be proximity-presentable and internet-presentable within the EUDI Wallet ecosystem and therefore SHALL support an mdoc representation.

#### 3.1.1 DTA mdoc document type and namespace

The `docType` and `namespace` for the **APTITUDE DTA mdoc** SHALL be `eu.europa.ec.eudiw.dta.1`.

#### 3.1.2 DTA data elements matching table
The following general encoding rules apply:

* `tstr`, `uint`, `bstr`, and `bool` follow the CDDL representation conventions.
* All string values SHALL be UTF-8 encoded.
* Dates expressed as textual values SHOULD follow RFC 3339-compatible syntax where applicable.
* Canonical CBOR encoding SHOULD be used for mdoc payloads.

The table below . "Presence" indicates whether the element is mandatory (M), optional (O) or conditional (C) in this mdoc profile.

| identifier                   | CBOR type          | Presence | [ICAO-DTA-TR] source or description               | VDS-NC field (§3.3) | 
| ---------------------------- | ----------------- | ---------- | ------------------------------------------------ | ---------------------- | 
| `dta_number`                  | tstr               | M        | §2.5.4 "DTA Number"                               | `dtan`                  |
| `authority_doc_name`          | tstr               | M        | §2.5.4 "Document"                                 | N.A  |
| `travel_doc_holder_name`      | tstr               | M        | §2.5.4 "Name"; §2.7.1                             | `pi.n`                  |
| `birth_date`                  | full-date          | M        | §2.7.1 "Date of Birth"                            | `pi.dob`                |
| `sex`                         | tstr               | M        | §2.7.1 "Sex"                                      | `pi.sex`                |
| `nationality`                 | tstr               | M        | §2.7.1 "Nationality" (ISO 3166-1 alpha-3)         | `pi.nl`                 |
| `travel_doc_number`           | tstr               | M        | §2.5.4 "Passport Number"; §2.7.1                  | `pi.pn`                 |
| `travel_doc_issuer`           | tstr               | O        | §2.7.1 "Issuing State or Organization"            | N.A                     |
| `travel_doc_expiry_date`      | full-date          | O        | §2.5.4 "Passport Date of Expiry"                  | N.A                     |
| `place_of_issue`              | tstr               | M        | §2.5.4 "Place of issue"                           | `dta.poi`               |
| `valid_from_date`             | full-date          | M        | §2.5.4 "Valid from (date)"                        | `dta.vf`                |
| `valid_until_date`            | full-date          | M        | §2.5.4 "Valid until (date)"                       | `dta.vu`                |
| `duration_of_stay`            | tstr               | O        | §2.5.4 "Duration of Stay"                         | `dta.dos`               |
| `number_of_entries`           | tstr               | M        | §2.5.4 "Number of entries"                        | `dta.noe`               |
| `type_class_category`         | tstr               | M        | §2.5.4 "Type/class/category"                      | `dta.tcc`               |
| `additional_information`      | tstr               | O        | §2.5.4 "Additional information"                   | `dta.ai`                |
| `visible_digital_seal`        | bstr               | M        | §2.5.4 "Verification feature"; §3 (whole VDS-NC)  | *(entire object)*       |
| `issuing_authority`           | tstr               | O        | §2.5.4 (issuer context)                           | N.A                     |
| `issuing_country`             | tstr               | M        | §3 header `is`                                    | `hdr.is`                |
| `version`                     | uint               | M        | §3 header `v`                                     | `hdr.v`                 |
| `portrait`                    | bstr               | C        | Portrait data encoded as JPEG or JPEG2000         | N.A                     |

#### 3.1.3 Additional document encryption

If a Relying Party requires document response encryption in addition to the session encryption layer, it SHALL use the mechanism defined in [ISO/IEC 18013-5.2]. The EUDI Wallet SHALL encrypt the requested data elements according to [ISO/IEC 18013-5.2].

## 4 Attestation Usage
This section briefly describes example use cases for **APTITUDE DTA**. All requested attributes are examples and the request may include other data elements as given in the use cases.

### 4.1 Remote Online readiness to travel verification

**Context:** An airline or travel agent verifies ahead of departure that the passenger holds a valid **APTITUDE DTA** for the destination State, per [ICAO-DTA-TR] §2.4 (aircraft-operator benefits). This can also be requested during airline checkin process.

**Requested attributes:** `dta_number`, `travel_doc_holder_name`, `travel_doc_number`, `valid_from_date`, `valid_until_date`, `number_of_entries`, `type_class_category`, `visible_digital_seal`.

**Post-processing:** the verifier SHALL validate the mdoc issuer signature and optionally VDS-NC signature against the DTA signer certificate chain rooted at the applicable CSCA (§5). It MAY check revocation/status using the applicable trust anchors. Verification outcome drives pre-assessment workflows. If selective disclosure was used, the backend SHALL verify the integrity and authenticity of the disclosed data elements using the cryptographic mechanism of the selected data format.

### 4.2 Remote Online Border inspection verification

**Context:** Traveler is able to present online its APTITUDE DTA from EUDI wallet to the border control verifier. Border officials verify a DTA. 

**Requested attributes:** all mandatory elements of §2.2, plus `duration_of_stay` and `additional_information` where present and applicable.

**Post-processing:** Same as defined in §4.1.

## 5 Trust Anchors

According to [ICAO-DTA-TR] §3.1, the CSCA used to sign the DTA barcode signer **SHALL be the same CSCA used to issue eMRTDs** of the issuing State.

The mdoc issuer-signed structure (MSO) SHALL be signed by a APTITUDE DTA-issuer key certified under the same CSCA hierarchy, so a single trust chain verifies both the embedded VDS-NC and the mdoc MSO. CSCA root certificates MAY be obtained from the ICAO PKD by any Relying Party, consistent with [ICAO-DTA-TR] §3.1.

For interoperability testing, issuing authorities SHOULD provide a test CSCA distinguishable from production trust anchors.

## 6 Revocation

[ICAO-DTA-TR] does not itself define a revocation mechanism for a DTA (the Notification is a static, signed artefact). 

For the APTITUDE DTA mdoc:
- Revocation SHALL be implemented according to [ISO/IEC 18013-5.2] MSO revocation mechanisms. The issuing authority SHALL provide the corresponding status list.
- If it is marked revoked, a Relying Party SHALL reject it and all disclosed data elements, and SHALL NOT rely on the embedded VDS-NC alone to establish current validity.
- Reasons for revocation include but not limited to: refusal reversal after issuance, fraud or data-error findings, replacement of the linked passport (which changes `travel_doc_number`), or loss/compromise of the Wallet Unit.

## 7 Compliance

### 7.1 Compliance with ICAO DTA specification

1. The APTITUDE DTA mdoc is compliant with [ICAO-DTA-TR] §2.5.4 in that it carries every mandatory Notification field listed there.
2. The APTITUDE DTA mdoc embeds a VDS-NC object compliant with [ICAO-DTA-TR] §3, satisfying the mandatory "Verification feature" requirement without requiring a separate printed barcode.
3. Where a Relying Party's reader supports only VDS-NC/VDS barcode scanning (not mdoc), the wallet SHOULD be able to render the VDS barcode since [ICAO-DTA-TR] does not mandate mdoc support by all readers.
4. The choice between VDS and VDS-NC as the embedded barcode format is left to the issuing State per [ICAO-DTA-TR] §3.4, this rulebook assumes VDS-NC, as it "includes the barcode signer and does not require a separate distribution mechanism."
5. APTITUDE DTA can be verified by any reader, i.e. Relying Party, within EUDI-Wallet ecosystem.
6. APTITUDE DTA can be verified internationally by any reader compliant to [ISO/IEC 18013-5] and [ISO/IEC 18013-7.2], e.g. supporting OpenID4VP.

### 7.2 ICAO VDS-NC reconstruction

A reader that only understands the flat ICAO VDS-NC `hdr`/`msg` structure (§3.3) MAY reconstruct it from the mdoc `visible_digital_seal` element directly, since that element SHALL contain the complete, unmodified VDS-NC object as issued.

## 8 Considerations for issuance of APTITUDE DTA mdoc credentials

The table below indicates, for each attribute, whether its value originates from the applicant's Application submission ([ICAO-DTA-TR] §2.5.1), the linked passport's MRZ ([ICAO-DTA-TR] §2.7.1), or is assigned by the issuing authority during adjudication ([ICAO-DTA-TR] §2.5.4).

| Data field                  | From applicant Application | From passport MRZ | Assigned by issuing authority |
| ------------------------------ | -------------------------------------- | ----------------------------- | ----------------------------------------- |
| `dta_number`                    |                                         |                                | X                                         |
| `authority_doc_name`             |                                         |                                | X                                         |
| `travel_doc_holder_name`                    | X (as entered, cross-checked vs MRZ)   | X                              |                                           |
| `birth_date`                     | X                                      | X                              |                                           |
| `sex`                             | X                                      | X                              |                                           |
| `nationality`                     | X                                      | X                              |                                           |
| `travel_doc_number`               | X                                      | X                              |                                           |
| `travel_doc_issuer`               | X                                      | X                              |                                           |
| `travel_doc_expiry_date`          | X                                      | X                              |                                           |
| `place_of_issue`                  |                                         |                                | X                                         |
| `valid_from_date`                 |                                         |                                | X                                         |
| `valid_until_date`                |                                         |                                | X                                         |
| `duration_of_stay`                |                                         |                                | X                                         |
| `number_of_entries`               |                                         |                                | X                                         |
| `type_class_category`             | X (as requested)                       |                                | X (as granted)                            |
| `additional_information`          |                                         |                                | X                                         |
| `visible_digital_seal`            |                                         |                                | X                                         |
| `issuing_authority`               |                                         |                                | X                                         |
| `issuing_country`                 |                                         |                                | X                                         |
| `portrait`                        | X                                       |                                | X                                         |

*Note:* Per [ICAO-DTA-TR] §2.5.2, the application interface "should enable the electronic capture of the passport data page for automatically populating the fields in the application," and for ePassports, chip data should be used i.e. `travel_doc_holder_name`, `birth_date`, `sex`, `nationality`, `travel_doc_number`, `travel_doc_issuer` and `travel_doc_expiry_date` SHOULD be captured from the passport rather than free-typed, to ensure the mdoc content is consistent with the MRZ the border authority will independently read.

## 9 References

| Item Reference     | Standard name/details                                                                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ICAO-DTA-TR]        | ICAO Machine Readable Travel Documents Technical Report, *Digital Travel Authorizations*, Version 2.15, June 2021, ISO/IEC JTC1 SC17 WG3/TF1. [PDF](https://www.icao.int/sites/default/files/TRIP/Publications/Digital-Travel-Authorizations-New.pdf) |
| [VDS-NC]             | Visible Digital Seal for Non-Constrained Environments V1.1, as referenced in [ICAO-DTA-TR] §4.                                                                          |
| [ISO/IEC 18013-5]    | ISO/IEC 18013-5:2021, Personal identification: ISO-compliant driving licence Part 5: Mobile driving licence (mDL) application.                                        |
| [ISO/IEC 18013-5.2]  | ISO/IEC 18013-5, second edition (in development), including MSO status-list revocation and document response encryption mechanisms.                                     |
| [RFC 2119]           | RFC 2119 Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997.                                                                              |
