# OWP Implementation Profiles

OWP adoption is incremental. No implementation is required to install every adjacent standard.

## OWP-Core

Minimum portable work semantics:

- parse/emit WorkIntent, WorkContract, ProviderDecision, Attempt, DeliveryManifest, CustomerDisposition, HandoffManifest;
- preserve work/contract/attempt identifiers;
- support ACCEPT/PASS;
- keep VALID_DELIVERY distinct from customer disposition;
- preserve handoff history.

No payment, blockchain, A2A server, Git forge, or reputation system is required.

## OWP-Git

Adds content-addressed software delivery and fresh validation evidence.

Requires OWP-Core.

## OWP-A2A

Maps attempts to A2A Tasks and OWP metadata to an A2A extension.

Requires OWP-Core. Does not require OWP-Commerce.

## OWP-Commerce

Binds attempts to payment/authority evidence. x402 + AP2 are recommended profiles, not core dependencies.

Requires OWP-Core.

## OWP-Trust

Publishes/consumes portable identity, reputation, and validation evidence. ERC-8004 is a recommended profile, not a core dependency.

Requires OWP-Core.

## OWP-Simple

Human gateway profile for natural-language intake, plain contract preview, and simple review/steer decisions.

Requires OWP-Core underneath but customer-facing products do not expose protocol vocabulary.

## Conformance labels

An implementation SHOULD declare exactly which profiles and versions it supports. Examples:

```text
OWP-Core/0.2
OWP-Git/0.2
OWP-A2A/0.2
OWP-Simple/0.2
```

Implementations MUST NOT claim a profile they cannot pass in the corresponding TCK track.
