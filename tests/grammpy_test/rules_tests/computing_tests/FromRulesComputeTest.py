#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:04
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule
from grammpy.exceptions.NotASingleSymbolException import NotASingleSymbolException
from grammpy.exceptions.CantCreateSingleRuleException import CantCreateSingleRuleException


class OneRule(Rule):
    rules = [([0], [1])]


class OneRuleTwoRight(Rule):
    rules = [([0], [1, 2])]


class TwoLeftRule(Rule):
    rules = [([0, 1], [2])]


class TwoRules(Rule):
    rules = [([0], [1]), ([2], [3, 4])]


class FromRulesComputeTest(TestCase):
    def test_ruleFromOne(self):
        r = OneRule.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0])
        self.assertEqual(r[1], [1])

    def test_leftRightFromOne(self):
        self.assertEqual(OneRule.left, [0])
        self.assertEqual(OneRule.right, [1])

    def test_leftRightSymbolFromOne(self):
        self.assertEqual(OneRule.fromSymbol, 0)
        self.assertEqual(OneRule.toSymbol, 1)

    def test_ruleFromTwoRight(self):
        r = OneRuleTwoRight.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0])
        self.assertEqual(r[1], [1, 2])

    def test_leftRightFromTwoRight(self):
        self.assertEqual(OneRuleTwoRight.left, [0])
        self.assertEqual(OneRuleTwoRight.right, [1, 2])

    def test_leftRightSymbolFromTwoRight(self):
        self.assertEqual(OneRuleTwoRight.fromSymbol, 0)
        with self.assertRaises(NotASingleSymbolException):
            x = OneRuleTwoRight.toSymbol

    def test_ruleFromTwoLeft(self):
        r = TwoLeftRule.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0, 1])
        self.assertEqual(r[1], [2])

    def test_leftRightFromTwoLeft(self):
        self.assertEqual(TwoLeftRule.left, [0, 1])
        self.assertEqual(TwoLeftRule.right, [2])

    def test_leftRightSymbolFromTwoLeft(self):
        self.assertEqual(TwoLeftRule.toSymbol, 2)
        with self.assertRaises(NotASingleSymbolException):
            x = TwoLeftRule.fromSymbol

    def test_ruleFromOne(self):
        with self.assertRaises(CantCreateSingleRuleException):
            r = TwoRules.rule

    def test_leftRightFromTwo(self):
        with self.assertRaises(CantCreateSingleRuleException):
            x = TwoRules.left
        with self.assertRaises(CantCreateSingleRuleException):
            x = TwoRules.right

    def test_leftRightSymbolFromOne(self):
        with self.assertRaises(CantCreateSingleRuleException):
            x = TwoRules.fromSymbol
        with self.assertRaises(CantCreateSingleRuleException):
            x = TwoRules.toSymbol


if __name__ == '__main__':
    main()
