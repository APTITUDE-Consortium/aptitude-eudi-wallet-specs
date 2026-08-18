# Generic issuance flow specification

Version 0.9 (draft)
Date 18-08-2026

## Authors

1. Aleksandar Simsic, ICTU
2. Nikos Triantafyllou, University of the Aegean
3. Andrea Moro, Fondazione Bruno Kessler

## Reviewers

1. Giancarlo Degani, Infocert
2. Luca Vallone, IPZS
3. ...

## Table of Contents

1. Introduction
2. Aptitude landscape overview
   * 2.1 Relation between different standards and interfaces
3. Interaction details
   * 3.1 Flow requirements
     * 3.1.1 OID4VCI requirements
     * 3.1.2 HAIP requirements
     * 3.1.3 ETSI 119 472-3 requirements
     * 3.1.4 TS3 requirements
     * 3.1.5 Additional Aptitude requirements
   * 3.2 Detailed technical flow description (sequence diagram)
     * 3.2.1 Steps mapping overview

## 1 Introduction

This document is a **non-normative companion** to the APTITUDE horizontal RFC specifications. It provides implementers with a single entry point for the generic credential issuance flow by:

* mapping the APTITUDE issuance flow end-to-end as a sequence diagram
* identifying which RFC section governs each step
* clarifying which interfaces and scenarios are in or out of scope for APTITUDE

It does not define new requirements — those are in the RFCs. In case of conflict between this document and an RFC, the RFC takes precedence.

## 2\. Aptitude landscape overview

Following diagram uses EUDI Wallet ecosystem roles diagram from [ARF 2.9](https://eudi.dev/2.9.0/architecture-and-reference-framework-main/#3-roles-within-the-eudi-wallet-ecosystem) as base and presents adaptations relevant for issuance process within the Aptitude LSP.

![Aptitude roles and interactions overview - issuance flow](Aptitude_roles_and_interactions_overview-issuance_flow.png)

Aptitude has several specifics on how the trust framework specific roles are filled in where it differs from the way that the related roles will finally being filled in within the full production setup in the Europe.

Here we are only clarifying which roles and/or interfaces are out of the scope of this flow specification:

| Interface | Description | Rationale |
|-----------|-------------|-----------|
| Authentic Source → Issuer | How the Issuer retrieves data from the national authentic source | Assumed to be resolved at national level by each partner acting as Issuer |
| QTSP → Attribute Catalogue | Citizen-initiated flow where a QTSP validates and issues a VC from scratch | No WP in APTITUDE covers this scenario |
| Wallet → APTITUDE Register (runtime) | Runtime lookup from Wallet to APTITUDE Register | Redundant: WRPRC is provisioned at onboarding time (design-time); registration certificate is becoming mandatory per 2025/848 IA.<br><br>*Note: A Wallet Instance MAY still use the Register APIs to:*<ul><li>*Check fresh Entity registration information as a backup to the WRPRC failure,*</li><li>*Check that the Registration certificate obtained by the WRP is bound to the service the Wallet Instance is interacting with.*</li></ul> |

### 2.1 Relation between different standards and interfaces

Following diagram uses Aptitude EUDI Wallet ecosystem diagram as starting point, keeping in the picture just the roles that are relevant for the scope of this flow specification. It labels each interaction between the two roles and classifies each interface as a design time (blue label) or as a runtime (red label) interface.

![Aptitude issuance landscape roles and interfaces](Aptitude_issuance_landscape-roles_and_interfaces_overview.png)

In following table for each identified interface one or more of the relevant standards are listed. Further down within this flow specification these interfaces and related standards will be further used and referenced.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Interface</strong></th>
<th style="text-align: center;"><strong>Applicable
standards</strong></th>
<th style="text-align: center;"><strong>Additional comment</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>O1</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md">TS6</a>,</td>
<td>Register party with its role (Issuer/Wallet Provider)</td>
</tr>
<tr>
<td>O2</td>
<td><a
href="https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf">ETSI
TS 119 411-8 ver1.1.1</a>, <a
href="https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.02.01_60/ts_119475v010201p.pdf">ETSI
TS 119 475 ver1.2.1</a>, <a
href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a>, <a
href="https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf">ETSI
EN 319 412-2</a>, <a
href="https://www.etsi.org/deliver/etsi_en/319400_319499/31941203/01.03.01_60/en_31941203v010301p.pdf">ETSI
EN 319 412-3</a>, <a
href="https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf">ETSI
TS 119 412-6</a></td>
<td>Distribution of WRPACs, Sign/Seal Certififcates and WRPRCs</td>
</tr>
<tr>
<td>O3</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts2-notification-publication-provider-information.md">TS2</a></td>
<td>Notifying TLP’s for related TL’s (Wallet Providers, (Pub-)EAA
Providers, Providers of Access and Register Certificate)</td>
</tr>
<tr>
<td>O4</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md">TS3 ver1.5.2</a></td>
<td>Issuing of WUAs (WIA \\\&amp; KAs) for WI as per <a
href="https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202601731">CIR 2026/1731</a></td>
</tr>
<tr>
<td>O5</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md">TS3 ver1.5.2</a>, <a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-management-lifecycle/">APTITUDE Trust management and lifecycle</a>, <a
href="https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/21/">IETF Token Status List Draft 21</a></td>
<td>Scheduled revocation checks for WIA and KA as per <a
href="https://eudi.dev/3.0.0/annexes/annex-2/annex-2.02-high-level-requirements-by-topic/#a2322-topic-38-wallet-unit-revocation">ARF Topic 38</a> and requirement WURevocation_19</td>
</tr>
<tr>
<td>R1</td>
<td><p><a
href="https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html">OID4VCI ver1.0</a>,
<a
href="https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-final.html">HAIP ver1.0</a>,
<a
href="https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf">ETSI
TS 119 472-3 ver1.1.1</a>,
<a
href="https://www.rfc-editor.org/rfc/rfc9449.html">RFC9449</a>,
<a
href="https://datatracker.ietf.org/doc/html/draft-ietf-oauth-attestation-based-client-auth-10">IETF OAuth 2.0 Attestation-Based Client Authentication Draft 10</a></p>
<p>ISO18013-5, <a
href="https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/17/">SD-JWT
VC Draft 17</a>, <a
href="https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.01.01_60/ts_11947201v010101p.pdf">ETSI
TS 119 472-1 ver1.1.1</a></p></td>
<td>VCI and supporting standards</td>
</tr>
<tr>
<td>R2</td>
<td><a
href="https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf">ETSI
TS 119 602 ver1.1.1</a>, <a
href="https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf">ETSI
TS 119 612 ver2.4.1</a>, <a
href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a></td>
<td>Fetching QEAA or PubEAA TL (what do we do with EAA TL?)<br>Fetching WRPAC and WRPRC LoTEs from their respective LoTE Providers</td>
</tr>
<tr>
<td>R3</td>
<td><a
href="https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf">ETSI
TS 119 602 ver1.1.1</a>, <a
href="https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf">ETSI
TS 119 612 ver2.4.1</a></td>
<td>Fetching Wallet Providers LoTE</td>
</tr>
<tr>
<td>R4</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md#222-transport-of-key-attestation-ka">TS3 ver1.5.2</a></td>
<td>Signing WIA and KA as per <a
href="https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202601731">CIR 2026/1731</a></td>
</tr>
<tr>
<td>R5</td>
<td><a
href="https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts3-wallet-unit-attestation.md#243-pid-provider-and-attestation-provider-responsibilities">TS3 ver1.5.2</a>, <a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-management-lifecycle/">APTITUDE Trust management and lifecycle</a>, <a
href="https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/21/">IETF Token Status List Draft 21</a></td>
<td>Runtime status, and key-storage status checks on WIA/KA; the checks are to be profiled precisely in <a href="../horizontal-RFCs/RFC004.md">RFC004</a>.</td>
</tr>
</tbody>
</table>

The process behind O1, O2 and O3 is further explained in Apptitude on-boarding document, please look here <span class="mark"><</span>
<span class="mark">[wp2-trust-specifications/docs/topics/onboarding-process.md at main · APTITUDE-Consortium/wp2-trust-specifications](https://github.com/APTITUDE-Consortium/wp2-trust-specifications/blob/main/docs/topics/onboarding-process.md)></span> for more details.

## 3\. Interaction details

In this section generic issuance flow is further detailed by identifying exact API/message or other mechanism that takes place at each step.
After the diagram each step is then linked to the underlying RFC that provides more details on it’s usage.

### 3.1 Flow requirements

Here is the overview of the requirements taken from identified standard specifications that do have impact on flow diagram provided within this document.

#### 3.1.1 OID4VCI requirements

In follow up table the requirements are listed with decision if it is in the scope or not of this version of the Aptitude issuance flow specification.

|**Requirement**|**Scope decision**|
|-|-|
|Authorization and pre-authorized code flows|In scope\[^1]\[^2]|
|Wallet initiated and issuer initiated flow|In scope|
|Same device and cross-device flow|In scope|
|Immediate and deferred issuance|In scope|
|Nonce Endpoint offered by the issuer|In scope|
|Metadata Endpoint offered by the issuer|In scope|
|Sending credential offer by value and by reference|In scope|
|Notification Endpoint for credential lifecycle mngmt|Not in the scope|

#### 3.1.2 HAIP requirements

Comparing to the OID4VCI the HAIP requirements are stricter on what must
be implemented versus what may be implemented. In the following table
the requirements impacting issuance flow are listed.

|**Requirement**|**Scope decision**|
|-|-|
|Authorization code flow shall be supported|In scope|
|Shall use PKCE with s256 as the code challenge method ([RFC7636](https://www.rfc-editor.org/rfc/rfc7636.txt))|In scope|
|Shall use Pushed Authorization Request – PAR ([RFC9126](https://www.rfc-editor.org/rfc/rfc9126.txt))|In scope|
|Shall support DPOP including DPOP-Nonce HTTP header ([RFC9449](https://www.rfc-editor.org/rfc/rfc9449.txt))|In scope|
|Shall support wallet attestation as OAuth client authentication|In scope|
|Shall support attestation proof type including nonce within KA|In scope|

#### 3.1.3 ETSI 119 472-3 requirements

ETSI profile is delivered on top of HAIP profile to clarify all the
specifics for the EUDI wallet implementation. It includes clarifications
on how different trust and policy checks should take place, something
that is also referenced later within the generic technical flow
(sequence diagram). Follow up table includes therefore requirements
impacting issuance flow and designed validation checks.

|**Requirement**|**Scope decision**|
|-|-|
|Issuer and wallet unit shall support access and registration certificate of (Pub-)EAA provider|In scope|
|Issuer may support inclusion of embedded disclosure policy and wallet unit shall process it|In scope|
|Wallet unit shall include WIA to the push authorization and token endpoint|In scope|
|Wallet unit shall include KA to the credential endpoint when issuing device bound attestation|In scope|
|Holder shall prove the possession of private key associated to the public key in KA|In scope|
|Proofing that the same WSCA/WSCD possesses the private keys associated to the public keys in the WIA and one used for the attestation binding|In scope|
|Issuer metadata shall be signed as per [OID4VCI instructions](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html#name-signed-metadata)|In scope|
|Issuer metadata may include provision of EAA reuse policy|Not in the scope|

#### 3.1.4 TS3 requirements

Latest [IA 2026/1731](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601731) with Annex Ib and according ARF TS03 specifications introduce following requirements relevant for the wallet providers and issuers during the issuance process.

|**Requirement**|**Scope decision**|
|-|-|
|Issuer shall check run time WIA revocation status during the issuance process|In scope|
|Issuer shall check run time KA revocation status during the issuance process of the device bound attestation|In scope|
|Attestation provider issuing revocable attestation may set periodical revocation WIA and KA checks. Checks support decision to revoke an attestation in the case that the wallet provider revoked the wallet unit or the issued key|In scope|

#### 3.1.5 Additional Aptitude requirements

In some cases to simplify implementation for the partners there are number of additional requirements added on the top of all formal standards and specifications

|**Requirement**|**Scope decision**|
|-|-|
|Issuer and wallet unit shall use so called "combined mode" using only DPoP proof, as per [IETF oAuth attestation based client authentication DPoP Combined Mode](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-attestation-based-client-auth-10#name-dpop-combined-mode) |In scope|
|Issuer authorization and resource servers shall mandate using of fresh nonce value within the DPoP |In scope|
|Issuer shall offer Nonce Endpoint  |In scope|
|Issuer shall require a presence of WIA and DPoP header on token endpoint for pre-authorized code flow  |In scope|
|Wallet shall send WIA at the PAR and Token endpoints for Authorization Code Flow, prove possession of the WIA `cnf` key, and Issuers shall validate the WIA signature, expiry, and proof of possession as profiled in [RFC-01](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#73-authorisation-endpoint-and-par)|In scope|
|Wallet shall send KA at the Credential Endpoint using the selected proof method, and Issuers shall validate the KA and bind issued credentials to the attested keys as profiled in [RFC-01](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#75-credential-endpoint)|In scope|
|Trust anchors for EAA Providers shall be present in a dedicated LoTE|In scope|
|Authentic Source integration|Not in scope|
|Common Credential Catalogue discovery|Not in scope|

The generic issuance flow does not define an Authentic Source interface or a common Credential Catalogue. A Wallet therefore cannot discover credentials through a shared catalogue; each use case manages its own credential offers and selection.

### 3.2 Detailed technical flow description (sequence diagram)

E2E issuance flow is presented through sequence diagram (SD) and after that each step is linked to the relevant Aptitude profile specification document. Referenced specs are:

* [Aptitude Issuance profile RFC-01](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md)
* [Aptitude Trust Evaluation RFC-03](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC003.md)
* [Aptitude Trust Evaluation RFC-04](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC004.md)
* [Aptitude trust framework](https://aptitude-consortium.github.io/wp2-trust-specifications/latest/trust-framework/)

Within the following diagram we introduce the LoTE Provider endpoint as specified in [RFC003](https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC003.md#71-lote-endpoint). Each entity type (Wallet Provider, PID/Attestation Provider, WRPAC/WRPRC Provider) has a unique LoTE published at a specific endpoint detailed in the Official Journal of Aptitude (OJA), which will be made available by WP2 in piloting. The diagram abstracts these different LoTE endpoints into a single LoTE Provider interaction.

![QEAA issuance Aptitude profile sequence diagram]({Q}EAA_issuance_Aptitude_profile_on_top_of_HAIP&ETSI_profiles_including_trustframework.png)

### 3.2.1 Steps mapping overview

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 31%" />
<col style="width: 25%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>SD step number</strong></th>
<th style="text-align: center;"><strong>API/message</strong></th>
<th style="text-align: center;"><strong>More info</strong></th>
<th style="text-align: center;"><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1a Select Issuer</td>
<td>N.A.</td>
<td><a
href="https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html#appendix-H.6">OIDVCI
– H6</a></td>
<td></td>
</tr>
<tr>
<td>1b2A, 1.b.2B1</td>
<td>Credential Offer</td>
<td rowspan="2"><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#622-credential-offer-creation">RFC-01
6.2.2</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#623-credential-offer-delivery-and-wallet-invocation">RFC-01
6.2.3</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#81-wallet-invocation-interface">RFC-01
8.1</a></p></td>
<td></td>
</tr>
<tr>
<td><p>1b.2B2, 1b.2C</p>
<p>1b.2D5, 1b.2E6</p></td>
<td>Get Credential Offer</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Get Issuer metadata</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#611-configuration-and-discovery">RFC-01
6.1.1</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#89-metadata-endpoints">RFC-01
8.9</a></p></td>
<td></td>
</tr>
<tr>
<td>V2.1</td>
<td>Validate issuer metadata</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC001.md#89-metadata-endpoints">RFC-01
8.9</a></p>
</td>
<td></td>
</tr>
<tr>
<td>V2.2</td>
<td>Validate WRPAC</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/wp2-trust-specifications/blob/main/docs/topics/access-certificate.md">Aptitude
WRPAC</a></p>
<p><a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-evaluation-process/#authentication-process">Authentication Process</a></p></td>
<td></td>
</tr>
<tr>
<td>V2.3, V4a.2</td>
<td>Get LoTE</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC003.md#71-lote-endpoint">RFC003
LoTE Endpoint</a></p>
<p><a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-evaluation-process/#list-of-trusted-entities-validation-process">LoTE Validation Process</a></p></td>
<td></td>
</tr>
<tr>
<td>V2.4</td>
<td>Get QEAA/Pub-EAA/EAA Provider LoTE</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC003.md#71-lote-endpoint">RFC003
LoTE Endpoint</a></p>
<p><a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-evaluation-process/#list-of-trusted-entities-validation-process">LoTE Validation Process</a></p></td>
<td></td>
</tr>
<tr>
<td>V2.5</td>
<td>Validate WRPRC</td>
<td><a
href="https://github.com/APTITUDE-Consortium/wp2-trust-specifications/blob/main/docs/topics/registration-certificate.md">Aptitude
WRPRC</a></td>
<td></td>
</tr>
<tr>
<td>V2.6</td>
<td>Process Embedded Policy</td>
<td><a
href="https://github.com/APTITUDE-Consortium/wp2-trust-specifications/blob/main/docs/topics/embedded-disclosure-policy.md">Aptitude
embedded disclosure policies</a></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nonce Request</td>
<td><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#86-nonce-endpoint">RFC-01
8.6</a></td>
<td></td>
</tr>
<tr>
<td>3.1</td>
<td>KA request</td>
<td></td>
<td></td>
</tr>
<tr>
<td>3.2</td>
<td>WIA request</td>
<td></td>
<td></td>
</tr>
<tr>
<td>4.a.2</td>
<td>PAR request</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#613-pushed-authorisation-request-par">RFC-01
6.1.3</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#83-par-endpoint">RFC-01
8.3</a></p></td>
<td></td>
</tr>
<tr>
<td>4.a.3</td>
<td>Authorization request</td>
<td></td>
<td></td>
</tr>
<tr>
<td>V4a.1, V5.1</td>
<td>Validate WIA</td>
<td>
  <p>TODO: Sign/Seal Validation link</p>
</td>
<td></td>
</tr>
<tr>
<td>V4a.3</td>
<td>Get Wallet Providers LoTE</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/rfc003-trust/docs/horizontal-RFCs/RFC003.md#71-lote-endpoint">RFC003
LoTE Endpoint</a></p>
<p><a
href="https://aptitude-consortium.github.io/wp2-trust-specifications/latest/sections/trust-evaluation-process/#list-of-trusted-entities-validation-process">LoTE Validation Process</a></p></td>
<td></td>
</tr>
<tr>
<td>4.a.6</td>
<td>Authorization response</td>
<td></td>
<td></td>
</tr>
<tr>
<td>5.1</td>
<td>Token request</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#615-token-request">RFC-01
6.1.5</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#84-token-endpoint">RFC-01
8.4</a></p></td>
<td></td>
</tr>
<tr>
<td>6.1</td>
<td>Credential Request</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#616-credential-request">RFC-01
6.1.6</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#627-credential-request">RFC-01
6.2.7</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#75-credential-endpoint">RFC-01
7.5</a></p></td>
<td></td>
</tr>
<tr>
<td>V6.1</td>
<td>Verify Key Proof</td>
<td></td>
<td></td>
</tr>
<tr>
<td>6.2</td>
<td>Deferred credential</td>
<td><p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#63-deferred-credential-request">RFC-01
6.3</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#76-deferred-credential-endpoint">RFC-01
7.6</a></p>
<p><a
href="https://github.com/APTITUDE-Consortium/aptitude-eudi-wallet-specs/blob/main/docs/horizontal-RFCs/RFC001.md#88-deferred-credential-endpoint">RFC-01
8.8</a></p></td>
<td></td>
</tr>
</tbody>
</table>

\[^1]: Note that wallet must implement both code flows, the issuer may choose to implement only one

\[^2]: Note that pre-authorized code flow doesn’t meet requirements for issuing the attestation with Level of Assurance HIGH
