# Trust Model

OWP separates:

1. identity — who is the actor?
2. authority — may the actor spend/modify?
3. payment — was this attempt funded/settled?
4. delivery — what artifacts did the provider produce?
5. quality — did independent validation and history support success?

No single signature proves all five.

Recommended evidence graph:

```text
WorkContract hash
  +-- authority proof
  +-- payment proof
  +-- provider identity
  +-- DeliveryManifest hash
        +-- Git commit/tree
        +-- CI/build evidence
        +-- validator response
        +-- reputation evidence
```

Customer feedback is useful but not enough. Quality routers should weight verified transactions, machine validation, sample size, recency, source trust, and task/domain fit.
