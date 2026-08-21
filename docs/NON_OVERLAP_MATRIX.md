# Non-Overlap Matrix

| Existing layer | It owns | OWP deliberately does not own | OWP composition point |
|---|---|---|---|
| A2A | opaque agent discovery/communication, Tasks, Messages, Artifacts, transports | agent RPC or task transport | one OWP Attempt may map to one A2A Task through an extension |
| MCP | model/agent access to tools, data, context | tool invocation/context protocol | a provider may use MCP internally; no OWP dependency |
| AP2 | cryptographic purchase authority/mandates | commerce/work semantics | optional authority reference for an Attempt |
| x402 | machine-native HTTP payment | work contract or quality routing | optional payment proof bound to Attempt IDs |
| ERC-8004 | portable identity/reputation/validation registries | one canonical quality algorithm | optional source/sink of trust evidence |
| Git | source history/content identity | task economics/customer rights | OWP-Git binds delivery to immutable Git state |
| GitHub/GitLab/etc. | forge, permissions, CI, PR/MR UX | source hosting | workspace adapters can use native app/token models |
| AGENTS.md | repository guidance for coding agents | work contract/economic lifecycle | provider agents can follow repository guidance while executing OWP work |
| OpenAPI | API interface description | outcome-work semantics | OWP HTTP surfaces may be described with OpenAPI |

## Architectural rule

If an OWP proposal duplicates a responsibility already owned by an adjacent standard, the default action is **bind, do not absorb**.
