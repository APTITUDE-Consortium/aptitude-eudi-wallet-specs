# Attestation Rulebook for attestations of type  *APTITUDE DTC*

Author(s):

* Matthias Schwan, bdr, Germany
* Corrado Guidobaldi, IPZS, Italy
* Zahra Ebadi Ansaroudi, FBK, Italy
* Anthony Carmoy, ANTS, France
* Alban Feraud, IN Groupe, France
* Antonio Maio, INCM, Portugal
* Arjan Geluk, A4 Adivsory, The Netherlands

| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |
| 0.2 | 27-05-2026 | Updated based on design assumptions from D3.1  |
| 0.3 | 29-05-2026 | Addition of schema and mapping |
| 0.4 | 12-06-2026 | Synchronization with PhotoID specification in [ISO/IEC 23220-4] |
| 0.5 | 01-07-2026 | Align clause 2 and 3 with rulebook template, bibliography added, trust model and revocation added |
| 0.6 | 08-07-2026 | Use cases added in clause 4, editorial changes |
| 0.7 | 23-07-2026 | Addition of modalities in clause 4.3, editorial changes |

Feedback:

* <matthias.schwan@bdr.de>
* <c.guidobaldi@ipzs.it>
* <zebadiansaroudi@fbk.eu>
* <anthony.carmoy@interieur.gouv.fr>
* <alban.feraud@ingroupe.com>
* <antonio.maio@incm.pt>
* <arjan.geluk@a4advisory.com>

## 1 Introduction

### 1.1 Document scope and purpose

This Attestation Rulebook defines the Digital Travel Credential (DTC) as an electronic attestation of attributes for the EUDI Wallet ecosystem. The DTC enables travellers to store and present identity data in their Wallet Unit for border control and travel-related use cases.

The primary objective of the DTC is to facilitate secure and privacy-preserving identity verification and travel document validation at border crossing points, as well as before and during travel (for details see §4). The DTC is designed to complement existing physical travel documents (e.g., passports, visas) by providing a digital equivalent that supports selective disclosure, proximity, as well as remote presentation and strong cryptographic verification.

Within the APTITUDE context, the target model is the ICAO DTC Type 2, comprising a DTC-VC bound to (1) a physical eMRTD and (2) a DTC-PC which is an EUDI Wallet, and derived using mechanisms aligned with European regulations and ICAO guidelines. A DTC of Type 2 is therefore considered the primary and preferred implementation model. However, in the light of the features, interfaces and specifications of the EUDI Wallet, the mechanisms for binding the DTC-VC to the DTC-PC (i.e. the WSCD/WSCA of the EUDI Wallet) differ from those specificied by ICAO in [ICAO-DTC-PC-TR] (for details see §7). This results in differences in the content of the DTC-VC, as the methods and information for binding the DTC-VC to DTC-PC are different.

Thus, the APTITUDE DTC draws inspiration from the principle underlying ICAO DTC Type 2, i.e. the secure physical element of the ID document, signed by a sovereign authority. The guiding idea is to preserve this trust anchor. Since the ICAO Type 2 specification is at the time of writing still under finalization, APTITUDE DTC may diverge from ICAO’s strict specifications in two key dimensions (for details see §7):

* Data content: The APTITUDE DTC-VC retains ICAO’s core data groups (DG1, DG2, DG14, SOD) and extends them with EUDI Wallet-specific attributes (e.g. for  selective disclosure).
* Presentation protocols: ICAO DTC Type 2 assumes proximity-based interactions with the ID Document eMRTD‘s chip, whereas the APTITUDE DTC leverages EUDI Wallet’s remote and proximity presentation protocols (e.g., OpenID4VP, ISO/IEC 18013-5), introducing additional layers for privacy and interoperability.

The present rulebook specifies:

* The attributes and metadata that comprise an APTITUDE DTC attestation
* The encoding formats to be supported for APTITUDE DTC attestations.
* The issuance, presentation and verification requirements for APTITUDE DTC attestations within the EUDI Wallet framework.
* The trust anchor mechanisms, revocation procedures and compliance requirements that apply to APTITUDE DTC attestations.

### 1.2 Document structure

* Chapter 2, which describes the requirements on the APTITUDE DTC.
* Chapter 3, which specifies how the attestation attributes and metadata are encoded in case the attestation complies with ISO/IEC 18013-5. Each encoding SHALL be specified in a separate section, or even in a separate chapter.
* Chapter 4, which specifies attestation usage.
* Chapter 5, which specifies trust anchors.
* Chapter 6, which specifies revocation.
* Chapter 7, which specifies compliance with ICAO specification.
* Chapter 8, which discusses consideration for the issuance of the APTITUDE DTC.

### 1.3 Key words

This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.

### 1.4 Terminology

Terminology and definitions within APTITUDE project are listed in [APTITUDE Glossary](../../glossary.md)

## 2 Attestation attributes and metadata

### 2.1 Introduction

This section defines the functional and semantic scope of the data composing the APTITUDE Digital Travel Credential (DTC), based on the evidence collected during the stock‑taking phase. The cross‑border value of a DTC critically depends on preserving full alignment with the ICAO data model while at the same time allowing extensions required for integration within the EUDI Wallet ecosystem and the eIDAS 2.0 framework. Minimization of impact on existing border‑control infrastructure would be valuable for DTC deployment. As a result, the ICAO LDS data model (DG1, DG2, DG14, SOD) constitutes the mandatory baseline.

The objective is to preserve a single interoperable DTC representation that is:

* aligned with ICAO DTC Type 2 concept and eMRTD LDS semantics and data model,
* compatible with EUDI Wallet proximity presentation,
* suitable for both on-site border-control use cases and remote wallet-driven presentations,
* capable of preserving the cryptographic binding between the virtual credential and the Wallet Secure Component Application (WSCA).

#### Table 1 — Requirements on data model

| Index | Requirement specification |
| --- | --- |
| DTC_AE_01 | APTITUDE DTC SHALL use ISO/IEC 23220-4 PhotoID as the sole credential format. |
| DTC_AE_02 | APTITUDE DTC SHALL use ISO/IEC 18013-5 mdoc-cbor encoding for the PhotoID credential. |
| DTC_AE_03 | APTITUDE DTC SHALL support NFC engagement for proximity presentation and BLE data retrieval for Android and iOS. |
| DTC_AE_04 | APTITUDE DTC SHALL preserve ICAO LDS semantics and data model, including at least EF.DG1, EF.DG2, EF.DG14, EF.SOD.|
| DTC_AE_05 | APTITUDE DTC SHALL preserve the ISO/IEC 23220-4 PhotoID profile. |
| DTC_AE_06 | APTITUDE DTC SHALL adopt open, standard-based encoding to maximize interoperability and avoid vendor lock-in. <br><br> Note : "open" means that the specification is public and free to use. |
| DTC_AE_07 | APTITUDE DTC SHALL support a trust architecture that enables verification via ICAO CSCA/DS and EUDI Wallet/eIDAS trust anchors. |
| DTC_AE_08 | APTITUDE DTC SHALL preserve the cryptographic binding between the virtual credential and the Wallet Secure Component across issuance, storage, presentation, and verification. |
| DTC_AE_09 | APTITUDE DTC SHALL support selective disclosure and minimisation as a layer on top of the single PhotoID credential format, not by introducing a second credential format. |

#### Table 2 — Requirements on issuing

| Index | Requirement specification |
| --- | --- |
| DTC_IS_01 | APTITUDE DTC SHALL be issued exclusively by the National Passport Issuing Authority of the Member State that issued the corresponding physical eMRTD. <br><br> Note : this requirement applies to the issuing authority and issuing subdivision used for the issuance of the APTITUDE DTC. |
| DTC_IS_02 | APTITUDE DTC SHALL be both issued (1) alongside the issuance of new eMRTDs, or (2) for already issued eMRTDs, except where the national authentic sources or issuing authorities require a restriction. |
| DTC_IS_03 | The issuance process SHALL result in an ICAO DTC Type 2 (eMRTD-PC bound), where the virtual component is cryptographically linked to the WSCD being the physical component within the EUDI Wallet. |
| DTC_IS_04 | The system SHALL support the complete lifecycle management of the DTC, including secure revocation and update mechanisms managed by the issuing authority. |

#### Table 3 — Requirements on data elements

| Index | Requirement specification |
| --- | --- |
| DTC_DM_01 | The APTITUDE DTC SHALL contain DG1, DG2, DG14, SOD  as derived from the physical eMRTD passport and MAY contain other data groups allowed by ICAO DTC-VC specifications, as long as they are also present in the corresponding physical eMRTD. |
| DTC_DM_02 | The APTITUDE DTC MAY contain additional attributes beyond those available in the eMRTD dataset.|
| DTC_DM_03 | The APTITUDE DTC data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |

### 2.2 Mandatory attributes

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``family_name`` | according to [ISO/IEC 23220-2.2] | Hardt |
| ``given_name`` | according to [ISO/IEC 23220-2.2] | Giovanni |
| ``birth_date`` | according to [ISO/IEC 23220-2.2] | 01-01-1980 |
| ``portrait`` | according to [ISO/IEC 23220-2.2] | ... |
| ``age_over_18`` | according to [ISO/IEC 23220-2.2] | T  |
| ``document_number`` | identifier of the APTITUDE DTC according to [ISO/IEC 23220-2.2] | YA1234567 |
| ``person_id`` | according to [ISO/IEC 23220-4] | 1234567890 |
| ``dg1`` | according to [ISO/IEC 23220-4] | PPITA<<HARDT<<GIOVANNI<<<<<<<<<<<<<<<< |
| ``dg2`` | according to [ISO/IEC 23220-4] | ... |
| ``dg14`` | according to [ISO/IEC 23220-4] | ... |

### 2.3 Optional and conditional attributes

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``family_name_viz`` | according to [ISO/IEC 23220-4] | HARDT |
| ``given_name_viz`` | according to [ISO/IEC 23220-4] | GIOVANNI |
| ``enrolment_portrait_image`` | according to [ISO/IEC 23220-4] <br><br> portrait image captured during enrolment of the APTITUDE DTC/PhotoID holder that can be different to image in ``portrait``| ...  |
| ``age_in_years`` | according to [ISO/IEC 23220-4] | 28  |
| ``age_birth_year`` | according to [ISO/IEC 23220-4] | 1998  |
| ``portrait_capture_date`` | according to [ISO/IEC 23220-4] <br> this field denotes the date of capture of the portrait stored in the field “enrolment_portrait_image” | 20-04-2023 |
| ``birthplace`` | according to [ISO/IEC 23220-4] | Italy, Trento |
| ``name_at_birth`` | according to [ISO/IEC 23220-4] | Nick |
| ``resident_address`` | according to [ISO/IEC 23220-4] and further clarified in [ISO/IEC 23220-2.2] | Roma, 45 |
| ``resident_address_latin1`` | according to [ISO/IEC 23220-4] and further clarified in [ISO/IEC 23220-2.2] | Roma, 45 |
| ``resident_city`` | according to [ISO/IEC 23220-4] | Trento |
| ``resident_postal_code`` | according to [ISO/IEC 23220-4] | 38122 |
| ``resident_country`` | according to [ISO/IEC 23220-4] | IT |
| ``resident_city_latin1`` | according to [ISO/IEC 23220-4] | ... |
| ``sex`` | according to [ISO/IEC 23220-4] <br> This field SHALL take either the values '1' (for male), '2' (for female) or '0' (when unknown)| '1' (for male) |
| ``nationality`` | according to [ISO/IEC 23220-4] <br> This field SHALL be encoded in three letter code (alpha-3 code) defined in ISO 3166-1| ITA  |
| ``family_name_latin1`` | according to [ISO/IEC 23220-4] | ...  |
| ``given_name_latin1`` | according to [ISO/IEC 23220-4] | ...  |
| ``birth_country`` |  according to [ISO/IEC 23220-4] | IT |
| ``birth_state`` |  according to [ISO/IEC 23220-4] | Trento |
| ``birth_city`` |  according to [ISO/IEC 23220-4] | Trento |
| ``resident_street`` | according to [ISO/IEC 23220-4] | Roma |
| ``resident_house_number`` | according to [ISO/IEC 23220-4] | 45 |
| ``resident_state`` | according to [ISO/IEC 23220-4] | IT |
| ``dg3`` | according to [ISO/IEC 23220-4] | ... |
| ``dg4`` | according to [ISO/IEC 23220-4] | ... |
| ``dg5`` | according to [ISO/IEC 23220-4] | ... |
| ``dg6`` | according to [ISO/IEC 23220-4] | ... |
| ``dg7`` | according to [ISO/IEC 23220-4] | ... |
| ``dg8`` | according to [ISO/IEC 23220-4] | ... |
| ``dg9`` | according to [ISO/IEC 23220-4] | ... |
| ``dg10`` | according to [ISO/IEC 23220-4] | ... |
| ``dg11`` | according to [ISO/IEC 23220-4] | ... |
| ``dg12`` | according to [ISO/IEC 23220-4] | ... |
| ``dg13`` | according to [ISO/IEC 23220-4] | ... |
| ``dg15`` | according to [ISO/IEC 23220-4] <br><br>*Condition:* mandatory if available in the corresponding physical eMRTD | ... |
| ``dg16`` | according to [ISO/IEC 23220-4] | ... |

### 2.4 Mandatory metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``issue_date`` | date of issuance of the APTITUDE DTC according to [ISO/IEC 23220-2.2] | 20-04-2023 |
| ``expiry_date`` | date of expiry of the APTITUDE DTC according to [ISO/IEC 23220-2.2] | 20-04-2033 |
| ``issuing_authority`` | issuing authority of the APTITUDE DTC according to [ISO/IEC 23220-2.2] | Ministero dell'Interno |
| ``version`` | according to [ISO/IEC 23220-4] | 1.0 |
| ``sod`` | Security object data of related eMRTD according to [ISO/IEC 23220-4] | ... |

### 2.5 Optional metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``issuing_subdivision`` | according to [ISO/IEC 23220-2.2] | TN  |
| ``administrative_number`` | according to [ISO/IEC 23220-4] | 9876543210 |
| ``travel_document_type`` | according to [ISO/IEC 23220-2.2] | PP |
| ``travel_document_number`` | according to [ISO/IEC 23220-4] | I13235678 |
| ``travel_document_mrz`` | according to [ISO/IEC 23220-4] | PPITA<<HARDT<<GIOVANNI<<<<<<<<<<<<<<<< |

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

Member States MAY add additional namespaces under their responsibility. The namespace for **Member State specific data elements** SHALL be as specified in clause C.1.2 of [ISO/IEC 23220-4].

*Note:* The domestic namespace of the European Union is ``org.iso.23220.photoid.EU.1`` with number 1 indicating the version of this namespace and excluding the version number of photoid namespace.

The next section defines general and specific data elements of the PhotoID.
These elements are given in tables of three columns:

* The "Identifier" column is the reference of the data element specified in clause 2.
* The “data element identifier according to [ISO/IEC 23220-4]” column gives the mapping of the data element to the data element identifier specified in [ISO/IEC 23220-4].
* The "Presence" column indicates whether the presence of the element on an APTITUDE DTC is mandatory (M), optional (O) or conditional (C). A mandatory data element SHALL be present in an APTITUDE DTC whereas an optional data element MAY be present. If a data element is conditional the respective condition is given in the specification. If the condition is met the data element SHALL be present.

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
| ``resident_address_latin1`` | ``resident_address_latin1`` | O  |
| ``resident_city`` | ``resident_city`` | O  |
| ``resident_postal_code`` | ``resident_postal_code`` | O  |
| ``resident_country`` | ``resident_country`` | O  |
| ``resident_city_latin1`` | ``resident_city_latin1`` | O  |
| ``sex`` | ``sex`` | O  |
| ``nationality`` | ``nationality`` | O  |
| ``document_number`` | ``document_number`` | M  |
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
| ``travel_document_type`` | ``travel_document_type`` | M <br><br>As per [ISO/IEC 23220-4] it SHALL be present as dg1 data element SHALL be present |
| ``travel_document_number`` | ``travel_document_number`` | M |
| ``resident_state`` | ``resident_state`` | O |
| ``travel_document_mrz`` | ``travel_document_mrz`` | M <br><br>As per [ISO/IEC 23220-4] it SHALL be present as dg1 data element SHALL be present |
| ``family_name_viz`` | ``family_name_viz`` | HARDT |
| ``given_name_viz`` | ``given_name_viz`` | GIOVANNI |
| ``enrolment_portrait_image`` | ``enrolment_portrait_image`` | O |

#### 3.1.4 ICAO PhotoID data elements

The ICAO PhotoID data elements of APTITUDE DTC SHALL be as defined in Table 3 and belong to the namespace given in 3.1.1. The data element definitions given in clause C.2.1 and Table C.3 in [ISO/IEC 23220-4] apply if not stated otherwise.

##### Table 3 — ICAO PhotoID data elements

| **Identifier** | **data element identifier**<br> **according to [ISO/IEC 23220-4]** | **Presence in**<br> **APTITUDE DTC** |
| --- | --- | --- |
| ``version`` | ``version`` | M |
| ``dg1`` | ``dg1`` | M |
| ``dg2`` | ``dg2`` | M |
| ``dg3`` | ``dg3`` | Not present |
| ``dg4`` | ``dg4`` | Not present |
| ``dg5`` | ``dg5`` | O |
| ``dg6`` | ``dg6`` | O |
| ``dg7`` | ``dg7`` | O |
| ``dg8`` | ``dg8`` | O |
| ``dg9`` | ``dg9`` | O |
| ``dg10`` | ``dg10`` | O |
| ``dg11`` | ``dg11`` | O |
| ``dg12`` | ``dg12`` | O |
| ``dg13`` | ``dg13`` | O |
| ``dg14`` | no further information<br><br> *Note:* DG14 is mandatory in EU/SAC eMRTDs | M |
| ``dg15`` | no further information<br><br> *Condition:* mandatory if available in eMRTD | C |
| ``dg16`` | ``dg16`` | O |
| ``sod`` | ``sod`` | M |

#### 3.1.5 Additional document encryption

If a Relying Party requires document encryption in addition to the session encryption layer, it SHALL use the "Document response encryption" security mechanism as defined in [ISO/IEC 18013-5.2] and encode the document request according to [ISO/IEC 18013-5.2]. The EUDI Wallet SHALL encrypt the requested data elements according to [ISO/IEC 18013-5.2].  

#### 3.1.6 Mapping from PhotoID to ICAO-based encoding

The following table maps selected PhotoID data elements to the corresponding ICAO eMRTD LDS data, either as carried ICAO data groups or as values obtained or computed from those data groups.

|org.iso.23220.1 | org.iso.23220.datagroups.1 |eMRTD|
|----                   | ----------          |---|
| | dg1 | EF.DG1 |
| | dg2 | EF.DG2 |
| | dg14 | EF.DG14 |
| | sod | EF.SOD |
| birth_date | | EF.DG1 |
| age_over_18 | | EF.DG1 |
| portrait | | EF.DG2 |

More details regarding the mapping of the content of the PhotoID with the eMRTD content are  provided in clause 8.

## 4 Attestation Usage

This section briefly describes how attestations of type *APTITUDE DTC* are intended to be used. All requested attributes are examples and the request may include other data elements as given in the use cases.

### 4.1 Airline-mediated remote pre‑clearance (airline registers passenger with Border Control)

**Context:** Passenger who booked an international flight checks in remotely (app or website) and the airline must register the passenger with the Member State Border Authority for pre‑clearance (advance checks / pre‑assessment), see [APTITUDE-D3.1].

This use case is without prejudice to applicable Advance Passenger Information (API) obligations, including [EU-API-2025-12] where applicable. APTITUDE DTC data MAY support or complement the carrier’s API submission, subject to Member State implementation.

[//]: # (See D3.1: Stock‑Taking, Analysis and Specifications — pilot use cases and advance submission, 27‑02‑2026.)

**Flow:** remote (airline backend → Border Authority submission endpoint / Traveller Router).

[//]: # (D3.1 documents airline‑mediated pre‑assessment patterns but does not mandate a single transport/envelope.)

**Requested attributes:**

APTITUDE DTC:

* General PhotoID data elements: ``family_name``, ``family_name_latin1``, ``given_name``, ``given_name_latin1``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``
* Special PhotoID data elements: ``travel_document_mrz``
* ICAO PhotoID data elements: ``version``, ``dg1``, ``dg2``, ``dg14``, ``sod``, and ``dg15`` where available and required by the Border Authority.

[//]: # (These are the rulebook §2 mandatory/priority attributes; D3.1 does not define a stricter per‑scenario list.)

**Post‑processing:** the airline backend (or its designated submission service) MUST verify holder proof/possession assertions from the wallet (if applicable), carry out the issuer data authentication of the APTITUDE DTC as defined in [ISO/IEC 18013-5.2], and validate the certificate chain and check revocation/status using the applicable trust anchors (CSCA/DS and/or EU trust lists) as defined in clause 5. The airline then packages the verified data for server‑to‑server submission to the Border Authority (mapping of APTITUDE DTC elements to the receiving envelope is a Member State decision; legacy readers may require extraction/encapsulation into ICAO DTCContentInfo/ASN.1 (DTC-VC compliant with [ICAO-DTC-VC-TR]). The Border Authority performs full verification in accordance with ICAO trust framework (passive authentication: SOD/DG hash checks, PKI chain, revocation/status) and ingests the required ICAO PhotoID data elements for registration and risk checks. Where supported by the Member State implementation, the verification outcome MAY be returned to the traveller through the carrier or designated submission channel.

[//]: # (D3.1 describes the pre‑assessment use case and the need for an interoperable transmission protocol; it does not mandate a single packaging mechanism — implementers must document the chosen transport and envelope.)

### 4.2 Traveller direct pre‑registration (traveller → Member State pre‑travel system)

**Context:** EU national uses their EUDIW or the EU Digital Travel Application to submit their DTC directly to a Member State’s pre‑travel system for advance checks within a 36‑hour window.

[//]: # (See D3.1 §§1.2 and 3.2 for traveller‑initiated advance submission.)

**Flow:** remote (wallet → Traveller Router or direct submission endpoint → Border backend). The remote presentation protocol complies with the regulation's Implementing Acts (i.e. OpenID4VP and iso18013-7).

**Requested attributes:**

APTITUDE DTC:

* General PhotoID data elements: ``family_name``, ``family_name_latin1``, ``given_name``, ``given_name_latin1``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``, ``age_over_18``, ``portrait``
* Special PhotoID data elements: ``travel_document_mrz``
* ICAO PhotoID data elements: ``version``, ``dg1``, ``dg2``, ``dg14``, ``sod``.

The request may include ``age_over_18`` where required for age-based verification or ``portrait`` if required by the Member State for biometric pre‑matching.

[//]: # (These follow the rulebook §2 attribute set; D3.1 does not specify per‑scenario attribute subsets.)

**Post-processing:** the receiving Border backend validates the wallet presentation, including any proof of possession, carry out the issuer data authentication of the APTITUDE DTC as defined in [ISO/IEC 18013-5.2], and validate the certificate chain and check revocation/status using the applicable trust anchors (CSCA/DS and/or EU trust lists) as defined in clause 5. Verification outcome drives pre-assessment workflows (EES/ETIAS/API/SIS/SLTD queries). If selective disclosure was used, the backend MUST verify the integrity and authenticity of the disclosed PhotoID data elements using the cryptographic mechanism of the selected data format. Where ICAO PhotoID data elements are disclosed, the backend SHALL additionally perform ICAO passive authentication by validating the SOD, checking the disclosed DG hashes, and verifying the applicable ICAO trust chain. Where supported by the Member State implementation, the backend MAY return a status or operational instruction to the traveller, such as confirmation of successful pre-registration, required corrective action, or guidance on the applicable border-control process.

[//]: # (D3.1 highlights the selective‑disclosure vs LDS integrity tension but does not prescribe a single resolution, so the Member State policy must define acceptance criteria.)

### 4.3 Proximity presentation at border control (on‑site verification / e‑gate or officer kiosk)

**Context:** Traveller presents their APTITUDE DTC from the EUDIW at the border control point (e‑gate, kiosk or officer reader) for immediate verification and biometric match. (D3.1 describes proximity presentation requirements and the need to reconcile ISO/IEC 18013‑5 and ICAO NFC/APDU approaches.)

**Flow:** proximity (device engagement / NFC or mdoc proximity per chosen implementation).

**Modalities (as defined in D3.2 Chapter 10.3 Functional Flow):**

1. Proximity presentation of the APTITUDE DTC and 1:1 matching: The user presents its APTITUDE DTC from the EUDI Wallet, with device engagement, allowing gates to retrieve the APTITUDE DTC from the wallet with biometric verification in 1:1 between the passenger and the photo contained in his APTITUDE DTC.

2. Proximity presentation of a token and 1:1 matching: The user presents a token, containing a decryption key, allowing the gates to decrypt the pre-loaded APTITUDE DTC for a specific flight. 1:1 biometric matching between the passenger and the photo contained in the pre-loaded APTITUDE DTC.

3. Proximity presentation of the DTC‑VC (compliant with [ICAO-DTC-VC-TR]), retrieval of the pre-loaded DTC‑VC and 1:1 matching: The traveller presents the DTC-VC stored in their wallet (or taps their passport at the gate). The information presented enables the gate to identify and retrieve the corresponding DTC-VC, previously pre-loaded in the gate system together with its associated pre-clearance status. The gate then performs a matching between the DTC-VC presented by the traveller and the pre-loaded DTC-VC to authenticate the traveller and confirm the correct record has been retrieved. Once this matching has been successfully completed, a 1:1 biometric verification is performed between the traveller and the portrait contained in the corresponding pre-loaded DTC-VC.

4. Matching 1:n then presentation of the APTITUDE DTC: The user approaches the gates, and proceeds to a 1:n matching to retrieve the APTITUDE DTC preloaded in the gates. He then presents his APTITUDE DTC stored in his EUDI Wallet (or tap his passport), in order to establish the cryptographic link to authenticate the passenger and his APTITUDE DTC.

**Requested attributes:**

APTITUDE DTC

* General PhotoID data elements: ``family_name``, ``family_name_latin1``, ``given_name``, ``given_name_latin1``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``age_over_18``, ``portrait``
* Special PhotoID data elements: ``person_id``
* ICAO PhotoID data elements: ``version``, ``dg1``, ``dg2``, ``dg14``, ``sod``, and ``dg15`` where available and required for Active Authentication.

Priority attributes for on‑site verification and biometric matching are ``dg2`` (portrait), ``dg1`` (biographic / MRZ), ``sod``, ``dg14`` if the Member State uses it for inspection. Attributes ``version``, ``person_id``, ``expiry_date``, ``issuing_authority``, ``age_over_18`` and ``portrait`` are optional depending on the check (age verification, biometric fallback).

[//]: # (Chosen attributes reflect rulebook §2 priorities and D3.1 emphasis on DG2/SOD for biometric anchoring.)

**Post‑processing:** the proximity reader / e‑gate performs device engagement, retrieves the APTITUDE DTC, validates SOD / passive authentication in accordance with ICAO trust framework(signature verification and PKI chain to CSCA/PKD), checks revocation/status and carries out biometric 1:1 matching of the live capture to dg2. The gate/backend then forwards verification results and any required DGs (dg1/dg2/sod and selected metadata) to backend systems for database checks (EES, SIS, SLTD) and final decision. The pilot MUST state whether translation to ASN.1 DTCContentInfo (DTC-VC compliant with [ICAO-DTC-VC-TR]) is required for legacy inspection systems; D3.1 signals this requirement as a possible necessity but does not fix the mapping responsibilities. The reader, eGate or officer interface presents the applicable operational outcome according to the Member State border-control process.
Where deemed necessary by the border control authority, the field ``dg14`` obtained from the ICAO PhotoID data elements MAY be used by the reader to verify the cryptographic binding between the APTITUDE DTC being presented and the eMRTD owned by the traveller. The same applies for the DTC-VC compliant with [ICAO-DTC-VC-TR] obtained from the APTITUDE DTC.

### 4.4 Cross‑jurisdiction proximity presentation (EU traveller arriving outside Schengen — optional)

**Context:** EU national with an EUDIW‑stored APTITUDE DTC presents the credential in proximity to a non‑EU local border authority to test cross‑jurisdiction interoperability.

[//]: # (D3.1 lists the outside‑Schengen arrival scenario as optional and highlights interoperability constraints.)

**Flow:** proximity (wallet → non‑EU verifier). The destination’s native inspection interface determines the mode (NFC/APDU, mdoc, or other).

[//]: # (D3.1 notes that non‑EU systems may expect ICAO ASN.1 structures and PKI anchors.)

**Requested attributes:**

APTITUDE DTC

* General PhotoID data elements: ``family_name``, ``family_name_latin1``, ``given_name``, ``given_name_latin1``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``, ``portrait``
* Special PhotoID data elements: ``travel_document_mrz``
* ICAO PhotoID data elements: ``version``, ``dg1``, ``dg2``, ``dg14``, ``sod``.

[//]: # (D3.1 does not define which attributes a receiving non‑EU authority will require; this baseline reflects rulebook §2 mandatory/priority elements typically needed for equivalence to an eMRTD.)

**Post‑processing:** the non‑EU verifier validates the credential using ICAO PKI (CSCA/DS via PKD) and its local acceptance policy. If the receiving system requires ICAO ASN.1 DTCContentInfo (DTC-VC compliant with [ICAO-DTC-VC-TR]), an intermediate gateway or the wallet/traveller router may need to extract the disclosed ICAO PhotoID data elements and encapsulate them accordingly; D3.1 documents that such translation and trust alignment are common cross‑jurisdiction issues but does not prescribe which actor must perform the translation. If the verifier cannot validate under available trust anchors, the fallback/acceptance policy is a matter for the receiving authority. Where supported by the receiving authority, the verifier MAY return an operational outcome to the traveller according to the applicable local border-control process.

### 4.5 Booklet-based proximity presentation to legacy eGate (“fallback”)

**Context:** Use cases 4.1 or 4.2 have succeeded such that traveller has been successfully registered. Traveller approaches legacy eGate in order to cross the border, with booklet passport.

**Flow:**

Option 1: MRZ Scan (traditional)

* Scan the Machine Readable Zone (MRZ) on the travel document.
* Open the chip.
* Link the document to the pre-registration data by matching dg1, for example.
* Perform biometric verification.
* Active/Chip Authentication

Option 2: Tap&go

* Biometric identification.
* Link person to the pre-registration data
* Open the chip using the document-supported access mechanism, then link the result to the pre-registration data, for example by matching ``dg1`` or the corresponding ``document_number``.
* Active/Chip Authentication

**Requested attributes:**

APTITUDE DTC (see pre-registration use cases 4.1 or 4.2)

* ICAO PhotoID data elements: ``version``, ``dg1``, ``dg2``, ``dg14``, ``sod``, and ``dg15`` where available and required by the inspection system.

**Post-processing:** the legacy eGate or officer interface performs the applicable chip, document and biometric checks, links the live passport read to the pre-registration data, and presents the applicable operational outcome according to the Member State border-control process.

## 5 Trust Anchors

The APTITUDE DTC is derived from data contained in the LDS data groups of the corresponding physical eMRTD and is signed by the national issuing authority. The issuing authority SHALL sign the issuer signed data, i.e. the Mobile Security Object (MSO), using a DTC signer key and certificate under the respective CSCA root certificate.
The document signer key and certificate SHALL comply with clause 2.2 in [ICAO-DTC-VC-TR] and SHALL meet the following conditions:

* The DTC signer certificate SHALL include the following OID in the extendedKeyUsage extension : xxxxx;

The following key usage period and certificate/public key validity period SHALL be used for the DTC signer:

* Private key usage period : between xx days and 3 months;
* certificate/public key validity period : xxx;

* Private key usage period : between xx days and 3 months;
* certificate/public key validity period : xxx;

The following key usage period and certificate/public key validity period SHALL be used for the DTC signer:

* Private key usage period : between xx days and 3 months;
* certificate/public key validity period : xxx;

It is recommended to make the CSCA root certificates of the EU Member States available to Relying Parties in the EUDI Wallet ecosytem by a respective EU Trust List, i.e. APTITUDE DTC TL.

CSCA root certificates MAY also be obtained from the ICAO PKD by any Relying Party.

For the purpose of interoperability tests and piloting, issuing authorities are requested to provide certificates of a test CSCA which

* SHALL be published at a stated distribution point,
* SHALL be bounded in validity and
* SHALL be distinguishable from production trust anchors, and the operator of the test PKI SHALL be name

## 6 Revocation

### 6.1 Reasons for revocation

Reasons for revocation or invalidation may include, but are not limited to, device loss or compromise of the Wallet Unit, revocation or replacement of the corresponding physical eMRTD, compromise of the APTITUDE DTC issuer certificate or issuer trust chain, incorrect or fraudulently issued APTITUDE DTC data, or invalidation of the applicable ICAO certificate chain.

### 6.2 APTITUDE DTC revocation

Revocation of the APTITUDE DTC, i.e. the mdoc, SHALL be implemented according to [ISO/IEC 18013-5.2], i.e. MSO revocation information. The issuing authority SHALL provide the respective status list.

If an APTITUDE DTC is marked revoked, a Relying Party SHALL reject the APTITUDE DTC and all received data elements of the various namespaces.

### 6.3 Linked eMRTD revocation

Revocation of the linked eMRTD and LDS data given in the ICAO PhotoID data elements remains unchanged and is governed by the applicable ICAO, eMRTD and national procedures.

## 7 Compliance with ICAO specifications

After successfully processing the device response and the verification procedure, a reader MAY recontruct from the content of the APTITUDE DTC Attestation an ICAO compliant DTC-VC as defined in [ICAO-DTC-VC-TR], supporting the following Type of ICAO DTC:

**ICAO DTC Type 1, also named eMRTD bound DTC**
In this case the reader SHALL bundle the ``dg1``, ``dg2``, ``sod``, and if present ``dg3``, ``dg4``, ``dg5``, ``dg6``, ``dg7``, ``dg8``, ``dg9``, ``dg10``, ``dg11``, ``dg12``, ``dg13``, ``dg14``, ``dg15``, ``dg16`` within the structure ``DTCData`` to build the structure ``DTCContentInfo``.

*Note:* In this case, the structure ``DTCContentInfo`` does not contain stuctures ``DTCTBS``, ``DTCSignerInfo``, ``DTCSecurityInfo`` and ``DTCOtherInfo``.

The binding between the DTC-VC and the EUDI Wallet enabled by the Rulebook is not compliant with the mechanisms currently defined by ICAO for the binding between the DTC-VC and DTC-PC. Therefore, the following features allowed by the Rulebook are currently not compliant with ICAO specifications:

* binding between the DTC-PC (EUDI Wallet) and the DTC-VC;
* security mechanisms implemented by the DTC-PC (EUDI Wallet);

### 7.1 Compliance with ICAO specifications

The following statements apply for APTITUDE DTC:

1. APTITUDE DTC is compliant to DTC-VC Type 1 acc. to [ICAO-DTC-VC-TR], i.e. the eMRTD being the physical component.
2. APTITUDE DTC is compliant to DTC-VC Type 2 acc. to [ICAO-DTC-VC-TR] with the following properties
    * eMRTD-PC is implemented through EUDI-Wallet including WSCD/WSCA
    * DTCCapabilitiesInfo is substituted by device engagement in proximity case
    * DTCSignerInfo is substituted by IssuerSigned data, i.e. Mobile Security Object, of mdoc structure
    * DTCSecurityInfo is substituted by IssuerSigned data, i.e. Mobile security Object, of mdoc structure
    * Cryptographic link between DTC-VC and DTC-PC is provided by Device Request/Response protocol according to ISO/IEC 18013-5
3. Strength of cloning protection of APTITUDE DTC, i.e authentication factor of possession, is determined by strength of WSCD/WSCA mechanisms, i.e. protection of the device key managed by the WSCD/WASCA.
4. APTITUDE DTC can be verified by any reader, i.e. Relying Party, within EUDI-Wallet ecosystem.
5. APTITUDE DTC can be verified internationally by any reader compliant to ISO/IEC 18013-5 and ISO/IEC 18013-7.
6. APTITUDE DTC does not support ICAO protocols according to [ICAO-DTC-PC-TR], e.g. ISO/IEC 14443 interface, PACE protocols, and anti-cloning methods like Chip Authentication or Active Authentication as this is implemented based on other protocols (see statement 2)

* ICAO DTC Type 1, also named eMRTD bound DTC;
* eMRTD bound extended DTC;

#### ICAO DTC Type 1, also named eMRTD bound DTC

After successfully processing the device response and the verification procedure, a reader MAY recontruct from the content of the APTITUDE DTC Attestation an ICAO compliant DTC-VC as defined in [ICAO-DTC-VC-TR].

In this case the reader SHALL bundle the ``dg1``, ``dg2``, ``sod``, and if present ``dg3``, ``dg4``, ``dg5``, ``dg6``, ``dg7``, ``dg8``, ``dg9``, ``dg10``, ``dg11``, ``dg12``, ``dg13``, ``dg14``, ``dg15``, ``dg16`` within the structure ``DTCData`` to build the structure ``DTCContentInfo`` (see §7.2).

#### eMRTD bound extended DTC

In this case the reader SHALL bundle the ``dg1``, ``dg2``, ``sod``, and if present ``dg3``, ``dg4``, ``dg5``, ``dg6``, ``dg7``, ``dg8``, ``dg9``, ``dg10``, ``dg11``, ``dg12``, ``dg13``, ``dg14``, ``dg15``, ``dg16`` to get the structure ``DTCData``. Subsequently, the reader SHALL (1) append the stucture ``DTCOtherInfo`` found within the APTITUDE DTC Attestation in the structure ``DTCData`` and (2) bundle the structures ``DTCTBS`` and ``DTCSignerInfo`` found within the APTITUDE DTC Attestation together with ``DTCData`` to build the structure ``DTCContentInfo``.
Conversly, during issuance of the APTITUDE DTC, the issuing authority SHALL compute the following structures in accordance with [ICAO-DTC-VC-TR] and store them within the APTITUDE DTC Attestation:

* ``DTCTBS``
* ``DTCOtherInfo``
* ``DTCSignerInfo``

*Note:* In this case, the structure ``DTCData`` does not contain the stucture ``DTCSecurityInfo``.

The binding between the DTC-VC and the EUDI Wallet enabled by the Rulebook is not compliant with the mechanisms currently defined by ICAO for the binding between the DTC-VC and DTC-PC. Therefore, the following features allowed by the Rulebook are currently not compliant with ICAO specifications:

* binding between the DTC-PC (EUDI Wallet) and the DTC-VC;
* security mechanisms implemented by the DTC-PC (EUDI Wallet);

### 7.2 ICAO based encoding

The ICAO based encoding for DTC-VC is defined in [ICAO-DTC-VC-TR] and encoding for DTC-PC is defined in [ICAO-DTC-PC-TR]. The ASN.1 definition below reproduces the generic ICAO DTC-VC encoding. For APTITUDE DTC, only the eMRTD-bound encoding is applicable. The eMRTD-PC-bound encoding is retained for comparison with the ICAO Type 2 model, while the PC-bound encoding is outside the scope of the current profile.

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

## 8 Consideration for issuance of APTITUDE DTC credentials

APTITUDE DTC is bound to an existing eMRTD, either issued before the APTITUDE DTC (pre-existing eMRTD) or issued simultaneously.
Many of the attributes contained in the APTITUDE DTC are or may be also present in the underlying eMRTD. Therefore it is of the utmost importance to ensure their consistency with the eMRTD content to (1) avoid creation of flawed APTITUDE DTC and (2) avoid errors when the APTITUDE DTC is processed by a relying party. Where the issuing authority reads out the eMRTD and reuses its content for APTITUDE DTC issuance, consistency is directly ensured. Alternatively, issuing authority may also issue an APTITUDE DTC with attributes obtained from its own registers, provided consistency with eMRTD content is guaranteed.
Other attributes contained in the APTITUDE DTC are not present in eMRTD, and therefore have to be provided by the issuing authority at DTC issuance. These attributes are either attributes related to the holder which are absent from eMRTD LDS, or relating to the APTITUDE DTC credential.
The first table below aims at showing for each attribute of the APTITUDE DTC whether:

* it is present in the underlying eMRTD;
* it may be present in the underlying eMRTD, and if absent, it shall be provided by the issuing authority;
* it is not present in the underlying eMRTD and shall be provided by the issuing authority;

| **Data field** | **Is present in the eMRTD**| **May be present in the eMRTD<br><br>If not present in the eMRTD, provided by the issuing authority**| **Provided by the issuing authority**|
| ----- | ----- |----- |----- |
| **Mandatory Attributes**||||
| ``family_name`` | | X | |
| ``given_name`` | | X | |
| ``birth_date`` | X | | |
| ``portrait`` | | X | |
| ``age_over_18`` | | | X |
| ``document_number`` | | | X |
| ``person_id`` | | | X |
| ``dg1`` | X  | | |
| ``dg2`` | X | | |
| ``dg14`` | X | | |
| **Optional Attributes**||||
| ``family_name_viz`` | X | | |
| ``given_name_viz`` | X | | |
| ``enrolment_portrait_image`` | | | X |
| ``age_in_years`` | | | X |
| ``age_birth_year`` | X | | |
| ``portrait_capture_date`` | | X | |
| ``birthplace`` | | X | |
| ``name_at_birth`` | | | X |
| ``resident_address`` | | X | |
| ``resident_address_latin1`` | | X | |
| ``resident_city`` | | X | |
| ``resident_postal_code`` | | X | |
| ``resident_country`` | | X | |
| ``resident_city_latin1`` | | X | |
| ``sex`` | X | | |
| ``nationality`` | X | | |
| ``family_name_latin1`` | | X | |
| ``given_name_latin1`` | | X | |
| ``birth_country`` | | X | |
| ``birth_state`` | | X | |
| ``birth_city`` | | X | |
| ``resident_street`` | | X | |
| ``resident_house_number`` | | X | |
| ``resident_state`` | | X | |
| ``dg3`` | X | | |
| ``dg4`` | X | | |
| ``dg5`` | X | | |
| ``dg6`` | X | | |
| ``dg7`` | X | | |
| ``dg8`` | X | | |
| ``dg9`` | X | | |
| ``dg10`` | X | | |
| ``dg11`` | X | | |
| ``dg12`` | X | | |
| ``dg13`` | X | | |
| ``dg15`` | X | | |
| ``dg16`` | X | | |
| **Mandatory Metadata**||||
| ``issue_date`` | | | X |
| ``expiry_date`` | | | X |
| ``issuing_authority`` | X | | |
| ``version`` | | | X |
| ``sod`` | X | | |
| **Optional Metadata**||||
| ``issuing_subdivision`` | | | X |
| ``administrative_number`` | | | X |
| ``travel_document_type`` | X | | |
| ``travel_document_number`` | X | | |
| ``travel_document_mrz`` | X | | |

The second table below defines the rules applicable to each of these attributes including:

* requirements to ensure overall consistency between the APTITUDE DTC and the underlying eMRTD;
* clarification as to whether it refers to the  eMRTD or APTITUDE DTC (where applicable);
* the origin of the attribute;

| **Data field** | **Value**|
| ----- | ----- |
| **Mandatory Attributes**|<br><br>|
| ``family_name`` |This field MAY not be present in the eMRTD.<br><br>If a DG11 is present in the eMRTD, this field SHALL contain the family name present in the DE “Name of holder (in full)” of the DG11 (if this DE is present).<br><br> Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``given_name`` |This field MAY not be present in the eMRTD.<br><br>If a DG11 is present in the eMRTD this field SHALL contain the given name present in the DE “Name of holder (in full)” of the DG11 (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority|
| ``birth_date`` |This field SHALL contain the DE “Date of birth” as found in DG1 of the eMRTD|
| ``portrait`` |This field SHALL contain the image present in the DG2 (JPEG or JPEG2000 without any metadata) of the eMRTD|
| ``age_over_18`` |This field SHALL be computed by the issuing authority at DTC issuance from the DE “date of birth” (see above) and a date of reference.|
| ``document_number`` |This field SHALL be assigned by the issuing authority at DTC issuance.<br><br>This information is related to the DTC and not the eMRTD.|
| ``person_id`` |This field SHALL be assigned by the issuing authority at DTC issuance.|
| ``dg1`` |This field SHALL replicate the DG1 of the eMRTD|
| ``dg2`` |This field SHALL replicate the DG2 of the eMRTD|
| ``dg14`` |This field SHALL replicate the DG14 of the eMRTD|
| **Optional Attributes**||
| ``family_name_viz`` |This field SHALL contain the family name present in the DE “name of holder” as found in DG1 of the eMRTD|
| ``given_name_viz`` |This field SHALL contain the given name present in the DE “name of holder” as found in DG1 of the eMRTD|
| ``enrolment_portrait_image`` |This field MAY contain a newer portrait acquired in the course of the DTC issuance process by the issuing authority, provided it is matched with the one stored in the DG2 of the eMRTD|
| ``age_in_years`` |This field SHALL be computed by the issuing authority at DTC issuance from the DE “date of birth” (see above) and a date of reference.|
| ``age_birth_year`` |This field SHALL contain the year present in the DE “Date of birth” as found in DG1 of the eMRTD|
| ``portrait_capture_date`` |This field MAY be present if the field ``enrolment_portrait_image`` is present. If present, it SHALL indicate the capture date of ``enrolment_portrait_image``.|
| ``birthplace`` |If the eMRTD contains a DG11, this field SHALL contain the value present in the DE “place of birth” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``name_at_birth`` |This field is not present in the eMRTD LDS.<br><br>This field SHALL be provided by the DTC issuing authority.|
| ``resident_address`` |If the eMRTD contains a DG11, this field SHALL contain the value present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_address_latin1`` |If the eMRTD contains a DG11, this field SHALL contain the value present in the DE “Permanent address” (if this DE is present and if expressed using latin alphabet).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_city`` |If the eMRTD contains a DG11, this field SHALL contain the resident city present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_postal_code`` |If the eMRTD contains a DG11, this field SHALL contain the postal code present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_country`` |If the eMRTD contains a DG11, this field SHALL contain the country present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_city_latin1`` |This field MAY not be present in the eMRTD.<br><br>If a DG11 is present in the eMRTD, this field SHALL contain the city present in the DE “Permanent address” (if this DE is present and if expressed using latin alphabet).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``sex`` |This field SHALL contain the DE “sex” as found in DG1 of the eMRTD converted as follows 'M' => '1', 'F' =>'2', '<' or 'X' =>'0'|
| ``nationality`` |This field SHALL contain the DE “Nationality” as found in DG1 of the eMRTD.<br><br>This field SHALL be encoded as three letter code alpha-3 code defined in ISO 3166-1.|
| ``family_name_latin1`` |This field MAY not be present in the eMRTD.<br><br>If a DG11 is present in the eMRTD, this field SHALL contain the family name present in the DE “Name of holder (in full)” (if this DE is present and if expressed using latin alphabet).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``given_name_latin1`` |This field MAY not be present in the eMRTD.<br><br>If a DG11 is present in the eMRTD, this field SHALL contain the given name present in the DE “Name of holder (in full)” (if this DE is present and if expressed using latin alphabet).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``birth_country`` |If a DG11 is present in the eMRTD this field SHALL contain the birth country present in the DE “Place of birth” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
|``birth_state``|If a DG11 is present in the eMRTD this field SHALL contain the birth state present in the DE “Place of birth” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``birth_city`` |If a DG11 is present in the eMRTD this field SHALL contain the birth city present in the DE “Place of birth” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_street`` |If the eMRTD contains a DG11, this field SHALL contain the street present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_house_number`` |If the eMRTD contains a DG11, this field SHALL contain the house number present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``resident_state`` |If the eMRTD contains a DG11, this field SHALL contain the state present in the DE “Permanent address” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``dg3`` |This field SHALL replicate the DG3 of the eMRTD.|
| ``dg4`` |This field SHALL replicate the DG4 of the eMRTD.|
| ``dg5`` |This field SHALL replicate the DG5 of the eMRTD.|
| ``dg6`` |This field SHALL replicate the DG6 of the eMRTD.|
| ``dg7`` |This field SHALL replicate the DG7 of the eMRTD.|
| ``dg8`` |This field SHALL replicate the DG8 of the eMRTD.|
| ``dg9`` |This field SHALL replicate the DG9 of the eMRTD.|
| ``dg10`` |This field SHALL replicate the DG10 of the eMRTD.|
| ``dg11`` |This field SHALL replicate the DG11 of the eMRTD.|
| ``dg12`` |This field SHALL replicate the DG12 of the eMRTD.|
| ``dg13`` |This field SHALL replicate the DG13 of the eMRTD.|
| ``dg15`` |This field SHALL replicate the DG15 of the eMRTD.|
| ``dg16`` |This field SHALL replicate the DG16 of the eMRTD.|
| **Mandatory Metadata**||
| ``issue_date`` |This field SHALL contain the date of issuance of the DTC.<br><br>This field is assigned by the issuing authority at DTC issuance.|
| ``expiry_date`` |This field SHALL contain the date of expiry of the DTC.<br><br>This field is assigned by the issuing authority at DTC issuance.|
| ``issuing_authority`` |If the eMRTD contains a DG11, this field SHALL contain the issuing authority present in the DE “Issuing Authority” (if this DE is present).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority .|
| ``version`` |This field SHALL be set to 1.0|
| ``sod`` |This field SHALL replicate the SOD of the eMRTD.|
| **Optional Metadata**||
| ``issuing_subdivision`` |If the eMRTD contains a DG11, this field SHALL contain the issuing subdivision present in the DE “Issuing Authority” (if this DE is present and if it contains also the issuing subdivision).<br><br>Otherwise, this field SHALL be provided by the DTC issuing authority.|
| ``administrative_number`` |This field SHALL be assigned by the issuing authority at DTC issuance.|
| ``travel_document_type`` |This field SHALL contain the DE “Document code” as found in DG1 of the eMRTD.|
| ``travel_document_number`` |This field SHALL contain the DE “Document number” as found in DG1 of the eMRTD.|
| ``travel_document_mrz`` |This field SHALL contain the DG1 of the eMRTD.|

## 9 References

| **Item Reference** | **Standard name/details**|
| -----              | ----- |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO/IEC 18013-5.2] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, second edition, 2026-xx (Status DIS, voting terminates on 2026-03-26) |
| [ISO/IEC 23220-4] | ISO/IEC TS 23220-4: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 4: Protocols and services for the operational phase, First edition, 2026-04  |
| [ISO/IEC 23220-2.2] | ISO/IEC TS 23220-2: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 2: Data objects and encoding rules for generic eID systems, Second edition, 2026-04  |
 | [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
 | [ICAO-DTC-VC-TR] | ICAO Technical Report, Digital Travel Credentials (DTC) - Virtual Component Data Structure and PKI Mechanisms, Version 1.2, October 2020 |
 | [ICAO-DTC-PC-TR] | ICAO Technical Report, Digital Travel Credentials (DTC) - Physical Component and Protocols, Version 1.1, October 2022 |
 | [APTITUDE-D3.1] | APTITUDE, D3.1: Stock‑Taking, Analysis and Specifications — pilot use cases and advance submission, 27‑02‑2026. |
 | [APTITUDE-D3.2] | APTITUDE, D3.2: Work in progress on Technical and functional specifications for DTC experimentations. |
 | [EU-API-2025-12] | Regulation (EU) 2025/12 of the European Parliament and of the Council of 19 December 2024 on the collection and transfer of  advance passenger information for enhancing and facilitating external border checks, amending Regulations (EU) 2018/1726 and (EU) 2019/817, and repealing Council Directive 2004/82/EC. |
