```mermaid

---
config:
  layout: dagre
---
flowchart LR
 subgraph ECOSYSTEM["Ecosystem"]
    direction LR
        WP_BOX("Wallet Provider")
        IF_WP_W_BOX("WP to Wallet")
        WALLET_BOX("Wallet")
        IF_ISS_W_BOX("Issuer to Wallet")
        ISS_BOX("Credential Issuer")
        IF_W_RP_BOX("Wallet to RP")
        RP_BOX("Relying Party")
  end
  %% ── INTERFACE: Issuer to Wallet ──────────────────────────────
  subgraph IF_ISS_W_BOX["Issuer to Wallet"]
    direction LR
    OID4VCI("OpenID4VCI 1.0"):::published
    TS119472_3("TS 119 472-3\nEAA-PID issuance profiles"):::published
    ISO23220_3("ISO 23220-3\nInstallation and issuing protocols"):::draft
    CEN18098("CEN TS 18098\nUser onboarding"):::draft
    HAIP_I("HAIP 1.0\nHigh Assurance Interop Profile"):::published
    ClientAuth("OAuth Attestation-Based\nClient Auth"):::draft
    RFC6749_i("RFC 6749\nOAuth 2.0 Framework"):::published
  end

  %% ── INTERFACE: WP to Wallet ──────────────────────────────────
  subgraph IF_WP_W_BOX["WP to Wallet"]
    direction LR
    WP_W1("TS 119 476-3\nWallet Unit Attestation issuance"):::draft
  end

  %% ── WALLET / HOLDER ──────────────────────────────────────────
  subgraph WALLET_BOX["Wallet - Holder"]
    direction TB
    subgraph W_STORE["Credential Storage and Management"]
      direction LR
      TS119472_1("TS 119 472-1\nEAA general profiles"):::published
      ISO23220_1("ISO 23220-1\nGeneric eID architecture"):::published
      FIDO_CXF("FIDO CXF\nCredential Exchange Format"):::published
      FIDO_CEP("FIDO CEP\nCredential Exchange Protocol"):::draft
    end
    subgraph W_SIGN["Electronic Signatures"]
      direction LR
      CSC_API("CSC API v2.2\nRemote signature"):::published
      XADES("EN 319 132-1\nXAdES"):::published
      JADES("TS 119 182-1\nJAdES"):::published
      PADES("EN 319 142-1\nPAdES"):::published
    end
    subgraph W_ZKP["Selective Disclosure and ZKP"]
      direction LR
      TR119476("TR 119 476-1\nSD and ZKP feasibility"):::published
      RFC9901("RFC 9901 SD-JWT"):::published
      BBS("W3C Data Integrity BBS\nUnlinkable credentials"):::draft
    end
  end

  %% ── WALLET PROVIDER ──────────────────────────────────────────
  subgraph WP_BOX["Wallet Provider"]
    direction TB
    subgraph WUA["Wallet Unit Attestation"]
      direction LR
      TS119476_3("TS 119 476-3\nWUA and WIA"):::draft
      FIDO_CTAP("FIDO CTAP v2.2\nClient-to-Authenticator"):::published
      WebAuthn("W3C WebAuthn L2\nPseudonymisation"):::published
    end
    subgraph CRYPTO["Cryptographic Foundations"]
      direction LR
      TS119312("TS 119 312\nCrypto suites"):::published
      RFC7515("RFC 7515 JWS"):::published
      RFC7516("RFC 7516 JWE"):::published
      RFC7518("RFC 7518 JWA"):::published
      RFC9052("RFC 9052 COSE"):::published
      RFC8392("RFC 8392 CWT"):::published
      RFC8949("RFC 8949 CBOR"):::published
      RFC8610("RFC 8610 CDDL"):::published
    end
  end

  %% ── CREDENTIAL ISSUER ────────────────────────────────────────
  subgraph ISS_BOX["Credential Issuer"]
    direction TB
    subgraph FMT["Credential Formats"]
      direction LR
      SDJWTVC("SD-JWT-VC\nIETF draft-13"):::draft
      MDOC("ISO 18013-5\nmdoc - mDL"):::published
      MDOC_E2("ISO 18013-5 Ed2\nmdoc draft"):::draft
      VCDM("W3C VCDM v2.0"):::published
      ISO23220_2("ISO 23220-2\nData objects and encoding"):::published
      ISO7367("ISO 7367-2\nMobile vehicle cert - draft"):::draft
    end
    subgraph PROOF["Identity Proofing"]
      direction LR
      TS119461("TS 119 461 v2.1\nIdentity proofing"):::published
    end
  end

    %% ── INTERFACE: Wallet to RP ──────────────────────────────────
  subgraph IF_W_RP_BOX["Wallet to RP"]
    direction LR
    OID4VP("OpenID4VP 1.0"):::published
    TS119472_2("TS 119 472-2\nEAA-PID presentation profiles"):::published
    ISO18013_5("ISO 18013-5\nmDL proximity"):::published
    ISO18013_7("ISO 18013-7\nmDL online"):::published
    ISO23220_4("ISO 23220-4\nOperational phase protocols"):::draft
    DCAPI("W3C Digital Credentials API"):::draft
    HAIP_P("HAIP 1.0\nHigh Assurance Interop Profile"):::published
  end

    %% ── RELYING PARTY ────────────────────────────────────────────
  subgraph RP_BOX["Relying Party"]
    direction TB
    subgraph RP_AUTH["RP Authentication and Registration"]
      direction LR
      RFC6749("RFC 6749\nOAuth 2.0"):::published
      OIDConnect("OpenID Connect Core 1.0"):::published
      TS119411_8("TS 119 411-8\nAccess Cert Policy - RP"):::published
      OIDConnect_RP("OpenID Connect\nRP Metadata Choices"):::draft
    end
    subgraph VAL["Credential Validation"]
      direction LR
      VCDI("W3C VCDI 1.0\nData Integrity"):::published
      SecVC("W3C Securing VC\nJOSE and COSE"):::published
      RFC7519("RFC 7519 JWT"):::published
      EdDSA("W3C Data Integrity EdDSA"):::published
      ECDSA("W3C Data Integrity ECDSA"):::published
      RFC5280_v("RFC 5280 X.509"):::published
      TSL_v("Token Status List"):::draft
      BSL_v("Bitstring Status List"):::published
    end
  end

 subgraph TRUST_BOX["Trust Architecture"]
    direction TB
        TL_BOX("Trusted Lists")
        CERT_BOX("Certificate Profiles and TSP Policy")
        FED_BOX("Federation and Access Rights")
        REVOC_BOX("Status and Revocation")
  end
    WP_BOX --> IF_WP_W_BOX
    IF_WP_W_BOX --> WALLET_BOX
    ISS_BOX --> IF_ISS_W_BOX
    IF_ISS_W_BOX --> WALLET_BOX
    WALLET_BOX --> IF_W_RP_BOX
    IF_W_RP_BOX --> RP_BOX

     WP_BOX:::wp
     IF_WP_W_BOX:::iface
     WALLET_BOX:::wallet
     IF_ISS_W_BOX:::iface
     ISS_BOX:::iss
     IF_W_RP_BOX:::iface
     RP_BOX:::rp
     TL_BOX:::trust
     CERT_BOX:::trust
     FED_BOX:::trust
     REVOC_BOX:::trust
    classDef wp fill:#eaf5e8,stroke:#1a6b3c,stroke-width:2px,color:#0f2540
    classDef wallet fill:#f3eeff,stroke:#6a3daa,stroke-width:2px,color:#0f2540
    classDef iss fill:#fffae8,stroke:#b07d00,stroke-width:2px,color:#0f2540
    classDef rp fill:#fff0f0,stroke:#aa3d3d,stroke-width:2px,color:#0f2540
    classDef iface fill:#f0ebff,stroke:#7a50cc,stroke-width:2px,stroke-dasharray:6,color:#3d1a80
    classDef trust fill:#d0e4f7,stroke:#2e6da4,stroke-width:1px,color:#0f2540
    style TRUST_BOX fill:#e8f0fb,stroke:#2e6da4,stroke-width:3px,color:#0f2540
    style ECOSYSTEM fill:#f8f8f8,stroke:#cccccc,stroke-width:1px,color:#333

  %% ── CLICK LINKS ──────────────────────────────────────────────
  click TS119476_3 href "https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/issues/500" _blank
  click FIDO_CTAP href "https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html" _blank
  click WebAuthn href "https://www.w3.org/TR/webauthn-2/" _blank
  click TS119312 href "https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.05.01_60/ts_119312v010501p.pdf" _blank
  click RFC7515 href "https://www.rfc-editor.org/rfc/rfc7515" _blank
  click RFC7516 href "https://datatracker.ietf.org/doc/rfc7516/" _blank
  click RFC7518 href "https://datatracker.ietf.org/doc/rfc7518/" _blank
  click RFC9052 href "https://www.rfc-editor.org/rfc/rfc9052" _blank
  click RFC8392 href "https://datatracker.ietf.org/doc/html/rfc8392" _blank
  click RFC8949 href "https://datatracker.ietf.org/doc/html/rfc8949" _blank
  click RFC8610 href "https://www.rfc-editor.org/rfc/rfc8610.html" _blank
  click TS119472_1 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/11947201/01.01.01_60/ts_11947201v010101p.pdf" _blank
  click FIDO_CXF href "https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html" _blank
  click CSC_API href "https://cloudsignatureconsortium.org/resources/csc-api-v2-2/" _blank
  click XADES href "https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf" _blank
  click JADES href "https://www.etsi.org/deliver/etsi_ts/119100_119199/11918201/01.02.01_60/ts_11918201v010201p.pdf" _blank
  click PADES href "https://www.etsi.org/deliver/etsi_en/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf" _blank
  click RFC9901 href "https://datatracker.ietf.org/doc/rfc9901" _blank
  click BBS href "https://www.w3.org/TR/vc-di-bbs/" _blank
  click OID4VCI href "https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html" _blank
  click TS119472_3 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/11947203/01.01.01_60/ts_11947203v010101p.pdf" _blank
  click HAIP_I href "https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-05.html" _blank
  click ClientAuth href "https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/" _blank
  click RFC6749_i href "https://datatracker.ietf.org/doc/html/rfc6749" _blank
  click SDJWTVC href "https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/" _blank
  click MDOC href "https://www.iso.org/standard/69084.html" _blank
  click VCDM href "https://www.w3.org/TR/vc-data-model-2.0/" _blank
  click ISO23220_2 href "https://www.iso.org/standard/86785.html" _blank
  click TS119461 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/119461/02.01.01_60/ts_119461v020101p.pdf" _blank
  click OID4VP href "https://openid.net/specs/openid-4-verifiable-presentations-1_0.html" _blank
  click TS119472_2 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/11947202/01.01.01_60/ts_11947202v010101p.pdf" _blank
  click ISO18013_5 href "https://www.iso.org/standard/69084.html" _blank
  click ISO18013_7 href "https://www.iso.org/standard/86785.html" _blank
  click DCAPI href "https://www.w3.org/TR/digital-credentials/" _blank
  click HAIP_P href "https://openid.net/specs/openid4vc-high-assurance-interoperability-profile-1_0-05.html" _blank
  click RFC6749 href "https://datatracker.ietf.org/doc/html/rfc6749" _blank
  click OIDConnect href "https://openid.net/specs/openid-connect-core-1_0.html" _blank
  click TS119411_8 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/11941108/01.01.01_60/ts_11941108v010101p.pdf" _blank
  click VCDI href "https://www.w3.org/TR/vc-data-integrity/" _blank
  click SecVC href "https://www.w3.org/TR/vc-jose-cose/" _blank
  click RFC7519 href "https://datatracker.ietf.org/doc/html/rfc7519" _blank
  click EdDSA href "https://www.w3.org/TR/vc-di-eddsa/" _blank
  click ECDSA href "https://www.w3.org/TR/vc-di-ecdsa/" _blank
  click RFC5280_v href "https://datatracker.ietf.org/doc/html/rfc5280" _blank
  click TSL_v href "https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/" _blank
  click BSL_v href "https://www.w3.org/TR/vc-bitstring-status-list/" _blank
  click TS119602 href "https://www.etsi.org/deliver/etsi_ts/119600_119699/119602/01.01.01_60/ts_119602v010101p.pdf" _blank
  click TS119612 href "https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf" _blank
  click TS119615 href "https://www.etsi.org/deliver/etsi_ts/119600_119699/119615/01.03.01_60/ts_119615v010301p.pdf" _blank
  click EN319411_1 href "https://www.etsi.org/deliver/etsi_en/319400_319499/31941101/01.05.01_60/en_31941101v010501p.pdf" _blank
  click EN319412_1 href "https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.06.01_60/en_31941201v010601p.pdf" _blank
  click EN319412_2 href "https://www.etsi.org/deliver/etsi_en/319400_319499/31941202/02.04.01_60/en_31941202v020401p.pdf" _blank
  click TS119412_6 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/11941206/01.01.01_60/ts_11941206v010101p.pdf" _blank
  click RFC6960 href "https://datatracker.ietf.org/doc/html/rfc6960" _blank
  click RFC9162 href "https://datatracker.ietf.org/doc/html/rfc9162" _blank
  click OIDFed href "https://openid.net/specs/openid-federation-1_0.html" _blank
  click OIDFedWallet href "https://openid.github.io/federation-wallet/main.html" _blank
  click TS119475 href "https://www.etsi.org/deliver/etsi_ts/119400_119499/119475/01.01.01_60/ts_119475v010101p.pdf" _blank
  click TSL_t href "https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/" _blank
  click BSL_t href "https://www.w3.org/TR/vc-bitstring-status-list/" _blank

  subgraph LEGEND["Legend"]
    direction LR
    L1("Published standard"):::published
    L2("Draft standard"):::draft
    L3("Interface protocol\nbetween actors"):::iface
  end

  %% ── STYLES ───────────────────────────────────────────────────
  classDef published fill:#1a6b3c,color:#fff,stroke:#0f4a2a
  classDef draft fill:#b07d00,color:#fff,stroke:#7a5600

  style WP_BOX fill:#eaf5e8,stroke:#1a6b3c,stroke-width:2px,color:#0f2540
  style WUA fill:#d4ecd0,stroke:#1a6b3c,stroke-width:1px,color:#0f2540
  style CRYPTO fill:#d4ecd0,stroke:#1a6b3c,stroke-width:1px,color:#0f2540

  style IF_WP_W_BOX fill:#f0ebff,stroke:#7a50cc,stroke-width:2px,stroke-dasharray:6,color:#3d1a80
  style IF_ISS_W_BOX fill:#f0ebff,stroke:#7a50cc,stroke-width:2px,stroke-dasharray:6,color:#3d1a80
  style IF_W_RP_BOX fill:#f0ebff,stroke:#7a50cc,stroke-width:2px,stroke-dasharray:6,color:#3d1a80

  style WALLET_BOX fill:#f3eeff,stroke:#6a3daa,stroke-width:2px,color:#0f2540
  style W_STORE fill:#e4d8ff,stroke:#6a3daa,stroke-width:1px,color:#0f2540
  style W_SIGN fill:#e4d8ff,stroke:#6a3daa,stroke-width:1px,color:#0f2540
  style W_ZKP fill:#e4d8ff,stroke:#6a3daa,stroke-width:1px,color:#0f2540

  style ISS_BOX fill:#fffae8,stroke:#b07d00,stroke-width:2px,color:#0f2540
  style FMT fill:#f5eccc,stroke:#b07d00,stroke-width:1px,color:#0f2540
  style PROOF fill:#f5eccc,stroke:#b07d00,stroke-width:1px,color:#0f2540

  style RP_BOX fill:#fff0f0,stroke:#aa3d3d,stroke-width:2px,color:#0f2540
  style RP_AUTH fill:#ffd8d8,stroke:#aa3d3d,stroke-width:1px,color:#0f2540
  style VAL fill:#ffd8d8,stroke:#aa3d3d,stroke-width:1px,color:#0f2540

  style TRUST_BOX fill:#e8f0fb,stroke:#2e6da4,stroke-width:3px,color:#0f2540
  style TL_BOX fill:#d0e4f7,stroke:#2e6da4,stroke-width:1px,color:#0f2540
  style CERT_BOX fill:#d0e4f7,stroke:#2e6da4,stroke-width:1px,color:#0f2540
  style FED_BOX fill:#d0e4f7,stroke:#2e6da4,stroke-width:1px,color:#0f2540
  style REVOC_BOX fill:#d0e4f7,stroke:#2e6da4,stroke-width:1px,color:#0f2540