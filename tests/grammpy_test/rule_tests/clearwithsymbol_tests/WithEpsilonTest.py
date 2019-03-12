#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.08.2017 17:25
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([A], [B, C]),
        ([A], [EPS]),
        ([B], [0, 1])]


class WithEpsilonTest(TestCase):
    def test_removeB(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C],
                    rules=[Rules])
        self.assertEqual(g.rules.size(), 3)
        g.nonterminals.remove(B)
        self.assertEqual(g.rules.size(), 1)
        class Tmp1(Rule):
            rule = ([A], [B, C])
        class Tmp2(Rule):
            rule = ([B], [0, 1])
        class Tmp3(Rule):
            rule = ([A], [EPS])
        self.assertNotIn(Tmp1, g.rules)
        self.assertNotIn(Tmp2, g.rules)
        self.assertIn(Tmp3, g.rules)
        self.assertNotIn(Rules, g.rules)


if __name__ == '__main__':
    main()
