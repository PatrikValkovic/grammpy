#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class RuleAto0B(Rule):
    fromSymbol = A
    right = [0, B]
class RuleBto1(Rule):
    fromSymbol = B
    toSymbol = 1


class SimpleTest(TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(terminals=[0, 1],
                         nonterminals=[A, B, C],
                         rules=[RuleAto0B, RuleBto1])

    def test_simpleTest(self):
        changed = ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, changed.terminals)
        self.assertIn(1, changed.terminals)
        self.assertIn(A, changed.nonterminals)
        self.assertIn(B, changed.nonterminals)
        self.assertNotIn(C, changed.nonterminals)

    def test_simpleTestWithoutChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertIn(C, self.g.nonterminals)

    def test_simpleTestWithChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g, inplace=True)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertNotIn(C, self.g.nonterminals)


if __name__ == '__main__':
    main()
