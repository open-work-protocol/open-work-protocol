# Git Work Profile — OWP-GIT/0.2

## Resource

```json
{
  "forge": "github",
  "repository": "owner/name",
  "base_ref": "main",
  "base_sha": "optional"
}
```

## Strong delivery evidence

- base SHA;
- result SHA;
- tree SHA;
- branch/PR;
- changed-file summary;
- build/test commands or CI identity;
- CI references;
- artifact digests;
- deployment evidence if contracted.

## Fresh validation

```text
fresh isolated environment
-> authorized snapshot
-> checkout exact result SHA
-> install
-> build
-> native tests
-> contract-specific acceptance
-> negative/security checks
-> evidence bundle
```

The tested commit must equal the delivered commit.

For GitHub, prefer least-privilege GitHub App installation tokens scoped to required repositories/permissions and never expose user PATs to agents.
