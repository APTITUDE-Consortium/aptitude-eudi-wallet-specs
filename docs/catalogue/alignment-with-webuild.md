# Alignment with WE BUILD

Where the [WE BUILD attestation rulebooks catalogue](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog) has a counterpart for an attestation type of this catalogue, the type follows the counterpart's claim names, structure, types, formats, enumerations and required lists, so that a verifier or an issuer that knows one catalogue meets few gaps in the other. This page records what each type takes from its counterpart, what stays different, and the questions for the owners of each type.

## Types with a WE BUILD counterpart

| Type | WE BUILD counterpart | What the type takes | Version |
| --- | --- | --- | --- |
| `eu-company-certificate` | `ds004-eucc`, rulebook `rb-eucc` | A flat claim list (`legal_person_name`, `legal_person_id`, `legal_form_type`, `registered_address`, `share_capital`, ...), `digital_contact_point` with `website` and `email`, the required list, and closed nested objects. `expiry_date` stays as an optional claim. | 2.0.0 |
| `legal-person-identification-data` | `ds001-ebwoid`, rulebook `rb-ebwoid`, ADR 001 of WP4 | `id`, `name`, `date_of_expiry` (full-date) and the required list of the EBWOID. The issuing and authentic source claims of the LPID stay. | 2.0.0 |
| `iban-attestation`, `iban-attestation-for-individuals` | `iban-ov`, rulebook `rb-iban-ov` | `iban`, `bic_swift`, `national_bank_code`, `account_currency` as an array, `owner_type` (`entity` or `person`), `legal_person_identifiers`, `nace_code`, closed nested objects. The six issuing and authentic source claims are removed. `bank_account_token` of the individuals type stays. | 2.0.0 |
| `signatory-rights-attestation` | `authorised-signatories`, rulebook `rb-authorised-signatories` | `legal_entity`, `authorised_persons[]` with `natural_person`, `birth_place`, `citizenship`, `person_role` (`representation_type` `SOLE` or `JOINT`) and `residence_address`. Legal-person signatories stay as the optional `authorised_legal_persons[]`. | 2.0.0 |
| `ultimate-beneficial-owners-attestation` | `ubo`, rulebooks `rb-ubo`, `rb-ownership`, `rb-control` | `ubo[]` with `jurisdiction`, `person`, `citizenship`, `residential_address`, `justification`, `effective_date` and `source[]`. The `legal_person` object, `inactive_date`, `last_change_date`, `tax_domicile` and `is_alive` stay as additions. | 0.11.0 |
| `person-identification-data` | `ds002-pid`, rulebook `rb-pid` | Full-date for `date_of_issuance` and `date_of_expiry`, `place_of_birth` as a required object, E.164 and JPEG patterns, and the required list. The ARF age claims and `address.house_number` stay. | 2.0.0 |
| `payment-wallet-attestation` | `sca-card-dpc`, rulebooks `rb-sca-card-dpc`, `rb-sca-iban`, `rb-sca-user` | Flat snake_case claims of the SCA family (`credential_id`, `network`, `card_id`, `masked_iban`, `iban`, `national_bank_code`, `bic`, `masked_psu_id`), and `exp` as required. One type covers account, card and any funding source through `funding_source_type`. | 0.11.0 |
| `vreceipts` | `e-receipt`, rulebook `rb-e-receipt` | The WE BUILD receipt model: `receipt_number`, `receipt_timestamp`, `currency_iso_code`, amounts in minor units, `merchant`, `products[]`, `vats[]`, `payments[]`, `verifications[]`, the code lists and the OCMF rule. | 0.11.0 |
| `student-id` | rulebook `rb-student` (no schema) | Multi-valued `schac*` and `eduPerson*` attributes as arrays, the mandatory attributes of the rulebook as required, and `cryptographically_bound_to`. | 0.11.0 |
| `personal-contact-details-document` | `contact-person` | `family_name`, `telephone` with the E.164 pattern, `email`, and minimum lengths. | 0.11.0 |

Three types have no counterpart: `ferry-boarding-pass`, `photo-id` and `idproofing-etsi461`.

## Decisions that apply to every type

- The `vct` of each type is its own identifier (`eu.aptitude.<slug>.1`, or the EU identifier of a type that the EU defines), so that no `vct` equals one of the WE BUILD catalogue. The PID type uses `urn:eudi:pid:aptitude:1`.
- The standard claims `iss`, `iat`, `nbf`, `exp`, `cnf` and `status` are optional properties, and `status` has the Token Status List shape. WE BUILD defines `status` as a flat object and requires `iss`, `iat`, `exp` and `cnf`.
- Country values are ISO 3166-1 alpha-2. The WE BUILD schemas for authorised signatories and IBAN ownership use alpha-3 in places.
- The WE BUILD payload claims `attestation_legal_category`, `trust_anchor`, `trust_anchor_url` and `schema_version` are not claims of the catalogue types. registry-cli would list them as credential claims, and the WE BUILD rulebooks mark `attestation_legal_category` as still open against ETSI TS 119 472-1.
- The IBAN pattern follows ISO 13616 (two letters, two check digits, up to 30 alphanumeric characters).
- Arrays of objects are one entry in the registry's claim list; the registry lists one nested level.

## Questions for the owners

- **Issuing metadata.** The IBAN types drop `issuing_authority`, `issuing_authority_id`, `authentic_source_id` and `authentic_source_name`, and make `bic_swift` and `legal_person_identifiers` required. The LPID and the EUCC make `issuance_date`, `issuing_authority_id` and `expiry_date` optional. Are these changes acceptable for existing issuers?
- **LPID.** WE BUILD replaces the LPID with the EBWOID (ADR 001). Does APTITUDE keep the LPID type, deprecate it or migrate to the EBWOID? Do `issuing_jurisdiction` and the other LPID metadata stay?
- **Signatory rights.** Is `authorised_legal_persons[]` the right way to keep legal-person signatories, and do `person_role.email` and `person_role.phone` stay?
- **UBO.** Do `legal_person`, `inactive_date`, `last_change_date`, `tax_domicile` and `is_alive` stay, and is it acceptable that the percentage brackets (`0-25` and so on) give way to a number?
- **PID.** Do the ARF age claims (`age_over_18`, `age_equal_or_over`, `age_in_years`, `age_birth_year`) stay? WE BUILD has none.
- **Payment wallet attestation.** One type with `funding_source_type`, or three types as in WE BUILD? Do `pan_last_four`, `par_last_four` and `iin` stay, given that the WE BUILD rulebook says `card_id` reveals no PAN fragment?
- **Receipts.** The WE BUILD rulebook writes `transactionId` and its schema `transaction_id`; the type follows the schema.
- **Student ID.** Does `cryptographically_bound_to` stay as a payload claim? The type changes its `vct` from `VerifiableStudentIDSDJWT`, which affects existing issuers.
- **Contact details.** Do the renames of `surname`, `phone` and `email_address` conform to the `eu.europa.ec.eudi.pcd.1` definition? Should the address claims become a nested `address` object like the PID?
- **Legal category and trust anchor.** Should the catalogue ever carry `attestation_legal_category` and `trust_anchor`, once WE BUILD settles them?
- **Identifiers.** Do the identifiers that changed (`PaymentWalletAttestation`, `VerifiablevReceiptSDJWT` and `VerifiableStudentIDSDJWT` became `eu.aptitude.<slug>.1`) match what existing issuers use?
