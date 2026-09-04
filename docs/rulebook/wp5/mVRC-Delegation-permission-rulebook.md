# Attestation Rulebook for attestations of type mVRC Delegation Permission

* Author(s):
  * Tomasz Sikorski, COI

| Version | Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0.1     | 31.03.2026 | Initial draft of the mVRC Delegation Permission Attestation Rulebook                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 0.2     | 12.05.2026 | Added initial attribute model and mdoc encoding for the mVRC Delegation Permission attestation.                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0.5     | 02.07.2026 | Removed delegated user identity data from the attestation model to support data minimization. Clarified that delegated user identity verification is performed separately by the mVRC Issuer during the delegated mVRC issuance flow. Aligned attribute identifiers and encoding with snake_case naming, including `vehicle_privileges`, `privileges_scope`, `partial_privileges`, `expiration_date_time`, and `issuing_organization`. Updated the CDDL definition and mdoc example accordingly. |

Feedback:

* <tomasz.sikorski@coi.gov.pl>

## 1 Introduction

### 1.1 Document scope and purpose

This Rulebook defines the attestation type **mVRC Delegation Permission**.

The purpose of this attestation is to provide a short-lived authorization credential that proves that an organization has authorized a delegated user to obtain a delegated mVRC for a specific vehicle, within a defined validity period and scope of delegated vehicle privileges.

Within the EUDI Wallet ecosystem, the mVRC Delegation Permission is intended to be issued to the delegated user’s Wallet and subsequently presented to the official mVRC Issuer, together with an identity credential, as proof of authorization in the delegated mVRC issuance flow. The attestation itself does not contain delegated user identity data; identity verification is performed separately by the mVRC Issuer during issuance.

This Rulebook defines:

* the semantic meaning of the attestation attributes and metadata in an encoding-independent manner;
* the attestation encoding for ISO/IEC 18013-5:2021-compliant mdoc;
* the intended usage of the attestation;
* trust anchor considerations;
* revocation and status considerations;
* compliance requirements.

### 1.2 Document structure

This document is structured as follows:

* Chapter 2 defines the attestation attributes and metadata in an encoding-independent manner.
* Chapter 3 defines the encoding of the attestation.
* Chapter 4 defines the intended usage of the attestation.
* Chapter 5 defines how trust anchors for attestation verification can be obtained.
* Chapter 6 defines revocation and status considerations.
* Chapter 7 provides compliance information.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as specified in [RFC 2119], i.e., to indicate requirements, recommendations and options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external constraint, i.e., a requirement that is not mandated by this document, but, for instance, by an external document. The word 'can' indicates a capability, whereas other words, such as 'will', and 'is' or 'are' are intended as statements of fact.

### 1.4 Terminology

This document uses the terminology specified in Annex 1 of the ARF.

## 2 Attestation attributes and metadata

### Chapter overview and requirements

This chapter defines the attributes and metadata that an attestation of type **mVRC Delegation Permission** may contain.

The mVRC Delegation Permission is intended to be used as an authorization attestation that binds:

* the vehicle reference;
* the delegated privilege scope;
* the expiration date and time;
* and a unique permission identifier.

The attestation does not include delegated user identity data. The delegated user identity is verified separately during the delegated mVRC issuance flow, by presenting an identity credential together with the mVRC Delegation Permission.

### 2.1 Attestation legal category

This Rulebook assumes that the attestation legal category is defined by the applicable governance and issuance model.

Unless otherwise specified by the applicable trust framework, this attestation is intended to be used as a non-qualified EAA.

### 2.2 Mandatory attributes

| Data Identifier | Definition | Data type | Example value |
|---|---|---|---|
| `delegation_permission_id` | Unique identifier of the mVRC Delegation Permission. | string | `00b91349-f07a-44d8-94c6-db69f2b72a1a` |
| `vehicle_identification_number` | Vehicle Identification Number (VIN) of the authorized vehicle. | string | `WVWZZZ1JZXW000001` |
| `vehicle_registration_number` | Registration number of the authorized vehicle. | string | `WX12345` |
| `privileges_scope` | Overall scope of delegated vehicle privileges. It defines the rights that the consumer receives in the delegation process. The scope of the rights can be full or partial. | string | `full` |
| `expiration_date_time` | Expiration date and time to be applied to the delegated mVRC issued on the basis of this mVRC Delegation Permission. This value does not define the validity period of the mVRC Delegation Permission attestation itself. | string (tdate) | `2026-05-01T10:00:00Z` |
| `issuing_organization` | Identifier or name of the organization issuing the mVRC Delegation Permission. | string | `Example Rental Company` |

### 2.3 Conditional attributes

| Data Identifier | Definition | Data type | Example value |
|---|---|---|---|
| `partial_privileges` | SHALL be present when `vehicle_privileges.privileges_scope` indicates partial delegation. | array of strings | `["drive","road_suitability"]` |

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5:2021-compliant encoding

This Rulebook defines an ISO/IEC 18013-5:2021-compliant mdoc encoding for the **mVRC Delegation Permission**.

The attestation is intended to be proximity-presentable and internet-presentable within the EUDI Wallet ecosystem and therefore SHALL support an mdoc representation.

#### 3.1.1 Document type and namespace

The document type (`docType`) for this attestation SHALL be:

`eu.europa.ec.eudiw.mvrc.delegation_permission.1`

Unless otherwise specified by the implementation profile, the following namespace is defined for the attestation attributes:

`eu.europa.ec.eudiw.mvrc.delegation_permission.1`

### 3.1.2 Attributes overview

The following general encoding rules apply:

* `tstr`, `uint`, `bstr`, and `bool` follow the CDDL representation conventions.
* All string values SHALL be UTF-8 encoded.
* Dates expressed as textual values SHOULD follow RFC 3339-compatible syntax where applicable.
* Canonical CBOR encoding SHOULD be used for mdoc payloads.

| **Data Identifier** | **Attribute identifier** | **Encoding format** | **Namespace**|
|------------------------|--------------|------------------|------------------|
| `delegation_permission_id` | `delegation_permission_id` | tstr | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|
| `vehicle_identification_number` |   `vehicle_identification_number` | tstr | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|
| `vehicle_registration_number` |   `vehicle_registration_number` | tstr | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|
| `vehicle_privileges` |   `vehicle_privileges` | map, see [Section 3.1.2.1](#3121-attribute-vehicle_privileges) | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|
| `expiration_date_time` |   `expiration_date_time` | tdate | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|
| `issuing_organization` |   `issuing_organization` | tstr | `eu.europa.ec.eudiw.mvrc.delegation_permission.1`|

#### 3.1.2.1 Attribute vehicle_privileges

The attribute `vehicle_privileges` is encoded as a type `vehicle_privileges`. Using CDDL notation as specified in RFC 8610, the encoding of this attribute is:

```cddl
vehicle_privileges = full_vehicle_privileges / partial_vehicle_privileges

full_vehicle_privileges = {
  "privileges_scope": "full"
}

partial_vehicle_privileges = {
  "privileges_scope": "partial",
  "partial_privileges": [+ partial_privilege_enum]
}

partial_privilege_enum = "drive"
                       / "road_suitability"
                       / "id_plate"
                       / "technical_properties"
```

`vehicle_privileges` SHALL contain the key-value pair `privileges_scope`.

If `privileges_scope` is set to `partial`, the key-value pair `partial_privileges` SHALL be present and SHALL contain one or more values from the allowed set.

If `privileges_scope` is set to `full`, the key-value pair `partial_privileges` SHALL NOT be present.

If present, `partial_privileges` SHALL contain one or more values from the following set:

**`drive`, `road_suitability`, `id_plate`, `technical_properties`**
The set of values for partial_privileges can be expanded based on the business needs and development of the mVRC pilot. At the moment, the proposed values refer to an authorisation to drive a car (drive), proof of road suitability (road_suitability), presenting an ID plate when registering for a parking subscription (id_plate), proof of technical properties in order to e.g. access a restricted place etc. (technical_properties). The owner or holder can decide what kind of privileges they wish to grant to the consumer.

### 3.1.3 CDDL definition

```cddl
mvrc_delegation_permission = {
  "delegation_permission_id": tstr,
  "vehicle_identification_number": tstr,
  "vehicle_registration_number": tstr,
  "vehicle_privileges": vehicle_privileges,
  "expiration_date_time": tstr,
  "issuing_organization": tstr
}

vehicle_privileges = full_vehicle_privileges / partial_vehicle_privileges

full_vehicle_privileges = {
  "privileges_scope": "full"
}

partial_vehicle_privileges = {
  "privileges_scope": "partial",
  "partial_privileges": [+ partial_privilege_enum]
}

partial_privilege_enum = "drive"
                       / "road_suitability"
                       / "id_plate"
                       / "technical_properties"
```

### 3.1.4 Example

```cbor-diag
{
  "docType": "eu.europa.ec.eudiw.mvrc.delegation_permission.1",
  "issuerSigned": {
    "nameSpaces": {
      "eu.europa.ec.eudiw.mvrc.delegation_permission.1": [
        24(<<{
          "digestID": 0,
          "random": h'7F9C2BA4E88F827D616045507605853E',
          "elementIdentifier": "delegation_permission_id",
          "elementValue": "00b91349-f07a-44d8-94c6-db69f2b72a1a"
        }>>),
        24(<<{
          "digestID": 1,
          "random": h'0D61F8370CAD1D412F80B84D143E1257',
          "elementIdentifier": "vehicle_identification_number",
          "elementValue": "WVWZZZ1JZXW000001"
        }>>),
        24(<<{
          "digestID": 2,
          "random": h'F1D3FF8443297732862DF21DC4E57262',
          "elementIdentifier": "vehicle_registration_number",
          "elementValue": "WX12345"
        }>>),
        24(<<{
          "digestID": 3,
          "random": h'7B8B965AD4BCA0E41AB51DE7B31363A1',
          "elementIdentifier": "vehicle_privileges",
          "elementValue": {
            "privileges_scope": "partial",
            "partial_privileges": [
              "drive",
              "id_plate"
            ]
          }
        }>>),
        24(<<{
          "digestID": 4,
          "random": h'45C48CCE2E2D7FBDEA1AFC51C7C6AD26',
          "elementIdentifier": "expiration_date_time",
          "elementValue": 0("2026-05-01T10:00:00Z")
        }>>),
        24(<<{
          "digestID": 5,
          "random": h'6512BD43D9CAA6E02C990B0A82652DCA',
          "elementIdentifier": "issuing_organization",
          "elementValue": "Example Rental Company"
        }>>)
      ]
    },
    "issuerAuth": [
      h'A10126',
      {
        33: [
          h'308201AA...MVRC_ISSUER_LEAF_CERT_DER...',
        ]
      },
      24(<<{
        "version": "1.0",
        "digestAlgorithm": "SHA-256",
        "valueDigests": {
          "eu.europa.ec.eudiw.mvrc.delegation_permission.1": {
            0: h'1111111111111111111111111111111111111111111111111111111111111111',
            1: h'2222222222222222222222222222222222222222222222222222222222222222',
            2: h'3333333333333333333333333333333333333333333333333333333333333333',
            3: h'4444444444444444444444444444444444444444444444444444444444444444',
            4: h'5555555555555555555555555555555555555555555555555555555555555555',
            5: h'6666666666666666666666666666666666666666666666666666666666666666'
          }
        },
        "deviceKeyInfo": {
          "deviceKey": {
            1: 2,
            -1: 1,
            -2: h'6C8F25B6C9A7B3E4F19D2A5C7E9B11223344556677889900AABBCCDDEEFF0011',
            -3: h'7D9E36C7DA8BC4F20A1B2C3D4E5F60718293A4B5C6D7E8F90123456789ABCDEF'
          }
        },
        "docType": "eu.europa.ec.eudiw.mvrc.delegation_permission.1",
        "validityInfo": {
          "signed": 0("2026-03-31T10:00:00Z"),
          "validFrom": 0("2026-03-31T10:00:00Z"),
          "validUntil": 0("2026-04-01T09:59:59Z")
        }
      }>>),
      h'5F8D3C2A1B0099EE7766554433221100AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF001122334455667788'
    ]
  }
}
```

## 4 Attestation usage

### 4.1 Intended usage

The mVRC Delegation Permission SHALL be used as an authorization attestation in the delegated mVRC issuance process.

It is intended to prove that:

* an organization has authorized the delegated user to obtain a delegated mVRC;
* the authorization applies to a specific vehicle;
* the authorization defines the expiration date and time to be applied to the delegated mVRC issued on the basis of this permission;
* the authorization may be limited to a partial set of vehicle privileges.

### 4.2 Usage constraints

The mVRC Delegation Permission:

* SHALL be treated as a short-lived credential with a validity period of no more than 24 hours;
* SHALL be used only within its validity period;
* SHOULD be treated as a one-time authorization credential where required by the scenario or issuing authority;
* SHALL NOT be used as a substitute for a final delegated mVRC in scenarios that require the final delegated mVRC.

The `expiration_date_time` attribute defines the expiration date and time of the delegated mVRC to be issued, while the validity period of the mVRC Delegation Permission itself is defined by the mdoc `validityInfo` structure.

### 4.3 Cryptographic binding

The attestation SHALL be cryptographically bound to the delegated user's (consumer's) wallet or the delegated user’s (consumer's) key material,
therefore attestation SHALL contain or be associated with the necessary metadata to verify that binding.

## 5 Trust anchors

The trust anchors required to validate the mVRC Delegation Permission SHALL be obtained according to the applicable governance framework for the scenario.

At a minimum, the verifier of the attestation SHALL be able to determine:

* the trust anchor and trust list used for validating the issuing organization’s certificate chain;
* the certificate status or trust status of the issuing organization where applicable.

If a machine-readable trusted list or trust anchor publication endpoint is used, its location SHOULD be made available through applicable metadata or governance documentation.

## 6 Revocation and status information

The **mVRC Delegation Permission** is a **short-lived credential** with a validity period of up to **24 hours**.

For this reason, no dedicated revocation or status mechanism is defined in this Rulebook. The attestation is considered valid until its expiration time, provided that trust validation of the issuing authority succeeds.

The validity period of the mVRC Delegation Permission itself is defined by the mdoc `validityInfo` structure. The `expiration_date_time` attribute defines the expiration date and time to be applied to the delegated mVRC issued on the basis of this permission and does not extend the validity period of the mVRC Delegation Permission.

Any additional invalidation or status mechanism is deployment-specific and outside the scope of this Rulebook.

## 7 Compliance information

An implementation conforms to this Rulebook if it satisfies all mandatory requirements defined in this document for the supported encoding and usage context.

In particular:

* issuers SHALL issue the attestation with the attributes defined as mandatory in this Rulebook;
* wallets SHALL be able to process the mdoc encoding defined in this Rulebook;
* verifiers SHALL be able to interpret and validate the attestation according to the defined attribute semantics, trust requirements, and usage constraints.

## 8 References

1. ISO/IEC 18013-5:2021
2. ISO/IEC DTS 7367-2
3. RFC 8610 - Concise Data Definition Language (CDDL)
4. RFC 8949 - Concise Binary Object Representation (CBOR)
5. Architecture and Reference Framework (ARF)
6. EUDI Wallet Attestation Rulebooks Catalogue
