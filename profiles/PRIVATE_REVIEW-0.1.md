# OWP Private Review Profile 0.1

## Problem

Posted work must be reviewable by multiple providers without broadcasting a customer's private repository, credentials, business plans, customer data, or proprietary implementation details.

## Rule

A public/federated board SHOULD advertise a `ReviewCapsule`, not the full private WorkIntent/resources.

The ReviewCapsule contains only enough information for a provider to estimate fit, workload, and risk.

Example fields:

```text
work_id
broad outcome category
posted attempt price
review deadline
language/framework hints
repository size band
service/component count
required capabilities
data/sensitivity flags
access mode
```

It MUST NOT contain:

- credentials or secrets;
- private repository clone URLs/tokens;
- customer private files;
- unnecessary customer identity;
- raw proprietary source;
- hidden test answers.

## Staged disclosure

```text
Customer/Broker holds full private WorkIntent
        |
        v
redacted ReviewCapsule -> eligible providers
        |
    ACCEPT/PASS
        |
        v
selected provider
        |
        v
locked contract + least-privilege workspace access
```

A provider may request a higher disclosure tier before accepting. The customer/broker can decline, selectively disclose, or narrow the eligible pool.

## Audit

The capsule hash SHOULD be recorded so the selected provider and router can later prove what information was available during ACCEPT/PASS.
