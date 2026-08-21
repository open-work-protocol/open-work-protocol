# Minimal Provider Adoption

An existing orchestrator can begin with **OWP-Core + OWP-Git**. No wallet or chain is required.

## Integration surface

1. Read a WorkIntent/ReviewCapsule.
2. Return `ACCEPT` or `PASS`.
3. When selected, map the locked WorkContract into your existing orchestrator request.
4. Execute however you already execute.
5. Emit DeliveryManifest with exact Git/evidence references.
6. Respond to a paid revision with `REMEDY` or `PASS`.
7. On PASS, export HandoffManifest.
8. Run the TCK.

Your model prompts, sub-agent topology, token budgets, framework, and private profit model stay private.

Add OWP-A2A only if you want A2A transport. Add OWP-Commerce only if you want standardized machine payment. Add OWP-Trust only if you want portable reputation/validation records.
