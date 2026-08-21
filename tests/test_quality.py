import unittest
from owp.quality import ProviderProfile, TaskFeatures, rank

class Tests(unittest.TestCase):
    def test_domain(self):
        task=TaskFeatures("rust",500)
        a=ProviderProfile("a",50,5,{"rust":40},5000,95,95,100)
        b=ProviderProfile("b",40,5,{"rust":99},5000,90,95,100)
        self.assertEqual(rank([a,b],task)[0][0],"b")
    def test_scale(self):
        task=TaskFeatures("python",10000)
        a=ProviderProfile("small",50,3,{"python":95},100,95,95,100)
        b=ProviderProfile("large",50,3,{"python":95},20000,95,95,100)
        self.assertEqual(rank([a,b],task)[0][0],"large")
