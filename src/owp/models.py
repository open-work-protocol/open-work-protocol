from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any

PROTOCOL_VERSION = "0.2"

class ProviderDecisionKind(str, Enum):
    ACCEPT = "ACCEPT"
    PASS = "PASS"

class CustomerDispositionKind(str, Enum):
    APPROVE = "APPROVE"
    STEER = "STEER"
    REJECT = "REJECT"

class ValidationOutcome(str, Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    INDETERMINATE = "INDETERMINATE"

@dataclass(frozen=True)
class WorkIntent:
    work_id: str
    goal: str
    resources: list[dict[str, Any]]
    attempt_price: str
    currency: str
    max_revisions: int
    review_open: str
    review_close: str
    evidence_policy: str = "owp-git-0.2"
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class WorkContract:
    work_id: str
    deliverables: list[str]
    acceptance: dict[str, Any]
    included_scope: list[str]
    excluded_scope: list[str]
    attempt_price: str
    currency: str
    max_revisions: int
    evidence_policy: str
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class ProviderDecision:
    work_id: str
    provider_id: str
    decision: ProviderDecisionKind
    valid_until: str
    proof: str = "unsigned-local"
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self):
        d = asdict(self); d["decision"] = self.decision.value; return d

@dataclass(frozen=True)
class Attempt:
    attempt_id: str
    work_id: str
    contract_hash: str
    provider_id: str
    revision: int
    parent_attempt_id: str | None = None
    payment_ref: str | None = None
    authority_ref: str | None = None
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class DeliveryManifest:
    work_id: str
    attempt_id: str
    contract_hash: str
    provider_id: str
    repository: str
    base_sha: str
    result_sha: str
    tree_sha: str | None
    checks: dict[str, str]
    artifacts: list[dict[str, Any]] = field(default_factory=list)
    pr_url: str | None = None
    deployment_url: str | None = None
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class CustomerDisposition:
    work_id: str
    attempt_id: str
    disposition: CustomerDispositionKind
    feedback: dict[str, Any] | None = None
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self):
        d = asdict(self); d["disposition"] = self.disposition.value; return d

@dataclass(frozen=True)
class HandoffManifest:
    work_id: str
    from_provider_id: str
    current_repository: str
    current_sha: str
    contract_hash: str
    attempts: list[str]
    evidence_refs: list[str]
    customer_feedback: list[dict[str, Any]]
    known_blockers: list[str]
    remaining_revisions: int
    extensions: dict[str, Any] = field(default_factory=dict)
    protocol_version: str = PROTOCOL_VERSION
    def to_dict(self): return asdict(self)
