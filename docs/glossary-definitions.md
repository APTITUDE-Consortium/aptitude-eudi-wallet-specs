# Glossary Definitions

roles:Wallet User
: Person who controls a Wallet Unit.

roles:Wallet Provider
: Natural or legal person that provides Wallet Solutions.

roles:PID Provider
: Entity issuing and revoking Person Identification Data (PID) and binding it to a Wallet Unit.

roles:Attestation Provider
: Collective term for QEAA, PuB-EAA, or EAA providers.

roles:(Wallet-) Relying Party
: Natural or legal person intending to rely on Wallet Units for digital interactions.

roles:Access Certificate Authority
: Provider mandated by a Member State to issue wallet-relying party access certificates.

roles:Holder
: Natural person or legal representative controlling the Wallet and authorising credential issuance or presentation.

roles:Verifier
: Entity requesting verifiable presentations, validating the response, and making an authorisation or business decision based on the outcome.

roles:Credential Issuer
: Entity that decides to issue Verifiable Credentials and operates, or is associated with, the issuance service.

roles:Authorisation Server
: OAuth 2.0 / OpenID component responsible for authenticating the Holder and issuing tokens authorising access to protected endpoints.

roles:Verifier Backend
: Server-side component that creates presentation requests, receives presentation responses, validates them, and returns the result to the relying application.

roles:Relying Application
: User-facing application, service, or workflow in which credential verification is performed.

roles:Holder (W2W)
: User presenting attributes from their Wallet Unit to another Wallet Unit.

roles:Verifier (W2W)
: User requesting attributes from another Wallet Unit.

components:Wallet Solution
: Combination of software, hardware, services, settings, and configurations, including Wallet Instances, WSCA(s), and WSCD(s).

components:EUDI Wallet
: European Digital Identity Wallet used in APTITUDE pilots.

components:Wallet Unit
: Unique configuration of a Wallet Solution provided to a Wallet User.

components:Wallet Instance
: Application installed and configured on a User's device/environment to interact with the Wallet Unit.

components:Wallet Secure Cryptographic Application (WSCA)
: Application managing critical assets using the functions of a WSCD.

components:Wallet Secure Cryptographic Device (WSCD)
: Tamper-resistant device providing the secure environment and crypto functions used by a WSCA.

components:Wallet Unit Attestation (WUA)
: Data object describing Wallet Unit components or enabling their authentication/validation.

components:Wallet Instance Attestation (WIA)
: Client attestation material presented by a Wallet Instance at the PAR and Token endpoints to authenticate the Wallet during issuance flows.

components:Keystore
: Hardware-backed repository for generating, storing, and using non-critical cryptographic assets.

component:Qualified Trust Service Provider (QTSP)
: A qualified trust services provider authorised, among other things, to issue QEAA under eIDAS/eIDAS2.

credentials:Person Identification Data (PID)
: Data set that enables the establishment of a person's identity.

credentials:Electronic Attestation of Attributes (EAA)
: Electronic attestation that allows attributes to be authenticated.

credentials:Qualified Electronic Attestation of Attributes (QEAA)
: EAA issued by a Qualified Trust Service Provider in line with Annex V.

credentials:Public Electronic Attestation of Attributes (PuB-EAA)
: An attestation issued by a public sector body responsible for an authentic source of data (outside the qualified trust service regime).

credentials:Attestation
: Collective term for QEAA, PuB-EAA, or non-qualified EAA.

credentials:Attestation type
: Identifier for a type of attestation, unique within the EUDI Wallet ecosystem.

credentials:Namespace
: Specification of attribute identifiers, syntax, and semantics for an attestation.

credentials:Attestation Rulebook
: Document describing attestation type, namespaces, and related features.

credentials:Wallet-relying party access certificate
: Certificate authenticating and validating a (wallet-) relying party.

credentials:Wallet-relying party registration certificate
: Data object indicating the attributes a Relying Party has registered to request.

credentials:Administrative validity period
: Dates during which attributes in an attestation remain valid as represented inside it.

credentials:Technical validity period
: Metadata dates/times during which the attestation is valid; typically shorter than the administrative period.

credentials:Attestation Revocation List
: List-based mechanism for communicating revoked PIDs or attestations.

credentials:Attestation Status List
: Mechanism publishing status (valid/invalid) for relevant PIDs or attestations.

credentials:Pseudonym
: Data uniquely representing a User without revealing their attributes by itself.

credentials:Selective Disclosure
: Capability for a User to present only a subset of attributes from a PID or attestation.

credentials:EU-mVRC (European Union mobile Vehicle Registration Certificate)
: The mobile (digital) vehicle registration certificate as an attestation in the EUDI Wallet; a profile of mVC under ISO/IEC 7367‑2.

credentials:mVC (mobile Vehicle Certificate
: The family of mobile vehicle certificates defined in ISO/IEC 7367‑2, on which the EU‑mVRC is profiled.

credentials:mTR (mobile Technical Report)
: A mobile roadworthiness/inspection report (companion to mVRC/mDL) per ISO/IEC 7367‑3.

credentials:mDL (mobile Driving Licence)
: The mobile driving licence per ISO/IEC 18013‑5/-7; used alongside mVRC and mTR in the EUDI Wallet.

credentials:MSO (Mobile Security Object)
: A security object carrying metadata and the issuer’s signature over data elements in mdoc/mDL/mVRC.

credentials:mdoc
: The generic model and protocols for mobile documents per ISO/IEC 23220‑4.

credentials:Proximity flow
: Short‑range presentation protocol (NFC/BLE/Wi‑Fi Aware) per ISO/IEC 18013‑5/‑7.

credentials:Remote flow
: Remote presentation protocol (same‑device or cross‑device).

credentials:Trust anchor
: The root of trust (certificates/chain) required to verify an attestation’s signature.

credentials:IACA
: The issuing authority/CA used in the mDL/mVRC trust infrastructure under ISO (may be shared with mDL or set up separately).

credentials:CBOR (Concise Binary Object Representation)
: The binary serialisation format used for mdoc transfers.

credentials:CDDL (Concise Data Definition Language)
: The language to define CBOR structures (e.g., `tstr`, `uint`, `bstr`, `tdate`).

credentials:eCoC (electronic Certificate of Conformity)
: Manufacturer’s electronic certificate; selected entries are mapped into EU‑mVRC.

credentials:SD‑JWT VC (Selective Disclosure Java Web Token Verifiable Credential)
: A verifiable credential format based on Selective Disclosure JWT; one of the formats supported in EUDI for some attestations.

credentials:W3C VCDM v2.0 (W3C Verifiable Credentials Data Model v2.0)
: A family of specifications for VC data models.

credentials:OID4VCI (OpenID for Verifiable Credentials Issuance)
: OID4VCI is an open standard that defines a secure API for issuing Verifiable Credentials (VCs) to a user's digital wallet.

credentials:OID4VP (OpenID for Verifiable Presentation)
: OID4VP is a standard that defines how a user presents Verifiable Credentials from their wallet to a verifier.

credentials:HAIP (High Assurance Interoperability Profile)
: OpenID4VC profile aimed at higher assurance interoperability.

credentials:IANA JWT Claims (Internet Assigned Numbers Authority JSON Web Token Claims)
: IANA registry of standard JWT claim names.
protocols:Credential Offer
: Data structure created by a Credential Issuer to initiate issuer-initiated issuance, containing grant information and credential configuration references.

credentials:mVC (mobile Vehicle Certificate
: The family of mobile vehicle certificates defined in ISO/IEC 7367‑2, on which the EU‑mVRC is profiled.

credentials:mTR (mobile Technical Report)
: A mobile roadworthiness/inspection report (companion to mVRC/mDL) per ISO/IEC 7367‑3.

credentilas:mDL (mobile Driving Licence)
: The mobile driving licence per ISO/IEC 18013‑5/-7; used alongside mVRC and mTR in the EUDI Wallet.

credentials:MSO (Mobile Security Object)
: A security object carrying metadata and the issuer’s signature over data elements in mdoc/mDL/mVRC.

credentials:mdoc
: The generic model and protocols for mobile documents per ISO/IEC 23220‑4.

credentials:Proximity flow
: Short‑range presentation protocol (NFC/BLE/Wi‑Fi Aware) per ISO/IEC 18013‑5/‑7.

credentials:Remote flow
: Remote presentation protocol (same‑device or cross‑device).

credentials:Trust anchor
: The root of trust (certificates/chain) required to verify an attestation’s signature.

credentials:IACA
: The issuing authority/CA used in the mDL/mVRC trust infrastructure under ISO (may be shared with mDL or set up separately).

credentials:CBOR (Concise Binary Object Representation)
: The binary serialisation format used for mdoc transfers.

credentials:CDDL (Concise Data Definition Language)
: The language to define CBOR structures (e.g., `tstr`, `uint`, `bstr`, `tdate`).

credentials:eCoC (electronic Certificate of Conformity)
: Manufacturer’s electronic certificate; selected entries are mapped into EU‑mVRC.

credentials:SD‑JWT VC (Selective Disclosure Java Web Token Verifiable Credential)
: A verifiable credential format based on Selective Disclosure JWT; one of the formats supported in EUDI for some attestations.

credentials:W3C VCDM v2.0 (W3C Verifiable Credentials Data Model v2.0)
: A family of specifications for VC data models.

credentials:OID4VCI (OpenID for Verifiable Credentials Issuance)
: OID4VCI is an open standard that defines a secure API for issuing Verifiable Credentials (VCs) to a user's digital wallet.

credentials:OID4VP (OpenID for Verifiable Presentation)
: OID4VP is a standard that defines how a user presents Verifiable Credentials from their wallet to a verifier.

credentials:HAIP (High Assurance Interoperability Profile)
: OpenID4VC profile aimed at higher assurance interoperability.

credentials:IANA JWT Claims (Internet Assigned Numbers Authority JSON Web Token Claims)
: IANA registry of standard JWT claim names.
