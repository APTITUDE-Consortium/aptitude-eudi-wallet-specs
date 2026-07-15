#!/usr/bin/env python3
"""Replace glossary terms with ezglossary <section:term> link syntax in RFC files.

Also removes Section 3.1 Terminology from each RFC.
"""
import re
import sys

# Terms ordered by descending search-pattern length to prevent partial matches.
# Each entry: (regex_pattern, replacement, table_replacement)
# table_replacement has | escaped to \| for use inside markdown table rows.
TERMS = [
    # === Full forms with abbreviation in parentheses (longest first) ===
    (r'\bQualified Electronic Attestation of Attributes \(QEAA\)',
     '<credentials:Qualified Electronic Attestation of Attributes (QEAA)>',
     '<credentials:Qualified Electronic Attestation of Attributes (QEAA)>'),
    (r'\bElectronic Attestation of Attributes \(EAA\)',
     '<credentials:Electronic Attestation of Attributes (EAA)>',
     '<credentials:Electronic Attestation of Attributes (EAA)>'),
    (r'\bPerson Identification Data \(PID\)',
     '<credentials:Person Identification Data (PID)>',
     '<credentials:Person Identification Data (PID)>'),
    (r'\bWallet Unit Attestation \(WUA\)',
     '<components:Wallet Unit Attestation (WUA)>',
     '<components:Wallet Unit Attestation (WUA)>'),
    (r'\bWallet Instance Attestation \(WIA\)',
     '<components:Wallet Instance Attestation (WIA)>',
     '<components:Wallet Instance Attestation (WIA)>'),
    (r'\bPushed Authorisation Request \(PAR\)',
     '<protocols:Pushed Authorisation Request (PAR)>',
     '<protocols:Pushed Authorisation Request (PAR)>'),

    # === Multi-word compound terms (longest first) ===
    # "Wallet Unit Attestation" / "Wallet Instance Attestation" without the abbreviation
    (r'\bWallet Unit Attestations\b',
     '<components:Wallet Unit Attestation (WUA)|Wallet Unit Attestations>',
     r'<components:Wallet Unit Attestation (WUA)\|Wallet Unit Attestations>'),
    (r'\bWallet Unit Attestation\b',
     '<components:Wallet Unit Attestation (WUA)|Wallet Unit Attestation>',
     r'<components:Wallet Unit Attestation (WUA)\|Wallet Unit Attestation>'),
    (r'\bWallet Instance Attestations\b',
     '<components:Wallet Instance Attestation (WIA)|Wallet Instance Attestations>',
     r'<components:Wallet Instance Attestation (WIA)\|Wallet Instance Attestations>'),
    (r'\bWallet Instance Attestation\b',
     '<components:Wallet Instance Attestation (WIA)|Wallet Instance Attestation>',
     r'<components:Wallet Instance Attestation (WIA)\|Wallet Instance Attestation>'),

    # Multi-word role/component terms
    (r'\bAttestation Providers\b',
     '<roles:Attestation Provider (AP)|Attestation Providers>',
     r'<roles:Attestation Provider (AP)\|Attestation Providers>'),
    (r'\bAttestation Provider\b',
     '<roles:Attestation Provider (AP)|Attestation Provider>',
     r'<roles:Attestation Provider (AP)\|Attestation Provider>'),
    (r'\bAuthorisation Servers\b',
     '<components:Authorisation Server|Authorisation Servers>',
     r'<components:Authorisation Server\|Authorisation Servers>'),
    (r'\bAuthorisation Server\b',
     '<components:Authorisation Server>',
     '<components:Authorisation Server>'),
    (r'\bRelying Party Backends\b',
     '<components:Relying Party Backend|Relying Party Backends>',
     r'<components:Relying Party Backend\|Relying Party Backends>'),
    (r'\bRelying Party Backend\b',
     '<components:Relying Party Backend>',
     '<components:Relying Party Backend>'),
    (r'\bRelying Party Instances\b',
     '<components:Relying Party Instance|Relying Party Instances>',
     r'<components:Relying Party Instance\|Relying Party Instances>'),
    (r'\bRelying Party Instance\b',
     '<components:Relying Party Instance>',
     '<components:Relying Party Instance>'),
    (r'\bWallet Providers\b',
     '<roles:Wallet Provider (WP)|Wallet Providers>',
     r'<roles:Wallet Provider (WP)\|Wallet Providers>'),
    (r'\bWallet Provider\b',
     '<roles:Wallet Provider (WP)>',
     '<roles:Wallet Provider (WP)>'),
    (r'\bWallet Solutions\b',
     '<components:Wallet Solution|Wallet Solutions>',
     r'<components:Wallet Solution\|Wallet Solutions>'),
    (r'\bWallet Solution\b',
     '<components:Wallet Solution>',
     '<components:Wallet Solution>'),
    (r'\bEUDI Wallets\b',
     '<components:EUDI Wallet|EUDI Wallets>',
     r'<components:EUDI Wallet\|EUDI Wallets>'),
    (r'\bEUDI Wallet\b',
     '<components:EUDI Wallet>',
     '<components:EUDI Wallet>'),
    (r'\bWallet Units\b',
     '<components:Wallet Unit|Wallet Units>',
     r'<components:Wallet Unit\|Wallet Units>'),
    (r'\bWallet Unit\b',
     '<components:Wallet Unit>',
     '<components:Wallet Unit>'),
    (r'\bWallet Instances\b',
     '<components:Wallet Instance|Wallet Instances>',
     r'<components:Wallet Instance\|Wallet Instances>'),
    (r'\bWallet Instance\b',
     '<components:Wallet Instance>',
     '<components:Wallet Instance>'),

    # Multi-word protocol/credential terms
    (r'\bSelective Disclosure\b',
     '<processes:Selective Disclosure>',
     '<processes:Selective Disclosure>'),
    (r'\bCredential Offers\b',
     '<artifacts:Credential Offer|Credential Offers>',
     r'<artifacts:Credential Offer\|Credential Offers>'),
    (r'\bCredential Offer\b',
     '<artifacts:Credential Offer>',
     '<artifacts:Credential Offer>'),
    (r'\bRequest Objects\b',
     '<protocols:Request Object|Request Objects>',
     r'<protocols:Request Object\|Request Objects>'),
    (r'\bRequest Object\b',
     '<protocols:Request Object>',
     '<protocols:Request Object>'),
    (r'\bPresentation Requests\b',
     '<artifacts:Presentation Request|Presentation Requests>',
     r'<artifacts:Presentation Request\|Presentation Requests>'),
    (r'\bPresentation Request\b',
     '<artifacts:Presentation Request>',
     '<artifacts:Presentation Request>'),

    # Hyphenated protocol terms
    (r'\bProof-of-possession\b',
     '<processes:Proof of Possession>',
     '<processes:Proof of Possession>'),
    (r'\bproof-of-possession\b',
     '<processes:Proof of Possession|proof-of-possession>',
     r'<processes:Proof of Possession\|proof-of-possession>'),
    (r'\bKey binding\b',
     '<processes:Key Binding>',
     '<processes:Key Binding>'),
    (r'\bkey binding\b',
     '<processes:Key Binding|key binding>',
     r'<processes:Key Binding\|key binding>'),
    (r'\bDevice binding\b',
     '<processes:Device Binding>',
     '<processes:Device Binding>'),
    (r'\bdevice binding\b',
     '<processes:Device Binding|device binding>',
     r'<processes:Device Binding\|device binding>'),

    (r'\bSessionTranscript\b',
     '<protocols:SessionTranscript>',
     '<protocols:SessionTranscript>'),
    (r'\bDeviceResponse\b',
     '<protocols:DeviceResponse>',
     '<protocols:DeviceResponse>'),

    # === Single-word terms ===
    (r'\bUsers\b',
     '<roles:User|Users>',
     r'<roles:User\|Users>'),
    (r'\bUser\b',
     '<roles:User>',
     '<roles:User>'),
    (r'\bDPoP\b',
     '<protocols:DPoP>',
     '<protocols:DPoP>'),
    (r'\bPKCE\b',
     '<protocols:PKCE>',
     '<protocols:PKCE>'),
    (r'\bWUAs?\b',
     '<components:Wallet Unit Attestation (WUA)|WUA>',
     r'<components:Wallet Unit Attestation (WUA)\|WUA>'),
    (r'\bWIAs?\b',
     '<components:Wallet Instance Attestation (WIA)|WIA>',
     r'<components:Wallet Instance Attestation (WIA)\|WIA>'),

    # Nonce — only standalone, not inside c_nonce or identifiers
    (r'\bNonces\b',
     '<artifacts:Nonce|Nonces>',
     r'<artifacts:Nonce\|Nonces>'),
    (r'(?<![_`])\bNonce\b(?![_`])',
     '<artifacts:Nonce>',
     '<artifacts:Nonce>'),
    (r'\bnonces\b',
     '<artifacts:Nonce|nonces>',
     r'<artifacts:Nonce\|nonces>'),
    (r'(?<![_`c])\bnonce\b(?![_`s])',
     '<artifacts:Nonce|nonce>',
     r'<artifacts:Nonce\|nonce>'),

    # Namespace
    (r'\bNamespaces\b',
     '<data-elements:Namespace|Namespaces>',
     r'<data-elements:Namespace\|Namespaces>'),
    (r'\bNamespace\b',
     '<data-elements:Namespace>',
     '<data-elements:Namespace>'),
    (r'\bnamespaces\b',
     '<data-elements:Namespace|namespaces>',
     r'<data-elements:Namespace\|namespaces>'),
    (r'\bnamespace\b',
     '<data-elements:Namespace|namespace>',
     r'<data-elements:Namespace\|namespace>'),

    # Provider of WRPAC
    (r'\bProvider of Wallet Relying Party Access Certificate \(Provider of WRPAC\)',
     '<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)>',
     r'<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)>'),
    (r'\bProvider of Wallet Relying Party Access Certificate\b',
     '<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)|Provider of Wallet Relying Party Access Certificate>',
     r'<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)\|Provider of Wallet Relying Party Access Certificate>'),
    (r'\bProvider of WRPAC\b',
     '<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)|Provider of WRPAC>',
     r'<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)\|Provider of WRPAC>'),
    (r'\bProvider of WRPACs\b',
     '<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)|Provider of WRPACs>',
     r'<roles:Provider of Wallet Relying Party Access Certificate (Provider of WRPAC)\|Provider of WRPACs>'),

    # Provider of WRPRC
    (r'\bProvider of Wallet Relying Party Registration Certificate \(Provider of WRPRC\)',
     '<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)>',
     r'<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)>'),
    (r'\bProvider of Wallet Relying Party Registration Certificate\b',
     '<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)|Provider of Wallet Relying Party Registration Certificate>',
     r'<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)\|Provider of Wallet Relying Party Registration Certificate>'),
    (r'\bProvider of WRPRC\b',
     '<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)|Provider of WRPRC>',
     r'<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)\|Provider of WRPRC>'),
    (r'\bProvider of WRPRCs\b',
     '<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)|Provider of WRPRCs>',
     r'<roles:Provider of Wallet Relying Party Registration Certificate (Provider of WRPRC)\|Provider of WRPRCs>'),

    # PuB-EAA Provider
    (r'\bPuB-EAA Provider\b',
     '<roles:PuB-EAA Provider>',
     r'<roles:PuB-EAA Provider>'),
    (r'\bPuB-EAA Providers\b',
     '<roles:PuB-EAA Provider|PuB-EAA Providers>',
     r'<roles:PuB-EAA Provider\|PuB-EAA Providers>'),

    # PuB-EAA Provider
    (r'\bQEAA Provider\b',
     '<roles:QEAA Provider>',
     r'<roles:QEAA Provider>'),
    (r'\bQEAA Providers\b',
     '<roles:QEAA Provider|QEAA Providers>',
     r'<roles:QEAA Provider\|QEAA Providers>'),

    # PuB-EAA Provider
    (r'\bQEAA Provider\b',
     '<roles:QEAA Provider>',
     r'<roles:QEAA Provider>'),
    (r'\bQEAA Providers\b',
     '<roles:QEAA Provider|QEAA Providers>',
     r'<roles:QEAA Provider\|QEAA Providers>'),

    # Relying Party Intermediary (RPI)
    (r'\bRelying Party Intermediary\b',
     '<roles:Relying Party Intermediary (RPI)|Relying Party Intermediary>',
     r'<roles:Relying Party Intermediary (RPI)\|Relying Party Intermediary>'),
    (r'\bRelying Party Intermediaries\b',
     '<roles:Relying Party Intermediary (RPI)|Relying Party Intermediaries>',
     r'<roles:Relying Party Intermediary (RPI)\|Relying Party Intermediaries>'),

    # Registrar
    (r'\bRegistrar\b',
     '<roles:Registrar>',
     r'<roles:Registrar>'),
    (r'\bRegistrars\b',
     '<roles:Registrar|Registrars>',
     r'<roles:Registrar\|Registrars>'),

    # Trusted Entity
    (r'\bTrusted Entity\b',
     '<roles:Trusted Entity>',
     r'<roles:Trusted Entity>'),
    (r'\bTrusted Entities\b',
     '<roles:Trusted Entity|Trusted Entities>',
     r'<roles:Trusted Entity\|Trusted Entities>'),

    # Catalogue of Attributes
    (r'\bCatalogue of Attributes\b',
     '<artifacts:Catalogue of Attributes>',
     r'<artifacts:Catalogue of Attributes>'),
    (r'\bCatalogues of Attributes\b',
     '<artifacts:Catalogue of Attributes|Catalogues of Attributes>',
     r'<artifacts:Catalogue of Attributes\|Catalogues of Attributes>'),

    # Catalogue of Schemes for the Attestation of Attributes
    (r'\bCatalogue of Schemes for the Attestation of Attributes\b',
     '<artifacts:Catalogue of Schemes for the Attestation of Attributes>',
     r'<artifacts:Catalogue of Schemes for the Attestation of Attributes>'),
    (r'\bCatalogues of Schemes for the Attestation of Attributes\b',
     '<artifacts:Catalogue of Schemes for the Attestation of Attributes|Catalogues of Schemes for the Attestation of Attributes>',
     r'<artifacts:Catalogue of Schemes for the Attestation of Attributes\|Catalogues of Schemes for the Attestation of Attributes>'),

    # Official Journal of the European Union (OJEU)
    (r'\bOfficial Journal of the European Union \(OJEU\)',
     '<artifacts:Official Journal of the European Union (OJEU)>',
     r'<artifacts:Official Journal of the European Union (OJEU)>'),
    (r'\bOfficial Journal of the European Union\b',
     '<artifacts:Official Journal of the European Union (OJEU)|Official Journal of the European Union>',
     r'<artifacts:Official Journal of the European Union (OJEU)\|Official Journal of the European Union>'),
    (r'\bOJEU\b',
     '<artifacts:Official Journal of the European Union (OJEU)|OJEU>',
     r'<artifacts:Official Journal of the European Union (OJEU)\|OJEU>'),

    # Embedded Disclosure Policy (EDP)
    (r'\bEmbedded Disclosure Policy \(EDP\)',
     '<artifacts:Embedded Disclosure Policy (EDP)>',
     r'<artifacts:Embedded Disclosure Policy (EDP)>'),
    (r'\bEmbedded Disclosure Policy\b',
     '<artifacts:Embedded Disclosure Policy (EDP)|Embedded Disclosure Policy>',
     r'<artifacts:Embedded Disclosure Policy (EDP)\|Embedded Disclosure Policy>'),
    (r'\bEmbedded Disclosure Policies\b',
     '<artifacts:Embedded Disclosure Policy (EDP)|Embedded Disclosure Policies>',
     r'<artifacts:Embedded Disclosure Policy (EDP)\|Embedded Disclosure Policies>'),
    (r'\bEDP\b',
     '<artifacts:Embedded Disclosure Policy (EDP)|EDP>',
     r'<artifacts:Embedded Disclosure Policy (EDP)\|EDP>'),

    # Entitlement
    (r'\bEntitlement\b',
     '<data-elements:Entitlement>',
     r'<data-elements:Entitlement>'),
    (r'\bEntitlements\b',
     '<data-elements:Entitlement|Entitlements>',
     r'<data-elements:Entitlement\|Entitlements>'),

    # EU Member State Trusted List (EUMS TL)
    (r'\bEU Member State Trusted List \(EUMS TL\)',
     '<artifacts:EU Member State Trusted List (EUMS TL)>',
     r'<artifacts:EU Member State Trusted List (EUMS TL)>'),
    (r'\bEU Member State Trusted List\b',
     '<artifacts:EU Member State Trusted List (EUMS TL)|EU Member State Trusted List>',
     r'<artifacts:EU Member State Trusted List (EUMS TL)\|EU Member State Trusted List>'),
    (r'\bEU Member State Trusted Lists\b',
     '<artifacts:EU Member State Trusted List (EUMS TL)|EU Member State Trusted Lists>',
     r'<artifacts:EU Member State Trusted List (EUMS TL)\|EU Member State Trusted Lists>'),
    (r'\bEUMS TL\b',
     '<artifacts:EU Member State Trusted List (EUMS TL)|EUMS TL>',
     r'<artifacts:EU Member State Trusted List (EUMS TL)\|EUMS TL>'),

    # List of Trusted Entities (LoTE)
    (r'\bList of Trusted Entities \(LoTE\)',
     '<artifacts:List of Trusted Entities (LoTE)>',
     r'<artifacts:List of Trusted Entities (LoTE)>'),
    (r'\bList of Trusted Entities\b',
     '<artifacts:List of Trusted Entities (LoTE)|List of Trusted Entities>',
     r'<artifacts:List of Trusted Entities (LoTE)\|List of Trusted Entities>'),
    (r'\bLists of Trusted Entities\b',
     '<artifacts:List of Trusted Entities (LoTE)|Lists of Trusted Entities>',
     r'<artifacts:List of Trusted Entities (LoTE)\|Lists of Trusted Entities>'),
    (r'\bL[oO]TE\b',
     '<artifacts:List of Trusted Entities (LoTE)|LoTE>',
     r'<artifacts:List of Trusted Entities (LoTE)\|LoTE>'),

    # List Of Trusted Lists (LOTL)
    (r'\bList Of Trusted Lists \(LOTL\)',
     '<artifacts:List Of Trusted Lists (LOTL)>',
     r'<artifacts:List Of Trusted Lists (LOTL)>'),
    (r'\bList Of Trusted Lists\b',
     '<artifacts:List Of Trusted Lists (LOTL)|List Of Trusted Lists>',
     r'<artifacts:List Of Trusted Lists (LOTL)\|List Of Trusted Lists>'),
    (r'\bLists Of Trusted Lists\b',
     '<artifacts:List Of Trusted Lists (LOTL)|Lists Of Trusted Lists>',
     r'<artifacts:List Of Trusted Lists (LOTL)\|Lists Of Trusted Lists>'),
    (r'\bL[oO]TL\b',
     '<artifacts:List Of Trusted Lists (LOTL)|LOTL>',
     r'<artifacts:List Of Trusted Lists (LOTL)\|LOTL>'),

    # Register
    (r'\bRegister\b',
     '<components:Register>',
     r'<components:Register>'),
    (r'\bRegisters\b',
     '<components:Register|Registers>',
     r'<components:Register\|Registers>'),

    # Scheme for the Attestation of Attributes
    (r'\bScheme for the Attestation of Attributes\b',
     '<artifacts:Scheme for the Attestation of Attributes>',
     r'<artifacts:Scheme for the Attestation of Attributes>'),
    (r'\bSchemes for the Attestation of Attributes\b',
     '<artifacts:Scheme for the Attestation of Attributes|Schemes for the Attestation of Attributes>',
     r'<artifacts:Scheme for the Attestation of Attributes\|Schemes for the Attestation of Attributes>'),

    # Trusted List (TL)
    (r'\bTrusted List \(TL\)',
     '<artifacts:Trusted List (TL)>',
     r'<artifacts:Trusted List (TL)>'),
    (r'\bTrusted List\b',
     '<artifacts:Trusted List (TL)|Trusted List>',
     r'<artifacts:Trusted List (TL)\|Trusted List>'),
    (r'\bTrusted Lists\b',
     '<artifacts:Trusted List (TL)|Trusted Lists>',
     r'<artifacts:Trusted List (TL)\|Trusted Lists>'),
    (r'\bTL\b',
     '<artifacts:Trusted List (TL)|TL>',
     r'<artifacts:Trusted List (TL)\|TL>'),
    (r'\bTLs\b',
     '<artifacts:Trusted List (TL)|TLs>',
     r'<artifacts:Trusted List (TL)\|TLs>'),

    # Wallet-Relying Party Access Certificate (WRPAC)
    (r'\bWallet[\-\s]Relying Party Access Certificate \(WRPAC\)',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)>'),
    (r'\bWallet[\-\s]Relying Party Access Certificates \(WRPACs\)',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)|Wallet-Relying Party Access Certificates (WRPACs)>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)\|Wallet-Relying Party Access Certificates (WRPACs)>'),
    (r'\bWallet[\-\s]Relying Party Access Certificate\b',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)|Wallet-Relying Party Access Certificate>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)\|Wallet-Relying Party Access Certificate>'),
    (r'\bWallet[\-\s]Relying Party Access Certificates\b',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)|Wallet-Relying Party Access Certificates>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)\|Wallet-Relying Party Access Certificates>'),
    (r'\bWRPAC\b',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)|WRPAC>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)\|WRPAC>'),
    (r'\bWRPACs\b',
     '<artifacts:Wallet-Relying Party Access Certificate (WRPAC)|WRPACs>',
     r'<artifacts:Wallet-Relying Party Access Certificate (WRPAC)\|WRPACs>'),

    # Wallet-Relying Party Registration Certificate (WRPRC)
    (r'\bWallet[\-\s]Relying Party Registration Certificate \(WRPRC\)',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)>'),
    (r'\bWallet[\-\s]Relying Party Registration Certificates \(WRPRCs\)',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|Wallet-Relying Party Registration Certificates (WRPRCs)>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|Wallet-Relying Party Registration Certificates (WRPRCs)>'),
    (r'\bWallet[\-\s]Relying Party Registration Certificate\b',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|Wallet-Relying Party Registration Certificate>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|Wallet-Relying Party Registration Certificate>'),
    (r'\bWallet[\-\s]Relying Party Registration Certificates\b',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|Wallet-Relying Party Registration Certificates>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|Wallet-Relying Party Registration Certificates>'),
    (r'\bWRPRC\b',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|WRPRC>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|WRPRC>'),
    (r'\bWRPRCs\b',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|WRPRCs>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|WRPRCs>'),

    # Selective Disclosure JWT (SD-JWT)
    (r'\bSelective Disclosure JWT \(SD-JWT\)',
     '<formats:Selective Disclosure JWT (SD-JWT)>',
     r'<formats:Selective Disclosure JWT (SD-JWT)>'),
    (r'\bSelective Disclosure JWT\b',
     '<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)|Selective Disclosure JWT>',
     r'<artifacts:Wallet-Relying Party Registration Certificate (WRPRC)\|Selective Disclosure JWT>'),
    (r'\bSD-JWT\b',
     '<formats:Selective Disclosure JWT (SD-JWT)|SD-JWT>',
     r'<formats:Selective Disclosure JWT (SD-JWT)\|SD-JWT>'),
]


def replace_outside_protected(text, pattern, replacement):
    """Apply regex replacement only outside <...> tags and `...` inline code."""
    # Split on: angle-bracket tags (ezglossary links, HTML) and backtick inline code
    segments = re.split(r'(<[^>]+>|`[^`]+`|\[[^\]]*\]\([^)]*\))', text)
    for i, seg in enumerate(segments):
        # Only process unprotected segments (not tags, code, or links)
        if not (seg.startswith('<') or seg.startswith('`') or seg.startswith('[')):
            segments[i] = re.sub(pattern, replacement, seg)
    return ''.join(segments)


def is_heading(line):
    """Lines starting with # are headings."""
    return line.lstrip().startswith('#')


def is_toc_link(line):
    """ToC entries like '- [text](#anchor)' or '  - [text](#anchor)'."""
    return bool(re.match(r'\s*-\s*\[.*\]\(#', line))


def is_separator(line):
    return line.strip() == '---'


def is_table_sep(line):
    """Table header separator row: | --- | --- |"""
    return bool(re.match(r'\s*\|[\s\-:|]+\|\s*$', line))


def is_table_row(line):
    s = line.strip()
    return s.startswith('|') and s.endswith('|')


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result = []
    in_code_block = False
    in_references = False
    skip_terminology = False  # True when inside Section 3.1 Terminology

    for line in lines:
        # --- Track fenced code blocks ---
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if in_code_block:
            result.append(line)
            continue

        # --- Detect and remove Section 3.1 Terminology ---
        if re.match(r'^###\s+\*\*3\.1\s+Terminology\*\*', stripped):
            skip_terminology = True
            continue
        if skip_terminology:
            # Stop skipping at the next --- separator or ## heading
            if is_separator(line) or re.match(r'^##\s', stripped):
                skip_terminology = False
                result.append(line)
            # Otherwise skip the line (paragraph text, blank lines)
            continue

        # --- Detect References section (no replacements after this) ---
        if re.match(r'^##\s.*\bReferences\b', stripped):
            in_references = True
        if in_references and stripped.startswith('#'):
            in_references = False
        if in_references:
            result.append(line)
            continue

        # --- Skip heading lines ---
        if is_heading(line):
            result.append(line)
            continue

        # --- Skip ToC anchor links ---
        if is_toc_link(line):
            result.append(line)
            continue

        # --- Skip separator lines and table-header separators ---
        if is_separator(line) or is_table_sep(line):
            result.append(line)
            continue

        # --- Apply term replacements ---
        is_tbl = is_table_row(line)
        for pattern, repl, table_repl in TERMS:
            r = table_repl if is_tbl else repl
            line = replace_outside_protected(line, pattern, r)

        result.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ezglossary_replace.py <file1.md> [file2.md ...]")
        sys.exit(1)
    for fp in sys.argv[1:]:
        print(f"Processing {fp} ...")
        process_file(fp)
        print(f"  Done: {fp}")
