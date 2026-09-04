"""Reference boundary for an Upwork AI Agent Playground integration.

This is intentionally an adapter contract, not an undocumented Upwork API client.
It makes OWP routing executable while requiring a real authorized integration to
supply the vendor-specific assignment and delivery operations.
"""
from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence

from .marketplace import (
    DeliveryPreference,
    FallbackPolicy,
    RouteKind,
    RoutingRequest,
    RoutingResult,
    route_marketplace_work,
)
from .models import ProviderDecision
from .quality import ProviderProfile, TaskFeatures


@dataclass(frozen=True)
class PlaygroundJob:
    job_id: str
    title: str
    description: str
    domain: str
    value: float
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PlaygroundRouteOutcome:
    job_id: str
    routing: RoutingResult
    applied: bool
    marketplace_action: str


class UpworkAuthorizedOperations(Protocol):
    """Operations supplied only by an authorized marketplace integration."""

    def can_apply_provider(self, job: PlaygroundJob, provider_id: str) -> bool: ...
    def apply_provider(self, job: PlaygroundJob, provider_id: str) -> None: ...


def route_playground_job(
    job: PlaygroundJob,
    preference: DeliveryPreference,
    decisions: Sequence[ProviderDecision],
    profiles: Mapping[str, ProviderProfile],
    operations: UpworkAuthorizedOperations | None = None,
    fallback: FallbackPolicy = FallbackPolicy.DEFAULT_MARKETPLACE,
) -> PlaygroundRouteOutcome:
    """Route a Playground-shaped job with Upwork as the safe default.

    If OWP selects a provider but no authorized operation can apply the award,
    the result becomes a recommendation and returns control to the marketplace.
    This prevents the reference implementation from pretending an undocumented
    vendor assignment API exists.
    """
    routing = route_marketplace_work(
        RoutingRequest(job.job_id, preference, fallback),
        decisions,
        profiles,
        TaskFeatures(job.domain, job.value),
    )

    if routing.route == RouteKind.MARKETPLACE_DEFAULT:
        return PlaygroundRouteOutcome(job.job_id, routing, False, "DEFAULT_UPWORK")
    if routing.route == RouteKind.FAIL_CLOSED:
        return PlaygroundRouteOutcome(job.job_id, routing, False, "STOP_FOR_CLIENT")

    assert routing.provider_id is not None
    if operations is None or not operations.can_apply_provider(job, routing.provider_id):
        if fallback == FallbackPolicy.FAIL_CLOSED:
            unavailable = RoutingResult(
                job.job_id,
                RouteKind.FAIL_CLOSED,
                provider_id=routing.provider_id,
                score=routing.score,
                scorer=routing.scorer,
                reason="MARKETPLACE_REJECTED_SELECTION",
            )
            return PlaygroundRouteOutcome(job.job_id, unavailable, False, "STOP_FOR_CLIENT")
        unavailable = RoutingResult(
            job.job_id,
            RouteKind.MARKETPLACE_DEFAULT,
            provider_id=routing.provider_id,
            score=routing.score,
            scorer=routing.scorer,
            reason="MARKETPLACE_REJECTED_SELECTION",
        )
        return PlaygroundRouteOutcome(job.job_id, unavailable, False, "DEFAULT_UPWORK")

    operations.apply_provider(job, routing.provider_id)
    return PlaygroundRouteOutcome(job.job_id, routing, True, "OWP_PROVIDER_APPLIED")
