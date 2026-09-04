import unittest

from owp.marketplace import (
    DeliveryPreference,
    FallbackPolicy,
    RouteKind,
    RoutingRequest,
    route_marketplace_work,
)
from owp.models import ProviderDecision, ProviderDecisionKind
from owp.quality import ProviderProfile, TaskFeatures


class MarketplaceRoutingTests(unittest.TestCase):
    def setUp(self):
        self.task = TaskFeatures(domain="python", value=500.0)
        self.profiles = {
            "provider-a": ProviderProfile("provider-a", 8, 2, {"python": 70}, 1000),
            "provider-b": ProviderProfile("provider-b", 20, 1, {"python": 95}, 2000),
        }
        self.decisions = [
            ProviderDecision("w1", "provider-a", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z"),
            ProviderDecision("w1", "provider-b", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z"),
        ]

    def test_marketplace_is_default_and_does_not_select_provider(self):
        result = route_marketplace_work(RoutingRequest("w1"), self.decisions, self.profiles, self.task)
        self.assertEqual(result.route, RouteKind.MARKETPLACE_DEFAULT)
        self.assertIsNone(result.provider_id)
        self.assertEqual(result.reason, "OWP_DISABLED")

    def test_prefer_quality_selects_best_acceptor_automatically(self):
        result = route_marketplace_work(
            RoutingRequest("w1", DeliveryPreference.PREFER_QUALITY),
            self.decisions,
            self.profiles,
            self.task,
        )
        self.assertEqual(result.route, RouteKind.OWP_AWARD)
        self.assertEqual(result.provider_id, "provider-b")
        self.assertTrue(result.selected_by_owp)
        self.assertEqual(result.scorer, "owp-reference-quality/0.2")

    def test_pass_is_not_eligible(self):
        decisions = [
            ProviderDecision("w1", "provider-b", ProviderDecisionKind.PASS, "2099-01-01T00:00:00Z"),
            ProviderDecision("w1", "provider-a", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z"),
        ]
        result = route_marketplace_work(
            RoutingRequest("w1", DeliveryPreference.PREFER_QUALITY),
            decisions,
            self.profiles,
            self.task,
        )
        self.assertEqual(result.provider_id, "provider-a")

    def test_no_accepts_falls_back_to_marketplace(self):
        decisions = [ProviderDecision("w1", "provider-a", ProviderDecisionKind.PASS, "2099-01-01T00:00:00Z")]
        result = route_marketplace_work(
            RoutingRequest("w1", DeliveryPreference.PREFER_QUALITY),
            decisions,
            self.profiles,
            self.task,
        )
        self.assertEqual(result.route, RouteKind.MARKETPLACE_DEFAULT)
        self.assertEqual(result.reason, "NO_ACCEPTS")

    def test_fail_closed_is_explicit(self):
        result = route_marketplace_work(
            RoutingRequest("w1", DeliveryPreference.PREFER_QUALITY, FallbackPolicy.FAIL_CLOSED),
            [],
            self.profiles,
            self.task,
        )
        self.assertEqual(result.route, RouteKind.FAIL_CLOSED)
        self.assertEqual(result.reason, "NO_ACCEPTS")

    def test_missing_profile_falls_back_safely(self):
        decisions = [ProviderDecision("w1", "unknown", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z")]
        result = route_marketplace_work(
            RoutingRequest("w1", DeliveryPreference.PREFER_QUALITY),
            decisions,
            self.profiles,
            self.task,
        )
        self.assertEqual(result.route, RouteKind.MARKETPLACE_DEFAULT)
        self.assertEqual(result.reason, "MISSING_PROFILE")


if __name__ == "__main__":
    unittest.main()
