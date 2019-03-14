#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 18:18
:Licence MIT
Part of grammpy-transforms

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import ContextFree


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class RuleAto0B(Rule):
    rule = ([A], [0, B])
class RuleBto01(Rule):
    rule = ([B], [0, 1])
class RuleAto1C(Rule):
    rule = ([A], [1, C])
class RuleCto0C(Rule):
    rule = ([C], [0, C])


class PartCompleteTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(terminals=[0, 1, 2],
                         nonterminals=[A, B, C],
                         rules=[RuleAto0B, RuleBto01,
                                RuleAto1C, RuleCto0C])

    def test_partlyIncompleteTest(self):
        changed = ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, changed.terminals)
        self.assertIn(1, changed.terminals)
        self.assertIn(A, changed.nonterminals)
        self.assertIn(B, changed.nonterminals)
        self.assertNotIn(C, changed.nonterminals)

    def test_partlyIncompleteTestWithoutChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertIn(C, self.g.nonterminals)

    def test_partlyIncompleteTestWithChange(self):
        ContextFree.remove_nongenerating_nonterminals(self.g, inplace=True)
        self.assertIn(0, self.g.terminals)
        self.assertIn(1, self.g.terminals)
        self.assertIn(A, self.g.nonterminals)
        self.assertIn(B, self.g.nonterminals)
        self.assertNotIn(C, self.g.nonterminals)


if __name__ == '__main__':
    main()
