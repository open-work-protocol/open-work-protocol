# ERC-8004 Profile — Experimental

ERC-8004 can supply portable identity, raw reputation, and validation records.

OWP SHOULD NOT define one universal on-chain quality score.

Suggested tags:

```text
owp.valid-delivery
owp.contract-fidelity
owp.build
owp.tests
owp.security
owp.first-attempt
owp.handoff
owp.on-time
owp.domain.<domain>
owp.value-band.<band>
```

Off-chain evidence should bind work ID, contract hash, attempt ID, DeliveryManifest hash, validator policy/version, and payment proof where appropriate.

Scorers should treat raw feedback as potentially Sybil/spam influenced and weight source trust, verified transactions, validation, recency, and sample size.
