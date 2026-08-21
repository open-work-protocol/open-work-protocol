# Plain-Language Mapping

OWP is machine infrastructure. Customer-facing products should translate it.

| Internal term | Default customer language |
|---|---|
| WorkIntent | What you need |
| WorkContract | What we'll deliver |
| attempt_price | Price for this try |
| max_revisions | Changes you can request |
| Provider | Work team |
| Quality Router | hidden |
| VALID_DELIVERY | Ready to review |
| CustomerDisposition | Your decision |
| APPROVE | Looks good |
| STEER | Change something |
| REJECT | Doesn't meet what I asked for |
| PASS | hidden; another work team may continue |
| HandoffManifest | hidden; continuation record |

The default customer UI should never expose hashes, manifests, protocol bindings, wallet addresses, or reputation registries unless the user opens an advanced/audit view.
