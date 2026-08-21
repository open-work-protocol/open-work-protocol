# Standards Positioning

## The smallest claim

OWP is **not a new agent transport**. It is a transport-neutral semantic contract for transferable outcome work.

The first external standardization target should be the smallest useful subset:

```text
WorkContract + Attempt + DeliveryManifest + CustomerDisposition + HandoffManifest
```

and an A2A binding that carries those semantics without changing A2A core behavior.

## Why not just add fields to A2A core?

Because paid-work economics, customer disposition, validation policy, and cross-provider commercial handoff are domain semantics rather than universal agent communication requirements. Keeping them in an extension avoids imposing commerce on every A2A implementation.

## Why not build a standalone marketplace protocol first?

Because central discovery/routing/payment would create unnecessary ownership and adoption fights. OWP's board/router/commerce implementations are optional products around the semantic core.

## Promotion principle

Prove independent implementations and interoperability before requesting official status from any standards organization.
