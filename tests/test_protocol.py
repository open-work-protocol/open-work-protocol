import unittest
from owp.canonical import sha256_id
from owp.ledger import EventLedger
from owp.models import WorkContract, DeliveryManifest
from owp.state import StateMachine, WorkState
from owp.validator import validate_delivery

class Tests(unittest.TestCase):
    def test_canonical_hash(self):
        self.assertEqual(sha256_id({"b":2,"a":1}),sha256_id({"a":1,"b":2}))
    def test_ledger(self):
        l=EventLedger(); l.append("w","A","x",{}); l.append("w","B","y",{})
        self.assertTrue(l.verify())
    def test_illegal_transition(self):
        s=StateMachine()
        with self.assertRaises(ValueError): s.transition(WorkState.EXECUTING)
    def test_validator(self):
        c=WorkContract("w",["x"],{"build":True,"tests":True},["x"],[],"10.00","USD",1,"owp-git-0.2")
        h=sha256_id(c.to_dict())
        d=DeliveryManifest("w","a",h,"p","x/y","a"*40,"b"*40,"c"*40,{"build":"PASS","tests":"PASS"})
        self.assertEqual(validate_delivery(c,d).outcome.value,"VALID")
        bad=DeliveryManifest("w","a",h,"p","x/y","a"*40,"b"*40,"c"*40,{"build":"PASS","tests":"FAIL"})
        self.assertEqual(validate_delivery(c,bad).outcome.value,"INVALID")
