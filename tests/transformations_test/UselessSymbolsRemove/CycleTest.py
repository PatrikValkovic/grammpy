#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.08.2017 16:13
:Licence MIT
Part of grammpy-transforms

"""
from unittest import TestCase
from grammpy import *
from grammpy.transforms import *


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class Rules(Rule):
    rules = [([S], [A, B]),
             ([S], [C]),
             ([A], ['a', A]),
             ([A], ['a']),
             ([B], ['b', B]),
             ([C], ['c']),
             ([D], ['b', 'c'])]


class CycleTest(TestCase):
    def test_cycleTest(self):
        g = Grammar(terminals=['a', 'b', 'c'],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 7)
        com = ContextFree.remove_useless_symbols(g)
        self.assertIn('c', com.terminals)
        self.assertNotIn('a', com.terminals)
        self.assertNotIn('b', com.terminals)
        self.assertIn(S, com.nonterminals)
        self.assertIn(C, com.nonterminals)
        self.assertNotIn(A, com.nonterminals)
        self.assertNotIn(B, com.nonterminals)
        self.assertNotIn(D, com.nonterminals)
        self.assertEqual(com.rules.size(), 2)

    def test_cycleTestShouldNotChange(self):
        g = Grammar(terminals=['a', 'b', 'c'],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 7)
        ContextFree.remove_useless_symbols(g)
        self.assertIn('c', g.terminals)
        self.assertIn('a', g.terminals)
        self.assertIn('b', g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertEqual(g.rules.size(), 7)

    def test_cycleTestShouldChange(self):
        g = Grammar(terminals=['a', 'b', 'c'],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        self.assertEqual(g.rules.size(), 7)
        ContextFree.remove_useless_symbols(g, inplace=True)
        self.assertIn('c', g.terminals)
        self.assertNotIn('a', g.terminals)
        self.assertNotIn('b', g.terminals)
        self.assertIn(S, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertNotIn(A, g.nonterminals)
        self.assertNotIn(B, g.nonterminals)
        self.assertNotIn(D, g.nonterminals)
        self.assertEqual(g.rules.size(), 2)
