"""Vendor-neutral marketplace routing for optional OWP quality selection.

This module deliberately does not call a marketplace API.  It produces a routing
result an authorized adapter can apply.  Native marketplace behavior is the
compatibility default.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence

from .broker import Award, choose_provider
from .models import ProviderDecision
from .quality import ProviderProfile, TaskFeatures


class DeliveryPreference(str, Enum):
    DEFAULT_MARKETPLACE = "DEFAULT_MARKETPLACE"
    PREFER_QUALITY = "PREFER_QUALITY"


class FallbackPolicy(str, Enum):
    DEFAULT_MARKETPLACE = "DEFAULT_MARKETPLACE"
    FAIL_CLOSED = "FAIL_CLOSED"


class RouteKind(str, Enum):
    MARKETPLACE_DEFAULT = "MARKETPLACE_DEFAULT"
    OWP_AWARD = "OWP_AWARD"
    FAIL_CLOSED = "FAIL_CLOSED"


@dataclass(frozen=True)
class RoutingRequest:
    work_id: str
    preference: DeliveryPreference = DeliveryPreference.DEFAULT_MARKETPLACE
    fallback: FallbackPolicy = FallbackPolicy.DEFAULT_MARKETPLACE


@dataclass(frozen=True)
class RoutingResult:
    work_id: str
    route: RouteKind
    provider_id: str | None = None
    score: str | None = None
    scorer: str | None = None
    reason: str | None = None

    @property
    def selected_by_owp(self) -> bool:
        return self.route == RouteKind.OWP_AWARD


def route_marketplace_work(
    request: RoutingRequest,
    decisions: Sequence[ProviderDecision],
    profiles: Mapping[str, ProviderProfile],
    task: TaskFeatures,
) -> RoutingResult:
    """Choose a route without assuming vendor authorization.

    DEFAULT_MARKETPLACE never invokes OWP assignment.  PREFER_QUALITY delegates
    selection to the existing OWP broker.  Selection failures either return to
    the marketplace or fail closed according to the explicit policy.
    """
    if request.preference == DeliveryPreference.DEFAULT_MARKETPLACE:
        return RoutingResult(
            request.work_id,
            RouteKind.MARKETPLACE_DEFAULT,
            reason="OWP_DISABLED",
        )

    try:
        award: Award = choose_provider(request.work_id, decisions, profiles, task)
    except (ValueError, KeyError) as exc:
        if request.fallback == FallbackPolicy.FAIL_CLOSED:
            return RoutingResult(
                request.work_id,
                RouteKind.FAIL_CLOSED,
                reason=_fallback_reason(exc),
            )
        return RoutingResult(
            request.work_id,
            RouteKind.MARKETPLACE_DEFAULT,
            reason=_fallback_reason(exc),
        )

    return RoutingResult(
        request.work_id,
        RouteKind.OWP_AWARD,
        provider_id=award.provider_id,
        score=award.score,
        scorer=award.scorer,
    )


def _fallback_reason(exc: Exception) -> str:
    message = str(exc)
    if "no provider accepted" in message:
        return "NO_ACCEPTS"
    if "missing profile" in message:
        return "MISSING_PROFILE"
    return "SCORER_ERROR"
