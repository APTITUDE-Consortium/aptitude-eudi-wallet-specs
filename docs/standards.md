# Relevant Standards

> **Note:** Tables on this page are designed to display at full browser width. On smaller screens, use horizontal scrolling to view all columns.

This page is APTITUDE's register of the standards and technical specifications
the pilot relies on. It is not a survey of everything published in the EUDI
Wallet domain: it records which standards APTITUDE commits to, at which version,
and on what basis.

## Column definitions

The table below uses the classification scheme introduced by the European
Commission's standards tracking work. Columns are defined as follows.

**Deliverable** — The issuing body followed by the standard or technical
specification reference number (e.g. *ETSI TS 119 612*, *ISO/IEC 18013-5*,
*IETF RFC 5280*), hyperlinked to the published document. Where the body does not
assign a reference number, the body name alone is shown here and the link is
carried on the *Title* instead. Where no public document is yet available, the
entry is not hyperlinked.

**Title** — The full title as published by the issuing organisation.

**Version** — The version of the deliverable to which the entry refers. Where
the same deliverable appears more than once, each row refers to a distinct
version.

**Status** — Publication state of that version: Published, Under publication,
or Draft.

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

Note: Titles are shortened and  omit the shared series prefix carried by every entry from the same body (e.g. the ETSI "…(ESI);" lead-in, and the ISO/IEC 18013 and 23220 family headers). Only the distinctive part is shown; the full official title is at the linked source in *Deliverable*.

Note: Titles are shortened and  omit the shared series prefix carried by every entry from the same body (e.g. the ETSI "…(ESI);" lead-in, and the ISO/IEC 18013 and 23220 family headers). Only the distinctive part is shown; the full official title is at the linked source in *Deliverable*.

<div class="standards-table" markdown>

|Deliverable|Title|Version|Status|Further refined by IA?|Relevance|Scope|Roles to which it is applicable|
|:---|:---|:---|:---|:---|:---|:---|:---|
|[ETSI TS 119 312](https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.05.01_60/ts_119312v010501p.pdf)| Cryptographic Suites|1.5.1|Published|||—||
|[ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)| Lists of trusted entities; Data model|1.1.1|Published||Trusted list|trust-model||
|ETSI TS 119 605| Trusted lists; Procedures for using and interpreting trusted lists; Processing trusted lists and trusted list content||Draft||Trusted list|trust-model||
|[ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)| Trusted Lists|2.4.1|Published|Mandated by CID (EU) 2025/2164 ([OJ link](https://eur-lex.europa.eu/eli/dec_impl/2025/2164/oj/eng))|Trusted list|trust-model||
|[ETSI TS 119 615](https://www.etsi.org/deliver/etsi_ts/119600_119699/119615/01.03.01_60/ts_119615v010301p.pdf)|Trusted lists; Procedures for using and interpreting European Union Member States national trusted lists|1.3.1|Published||Trusted list|trust-model||
|[ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.05.01_60/en_31941101v010501p.pdf)| Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements|1.5.1|Published|||trust-model||
|[ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf)| Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties|1.1.1|Published|||trust-model||
|[ETSI TS 119 461](https://www.etsi.org/deliver/etsi_ts/119400_119499/119461/02.01.01_60/ts_119461v020101p.pdf)| Policy and security requirements for trust service components providing identity proofing of trust service subjects|2.1.1|Published|||issuance-process, issuance-protocol?||
|[ETSI TS 119 475](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf)| Relying party attributes supporting EUDI Wallet user's authorization decisions|1.1.1|Published|||trust-model||
|[ETSI TR 119 476](https://www.etsi.org/deliver/etsi_tr/119400_119499/119476/01.02.01_60/tr_119476v010201p.pdf)| Analysis of selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes|1.2.1|Published||Useful where ZKP are considered|presentation-protocol, format||
|[ETSI TR 119 476-1](https://www.etsi.org/deliver/etsi_tr/119400_119499/11947601/01.03.01_60/tr_11947601v010301p.pdf)| Selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes; Part 1: Feasibility study|1.3.1|Published||Useful where ZKP are considered|presentation-protocol, format||
|[ETSI TS 119 476-3](https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/issues/500)| Selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes; Part 3: EUDI Wallet Unit Attestation (WUA) and Wallet Instance Attestation (WIA)||Draft||Y|issuance-process, issuance-protocol, trust-model|Wallet Provider, Issuer|
|[ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf)| Certificate Profiles; Part 1: Overview and common data structures|1.6.1|Published|||trust-model||
|[ETSI EN 319 412-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf)| Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons|2.4.1|Published|||trust-model||
|[ETSI EN 319 412-3](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf)|Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons|1.3.1|Published|||trust-model||
|[ETSI TS 119 412-6](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf)| Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers|1.1.1|Published|||trust-model||
|ETSI TS 119 412-6| Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers|1.1.3|Draft|||trust-model||
|[ETSI TS 119 431-1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11943101/01.03.01_60/ts_11943101v010301p.pdf)| Policy and security requirements for trust service providers; Part 1: TSP services operating a remote QSCD / SCDev|1.3.1|Published||Applicable for electronic signature|—||
|[ETSI TS 119 431-2](https://www.etsi.org/deliver/etsi_ts/119400_119499/11943102/01.02.01_60/ts_11943102v010201p.pdf)|Policy and security requirements for trust service providers; Part 2: TSP service components supporting AdES digital signature creation|1.2.1|Published||Applicable for electronic signature|—||
|[ETSI TS 119 432](https://www.etsi.org/deliver/etsi_ts/119400_119499/119432/01.02.01_60/ts_119432v010201p.pdf)|Protocols for remote digital signature creation|1.2.1|Published||Applicable for electronic signature|—||
|[ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf)| XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures|1.3.1|Published||Applicable for electronic signature|—||
|[ETSI TS 119 182-1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf)| JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures|1.2.1|Published||Applicable for electronic signature|—||
|[ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf)|CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures|1.3.1|Published||Applicable for electronic signature|—||
|[ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf)|Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers|1.1.1|Published||Applicable for electronic signature|—||
|[ETSI EN 319 142-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf)|PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures|1.2.1|Published||Applicable for electronic signature|—||
|[ETSI EN 319 142-2](https://www.etsi.org/deliver/etsi_en/319100_319199/31914202/01.02.01_60/en_31914202v010201p.pdf)| PAdES digital signatures; Part 2: Additional PAdES signatures profiles|1.2.1|Published||Applicable for electronic signature|—||
|[ETSI TS 119 472-1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.01.01_60/ts_11947201v010101p.pdf)| Profiles for Electronic Attestation of Attributes; Part 1: General requirements|1.1.1|Published||Applicable for all credential formats supported in the wallet|issuance-process, issuance-protocol, format, trust-model, validation|Issuer, Wallet, RP|
|[ETSI TS 119 472-2](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf)| Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party|1.2.1|Published||Applicable for the credential presentation process into the wallet|presentation-protocol|RP, Wallet|
|[ETSI TS 119 472-3](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf)| Profiles for Electronic Attestation of Attributes; Part 3: Profiles for issuance of EAA or PID|1.1.1|Published||Applicable for the credential issuance process into the wallet|issuance-process, issuance-protocol|Issuer, Wallet|
|CEN TS 18098|Guidelines for the onboarding of user personal identification data within European Digital Identity Wallets||Under publication|||issuance-process, issuance-protocol||
|CEN TS 18297|EUDI Wallet Held Attributes Access Control, operation and management||Draft|||—||
|[OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)|OpenID for Verifiable Credential Issuance 1.0|1.0|Published|||issuance-process, issuance-protocol, format, trust-model||
|[OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)|OpenID for Verifiable Presentations 1.0|1.0|Published|||presentation-protocol, format, trust-model||
|[DCQL](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html#name-digital-credentials-query-l)|Digital Credentials Query Language; defined within OpenID for Verifiable Presentations 1.0, clause 6|1.0|Published||Query language used by Relying Parties to request attestations|presentation-protocol, format||
|OpenID|[Conformance tests for OID4VC](https://openid.net/certification/conformance-testing-for-openid-for-verifiable-presentations/)||Published|||issuance-process, issuance-protocol, presentation-protocol, format, trust-model||
|[OpenID Oauth 2.0](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html)|OAuth 2.0 Multiple Response Type Encoding Practices|1.0|Published||Response encoding|issuance-protocol, presentation-protocol||
|[OpenID HAIP](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-05.html)|OpenID4VC High Assurance Interoperability Profile|1.0|Published|||issuance-process, issuance-protocol, presentation-protocol, format, trust-model||
|OpenID|[OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html)||Published|||—||
|OpenID|[OpenID Connect Relying Party Metadata Choices 1.0 - draft 04](https://openid.net/specs/openid-connect-rp-metadata-choices-1_0.html)|v1.0 draft04|Draft||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|presentation-protocol||
|OpenID|[OpenID Federation 1.0 - draft 47](https://openid.net/specs/openid-federation-1_0.html)|v1.0 draft47|Draft||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|trust-model||
|OpenID|[OpenID Federation for Wallet Architectures 1.0 - draft 04](https://openid.github.io/federation-wallet/main.html)|v1.0 draft04|Draft||This document defines an alternative trust model to the one underpinned by the trusted lists as defined in ETSI/TS 119 612. This alternative trust model may be relevant for some types of use cases, in particular those requiring scalability|trust-model||
|OpenID|[OpenID Identity Assurance Schema Definition 1.0](https://openid.net/specs/openid-ida-verified-claims-1_0-final.html)|1.0|Published|||—||
|OpenID|[OpenID Connect for Identity Assurance Claims Registration](https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html)|1.0|Published|||—||
|[W3C VCDM](https://www.w3.org/TR/vc-data-model-2.0/)|Verifiable Credentials Data Model v2.0|2.0|Published|||format||
|[W3C VCDI](https://www.w3.org/TR/vc-data-integrity/)|Verifiable Credential Data Integrity 1.0|1.0|Published||To be assessed in case ZKPs would be in scope|presentation-protocol, format, trust-model||
|W3C|[Data Integrity EdDSA Cryptosuites v1.0: Achieving Data Integrity using EdDSA with Edwards curves](https://www.w3.org/TR/vc-di-eddsa/)|15 May 2025|Published|||presentation-protocol, format, trust-model||
|W3C|[Data Integrity ECDSA Cryptosuites v1.0: Achieving Data Integrity using ECDSA with NIST-compliant curves](https://www.w3.org/TR/vc-di-ecdsa/)|15 May 2025|Published|||presentation-protocol, format, trust-model||
|[W3C WebAuthn](https://www.w3.org/TR/webauthn-2/)|Web Authentication: An API for accessing Public Key Credentials Level 2|8 April 2021|Published||Useful when implementing<br>pseudonymisation with an external token<br>containing a public key|issuance-process, issuance-protocol, presentation-protocol||
|[W3C Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)|Bitstring Status List v1.0|15 May 2025|Published||Useful for revocation/suspension|trust-model, validation, other||
|[W3C DID](https://www.w3.org/TR/did-1.1/)|Decentralized Identifiers (DIDs) v1.1|24 January 2026|Published|||presentation-protocol, format, trust-model||
|[W3C JSON-LD](https://www.w3.org/TR/json-ld11)|JSON-LD 1.1|16 July 2020|Published|||format||
|[W3C DC API](https://www.w3.org/TR/digital-credentials/)|Digital Credentials API|29 January 2026|Draft||See HLR OIA_08|presentation-protocol||
|W3C|[Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/)|15 May 2025|Published|||presentation-protocol, format||
|W3C|[Securing Verifiable Credentials using JOSE and COSE Interoperability Report](https://w3c.github.io/vc-jose-cose-test-suite/)|23 November 2025|Published|||presentation-protocol, format||
|W3C|[Data Integrity BBS Cryptosuites v1.0: Achieving Unlinkable Data Integrity with Pairing-based Cryptography](https://www.w3.org/TR/vc-di-bbs/)|3 April 2025|Draft|||presentation-protocol, format, trust-model, validation||
|W3C|[Subresource Integrity](https://www.w3.org/TR/sri/)|10 July 2025|Draft|||—||
|[FIDO CTAP](https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html)|Client to Authenticator Protocol (CTAP)|v2.2 July 14, 2025|Published||Useful when implementing<br>pseudonymisation with an external token<br>containing a public key|issuance-process, issuance-protocol, presentation-protocol||
|[FIDO CXP](https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html)|FIDO Credential Exchange Format (CXF)|August 14, 2025|Published|||—||
|[FIDO CEP](https://fidoalliance.org/specs/cx/cxp-v1.0-wd-20241003.html)|Credential Exchange Protocol|October 03, 2024|Draft|||—||
|[IETF RFC 1950](https://datatracker.ietf.org/doc/html/rfc1950)|ZLIB Compressed Data Format Specification version 3.3||Published||Compression of the Status List Token `lst` claim|validation, other||
|[IETF RFC 1951](https://datatracker.ietf.org/doc/html/rfc1951)|DEFLATE Compressed Data Format Specification version 1.3||Published||Compression of the Status List Token `lst` claim|validation, other||
|[IETF RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119)|Key words for use in RFCs to Indicate Requirement Levels||Published||Normative language of the APTITUDE RFC series (BCP 14, with RFC 8174)|other||
|[IETF RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)|Date and Time on the Internet: Timestamps||Published||Encoding of date and time attributes in attestations|format||
|[IETF RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280)|Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile||Published|||trust-model, validation, other||
|[IETF RFC 5755](https://datatracker.ietf.org/doc/html/rfc5755)|An Internet Attribute Certificate Profile for Authorization||Published||Underlying profile for the X509-AC EAA format identifier `x509_attr`|format||
|[IETF RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)|The OAuth 2.0 Authorization Framework||Published|||issuance-protocol, presentation-protocol||
|[IETF RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960)|X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP||Published|||trust-model, validation, other||
|[IETF RFC 7515](https://www.rfc-editor.org/rfc/rfc7515)|JSON Web Signature (JWS)||Published|||—||
|[IETF RFC 7516](https://datatracker.ietf.org/doc/rfc7516/)|JSON Web Encryption (JWE)||Published|||—||
|[IETF RFC 7518](https://datatracker.ietf.org/doc/rfc7518/)|JSON Web Algorithms (JWA)||Published|||—||
|[IETF RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)|JSON Web Token (JWT)||Published|||format||
|[IETF RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)|Proof Key for Code Exchange by OAuth Public Clients (PKCE)||Published||Required with `S256` for the Authorisation Code Flow in issuance|issuance-protocol||
|[IETF RFC 8152](https://datatracker.ietf.org/doc/html/rfc8152)|CBOR Object Signing and Encryption (COSE)||Published|||format||
|[IETF RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)|Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words||Published||Normative language of the APTITUDE RFC series (BCP 14, with RFC 2119)|other||
|[IETF RFC 8259](https://datatracker.ietf.org/doc/rfc8259/)|The JavaScript Object Notation (JSON) Data Interchange Format||Published|||—||
|[IETF RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392)|CBOR Web Token (CWT)||Published|||—||
|[IETF RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446)|The Transport Layer Security (TLS) Protocol Version 1.3||Published||Transport protection of issuance, presentation and status endpoints|issuance-protocol, presentation-protocol, validation||
|[IETF RFC 8610](https://www.rfc-editor.org/rfc/rfc8610.html)|Concise Data Definition Language (CDDL)||Published|||—||
|[IETF RFC 8943](https://www.rfc-editor.org/rfc/rfc8943)|Concise Binary Object Representation (CBOR) Tags for Date||Published|||—||
|[IETF RFC 8949](https://datatracker.ietf.org/doc/html/rfc8949)|Concise Binary Object Representation (CBOR)||Published|||format||
|[IETF RFC 9052](https://www.rfc-editor.org/rfc/rfc9052)|CBOR Object Signing and Encryption (COSE): Structures and Process||Published|||—||
|[IETF RFC 9101](https://datatracker.ietf.org/doc/html/rfc9101)|The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)||Published||Signed Request Object used in presentation requests|presentation-protocol||
|[IETF RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110)|HTTP Semantics||Published||Methods, header fields and status codes of the trust evaluation and status endpoints|validation, trust-model, other||
|[IETF RFC 9111](https://datatracker.ietf.org/doc/html/rfc9111)|HTTP Caching||Published||`Cache-Control` and `Expires` behaviour of the Register and status endpoints; obsoletes RFC 7234|validation, trust-model, other||
|[IETF RFC 9126](https://datatracker.ietf.org/doc/html/rfc9126)|OAuth 2.0 Pushed Authorization Requests (PAR)||Published||Required for the Authorisation Code Flow in issuance|issuance-protocol||
|[IETF RFC 9162](https://datatracker.ietf.org/doc/html/rfc9162)|Certificate Transparency Version 2.0||Published|||trust-model||
|[IETF RFC 9449](https://datatracker.ietf.org/doc/html/rfc9449)|OAuth 2.0 Demonstrating Proof of Possession (DPoP)||Published||Sender-constrained access tokens in issuance|issuance-protocol||
|[IETF RFC 9562](https://www.ietf.org/rfc/rfc9562.pdf)|Universally Unique IDentifiers (UUIDs)||Published|||—||
|[IETF RFC 9682](https://www.rfc-editor.org/rfc/rfc9682.pdf)|Updates to the Concise Data Definition Language (CDDL) Grammar||Published|||—||
|[IETF RFC 9901](https://datatracker.ietf.org/doc/rfc9901)|Selective Disclosure for JSON Web Tokens||Published|||format||
|[IETF SD-JWT-VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)|SD-JWT-based Verifiable Credentials (SD-JWT VC)|draft-ietf-oauth-sd-jwt-vc-13|Draft||Credential format supporting selective disclosure|format||
|[IETF Client authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/)|OAuth 2.0 Attestation-Based Client Authentication|draft-ietf-oauth-attestation-based-client-auth-07|Draft||Client authentication|presentation-protocol||
|[IETF Token Status List](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/)|Token Status List (TSL)|draft-ietf-oauth-status-list-17|Draft||Useful for revocation/suspension|validation, other||
|ISO/IEC 18013-5|Part 5: Mobile driving licence (mDL) application|2021|Published||mdoc concept<br>Proximity use case|presentation-protocol, format, trust-model, validation||
|ISO/IEC 18013-5|Part 5: Mobile driving licence (mDL) application|Ed2|Draft (DIS)||mdoc concept<br>Proximity use case|presentation-protocol, format, trust-model, validation||
|ISO/IEC 18013-7|Part 7: Mobile driving licence (mDL) add-on functions|2025|Published||mdoc concept<br>Online use case|presentation-protocol, format, trust-model, validation||
|ISO/IEC 18013-7|Part 7: Mobile driving licence (mDL) add-on functions|Ed2|Draft (DTS)||mdoc concept<br>Online use case|presentation-protocol, format, trust-model, validation||
|ISO/IEC 23220-1|Part 1: Generic system architectures of mobile eID systems|2023|Published|||issuance-process, issuance-protocol, presentation-protocol, other||
|ISO/IEC 23220-2|Part 2: Data objects and encoding rules for generic eID systems|2024|Published|||format||
|ISO/IEC 23220-3|Part 3: Protocols and services for installation and issuing phase||Draft (DTS)|||issuance-protocol||
|ISO/IEC 23220-4|Part 4: Protocols and services for operational phase||Draft (DTS)|||presentation-protocol, format, validation||
|ISO/IEC 23220-5|Part 5: Trust models and confidence level assessment||Draft|||trust-model||
|ISO/IEC 23220-7|Part 7: Registration Authority Procedures for Mobile Document||Draft|||format||
|ISO/IEC 7367-2|Personal identification — mdoc schemas Part 2: Mobile vehicle certificate||Draft (DTS)|||format||
|ISO/IEC 7367-3|Personal identification — mdoc schemas Part 3: Mobile technical report||Draft (NWIP)|||format||
|ISO/IEC 23635|Blockchain and distributed ledger technologies — Guidelines for governance|2022|Published||DLT/Blockchain trust model is not considered for the moment for APTITUDE|—||
|ISO/IEC 23257|Blockchain and distributed ledger technologies — Reference architecture|2022|Published||DLT/Blockchain trust model is not considered for the moment for APTITUDE|—||
|[IANA JWT Claims Registry](https://www.iana.org/assignments/jwt/jwt.xhtml)|JSON Web Token (JWT) Claims Registry|n/a|Continuously maintained||Registry of registered JWT claim names used in attestation metadata|format, other||
|ISO 15000-3|Electronic business eXtensible Markup Language (ebXML) Part 3: Registry and repository|2023|Published|||—||
|[ITU-T X.690](https://www.itu.int/rec/T-REC-X.690)|Information technology — ASN.1 encoding rules: Specification of Basic (BER), Canonical (CER) and Distinguished (DER) Encoding Rules; published jointly as ISO/IEC 8825-1|02/2021|Published||DER encoding of CRLs, OCSP requests and OCSP responses|validation, other||
|[CSC API](https://cloudsignatureconsortium.org/resources/csc-api-v2-2/)|CSC API version 2.2.0.0 - Architectures and protocols for remote signature applications|2.2.0.0|Published||Applicable for electronic signature|—||
|[CSC Data model](https://cloudsignatureconsortium.org/wp-content/uploads/2025/10/csc-dm.pdf)|CSC API Data Model for remote signature applications, V 1.0.0 ([additional](https://cloudsignatureconsortium.org/resources/download-api-specifications/))|1.0.0|Published||Applicable for electronic signature|—||
|[CSC Data model bindings](https://cloudsignatureconsortium.org/wp-content/uploads/2025/10/data-model-bindings.pdf)|CSC Data Model Bindings – version 1.0.0 ([additional](https://cloudsignatureconsortium.org/resources/download-api-specifications/))|1.0.0|Published||Applicable for electronic signature|—||

</div>

> **Note:** For the complete table of standards and specifications, refer to the [relevant-standards.md](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-rfcs/blob/main/doc/relevant-standards.md) file in the repository documentation folder.
