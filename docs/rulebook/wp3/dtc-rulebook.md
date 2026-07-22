# Attestation Rulebook for attestations of type  *APTITUDE DTC*

Author(s):

* Matthias Schwan, bdr, Germany
* Corrado Guidobaldi , IPZS, Italy
* Zahra Ebadi Ansaroudi, FBK, Italy
* Anthony Carmoy, ANTS, France
* Antonio Maio , INCM, Portugal
  
| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |
| 0.2 | 27-05-2026 | Updated based on design assumptions from D3.1  |
| 0.3 | 29-05-2026 | addition of schema and mapping |
| 0.4 | 12-06-2026 | synchronization with PhotoID specification in [ISO/IEC 23220-4] |
| 0.5 | 01-07-2026 | align clause 2 and 3 with rulebook template, biblopgraphy added, trust model and revocation added |
| 0.6 | 08-07-2026 | use cases added in clause 4, editorial changes |

Feedback:

* <matthias.schwan@bdr.de>
* <c.guidobaldi@ipzs.it>
* <zebadiansaroudi@fbk.eu>
* <anthony.carmoy@interieur.gouv.fr>
* <antonio.maio@incm.pt>

## 1 Introduction

### 1.1 Document scope and purpose

This Attestation Rulebook defines the Digital Travel Credential (DTC) as an electronic attestation of attributes for the EUDI Wallet ecosystem. The DTC enables travellers to store and present identity data in their Wallet Unit for border control and travel-related use cases.

The primary objective of the DTC is to facilitate secure and privacy-preserving identity verification and travel document validation at border crossing points and during travel. The DTC is designed to complement existing physical travel documents (e.g. passports, visas) by providing a digital equivalent that supports selective disclosure, offline and online presentation and strong cryptographic verification.

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

This section defines the functional and semantic scope of the data composing the APTITUDE Digital Travel Credential (DTC), based on the evidence collected during the stock‑taking phase. The cross‑border value of a DTC critically depends on preserving full alignment with the ICAO data model while at the same time allowing extensions required for integration within the EUDI Wallet ecosystem and the eIDAS 2.0 framework. Minimization of impact on existing border‑control infrastructure would be valuable for DTC deployment. As a result, the ICAO LDS data model (DG1, DG2, DG14, SOD) constitutes the mandatory baseline.

The objective is to preserve a single interoperable DTC representation that is:

* aligned with ICAO DTC Type 2 and eMRTD LDS semantics,
* compatible with EUDI Wallet proximity presentation,
* suitable for both on-site border-control use cases and remote wallet-driven presentations,
* capable of preserving the cryptographic binding between the virtual credential and the Wallet Secure Component (WSCD).

#### Table 1 — Requirements on data model

| Index | Requirement specification |
| --- | --- |
| DTC_AE_01 | APTITUDE DTC SHALL use ISO/IEC 23220-4 PhotoID as the sole credential format. |
| DTC_AE_02 | APTITUDE DTC SHALL use ISO/IEC 18013-5 mdoc-cbor encoding for the PhotoID credential. |
| DTC_AE_03 | APTITUDE DTC SHALL support NFC engagement for proximity presentation and BLE data retrieval for Android and iOS. |
| DTC_AE_04 | APTITUDE DTC SHALL preserve ICAO LDS semantics, including e.g. EF.DG1, EF.DG2, DG14, EF.SOD, and the PhotoID profile. |
| DTC_AE_05 | APTITUDE DTC SHALL adopt open, standard-based encoding to maximize interoperability and avoid vendor lock-in. |
| DTC_AE_06 | APTITUDE DTC SHALL support a trust architecture that enables verification via ICAO CSCA/DS and EUDI Wallet / eIDAS trust anchors. |
| DTC_AE_07 | APTITUDE DTC SHALL preserve the cryptographic binding between the virtual credential and the Wallet Secure Component across issuance, storage, presentation, and verification. |
| DTC_AE_08 | APTITUDE DTC SHALL support selective disclosure and minimisation as a layer on top of the single PhotoID credential format, not by introducing a second credential format. |

#### Table 2 — Requirements on issuing

| Index | Requirement specification |
| --- | --- |
| DTC_IS_01 | APTITUDE DTC SHALL be issued exclusively by the National Passport Issuing Authority of the Member State that issued the corresponding physical eMRTD. |
| DTC_IS_02 | APTITUDE DTC SHALL be derived both from newly issued and already issued eMRTDs, except where the national authentic sources require a restriction. |
| DTC_IS_03 | The issuance process SHALL result in an ICAO DTC Type 2 (eMRTD-PC bound), where the virtual component is cryptographically linked to the WSCD being the physical component within the EUDI Wallet. |
| DTC_IS_04 | The system SHALL support the complete lifecycle management of the DTC, including secure revocation and update mechanisms managed by the issuing authority. |

#### Table 3 — Requirements on data elements

| Index | Requirement specification |
| --- | --- |
| DTC_DM_01 | The APTITUDE DTC SHALL contain DG1, DG2, DG14, SOD  as from the physical eMRTD passport and MAY contain other data groups allowed by ICAO DTC-VC specifications, as long as they are also present in the corresponding physical eMRTD |
| DTC_DM_02 | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| DTC_DM_03 | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |

### 2.2 Mandatory attributes

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``family_name`` | according to [ISO/IEC 23220-2.2] | Hardt |
| ``given_name`` | according to [ISO/IEC 23220-2.2] | Giovanni |
| ``birth_date`` | according to [ISO/IEC 23220-2.2] | 01-01-1980 |
| ``portrait`` | according to [ISO/IEC 23220-2.2] | ... |
| ``age_over_18`` | according to [ISO/IEC 23220-2.2] | T  |
| ``document_number`` | according to [ISO/IEC 23220-2.2] | YA1234567 |
| ``person_id`` | according to [ISO/IEC 23220-4] | 1234567890 |
| ``dg1`` | according to [ISO/IEC 23220-4] | P<ITA<<HARDT<<GIOVANNI<<<<<<<<<<<<<<<< |
| ``dg2`` | according to [ISO/IEC 23220-4] | ... |
| ``dg14`` | according to [ISO/IEC 23220-4] | ... |

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
| ``dg15`` | according to [ISO/IEC 23220-4] | ... |
| ``dg16`` | according to [ISO/IEC 23220-4] | ... |

### 2.4 Mandatory metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
| ``issue_date`` | according to [ISO/IEC 23220-2.2] | 20-04-2023 |
| ``expiry_date`` | according to [ISO/IEC 23220-2.2] | 20-04-2033 |
| ``issuing_authority`` | according to [ISO/IEC 23220-2.2] | Ministero dell'Interno |
| ``version`` | according to [ISO/IEC 23220-4] | 1.0 |
| ``sod`` | Security object data of related eMRTD according to [ISO/IEC 23220-4] | ... |

### 2.5 Optional metadata

| **Identifier** | **Description** | **Example** |
| --- | --- | --- |
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
| ``dg14`` | no further information<br><br> *Note:* DG14 is mandatory in EU eMRTDs | M |
| ``dg15`` | no further information<br><br> *Condition:* mandatory if available in eMRTD | C |
| ``dg16`` | ``dg16`` | O |
| ``sod`` | ``sod`` | M |

#### 3.1.5 Additonal document encryption

If a Relying Party requires document encryption in addition to the session encrption layer, it SHALL encode the document request according to [ISO/IEC 18013-5.2]. The EUDI-Wallet SHALL encrypt the requested data elements acording to [ISO/IEC 18013-5.2].  

## 4 Attestation Usage

This section briefly describes how attestions of type *APTITUDE DTC* are intended to be used. All requested attributes are examples and the request may include other data elemenst as given in the use cases.

### 4.1 Airline-mediated remote pre‑clearance (airline registers passenger with Border Control)

**Context:** Passenger who booked an international flight checks in remotely (app or website) and the airline must register the passenger with the Member State Border Authority for pre‑clearance (advance checks / pre‑assessment), see [APTITUDE-D3.1].

[//]: # (See D3.1: Stock‑Taking, Analysis and Specifications — pilot use cases and advance submission, 27‑02‑2026.)

**Flow:** remote (airline backend → Border Authority submission endpoint / Traveller Router).

[//]: # (D3.1 documents airline‑mediated pre‑assessment patterns but does not mandate a single transport/envelope.)

**Requested attributes:**

APTITUDE DTC:

* General PhotoID data elements: ``family_name``, ``given_name``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``
* Special PhotoID data elements: ``travel_document_mrz``
* ICAO PhotoID data elements: ``dg1``, ``dg2``, ``dg14``, ``sod``

[//]: # (These are the rulebook §2 mandatory/priority attributes; D3.1 does not define a stricter per‑scenario list.)

**Post‑processing:** the airline backend (or its designated submission service) MUST verify holder proof/possession assertions from the wallet (if applicable), validate the DTC signature and certificate chain and check revocation/status using the applicable trust anchors (CSCA/DS and/or EU trust lists). The airline then packages the verified data for server‑to‑server submission to the Border Authority (mapping of DTC elements to the receiving envelope is a Member State decision; legacy readers may require extraction/encapsulation into ICAO DTCContentInfo/ASN.1). The Border Authority performs full verification (passive authentication: SOD/DG hash checks, PKI chain, revocation/status) and ingests dg1, dg2, dg14 and sod for registration and risk checks.

[//]: # (D3.1 describes the pre‑assessment use case and the need for an interoperable transmission protocol; it does not mandate a single packaging mechanism — implementers must document the chosen transport and envelope.)

### 4.2 Traveller direct pre‑registration (traveller → Member State pre‑travel system)

**Context:** EU national uses their EUDIW or the EU Digital Travel Application to submit their DTC directly to a Member State’s pre‑travel system for advance checks within a 36‑hour window.

[//]: # (See D3.1 §§1.2 and 3.2 for traveller‑initiated advance submission.)

**Flow:** remote (wallet → Traveller Router or direct submission endpoint → Border backend). The exact presentation protocol (OpenID4VP, mdoc, Traveller Router) is not mandated in D3.1 and must be chosen by implementers.

**Requested attributes:**

APTITUDE DTC:

* General PhotoID data elements: ``family_name``, ``given_name``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``, ``age_over_18``, ``portrait``
* Special PhotoID data elements: ``travel_document_mrz``

The request may include ``age_over_18`` or ``portrait`` if required by the Member State for biometric pre‑matching.

[//]: # (These follow the rulebook §2 attribute set; D3.1 does not specify per‑scenario attribute subsets.)

**Post‑processing:** the receiving Border backend validates the wallet presentation (proof of possession), verifies the DTC signature and PKI chain and checks revocation/status. Verification outcome drives pre‑assessment workflows (EES/ETIAS/API/SIS/SLTD queries). If selective disclosure was used, the backend MUST verify integrity (for example by checking SOD/DG hashes or using a documented bridging mechanism) before accepting partial disclosures.

[//]: # (D3.1 highlights the selective‑disclosure vs LDS integrity tension but does not prescribe a single resolution, so the Member State policy must define acceptance criteria.)

### 4.3 Proximity presentation at border control (on‑site verification / e‑gate or officer kiosk)

**Context:** Traveller presents their DTC from the EUDIW at the border control point (e‑gate, kiosk or officer reader) for immediate verification and biometric match. (D3.1 describes proximity presentation requirements and the need to reconcile ISO/IEC 18013‑5 and ICAO NFC/APDU approaches.)

**Flow:** proximity (device engagement / NFC or mdoc proximity per chosen implementation). D3.1 notes both ISO/IEC 18013‑5 (EUDIW proximity) and ISO/IEC 14443/APDU (ICAO backwards compatibility) and does not mandate one universal mode — the pilot must specify which mode(s) will be tested.

**Modalities (as defined in D3.2 Chapter 10.3 Functional Flow):** 

1. Proximity presentation of the DTC‑VC and 1:1 matching: The user presents its DTC-VC from the EUDI Wallet, with device engagement, allowing gates to retrieve the DTC-VC from the wallet with biometric verification in 1:1 between the passenger and the photo contained in his DTC-VC.

2. Proximity presentation of a token and 1:1 matching: The user presents a token, containing a decryption key, allowing the gates to decrypt the pre-loaded DTC-VC for a specific flight. 1:1 biometric matching between the passenger and the photo contained in the pre-loaded DTC.

3. DTC‑VC presentation: The user presents his DTC-VC stored in his wallet (or taps his passport against the gates) which allows the gates to retrieve the DTC-VC from a gallery of DTC-VC pre-loaded on the gates. A biometric matching is then carried out in 1:1.

4. Matching 1:n then presentation of the DTC-VC: The user approaches the gates, and proceeds to a 1:n matching to retrieve the DTC-VC preloaded in the gates. He then presents his DTC-VC stored in his EUDI Wallet (or types his passport), in order to establish the cryptographic link to authenticate the passenger and his DTC.

**Requested attributes:**

APTITUDE DTC

* General PhotoID data elements: ``family_name``, ``given_name``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``age_over_18``, ``portrait``
* Special PhotoID data elements: ``person_id``
* ICAO PhotoID data elements: ``dg1``, ``dg2``, ``dg14``, ``sod``, ``version``

Priority attributes for on‑site verification and biometric matching are ``dg2`` (portrait), ``dg1`` (biographic / MRZ), ``sod``, ``dg14`` if the Member State uses it for inspection). Attributes ``version``, ``person_id``, ``expiry_date``, ``issuing_authority``, ``age_over_18`` and ``portrait`` are optional depending on the check (age verification, biometric fallback).

[//]: # (Chosen attributes reflect rulebook §2 priorities and D3.1 emphasis on DG2/SOD for biometric anchoring.)

**Post‑processing:** the proximity reader / e‑gate performs device engagement, retrieves the DTC, validates SOD / passive authentication (signature verification and PKI chain to CSCA/PKD), checks revocation/status and carries out biometric 1:1 matching of the live capture to dg2. The gate/backend then forwards verification results and any required DGs (dg1/dg2/sod and selected metadata) to backend systems for database checks (EES, SIS, SLTD) and final decision. The pilot MUST state whether translation to ASN.1 DTCContentInfo is required for legacy inspection systems; D3.1 signals this requirement as a possible necessity but does not fix the mapping responsibilities.

### 4.4 Cross‑jurisdiction proximity presentation (EU traveller arriving outside Schengen — optional)

**Context:** EU national with an EUDIW‑stored DTC presents the credential in proximity to a non‑EU local border authority to test cross‑jurisdiction interoperability.

[//]: # (D3.1 lists the outside‑Schengen arrival scenario as optional and highlights interoperability constraints.)

**Flow:** proximity (wallet → non‑EU verifier). The destination’s native inspection interface determines the mode (NFC/APDU, mdoc, or other). D3.1 notes that non‑EU systems may expect ICAO ASN.1 structures and PKI anchors.

**Requested attributes:**

APTITUDE DTC

* General PhotoID data elements: ``family_name``, ``given_name``, ``birth_date``, ``issue_date``, ``expiry_date``, ``issuing_authority``, ``document_number``, ``portrait``
* Special PhotoID data elements: ``travel_document_mrz``

[//]: # (D3.1 does not define which attributes a receiving non‑EU authority will require; this baseline reflects rulebook §2 mandatory/priority elements typically needed for equivalence to an eMRTD.)

**Post‑processing:** the non‑EU verifier validates the credential using ICAO PKI (CSCA/DS via PKD) and its local acceptance policy. If the receiving system requires ICAO ASN.1 DTCContentInfo, an intermediate gateway or the wallet/traveller router may need to extract dg1/dg2/sod and encapsulate them accordingly; D3.1 documents that such translation and trust alignment are common cross‑jurisdiction issues but does not prescribe which actor must perform the translation. If the verifier cannot validate under available trust anchors, the fallback/acceptance policy is a matter for the receiving authority.

### 4.5 Booklet-based proximity presentation to legacy eGate (“fallback”)

**Context:** Use casess 4.1 or 4.2 have succeeded such that traveler has been successfully registered. Traveler approaches legacy eGate in order to cross border, with booklet passport.

**Flow:**

Option 1: MRZ Scan (traditional)

* Scan the Machine Readable Zone (MRZ) on the travel document.
* Open the chip.
* Link the document to the pre-registration data by matching dg1 for example
* Perform biometric verification.
* Active/Chip Authentication

Option 2: Tap&go

* biometric identification.
* Link person to the pre-registration data
* open the chip with dg1 from pre-registration data
* Active/Chip Authentication

**Requested attributes:**

APTITUDE DTC (see pre-registration use cases 4.1 or 4.2)

* ICAO PhotoID data elements: ``dg1``, ``dg2``, ``dg14``, ``sod``

## 5 Trust Anchors

The APTITUDE DTC is derived from the physical eMRTD LDS data groups and signed by the national issuing authority. The issuing authority SHALL sign the issuer signed data, i.e. the MSO, using a document signer key and certificate under the respective CSCA root certificate according to clause 2.2 in [ICAO-DTC-VC-TR].

*Note:* According to [ICAO-DTC-VC-TR], the DTC signer certificate includes a dedicated OID in the extendedKeyUsage extension, i.e. ``2.23.136.1.1.12.1``.

It is recommended to make the CSCA root certificates of the EU Member States available to Relying Parties in the EUDI-Wallet ecosytem by a respective EU Trust List, i.e. APTITUDE DTC TL. In addition, it is recommended to make the content of the APTITUDE DTC TL available to Relying Parties outside of the EUDI-Wallet ecosystem by a VICAL according to [ISO/IEC 18013-5].

CSCA root certificates MAY be also obtained from the ICAO PKD by any Relying Party.

## 6 Revocation

Revocation of the APTITUDE DTC, i.e. the mdoc, SHALL be implemented according to [ISO/IEC 18013-5.2], i.e. MSO revocation information. The issuing authority SHALL provide the respective status list.

Revocation of the linked eMRTD and LDS data given in the ICAO PhotoID data elements remains unchanged.

If an APTITUDE DTC is marked revoked, a Relying Party SHALL reject all recieved data elements of the various name spaces. If parts of the data elemnts are encrypted according clause 3.1.5, the Relying Party shall also reject the encrypted data.

## 7 Compliance

If compliance to ICAO DTC-VC Type 1 is required, a reader may after succsessfull processing the device response and the verification prodecure encapsule the data in the structure given in clause 7.1. The reader SHALL use the option eMRTD bound for DTC-VC encoding. The ICAO based encoding for DTC-VC is defined in [ICAO-DTC-VC-TR] and encoding for DTC-PC is defined in [ICAO-DTC-PC-TR]. The reader SHALL use the option eMRTD bound for DTC-VC encoding.

*Note:* Option eMRTD bound does not include elemts dtcTBS, dtcSignerInfo, DTCSecurityInfo and DTCOtherInfo.  

### 7.1 ICAO based encoding

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
| -----              | ----- |
| [ISO/IEC 18013-5] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, First edition, 2021-09 |
| [ISO/IEC 18013-5.2] |  ISO/IEC 18013-5, Personal identification --- ISO-compliant driving licence - Part 5: Mobile driving licence (mDL) application, second edition, 2026-xx (Status DIS) |
| [ISO/IEC 23220-4] | ISO/IEC TS 23220-4: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 4: Protocols and services for the operational phase, First edition, 2026-04  |
| [ISO/IEC 23220-2.2] | ISO/IEC TS 23220-2: Cards and Security Devices for Personal Identification – Building Blocks for Identity Management via Mobile Devices –Part 2: Data objects and encoding rules for generic eID systems, Second edition, 2026-04  |
 | [RFC 2119] | RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997 |
 | [ICAO-DTC-VC-TR] | ICAO Technical Report, Digital Travel Credentials (DTC) - Virtual Component Data Structure and PKI Mechanisms, Version 1.2, October 2020 |
 | [ICAO-DTC-PC-TR] | ICAO Technical Report, Digital Travel Credentials (DTC) - Physical Component and Protocols, Version 1.1, October 2022 |
 | [APTITUDE-D3.1] | APTITUDE, D3.1: Stock‑Taking, Analysis and Specifications — pilot use cases and advance submission, 27‑02‑2026. |
