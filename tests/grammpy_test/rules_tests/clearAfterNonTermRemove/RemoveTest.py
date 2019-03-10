#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 22:07
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import *
from ..grammar import *


class RemoveTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar()
        self.g.add_term([0, 1, 2, 'a', 'b', 'c'])
        self.g.add_nonterm([NFirst, NSecond, NThird, NFourth, NFifth])

    def test_removeOneByTerminal(self):
        class Tmp(Rule):
            rule = ([NFirst], ['a', 0])
        self.g.add_rule(Tmp)
        self.g.remove_term('a')
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertEqual(self.g.rules_count(), 0)

    def test_removeOneByNonterminal(self):
        class Tmp(Rule):
            rule = ([NFirst], ['a', 0])
        self.g.add_rule(Tmp)
        self.g.remove_nonterm(NFirst)
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertEqual(self.g.rules_count(), 0)

    def test_removeThreeByTerminal(self):
        class Tmp1(Rule):
            rule = ([NFirst], ['a', 0])
        class Tmp2(Rule):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(Rule):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.g.remove_term(0)
        self.assertFalse(self.g.have_rule(Tmp1))
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertFalse(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.rules_count(), 0)

    def test_removeThreeByNonterminal(self):
        class Tmp1(Rule):
            rule = ([NFirst], ['a', 0])
        class Tmp2(Rule):
            rule = ([NSecond], ['a', 0, NFirst])
        class Tmp3(Rule):
            rule = ([NFirst], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.g.remove_nonterm(NFirst)
        self.assertFalse(self.g.have_rule(Tmp1))
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertFalse(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.rules_count(), 0)

    def test_removeTwoFromMoreByTerminal(self):
        class Tmp1(Rule):
            rule = ([NFirst], ['a', 0])
        class Tmp2(Rule):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(Rule):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.g.remove_term('a')
        self.assertFalse(self.g.have_rule(Tmp1))
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.rules_count(), 1)

    def test_removeTwoFromMoreByNonterminal(self):
        class Tmp1(Rule):
            rule = ([NFirst], ['a', 0])
        class Tmp2(Rule):
            rule = ([NSecond], ['a', 0, NFirst])
        class Tmp3(Rule):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.g.remove_term('a')
        self.assertFalse(self.g.have_rule(Tmp1))
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.rules_count(), 1)

    def test_useMultipleSameSymbol(self):
        class Tmp(Rule):
            rule = ([NFirst], [NSecond, NFirst])
        self.g.add_rule(Tmp)
        self.g.remove_nonterm(NFirst)
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertEqual(self.g.rules_count(), 0) 

if __name__ == '__main__':
    main()
