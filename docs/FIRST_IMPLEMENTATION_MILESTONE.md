# First implementation milestone

OWP should earn adoption through interoperability evidence, not announcement volume.

The first milestone is complete only when all of the following exist publicly:

1. the seed Python reference passes the TCK;
2. one **unaffiliated** implementation can parse/emit the OWP-Core objects;
3. one external provider adapter can return `ACCEPT|PASS` and a `DeliveryManifest`;
4. two providers can inherit the same Git work through a `HandoffManifest`;
5. an independent validator can fresh-clone the exact delivered SHA and reproduce the required checks;
6. at least one protocol ambiguity discovered by the second implementation is repaired through the public RFC process.

A2A/x402/AP2/ERC-8004 integration is valuable, but none is required to complete this milestone.

## The public challenge

> Implement only the smallest OWP slice you need. If OWP forces you to surrender your transport, orchestrator, payment system, scorer, forge, model stack, or customer relationship, file a spec bug: that is a protocol defect.
