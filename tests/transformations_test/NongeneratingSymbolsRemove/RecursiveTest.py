#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class E(Nonterminal): pass
class RuleAto0B(Rule):
    rule = ([A], [0, B])
class RuleBto1(Rule):
    fromSymbol = B
    toSymbol = 1
class RuleCto1D(Rule):
    rule = ([C], [1, D])
class RuleDto0E(Rule):
    rule = ([D], [0, E])
class RuleEto0C(Rule):
    rule = ([E], [0, C])


class RecursiveTest(TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(terminals=[0, 1],
                         nonterminals=[A, B, C, D, E],
                         rules=[RuleAto0B, RuleBto1,
                                RuleCto1D, RuleDto0E,
                                RuleEto0C])

    def test_recursiveTest(self):
        changed = ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, changed.terminals)
        self.assertIn(1, changed.terminals)
        self.assertIn(A, changed.nonterminals)
        self.assertIn(B, changed.nonterminals)
        self.assertNotIn(C, changed.nonterminals)
        self.assertNotIn(D, changed.nonterminals)
        self.assertNotIn(E, changed.nonterminals)

    def test_recursiveTestWithoutChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertIn(C, self.g.nonterminals)
        self.assertIn(D, self.g.nonterminals)
        self.assertIn(E, self.g.nonterminals)

    def test_recursiveTestWithChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g, inplace=True)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertNotIn(C, self.g.nonterminals)
        self.assertNotIn(D, self.g.nonterminals)
        self.assertNotIn(E, self.g.nonterminals)


if __name__ == '__main__':
    main()
