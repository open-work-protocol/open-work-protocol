# Compatibility Contract

## Pre-1.0

OWP remains experimental. Breaking changes are permitted only with:

1. explicit protocol/profile version change;
2. migration notes;
3. before/after TCK vectors;
4. no silent reinterpretation of an existing version.

## Capability claims

Implementations advertise exact supported profile/version pairs. Unsupported optional profiles do not make OWP-Core incompatible.

## Transport independence

A WorkContract/Attempt/DeliveryManifest generated through one transport remains interpretable through another transport if the same profile versions and extensions are supported.

## No mandatory ecosystem upgrade

Adopting OWP-Core/0.2 does not require A2A, x402, AP2, ERC-8004, a blockchain, a specific Git forge, or a specific model/orchestrator.
