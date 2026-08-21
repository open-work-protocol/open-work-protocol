# x402 Binding Profile — Experimental

OWP does not define a payment rail. x402 is a natural HTTP-native profile.

Provisional extension key:

```text
owp-work
```

Bind payment metadata to:

```json
{
  "workId": "owp_...",
  "contractHash": "sha256:...",
  "attemptId": "attempt_...",
  "providerId": "provider:...",
  "chargeType": "base|revision"
}
```

A settlement evidence record should capture payment identifier/proof, network/scheme, amount, payer, payee, work ID, attempt ID, and contract hash.

Payment receipts prove economic interaction; DeliveryManifest/validator evidence prove the associated work.
