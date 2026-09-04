import unittest

from owp.marketplace import DeliveryPreference, FallbackPolicy, RouteKind
from owp.models import ProviderDecision, ProviderDecisionKind
from owp.quality import ProviderProfile
from owp.upwork_playground import PlaygroundJob, route_playground_job


class FakeAuthorizedUpworkOperations:
    def __init__(self, allowed=True):
        self.allowed = allowed
        self.applied = []

    def can_apply_provider(self, job, provider_id):
        return self.allowed

    def apply_provider(self, job, provider_id):
        self.applied.append((job.job_id, provider_id))


class UpworkPlaygroundTests(unittest.TestCase):
    def setUp(self):
        self.job = PlaygroundJob("upwork-job-1", "Fix parser", "Fix the parser", "python", 500.0)
        self.profiles = {
            "a": ProviderProfile("a", 5, 4, {"python": 60}, 500),
            "b": ProviderProfile("b", 30, 1, {"python": 95}, 2000),
        }
        self.decisions = [
            ProviderDecision("upwork-job-1", "a", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z"),
            ProviderDecision("upwork-job-1", "b", ProviderDecisionKind.ACCEPT, "2099-01-01T00:00:00Z"),
        ]

    def test_default_is_upwork_even_when_owp_has_candidates(self):
        ops = FakeAuthorizedUpworkOperations()
        outcome = route_playground_job(
            self.job, DeliveryPreference.DEFAULT_MARKETPLACE,
            self.decisions, self.profiles, ops,
        )
        self.assertEqual(outcome.marketplace_action, "DEFAULT_UPWORK")
        self.assertFalse(outcome.applied)
        self.assertEqual(ops.applied, [])

    def test_prefer_quality_applies_best_provider_when_authorized(self):
        ops = FakeAuthorizedUpworkOperations()
        outcome = route_playground_job(
            self.job, DeliveryPreference.PREFER_QUALITY,
            self.decisions, self.profiles, ops,
        )
        self.assertTrue(outcome.applied)
        self.assertEqual(outcome.routing.route, RouteKind.OWP_AWARD)
        self.assertEqual(outcome.routing.provider_id, "b")
        self.assertEqual(ops.applied, [("upwork-job-1", "b")])

    def test_prefer_quality_falls_back_when_upwork_cannot_apply_award(self):
        ops = FakeAuthorizedUpworkOperations(allowed=False)
        outcome = route_playground_job(
            self.job, DeliveryPreference.PREFER_QUALITY,
            self.decisions, self.profiles, ops,
        )
        self.assertFalse(outcome.applied)
        self.assertEqual(outcome.marketplace_action, "DEFAULT_UPWORK")
        self.assertEqual(outcome.routing.reason, "MARKETPLACE_REJECTED_SELECTION")
        self.assertEqual(outcome.routing.provider_id, "b")

    def test_prefer_quality_without_vendor_client_never_fakes_assignment(self):
        outcome = route_playground_job(
            self.job, DeliveryPreference.PREFER_QUALITY,
            self.decisions, self.profiles,
        )
        self.assertFalse(outcome.applied)
        self.assertEqual(outcome.marketplace_action, "DEFAULT_UPWORK")
        self.assertEqual(outcome.routing.reason, "MARKETPLACE_REJECTED_SELECTION")

    def test_fail_closed_stops_when_selected_provider_cannot_be_applied(self):
        outcome = route_playground_job(
            self.job, DeliveryPreference.PREFER_QUALITY,
            self.decisions, self.profiles,
            FakeAuthorizedUpworkOperations(allowed=False),
            FallbackPolicy.FAIL_CLOSED,
        )
        self.assertEqual(outcome.routing.route, RouteKind.FAIL_CLOSED)
        self.assertEqual(outcome.marketplace_action, "STOP_FOR_CLIENT")


if __name__ == "__main__":
    unittest.main()
