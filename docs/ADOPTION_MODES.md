# Incremental Adoption Modes

No organization needs to adopt the entire OWP ecosystem.

## Mode 1 — Object-only

Parse/emit WorkContract, Attempt, DeliveryManifest, CustomerDisposition, and HandoffManifest in an existing product. Keep all existing transport and payments.

## Mode 2 — Provider shim

Add `review -> ACCEPT/PASS`, `execute -> DeliveryManifest`, and `handoff -> HandoffManifest` to an existing orchestrator. Internal agents/models remain unchanged.

## Mode 3 — Git evidence

Adopt OWP-Git only for portable delivery/validation evidence.

## Mode 4 — A2A binding

Carry OWP objects/identifiers as an A2A extension while using normal A2A Task/Artifact lifecycle.

## Mode 5 — Commerce binding

Attach an existing payment/authority system to Attempt IDs. x402/AP2 are reference profiles, not mandatory rails.

## Mode 6 — Trust/quality

Publish or consume evidence in an external reputation/validation system. No canonical OWP score is required.

## Mode 7 — Human gateway

Hide the protocol behind plain-language intake and approval. The customer does not need to know OWP exists.
