# Validation Tiers

Not every aspect of useful work is machine-judgeable. OWP must not fake objectivity.

## D — Deterministic

Examples: fresh clone, build, native tests, schema checks, exact files, API responses, deployment health.

A deterministic validator can independently repeat these checks.

## E — Evidence-backed

Examples: screenshot exists, accessibility report, license-search report, benchmark artifact, deployment URL, generated document package.

The validator can verify evidence presence/integrity and some properties, but not necessarily subjective quality.

## H — Human-judged

Examples: "the brand feels right", aesthetic preference, strategic judgment, final customer taste.

These remain explicit customer/human acceptance items.

## Meaning of VALID_DELIVERY

`VALID_DELIVERY` means the delivery satisfied the named machine/evidence validator policy and is legitimately ready for the next customer decision. It MUST NOT be represented as proof that subjective H-tier criteria are liked by the customer or that all legal obligations are complete.

A WorkContract SHOULD label acceptance requirements by tier.
