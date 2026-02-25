| Version | Date | Description |
|---------|------------|------------|
| 0.1 | 11-02-2026 | First draft version - Filled par 1.1 |

# APTITUDE - *Digital Travel Credential (DTC) rulebook*

* Author(s):
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

The DTC attestation type is intended for use by national authorities issuing travel documents and by border control agencies as Relying Parties.

### 1.2 Document structure
### 1.3 Key words
This document uses the capitalised keywords 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e. to indicate requirements, recommendations and options specified in this document.
### 1.4 Terminology

## 2 Attestation attributes and metadata
### Chapter overview and requirements
#### Issuance
| Index | Requirement specification |
| --- | --- |
| XX_XX | The APTITUDE DTC SHALL be issued exclusively by the National Passport Issuing Authority of the Member State that issued the physical eMRTD. |
| XX_XX | APTITUDE DTC SHALL be derived from eMRTD chip data (Logical Data Structure - LDS) ensuring a cryptographic link to the physical travel document. |
| XX_XX | APTITUDE DTC SHALL be derived both from newly issued and already issued eMRTDs. | 
| XX_XX | The issuance process SHALL result in an ICAO DTC Type 2 (eMRTD-PC bound), where the virtual component is cryptographically linked to a physical secure element within the EUDI Wallet. |
| XX_XX | APTITUDE DTC SHALL be digitally signed by the national issuing authority acting as a Trusted Attestation Provider within the eIDAS 2.0 framework. |
| XX_XX | The system SHALL support the complete lifecycle management of the DTC, including secure revocation and update mechanisms managed by the issuing authority. |

#### Data model
| Index | Requirement specification |
| --- | --- |
| XX_XX | According to ICAO’s DTC-VC data model, the APTITUDE DTC SHALL contain DG1, DG2, SOD as from the physical eMRTD passport |
| XX_XX | According to ICAO's DTC-VC data model, the APTITUDE DTC SHALL contain fields like: dtcSecurityInfo, DTCIdentifier, DTCDOE, and a signature structure for validation |
| XX_XX | The APTITUDE DTC SHALL be encapsulated as a Verifiable Credential (VC), ensuring compatibility with the EUDI Wallet data formats (e.g., SD-JWT or mDL). |
| XX_XX | For Type 2 credentials, the data model SHALL include a cryptographic binding between the Virtual Component (VC) and the Physical Component (PC) stored in the Wallet's secure element. |
| XX_XX | APTITUDE DTC MAY contain additional attributes beyond the derived eMRTD dataset |
| XX_XX | The data model SHALL support Selective Disclosure, allowing the traveller to share only the strictly necessary attributes (e.g., only DG2 for biometric match) with Relying Parties. |


## 3 Attestation encoding
### Chapter overview and requirements
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL be encoded as an eIDAS2 attestation compliant | 
| XX_XX | APTITUDE DTC SHALL encode the photoID profile as per ISO/IEC 23220‑4 Annex C | 
| XX_XX | APTITUDE DTC SHALL preserve the ICAO LDS semantics | 
| XX_XX | APTITUDE DTC SHALL support SD‑JWT VC encoding | 
| XX_XX | APTITUDE DTC SHALL ISO/IEC 18013‑5 mdoc-cbor encoding for proximity presentation and interaction with EUDI Wallet readers. | 
| XX_XX | APTITUDE DTC SHALL implement an encoding approach that addresses the incompatibility between ARF selective disclosure and ICAO LDS integrity‑bound | 
| XX_XX | APTITUDE DTC SHALL adopt open, standard-based credential encodings to maximize interoperability and avoid vendor lock-in | 
| XX_XX | The encoding SHALL support a dual-signature or hybrid structure to allow validation via both ICAO CSCA/DS (PKI) and eIDAS Trusted Lists. |
| XX_XX | The encoding SHALL ensure that the cryptographic link (binding) between the VC and the EUDI Wallet device is preserved across different encoding formats. |

## 4 Attestation usage
### Chapter overview and requirements
#### Presentation
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL support remote usage where the attestation can be transmitted in advance for identity validation and risk assessment |
| XX_XX | APTITUDE DTC SHALL support proximity presentation at border control using border authority proximity control systems (e-gates, desktop equipment, mobile devices) |
| XX_XX | APTITUDE DTC SHALL ensure explicit user consent in the wallet-based presentation flow |
| XX_XX | APTITUDE DTC SHALL support selective disclosure / data minimisation |
| XX_XX | APTITUDE DTC SHALL support an approach that accounts for the reported protocol gap between ISO/IEC 18013‑5 (wallet proximity) and ISO/IEC 14443/APDU (border inspection backwards compatibility) |

#### Verification
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL support cryptographic integrity verification |

## 5 Trust anchors
### Chapter overview and requirements
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL support an inspection system can verify it using the existing MRTD PKI infrastructure (CSCA/DS model) |
| XX_XX | APTITUDE DTC SHALL shall enforce (or be configurable to enforce) the principle that the CSCA issuing APTITUDE DTC Signer certificates is the same CSCA that issues Document Signer certificates for the underlying eMRTD |
| XX_XX | APTITUDE DTC SHALL support the same level of security as the eMRTD |
| XX_XX | APTITUDE DTC SHALL support reliance on EU-style governance artefacts needed for attestations, specifically: a trusted list of DTC issuers, an attestation catalogue, and rules for registering relying parties |
| XX_XX | APTITUDE DTC SHALL support a design that acknowledges and manages the structural divergence between ICAO trust anchors (CSCA/DS certificates / PKD) and eIDAS trust anchors (QEAA/Pub‑EAA within EUDIW) |
| XX_XX | APTITUDE DTC SHALL support a bridging approach/layer to enable interoperability when the attestation is not directly verifiable by non-EU inspection systems relying on existing PKI |
| XX_XX | APTITUDE DTC SHALL not assume a trust model where the DTC must be issued as QEAA in a way that makes the issuer a QTSP instead of the passport authority, because the report flags this as contradicting ICAO principles requiring the Travel Document Issuing Authority to sign DTC data |
| XX_XX | APTITUDE DTC SHALL support an option where the DTC is stored/handled as a Pub‑EAA to preserve issuer sovereignty |
| XX_XX | APTITUDE DTC SHALL allow the applicable attestation trust type (e.g., QEAA vs Pub‑EAA) to be policy/configuration-driven |
| XX_XX | APTITUDE DTC SHALL be able to accommodate alternative/extra signing arrangements (e.g., a possible EU model where DTCs may need to be re-signed by eu‑LISA) |

## 6 Revocation
### Chapter overview and requirements
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL support a full DTC lifecycle covering issuance, verification, and revocation |
| XX_XX | APTITUDE DTC SHALL support mechanisms for revocation and status checking |
| XX_XX | APTITUDE DTC SHALL support alignment between EUDI Wallet attestation lifecycle and ICAO DTC lifecycle requirements |

## 7 Compliance
### Chapter overview and requirements
| Index | Requirement specification |
| --- | --- |
| XX_XX | APTITUDE DTC SHALL support privacy-by-design expectations |

## 8 References
| **Item Reference** | **Standard name/details** |
| [RFC 2119] | Key words for use in RFCs |
| --- | --- |
| ... | ...|
| ... | ... |