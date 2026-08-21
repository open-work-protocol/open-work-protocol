import unittest
from owp.golden import run_golden_journey
from owp.models import WorkIntent
from owp.review import make_capsule

class GoldenTests(unittest.TestCase):
    def test_full_customer_to_two_provider_git_journey(self):
        r=run_golden_journey(); self.assertFalse(r['protocol_terms_visible']); self.assertTrue(r['auto_workspace']); self.assertFalse(r['review_capsule_has_resources']); self.assertTrue(r['provider_handoff']); self.assertEqual(r['payments'],2); self.assertTrue(r['fresh_clone_validated_twice']); self.assertEqual(r['final_decision'],'APPROVE'); self.assertTrue(r['export_created'])
    def test_review_capsule_does_not_copy_private_resources_or_goal(self):
        i=WorkIntent('w','SECRET ACQUISITION PLAN',[{'repository':'private/secret','token':'do-not-leak'}],'100.00','USD',1,'now','later')
        raw=str(make_capsule(i,category='business-software').to_dict())
        self.assertNotIn('SECRET ACQUISITION PLAN',raw); self.assertNotIn('private/secret',raw); self.assertNotIn('do-not-leak',raw)
