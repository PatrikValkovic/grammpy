import unittest as ut
from grammpy.travis_coverage import sum


class CoverageTest(ut.TestCase):
    def test_sumCoverage(self):
        self.assertEqual(2, sum(1, 1))

    def test_anotherSumCoverage(self):
        self.assertEqual(3, sum(1, 2))
