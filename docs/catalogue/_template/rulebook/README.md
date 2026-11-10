# {{title}} Rulebook

Author(s):

- [NAME SURNAME, AFFILIATION]

| Version | Date | Description |
| --- | --- | --- |
| 0.1 | [PUBLICATION DATE] | First draft |

**Feedback:**

- [LINK TO AN ISSUE TRACKER OR A CONTACT EMAIL ADDRESS]

## 1 Introduction

### 1.1 Document scope and purpose

State the business problem that the attestation addresses, the objective of the attestation, and the intended users and relying parties. Name the application domain, at least one use case, the preconditions and the usage limitations.

### 1.2 Document structure

Describe the chapters of this rulebook.

### 1.3 Key words

The key words SHALL, SHALL NOT, SHOULD, SHOULD NOT and MAY are used as described in the contributing guide of this repository.

### 1.4 Terminology

List the terms that the rulebook defines or relies on.

## 2 Attestation attributes and metadata

### 2.1 Introduction

Define the attributes in an encoding-independent way. Each attribute has an `identifier`, a `definition`, a `data type` and an `example value`.

### 2.2 Mandatory attributes

| Identifier | Definition | Data type | Example value |
| --- | --- | --- | --- |
| `example_attribute` | Description of the attribute. | string | `Example` |

### 2.3 Optional attributes

### 2.4 Conditional attributes

### 2.5 Mandatory metadata

### 2.6 Optional metadata

### 2.7 Conditional metadata

## 3 Attestation encoding

### 3.1 SD-JWT VC

The data schema [{{slug}}-sd-jwt.json](../../data-schemas/sd-jwt/{{slug}}-sd-jwt.json) describes the payload. State the `vct` value, the character encoding and the encoding rules.

### 3.2 mdoc

If the attestation has an mdoc encoding, state the document type, the namespace and the data element identifiers, and link the data schema in `data-schemas/mdoc/`.

## 4 Attestation usage

Describe the issuance, presentation and verification flows of the attestation, the information that a verifier receives, the rules for selective disclosure, the checks that a verifier performs and the failure conditions.

## 5 Trust anchors

Identify the trust anchors and the trust list that a verifier uses, and describe how the trust chain is validated.

## 6 Revocation

Describe how the status of the attestation is published and checked, or justify why revocation does not apply.

## 7 Compliance

List the regulations and standards that apply, trace each requirement to its source, and document and justify every deviation.

## 8 References

List the normative and informative references, including the related RFCs of this repository.
