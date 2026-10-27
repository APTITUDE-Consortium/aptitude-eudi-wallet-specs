# Alignment with WE BUILD and standards

The file names in this document are the names of the attestation types in the EWC repository that the catalogue continues; in this catalogue the `dsNNN-` prefix is dropped.

This document records how the EWC attestation schemas relate to the [WE BUILD attestation rulebooks catalogue](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog) and to the standards they build on. It lists what the schemas now do, what is proposed for the schema owners to decide, and the questions that need an owner's answer.

## Applied in this repository

These changes keep every currently valid credential valid. Each schema's `version` has a minor bump.

- The standard SD-JWT VC claims `iss`, `iat`, `nbf`, `exp`, `cnf` and `status` are defined as optional properties in every schema. `status` has the IETF Token Status List shape `{"status_list": {"idx": 0, "uri": "https://..."}}`. The rulebooks name these claims in a closing section.
- The top level of each schema states `"additionalProperties": true`, because issued SD-JWT VCs can carry `vct#integrity`, `extends` and issuer claims.
- Country and currency values that the description defines as ISO 3166-1 alpha-2 or ISO 4217 carry the matching pattern: `issuing_country` (DS-001, 004, 012, 014), `registration_member_state` (DS-001), `provider_country` (DS-002, 015), `place_of_birth.country` and `address.country` (DS-012), `resident_country` (DS-014); `share_capital.currency` (DS-001) and `account_currency` (DS-002, 015).
- The IBAN pattern follows ISO 13616: two letters, two check digits and up to 30 alphanumeric characters (15 to 34 in total); the earlier pattern stopped at 32.
- DS-007 `iat`, `nbf` and `exp` are integers, and `iss` has `format: uri`.
- The `vct` values use `eu.aptitude.<slug>.1`, and the PID uses `urn:eudi:pid:aptitude:1`. No `vct` equals one in the WE BUILD catalogue, so a registry can tell the types apart.
- DS-013 no longer uses `format: binary`, which is not a JSON Schema format; `contentEncoding: base64` stays.

## Proposed, for the owners to decide

The changes below alter what an issuer or a verifier sends, so they are not applied. They are marked BREAKING in the per-credential list.

## 0. What WE BUILD does (facts read from the clone)

- vct styles are mixed: `eu.we-build:<name>:1` (companyinfo, ubo, ownership, control, authorisedsignatories, contactperson, duns, approvedsupplier), `eu.we-build.<name>.1` (ereceipt, iban-ov, ds-membership), `eu.webuildconsortium.helloworld.v1`, URLs (`https://webuildconsortium.eu/credentials/microcredential/1.0`, SCA family `https://webuildconsortium.eu/sca/<x>/1.0` with `extends` + `extends#integrity`), standard URNs (`urn:eudi:pid:1`, `urn:eudi:eucc:1`), `uri:eu.ebw.oid.1` (EBWOID), and bare `VerifiableStudentID` (rb-student).
- Schemas use `const` for vct in about half the files (company-info, ubo, ownership, control, microcredentials, e-receipt); the others give `examples` only (authorised-signatories, iban-ov, ds001-ebwoid, ds002-pid, ds004-eucc) or `format: uri` (sca-card-dpc, eu-poa).
- Common payload block in business-wallet schemas: `iss` (uri), `iat`, `exp` (required integers), `nbf`, `jti`, `cnf.jwk`, `attestation_legal_category` (required; values `EAA`, `QEAA`, `PUB-EAA`, `PuB-EAA`, `non-qualified-EAA` across files), `schema_version`, `trust_anchor_url` (ds-numbered files use `trust_anchor`), `issuing_entity`, `status`.
- `status` has two shapes: (a) flat `{type, status_list_credential, status_list_index, status_purpose}` in company-info, ubo, ownership, control, authorised-signatories, contact-person, ds001-ebwoid, ds002-pid, ds004-eucc, ds007-eu-poa (a W3C-BitstringStatusList look-alike); (b) `{status_list:{idx, uri}}` in iban-ov, which is the IETF Token Status List shape. e-receipt leaves `status` untyped.
- Conventions: `additionalProperties:false` in company-info, ubo, ownership, control, e-receipt, ds004-eucc, ds007-eu-poa; `true` in authorised-signatories, iban-ov, contact-person, ds001-ebwoid, ds002-pid, microcredentials, sca-card-dpc (sca-card states why: `vct#integrity`, `extends`). `$id` values are inconsistent (`we-build.example.com`, `example.org`, `webuildconsortium.eu`). `version` appears in about half of the files, plus `$id`-embedded versions for ubo/control. Selective disclosure is stated per claim in prose in company-info ("NOT selectively disclosable"); most other files do not mark it. Sample payloads live in `data-schemas/sd-jwt/sample-data/`.
- Country codes: alpha-2 almost everywhere; alpha-3 (`^[A-Z]{3}$`) in authorised-signatories (birth_place.country, residence_address.country, identifier.issuing_country) and iban-ov (`provider_country`).
- Dates: business dates as `format: date`; `iat/exp/nbf` as integers (NumericDate).
- WB has no schema for LPID (replaced by EBWOID, ADR 001), Photo ID, ETSI 119 461 ID proofing, ferry boarding pass, personal contact details, payment wallet attestation, student ID (rulebook only), vReceipts (e-receipt covers receipts with a different model).

## 1. Matrix

| EWC credential (file) | WB counterpart | vct: EWC vs WB | Claim-name differences | Metadata/status differences | Recommended action |
|---|---|---|---|---|---|
| ds001 EU Company Certificate (`ds001-eu-company-certificate`) | `ds004-eucc-sd-jwt.json` (EUCC, also `company-info-sd-jwt.json` as related) | `eu.aptitude.eu-company-certificate.1` vs `urn:eudi:eucc:1` (domestic `urn:eudi:eucc:<cc>:1`) | EWC nests everything under `legal_person{...}`; WB EUCC is flat (`legal_person_name`, `legal_person_id`, `legal_form_type`, `registration_member_state`, ...). EWC `contact_point{contact_page, contact_email}` vs WB `digital_contact_point{website, email}`. `share_capital` amount/currency optional in EWC, required in WB. `legal_representative` entries: same members (`full_name`, `date_of_birth`, `nationality`, `signatory_rule`); WB legal-person variant uses `name`,`id`,`legal_form_type`; EWC variant `legal_person_name`,`legal_person_id` (verify in file) | EWC requires `expiry_date` and has no `iss/iat/exp/cnf/status/attestation_legal_category/trust_anchor`; WB has them (all optional except identity members). `issuance_date` date-time in both | Keep EWC structure (decision: nesting is an EWC design choice, renaming is BREAKING); add optional metadata block; ask owners whether flat WB EUCC shape is the target (Q1) |
| ds002 IBAN Attestation | `iban-ov-sd-jwt.json` (IBAN-OV) | `eu.aptitude.iban-attestation.1` vs `eu.we-build.iban-ov.1` | `IBAN` vs `iban`; `BIC` vs `bic_swift` (sca-iban uses `bic`); `provider_country` alpha-2 vs alpha-3 in WB; `account_currency` string vs array in WB; WB `account_ownership{owner_type, owner_name, given_name, surname, legal_person_identifiers[]}` vs EWC `{owner_name, parties[]}`; WB provider has `national_bank_code`, `nace_code`, `legal_person_identifiers`; EWC has `bank_identifier` | EWC has `authentic_source_*`, `issuing_authority*`; WB has `iss/iat/exp`, `attestation_legal_category`, `status` (Token Status List shape), `cnf`, `trust_anchor_url` | Rename `IBAN`->`iban`, `BIC`->`bic` only if owners agree (BREAKING); add optional `owner_type`; add IBAN/BIC format fixes (COMPATIBLE) |
| ds003 Signatory Rights Attestation | `authorised-signatories-sd-jwt.json` | `eu.aptitude.signatory-rights-attestation.1` vs `eu.we-build:authorisedsignatories:1` | Different models. EWC: `legal_person_name`, `legal_person_id`, `signatory_rights[]` (person: `full_name`, `date_of_birth`, `nationality`, `signatory_rule`, `post[]`; legal person variant). WB: `legal_entity{legal_person, identifier{euid, lei, tax,...}}`, `authorised_persons[]` (`natural_person{first_name,surname,date_of_birth}`, `birth_place`, `citizenship[]`, `person_role{representation_type SOLE/JOINT}`, `identifier{document_*}`). `signatory_rule` enum is `["alone"]` only in EWC (EUCC allows alone/joint) | EWC has no `iss/iat/exp/cnf/status`; WB requires them and `attestation_legal_category` (`EAA`) | Do not merge models. Fix `signatory_rule` enum if "joint" is intended (Q3). Add metadata block |
| ds004 Legal Person Identification Data | `ds001-ebwoid-sd-jwt.json` (LPID deprecated by ADR 001) | `eu.aptitude.legal-person-identification-data.1` vs `uri:eu.ebw.oid.1` | EWC `legal_person_id`, `legal_person_name`; EBWOID `id`, `name`. EWC adds `issuing_*`, `authentic_source_*` | EBWOID has `attestation_legal_category` (`QEAA`/`PUB-EAA`), `date_of_expiry`, `status`, `trust_anchor`, `cnf` | ADR 001: WB deprecates LPID and migrates to EBWOID. Mark ds004 as deprecated in `description` (COMPATIBLE); decide whether to keep or replace (Q2) |
| ds005 Ferry Boarding Pass | none | `VerifiableFerryBoardingPassCredentialSDJWT` vs - | camelCase claims (`ticketQR`, `ticketLet`, `seatType`, ...) | none | Namespace the vct (BREAKING); no WB comparison possible |
| ds006 Ultimate Beneficial Owners | `ubo-sd-jwt.json` (also `ownership`, `control`) | `eu.aptitude.ultimate-beneficial-owners-attestation.1` vs `eu.we-build:ubo:1` | Different models. EWC: `legal_person{...}` + `ultimate_beneficial_owner[]` (`natural_person_details{family_name, first_name, birth_date, postal_address, nationality, ...}`, `ownership_details[]`). WB: `ubo[]` with `jurisdiction`, `person`, `birth_place`, `citizenship[]`, `residential_address`, `person_identifier`, `justification`, `effective_date`, `source[]` | WB: `iss,iat,exp`, `attestation_legal_category`, `status` (flat, `status-list`, `revocation`), `schema_version`, `trust_anchor_url`. EWC none | Keep EWC model; note WB UBO model in rulebook; add metadata block; ask whether convergence is wanted (Q4) |
| ds007 Payment Wallet Attestation | `sca-card-dpc-sd-jwt.json`, `rb-sca-iban`, `rb-sca-user` (no schemas for the last two) | `PaymentWalletAttestation` vs `https://webuildconsortium.eu/sca/{sca-card-dpc,sca-iban,sca-user}/1.0` with issuer-specific `extends` | `fundingSource{type, panLastFour, iin, parLastFour, ibanLastFour, bic, sortCode, aliasId, currency, scheme, icon}` camelCase vs WB `credential_id`, `network`, `card_id`, `masked_iban`, `iban`, `bic`, `masked_psu_id` snake_case | Both model `iss/iat/exp/cnf`; WB requires `attestation_legal_category`; WB cards use `extends` + `vct#integrity`. EWC `iat/nbf/exp` typed `number` (should be `integer`) | Namespace or URL-ify vct (BREAKING); change `number`->`integer` (COMPATIBLE for conforming data); ask whether ds007 is meant to be a SCA base type (Q5) |
| ds009 Personal Contact Details | `contact-person-sd-jwt.json` (different subject: company contacts) | `eu.europa.ec.eudi.pcd.1` vs `eu.we-build:contactperson:1` | EWC: `surname`, `given_name`, `phone`, `email_address`; WB: `family_name`, `given_name`, `telephone`, `email` inside `contact_persons[]` | EWC requires `iss` (uri), `iat` as top-level required | No real counterpart. Keep EC `pcd` vct. Note `surname` vs PID `family_name` (Q6) |
| ds010 Student ID | `rb-student/README.md` (no schema in WB) | `VerifiableStudentIDSDJWT` vs `VerifiableStudentID` | Names equal (`firstName`, `familyName`, `eduPerson*`, `schac*`, `mail`, `dateOfBirth`). WB rulebook types `schacPersonalUniqueID`, `eduPersonAffiliation`, `eduPersonScopedAffiliation`, `eduPersonAssurance` as arrays of strings (rb-student lines 232-239); EWC types them as strings | WB rulebook lists `iss`, `iat`, `exp`, `cnf` | Align vct with WB rulebook or move to namespaced form (Q7); array typing (BREAKING) |
| ds011 vReceipts | `e-receipt-sd-jwt.json` | `VerifiablevReceiptSDJWT` vs `eu.we-build.ereceipt.1` | Entirely different models: EWC UBL-like camelCase with string amounts; WB snake_case (`receipt_number`, `receipt_timestamp`, `currency_iso_code`, integer minor-unit amounts, `merchant`, `products[]`, `vats[]`, `payments[]`) | WB requires `iss,iat,exp,cnf`, `attestation_legal_category`, has `status` | Do not converge now; namespace vct; add currency/country patterns (Q8) |
| ds012 PID | `ds002-pid-sd-jwt.json` | `urn:eudi:pid:aptitude:1` vs `urn:eudi:pid:1` (the identifier WB `ds002-pid` and the ARF use) | WB: `date_of_issuance` and `date_of_expiry` `format: date`, `place_of_birth` required, `address` without `house_number`, `phone_number` pattern `^\+[0-9]{4,15}$`, `picture` jpeg data URI, `attestation_legal_category` const `PUB-EAA`. EWC: `date_of_issuance`/`date_of_expiry` date-time, `place_of_birth` optional, `address.house_number`, extra `age_over_18`, `age_equal_or_over{16,18,21,65}`, `age_in_years`, `age_birth_year`, `document_number`, `trust_anchor` | WB requires `cnf`; both lack `iss` requirement in EWC; EWC has no `status/cnf` | Fix date formats (BREAKING for issuers sending date-time); require `place_of_birth` (BREAKING) if ARF confirms |
| ds013 Photo ID | none | `eu.europa.ec.eudi.photoid.1` vs - | Names follow ISO/IEC 23220 mdoc element identifiers (`family_name_unicode`, `portrait`, `issuing_authority_unicode`, `dtc_*`) | n/a | Format fixes only (see section 3) |
| ds014 ID Proofing ETSI 461 | none | `eu.aptitude.idproofing-etsi461.1` vs - | PID-like claims plus `documentInfo{document_type, document_number, issued_on, expires_on}` and `identityProofingProcessCompliance` (camelCase, unlike the rest) | n/a | Format fixes; question on camelCase members (Q9) |
| ds015 IBAN Attestation for Individuals | `iban-ov-sd-jwt.json` (`owner_type: person`) | `eu.aptitude.iban-attestation-for-individuals.1` vs `eu.we-build.iban-ov.1` | As ds002, plus `bank_account_token{account_token_number, masked_account_number, token_attributes}`; WB sca-iban has `masked_iban` | As ds002 | Same edits as ds002; treat ds002/ds015 as one rename decision |

## 2. Cross-cutting proposals (ordered by value)

1. Shared issuer metadata claim set (value: every verifier needs trust, validity and revocation uniformly; EWC schemas currently define none of `iss`, `iat`, `exp`, `cnf`, `status` except ds007/ds009).
   Add to every schema, as optional properties with descriptions: `iss` (string, format uri), `iat`, `nbf`, `exp` (integer, NumericDate), `cnf` (object with `jwk`), `status` (see 3). registry-cli leaves these out of the claim list. `attestation_legal_category` and `trust_anchor` are not part of this set: registry-cli would list them as claims, so they need an owner decision first (Q11). Keep EWC `issuing_authority`, `issuing_authority_id`, `issuing_country`, `issuance_date`, `expiry_date`, `authentic_source_*` as business attributes and state in their descriptions how they relate to `iss/iat/exp` (they are attributes about the authentic source/document, JWT claims are about the token). COMPATIBLE when optional.
2. vct naming scheme: recommend `eu.aptitude.<slug>.1` (the identifiers of this repository, and the same dotted style as WB e-receipt/iban-ov/ds-membership and `eu.europa.ec.eudi.*`), while keeping externally-owned identifiers unchanged (`urn:eudi:pid:1`, `eu.europa.ec.eudi.photoid.1`, `eu.europa.ec.eudi.pcd.1`, and `eu.we-build...` only for WB-owned types). Justification: SD-JWT VC requires a collision-resistant `vct`; bare strings (`PaymentWalletAttestation`, `Verifiable...SDJWT`, `VerifiableFerryBoardingPassCredentialSDJWT`) are not. Rename those four to `eu.aptitude.<slug>.1`: BREAKING. Consider `https://` vct values later only if type metadata is hosted (needed for `vct#integrity`); this is a rulebook-level decision (document-formats ADR delegates formats to WP4 Architecture; no vct rule is recorded there).
3. `status` claim shape: use the IETF Token Status List form `{"status": {"status_list": {"idx": <int>, "uri": <uri>}}}` (the shape iban-ov already uses and SD-JWT VC references). Do not copy the flat `status_list_credential/status_list_index/status_purpose` form used in most WB files: it follows the W3C Bitstring Status List and has no meaning in SD-JWT VC. Optional property in each schema. COMPATIBLE (new optional claim). Note the `status` claim is a JWT-level claim, never selectively disclosable.
4. Dates, countries, currencies (see per-credential edits): ISO 8601 `format: date` for date-only attributes (`birthdate`, `date_of_expiry`, registration dates); `date-time` only where a time of day exists (`portrait_capture_date`, `receipt_timestamp`). ISO 3166-1 alpha-2 `^[A-Z]{2}$` everywhere (WB alpha-3 in authorised-signatories and iban-ov is the outlier; do not copy it). ISO 4217 `^[A-Z]{3}$`. `issuing_jurisdiction`: ISO 3166-2 `^[A-Z]{2}-[A-Z0-9]{1,3}$` (EWC currently minLength 2/maxLength 6; to verify against the PID rulebook).
5. `additionalProperties`: leave the top level open (explicit `true`) because issued SD-JWT VCs legitimately carry `vct#integrity`, `extends`, `extends#integrity` and issuer claims (WB sca-card states this reasoning). Set `false` only on nested objects where the attribute list is closed by the rulebook (e.g. `registered_address`, `bank_account`). Changing nested objects to `false` is BREAKING; adding `true` at top level is COMPATIBLE and documents the existing default.
6. Selective-disclosure marking: add the sentence "MUST be selectively disclosable" to personal-data claims, and "MUST NOT be selectively disclosable" (or WB style "NOT selectively disclosable") to `iss, iat, nbf, exp, cnf, status, vct`. The registry plugin turns the first wording into sd=always. EWC currently has no marking in any schema. Which claims to mark is a rulebook decision (Q10); COMPATIBLE as a description change.
7. Examples: 7 of 14 EWC schemas have no `examples` (ds005, ds006, ds009, ds010, ds011, ds013, ds014). Add one `examples` entry per claim for the main attributes and copy the full-document samples to `data-schemas/sd-jwt/sample-data/<name>-sd-jwt-sample.json` as WB does. COMPATIBLE.
8. Version policy: keep top-level `version` (semver; 1.0.0 approved, 0.9.0 under development, per the conventions file) and bump MAJOR for any BREAKING edit listed below, MINOR for added optional claims, PATCH for descriptions/examples. WB's `$id`-embedded versions (ubo 0.4.0, control 0.9.0) and the payload claim `schema_version` do not exist in EWC; do not add `schema_version` unless owners want parity (Q11). Do not copy WB `$id` hosts (`we-build.example.com`, `example.org`).
9. `attestation_legal_category` values: use `EAA`, `QEAA`, `PUB-EAA` (WB uses both `PUB-EAA` and `PuB-EAA`, and `non-qualified-EAA`; the ARF spelling is `PuB-EAA`, to verify). Pick one spelling for the enum in the shared block. The WB sca-card rulebook records that ARF requirement EW-DM-12-029 (legacy ARB_25) still requires this attribute; keep it optional in EWC (COMPATIBLE) unless owners require it.
10. TS11 SchemaMeta link (to verify against TS11 itself; I only read registry-cli's `pkg/schemameta/schemameta.go`): its record carries `id`, `version`, `attestationLoS`, `bindingType`, `supportedFormats`, `schemaURIs`, `rulebookURI`, `trustedAuthorities`. The schema `version` and `$id` map to the first two; `attestation_legal_category` maps to LoS. No schema edit needed beyond items 1, 8, 9.

## 3. Per-credential edits

Legend: B = BREAKING (changes what an issuer or verifier sends), C = COMPATIBLE. "Shared block" means item 1 of section 2 (C). All edits below also require the matching rulebook attribute table row to be updated.

### ds001 EU Company Certificate (`ds001-eu-company-certificate-sd-jwt.json`)

- C: `issuing_country`, `registration_member_state`: add `pattern ^[A-Z]{2}$` (keep length).
- C: `share_capital.currency`: add `pattern ^[A-Z]{3}$` (ISO 4217).
- C: `legal_person_id`: description names EUID (format from Commission Implementing Regulation (EU) 2021/1042, pattern not added, to verify).
- C: add shared block, `additionalProperties: true` at top level.
- B (only if owners choose WB shape, Q1): flatten `legal_person.*` to top level; rename `contact_point{contact_page, contact_email}` to `digital_contact_point{website, email}`.
- C: add one example for `legal_representative`.

### ds002 IBAN Attestation and ds015 IBAN for Individuals

- C: `IBAN` (and `account_token_number`): pattern to `^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$` (ISO 13616: country letters, 2 check digits, up to 30 alphanumerics, 15 to 34 characters). The current `[0-9A-Z]{13,30}` caps at 32 characters.
- C: `BIC`: current pattern already matches ISO 9362 (8 or 11 characters); no edit.
- C: `account_currency`, `provider_country`: add `^[A-Z]{3}$`, `^[A-Z]{2}$` patterns.
- C: add optional `account_ownership.owner_type` (enum `entity`, `person`; in ds015 const `person`) and optional `legal_person_identifiers[{type, value}]` as in iban-ov.
- B (Q12): rename `IBAN`->`iban` and `BIC`->`bic` for snake_case consistency with every other EWC claim and with iban-ov (`iban`).
- C: shared block (`status` as Token Status List).
- ds015: B if `account_token_number` is meant to differ from an IBAN (then drop the IBAN pattern from it; Q13).

### ds003 Signatory Rights Attestation

- C: add `$defs` descriptions already present; add `status`, `cnf`, `iss`, `iat`, `exp` shared block.
- B (Q3): `signatory_rule` enum `["alone"]` -> `["alone","joint"]` in `signatory_rights_held_by_person` and `_legal_person` if joint signatures are in scope. This widens accepted data; BREAKING for verifiers that rely on "alone".
- C: `date_of_birth` already `format: date`; `nationality`: add `^[A-Z]{2}$` pattern (ISO 3166-1 alpha-2) if the rulebook agrees; otherwise leave description.

### ds004 Legal Person Identification Data

- C: description: "Deprecated by ADR 001 (replace LPID with EBWOID); do not reference from new specifications."
- C: `issuing_country` pattern; shared block.
- B (Q2): migrate to EBWOID claims `id`, `name`, and vct `uri:eu.ebw.oid.1`. Not recommended inside this PR.

### ds005 Ferry Boarding Pass

- B: vct -> `eu.aptitude.ferry-boarding-pass.1`.
- C: add `pattern`/format to `departureTime`/`arrivalTime` (`^[0-2][0-9]:[0-5][0-9](:[0-5][0-9])?$`), examples, shared block.

### ds006 Ultimate Beneficial Owners

- C: `ownership_details.nature_of_control`/`ownership_type` enums stay; `nationality`, `tax_domicile`: add `^[A-Z]{2}$`.
- C: `legal_person.registered_address`, `postal_address` stay strings (WB uses an address object; do not change).
- C: add examples (none today); shared block (`exp` etc.).
- B (Q4): converge to WB `ubo` (`jurisdiction`, `person`, `citizenship[]`, `effective_date`, ...). Not recommended in this PR.

### ds007 Payment Wallet Attestation

- B: vct `PaymentWalletAttestation` -> `eu.aptitude.payment-wallet-attestation.1` (or a WB SCA URL, Q5).
- C: `iat`, `nbf`, `exp`: `number` -> `integer`.
- C: `fundingSource.currency` already `^[A-Z]{3}$`; `bic` add BIC pattern (same as ds002); `ibanLastFour` pattern `^[A-Z0-9]{4}$` kept.
- C: `iss`: add `format: uri` (SD-JWT VC; WB requires uri).
- C: required list contains `iss, sub, iat, cnf`; keep, add `exp` as optional description only.
- C: examples exist; keep.

### ds009 Personal Contact Details

- C: `iat`: `integer` fine; add `nbf`, `status`, `cnf`; `country_address`: `^[A-Z]{2}$`; `phone`: `^\+[1-9][0-9]{6,14}$` (E.164; WB contact-person uses it; "to verify" that EC pcd rulebook agrees).
- B (Q6): rename `surname` to `family_name` and `email_address` to `email` to match PID; not recommended unless the EC `pcd` definition allows it.

### ds010 Student ID

- B: vct `VerifiableStudentIDSDJWT` -> `eu.aptitude.student-id.1` (or `VerifiableStudentID` to match rb-student; Q7).
- B: `schacPersonalUniqueID`, `eduPersonAffiliation`, `eduPersonScopedAffiliation`, `eduPersonAssurance` -> arrays of strings (WB rb-student 3.x tables).
- C: `mail` stays `format: email`; `dateOfBirth` already `format: date`; add examples, `exp`, `cnf`, `status`.

### ds011 vReceipts

- B: vct `VerifiablevReceiptSDJWT` -> `eu.aptitude.vreceipts.1`.
- C: `documentCurrencyCode`: `^[A-Z]{3}$`; `*.countryIdentifier`: `^[A-Z]{2}$`; add examples.
- C: `purchaseReceiptLine[].item` defines `additionalItemProperty` twice (once under `itemInstance`, once directly); confirm which is intended (Q8). Removing one is BREAKING.
- C: `paidAmount`, `taxableAmount` and other amounts are strings; add description "decimal string" (no pattern; WB e-receipt uses integer minor units, do not change).

### ds012 PID (`ds012-person-identification-data-sd-jwt.json`)

- B: `date_of_expiry`, `date_of_issuance`: `format: date-time` -> `format: date` (ARF PID rulebook and WB ds002-pid use full-date; to verify in the ARF Annex).
- B: add `place_of_birth` to `required` (ARF PID mandatory attribute, to verify; WB requires it).
- C: `place_of_birth.country`, `address.country`: add `^[A-Z]{2}$`; `nationalities.items`: `^[A-Z]{2}$`.
- C: `phone_number`: add `^\+[0-9]{4,15}$` (as in WB); `picture`: keep (WB restricts to jpeg data URI; ARF text on picture encoding to verify).
- C: `sex`: enum 0,1,2,3,4,5,6,9 matches both WB and EWC; ISO/IEC 5218 core values are 0,1,2,9 (3-6 are EUDI additions, to verify).
- C: `age_equal_or_over` is an object with numeric keys: confirm keys against ARF (EWC `16,18,21,65`; to verify). Add shared block (`cnf`, `status`, `iss`).
- C: `vct` const `urn:eudi:pid:aptitude:1` follows the `urn:eudi:pid:<domain>:1` pattern of national PID types with `aptitude` as the domain, so that it differs from WB's `urn:eudi:pid:1`; the description states the pattern.

### ds013 Photo ID

- C: `issuing_country`, `resident_country`, `nationality`, `birth_country`: `^[A-Z]{2}$` (ISO 3166-1 alpha-2; ISO/IEC 23220 uses alpha-2, to verify).
- C: `dtc_*` and `dg_content_info`: replace `format: binary` (not a JSON Schema 2020-12 format) with `contentEncoding: base64`; no change for valid data.
- C: `sex` description: ISO/IEC 5218 (to verify); `age_over_18` stays required.
- C: `portrait`: keep data-URI pattern; add example; shared block.

### ds014 ID Proofing ETSI 461

- C: country fields: `^[A-Z]{2}$`; `nationality`; `resident_country`.
- C: `age_over_NN` is a placeholder for `age_over_<NN>` claims (ARF); express as `patternProperties` `^age_over_[0-9]{2}$` boolean instead of a literal property name (C if no literal `age_over_NN` was ever issued; B otherwise, Q9).
- C: description cross-reference to ETSI TS 119 461 (identity proofing levels) in `identityProofingProcessCompliance.compliant_with`; add `examples`.
- B (Q9): normalise `documentInfo`/`identityProofingProcessCompliance` camelCase to snake_case.

## 4. Questions only the schema owners can answer

1. Q1: Should EUCC (ds001) follow the flat WB `urn:eudi:eucc:1` shape or keep the nested `legal_person` structure, and is `eu.aptitude.eu-company-certificate.1` meant to coexist with `urn:eudi:eucc:1`?
2. Q2: Is ds004 LPID kept, deprecated in place, or replaced by EBWOID per ADR 001? ADR 001 itself records the PID/EBWOID working group agreement but not an EWC decision.
3. Q3: Is `signatory_rule` limited to "alone" on purpose in ds003, given EUCC allows "joint"?
4. Q4: Is the UBO model (ds006) intended to converge with the WB `ubo`/`ownership`/`control` models?
5. Q5: Is ds007 a wallet-level attestation (separate from the `sca-*` family), and which vct style should it use?
6. Q6: Is ds009 `surname`/`phone`/`email_address` fixed by the EC `eu.europa.ec.eudi.pcd.1` definition?
7. Q7: Which vct for the student ID (ds010): the WB rulebook's `VerifiableStudentID`, or a namespaced one? Are the eduPerson/SCHAC multi-valued attributes arrays?
8. Q8: ds011: is the duplicated `additionalItemProperty` intentional, and should it converge on WB e-receipt?
9. Q9: ds014: are camelCase members in `documentInfo` and `identityProofingProcessCompliance` deliberate; is `age_over_NN` ever issued literally?
10. Q10: Which claims MUST be selectively disclosable per credential (legal-person claims in EUCC/UBO especially)?
11. Q11: Do owners want `schema_version` and `trust_anchor_url` parity with WB payloads?
12. Q12: May `IBAN`/`BIC` be renamed to `iban`/`bic` (ds002, ds015)?
13. Q13: Is `bank_account_token.account_token_number` IBAN-shaped?

## Notes on the analysis

Read for this analysis: all EWC schemas, thirteen WE BUILD schemas, the WE BUILD rulebook text for the `sca-*` family, the student ID and the EBWOID, and three WP4 texts. Items marked "to verify" were not checked against the ARF annexes, ISO/IEC 23220, ISO/IEC 5218, the EUID format, TS11 or E.164. The EWC rulebook tables and the WE BUILD sample data were not compared.
