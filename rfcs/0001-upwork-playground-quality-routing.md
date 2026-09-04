# RFC 0001: Optional OWP quality routing for Upwork AI Agent Playground

Status: Proposed integration profile

## Problem

A marketplace may already own customer acquisition, job posting, platform identity, transport, contractual rails, feedback, and default assignment behavior. OWP should not replace those systems merely to add portable quality selection and delivery evidence.

The Upwork AI Agent Playground is a concrete example. Public beta terms describe clients posting jobs through Upwork, participating AI partners retrieving job posts through an Upwork-provided API, and agents returning deliverables through that API. The client may not control which AI agent attempts the job. Upwork remains the marketplace and transport boundary.

OWP needs a clean opt-in mechanism that lets a marketplace expose a customer preference such as "prefer quality" while preserving the marketplace-native path as the default.

## Goals

1. Preserve Upwork-native behavior by default.
2. Let a client explicitly request OWP-backed quality routing.
3. Allow fully automated provider selection when OWP routing is selected.
4. Keep Upwork transport, identity, marketplace, legal, feedback, and delivery APIs outside OWP-Core.
5. Emit an auditable selection result without making the OWP reference scorer canonical.
6. Permit marketplace fallback when OWP routing cannot safely select a provider.

## Non-goals

- Reimplementing Upwork APIs.
- Circumventing marketplace assignment, authorization, contractual, or payment controls.
- Claiming an Upwork partnership, endorsement, or production API capability not publicly documented.
- Making OWP mandatory for marketplace jobs.
- Making the OWP reference quality scorer a standard-mandated scorer.

## Customer delivery preference

An integrating marketplace SHOULD expose two semantic modes:

```text
DEFAULT_MARKETPLACE
PREFER_QUALITY
```

`DEFAULT_MARKETPLACE` MUST be the default when no explicit preference is present.

`PREFER_QUALITY` means the marketplace or its authorized integration asks an OWP router to select among OWP-eligible providers that have produced a valid `ACCEPT` decision for the same work.

The preference is marketplace UX, not a new OWP-Core object. An implementation MAY encode it in `WorkIntent.extensions` under an integration-owned namespace.

Example:

```json
{
  "extensions": {
    "marketplace.openwork.delivery": {
      "preference": "PREFER_QUALITY",
      "fallback": "DEFAULT_MARKETPLACE"
    }
  }
}
```

## Selection contract

When `DEFAULT_MARKETPLACE` is active:

- OWP MUST NOT change provider assignment.
- The integration MAY still create OWP delivery evidence after the marketplace selects a provider, but that is outside this RFC.

When `PREFER_QUALITY` is active:

1. Convert the marketplace job into a `WorkIntent` or bind it to an existing `WorkIntent`.
2. Produce the minimum review capsule permitted by the marketplace and privacy policy.
3. Collect OWP `ProviderDecision` values from eligible providers.
4. Discard `PASS`, expired, malformed, unauthorized, or work-id-mismatched decisions.
5. Score only valid `ACCEPT` providers using the configured scorer.
6. Select deterministically among equal scores.
7. Emit an award record containing at least work id, selected provider id, score, scorer identifier, and fallback status.
8. Hand the selected provider identifier back to the marketplace adapter. The adapter may proceed only through actions the marketplace authorizes.

OWP selection never grants marketplace authorization by itself.

## Fallback

The integration MUST declare one of these policies:

- `DEFAULT_MARKETPLACE`: if OWP cannot produce an authorized award, return control to the normal marketplace path.
- `FAIL_CLOSED`: stop and request client action.

For an Upwork-style integration, this RFC recommends `DEFAULT_MARKETPLACE` so the optional quality path cannot break ordinary job posting.

Fallback reasons SHOULD be machine-readable, including:

```text
NO_ELIGIBLE_PROVIDER
NO_ACCEPTS
MISSING_PROFILE
SCORER_ERROR
MARKETPLACE_REJECTED_SELECTION
OWP_DISABLED
```

## Marketplace adapter boundary

The adapter owns vendor-specific behavior:

```text
receive_job()
normalize_job()
list_owp_eligible_providers()
request_provider_decisions()
apply_award_if_authorized()
submit_delivery()
```

The core OWP router owns only OWP semantics and deterministic quality selection.

An adapter MUST NOT claim that a marketplace supports client-directed provider assignment unless the marketplace actually exposes that capability to the integration.

## Upwork AI Agent Playground mapping

Based on Upwork's public beta terms as reviewed on 2026-09-04:

| Playground concept | OWP integration concept |
| --- | --- |
| Job Post | source for `WorkIntent` |
| AI Partner / AI Agent | provider implementation |
| Playground API retrieval | marketplace transport adapter |
| agent Deliverable | payload represented or referenced by `DeliveryManifest` |
| client feedback | input to `CustomerDisposition` and reputation evidence |
| normal Upwork job posting | `DEFAULT_MARKETPLACE` path |
| opt-in quality preference | `PREFER_QUALITY` path owned by the integrating product |

The public beta terms state that a client may not have an opportunity to direct which AI agent engages with a job. Therefore a real Upwork integration MUST treat OWP's selected provider as a routing recommendation unless and until an authorized Upwork API or program agreement permits the integration to apply that selection.

## Security and privacy

- The quality router MUST use a review capsule rather than unrestricted private repository data before award when full disclosure is unnecessary.
- Marketplace credentials MUST stay in the adapter and MUST NOT enter OWP objects.
- Job metadata is untrusted input and MUST be treated as potentially prompt-injecting content.
- Provider scores MUST be explainable enough to audit which evidence contributed to an award.
- Automatic selection MUST be bounded to providers already eligible under marketplace and OWP policy.

## Compatibility

This is an integration profile. It changes no OWP-Core 0.2 wire object and requires no protocol version bump.

## Rejected alternatives

### OWP replaces Upwork assignment

Rejected. It would incorrectly make the protocol own vendor authorization and marketplace mechanics.

### OWP quality routing is the default

Rejected. The integration is deliberately optional. Existing marketplace behavior remains the safest compatibility default.

### Use marketplace star rating only

Rejected as the OWP path. A marketplace may use its own ranking by default; the purpose of `PREFER_QUALITY` is to select using portable, task-specific evidence across OWP providers.

### Require the reference scorer

Rejected. OWP permits alternative scorers. The award must identify which scorer produced the decision.

## Public sources used for this mapping

- Upwork AI Agent Playground Participation Terms (Beta), version 1.2, effective 2025-07-29: https://www.upwork.com/legal
- Upwork announcement of MCP marketplace access, 2026-08-10: https://www.upwork.com/press/releases/upwork-talent-is-now-everywhere-ai-works

These sources describe public product boundaries only. This RFC does not claim access to non-public Playground API documentation or endorsement by Upwork.
