# Stakeholder Objection Matrix

This is a design test, not evidence of endorsement by any named organization.

| Reviewer | Likely objection | OWP answer | Ownership change required? |
|---|---|---|---|
| A2A / Google | "Why is this not just A2A?" | OWP owns outcome-work commercial/validation semantics; A2A retains transport/Tasks/Artifacts. First standardization path is an optional extension. | No |
| GitHub / forge vendor | "Do we have to cede repo/workflow control?" | OWP-Git references native commits/PRs/CI and uses forge-native permissions. Merge authority stays with repository owners. | No |
| Anthropic / MCP | "Does this compete with MCP?" | MCP remains model/tool/context integration. An MCP-based orchestrator can implement OWP-Core without changing MCP. | No |
| OpenAI / coding agents | "Do we have to expose our internal harness?" | Provider internals are explicitly opaque. OWP standardizes only external contract/delivery boundaries. | No |
| Independent orchestrator | "Do we have to reveal token economics or bid lower?" | Public decision is ACCEPT/PASS; costs remain private; no reverse auction. | No |
| Independent OSS maintainer | "Does this override maintainer authority or force crypto?" | No. OWP-Core/Git can be used without payment; maintainers retain merge/release authority. | No |
| Enterprise buyer | "Does conformance mean secure/certified?" | No. OWP conformance covers wire/lifecycle semantics; enterprise security remains an implementation/control responsibility. | No |
| Payment/identity vendor | "Does OWP pick winners?" | Commerce and trust are optional profiles; competing rails/registries remain valid. | No |

## Committee rule

If a future OWP change makes any row require a third party to surrender control of its existing layer, that change carries a presumption of rejection.
