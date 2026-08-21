# Architecture

```text
A2A       agent communication + task lifecycle
x402      machine payment
AP2       purchase authority
ERC-8004  identity + raw reputation + validation hooks
Git       reproducible software state
OWP       paid outcome-contract semantics
```

## Roles

- Customer / Customer Agent
- optional Work Board
- Quality Router
- Provider Orchestrator
- Workspace Broker
- Validator
- Settlement Adapter
- Reputation Adapter

One operator may perform multiple roles. The protocol does not require a central server.

## Deployment modes

### Direct
A customer agent sends a WorkIntent to a known provider/broker.

### Board
A public/private Work Board advertises open WorkIntents and gathers ACCEPT/PASS.

### Federated
Multiple boards exchange signed WorkIntent references.

### Enterprise
An internal buyer routes work among approved orchestrator teams.

## Why Git first

Git gives cheap objective evidence:

- commit/tree identity;
- exact diff;
- clean checkout;
- native tests/CI;
- build artifacts;
- provenance/SBOM;
- deployment references;
- PR review;
- portable handoff.

OWP may generalize later, but Git is the proving ground.
