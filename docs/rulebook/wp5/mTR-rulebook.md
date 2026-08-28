# Attestation Rulebook for attestations of type  *EU-mTR*

Author(s):

- Matthias Schwan, Bundesdruckerei GmbH, Germany
- Jan Willem Stekelenburg, RDW, the Netherlands

| Version | Date | Description |
| --- | --- | --- |
| 0.2 | 28.08.2026 | first draft of EU-mTR |

**Feedback:**

- <matthias.schwan@bdr.de>
- <jstekelenburg@rdw.nl>

## 1 Introduction

### 1.1 Document scope and purpose

This document specifies the “European Union mobile Technical Report (EU-mTR)” serving as roadworthiness certificate in accordance with EU Directive [xzy]. An EU-mTR is a mobile document, i.e. QEAA or Pub-EAA, managed by an EUDI Wallet according to [European Digital Identity Regulation]. The specification of the EU-mTR is a profile of the mTR specified in [ISO/IEC 7367-3].
### 1.2 Document structure

- Chapter 2, which describes ...
- Chapter 3, which specifies how the attestation, attributes and metadata are encoded in case the attestation complies with [ISO/IEC 18013-5] .
- Chapter 4, which specifies attestation usage.
- Chapter 5, which defines how trust anchors for attestation verification can be obtained.
- Chapter 6, which defines attestation revocation mechanisms.
- Chapter 7, which provides compliance information.

### 1.3 Key words

This document uses the capitalised key words 'SHALL', 'SHOULD' and 'MAY' as
specified in [RFC 2119], i.e., to indicate requirements, recommendations and
options specified in this document.

In addition, 'must' (non-capitalised) is used to indicate an external
constraint, i.e., a requirement that is not mandated by this document, but, for
instance, by an external document. The word 'can' indicates a capability,
whereas other words, such as 'will', and 'is' or 'are' are intended as
statements of fact.

### 1.4 Terminology

Terminologies and definitions within Aptitude project are listed in [APTITUDE Glossary](/docs/glossary.md)

## 2 Attestation attributes and metadata

### 2.1 Introduction

This document describes the structure, type, data element identifiers, and logical organisation of the mandatory and optional attributes of the EU-mTR attestation within the EUDI Wallet. It also describes how Member States can specify any possible national attributes.

The specification of the EU-mTR is a profile of the mTR specified in [ISO/IEC 7367-3]. The mTR [ISO/IEC 7367-3] references data structures and security mechanisms defined for <credentials:mobile Driving Licence (mDL)|mDL> and <artifacts:mdoc>, such as device request/response structures, IssuerSigned and IssuerAuth structures (MSO) as well as protocols for proximity and remote flows. These protocols and structures are mandatory features of the EUDI Wallet ecosystem . The EU-mTR profile mandates the use of doc type and name space according to [ISO/IEC 7367-3] and gives more detailed information on the use of the data elements. A profile further specifies additional name spaces under responsibility of the EU and of respective Member States.

## 3 Attestation encoding

### 3.1 ISO/IEC 18013-5-compliant encoding

#### 3.1.1 EU mVRC document type and namespace

The objects ``docType`` and ``namespace`` are used to encapsulate the document type and the space in which the data elements are defined.

The document type for the **EU-mTR** SHALL be as specified in clause xx of [ISO/IEC 7367-3].

The namespace for **EU-mTR ISO compliant data elements** defined in clause 3.1.2 SHALL be as specified in clause xx of [ISO/IEC 7367-3].

Member States MAY add additional namespaces under their responsibility. References to those specifications are given in clause 2.4. The namespace for **EU-mTR Member State specific data elements** SHALL be as specified in clauses xxx and xxx of [ISO/IEC 7367-3] appended by the respective country code of the Member State after a period and optionally followed by a version number.

#### 3.1.2 EU-mVRC ISO compliant data elements
