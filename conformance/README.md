# Conformance seed

Implementations should prove:

1. WorkIntent parses and is treated immutable after publication.
2. ProviderDecision exposes ACCEPT/PASS, not provider price negotiation.
3. Contract hash binds exact locked contract.
4. Attempt revision numbers/parents remain coherent.
5. VALID_DELIVERY is distinct from customer disposition.
6. STEER/REJECT carry feedback.
7. PASS preserves history and permits handoff.
8. Hash-linked events detect tampering.
9. Unknown optional extension fields do not break parsing.
