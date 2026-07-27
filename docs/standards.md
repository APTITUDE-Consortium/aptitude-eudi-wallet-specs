# Relevant Standards

> **Note:** Tables on this page are designed to display at full browser width. On smaller screens, use horizontal scrolling to view all columns.

This page is APTITUDE's register of the standards and technical specifications
the pilot relies on. It is not a survey of everything published in the EUDI
Wallet domain: it records which standards APTITUDE commits to, at which version,
and on what basis.

## Column definitions

The table below uses the classification scheme introduced by the European
Commission's standards tracking work. Columns are defined as follows.

**Deliverable** — The standard or technical specification reference number,
hyperlinked to the published document. Where the issuing organisation does not
assign a reference number, the link is carried on the *Title* instead. Where no
public document is yet available, the entry is not hyperlinked.

**Title** — The full title as published by the issuing organisation.

**Organisation** — The body responsible for the deliverable (ETSI, CEN, ISO,
OpenID Foundation, W3C, IETF).

**Type** — The deliverable class used by the issuing organisation. For ETSI:
EN (European Standard), TS (Technical Specification), TR (Technical Report).

**Version** — The version of the deliverable to which the entry refers. Where
the same deliverable appears more than once, each row refers to a distinct
version.

**Status** — Publication state of that version: Published, Under publication,
or Draft.

**Considered in STS Roadmap?** — Whether the deliverable appears in the European
Commission's Standards and Technical Specifications roadmap for the EUDI Wallet
ecosystem. See the
[EC standards tracking board](https://github.com/orgs/eu-digital-identity-wallet/projects/29/views/4).

**Further refined by IA?** — Whether an Implementing Act or Commission
Implementing Decision constrains the use of the deliverable, for instance by
designating a specific version. Where applicable, the instrument is cited.

**Relevance** — Free-text note on why the deliverable matters in this context,
or on limitations affecting its use.

**Scope** — The aspects of the ecosystem to which the deliverable applies. A
deliverable may carry several values; they are listed comma-separated. An em
dash (—) indicates that the deliverable has not yet been classified, not that no
aspect applies. Permitted values are:

| Value | Meaning |
|:---|:---|
| `issuance-process` | The deliverable is relevant to the generation and provisioning of credentials. It does not cover mechanisms that establish trust in the credential, such as trusted lists; those are classified as `trust-model`. |
| `issuance-protocol` | The deliverable defines or constrains the protocol exchange through which a credential is issued to a Wallet Unit, as distinct from the surrounding issuance process. |
| `presentation-protocol` | The deliverable is relevant to the presentation of credentials and to the associated security mechanisms involving the credential holder. It covers only the interaction between the holder and the Relying Party. Mechanisms for ascertaining trust in the presented credential are classified as `validation`. |
| `format` | The deliverable defines the encoding or format of credentials. |
| `trust-model` | The deliverable is relevant to establishing and verifying trust in (1) credentials and (2) the surrounding stakeholders. Such deliverables may also bear on the credential lifecycle and on the lifecycle of those stakeholders — for example, revocation of a Wallet Unit or of a Relying Party's access rights. Where this value applies, the lifecycle-specific values are not also assigned. |
| `validation` | The deliverable enables a Relying Party receiving a credential to verify its validity status. This covers both (1) the actions the Relying Party carries out to perform that verification and (2) the input data it relies on to do so. |
| `other` | The deliverable has an applicability not captured by the values above. The aspect concerned is stated in *Relevance*. |

A value followed by a question mark (for example `issuance-protocol?`) indicates
an applicability that has been proposed but not yet confirmed.

**Roles to which it is applicable** — The ecosystem roles the deliverable
applies to: Wallet Provider, Credential Issuer, Relying Party, or Other. A
deliverable may apply to several roles.

## Identification of standards&TS

<div class="standards-table" markdown>

|Deliverable|Title|Organisation|Type|Version|Status|Considered in STS Roadmap?|Further refined by IA?|Relevance|Scope|Roles to which it is applicable|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|[TS 119 312](https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.05.01_60/ts_119312v010501p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Cryptographic Suites|ETSI|TS|1.5.1|Published|Yes|||—||
|[TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Lists of trusted entities; Data model|ETSI|TS|1.1.1|Published|Yes||Trusted list|trust-model||
|TS 119 605|Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Procedures for using and interpreting trusted lists; Processing trusted lists and trusted list content|ETSI|TS||Draft|Yes||Trusted list|trust-model||
|[TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists|ETSI|TS|2.4.1|Published|No|COMMISSION IMPLEMENTING DECISION (EU) 2025/2164 of 27 October 2025 amending Implementing Decision (EU) 2015/1505 as regards the version of the standard on which the common template for the trusted lists is based ([OJ link](https://eur-lex.europa.eu/eli/dec_impl/2025/2164/oj/eng))|Trusted list|trust-model||
|[TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/01.02.01_60/ts_119612v010201p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists|ETSI|TS|1.2.1|Published|No|This version is not considered by COMMISSION IMPLEMENTING DECISION (EU) 2025/2164 of 27 October 2025 amending Implementing Decision (EU) 2015/1505 as regards the version of the standard on which the common template for the trusted lists is based ([OJ link](https://eur-lex.europa.eu/eli/dec_impl/2025/2164/oj/eng))|Trusted list (this version is obsolete)|trust-model||
|[TS 119 615](https://www.etsi.org/deliver/etsi_ts/119600_119699/119615/01.03.01_60/ts_119615v010301p.pdf)|Electronic Signatures and Infrastructures (ESI); Trusted lists; Procedures for using and interpreting European Union Member States national trusted lists|ETSI|TS|1.3.1|Published|No||Trusted list|trust-model||
|[EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.05.01_60/en_31941101v010501p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements|ETSI|EN|1.5.1|Published|No|||trust-model||
|[TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties|ETSI|TS|1.1.1|Published|No|||trust-model||
|[TS 119 461](https://www.etsi.org/deliver/etsi_ts/119400_119499/119461/02.01.01_60/ts_119461v020101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for trust service components providing identity proofing of trust service subjects|ETSI|TS|2.1.1|Published|No|||issuance-process, issuance-protocol?||
|[TS 119 475](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Relying party attributes supporting EUDI Wallet user's authorization decisions|ETSI|TS|1.1.1|Published|No|||trust-model||
|[TR 119 476](https://www.etsi.org/deliver/etsi_tr/119400_119499/119476/01.02.01_60/tr_119476v010201p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Analysis of selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes|ETSI|TR|1.2.1|Published|No||Useful where ZKP are considered|presentation-protocol, format||
|[TR 119 476-1](https://www.etsi.org/deliver/etsi_tr/119400_119499/11947601/01.03.01_60/tr_11947601v010301p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes; Part 1: Feasibility study|ETSI|TR|1.3.1|Published|No||Useful where ZKP are considered|presentation-protocol, format||
|[TS 119 476-3](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/issues/500)|Electronic Signatures and Trust Infrastructures (ESI); Selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes; Part 3: EUDI Wallet Unit Attestation (WUA) and Wallet Instance Attestation (WIA)|ETSI|TS||Draft|Yes||Y|issuance-process, issuance-protocol, trust-model|Wallet Provider, Issuer|
|[EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 1: Overview and common data structures|ETSI|EN|1.6.1|Published|No|||trust-model||
|[EN 319 412-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons|ETSI|EN|2.4.1|Published|No|||trust-model||
|[EN 319 412-3](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf)|Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons|ETSI|EN|1.3.1|Published|No|||trust-model||
|[TS 119 412-6](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers|ETSI|TS|1.1.1|Published|No|||trust-model||
|TS 119 412-6|Electronic Signatures and Trust Infrastructures (ESI); Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers|ETSI|TS|1.1.3|Draft|No|||trust-model||
|[TS 119 431-1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11943101/01.03.01_60/ts_11943101v010301p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for trust service providers; Part 1: TSP services operating a remote QSCD / SCDev|ETSI|TS|1.3.1|Published|No||Applicable for electronic signature|—||
|[TS 119 431-2](https://www.etsi.org/deliver/etsi_ts/119400_119499/11943102/01.02.01_60/ts_11943102v010201p.pdf)|Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers; Part 2: TSP service components supporting AdES digital signature creation|ETSI|TS|1.2.1|Published|No||Applicable for electronic signature|—||
|[TS 119 432](https://www.etsi.org/deliver/etsi_ts/119400_119499/119432/01.02.01_60/ts_119432v010201p.pdf)|Electronic Signatures and Infrastructures (ESI); Protocols for remote digital signature creation|ETSI|TS|1.2.1|Published|No||Applicable for electronic signature|—||
|[EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures|ETSI|EN|1.3.1|Published|No||Applicable for electronic signature|—||
|[TS 119 182-1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures|ETSI|TS|1.2.1|Published|No||Applicable for electronic signature|—||
|[EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf)|Electronic Signatures and Infrastructures (ESI); CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures|ETSI|EN|1.3.1|Published|No||Applicable for electronic signature|—||
|[EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf)|Electronic Signatures and Infrastructures (ESI); Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers|ETSI|EN|1.1.1|Published|Yes||Applicable for electronic signature|—||
|[EN 319 142-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf)|Electronic Signatures and Infrastructures (ESI); PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures|ETSI|EN|1.2.1|Published|No||Applicable for electronic signature|—||
|[EN 319 142-2](https://www.etsi.org/deliver/etsi_en/319100_319199/31914202/01.02.01_60/en_31914202v010201p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); PAdES digital signatures; Part 2: Additional PAdES signatures profiles|ETSI|EN|1.2.1|Published|No||Applicable for electronic signature|—||
|[TS 119 472-1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.01.01_60/ts_11947201v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 1: General requirements|ETSI|TS|1.1.1|Published|Yes||Applicable for all credential formats supported in the wallet|issuance-process, issuance-protocol, format, trust-model, validation|Issuer, Wallet, RP|
|[TS 119 472-2](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party|ETSI|TS|1.1.1|Published|Yes||Applicable for the credential presentation process into the wallet|presentation-protocol|RP, Wallet|
|[TS 119 472-3](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf)|Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestation of Attributes; Part 3: Profiles for issuance of EAA or PID|ETSI|TS|1.1.1|Published|Yes||Applicable for the credential issuance process into the wallet|issuance-process, issuance-protocol|Issuer, Wallet|
|TS 18098|Guidelines for the onboarding of user personal identification data within European Digital Identity Wallets|CEN|TS||Under publication|Yes|||issuance-process, issuance-protocol||
|TS 18297|EUDI Wallet Held Attributes Access Control, operation and management|CEN|TS||Draft|Yes|||—||
|[OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)|OpenID for Verifiable Credential Issuance 1.0|OpenID||1.0|Published|Yes|||issuance-process, issuance-protocol, format, trust-model||
|[OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)|OpenID for Verifiable Presentations 1.0|OpenID||1.0|Published|Yes|||presentation-protocol, format, trust-model||
||[Conformance tests for OID4VC](https://openid.net/certification/conformance-testing-for-openid-for-verifiable-presentations/)|OpenID|||Published|Yes|||issuance-process, issuance-protocol, presentation-protocol, format, trust-model||
|[Oauth 2.0](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html)|OAuth 2.0 Multiple Response Type Encoding Practices|OpenID||1.0|Published|No||Response encoding|issuance-protocol, presentation-protocol||
|[HAIP](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-05.html)|OpenID4VC High Assurance Interoperability Profile 1.0 - draft 05|OpenID||24 December 2025 - v1.0|Published|Yes|||issuance-process, issuance-protocol, presentation-protocol, format, trust-model||
||[OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html)|OpenID|||Published|Yes|||—||
||[OpenID Connect Relying Party Metadata Choices 1.0 - draft 04](https://openid.net/specs/openid-connect-rp-metadata-choices-1_0.html)|OpenID||v1.0 draft04|Draft|No||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|presentation-protocol||
||[OpenID Federation 1.0 - draft 47](https://openid.net/specs/openid-federation-1_0.html)|OpenID||v1.0 draft47|Draft|No||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|trust-model||
||[OpenID Federation for Wallet Architectures 1.0 - draft 04](https://openid.github.io/federation-wallet/main.html)|OpenID||v1.0 draft04|Draft|No||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|trust-model||
||[OpenID Identity Assurance Schema Definition 1.0](https://openid.net/specs/openid-ida-verified-claims-1_0-final.html)|OpenID||1.0|Published|Yes|||—||
||[OpenID Connect for Identity Assurance Claims Registration](https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html)|OpenID||1.0|Published|Yes|||—||
|[VCDM](https://www.w3.org/TR/vc-data-model-2.0/)|Verifiable Credentials Data Model v2.0|W3C||2.0|Published|Yes|||format||
|[VCDI](https://www.w3.org/TR/vc-data-integrity/)|Verifiable Credential Data Integrity 1.0|W3C||1.0|Published|Yes||To be assessed in case ZKPs would be in scope|presentation-protocol, format, trust-model||
||[Data Integrity EdDSA Cryptosuites v1.0: Achieving Data Integrity using EdDSA with Edwards curves](https://www.w3.org/TR/vc-di-eddsa/)|W3C||15 May 2025|Published|Yes|||presentation-protocol, format, trust-model||
||[Data Integrity ECDSA Cryptosuites v1.0: Achieving Data Integrity using ECDSA with NIST-compliant curves](https://www.w3.org/TR/vc-di-ecdsa/)|W3C||15 May 2025|Published|Yes|||presentation-protocol, format, trust-model||
|[WebAuthn](https://www.w3.org/TR/webauthn-2/)|Web Authentication: An API for accessing Public Key Credentials Level 2|W3C||8 April 2021|Published|Yes||Useful when implementing<br>pseudonymisation with an external token<br>containing a public key|issuance-process, issuance-protocol, presentation-protocol||
|[Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)|Bitstring Status List v1.0|W3C||15 May 2025|Published|No||Useful for revocation/suspension|trust-model, validation, other||
|[DID](https://www.w3.org/TR/did-1.1/)|Decentralized Identifiers (DIDs) v1.1|W3C||24 January 2026|Published|No|||presentation-protocol, format, trust-model||
|[JSON-LD](https://www.w3.org/TR/json-ld11)|JSON-LD 1.1|W3C||16 July 2020|Published|No|||format||
|[DC API](https://www.w3.org/TR/digital-credentials/)|Digital Credentials API|W3C||29 January 2026|Draft|Yes||See HLR OIA_08|presentation-protocol||
||[Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/)|W3C||15 May 2025|Published|Yes|||presentation-protocol, format||
||[Securing Verifiable Credentials using JOSE and COSE Interoperability Report](https://w3c.github.io/vc-jose-cose-test-suite/)|W3C||23 November 2025|Published|Yes|||presentation-protocol, format||
||[Data Integrity BBS Cryptosuites v1.0: Achieving Unlinkable Data Integrity with Pairing-based Cryptography](https://www.w3.org/TR/vc-di-bbs/)|W3C||3 April 2025|Draft|Yes|||presentation-protocol, format, trust-model, validation||
||[Subresource Integrity](https://www.w3.org/TR/sri/)|W3C||10 July 2025|Draft|Yes|||—||
|[FIDO CTAP](https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html)|Client to Authenticator Protocol (CTAP)|FIDO||v2.2 July 14, 2025|Published|Yes||Useful when implementing<br>pseudonymisation with an external token<br>containing a public key|issuance-process, issuance-protocol, presentation-protocol||
|[FIDO CXP](https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html)|FIDO Credential Exchange Format (CXF)|FIDO||August 14, 2025|Published|Yes|||—||
|[FIDO CEP](https://fidoalliance.org/specs/cx/cxp-v1.0-wd-20241003.html)|Credential Exchange Protocol|FIDO||October 03, 2024|Draft|Yes|||—||
|[RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280)|RFC 5280 - Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile|IETF|RFC||Published|Yes|||trust-model, validation, other||
|[RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)|RFC 6749 - The OAuth 2.0 Authorization Framework|IETF|RFC||Published|No|||issuance-protocol, presentation-protocol||
|[RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960)|RFC 6960 - X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP|IETF|RFC||Published|No|||trust-model, validation, other||
|[RFC 7515](https://www.rfc-editor.org/rfc/rfc7515)|RFC 7515 - JSON Web Signature (JWS)|IETF|RFC||Published|Yes|||—||
|[RFC 7516](https://datatracker.ietf.org/doc/rfc7516/)|RFC 7516 - JSON Web Encryption (JWE)|IETF|RFC||Published|Yes|||—||
|[RFC 7518](https://datatracker.ietf.org/doc/rfc7518/)|RFC 7518 - JSON Web Algorithms (JWA)|IETF|RFC||Published|Yes|||—||
|[RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)|RFC 7519 - JSON Web Token (JWT)|IETF|RFC||Published|Yes|||format||
|[RFC 8152](https://datatracker.ietf.org/doc/html/rfc8152)|RFC 8152 - CBOR Object Signing and Encryption (COSE)|IETF|RFC||Published|No|||format||
|[RFC 8259](https://datatracker.ietf.org/doc/rfc8259/)|RFC 8259 - The JavaScript Object Notation (JSON) Data Interchange Format|IETF|RFC||Published|Yes|||—||
|[RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392)|RFC 8392 - CBOR Web Token (CWT)|IETF|RFC||Published|Yes|||—||
|[RFC 8610](https://www.rfc-editor.org/rfc/rfc8610.html)|RFC 8610 - Concise Data Definition Language (CDDL)|IETF|RFC||Published|Yes|||—||
|[RFC 8943](https://www.rfc-editor.org/rfc/rfc8943)|RFC 8943 - Concise Binary Object Representation (CBOR) Tags for Date|IETF|RFC||Published|Yes|||—||
|[RFC 8949](https://datatracker.ietf.org/doc/html/rfc8949)|RFC 8949 - Concise Binary Object Representation (CBOR)|IETF|RFC||Published|Yes|||format||
|[RFC 9052](https://www.rfc-editor.org/rfc/rfc9052)|RFC 9052 - CBOR Object Signing and Encryption (COSE): Structures and Process|IETF|RFC||Published|Yes|||—||
|[RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)|RFC 9162 - Certificate Transparency Version 2.0|IETF|RFC||Published|Yes|||trust-model||
|[RFC 9562](https://www.ietf.org/rfc/rfc9562.pdf)|RFC 9562 - Universally Unique IDentifiers (UUIDs)|IETF|RFC||Published|Yes|||—||
|[RFC 9682](https://www.rfc-editor.org/rfc/rfc9682.pdf)|RFC 9682 - Updates to the Concise Data Definition Language (CDDL) Grammar|IETF|RFC||Published|Yes|||—||
|[RFC 9901](https://datatracker.ietf.org/doc/rfc9901)|RFC 9901 - Selective Disclosure for JSON Web Tokens|IETF|RFC||Published|Yes|||format||
|[SD-JWT-VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)|SD-JWT-based Verifiable Credentials (SD-JWT VC)|IETF|RFC|draft-ietf-oauth-sd-jwt-vc-13|Draft|Yes||Credential format supporting selective disclosure|format||
|[Client authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/)|OAuth 2.0 Attestation-Based Client Authentication|IETF|RFC|draft-ietf-oauth-attestation-based-client-auth-07|Draft|Yes||Client authentication|presentation-protocol||
|[Token Status List](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/)|Token Status List (TSL)|IETF|RFC|draft-ietf-oauth-status-list-17|Draft|Yes||Useful for revocation/suspension|validation, other||
|18013-5|Personal identification — ISO-compliant driving licence Part 5: Mobile driving licence (mDL) application|ISO/IEC|IS|2021|Published|Yes||mdoc concept<br>Proximity use case|presentation-protocol, format, trust-model, validation||
|18013-5|Personal identification — ISO-compliant driving licence Part 5: Mobile driving licence (mDL) application|ISO/IEC|IS|Ed2|Draft (DIS)|Yes||mdoc concept<br>Proximity use case|presentation-protocol, format, trust-model, validation||
|18013-7|Personal identification — ISO-compliant driving licence Part 7: Mobile driving licence (mDL) add-on functions|ISO/IEC|TS|2025|Published|Yes||mdoc concept<br>Online use case|presentation-protocol, format, trust-model, validation||
|18013-7|Personal identification — ISO-compliant driving licence Part 7: Mobile driving licence (mDL) add-on functions|ISO/IEC|TS|Ed2|Draft (DTS)|Yes?||mdoc concept<br>Online use case|presentation-protocol, format, trust-model, validation||
|23220-1|Cards and security devices for personal identification — Building blocks for identity management via mobile devices Part 1: Generic system architectures of mobile eID systems|ISO/IEC|TS|2023|Published|No|||issuance-process, issuance-protocol, presentation-protocol, other||
|23220-2|Cards and security devices for personal identification — Building blocks for identity management via mobile devices Part 2: Data objects and encoding rules for generic eID systems|ISO/IEC|TS|2024|Published|Yes|||format||
|23220-3|Cards and security devices for personal identification — Building blocks for identity management via mobile devices Part 3: Protocols and services for installation and issuing phase|ISO/IEC|TS||Draft (DTS)|Yes|||issuance-protocol||
|23220-4|Cards and security devices for personal identification — Building blocks for identity management via mobile devices Part 4: Protocols and services for operational phase|ISO/IEC|TS||Draft (DTS)|Yes|||presentation-protocol, format, validation||
|23220-5|Cards and security devices for personal identification - Building blocks for identity management via mobile devices; Part 5: Trust models and confidence level assessment|ISO/IEC|TS||Draft|Yes|||trust-model||
|23220-7|Cards and security devices for personal identification — Building blocks for identity management via mobile devices, Part 7: Registration Authority Procedures for Mobile Document|ISO/IEC|||Draft|Yes|||format||
|7367-2|Personal identification — mdoc schemas Part 2: Mobile vehicle certificate|ISO/IEC|TS||Draft (DTS)|Yes|||format||
|23635|Blockchain and distributed ledger technologies — Guidelines for governance|ISO/IEC|TS|2022|Published|Yes||DLT/Blockchain trust model is not considered for the moment for APTITUDE|—||
|23257|Blockchain and distributed ledger technologies — Reference architecture|ISO/IEC|IS|2022|Published|Yes||DLT/Blockchain trust model is not considered for the moment for APTITUDE|—||
|15000-3|Electronic business eXtensible Markup Language (ebXML) Part 3: Registry and repository|ISO|IS|2023|Published|Yes|||—||
|[CSC API](https://cloudsignatureconsortium.org/resources/csc-api-v2-2/)|CSC API version 2.2.0.0 - Architectures and protocols for remote signature applications|CSC||2.2.0.0|Published|Yes||Applicable for electronic signature|—||
|[CSC Data model](https://cloudsignatureconsortium.org/wp-content/uploads/2025/10/csc-dm.pdf)|CSC API Data Model for remote signature applications, V 1.0.0 ([additional](https://cloudsignatureconsortium.org/resources/download-api-specifications/))|CSC||1.0.0|Published|Yes||Applicable for electronic signature|—||
|[CSC Data model bindings](https://cloudsignatureconsortium.org/wp-content/uploads/2025/10/data-model-bindings.pdf)|CSC Data Model Bindings – version 1.0.0 ([additional](https://cloudsignatureconsortium.org/resources/download-api-specifications/))|CSC||1.0.0|Published|Yes||Applicable for electronic signature|—||

</div>

> **Note:** For the complete table of standards and specifications, refer to the [relevant-standards.md](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-rfcs/blob/main/doc/relevant-standards.md) file in the repository documentation folder.
