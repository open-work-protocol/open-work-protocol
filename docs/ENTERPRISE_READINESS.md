# Enterprise Readiness Boundary

OWP specifies evidence and lifecycle semantics; it does not certify an implementation as secure.

A production deployment handling private repositories or material payments should independently address:

- tenant isolation and authorization;
- short-lived least-privilege repository credentials;
- untrusted-code sandboxing;
- egress/secret controls;
- audit retention and privacy policy;
- idempotent payment/attempt transitions;
- signature/key rotation where signatures are used;
- validator independence proportional to value at risk;
- supply-chain provenance/SBOM policy where appropriate;
- human/legal review for subjective, regulated, or safety-critical acceptance;
- incident response and security disclosure.

OWP conformance is **not** equivalent to enterprise-security certification.
