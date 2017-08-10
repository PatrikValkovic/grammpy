#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:08
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy import Rule, EPS
from ..grammar import *


class ValidRulesTest(TestCase):
    def test_regular(self):
        class tmp(Rule):
            rules = [([NFifth], [TFirst, NFirst])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_epsilon(self):
        class tmp(Rule):
            rules = [([NFifth], [EPS])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_leftEpsilon(self):
        class tmp(Rule):
            rules = [([EPS], [TFirst, 0])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_twoLeft(self):
        class tmp(Rule):
            rules = [([TFirst, NFifth], ['a'])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_multipleBoth(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_multipleWithEpsilon(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], [EPS])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_twoRules(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]), ([NFifth], [EPS])]
        self.assertTrue(tmp.is_valid(grammar))

    def test_multipleRules(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     ([NFifth], [EPS]),
                     ([TSecond, 'b', TThird], [EPS]),
                     ([TFirst, NFifth], ['a'])]
        self.assertTrue(tmp.is_valid(grammar))


if __name__ == '__main__':
    main()
