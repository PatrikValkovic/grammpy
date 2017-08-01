#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule
from grammpy import EPS


class CountTest(TestCase):
    def test_osneRule(self):
        class tmp(Rule):
            rule = ([0, 1], [2, 3])
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneSimpleRule(self):
        class tmp(Rule):
            rule = ([EPS], [0])
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneRules(self):
        class tmp(Rule):
            rules = [([0, 1], [2, 3])]
        self.assertEqual(tmp.rules_count(), 1)

    def test_twoRules(self):
        class tmp(Rule):
            rules = [([0, 1], [2]), ([3], [4, 5])]
        self.assertEqual(tmp.rules_count(), 2)

    def test_threeRules(self):
        class tmp(Rule):
            rules = [([0, 1], [2]), ([3], [4, 5]), ([6], [7])]
        self.assertEqual(tmp.rules_count(), 3)

    def test_oneLeftRight(self):
        class tmp(Rule):
            left = [0, 1]
            right = [3]
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneLeftRightSimple(self):
        class tmp(Rule):
            left = [2]
            right = [3, 4]
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneLeftSymbol(self):
        class tmp(Rule):
            fromSymbol = 0
            right = [1,2]
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneRightSymbol(self):
        class tmp(Rule):
            left = [1,2]
            toSymbol = 3
        self.assertEqual(tmp.rules_count(), 1)

    def test_oneSymbols(self):
        class tmp(Rule):
            fromSymbol = 0
            toSymbol = 1
        self.assertEqual(tmp.rules_count(), 1)

if __name__ == '__main__':
    main()
