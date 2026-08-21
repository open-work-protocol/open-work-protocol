# OWP Versioning and Compatibility

OWP objects carry a protocol version. Profiles/extensions version independently.

## Pre-1.0

Breaking changes are allowed but MUST be explicit, documented, and accompanied by updated TCK vectors/migration notes.

## 1.0 and later

- Unknown optional fields remain ignorable.
- Required semantic changes require a new compatible feature/profile version or protocol major version.
- Implementations SHOULD support a reasonable deprecation window; the project should prefer extensions/profiles over frequent core breakage.
- TCK scenarios are release gates for normative behavior.

## Capability declaration

Implementations should advertise profile/version pairs, e.g.:

```text
OWP-Core/0.2
OWP-Git/0.2
OWP-Simple/0.2
```

No implementation should claim a profile/version it has not tested against that profile's published conformance suite.
