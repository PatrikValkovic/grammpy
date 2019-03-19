#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:08
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy import Rule
from grammpy.exceptions import MultipleDefinitionException
from .grammar import *


class MultipleDefinitionTest(TestCase):
    def test_defineSameRulesAndRule(self):
        class R(Rule):
            rules = [([NFirst], [NSecond, 2])]
            rule = ([NFirst], [NSecond, 2])
        self.assertFalse(R.is_valid(grammar))

    def test_defineSameRulesAndLeftRight(self):
        class R(Rule):
            rules = [([NFirst], [NSecond, 2])]
            left = [NFirst]
            right = [NSecond, 2]
        with self.assertRaises(MultipleDefinitionException):
            R.validate(grammar)

    def test_defineSameRulesAndFromToSymbol(self):
        class R(Rule):
            rules = [([NFirst], [2])]
            fromSymbol = NFirst
            toSymbol = 2
        self.assertFalse(R.is_valid(grammar))

    def test_defineSameRulesAndToSymbolRight(self):
        class R(Rule):
            rules = [([NFirst], [2, NSecond])]
            fromSymbol = NFirst
            right = [2, NSecond]
        with self.assertRaises(MultipleDefinitionException):
            R.validate(grammar)

    def test_defineSameRuleAndLeftRight(self):
        class R(Rule):
            rule = ([NFirst], [NSecond, 2])
            left = [NFirst]
            right = [NSecond, 2]
        self.assertFalse(R.is_valid(grammar))

    def test_defineDifferentRuleAndFromToSymbol(self):
        class R(Rule):
            rule = ([NFirst], [2])
            fromSymbol = NFirst
            toSymbol = 1
        with self.assertRaises(MultipleDefinitionException):
            R.validate(grammar)

    def test_defineDifferentRuleAndToSymbolRight(self):
        class R(Rule):
            rule = ([NFirst], [2, NSecond])
            fromSymbol = NFirst
            right = [2, NThird]
        self.assertFalse(R.is_valid(grammar))

    def test_defineDifferentLeftRightAndToFromSymbol(self):
        class R(Rule):
            left = [NFirst]
            right = [2]
            fromSymbol = NThird
            toSymbol = 2
        self.assertFalse(R.is_valid(grammar))

    def test_defineDifferentLeftRightAndFromSymbol(self):
        class R(Rule):
            fromSymbol = NFirst
            left = [NThird]
            right = [2, NSecond]
        with self.assertRaises(MultipleDefinitionException):
            R.validate(grammar)


if __name__ == '__main__':
    main()
