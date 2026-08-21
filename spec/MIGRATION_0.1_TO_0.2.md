# Migration: OWP 0.1 -> 0.2

OWP is pre-1.0; 0.2 intentionally fixes portability issues before implementations accumulate.

## Monetary values

Before:

```json
{"attempt_price": 1000.0}
```

After:

```json
{"attempt_price": "1000.00"}
```

Profiles define currency/minor-unit policy; core treats amount as a non-negative decimal string.

## Contract hashes

0.2 hashed artifacts prohibit JSON floats and non-ASCII property names and use the hashing profile in `HASHING_PROFILE.md`.

Implementations MUST NOT compare a 0.1 hash to a 0.2 hash as if they represented the same wire artifact.

## Extensions

New experimental data should use the `extensions` map with a globally scoped key rather than unnamespaced top-level fields.

## Capability advertising

Advertise exact profile versions. A 0.2 implementation may separately support 0.1 during migration but must not silently reinterpret 0.1 payloads as 0.2.
