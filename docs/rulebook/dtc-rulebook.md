# APTITUDE - *Digital Travel Credential (DTC) rulebook*

* Author(s):
  * IPZS ...
  * ANTS ...
  * [frank.dietrich@bdr.de](mailto:frank.dietrich@bdr.de)
  
| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |
| 0.2 | 27-05-2026 | Updated based on design assumptions from D3.1  |
| 0.3 | 29-05-2026 | addition of schema and mapping |

## 1 Introduction

### 1.1 Document scope and purpose

This Attestation Rulebook defines the Digital Travel Credential (DTC) as an electronic attestation of attributes for the EUDI Wallet ecosystem. The DTC enables travellers to store and present identity and travel authorization data in their Wallet Unit for border control and travel-related use cases.

The primary objective of the DTC is to facilitate secure and privacy-preserving identity verification and travel document validation at border crossing points and during travel. The DTC is designed to complement existing physical travel documents (e.g. passports, visas) by providing a digital equivalent that supports selective disclosure, offline presentation and strong cryptographic verification.

Within the Aptitude context, the target model is the ICAO DTC Type 2, bound to a physical eMRTD and derived using mechanisms aligned with European regulations and ICAO guidelines.

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

### 1.3 Key words

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

### 1.4 Terminology

Terminologies and definitions within Aptitude project are listed in [APTITUDE Glossary](../glossary.md)

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This section defines the functional and semantic scope of the data composing the APTITUDE Digital Travel Credential (DTC), based on the evidence collected during the stock‑taking phase.

The cross‑border value of a DTC critically depends on preserving full alignment with the ICAO data model while at the same time allowing extensions required for integration within the EUDI Wallet ecosystem and the eIDAS 2.0 framework.

#### Data model

 International interoperability and backward compatibility with existing border‑control infrastructure remain core requirements for any realistic DTC deployment.
 As a result, the ICAO LDS data model (DG1, DG2, SOD) constitutes the mandatory baseline.

 This section defines which data sets must be present and preserved.

| Index | Requirement specification |
| --- | --- |
| XX_XX | According to ICAO’s DTC-VC data model, the APTITUDE DTC SHALL contain DG1, DG2, SOD as from the physical eMRTD passport.|
| XX_XX | According to ICAO's DTC-VC data model, the APTITUDE DTC MAY contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation in case of eMRTD-PC bound    |
| XX_XX | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (e.g., SD-JWT or mDoc acc. ISO 23220-4).                      |
| XX_XX | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset                                                                                                                |
| XX_XX | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties.           |

### 2.2 Requirements
This chapter defines the credential format and encoding requirements for the APTITUDE Digital Travel Credential (DTC). The APTITUDE DTC SHALL use exactly one credential format: the ISO/IEC 23220-4 PhotoID profile, encoded as ISO/IEC 18013-5 mdoc-cbor.

The objective is to preserve a single interoperable DTC representation that is:

* aligned with ICAO DTC Type 2 and eMRTD LDS semantics,
* compatible with EUDI Wallet proximity presentation,
* suitable for both on-site border-control use cases and remote wallet-driven presentations,
* capable of preserving the cryptographic binding between the virtual credential and the Wallet Secure Component (WSCD).

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
#### Issuance

| Index | Requirement specification |
| --- | --- |
| XX_XX | The APTITUDE DTC SHALL be issued exclusively by the National Passport Issuing Authority of the Member State that issued the physical eMRTD. |
| XX_XX | APTITUDE DTC SHALL be derived from eMRTD chip data (Logical Data Structure - LDS) ensuring a cryptographic link to the physical travel document. |
| XX_XX | APTITUDE DTC SHALL be derived both from newly issued and already issued eMRTDs, except where the national authentic sources require a restriction. |
| XX_XX | The issuance process SHALL result in an ICAO DTC Type 2 (eMRTD-PC bound), where the virtual component is cryptographically linked to a physical secure element within the EUDI Wallet. |
| XX_XX | APTITUDE DTC SHALL be digitally signed by the national issuing authority acting as a Trusted Attestation Provider within the eIDAS 2.0 framework. |
| XX_XX | The system SHALL support the complete lifecycle management of the DTC, including secure revocation and update mechanisms managed by the issuing authority. |

#### Data model

International interoperability and backward compatibility with existing border‑control infrastructure remain core requirements for any realistic DTC deployment.

This section defines which data sets must be present and preserved.

| Index | Requirement specification |
| --- | --- |
| DTC_DM_01 | The APTITUDE DTC SHALL contain DG1, DG2, SOD as from the physical eMRTD passport |
| DTC_DM_02 | The APTITUDE DTC SHALL contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation |
| DTC_DM_03 | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (SD-JWT or MDOC-CBOR). |
| DTC_DM_04 | The APTITUDE DTC SHALL include a cryptographic binding between the Virtual Component (VC) and the Physical Component (PC) stored in the WSCD. |
| DTC_DM_05 | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| DTC_DM_06 | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |

## 3 Attestation Encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

#### 3.1.1 APTITUDE DTC document type and namespaces

The objects ``docType`` and ``namespace`` are used to encapsulate the document type and the space in which the data elements are defined.

The document type for the **APTITUDE DTC** SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4].

*Note* The document type is ``org.iso.23220.photoid.1``.

The namespace of APTITUDE DTC for **general PhotoID data elements** defined in clause 3.1.2 SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4] and 6.3.1.1 of [ISO/IEC 23220-2].
The namespace for **specific PhotoID data elements** defined in clause 3.1.3 SHALL be as specified in clause C.2.1 of [ISO/IEC 23220-4]. 
### 3.1.2 General PhotoID data elements

The general PhotoID data elements of APTITUDE DTC SHALL be as defined in Table 1 and belong to the namespace given in 3.1.1.

| **Identifier** | **additional description** | **Presence in APTITUDE DTC** |
| --- | --- | --- |
| ``family_name`` | no further information | M |
| ``given_name`` | no further information | M  |



### 3.1.3 Specific PhotoID data elements
###### Table 2 — specific PhotoID data elements

| **Identifier** | **additional description** | **Presence in APTITUDE DTC** |
| --- | --- | --- |
| ``person_id`` | no further information | M |
| ``birth_country`` | no further information | M |


| Data Identifier | Attribute identifier | Encoding format | Namespace |
| --- |----------------------| --- | --- |
| family_name | family_name          | tstr | org.iso.23220.photoID.1 |
| given_name | given_name           | tstr | org.iso.23220.photoID.1 |
| date_of_birth | date_of_birth        | tdate | org.iso.23220.photoID.1 |
| document_number | document_number      | tstr | org.iso.23220.photoID.1 |
| nationality | nationality          | tstr | org.iso.23220.photoID.1 |
| photo | face_image           | bstr | org.iso.23220.photoID.1 |
| sod | dg1                  | bstr | org.iso.23220.datagroups.1 |
| sod | dg2                  | bstr | org.iso.23220.datagroups.1 |
| sod | dg14                 | bstr | org.iso.23220.datagroups.1 |
| sod | sod                  | bstr | org.iso.23220.datagroups.1 |

### 3.1.4 ICAO PhotoID data elements 

###### Table 3 — ICAO PhotoID data elements

| **Identifier** | **EU additional description** | **Presence in EU-mVRC** |
| --- | --- | --- |
| ``version`` | no further information | M |
| ``dg1`` | no further information | M |

### 3.2 ICAO based encoding

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

### 3.3 Mapping from photoId to ICAO based encoding

|org.iso.23220.photoID.1 | org.iso.23220.datagroups.1 |eMRTD|
|----                   | ----------          |---|
| dg1 | | EF.DG1 |
| dg2 | | EF.DG2 |
| dg14 | | EF.DG14 |
| sod| | EF.sod |
|    |birth_date | EF.DG1 |
|    |age_over_18 | EF.DG1 |
|    |portrait | EF.DG2 |


## 4 Attestation Usage

## 5 Trust Anchors

The APTITUDE DTC is derived from the physical eMRTD LDS data groups and signed by the national issuing authority. The PhotoID credential SHALL carry the same derived content as the DTC data model, ensuring the credential remains linked to the physical document and the wallet secure component.