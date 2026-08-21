import unittest
from owp.demo import run_demo

class Tests(unittest.TestCase):
    def test_full_lifecycle(self):
        r=run_demo(verbose=False)
        self.assertEqual(r["final_state"],"CLOSED")
        self.assertEqual(r["attempts_paid"],2)
        self.assertTrue(r["ledger_valid"])
        self.assertNotEqual(r["initial_provider"],r["revision_provider"])
