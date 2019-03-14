#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.08.2017 16:34
:Licence MIT
Part of grammpy-transforms

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import *


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [0, S]),
        ([S], [1, D]),
        ([S], [EPS]),
        ([A], [0, C, B]),
        ([A], [0, A, D]),
        ([B], [1, B]),
        ([B], [1, 1, 0]),
        ([C], [1, C, C]),
        ([C], [0, A, 1, B]),
        ([D], [1, 1, A]),
        ([D], [0, D, 0, 0]),
        ([D], [1, S]),
        ([D], [EPS])]

class SimpleTest(TestCase):
    def test_epsilonTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 13)
        com = ContextFree.remove_useless_symbols(g)
        self.assertIn(0, com.terminals)
        self.assertIn(1, com.terminals)
        self.assertIn(S, com.nonterminals)
        self.assertIn(D, com.nonterminals)
        self.assertNotIn(A, com.nonterminals)
        self.assertNotIn(B, com.nonterminals)
        self.assertNotIn(C, com.nonterminals)
        self.assertEqual(com.rules.size(), 6)

    def test_epsilonTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 13)
        ContextFree.remove_useless_symbols(g)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertEqual(g.rules.size(), 13)

    def test_epsilonTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 13)
        ContextFree.remove_useless_symbols(g, inplace=True)
        self.assertIn(0, g.terminals)
        self.assertIn(1, g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertNotIn(A, g.nonterminals)
        self.assertNotIn(B, g.nonterminals)
        self.assertNotIn(C, g.nonterminals)
        self.assertEqual(g.rules.size(), 6)


if __name__ == '__main__':
    main()