#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 15:31
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from .grammar import *


class RulesTest(TestCase):
    def setUp(self):
        self.g = Grammar(terminals=[0, 1, 2,
                                    'a', 'b', 'c',
                                    TFirst, TSecond, TThird,
                                    TInstFirst, TInstSecond, TInstThird],
                         nonterminals=[NFirst, NSecond, NThird, NFourth, NFifth])

    def test_oneInRules(self):
        class Tmp1(Rule):
            rules = [([NFirst], [NSecond, 0]),
                     ([NThird], [0, 1]),
                     ([NSecond], [NSecond, 'a'])]
        self.g.add_rule(Tmp1)
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule(Tmp1))

    def test_oneInRulesIteration(self):
        class Tmp1(Rule):
            rules = [([NFirst], [NSecond, 0]),
                     ([NThird], [0, 1]),
                     ([NSecond], [NSecond, 'a'])]
        self.g.add_rule(Tmp1)
        for rule in self.g.rule():
            self.assertIn(rule.rule, Tmp1.rules)

    def test_hashes(self):
        class Tmp1(Rule):
            rules = [([NFirst], [NSecond, 0]),
                     ([NThird], [0, 1]),
                     ([NSecond], [NSecond, 'a'])]
        class Tmp2(Rule):
            rules = [([NFirst], [NSecond, 0]),
                     ([NThird], [0, 1]),
                     ([NSecond], [NSecond, 'a'])]
        hash1 = hash(Tmp1)
        hash2 = hash(Tmp2)
        self.assertEqual(Tmp1, Tmp2)
        self.assertEqual(hash1, hash2)

if __name__ == '__main__':
    main()
