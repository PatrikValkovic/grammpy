#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 14:14
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Grammar, Nonterminal, Rule as _R
from ..grammar import *


class InactiveRulesTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_countWithInactive(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
            _active = False
        self.g.add_rule(Tmp1)
        self.assertEqual(self.g.rules_count(), 0)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertNotIn(Tmp1, self.g.rules())
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        self.g.add_rule(Tmp2)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertNotIn(Tmp1, self.g.rules())
        self.assertIn(Tmp2, self.g.rules())


if __name__ == '__main__':
    main()
