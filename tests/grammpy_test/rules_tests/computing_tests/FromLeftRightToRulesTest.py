#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:04
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule
from grammpy.exceptions import NotASingleSymbolException


class Simple(Rule):
    left = [0]
    right = [1]


class TwoRight(Rule):
    left = [0]
    right = [1, 2]


class ThreeLeft(Rule):
    left = [0, 1, 2]
    right = [3]


class Multiple(Rule):
    left = [0, 1, 2]
    right = [3, 4]


class FromLeftRIghtToRulesTest(TestCase):
    def test_rules_simple(self):
        r = Simple.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0])
        self.assertEqual(r[0][1], [1])

    def test_rule_simple(self):
        r = Simple.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0])
        self.assertEqual(r[1], [1])

    def test_symbol_simple(self):
        self.assertEqual(Simple.fromSymbol, 0)
        self.assertEqual(Simple.toSymbol, 1)

    def test_rules_twoRight(self):
        r = TwoRight.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0])
        self.assertEqual(r[0][1], [1, 2])

    def test_rule_twoRight(self):
        r = TwoRight.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0])
        self.assertEqual(r[1], [1, 2])

    def test_symbol_twoRight(self):
        self.assertEqual(TwoRight.fromSymbol, 0)
        with self.assertRaises(NotASingleSymbolException):
            x = TwoRight.toSymbol

    def test_rules_threeLeft(self):
        r = ThreeLeft.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0, 1, 2])
        self.assertEqual(r[0][1], [3])

    def test_rule_threeLeft(self):
        r = ThreeLeft.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0, 1, 2])
        self.assertEqual(r[1], [3])

    def test_symbol_threeLeft(self):
        with self.assertRaises(NotASingleSymbolException):
            x = ThreeLeft.fromSymbol
        self.assertEqual(ThreeLeft.toSymbol, 3)

    def test_rules_multiple(self):
        r = Multiple.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0, 1, 2])
        self.assertEqual(r[0][1], [3, 4])

    def test_rule_multiple(self):
        r = Multiple.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0, 1, 2])
        self.assertEqual(r[1], [3, 4])

    def test_symbol_multiple(self):
        with self.assertRaises(NotASingleSymbolException):
            x = Multiple.fromSymbol
        with self.assertRaises(NotASingleSymbolException):
            x = Multiple.toSymbol


if __name__ == '__main__':
    main()
