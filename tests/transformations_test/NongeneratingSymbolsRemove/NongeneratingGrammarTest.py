#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.03.2019 16:57
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([A], [0, B]),
        ([B], [1, C]),
        ([C], [0, D]),
        ([D], [1, A])
    ]


class SimpleTest(TestCase):
    def test_shouldRemoveAllNonterminals(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D],
                    rules=[Rules],
                    start_symbol=A)
        com = ContextFree.remove_nongenerating_nonterminals(g)
        self.assertIsNone(com.start)
        self.assertEqual(com.nonterminals.size(), 0)
        self.assertNotIn(A, com.nonterminals)
        self.assertNotIn(B, com.nonterminals)
        self.assertNotIn(C, com.nonterminals)
        self.assertNotIn(D, com.nonterminals)
        self.assertEqual(com.rules.size(), 0)

    def test_shouldntModifyOriginalGrammar(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D],
                    rules=[Rules],
                    start_symbol=A)
        ContextFree.remove_nongenerating_nonterminals(g)
        self.assertIsNotNone(g.start)
        self.assertEqual(g.start, A)
        self.assertEqual(g.nonterminals.size(), 4)
        self.assertIn(A, g.nonterminals)
        self.assertIn(B, g.nonterminals)
        self.assertIn(C, g.nonterminals)
        self.assertIn(D, g.nonterminals)
        self.assertEqual(g.rules.size(), 4)
        self.assertIn(Rules, g.rules)

    def test_shouldModifyGrammar(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D],
                    rules=[Rules],
                    start_symbol=A)
        ContextFree.remove_nongenerating_nonterminals(g, inplace=True)
        self.assertIsNone(g.start)
        self.assertEqual(g.nonterminals.size(), 0)
        self.assertNotIn(A, g.nonterminals)
        self.assertNotIn(B, g.nonterminals)
        self.assertNotIn(C, g.nonterminals)
        self.assertNotIn(D, g.nonterminals)
        self.assertEqual(g.rules.size(), 0)


if __name__ == '__main__':
    main()
