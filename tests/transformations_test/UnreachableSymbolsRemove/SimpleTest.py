#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence MIT
Part of grammpy-transforms

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class E(Nonterminal): pass
class F(Nonterminal): pass
class RuleAto0B(Rule): rule = ([A], [0, B])
class RuleBto1C(Rule): rule = ([B], [1, C])
class RuleCto01(Rule): rule = ([C], [0, 1])


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01],
                    start_symbol=A)
        com = ContextFree.remove_unreachable_symbols(g)
        self.assertIn(0, com.terminals)
        self.assertIn(1, com.terminals)
        self.assertIn(A, com.nonterminals)
        self.assertIn(B, com.nonterminals)
        self.assertIn(C, com.nonterminals)
        self.assertNotIn(D, com.nonterminals)
        self.assertNotIn(E, com.nonterminals)
        self.assertNotIn(F, com.nonterminals)

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertIn(E, g.nonterminals)
        self.assertIn(F, g.nonterminals)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g, inplace=True)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertNotIn(D, g.nonterminals)
        self.assertNotIn(E, g.nonterminals)
        self.assertNotIn(F, g.nonterminals)


if __name__ == '__main__':
    main()
