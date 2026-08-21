# Open Work Protocol 0.1 — Seed Specification

Status: Experimental / seed proposal.

Requirements words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY use RFC 2119 meanings.

## 1. Scope

OWP standardizes the commercial/work lifecycle for a posted-price outcome fulfilled by an opaque agent orchestrator.

OWP does not require a central marketplace.

## 2. Roles

- **Customer** — defines outcome, economics, revision budget, and resource authority.
- **Customer Agent** — acts for Customer under an external authority mechanism.
- **Work Board** — optional relay that advertises work and gathers ProviderDecisions.
- **Quality Router** — chooses among eligible ACCEPT decisions.
- **Provider** — orchestrator/team that evaluates and executes work.
- **Workspace Broker** — grants least-privilege work access.
- **Validator** — checks DeliveryManifest against WorkContract.
- **Settlement Adapter** — binds attempts to payment.
- **Reputation Adapter** — publishes/consumes portable quality evidence.

One deployment MAY combine roles.

## 3. Identifiers

Every WorkIntent MUST have `protocol_version` and globally unique `work_id`.

Every contract, attempt, delivery, disposition, event, and handoff MUST reference `work_id`.

`contract_hash` MUST be a deterministic hash of canonical locked WorkContract JSON.

## 4. WorkIntent

WorkIntent is the immutable customer offer.

It MUST include:

- goal;
- resources/repositories or explicit absence;
- posted attempt price;
- currency/unit;
- max paid revisions;
- review window;
- evidence policy.

A published WorkIntent MUST NOT be silently mutated. Corrections become new signed/versioned history.

### 4.1 Disclosure

WorkIntent/resources MUST NOT contain credentials. A public or federated board SHOULD expose a redacted ReviewCapsule rather than private source/resources during provider review. Full private resources SHOULD be disclosed only under explicit policy/authorization, normally after provider selection. See `profiles/PRIVATE_REVIEW-0.1.md`.

## 5. ProviderDecision

Public decision semantics are only:

```text
ACCEPT
PASS
```

Core intentionally has no provider-price field.

Providers MAY maintain private cost models. They MUST NOT alter posted attempt price through ProviderDecision.

## 6. Quality routing

Among ACCEPT decisions, a quality-routed implementation SHOULD estimate provider success for the specific work rather than use a global star average.

Possible factors:

- verified outcome history;
- domain fit;
- scale/value fit;
- contract fidelity;
- first-attempt success;
- revision success;
- handoff quality;
- reliability/abandonment;
- security;
- evidence quality;
- recency;
- sample-size uncertainty.

The algorithm is intentionally not canonical.

## 7. WorkContract

The WorkContract is the locked interpretation of the WorkIntent and MUST include:

- work ID;
- attempt economics;
- deliverables;
- acceptance requirements;
- evidence requirements;
- included/excluded scope;
- max revisions.

Contract formation MAY include clarification before funding. Provider cannot unilaterally increase the posted attempt price.

## 8. Attempt

An Attempt is the atomic paid execution unit.

Each Attempt MUST have a unique `attempt_id` and identify:

- work and contract;
- provider;
- revision number;
- parent attempt where applicable;
- payment/authority references where present.

A customer STEER/REJECT after valid delivery creates a new Attempt only if a provider accepts it.

Unused revision capacity SHOULD NOT be charged.

## 9. DeliveryManifest

Provider claims completion by publishing DeliveryManifest.

Git-profile delivery SHOULD include:

- repository;
- base commit;
- result commit;
- tree hash;
- branch/PR;
- build/test results;
- deployment/security evidence when required;
- contract acceptance mapping;
- evidence hashes.

`DELIVERED` is a provider claim, not `VALID_DELIVERY`.

## 10. Validation

Validator checks the DeliveryManifest against the locked contract.

Outcomes:

```text
VALID
INVALID
INDETERMINATE
```

Validator MUST NOT silently weaken acceptance requirements.

## 11. CustomerDisposition

After valid delivery:

```text
APPROVE
STEER
REJECT
```

STEER/REJECT MUST carry useful feedback.

Subjective dissatisfaction SHOULD NOT retroactively invalidate a machine-valid prior attempt. Applicable law and fraud/authorization disputes remain external requirements.

## 12. Remedy and PASS

After STEER/REJECT, current provider MAY:

```text
REMEDY
PASS
```

REMEDY accepts a new paid attempt.

PASS ends future obligation but preserves prior completed history. Another provider MAY accept the next attempt.

## 13. HandoffManifest

Handoff MUST preserve enough machine-readable reality for another provider to continue.

Git handoff SHOULD include:

- current repository/commit/tree;
- original intent and contract hashes;
- prior attempt IDs;
- customer prompts/dispositions;
- delivery/validation evidence;
- known blockers;
- remaining revisions;
- access references without secret values.

## 14. Input-required vs paid steer

Supplying information already contemplated by the locked contract MAY be free `INPUT_REQUIRED`.

Changing desired behavior, design, deliverable, technology, acceptance condition, or locked assumption SHOULD be paid STEER.

## 15. Payment

Payment rails are pluggable.

Attempt payment SHOULD bind:

```text
work_id
contract_hash
attempt_id
provider_id
amount
```

## 16. Authority

Authority systems are pluggable and SHOULD be able to constrain work ID, payee, max total, per-attempt max, revision count, contract hash, and expiry.

## 17. Event history

Commercial/work events SHOULD be append-only and tamper-evident.

Reference event chain:

```text
event[n].previous_hash == hash(event[n-1])
```

## 18. Security

Repository credentials MUST NOT be embedded in portable work objects.

Workspace access SHOULD be least-privilege, repository-scoped, permission-scoped, time-bounded, and revocable.

Validators executing untrusted code MUST use isolation appropriate to value at risk.

## 19. Extensions

Unknown optional extension fields MUST be ignored.

Required extensions MUST identify themselves/version explicitly.

## 20. Interop

Profiles in this repo compose OWP with A2A, x402, AP2, ERC-8004, and Git/GitHub. Those profiles do not become mandatory dependencies of core parsing.
