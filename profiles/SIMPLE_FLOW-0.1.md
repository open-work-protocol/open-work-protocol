# OWP Simple Flow Profile 0.1

Status: Experimental human-gateway profile. This profile does not change OWP core.

## Goal

A person must be able to purchase OWP-backed work without knowing what OWP, Git, A2A, x402, AP2, ERC-8004, a manifest, or a validator is.

The visible flow is exactly five stages:

```text
1. DESCRIBE
2. PREVIEW
3. APPROVE
4. WORK
5. RECEIVE
```

### 1. DESCRIBE

The user supplies only what they know:

- goal in natural language;
- budget or maximum spend;
- optional files/links/accounts;
- optional deadline.

A gateway MUST NOT require a Git repository. If Git is needed and none exists, the gateway MAY provision one and MUST preserve an export/transfer path for the customer.

### 2. PREVIEW

Before charge/authorization, show a Plain Contract Card containing:

- **What you asked for**
- **What you will receive**
- **What is not included**
- **Price for this attempt**
- **Maximum possible spend under currently approved revision rights**
- **What counts as ready to review**
- **What the system still needs from you**

The visible card MUST NOT require protocol vocabulary.

### 3. APPROVE

Human-present mode requires an explicit approval of the Plain Contract Card and amount.

Autonomous customer-agent mode MAY use an external signed authority system, but the same human-readable summary SHOULD remain available for audit.

### 4. WORK

The visible status vocabulary is:

```text
Getting ready
Working
Need something from you
Ready to review
```

Internal OWP states remain machine-readable underneath.

### 5. RECEIVE

The visible choices are:

```text
Looks good
Change something
Doesn't meet what I asked for
```

They map to:

```text
Looks good                         -> APPROVE
Change something                   -> STEER
Doesn't meet what I asked for      -> REJECT
```

STEER/REJECT consumes another paid revision only after a provider accepts that revision and the customer/agent is authorized to pay it.

## Human Gateway conformance

A conforming Simple Flow gateway MUST:

1. accept a natural-language goal and numeric budget;
2. work when the customer has no repository;
3. show a plain-language contract card before an initial charge;
4. show maximum authorized exposure separately from current charge;
5. avoid protocol/cryptocurrency/Git terminology in the default customer flow;
6. make INPUT_REQUIRED free when it only supplies already-contracted information;
7. distinguish Change something from Doesn't meet what I asked for while making their paid-revision economics explicit;
8. export the final artifact/source/evidence in a customer-portable form;
9. preserve applicable refund, fraud, payment-dispute, accessibility, privacy, and consumer-law obligations outside OWP technical validity.
