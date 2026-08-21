# OWP Extension Model 0.2

Core objects may carry an `extensions` object.

- Extension keys MUST be globally scoped printable-ASCII identifiers, preferably URIs/URNs controlled by the extension publisher.
- Unknown optional extensions MUST be preserved when proxying and ignored when interpreting core semantics.
- A required extension MUST be declared by the surrounding profile/capability negotiation; silently treating an unknown required extension as optional is non-conformant.
- Extension fields MUST NOT redefine the meaning of existing core fields.
- New universal semantics belong in a new OWP core version after interoperability evidence, not in an unscoped top-level field.

OWP does not reserve another project's namespace. An A2A-hosted identifier may only be used after approval by A2A governance.
