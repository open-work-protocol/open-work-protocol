import unittest
from owp.simple import OutcomeRequest, compile_preview, customer_language

class SimpleFlowTests(unittest.TestCase):
    def test_no_repo_required(self):
        r=OutcomeRequest('Build a small inventory site',1000)
        c=compile_preview(r,1)
        self.assertEqual(c.asked_for,'Build a small inventory site')
        self.assertEqual(c.price_this_attempt,1000)
        self.assertEqual(c.maximum_authorized_spend,2000)
    def test_visible_language_hides_protocol(self):
        self.assertEqual(customer_language('VALID_DELIVERY'),'Ready to review')
        self.assertEqual(customer_language('STEER'),'Change something')
