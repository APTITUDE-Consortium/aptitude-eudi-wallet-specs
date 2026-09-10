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

**Consumed by** — The APTITUDE artefact or artefacts that reference the
deliverable, followed by the mechanism concerned. *Not directly referenced* marks a
deliverable that no artefact cites but on which a cited deliverable depends. *Used but
not referenced* marks one whose requirements an artefact applies without citing it, and
therefore indicates a missing reference in that artefact rather than an optional entry.

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
| `other` | The deliverable has an applicability not captured by the values above. The aspect concerned is stated in *Consumed by*. |

A value followed by a question mark (for example `issuance-protocol?`) indicates
an applicability that has been proposed but not yet confirmed.

## Identification of standards&TS

Note: Titles are shortened and  omit the shared series prefix carried by every entry from the same body (e.g. the ETSI "…(ESI);" lead-in, and the ISO/IEC 18013 and 23220 family headers). Only the distinctive part is shown; the full official title is at the linked source in *Deliverable*.

Note: Titles are shortened and  omit the shared series prefix carried by every entry from the same body (e.g. the ETSI "…(ESI);" lead-in, and the ISO/IEC 18013 and 23220 family headers). Only the distinctive part is shown; the full official title is at the linked source in *Deliverable*.

<div class="standards-table" markdown>

|Deliverable|Title|Version|Status|Consumed by|Scope|
|:---|:---|:---|:---|:---|:---|
|[ETSI TS 119 602](https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf)| Lists of trusted entities; Data model|1.1.1|Published|RFC-03, RFC-05, trust-fw — list of trusted entities (LoTE) data model|trust-model|
|[ETSI TS 119 612](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf)| Trusted Lists|2.4.1|Published|trust-fw — EU trusted list format|trust-model|
|[ETSI TS 119 615](https://www.etsi.org/deliver/etsi_ts/119600_119699/119615/01.03.01_60/ts_119615v010301p.pdf)|Trusted lists; Procedures for using and interpreting European Union Member States national trusted lists|1.3.1|Published|RFC-03, trust-fw — trusted list processing and interpretation procedures|trust-model|
|[ETSI EN 319 411-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.05.01_60/en_31941101v010501p.pdf)| Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements|1.5.1|Published|trust-fw — NCP policy requirements applicable to WRPAC issuance|trust-model|
|[ETSI EN 319 411-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941102/02.06.01_60/en_31941102v020601p.pdf)| Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates|2.6.1|Published|trust-fw — qualified certificate policy requirements referenced alongside EN 319 411-1|trust-model|
|[ETSI TS 119 411-8](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf)| Policy and security requirements for Trust Service Providers issuing certificates; Part 8: Access Certificate Policy for EUDI Wallet Relying Parties|1.1.1|Published|RFC-04, trust-fw — WRPAC certificate policy and chain validation|trust-model|
|[ETSI TS 119 461](https://www.etsi.org/deliver/etsi_ts/119400_119499/119461/02.01.01_60/ts_119461v020101p.pdf)| Policy and security requirements for trust service components providing identity proofing of trust service subjects|2.1.1|Published|trust-fw — identity proofing of trust service subjects|issuance-process, issuance-protocol?|
|[ETSI TS 119 475](https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.02.01_60/ts_119475v010201p.pdf)| Relying party attributes supporting EUDI Wallet user's authorization decisions|1.2.1|Published|RFC-05, trust-fw — Register attributes and WRPAC attribute derivation|trust-model|
|[ETSI EN 319 412-1](https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf)| Certificate Profiles; Part 1: Overview and common data structures|1.6.1|Published|trust-fw — common certificate data structures|trust-model|
|[ETSI EN 319 412-2](https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf)| Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons|2.4.1|Published|trust-fw — certificate profile for natural persons|trust-model|
|[ETSI EN 319 412-3](https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf)|Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons|1.3.1|Published|trust-fw — certificate profile for legal persons|trust-model|
|[ETSI EN 319 412-5](https://www.etsi.org/deliver/etsi_en/319400_319499/31941205/02.06.01_60/en_31941205v020601p.pdf)| Certificate Profiles; Part 5: QCStatements|2.6.1|Published|trust-fw — QCStatements carried in WRPAC certificates|trust-model|
|[ETSI TS 119 412-6](https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.02.01_60/ts_11941206v010201p.pdf)| Certificate Profiles; Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers|1.2.1|Published|RFC-04, trust-fw — certificate profiles for PID, Wallet and (Q)EAA providers|trust-model|
|[ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf)| XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures|1.3.1|Published|trust-fw — XAdES B-B signature over the EU LOTL|trust-model|
|[ETSI TS 119 182-1](https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf)| JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures|1.2.1|Published|trust-fw — JAdES B-B signature over the JWT realisation of the WRPRC|trust-model, format|
|[ETSI TS 119 472-1](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.02.01_60/ts_11947201v010201p.pdf)| Profiles for Electronic Attestation of Attributes; Part 1: General requirements|1.2.1|Published|RFC-01 — EAA data model underlying the issuance profile|issuance-process, issuance-protocol, format, trust-model, validation|
|[ETSI TS 119 472-2](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.02.01_60/ts_11947202v010201p.pdf)| Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party|1.2.1|Published|RFC-02, RFC-05, trust-fw — EAA/PID presentation profiles|presentation-protocol|
|[ETSI TS 119 472-3](https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf)| Profiles for Electronic Attestation of Attributes; Part 3: Profiles for issuance of EAA or PID|1.1.1|Published|RFC-01, trust-fw — EAA/PID issuance profiles|issuance-process, issuance-protocol|
|[OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)|OpenID for Verifiable Credential Issuance 1.0|1.0|Published|RFC-01, trust-fw — base issuance protocol|issuance-process, issuance-protocol, format, trust-model|
|[OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)|OpenID for Verifiable Presentations 1.0|1.0|Published|RFC-02, trust-fw, DTC rulebook — base presentation protocol|presentation-protocol, format, trust-model|
|[DCQL](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html#name-digital-credentials-query-l)|Digital Credentials Query Language; defined within OpenID for Verifiable Presentations 1.0, clause 6|1.0|Published|RFC-02, trust-fw — Relying Party attestation query|presentation-protocol, format|
|[OpenID HAIP](https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-05.html)|OpenID4VC High Assurance Interoperability Profile|1.0|Published|RFC-01, RFC-02, trust-fw, mVRC rulebook — interoperability profile of OpenID4VCI and OpenID4VP|issuance-process, issuance-protocol, presentation-protocol, format, trust-model|
|OpenID|[OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html)||Published|mVRC rulebook (References table only; not cited in the body)|other|
|[W3C VCDM](https://www.w3.org/TR/vc-data-model-2.0/)|Verifiable Credentials Data Model v2.0|2.0|Published|RFC-02, mVRC rulebook — JSON-LD W3C VC presentation realisation|format|
|[W3C JSON-LD](https://www.w3.org/TR/json-ld11)|JSON-LD 1.1|16 July 2020|Published|RFC-01, RFC-02 — JSON-LD W3C VC credential format|format|
|[W3C DC API](https://www.w3.org/TR/digital-credentials/)|Digital Credentials API|29 January 2026|Draft|RFC-02 — noted as a possible future extension; not normative|presentation-protocol|
|[IETF RFC 1950](https://datatracker.ietf.org/doc/html/rfc1950)|ZLIB Compressed Data Format Specification version 3.3||Published|RFC-04, trust-fw — compression of the Status List Token `lst` claim|validation, other|
|[IETF RFC 1951](https://datatracker.ietf.org/doc/html/rfc1951)|DEFLATE Compressed Data Format Specification version 1.3||Published|RFC-04, trust-fw — compression of the Status List Token `lst` claim|validation, other|
|[IETF RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119)|Key words for use in RFCs to Indicate Requirement Levels||Published|All APTITUDE RFCs and rulebooks — normative language (BCP 14, with RFC 8174)|other|
|[IETF RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)|Date and Time on the Internet: Timestamps||Published|mVRC rulebook — encoding of date and time attributes|format|
|[IETF RFC 3647](https://datatracker.ietf.org/doc/html/rfc3647)|Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework||Published|trust-fw — certificate policy framework underpinning the WRPAC NCP requirements|trust-model|
|[IETF RFC 3739](https://datatracker.ietf.org/doc/html/rfc3739)|Internet X.509 Public Key Infrastructure: Qualified Certificates Profile||Published|trust-fw — qualified certificate profile referenced by the WRPAC requirements|trust-model|
|[IETF RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)|Uniform Resource Identifier (URI): Generic Syntax||Published|RFC-04 — syntax of status and revocation endpoint identifiers|validation, other|
|[IETF RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280)|Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile||Published|RFC-03, RFC-04, RFC-05, trust-fw — X.509 certificate and CRL profile, certification path validation|trust-model, validation, other|
|[IETF RFC 5755](https://datatracker.ietf.org/doc/html/rfc5755)|An Internet Attribute Certificate Profile for Authorization||Published|Not directly referenced — attribute certificate profile used by ETSI TS 119 412-6|format|
|[IETF RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)|The OAuth 2.0 Authorization Framework||Published|Not directly referenced — base specification of OpenID4VCI and OpenID4VP|issuance-protocol, presentation-protocol|
|[IETF RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960)|X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP||Published|RFC-04, trust-fw — OCSP revocation checking|trust-model, validation, other|
|[IETF RFC 7515](https://www.rfc-editor.org/rfc/rfc7515)|JSON Web Signature (JWS)||Published|trust-fw — JWS realisation of the WRPRC|format, trust-model|
|[IETF RFC 7516](https://datatracker.ietf.org/doc/rfc7516/)|JSON Web Encryption (JWE)||Published|Not directly referenced — encrypted response handling in OpenID4VP|presentation-protocol, format|
|[IETF RFC 7518](https://datatracker.ietf.org/doc/rfc7518/)|JSON Web Algorithms (JWA)||Published|RFC-01 — A128GCM and A256GCM content encryption algorithms|format|
|[IETF RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)|JSON Web Token (JWT)||Published|trust-fw — JWT realisation of the WRPRC|format|
|[IETF RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)|Proof Key for Code Exchange by OAuth Public Clients (PKCE)||Published|RFC-01 — PKCE with `S256` in the Authorisation Code Flow|issuance-protocol|
|[IETF RFC 8174](https://datatracker.ietf.org/doc/html/rfc8174)|Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words||Published|All APTITUDE RFCs — normative language (BCP 14, with RFC 2119)|other|
|[IETF RFC 8259](https://datatracker.ietf.org/doc/rfc8259/)|The JavaScript Object Notation (JSON) Data Interchange Format||Published|Not directly referenced — base encoding of all JSON artefacts|format|
|[IETF RFC 8392](https://datatracker.ietf.org/doc/html/rfc8392)|CBOR Web Token (CWT)||Published|RFC-05, trust-fw — CWT realisation of the WRPRC|format, trust-model|
|[IETF RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446)|The Transport Layer Security (TLS) Protocol Version 1.3||Published|Used but not referenced — transport protection of issuance, presentation and status endpoints|issuance-protocol, presentation-protocol, validation|
|[IETF RFC 8610](https://www.rfc-editor.org/rfc/rfc8610.html)|Concise Data Definition Language (CDDL)||Published|RFC-05, mVRC rulebook — CDDL definitions of mdoc structures|format|
|[IETF RFC 8943](https://www.rfc-editor.org/rfc/rfc8943)|Concise Binary Object Representation (CBOR) Tags for Date||Published|mVRC rulebook — CBOR tags for date values|format|
|[IETF RFC 8949](https://datatracker.ietf.org/doc/html/rfc8949)|Concise Binary Object Representation (CBOR)||Published|RFC-05, mVRC rulebook — CBOR encoding of mdoc structures|format|
|[IETF RFC 9052](https://www.rfc-editor.org/rfc/rfc9052)|CBOR Object Signing and Encryption (COSE): Structures and Process||Published|RFC-05, trust-fw — COSE structures for the CWT realisation of the WRPRC|format, trust-model|
|[IETF RFC 9101](https://datatracker.ietf.org/doc/html/rfc9101)|The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)||Published|Used but not referenced — signed Request Object in RFC-02|presentation-protocol|
|[IETF RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110)|HTTP Semantics||Published|Used but not referenced — endpoint methods, header fields and status codes in RFC-03 clause 7|validation, trust-model, other|
|[IETF RFC 9111](https://datatracker.ietf.org/doc/html/rfc9111)|HTTP Caching||Published|Used but not referenced — `Cache-Control` and `Expires` in RFC-03 clause 7.3; obsoletes RFC 7234|validation, trust-model, other|
|[IETF RFC 9126](https://datatracker.ietf.org/doc/html/rfc9126)|OAuth 2.0 Pushed Authorization Requests (PAR)||Published|RFC-01 — Pushed Authorisation Requests in the Authorisation Code Flow|issuance-protocol|
|[IETF RFC 9360](https://datatracker.ietf.org/doc/html/rfc9360)|CBOR Object Signing and Encryption (COSE): Header Parameters for Carrying and Referencing X.509 Certificates||Published|trust-fw — X.509 header parameters of the CWT realisation of the WRPRC|trust-model, format|
|[IETF RFC 9449](https://datatracker.ietf.org/doc/html/rfc9449)|OAuth 2.0 Demonstrating Proof of Possession (DPoP)||Published|RFC-01 — sender-constrained access tokens (DPoP)|issuance-protocol|
|[IETF RFC 9608](https://datatracker.ietf.org/doc/html/rfc9608)|No Revocation Available for X.509 Public Key Certificates||Published|trust-fw — signalling the absence of revocation information for WRPAC certificates|trust-model, validation|
|[IETF RFC 9901](https://datatracker.ietf.org/doc/rfc9901)|Selective Disclosure for JSON Web Tokens||Published|Not directly referenced — base specification of SD-JWT VC|format|
|[IETF SD-JWT-VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)|SD-JWT-based Verifiable Credentials (SD-JWT VC)|draft-ietf-oauth-sd-jwt-vc-13|Draft|RFC-01, RFC-02, mVRC rulebook — selective-disclosure credential format|format|
|[IETF Client authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/)|OAuth 2.0 Attestation-Based Client Authentication|draft-ietf-oauth-attestation-based-client-auth-11|Draft|RFC-01 — attestation-based client authentication|presentation-protocol|
|[IETF Token Status List](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/)|Token Status List (TSL)|draft-ietf-oauth-status-list-17|Draft|RFC-04, RFC-05, trust-fw — attestation status and revocation|validation, other|
|ISO/IEC 18013-5|Part 5: Mobile driving licence (mDL) application|2021|Published|RFC-02, RFC-05, trust-fw, DTC rulebook, mVRC rulebook — mdoc concept and proximity presentation|presentation-protocol, format, trust-model, validation|
|ISO/IEC 18013-5|Part 5: Mobile driving licence (mDL) application|Ed2|Draft (DIS)|Not yet consumed — monitored for mdoc revocation and other Ed2 changes|presentation-protocol, format, trust-model, validation|
|ISO/IEC 18013-7|Part 7: Mobile driving licence (mDL) add-on functions|2025|Published|RFC-02, mVRC rulebook — online mdoc presentation|presentation-protocol, format, trust-model, validation|
|ISO/IEC 18013-7|Part 7: Mobile driving licence (mDL) add-on functions|Ed2|Draft (DTS)|Not yet consumed — monitored for Ed2 changes|presentation-protocol, format, trust-model, validation|
|ISO/IEC 23220-2|Part 2: Data objects and encoding rules for generic eID systems|2024|Published|DTC rulebook — data objects and encoding rules|format|
|ISO/IEC 23220-4|Part 4: Protocols and services for operational phase||Draft (DTS)|DTC rulebook, mVRC rulebook — operational-phase protocols and data element identifiers|presentation-protocol, format, validation|
|ISO/IEC 7367-2|Personal identification — mdoc schemas Part 2: Mobile vehicle certificate||Draft (DTS)|mVRC rulebook — mobile vehicle certificate schema|format|
|ISO/IEC 7367-3|Personal identification — mdoc schemas Part 3: Mobile technical report||Draft (NWIP)|mVRC rulebook — referenced alongside ISO/IEC 7367-2|format|
|ISO 3166-1|Codes for the representation of names of countries and their subdivisions — Part 1: Country codes|2020|Published|trust-fw — country codes in the Register data model and in certificate attributes|trust-model, format|
|[IANA JWT Claims Registry](https://www.iana.org/assignments/jwt/jwt.xhtml)|JSON Web Token (JWT) Claims Registry|n/a|Continuously maintained|mVRC rulebook (References table only; not cited in the body)|format, other|
|[ITU-T X.690](https://www.itu.int/rec/T-REC-X.690)|Information technology — ASN.1 encoding rules: Specification of Basic (BER), Canonical (CER) and Distinguished (DER) Encoding Rules; published jointly as ISO/IEC 8825-1|02/2021|Published|Used but not referenced — DER encoding of CRLs and OCSP messages in RFC-04|validation, other|

</div>

> **Note:** For the complete table of standards and specifications, refer to the [relevant-standards.md](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-rfcs/blob/main/doc/relevant-standards.md) file in the repository documentation folder.
