# APTITUDE - *Digital Travel Credential (DTC) rulebook*

* Author(s):
  * ...
  * [joenne.kriener@bdr.de](mailto:joenne.kriener@bdr.de)
  
| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |
| 0.2 | 27-05-2026 | Updated based on design assumptions from D3.1  |

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
| XX_XX | According to ICAO’s DTC-VC data model, the APTITUDE DTC SHALL contain DG1, DG2, SOD as from the physical eMRTD passport |
| XX_XX | According to ICAO's DTC-VC data model, the APTITUDE DTC SHALL contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation |
| XX_XX | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (e.g., SD-JWT or mDL). |
| XX_XX | For Type 2 credentials, the data model SHALL include a cryptographic binding between the Virtual Component (VC) and the Physical Component (PC) stored in the Wallet's secure element. |
| XX_XX | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| XX_XX | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |

### Attributes

#### TODO: involve T2.1.2 and WP3

#### TODO: should we specify the source that requires an attribute? i.e. DTC or ICAO or EUDI?

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### Optional attributes

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### Conditional attributes

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### Mandatory metadata

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### Optional metadata

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

### Conditional metadata

| **Data Identifier** | **Definition**          | **Data type**     | **Example value** |
|---------------------|-------------------------|-------------------|-------------------|
| *Provide a value*   | *Provide succinct text* | *Provide a value* | *Provide a value* |

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

## 3 Attestation

### Chapter overview and requirements

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

## 3.1 ISO/IEC 23220-4 PhotoID credential format

The APTITUDE DTC SHALL be encoded using the ISO/IEC 23220-4 PhotoID profile and carried as an ISO/IEC 18013-5 mdoc-cbor payload with document type `org.iso.23220.photoID.1`.

This single-format approach is consistent with the APTITUDE architecture described in WP3_Architektur-20260527.txt:

* the DTC is derived from physical eMRTD LDS data groups,
* the DTC payload is signed by the national issuing authority,
* the DTC is bound to both the physical eMRTD and the Wallet Secure Component,
* the PhotoID format supports the border-control use case and wallet presentation flows.

### 3.1.1 Supported encoding and semantics

The APTITUDE DTC SHALL support the following:

* ISO/IEC 23220-4 PhotoID as the canonical DTC credential format.
* ISO/IEC 18013-5 mdoc-cbor encoding for proximity presentation and secure transport.
* NFC engagement for reader interaction.
* BLE data retrieval for proximity presentation on both Android and iOS devices.
* Preservation of ICAO LDS semantics and the PhotoID profile.
* A hybrid trust structure that allows DTC validation against both ICAO PKI and EUDI Wallet / eIDAS trust mechanisms.
* A single payload model for issuance, storage, and presentation, avoiding a separate SD-JWT DTC format.

### 3.1.2 PhotoID mdoc encoding profile

For proximity presentation and wallet-native use, APTITUDE DTC SHALL use ISO/IEC 18013-5 mdoc-cbor with the PhotoID payload defined by ISO/IEC 23220-4 Annex C.

The following encoding rules SHALL apply:

* `tstr`, `uint`, `bstr`, `bool`, and `tdate` are CDDL representation types defined in RFC 8610.
* A `tstr` SHALL be encoded in UTF-8 and SHALL support the full Unicode range.
* `tstr` attributes SHALL be limited to 150 characters unless otherwise specified.
* `full-date` SHALL be defined as `#6.1004(tstr)` per RFC 8943.
* `tdate` attributes SHALL use RFC 3339 date-time strings.
* Fractions of seconds SHALL NOT be used.
* Time values SHALL use UTC (`Z`) only.
* Canonical CBOR rules from RFC 8949 section 4.2 SHALL be followed.

The mdoc SHALL include the document type `org.iso.23220.photoID.1` and SHALL contain the APTITUDE DTC payload as attestation content.

### 3.1.3 Attribute namespace and identifiers

The APTITUDE DTC credential format profile is designed around three namespaces:

* `org.iso.23220.photoID.1` as the ISO/IEC 18013-5 mdoc document type for the PhotoID credential envelope.
* `urn:eu:eudi-wallet:att:dtc` as the core DTC attribute namespace for APTITUDE-specific credential content derived from eMRTD LDS data groups.
* A domestic or profile-specific namespace for any rulebook-specific attributes that are not part of the EU-wide core DTC profile.

Each APTITUDE DTC attribute SHALL use the namespace `urn:eu:eudi-wallet:att:dtc` for core attributes. Domestic or profile-specific namespaces MAY be used only for rulebook-specific attributes outside EU-wide or sectoral definitions.

| Data Identifier | Attribute identifier | Encoding format | Namespace |
| --- | --- | --- | --- |
| family_name | family_name | tstr | urn:eu:eudi-wallet:att:dtc |
| given_name | given_name | tstr | urn:eu:eudi-wallet:att:dtc |
| date_of_birth | date_of_birth | tdate | urn:eu:eudi-wallet:att:dtc |
| document_number | document_number | tstr | urn:eu:eudi-wallet:att:dtc |
| nationality | nationality | tstr | urn:eu:eudi-wallet:att:dtc |
| photo | face_image | bstr | urn:eu:eudi-wallet:att:dtc |
| dtcSecurityInfo | dtcSecurityInfo | bstr | urn:eu:eudi-wallet:att:dtc |
| dtcIdentifier | dtcIdentifier | tstr | urn:eu:eudi-wallet:att:dtc |
| dtcDOE | dtcDOE | tdate | urn:eu:eudi-wallet:att:dtc |
| sod | sod | bstr | urn:eu:eudi-wallet:att:dtc |
| attestation_legal_category | attestation_legal_category | tstr | urn:eu:eudi-wallet:att:dtc |

### 3.1.4 Relationship to APTITUDE architecture

The APTITUDE DTC is derived from the physical eMRTD LDS data groups and signed by the national issuing authority. The PhotoID credential SHALL carry the same derived content as the DTC data model, ensuring the credential remains linked to the physical document and the wallet secure component.

The DTC SHALL be issued as an ICAO DTC Type 2 credential. The PhotoID payload SHALL preserve the cryptographic binding between the virtual credential and the Wallet Secure Component, while preserving the PhotoID semantics of ISO/IEC 23220-4.

The DTC payload SHALL include:

* DG1, DG2, SOD from the physical eMRTD,
* DTCSecurityInfo, DTCIdentifier, DTCDOE,
* optional eMRTD fallback elements such as EF.CardAccess / PACE SecurityInfos, MRZ or CAN, and DG14 chip authentication data where needed for Tap & Go with eMRTD.

This single-format definition keeps the APTITUDE DTC aligned with the architecture guidance in WP3_Architektur-20260527.txt and avoids introducing a second credential format for the DTC.
