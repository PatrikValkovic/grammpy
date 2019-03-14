#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 14:23
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
class RuleCto2C(Rule): rule = ([C], [2, C])


class RemovingTerminalsTest(TestCase):
    def test_removingTerminals(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto2C],
                    start_symbol=A)
        com = ContextFree.remove_unreachable_symbols(g)
        self.assertIn(0, com.terminals)
        self.assertIn(1, com.terminals)
        self.assertIn(2, com.terminals)
        self.assertNotIn(3, com.terminals)
        self.assertIn(A, com.nonterminals)
        self.assertIn(B, com.nonterminals)
        self.assertIn(C, com.nonterminals)
        self.assertNotIn(D, com.nonterminals)
        self.assertNotIn(E, com.nonterminals)
        self.assertNotIn(F, com.nonterminals)

    def test_removingTerminalsShouldNotChange(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto2C],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(2, g.terminals)
        self.assertIn(3, g.terminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertIn(E, g.nonterminals)
        self.assertIn(F, g.nonterminals)

    def test_removingTerminalsShouldChange(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto2C],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g, inplace=True)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(2, g.terminals)
        self.assertNotIn(3, g.terminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertNotIn(D, g.nonterminals)
        self.assertNotIn(E, g.nonterminals)
        self.assertNotIn(F, g.nonterminals)


if __name__ == '__main__':
    main()
