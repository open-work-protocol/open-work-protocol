# Proposed A2A Experimental Extension: Outcome Work Contract

Status: independent draft; not an A2A project artifact and not endorsed by A2A.

## Problem

A2A provides the Task/Message/Artifact lifecycle between opaque agents. Some cross-organization workflows additionally need portable semantics for a customer-posted outcome, fixed attempt economics, validation evidence, bounded paid revisions, and provider handoff.

## Design constraint

This extension MUST NOT redefine A2A Task states, transports, authentication, Agent Card semantics, Messages, Artifacts, or streaming.

## Mapping

One OWP `Attempt` maps to one A2A Task. OWP IDs and contract references are extension metadata. DeliveryManifest is emitted as or referenced by an A2A Artifact. Related paid revisions can use new Tasks while OWP `work_id` preserves lineage across provider servers.

## Optionality

A2A agents that do not understand the extension continue to implement normal A2A. Implementations may advertise extension support and may require it only for an individual skill/endpoint where the A2A extension mechanism permits.

## Promotion gate

Do not request A2A-hosted experimental status until there are at least two independent interoperable implementations and TCK evidence demonstrating that the extension adds no core incompatibility.
