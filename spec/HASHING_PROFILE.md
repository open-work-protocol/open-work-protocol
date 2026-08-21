# OWP Hashing Profile 0.2

Portable commercial/work identity must not depend on one language's JSON serializer.

## Rule

Normative OWP artifacts that are hashed MUST be serialized using the RFC 8785 JSON Canonicalization Scheme (JCS) over the restricted OWP hashed-artifact domain below, then hashed with SHA-256 and rendered as lowercase `sha256:<hex>`.

## OWP hashed-artifact restrictions

To keep every supported language deterministic and avoid financial floating-point ambiguity:

- monetary quantities are decimal **strings**, never JSON floating-point numbers;
- object/property names are ASCII;
- JSON floating-point numbers are forbidden inside hashed artifacts;
- integer values must fit the interoperable IEEE-754 safe integer range;
- extension payloads included in a hashed artifact must obey the same restrictions.

These restrictions are intentionally narrower than general JSON and make the reference canonicalizer deterministic across OWP core schemas. Implementers may use a full RFC 8785 library.

## Test vectors

The TCK publishes canonical-byte and SHA-256 vectors. An implementation MUST pass them before claiming OWP-Core/0.2 conformance.
