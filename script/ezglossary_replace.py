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
    (r'\bCredential Issuers\b',
     '<roles:Credential Issuer|Credential Issuers>',
     r'<roles:Credential Issuer\|Credential Issuers>'),
    (r'\bCredential Issuer\b',
     '<roles:Credential Issuer>',
     '<roles:Credential Issuer>'),
    (r'\bAuthorisation Servers\b',
     '<roles:Authorisation Server|Authorisation Servers>',
     r'<roles:Authorisation Server\|Authorisation Servers>'),
    (r'\bAuthorisation Server\b',
     '<roles:Authorisation Server>',
     '<roles:Authorisation Server>'),
    (r'\bVerifier Backends\b',
     '<roles:Verifier Backend|Verifier Backends>',
     r'<roles:Verifier Backend\|Verifier Backends>'),
    (r'\bVerifier Backend\b',
     '<roles:Verifier Backend>',
     '<roles:Verifier Backend>'),
    (r'\bRelying Applications\b',
     '<roles:Relying Application|Relying Applications>',
     r'<roles:Relying Application\|Relying Applications>'),
    (r'\bRelying Application\b',
     '<roles:Relying Application>',
     '<roles:Relying Application>'),
    (r'\bWallet Providers\b',
     '<roles:Wallet Provider|Wallet Providers>',
     r'<roles:Wallet Provider\|Wallet Providers>'),
    (r'\bWallet Provider\b',
     '<roles:Wallet Provider>',
     '<roles:Wallet Provider>'),
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
     '<credentials:Selective Disclosure>',
     '<credentials:Selective Disclosure>'),
    (r'\bCredential Offers\b',
     '<protocols:Credential Offer|Credential Offers>',
     r'<protocols:Credential Offer\|Credential Offers>'),
    (r'\bCredential Offer\b',
     '<protocols:Credential Offer>',
     '<protocols:Credential Offer>'),
    (r'\bRequest Objects\b',
     '<protocols:Request Object|Request Objects>',
     r'<protocols:Request Object\|Request Objects>'),
    (r'\bRequest Object\b',
     '<protocols:Request Object>',
     '<protocols:Request Object>'),
    (r'\bPresentation Requests\b',
     '<protocols:Presentation Request|Presentation Requests>',
     r'<protocols:Presentation Request\|Presentation Requests>'),
    (r'\bPresentation Request\b',
     '<protocols:Presentation Request>',
     '<protocols:Presentation Request>'),

    # Hyphenated protocol terms
    (r'\bProof-of-possession\b',
     '<protocols:Proof-of-possession>',
     '<protocols:Proof-of-possession>'),
    (r'\bproof-of-possession\b',
     '<protocols:Proof-of-possession|proof-of-possession>',
     r'<protocols:Proof-of-possession\|proof-of-possession>'),
    (r'\bKey binding\b',
     '<protocols:Key binding>',
     '<protocols:Key binding>'),
    (r'\bkey binding\b',
     '<protocols:Key binding|key binding>',
     r'<protocols:Key binding\|key binding>'),
    (r'\bDevice binding\b',
     '<protocols:Device binding>',
     '<protocols:Device binding>'),
    (r'\bdevice binding\b',
     '<protocols:Device binding|device binding>',
     r'<protocols:Device binding\|device binding>'),

    (r'\bSessionTranscript\b',
     '<protocols:SessionTranscript>',
     '<protocols:SessionTranscript>'),
    (r'\bDeviceResponse\b',
     '<protocols:DeviceResponse>',
     '<protocols:DeviceResponse>'),

    # === Single-word terms ===
    (r'\bHolders\b',
     '<roles:Holder|Holders>',
     r'<roles:Holder\|Holders>'),
    (r'\bHolder\b',
     '<roles:Holder>',
     '<roles:Holder>'),
    (r'\bVerifiers\b',
     '<roles:Verifier|Verifiers>',
     r'<roles:Verifier\|Verifiers>'),
    (r'\bVerifier\b',
     '<roles:Verifier>',
     '<roles:Verifier>'),
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
     '<protocols:Nonce|Nonces>',
     r'<protocols:Nonce\|Nonces>'),
    (r'(?<![_`])\bNonce\b(?![_`])',
     '<protocols:Nonce>',
     '<protocols:Nonce>'),
    (r'\bnonces\b',
     '<protocols:Nonce|nonces>',
     r'<protocols:Nonce\|nonces>'),
    (r'(?<![_`c])\bnonce\b(?![_`s])',
     '<protocols:Nonce|nonce>',
     r'<protocols:Nonce\|nonce>'),

    # Namespace
    (r'\bNamespaces\b',
     '<credentials:Namespace|Namespaces>',
     r'<credentials:Namespace\|Namespaces>'),
    (r'\bNamespace\b',
     '<credentials:Namespace>',
     '<credentials:Namespace>'),
    (r'\bnamespaces\b',
     '<credentials:Namespace|namespaces>',
     r'<credentials:Namespace\|namespaces>'),
    (r'\bnamespace\b',
     '<credentials:Namespace|namespace>',
     r'<credentials:Namespace\|namespace>'),
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
