# AP2 Authority Profile — Experimental

AP2 can secure customer-agent -> merchant/broker spending authority.

Provisional constraint type:

```text
org.openworkprotocol.work-budget.0.1
```

Conceptual constraint:

```json
{
  "work_id": "owp_...",
  "merchant": "merchant-id",
  "max_total": "3000.00",
  "attempt_max": "1000.00",
  "max_revision_count": 2,
  "contract_hash": "sha256:...",
  "expires_at": "2026-09-20T00:00:00Z"
}
```

A deterministic evaluator rejects mismatched work/merchant/contract, expired authority, excess attempt amount, excess cumulative total, or excess revision count.
