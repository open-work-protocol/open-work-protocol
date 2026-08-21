# Standardization Path

OWP should earn adoption before asking for institutional legitimacy.

## Stage 0 — Independent experiment

- public Apache-2.0 repository;
- reference implementation;
- test vectors/TCK;
- at least two provider implementations;
- real public Git work;
- published incompatibility/failure reports.

## Stage 1 — A2A extension proposal

A2A's current extension governance permits independent extensions and defines a proposal -> maintainer sponsorship -> experimental -> official path for extensions hosted under the A2A organization.

OWP should first publish independently, then open an A2A proposal containing:

- abstract;
- motivation;
- why core A2A does not already solve paid outcome semantics;
- initial technical approach;
- reference implementation;
- TCK evidence;
- at least one non-founding implementer if possible.

Do not imply A2A endorsement before maintainer sponsorship/approval.

## Stage 2 — Experimental A2A incubation, if invited/sponsored

If an A2A maintainer sponsors the proposal, adapt namespace/repository conventions to the official experimental-extension process and keep OWP's independent compatibility vectors mirrored.

## Stage 3 — Ecosystem implementations

Target orchestrators, not end users:

> Add OWP-Core + OWP-Git so your orchestrator can accept portable outcome work and emit evidence without changing its internal architecture.

Then optionally add A2A/Commerce/Trust.

## Stage 4 — Neutral institutional home

MCP, A2A, x402, and OpenAPI show a recurring pattern: useful technology earns ecosystem adoption, then neutral governance reduces vendor-risk and fragmentation.

A neutral foundation should be pursued only when OWP has multiple independent implementers and a real governance constituency. No specific foundation is promised by this protocol.
