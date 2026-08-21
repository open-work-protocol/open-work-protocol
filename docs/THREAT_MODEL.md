# Threat Model

## Customer attacks
- free scope expansion disguised as clarification;
- subjective rejection to avoid paying;
- malicious repositories attacking review/validator infrastructure.

Mitigations: locked contracts, paid STEER, separate VALID_DELIVERY, sandboxing, no ambient secrets.

## Provider attacks
- accept-everything spam;
- evidence forgery;
- abandonment;
- malicious/backdoored code.

Mitigations: delivery-gated payout, independent fresh validation, reliability/security reputation, least privilege.

## Router attacks
- self-preferencing;
- opaque scoring manipulation.

Mitigations: pluggable routers, scorer/version recorded in routing event, portable evidence.

## Validator attacks
- provider collusion;
- unsafe execution.

Mitigations: multiple validators for high value, portable re-checkable evidence, hardened disposable sandbox.
