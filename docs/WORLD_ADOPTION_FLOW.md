# World Adoption Flow

## User experience

A normal user experiences:

```text
Tell me what you need
-> See what you'll get and the price
-> Approve
-> Work happens
-> Review the finished result
-> Accept or request a paid change
```

OWP is invisible.

## Provider experience

```text
Receive redacted job capsule
-> privately estimate cost/risk
-> ACCEPT/PASS
-> if selected, receive contract + scoped workspace
-> use existing orchestrator
-> emit Git/evidence manifest
-> earn portable proof/reputation
```

OWP does not invade provider internals.

## Ecosystem adoption wedge

### Wedge 1: evidence
Support OWP-Git DeliveryManifest in existing coding orchestrators. Immediate value: a common definition of what was delivered.

### Wedge 2: transferable work
Add Attempt + HandoffManifest. Immediate value: failed/declined revisions can move between orchestrators without restart.

### Wedge 3: routing
Add ReviewCapsule + ACCEPT/PASS. Immediate value: orchestrators can discover profitable work without reverse-auction price disclosure.

### Wedge 4: A2A
Add the optional A2A extension so OWP attempts travel over a widely adopted agent transport.

### Wedge 5: commerce/trust
Add x402/AP2/ERC-8004 profiles where autonomous settlement/authority/portable trust is valuable.

## Institutional strategy

First earn interoperability with code/TCK and multiple implementers. Then, if the community wants it, pursue an appropriate neutral governance home. Do not claim endorsement or ownership by existing foundations/standards projects.
