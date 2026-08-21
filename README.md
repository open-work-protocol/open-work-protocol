# Open Work Protocol (OWP)

**A transport-neutral open work-contract layer for finished outcomes.**

OWP is an open semantic protocol/profile, originally imagined by **Keeltrace** and deliberately designed for community ownership. It does **not** replace A2A, MCP, payment rails, Git, or any orchestrator. It standardizes only the portable work-contract layer between:

- a customer (or customer agent) with a Git-solvable outcome and a posted budget; and
- independent agent orchestrators capable of doing real engineering work and returning a verifiably finished product.

OWP is **not** a reverse auction and does not prescribe how an orchestrator works internally.

The customer posts the outcome and price. Eligible providers privately estimate whether the job is profitable and answer **ACCEPT** or **PASS**. Among acceptors, a quality router selects the provider most likely to finish *this exact class of work*. Work proceeds through immutable paid attempts, independent validation, bounded customer steer/reject rights, portable handoff, and evidence-backed reputation.

## Ownership posture

> **Imagined by Keeltrace. Built in Git. Owned by no vendor. Usable by the world.**

There is no required vendor service, transport, wallet, model, broker, validator, scorer, registry, forge, or cloud. A vendor can implement one OWP profile while retaining every existing product and protocol boundary. See `spec/SCOPE.md` and `docs/NON_OVERLAP_MATRIX.md`.

## The seven core objects

1. `WorkIntent`
2. `WorkContract`
3. `ProviderDecision`
4. `Attempt`
5. `DeliveryManifest`
6. `CustomerDisposition`
7. `HandoffManifest`

A hash-linked `WorkEvent` envelope preserves history.

## Core flow

```text
Customer / Customer Agent
        |
        | goal + repo/context + posted price
        v
    WorkIntent
        |
        v
   REVIEW_OPEN
        |
        +------ Provider A -> ACCEPT
        +------ Provider B -> PASS
        +------ Provider C -> ACCEPT
        |
        v
  Quality Router
        |
        v
 WorkContract lock
        |
        v
 paid Attempt
        |
        v
 orchestrator team
        |
        v
 DeliveryManifest
        |
        v
 independent validator
        |
        +---- INVALID -> repair
        |
        v
  VALID_DELIVERY
        |
        +---- attempt payout
        |
        v
 customer disposition
   /       |       \
APPROVE  STEER    REJECT
   |        |        |
 close      +--- new paid Attempt
                    |
              REMEDY or PASS
                    |
             optional handoff
```


## Start with the part you need

OWP is intentionally incremental:

- **OWP-Core** — portable work/attempt/delivery/handoff semantics.
- **OWP-Git** — content-addressed software evidence.
- **OWP-Simple** — natural-language customer gateway; customers do not need a repository.
- **OWP-A2A** — optional A2A transport binding.
- **OWP-Commerce** — optional x402/AP2 payment + authority profile.
- **OWP-Trust** — optional ERC-8004 identity/reputation/validation profile.

No payment rail, chain, agent framework, broker, or reputation system is required to implement OWP-Core.

## Strongest included proof

Run the integrated golden journey:

```bash
PYTHONPATH=src python3 -m owp.cli golden-demo --json
```

It exercises a nontechnical no-repo request through automatic Git provisioning, redacted multi-provider review, quality routing, real Git delivery, fresh-clone validation, a paid customer change, provider PASS/handoff, second-provider delivery, final approval, and source export.

Run conformance:

```bash
PYTHONPATH=src python3 -m owp.cli tck
```

Run the reference plain-language preview gateway:

```bash
PYTHONPATH=src python3 -m owp.web_gateway --port 8080
```

The browser-facing reference deliberately hides Git/protocol/payment-registry vocabulary.

## Run it

Python 3.11+. No third-party runtime dependencies.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m owp.cli demo
```

Or:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
owp demo
```

## Repository map

```text
spec/        normative seed specification
schemas/     JSON Schemas
src/owp/     runnable reference core
openapi/     neutral Work Board HTTP surface
interop/     A2A/x402/AP2/ERC-8004/Git profiles
examples/    wire examples
tests/       executable semantics
docs/        architecture, trust, economics, adoption, threats
rfcs/        protocol evolution proposals
```

## Status

**OWP/0.2 — experimental seed, not a standard.**

The route to legitimacy is independent implementations, real Git jobs, conformance tests, adversarial review, and governance transfer away from any one founder.

## Standards-review packet

For multi-vendor / neutral-foundation review, start with:

- `docs/STANDARDS_COMMITTEE_PACKET.md`
- `spec/SCOPE.md`
- `docs/NON_OVERLAP_MATRIX.md`
- `docs/VENDOR_ADOPTION_WITHOUT_OWNERSHIP.md`
- `IP_POLICY.md`
- `ANTITRUST.md`
- `docs/ADOPTION_GATES.md`
- `docs/FOUNDATION_READINESS_CHECKLIST.md`

The repository deliberately distinguishes **technical readiness** from **external adoption or endorsement**. No named vendor or foundation is claimed to endorse OWP.
