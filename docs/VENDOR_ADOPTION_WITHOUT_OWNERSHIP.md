# Adoption Without Ownership Changes

This is a standards-review simulation, not a claim that any named organization endorses OWP.

## Google / A2A ecosystem

Possible adoption: treat OWP as an independent work-contract extension carried by A2A Tasks/Artifacts.

What does **not** change:
- A2A owns transport/task semantics and its own governance;
- Google/A2A implementations do not route through an OWP service;
- A2A can reject, modify, or never host the extension;
- OWP cannot claim an A2A namespace without A2A approval.

Value: standard paid/outcome semantics above A2A without a core protocol fork.

## GitHub / Git forge ecosystem

Possible adoption: emit/validate OWP-Git DeliveryManifests, expose least-privilege workspace integrations, or surface OWP work state in native PR/Actions UX.

What does **not** change:
- GitHub owns its authentication, Apps, repositories, Actions, billing, and UX;
- OWP never receives organization ownership or long-lived credentials;
- OWP-Git is forge-neutral and cannot make GitHub mandatory.

Value: portable evidence for agent-produced work, including work that moves between orchestrators.

## Anthropic / MCP ecosystem

Possible adoption: providers built with MCP can execute OWP work; MCP servers/tools remain entirely internal to provider execution.

What does **not** change:
- MCP remains the model/tool/context protocol;
- OWP defines no MCP tool semantics and requires no MCP changes;
- Anthropic does not need to adopt A2A, x402, or an OWP broker to implement OWP-Core.

Value: an MCP-based orchestrator can participate in cross-vendor paid work without exposing its internal tool graph.

## OpenAI / AGENTS.md ecosystem

Possible adoption: coding orchestrators use repository-native AGENTS.md guidance while OWP carries the external work contract/delivery boundary.

What does **not** change:
- AGENTS.md remains repository guidance;
- OpenAI/orchestrator internals, models, APIs, and coding workflows remain private;
- OWP cannot require a specific coding harness.

Value: repo guidance and external work-contract semantics compose instead of competing.

## Independent OSS maintainers

Possible adoption: publish a fixed-scope work request, receive ACCEPT/PASS from trusted orchestrators, and validate a PR/commit using OWP-Git. Payment can be absent, sponsored, or handled off-protocol.

What does **not** change:
- repository governance and maintainer merge authority remain local;
- OWP cannot force acceptance of generated code;
- no chain, wallet, commercial broker, or proprietary service is required.

Value: portable machine-readable work sponsorship and evidence without surrendering maintainer authority.
