# RFC-0003 — Git Evidence

Status: Seed.

"Agent says done" is not enough for paid engineering.

Git-profile work should bind exact source state to independent fresh-environment validation.

Minimum strong evidence:

- base SHA;
- result SHA;
- contract hash;
- exact build/test/CI identity;
- validator result;
- DeliveryManifest hash.

High-value policies may add deployment checks, SBOM/provenance, multiple validators, or human review.
