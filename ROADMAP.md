# Roadmap

OWP is evidence-gated, not version-number-gated. See `docs/ROADMAP_6_12_MONTHS.md`.

## Current 0.2 seed

- transport-neutral work-contract semantics;
- A2A-first optional binding;
- Git evidence + fresh-clone validation;
- plain-language no-repo customer gateway;
- redacted provider review capsule;
- ACCEPT/PASS quality routing;
- optional marketplace routing with native-marketplace default and explicit `PREFER_QUALITY` OWP selection;
- guarded Upwork AI Agent Playground adapter boundary that never invents vendor authorization;
- paid-attempt/revision semantics with commerce optional;
- cross-provider handoff;
- 20 TCK vectors plus executable protocol/integration tests;
- standards-grade governance/IP/antitrust/non-overlap packet.

## Marketplace integration gates

The OWP side of optional quality routing is executable. A real Upwork deployment additionally requires capabilities outside this repository:

1. authorized Upwork AI Agent Playground integration access and applicable agreement;
2. exact current vendor API schema, authentication, rate-limit, retry, and idempotency behavior;
3. confirmation of whether the integration may apply an OWP-selected provider or must use the award only as a recommendation;
4. privacy/security review of job-to-ReviewCapsule transformation;
5. shadow-routing outcome data before client-facing automated selection;
6. kill switch that returns every job to the native Upwork path.

OWP must not claim these vendor-side gates are complete merely because the protocol adapter exists.

## Next protocol gates

1. second unaffiliated implementation;
2. external TCK run;
3. real Git work and handoff;
4. multi-organization maintainers;
5. production security review;
6. only then, smallest appropriate standards/foundation proposal.

## 1.0

Requires real compatibility history. No self-imposed calendar date.
