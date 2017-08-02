#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule
from grammpy.exceptions import RuleSyntaxException
from .grammar import *


class InvalidSyntaxTest(TestCase):
    def test_rulesMissingEncloseList(self):
        class tmp(Rule):
            rules = ([0], [1])
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_rulesMissingTuple(self):
        class tmp(Rule):
            rules = [[0], [1]]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_rulesMissingInnerLeftList(self):
        class tmp(Rule):
            rules = [(0, [1])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_rulesMissingInnerRightList(self):
        class tmp(Rule):
            rules = [([0], 1)]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_multipleRulesMissingInnerLeftList(self):
        class tmp(Rule):
            rules = [(NFirst, TSecond), (0, [1])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_multipleRulesMissingInnerRightList(self):
        class tmp(Rule):
            rules = [(NFifth, TFirst), ([0], 1)]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_emptyRule(self):
        class tmp(Rule):
            rules = [([], [])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_emptyOneOfRules(self):
        class tmp(Rule):
            rules = [(NFifth, TFirst), ([], [])]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_onlyOuterArray(self):
        class tmp(Rule):
            rules = [NFifth, TFirst]
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)

    def test_outerIsTuple(self):
        class tmp(Rule):
            rules = (([NFirst], [TSecond]), ([0], [1]))
        with self.assertRaises(RuleSyntaxException):
            tmp.validate(grammar)


if __name__ == '__main__':
    main()
