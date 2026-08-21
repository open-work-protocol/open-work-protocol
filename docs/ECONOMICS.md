# Economics

## Posted-price quality routing

The buyer sets the attempt price. Providers privately estimate token/compute/tool/risk cost and answer ACCEPT or PASS.

No provider price is in the core decision object.

This turns orchestration efficiency into provider margin rather than rewarding underbidding.

## Attempts

Commercial unit:

```text
Attempt 0: $1,000
Max revisions: 2
Maximum authorized exposure: $3,000
```

Unused revisions should not be pre-charged.

After `VALID_DELIVERY`:

- APPROVE -> close
- STEER -> request another paid attempt
- REJECT -> request another paid attempt

The provider may REMEDY or PASS.

## Distinguish validity from taste

A customer preference change should not retroactively erase a valid prior attempt. Fraud, unauthorized payment, duplicate charge, and legal reversal remain separate payment/dispute concerns.
