# Security

OWP touches code execution, repository credentials, money, signed authority, evidence, and reputation.

Never run untrusted repository builds on a broker host. Production validators/workspaces need disposable isolation, no ambient secrets, network policy, filesystem boundaries, CPU/memory/time limits, and explicit artifact export.

Never place long-lived Git credentials in WorkIntent, WorkContract, prompts, logs, DeliveryManifest, or HandoffManifest.

High-risk reports should be handled privately by each deployment until a community security process is established.
