# Contributing

The most valuable contributions are independent implementations and failure cases.

Good first ecosystem work:

- implement `ProviderDecision` in another language;
- emit `DeliveryManifest` from another orchestrator;
- build a different quality scorer;
- run a WorkIntent through two unrelated providers;
- test PASS -> Handoff -> second-provider completion;
- build the A2A extension adapter;
- bind one real x402 test payment to an Attempt;
- publish ERC-8004 evidence backed by real Git work;
- attack the economics and schemas.

Protocol changes belong in `rfcs/` and should state problem, wire impact, security/economic impact, compatibility, and rejected alternatives.
