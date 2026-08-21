# A2A Binding Profile — Experimental

OWP layers on A2A instead of replacing it.

Provisional extension identifier:

```text
urn:owp:a2a:work-contract:0.2
```

A production community specification should move to a durable community URI namespace.

## Agent Card

```json
{
  "capabilities": {
    "extensions": [{
      "uri": "urn:owp:a2a:work-contract:0.2",
      "description": "Open Work Protocol work-contract metadata",
      "required": false
    }]
  }
}
```

One paid OWP Attempt SHOULD map to one A2A Task.

OWP identifiers ride in extension metadata:

```json
{
  "owp": {
    "work_id": "owp_...",
    "contract_hash": "sha256:...",
    "attempt_id": "attempt_...",
    "revision": 1
  }
}
```

A2A context can group related Tasks within one server; OWP `work_id` remains the cross-provider identifier because handoff may move to another server.
