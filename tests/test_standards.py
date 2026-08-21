import json
import unittest
from pathlib import Path
from owp.canonical import canonical_json, sha256_id
from owp.models import WorkContract

ROOT=Path(__file__).resolve().parents[1]

class StandardsTests(unittest.TestCase):
    def test_hashed_artifacts_reject_float(self):
        with self.assertRaises(TypeError):
            canonical_json({'amount': 1.1})

    def test_hashed_artifacts_reject_non_ascii_key(self):
        with self.assertRaises(ValueError):
            canonical_json({'café': 'ok'})

    def test_unicode_values_are_stable(self):
        a={'goal':'café inventory','revision':1}
        b={'revision':1,'goal':'café inventory'}
        self.assertEqual(canonical_json(a),canonical_json(b))
        self.assertEqual(sha256_id(a),sha256_id(b))

    def test_money_is_decimal_string_in_contract(self):
        c=WorkContract('w',['x'],{'tests':True},['x'],[],'10.00','USD',1,'owp-git-0.2')
        self.assertEqual(c.to_dict()['attempt_price'],'10.00')
        sha256_id(c.to_dict())

    def test_well_known_is_current_and_incremental(self):
        obj=json.loads((ROOT/'examples/well-known.json').read_text())
        self.assertEqual(obj['protocol_versions'],['0.2'])
        self.assertIn('OWP-Core/0.2',obj['profiles'])
        self.assertNotIn('OWP-Commerce/0.2',obj['profiles'])

    def test_required_standards_packet_exists(self):
        for rel in ['IP_POLICY.md','ANTITRUST.md','TRADEMARK_POLICY.md','spec/SCOPE.md','spec/HASHING_PROFILE.md','spec/EXTENSIONS.md','docs/NON_OVERLAP_MATRIX.md','docs/NEUTRAL_HOME_PATH.md']:
            self.assertTrue((ROOT/rel).exists(),rel)

    def test_committee_packet_is_honest_about_external_gates(self):
        text=(ROOT/'docs/FOUNDATION_READINESS_CHECKLIST.md').read_text()
        self.assertIn('[ ] two unaffiliated implementations',text)
        self.assertIn('not yet entitled',text)

    def test_scope_explicitly_rejects_transport_ownership(self):
        text=(ROOT/'spec/SCOPE.md').read_text().lower()
        self.assertIn('does **not** standardize',text)
        self.assertIn('agent-to-agent transport',text)

    def test_antitrust_prohibits_project_price_guidance(self):
        text=(ROOT/'ANTITRUST.md').read_text().lower()
        self.assertIn('minimum/maximum task prices',text)
        self.assertIn('provider margins',text)
