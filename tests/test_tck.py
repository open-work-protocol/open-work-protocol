import unittest
from pathlib import Path
from owp.tck import run_vectors

class TCKTests(unittest.TestCase):
    def test_seed_vectors(self):
        root=Path(__file__).resolve().parents[1]/'tck'/'vectors'
        passed,failures=run_vectors(root)
        self.assertGreaterEqual(passed,20)
        self.assertEqual(failures,[])
