# OWP Standards Committee Packet — 0.2

## Requested review

Review the **outcome-work semantic layer**, not a marketplace product.

Question for reviewers:

> Is there value in a vendor-neutral, transport-neutral contract for customer-posted outcome work, immutable attempts, delivery evidence, customer disposition, and provider handoff — without changing ownership of A2A, MCP, payments, Git, or orchestrator internals?

## Proposed disposition today

**Incubate independently; do not request core-standard status yet.**

The project should approach an existing standards community only after external interoperability gates are met. The first likely proposal is a narrow A2A experimental extension/binding, not a new agent transport.

## Why this is not a request for ownership transfer

No reviewing organization is asked to:

- route traffic through an OWP service;
- use a founder wallet/broker/scorer;
- change its agent framework;
- disclose provider costs/prompts;
- adopt x402/AP2/ERC-8004;
- change repository ownership or merge authority;
- recognize OWP as exclusive.

## Normative surface

The smallest useful shared semantics are:

1. WorkContract
2. Attempt
3. DeliveryManifest
4. CustomerDisposition
5. HandoffManifest

WorkIntent and ProviderDecision support open routing but can remain optional in environments that already have procurement/routing systems.

## Existing-standard boundaries

See `NON_OVERLAP_MATRIX.md`. OWP binds to adjacent standards instead of recreating them.

## Evidence in this repository

- 21 test cases across lifecycle, Git, human gateway, standards invariants, and portability;
- 20 TCK vectors;
- real local Git golden journey with fresh clones and provider handoff;
- pre-1.0 migration fixing float/hash ambiguity;
- public governance/IP/antitrust/trademark policies;
- no required founder-operated service.

## What is still missing before foundation submission

These are ecosystem gates, not code TODOs:

- two unaffiliated implementations;
- real third-party Git work;
- an external implementer running the TCK;
- multi-organization maintainers;
- security review of a production implementation.

The project MUST NOT represent these as complete until they exist.
