# Attestation Rulebook for attestations of type  *APTITUDE DTC*

Author(s):

* Matthias Schwan, bdr, Germany
* ... , IPZS, Italy
* ... , ANTS, France
* ... , INCM, Portugal
  
| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |
| 0.2 | 27-05-2026 | Updated based on design assumptions from D3.1  |
| 0.3 | 29-05-2026 | addition of schema and mapping |
| 0.4 | 12-06-2026 | synchronization with PhotoID specification in [ISO/IEC 23220-4] |
| 0.5 | 31-06-2026 | align clause 2 and 3 with rulebook template, biblopgraphy added, trust model and revocation added |

Feedback:

* <matthias.schwan@bdr.de>
* ...
* ...
* ...

## 1 Introduction

### 1.1 Document scope and purpose

This Attestation Rulebook defines the Digital Travel Credential (DTC) as an electronic attestation of attributes for the EUDI Wallet ecosystem. The DTC enables travellers to store and present identity and travel authorization data in their Wallet Unit for border control and travel-related use cases.

The primary objective of the DTC is to facilitate secure and privacy-preserving identity verification and travel document validation at border crossing points and during travel. The DTC is designed to complement existing physical travel documents (e.g. passports, visas) by providing a digital equivalent that supports selective disclosure, offline presentation and strong cryptographic verification.

Within the Aptitude context, the target model is the ICAO DTC Type 2, bound to a physical eMRTD and derived using mechanisms aligned with European regulations and ICAO guidelines. Type 2 is therefore considered the primary and preferred implementation model. However, the framework may also support ICAO DTC Type 1 where it is based on an LDS (Logical Data Structure) signed by the official passport authority. In such cases, the DTC is encapsulated within an attestation stored in the EUDI Wallet, ensuring that it remains cryptographically linked to a physical component and provides sufficient assurance for border control use cases.

This rulebook specifies:

* The attributes and metadata that comprise a DTC attestation
* The encoding formats that SHALL be supported for DTC attestations.
* The issuance, presentation and verification requirements for DTC attestations within the EUDI Wallet framework.
* The trust anchor mechanisms, revocation procedures and compliance requirements that apply to DTC attestations.

### 1.2 Document structure

* Chapter 2, which describes the requirements on the APTITUDE DTC.
* Chapter 3, which specifies how the attestation attributes and metadata are encoded in case the attestation complies with ISO/IEC 18013-5. Each encoding SHALL be specified in a separate section, or even in a separate chapter.
* Chapter 4, which specifies attestation usage.
* Chapter 5, which specifies trust anchors.
* Chapter 6, which specifies revocation.
* Chapter 7, which specificies compliance.

### 1.3 Key words

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

### 1.4 Terminology

Terminologies and definitions within Aptitude project are listed in [APTITUDE Glossary](../glossary.md)

## 2 Attestation attributes and metadata

### 2.1 Introduction

This section defines the functional and semantic scope of the data composing the APTITUDE Digital Travel Credential (DTC), based on the evidence collected during the stock‑taking phase.

The cross‑border value of a DTC critically depends on preserving full alignment with the ICAO data model while at the same time allowing extensions required for integration within the EUDI Wallet ecosystem and the eIDAS 2.0 framework.

International interoperability and backward compatibility with existing border‑control infrastructure remain core requirements for any realistic DTC deployment.
As a result, the ICAO LDS data model (DG1, DG2, DG14, DG15, SOD) constitutes the mandatory baseline.

The objective is to preserve a single interoperable DTC representation that is:

* aligned with ICAO DTC Type 2 and eMRTD LDS semantics,
* compatible with EUDI Wallet proximity presentation,
* suitable for both on-site border-control use cases and remote wallet-driven presentations,
* capable of preserving the cryptographic binding between the virtual credential and the Wallet Secure Component (WSCD).

#### Table 1 — General requirements

| Index | Requirement specification |
| --- | --- |
| DTC_GR_01 | According to ICAO’s DTC-VC data model, the APTITUDE DTC SHALL contain DG1, DG2, SOD as from the physical eMRTD passport.|
| DTC_GR_02 | According to ICAO's DTC-VC data model, the APTITUDE DTC MAY contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation in case of eMRTD-PC bound    |
| DTC_GR_03 | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (e.g., SD-JWT or mDoc acc. ISO 23220-4).  |
| DTC_GR_04 | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| DTC_GR_05 | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties.|

#### Table 2 — Requirements on data model

| Index | Requirement specification |
| --- | --- |
| DTC_AE_01 | APTITUDE DTC SHALL use ISO/IEC 23220-4 PhotoID as the sole credential format. |
| DTC_AE_02 | APTITUDE DTC SHALL use ISO/IEC 18013-5 mdoc-cbor encoding for the PhotoID credential. |
| DTC_AE_03 | APTITUDE DTC SHALL support NFC engagement for proximity presentation and BLE data retrieval for Android and iOS. |
| DTC_AE_04 | APTITUDE DTC SHALL preserve ICAO LDS semantics, including EF.DG1, EF.DG2, EF.SOD, and the PhotoID profile. |
| DTC_AE_05 | APTITUDE DTC SHALL adopt open, standard-based encoding to maximize interoperability and avoid vendor lock-in. |
| DTC_AE_06 | APTITUDE DTC SHALL support a trust architecture that enables verification via ICAO CSCA/DS and EUDI Wallet / eIDAS trust anchors. |
| DTC_AE_07 | APTITUDE DTC SHALL preserve the cryptographic binding between the virtual credential and the Wallet Secure Component across issuance, storage, presentation, and verification. |
| DTC_AE_08 | APTITUDE DTC SHALL support selective disclosure and minimisation as a layer on top of the single PhotoID credential format, not by introducing a second credential format. |

#### Table 3 — Requirements on issuing

| Index | Requirement specification |
| --- | --- |
| DTC_IS_01 | The APTITUDE DTC SHALL be issued exclusively by the National Passport Issuing Authority of the Member State that issued the physical eMRTD. |
| DTC_IS_02 | APTITUDE DTC SHALL be derived from eMRTD chip data (Logical Data Structure - LDS) ensuring a cryptographic link to the physical travel document. |
| DTC_IS_03 | APTITUDE DTC SHALL be derived both from newly issued and already issued eMRTDs, except where the national authentic sources require a restriction. |
| DTC_IS_04 | The issuance process SHALL result in an ICAO DTC Type 2 (eMRTD-PC bound), where the virtual component is cryptographically linked to a physical secure element within the EUDI Wallet. |
| DTC_IS_05 | APTITUDE DTC SHALL be digitally signed by the national issuing authority acting as a Trusted Attestation Provider within the eIDAS 2.0 framework. |
| DTC_IS_06 | The system SHALL support the complete lifecycle management of the DTC, including secure revocation and update mechanisms managed by the issuing authority. |

#### Table 4 — Requirements on data elements

| Index | Requirement specification |
| --- | --- |
| DTC_DM_01 | The APTITUDE DTC SHALL contain DG1, DG2, DG14, DG15, SOD as from the physical eMRTD passport |
| DTC_DM_02 | The APTITUDE DTC SHALL contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation |
| DTC_DM_03 | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (SD-JWT or MDOC-CBOR). |
| DTC_DM_04 | The APTITUDE DTC SHALL include a cryptographic binding between the Virtual Component (VC) and the Physical Component (PC) stored in the WSCD. |
| DTC_DM_05 | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| DTC_DM_06 | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |

### 2.2 Mandatory attributes

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``family_name`` | according to [ISO/IEC 23220-2.2] | Hardt |
| ``given_name`` | according to [ISO/IEC 23220-2.2] | Giovanni |
| ``birth_date`` | according to [ISO/IEC 23220-2.2] | 01-01-1980 |
| ``portrait`` | according to [ISO/IEC 23220-2.2] | ... |
| ``age_over_18`` | according to [ISO/IEC 23220-2.2] | T  |
| ``person_id`` | according to [ISO/IEC 23220-4] | 1234567890 |
| ``dg1`` | according to [ISO/IEC 23220-4] | P<ITA<<HARDT<<GIOVANNI<<<<<<<<<<<<<<<< |
| ``dg2`` | according to [ISO/IEC 23220-4] | ... |
| ``dg14`` | according to [ISO/IEC 23220-4] | ... |
| ``dg15`` | according to [ISO/IEC 23220-4] | ... |

### 2.3 Optional attributes

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``family_name_viz`` | according to [ISO/IEC 23220-4] | HARDT |
| ``given_name_viz`` | according to [ISO/IEC 23220-4] | GIOVANNI |
| ``enrolment_portrait_image`` | according to [ISO/IEC 23220-4] | ...  |
| ``age_in_years`` | according to [ISO/IEC 23220-4] | 28  |
| ``age_birth_year`` | according to [ISO/IEC 23220-4] | 1998  |
| ``portrait_capture_date`` | according to [ISO/IEC 23220-4] | 20-04-2023 |
| ``birthplace`` | according to [ISO/IEC 23220-4] | Italy, Trento |
| ``name_at_birth`` | according to [ISO/IEC 23220-4] | Nick |
| ``resident_address`` | according to [ISO/IEC 23220-4] | Sommarive, 18 |
| ``resident_city`` | according to [ISO/IEC 23220-4] | Trento |
| ``resident_postal_code`` | according to [ISO/IEC 23220-4] | 38122 |
| ``resident_country`` | according to [ISO/IEC 23220-4] | IT |
| ``resident_city_latin1`` | according to [ISO/IEC 23220-4] | ... |
| ``sex`` | according to [ISO/IEC 23220-4] | M |
| ``nationality`` | according to [ISO/IEC 23220-4] | IT  |
| ``family_name_latin1`` | according to [ISO/IEC 23220-4] | ...  |
| ``given_name_latin1`` | according to [ISO/IEC 23220-4] | ...  |
| ``birth_country`` |  according to [ISO/IEC 23220-4] | IT |
| ``birth_state`` |  according to [ISO/IEC 23220-4] | Trento |
| ``birth_city`` |  according to [ISO/IEC 23220-4] | Trento |
| ``resident_street`` | according to [ISO/IEC 23220-4] | Sommarive |
| ``resident_house_number`` | according to [ISO/IEC 23220-4] | 18 |
| ``resident_state`` | according to [ISO/IEC 23220-4] | IT |

### 2.4 Mandatory metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``issue_date`` | according to [ISO/IEC 23220-2.2] | 20-04-2023 |
| ``expiry_date`` | according to [ISO/IEC 23220-2.2] | 20-04-2033 |
| ``issuing_authority`` | according to [ISO/IEC 23220-2.2] | Ministero dell'Interno |
| ``version`` | according to [ISO/IEC 23220-4] | 1.0 |
| ``sod`` | Security object data of related eMRTD according to [ISO/IEC 23220-4] | ... |

### 2.4 Optional metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``document_number`` | according to [ISO/IEC 23220-2.2] | YA1234567 |
| ``issuing_subdivision`` | according to [ISO/IEC 23220-2.2] | TN  |
| ``administrative_number`` | according to [ISO/IEC 23220-2.2] | 9876543210 |
| ``travel_document_type`` | according to [ISO/IEC 23220-2.2] | Passport |
| ``travel_document_number`` | according to [ISO/IEC 23220-2.2] | I13235678 |
| ``travel_document_mrz`` | according to [ISO/IEC 23220-2.2] | P<ITA<<HARDT<<GIOVANNI<<<<<<<<<<<<<<<< |

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

#### 3.1.1 APTITUDE DTC document type and namespaces

The objects ``docType`` and ``namespace`` are used to encapsulate the document type and the space in which the data elements are defined.

The document type for the **APTITUDE DTC** SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4].

*Note:* The document type is ``org.iso.23220.photoid.1``.

The namespace of APTITUDE DTC for **general PhotoID data elements** defined in clause 3.1.2 SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4] and 6.3.1.1 of [ISO/IEC 23220-2.2].

*Note:* The namespace identifier is ``org.iso.23220.1``.

The namespace for **specific PhotoID data elements** defined in clause 3.1.3 SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4].

*Note:* The namespace identifier is ``org.iso.23220.photoid.1``.

The namespace for **ICAO PhotoID data elements** defined in clause 3.1.4 SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4].

*Note:* The namespace identifier is ``org.iso.23220.datagroups.1``.

Member States MAY add additional namespaces under their responsibility. The namespace for **Member State specific data elements** SHALL be as specified in clauses C.1.2 of [ISO/IEC 23220-4].

*Note:* The domestic namespace of the European Union is ``org.iso.23220.photoid.EU.1`` with number 1 indicating the version of this namespace and excluding the version number of photoid namespace.

The next section define general and specific data elements of the PhotoID.
These elements are given in tables of three columns:

* The "Identifier" column is the reference of the data element specified in clause 2.
* The “data element identifier according to [ISO/IEC 23220-4]” column gives the mapping of the data element to the data element identifier specified in [ISO/IEC 23220-4].
* The "Presence" column indicates whether the presence of the element on an APTITUDE DTC is mandatory (M), optional (O) or conditional (C). A mandatory data elemement SHALL be present in an APTITUTED DTC whereas an optional data element MAY be present. If a data element is conditional the respective condition is given in the specification. If the condition is met the data element SHALL be present.

#### 3.1.2 General PhotoID data elements

The general PhotoID data elements of APTITUDE DTC SHALL be as defined in Table 1 and belong to the namespace given in 3.1.1. The data element definitions given in clause C.2.1 and Table C.1 in [ISO/IEC 23220-4] apply if not stated otherwise.

##### Table 1 — general PhotoID data elements

| **Identifier** | **data element identifier**<br> **according to [ISO/IEC 23220-4]** | **Presence in**<br> **APTITUDE DTC** |
| --- | --- | --- |
| ``family_name`` | ``family_name`` | M |
| ``given_name`` | ``given_name`` | M  |
| ``family_name_viz`` | ``family_name_viz`` | O  |
| ``given_name_viz`` | ``given_name_viz`` | O  |
| ``birth_date`` | ``birth_date`` | M  |
| ``portrait`` | ``portrait`` | M  |
| ``enrolment_portrait_image`` | ``enrolment_portrait_image`` | O  |
| ``issue_date`` | ``issue_date`` | M  |
| ``expiry_date`` | ``expiry_date`` | M  |
| ``issuing_authority`` | ``issuing_authority`` | M  |
| ``age_over_18`` | ``age_over_18`` | M  |
| ``age_in_years`` | ``age_in_years`` | O  |
| ``age_birth_year`` | ``age_birth_year`` | O  |
| ``portrait_capture_date`` | ``portrait_capture_date`` | O  |
| ``birthplace`` | ``birthplace`` | O  |
| ``name_at_birth`` | ``name_at_birth`` | O  |
| ``resident_address`` | ``resident_address`` | O  |
| ``resident_city`` | ``resident_city`` | O  |
| ``resident_postal_code`` | ``resident_postal_code`` | O  |
| ``resident_country`` | ``resident_country`` | O  |
| ``resident_city_latin1`` | ``resident_city_latin1`` | O  |
| ``sex`` | ``sex`` | O  |
| ``nationality`` | ``nationality`` | O  |
| ``document_number`` | ``document_number`` | O  |
| ``issuing_subdivision`` | ``issuing_subdivision`` | O  |
| ``family_name_latin1`` | ``family_name_latin1`` | O  |
| ``given_name_latin1`` | ``given_name_latin1`` | O  |

#### 3.1.3 Specific PhotoID data elements

The specific PhotoID data elements of APTITUDE DTC SHALL be as defined in Table 2 and belong to the namespace given in 3.1.1. The data element definitions given in clause C.2.1 and Table C.2 in [ISO/IEC 23220-4] apply if not stated otherwise.

##### Table 2 — specific PhotoID data elements

| **Identifier** | **data element identifier**<br> **according to [ISO/IEC 23220-4]** | **Presence in**<br> **APTITUDE DTC** |
| --- | --- | --- |
| ``person_id`` | ``person_id`` | M |
| ``birth_country`` | ``birth_country`` | O |
| ``birth_state`` | ``birth_state`` | O |
| ``birth_city`` | ``birth_city`` | O |
| ``administrative_number`` | ``administrative_number`` | O |
| ``resident_street`` | ``resident_street`` | O |
| ``resident_house_number`` | ``resident_house_number`` | O |
| ``travel_document_type`` | ``travel_document_type`` | O |
| ``travel_document_number`` | ``travel_document_number`` | O |
| ``resident_state`` | ``resident_state`` | O |
| ``travel_document_mrz`` | ``travel_document_mrz`` | O |

#### 3.1.4 ICAO PhotoID data elements

The ICAO PhotoID data elements of APTITUDE DTC SHALL be as defined in Table 3 and belong to the namespace given in 3.1.1. The data element definitions given in clause C.2.1 and Table C.3 in [ISO/IEC 23220-4] apply if not stated otherwise.

##### Table 3 — ICAO PhotoID data elements

| **Identifier** | **data element identifier**<br> **according to [ISO/IEC 23220-4]** | **Presence in**<br> **APTITUDE DTC** |
| --- | --- | --- |
| ``version`` | ``version`` | M |
| ``dg1`` | ``dg1`` | M |
| ``dg2`` | ``dg2`` | M |
| ``dg3`` | ``dg3`` | O |
| ``dg4`` | ``dg4`` | O |
| ``dg5`` | ``dg5`` | O |
| ``dg6`` | ``dg6`` | O |
| ``dg7`` | ``dg7`` | O |
| ``dg8`` | ``dg8`` | O |
| ``dg9`` | ``dg9`` | O |
| ``dg10`` | ``dg10`` | O |
| ``dg11`` | ``dg11`` | O |
| ``dg12`` | ``dg12`` | O |
| ``dg13`` | ``dg13`` | O |
| ``dg14`` | ``dg14`` | O |
| ``dg15`` | no further information<br><br> *Condition:* mandatory if available in eMRTD | C |
| ``dg16`` | ``dg16`` | O |
| ``sod`` | ``sod`` | M |

#### 3.1.5 Additonal document encryption

If a Relying Party requires document encryption in addition to the session encrption layer, it SHALL encode the document request according to [ISO/IEC 18013-5.2]. The EUDI-Wallet SHALL encrypt the requested data elements acording to [ISO/IEC 18013-5.2].  

## 4 Attestation Usage

t.b.d.

## 5 Trust Anchors

The APTITUDE DTC is derived from the physical eMRTD LDS data groups and signed by the national issuing authority. The issuing authority SHALL sign the issuer signed data, i.e. the MSO, using a document signer key and certificate under the respective CSCA root certificate according to clause 2.2 in [ICAO-DTC-TR].

*Note:* According to [ICAO-DTC-TR], the DTC signer certificate includes a dedicated OID in the extendedKeyUsage extension, i.e. ``2.23.136.1.1.12.1``.

It is recommended to make the CSCA root certificates of the EU Member States available to Relying Parties in the EUDI-Wallet ecosytem by a respective EU Trust List, i.e. APTITUDE DTC TL. In addition, it is recommended to make the content of the APTITUDE DTC TL available to Relying Parties outside of the EUDI-Wallet ecosystem by a VICAL according to [ISO/IEC 18013-5].

CSCA root certificates MAY be also obtained from the ICAO PKD by any Relying Party.

## 6 Revocation

Revocation of the APTITUDE DTC, i.e. the mdoc, SHALL be implemented according to [ISO/IEC 18013-5.2], i.e. MSO revocation information. The issuing authority SHALL provide the respective status list.

Revocation of the linked eMRTD and LDS data given in the ICAO PhotoID data elements remains unchanged.

If an APTITUDE DTC is marked revoked, a Relying Party SHALL reject all recieved data elements of the various name spaces. If parts of the data elemnts are encrypted according clause 3.1.5, the Relying Party shall also reject the encrypted data.

## 7 Compliance

If compliance to ICAO DTC-VC is required, a reader may after succsessfull processing the device response and the verification prodecure encapsule the data in the structure given in clause 7.1.

### 7.1 ICAO based encoding

The ICAO based encoding for DTC-VC is defined in the Technical report "Virtual component data structure and PKI Mechanisms" version 1.2 october 2020.
The ICAO based encoding for DTC-PC is defined in the Technical report "Physical component and protocols" version 1.1 october 2022.

```asn.1
DTCContentInfo ::= SEQUENCE {
version Version,
dtcData DTCData,
dtcTBS [0] EXPLICIT DTCTBSValues OPTIONAL,
-- MUST be present if DTC is eMRTD-PC Bound or PC
-- Bound. This field MUST NOT be present if DTC is
-- eMRTD Bound.
dtcSignerInfo [1] EXPLICIT DTCSignerInfo OPTIONAL
-- MUST be present if DTC is eMRTD-PC Bound or PC
-- Bound. This field MUST NOT be present if DTC is
-- eMRTD Bound.
}
DTCTBSValues ::= SEQUENCE SIZE (3..ub-DTCData) OF DTCTBSValue
Version ::= INTEGER { v1(1) }
ub-DTCData INTEGER ::= 31
DTCData ::= SEQUENCE {
dtcSOD [0] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of SOD defined
-- in [Doc 9303]-10.
-- MUST be present if DTC is eMRTD Bound or
-- eMRTD-PC Bound. This field MUST NOT be present
dtcDG1 [1] IMPLICIT OCTET STRING,
-- Contains the encoding of Data Group 1 defined
-- in [Doc 9303]-10.
dtcDG2 [2] IMPLICIT OCTET STRING,
-- Contains the encoding of Data Group 2 defined
-- in [Doc 9303]-10.
dtcDG3 [3] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 3 defined
-- in [Doc 9303]-10.
dtcDG4 [4] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 4 defined
-- in [Doc 9303]-10.
dtcDG5 [5] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 5 defined
-- in [Doc 9303]-10.
dtcDG6 [6] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 6 defined
-- in [Doc 9303]-10.
dtcDG7 [7] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 7 defined
-- in [Doc 9303]-10.
dtcDG8 [8] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 8 defined
-- in [Doc 9303]-10.
dtcDG9 [9] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 9 defined
-- in [Doc 9303]-10.
dtcDG10 [10] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 10 defined
-- in [Doc 9303]-10.
dtcDG11 [11] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 11 defined
-- in [Doc 9303]-10.
dtcDG12 [12] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 12 defined
-- in [Doc 9303]-10.
dtcDG13 [13] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 13 defined
-- in [Doc 9303]-10.
dtcDG14 [14] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 14 defined
-- in [Doc 9303]-10.
dtcDG15 [15] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 15 defined
-- in [Doc 9303]-10.
dtcDG16 [16] IMPLICIT OCTET STRING OPTIONAL,
-- Contains the encoding of Data Group 16 defined
-- in [Doc 9303]-10.
...,
dtcSecurityInfo [22] EXPLICIT DTCSecurityInfo OPTIONAL,
-- MUST be present if DTC is eMRTD-PC Bound or PC
-- Bound. This field MUST NOT be present if DTC
-- is eMRTD Bound.
dtcOtherInfos [23] EXPLICIT DTCOtherInfos OPTIONAL,
-- The dtcOtherInfos is for internal State use.
-- MAY be present if DTC is eMRTD-PC Bound or PC
-- Bound. This field MUST NOT be present if DTC
-- is eMRTD Bound as it is not part of signed
-- data.
}
```

### 7.2 Mapping from photoId to ICAO based encoding

|org.iso.23220.photoID.1 | org.iso.23220.datagroups.1 |eMRTD|
|----                   | ----------          |---|
| dg1 | | EF.DG1 |
| dg2 | | EF.DG2 |
| dg14 | | EF.DG14 |
| sod| | EF.sod |
|    |birth_date | EF.DG1 |
|    |age_over_18 | EF.DG1 |
|    |portrait | EF.DG2 |

## 8 References

| **Item Reference** | **Standard name/details**|
| --- | --- |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO/IEC 18013-5.2] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, second edition, 2026-xx (Status DIS) |
| [ISO/IEC 23220-4] | ISO/IEC TS 23220-4: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 4: Protocols and services for the operational phase, First edition, 2026-04  |
| [ISO/IEC 23220-2.2] | ISO/IEC TS 23220-2: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 2: Data objects and encoding rules for generic eID systems, Second edition, 2026-04  |
 | [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
 | [ICAO-DTC-TR] | ICAO Technical Report, Digital Travel Credentials (DTC) - Virtual Component Data Structure and PKI Mechanisms, Version 1.2, October 2020 |
