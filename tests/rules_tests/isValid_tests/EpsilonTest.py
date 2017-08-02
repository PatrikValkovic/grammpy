#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule, EPS
from grammpy.exceptions import UselessEpsilonException
from .grammar import *


class EpsilonTest(TestCase):
    def test_epsilonToEpsilon(self):
        class tmp(Rule):
            rules = [([EPS], [EPS])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)

    def test_epsilonInRule(self):
        class tmp(Rule):
            rules = [([NThird], [0, EPS])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)

    def test_rewriteToEpsilon(self):
        class tmp(Rule):
            rules = [([NThird], [EPS])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_epsilonOnLeftBeginRule(self):
        class tmp(Rule):
            rules = [([NThird], [EPS, 1, TSecond])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)

    def test_epsilonOnLeft(self):
        class tmp(Rule):
            rules = [([NThird, EPS], [0, 1])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)

    def test_epsilonRewriteFromLeft(self):
        class tmp(Rule):
            rules = [([EPS], [0, 1])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_epsilonInMoreRules(self):
        class tmp(Rule):
            rules = [([TFirst, NFifth], ['a']),
                     ([NThird], [EPS, 1, TSecond])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)

    def test_epsilonOnRightInMoreRules(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     ([NThird, EPS], [0, 1])]
        with self.assertRaises(UselessEpsilonException):
            tmp.validate(grammar)


if __name__ == '__main__':
    main()
