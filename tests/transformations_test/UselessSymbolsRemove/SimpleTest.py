#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 14:39
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class RuleSto0(Rule): rule = ([S], [0])
class RuleStoA(Rule): rule = ([S], [A])
class RuleAtoAB(Rule): rule = ([A], [A, B])
class RuleBto1(Rule): rule = ([B], [1])


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B],
                    rules=[RuleSto0, RuleStoA, RuleAtoAB, RuleBto1],
                    start_symbol=S)
        com = ContextFree.remove_useless_symbols(g)
        self.assertIn(0, com.terminals)
        self.assertNotIn(1, com.terminals)
        self.assertIn(S, com.nonterminals)
        self.assertNotIn(A, com.nonterminals)
        self.assertNotIn(B, com.nonterminals)

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B],
                    rules=[RuleSto0, RuleStoA, RuleAtoAB, RuleBto1],
                    start_symbol=S)
        ContextFree.remove_useless_symbols(g)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B],
                    rules=[RuleSto0, RuleStoA, RuleAtoAB, RuleBto1],
                    start_symbol=S)
        ContextFree.remove_useless_symbols(g, inplace=True)
        self.assertIn(0, g.terminals)
        self.assertNotIn(1, g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertNotIn(A, g.nonterminals)
        self.assertNotIn(B, g.nonterminals)



if __name__ == '__main__':
    main()