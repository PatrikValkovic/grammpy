#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:20
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule
from grammpy.exceptions import RuleSyntaxException
from ..grammar import *


class InvalidSyntaxTest(TestCase):
    def test_rulesMissingEncloseList(self):
        class tmp(Rule):
            rules = ([0], [1])
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_rulesMissingTuple(self):
        class tmp(Rule):
            rules = [[0], [1]]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_rulesMissingInnerLeftList(self):
        class tmp(Rule):
            rules = [(0, [1])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_rulesMissingInnerRightList(self):
        class tmp(Rule):
            rules = [([0], 1)]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_multipleRulesMissingInnerLeftList(self):
        class tmp(Rule):
            rules = [(NFirst, TSecond), (0, [1])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_multipleRulesMissingInnerRightList(self):
        class tmp(Rule):
            rules = [(NFifth, TFirst), ([0], 1)]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_emptyRule(self):
        class tmp(Rule):
            rules = [([], [])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_emptyOneOfRules(self):
        class tmp(Rule):
            rules = [(NFifth, TFirst), ([], [])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_onlyOuterArray(self):
        class tmp(Rule):
            rules = [NFifth, TFirst]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_outerIsTuple(self):
        class tmp(Rule):
            rules = (([NFirst], [TSecond]), ([0], [1]))
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_threeParts(self):
        class tmp(Rule):
            rules = [([NFirst], [TSecond], [NFifth])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_threePartsInMultiple(self):
        class tmp(Rule):
            rules = [([0], [1]), ([NFirst], [TSecond], [NFifth])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))


if __name__ == '__main__':
    main()
