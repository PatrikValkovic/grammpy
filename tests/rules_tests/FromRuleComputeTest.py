#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule


class Single(Rule):
    rule = ([0], [1])


class TwoRight(Rule):
    rule = ([0], [1, 2])


class ThreeLeft(Rule):
    rule = ([0, 1, 'a'], [2])


class Multiple(Rule):
    rule = ([0, 1, 2], [3, 4])


class FromRuleComputeTest(TestCase):
    def test_rules_single(self):
        r = Single.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], Single.rule)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0])
        self.assertEqual(r[0][1], [1])
        self.assertEqual(r[0][0][0], 0)
        self.assertEqual(r[0][1][0], 1)

    def test_rules_twoRight(self):
        r = TwoRight.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], TwoRight.rule)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0])
        self.assertEqual(r[0][1], [1, 2])
        self.assertEqual(r[0][0][0], 0)
        self.assertEqual(r[0][1][0], 1)
        self.assertEqual(r[0][1][1], 2)

    def test_rules_threeLeft(self):
        r = ThreeLeft.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], ThreeLeft.rule)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0, 1, 'a'])
        self.assertEqual(r[0][1], [2])
        self.assertEqual(r[0][0][0], 0)
        self.assertEqual(r[0][0][1], 1)
        self.assertEqual(r[0][0][2], 'a')
        self.assertEqual(r[0][1][0], 2)

    def test_rules_multiple(self):
        r = Multiple.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], Multiple.rule)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0, 1, 2])
        self.assertEqual(r[0][1], [3, 4])
        self.assertEqual(r[0][0][0], 0)
        self.assertEqual(r[0][0][1], 1)
        self.assertEqual(r[0][0][2], 2)
        self.assertEqual(r[0][1][0], 3)
        self.assertEqual(r[0][1][1], 4)


if __name__ == '__main__':
    main()
