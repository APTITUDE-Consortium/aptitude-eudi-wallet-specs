# Glossary Definitions

## Roles

roles:Attestation Provider (AP)
: When not further qualified, a collective term for QEAA Provider, PuB-EAA Provider, or (non-qualified) EAA Provider [ARF], acting as an Issuer of electronic attestations of attributes.

roles:Certificate Authority (CA)
: An entity which is trusted by one or more parties in the EUDI Wallet ecosystem to create and seal certificates. [ARF]

roles:Conformity Assessment Body (CAB)
: A conformity assessment body as defined in Article 2, point 13, of Regulation (EC) No 765/2008, which is accredited in accordance with that Regulation as competent to carry out conformity assessment of a qualified trust service provider and the qualified trust services it provides, or as competent to carry out certification of European Digital Identity Wallets or electronic identification means. [ARF]

roles:EAA Provider
: Provider of EEAs.

roles:Issuer Authority Certificate Authority (IACA)
: The issuing authority/CA used in the mDL/mVRC trust infrastructure under ISO standards (may be shared with mDL or set up separately).

roles:List of Trusted Entities Provider (LoTE Provider)
: The body that is responsible for the operation and/or management of the approval scheme under which the corresponding LoTE is published. [ETSI TS 119 602]

roles:List of Trusted Lists Scheme Operator (LOTLSO)
: The body that is responsible for the operation and/or management of the approval scheme under which the corresponding LOTL is published.

roles:National Accreditation Bodies (NAB)
: A body that performs accreditation with authority derived from a Member State under Regulation (EC) No 765/2008. [ARF]

roles:Owner of a Scheme for the Attestation of Attribute
: An entity responsible for establishing and maintaining a scheme for the attestation of attributes. [CIR 2025/1569]

roles:Provider of Person Identification Data (PID Provider)
: A natural or legal person responsible for issuing and revoking the person identification data and ensuring that the person identification data of a user is cryptographically bound to a Wallet Unit. [ARF]

roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)
: A natural or legal person mandated by a Member State to issue Relying Party access certificates to (Wallet-) Relying Parties registered in that Member State. [ARF]

roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)
: A natural or legal person mandated by a Member State to issue (wallet-relying party) registration certificates to (wallet-)relying parties registered in that Member State. [ARF]

roles:PuB-EAA Provider
: Provider of Public Electronic Attestation of Attributes (PuB-EAAs).

roles:Public Sector Body
: A state, regional or local authority, a body governed by public law or an association formed by one or several such authorities or one or several such bodies governed by public law, or a private entity mandated by at least one of those authorities, bodies or associations to provide public services, when acting under such a mandate. [ARF]

roles:QEAA Provider
: Provider of Qualified Electronic Attestation of Attributes (QEAAs).

roles:Qualified Trust Service Provider (QTSP)
: Qualified Trust Service Provider means a trust service provider who provides one or more qualified trust services and is granted the qualified status by the supervisory body. [ARF]

roles:Registrar
: The body responsible for establishing and maintaining the list of registered wallet-relying parties established in their territory who has been designated by a Member State. [ARF]

roles:Relying Party (RP)
: A natural or legal person that relies upon electronic identification, European Digital Identity Wallets or other electronic identification means, or upon a trust service. [ARF]

roles:Relying Party Intermediary (RPI)
: A Relying Party that offers services to other (intermediated) Relying Parties to, on their behalf, connect to Wallet Units and request the User attributes that these intermediated Relying Parties need. [ARF]

roles:Supervisory Body
: An entity responsible for supervisory tasks in the designating Member State as regards trust services. [REG-EU-2024/1183]

roles:Trusted Entity
: An entity that is recognized as trustworthy within a given approval scheme for a specific scope or purpose. [ETSI TS 119 602]

roles:Trusted List Provider
: A body responsible for maintaining, managing, and publishing Trusted Lists. [ARF]

roles:User
: A natural or legal person, or a natural person representing another natural person or a legal person, that uses trust services or electronic identification means provided in accordance with the [European Digital Identity Regulation]. [ARF]

roles:Wallet Provider (WP)
: A natural or legal person who provides Wallet Solutions. [ARF]

roles:Wallet-Relying Party (WRP)
: A relying party that intends to rely upon Wallet Units for the provision of public or private services by means of digital interaction. [ARF]

---

## Components

components:Authentic Source
: A repository or system, held under the responsibility of a public sector body or private entity, that contains and provides attributes about a natural or legal person or object and that is considered to be a primary source of that information or recognised as authentic in accordance with Union law or national law, including administrative practice. [ARF]

components:Authorisation Server
: OAuth 2.0 / OpenID component responsible for authenticating the User (Holder) and issuing tokens authorising access to protected endpoints.

components:EUDI Wallet
: European Digital Identity Wallet, in accordance with Regulation (EU) 910/2014 (as amended), used in APTITUDE pilots.

components:Keystore
: A hardware-backed repository and service in which non-critical cryptographic assets are generated, stored, and used exclusively inside a dedicated hardware security boundary. [ARF]

components:Public Key Infrastructure (PKI)
: Systems, software, and communication protocols that are used by EUDI Wallet ecosystem components to distribute, manage, and control public keys. A PKI publishes public keys and establishes trust within an environment by validating and verifying the public keys mapping to an entity. [ARF]

components:Register
: An electronic register used by a Member State to make information on WRP registered in that Member State publicly available as set out in Article 5b(5) of Regulation (EU) No 910/2014. [CIR 2024/2980]

components:Relying Application
: User-facing application, service, or workflow in which credential verification is performed.

components:Relying Party Instance
: A software and/or hardware module with the capability to interact with a Wallet Unit and to perform Relying Party authentication, that is controlled by a Relying Party. [ARF]

components:Verifier Backend
: Server-side component that creates presentation requests, receives presentation responses, validates them, and returns the result to the Relying Party Instance.

components:Wallet Instance
: The application installed and configured on a User's device or environment, which is part of a Wallet Unit, and that the User uses to interact with the Wallet Unit. [ARF]

components:Wallet Secure Cryptographic Application (WSCA)
: An application that manages critical assets by being linked to and using the cryptographic and non-cryptographic functions provided by the Wallet Secure Cryptographic Device. [ARF]

components:Wallet Secure Cryptographic Device (WSCD)
: A tamper-resistant device that provides an environment that is linked to and used by the Wallet Secure Cryptographic Application to protect critical assets and provide cryptographic functions for the secure execution of critical operations. [ARF]

components:Wallet Solution
: A combination of software, hardware, services, settings, and configurations, including Wallet Instances, one or more Wallet Secure Cryptographic Applications and one or more Wallet Secure Cryptographic Devices. [ARF]

components:Wallet Unit
: A unique configuration of a Wallet Solution that includes Wallet instances, Wallet Secure Cryptographic Applications and Wallet Secure Cryptographic Devices provided by a Wallet Provider to an individual Wallet User. [ARF]

---

## Artifacts

artifacts:Attestation Rulebook
: A document describing the attestation type, namespace(s), and other features for a specific attestation type. [ARF]

artifacts:Catalogue of Attributes
: A digital repository of attributes that is maintained and published online by the Commission. [CIR 2025/1569]

artifacts:Catalogue of Schemes for the Attestation of Attributes
: A digital repository listing schemes for the attestation of attributes registered in accordance with this Regulation and that is maintained (and published online) by the Commission. [CIR 2025/1569]

artifacts:Certificate Revocation List (CRL)
: A time-stamped list identifying revoked certificates that is signed by a CA or CRL issuer and made freely available in a public repository. [RFC 5280]

artifacts:Credential Issuer Metadata
: Artifact containing information on the Credential Issuer's technical capabilities, supported Credentials, and (internationalized) display information. [OID4VCI]

artifacts:Credential Offer
: Data structure created by a Credential Issuer to initiate issuer-initiated issuance, containing grant information and credential configuration references.

artifacts:Electronic Seal
: Data in electronic form which is attached to or logically associated with other data in electronic form to ensure the latter's origin and integrity. [ARF]

artifacts:Electronic Signature
: Data in electronic form which is attached to or logically associated with other data in electronic form and which is used by the signatory to sign. [ARF]

artifacts:Embedded Disclosure Policy (EDP)
: A set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes. [ARF]

artifacts:Key Attestation (KA)
: A type of Wallet Unit Attestation that attests the certification and properties of a WSCA/WSCD or keystore available to the Wallet Unit, and that contains one or more public keys whose corresponding private keys are generated by and stored in that WSCA/WSCD or keystore, as well as a revocation reference for the WSCD or keystore. [ARF]

artifacts:List of Trusted Entities (LoTE)
: List of entities that are recognized as trustworthy within a given approval scheme for a specific scope or purpose. Based on [ETSI TS 119 602]. [ARF]

artifacts:List Of Trusted Lists (LOTL)
: In order to allow access to the TLs of all Member States in an easy manner, the European Commission (EC) publishes a central list, called the List of Trusted Lists (LoTL), with links to the locations where the TLs are published as notified by Member States. [ETSI TS 119 615]

artifacts:mdoc
: Document or application that resides on a mobile device or requires a mobile device as part of the process to gain access to the document or application. [ISO/IEC 18013-5]

artifacts:Normalised Certificate Policy (NCP)
: A standardized set of rules and requirements that a Trust Service Provider must adhere to when issuing digital certificates. These include, e.g., organizational liability, security management, data privacy, and rigorous identity verification of the certificate subscriber.

artifacts:Official Journal of the European Union (OJEU)
: The Official Journal of the European Union, published by the EU's Publications Office, is the official publication for EU legal acts. The authenticity and integrity of the machine processable version of the LOTL is ensured through a digital signature supported by a certificate which can be authenticated through a publication in the OJEU.

artifacts:Presentation Request
: A request from a Verifier, conveyed in a Request Object, that specifies which credentials or attributes the Wallet must present, typically using a Presentation Definition (DIF PE).

artifacts:Qualified Electronic Signature (QES)
: An advanced electronic signature that is created by a qualified electronic signature creation device, and which is based on a qualified certificate for electronic signatures. [ARF]

artifacts:Request Object
: A JWT carrying OAuth 2.0 authorization request parameters as defined in RFC 9101, which may be passed by value or by reference (JAR); used in OID4VP to convey the Verifier's presentation request.

artifacts:Scheme for the Attestation of Attributes
: A set of rules applicable to one or more types of electronic attestation of attributes. [CIR 2025/1569]

artifacts:Status List Token
: A token in JWT or CWT representation that contains a cryptographically secured Status List. [draft-ietf-oauth-status-list]

artifacts:Strong User Authentication (SUA) Attestation
: An attestation used for strong user authentication in the context of electronic payments, such that, when a Relying Party sends a presentation request for the attestation to a Wallet Unit, it includes transactional data in the request. [ARF]

artifacts:Trust Anchor
: An authoritative entity represented by a public key and associated data. [ARF]

artifacts:Trusted List (TL)
: List that provides information about the status and the status history of the trust services from trust service providers regarding compliance with the applicable requirements and the relevant provisions of the applicable legislation. [ARF]

artifacts:Wallet Instance Attestation (WIA)
: A type of Wallet Unit Attestation that attests the integrity and authenticity of a Wallet Instance, and that carries a revocation reference for the Wallet Instance, as well as information about the Wallet Solution, including its name, version, and certification. [ARF]

artifacts:Wallet Unit Attestation (WUA)
: A data object that describes the components of the Wallet Unit or allows authentication and validation of those components. [ARF]

artifacts:Wallet-Relying Party Access Certificate (WRPAC)
: A certificate for electronic seals or signatures authenticating and validating the (Wallet-) Relying Party, issued by a provider of wallet-relying party access certificates. [ARF]

artifacts:Wallet-Relying Party Registration Certificate (WRPRC)
: A data object that indicates the attributes the Relying Party has registered to intend to request from Users. [ARF]

---

## Credentials

credentials:Attestation
: When not further qualified, a collective term for a QEAA, PuB-EAA, or (non-qualified) EAA. [ARF]

credentials:electronic Certificate of Conformity (eCoC)
: Manufacturer's electronic certificate; selected entries are mapped into EU-mVRC.

credentials:Electronic Attestation of Attributes (EAA)
: An attestation in electronic form that allows attributes to be authenticated. [ARF]

credentials:European Union mobile Vehicle Registration Certificate (EU-mVRC)
: The mobile (digital) vehicle registration certificate as an attestation in the EUDI Wallet; a profile of mVC under ISO/IEC 7367-2.

credentials:Internet Assigned Numbers Authority JSON Web Token (IANA JWT) Claims
: IANA registry of standard JWT claim names.

credentials:mobile Driving Licence (mDL)
: The mobile driving licence per ISO/IEC 18013-5/-7; used alongside mVRC and mTR in the EUDI Wallet.

credentials:mobile Technical Report (mTR)
: A mobile roadworthiness/inspection report (companion to mVRC/mDL) per ISO/IEC 7367-3.

credentials:mobile Vehicle Certificate (mVC)
: The family of mobile vehicle certificates defined in ISO/IEC 7367-2, on which the EU-mVRC is profiled.

credentials:Person Identification Data (PID)
: A set of data that is issued in accordance with Union or national law and that enables the establishment of the identity of a natural or legal person, or of a natural person representing another natural person or a legal person. [ARF]

credentials:Public Electronic Attestation of Attributes (PuB-EAA)
: An electronic attestation of attributes issued by a public sector body that is responsible for an authentic source or by a public sector body that is designated by the Member State to issue such attestations of attributes on behalf of the public sector bodies responsible for authentic sources in accordance with Article 45f and with Annex VII. [ARF]

credentials:Qualified Electronic Attestation of Attributes (QEAA)
: An electronic attestation of attributes which is issued by a qualified trust service provider and meets the requirements laid down in Annex V. [ARF]

processes:Selective Disclosure Java Web Token Verifiable Credential (SD-JWT VC)
: A verifiable credential format based on Selective Disclosure JWT; one of the formats supported in EUDI for some attestations.

---

## Protocols

protocols:Attestation Revocation List
: A mechanism provided by a PID Provider or an Attestation Provider (or a trusted party acting on its behalf) for communicating the revocation status of PIDs and attestations, by publishing a list of identifiers of revoked PIDs or attestations. [ARF]

protocols:Attestation Status List
: A mechanism provided by a PID Provider or an Attestation Provider (or a trusted party acting on its behalf) for communicating the revocation status of PIDs and attestations, by publishing status information (Valid or Invalid) for all relevant PIDs or attestations. [ARF]

protocols:Certificate Policy (CP)
: A named set of rules that indicates the applicability of a certificate to a particular community and/or class of application with common security requirements. [ARF]

protocols:DPoP
: Demonstrating Proof of Possession. A mechanism that binds access tokens and refresh tokens to a client key pair, preventing token replay by third parties. [RFC 9449]

protocols:High Assurance Interoperability Profile (HAIP)
: OpenID4VC profile aimed at higher assurance interoperability.

protocols:Online Certificate Status Protocol (OCSP)
: Enables applications to determine the (revocation) state of an identified certificate. [RFC 2560]

protocols:OpenID for Verifiable Credentials Issuance (OID4VCI)
: OID4VCI is an open standard that defines a secure API for issuing Verifiable Credentials (VCs) to a user's digital wallet.

protocols:OpenID for Verifiable Presentation (OID4VP)
: OID4VP is a standard that defines how a user presents Verifiable Credentials from their wallet to a verifier.

protocols:PKCE
: Proof Key for Code Exchange. An extension to the OAuth 2.0 authorization code flow that prevents authorization-code interception attacks using a code verifier and code challenge. [RFC 7636]

protocols:Proximity Flow
: Short-range presentation protocol (NFC/BLE/Wi-Fi Aware) per ISO/IEC 18013-5/-7.

protocols:Remote Flow
: Remote presentation protocol (same-device or cross-device).

---

## Processes

processes:Authentication
: An electronic process that enables the confirmation of the electronic identification of a natural or legal person or the confirmation of the origin and integrity of data in electronic form. [ARF]

processes:Device Binding
: Association of a credential or session with a specific device, establishing that the credential can only be used from the bound device.

processes:Electronic Identification Scheme
: A system for electronic identification under which electronic identification means are issued to natural or legal persons or natural persons representing other natural persons or legal persons. [ARF]

processes:Key Binding
: Cryptographic binding of a credential to a specific key pair held by the Wallet, ensuring only the key holder can present that credential.

processes:Notification
: The act of transferring information to the European Commission. [ARF]

processes:Proof of Possession
: Cryptographic proof demonstrating control of a private key, produced by signing a server-issued challenge; used to bind credentials and tokens to a Wallet key.

processes:Selective Disclosure
: The capability enabling the User to present a subset of the attributes included in a PID or attestation. [ARF]

processes:Strong User Authentication
: An authentication based on the use of at least two authentication factors from different categories of either knowledge, something only the user knows, possession, something only the user possesses or inherence, something the user is, that are independent, in that the breach of one does not compromise the reliability of the others, and is designed in such a way as to protect the confidentiality of the authentication data. [ARF]

---

## Formats

formats: Concise Data Definition Language (CDDL)
: The language to define CBOR structures (e.g., `tstr`, `uint`, `bstr`, `tdate`).

formats:Concise Binary Object Representation (CBOR)
: The binary serialisation format used for mdoc transfers.

formats:Selective Disclosure JWT (SD-JWT)
: A composite structure, consisting of a JWS plus optional Disclosures, enabling selective disclosure of portions of the JWS payload. [RFC 9901]

formats:W3C Verifiable Credentials Data Model v2.0 (W3C VCDM v2.0)
: A family of specifications for VC data models.

---

## Data Elements

data-elements:Administrative Validity Period
: Dates during which attributes in an attestation remain valid as represented inside it.

data-elements:Attestation Type
: An identifier for a type of attestation, unique within the context of the EUDI Wallet ecosystem. [ARF]

data-elements:Attribute
: A characteristic, quality, right or permission of a natural or legal person or of an object. [ARF]

data-elements:Entitlement
: It represents the WRP role and is uniquely identified by a suitable identifier in form of an OID or URI. [CIR 2025/848]

data-elements:Mobile Security Object (MSO)
: A security object carrying metadata and the issuer's signature over data elements in mdoc/mDL/mVRC.

data-elements:Namespace
: A specification of the attribute identifier, syntax and semantics of attributes that can be used in an attestation, having an identifier that is unique within the context of the EUDI Wallet ecosystem. [ARF]

data-elements:Nonce
: A single-use, unpredictable value issued by a server to prevent replay attacks; Wallets must include it verbatim in proofs or responses.

data-elements:Pseudonym
: Data uniquely representing a User which in itself does not allow to infer the User's attributes or person identification data, without the use of additional information that is kept separately by the issuer of the data uniquely representing the user. [ARF]

data-elements:Technical Validity Period
: The dates (and possibly times) from and up to which the attestation is valid, which are represented as metadata of the attestation. [ARF]
