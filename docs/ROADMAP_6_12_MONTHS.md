# 6–12 Month Standards Roadmap

The dates begin from public repository launch, not from this design packet.

## Months 0–2 — external breakage

- publish 0.2 seed and TCK;
- recruit two unrelated orchestrator implementers;
- create TypeScript or Go implementation independent of Python reference;
- run public design reviews focused on A2A overlap, payment optionality, privacy, and handoff;
- do not seek official foundation status.

Exit: two implementations exchange WorkContract/Attempt/DeliveryManifest successfully.

## Months 2–4 — real Git evidence

- complete at least three real Git work items;
- complete one cross-provider handoff;
- externalize TCK CI results;
- document every incompatibility discovered;
- production implementation receives focused security review.

Exit: external implementation + real-work evidence.

## Months 4–6 — governance distribution

- add maintainers from multiple organizations;
- publish security response process;
- stabilize extension/compatibility rules;
- decide whether the demonstrated shape is best as A2A extension, AAIF project, or independent spec.

Exit: no single employer holds majority technical control.

## Months 6–9 — standards incubation

If evidence supports it, submit the smallest demonstrated surface to the relevant open governance process. Accept `defer`, `revise`, or `reject` without creating an incompatible fork merely to obtain a standards badge.

## Months 9–12 — compatibility hardening

- multi-language TCK matrix;
- migration/replay fixtures;
- enterprise threat review;
- 1.0 scope freeze only if external deployments justify it.
