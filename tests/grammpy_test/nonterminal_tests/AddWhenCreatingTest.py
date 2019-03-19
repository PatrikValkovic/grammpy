#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 17:46
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass


class AddWhenCreating(TestCase):
    def test_addOneInArray(self):
        gr = Grammar(nonterminals=[A])
        self.assertIn(A, gr.nonterminals)

    def test_addTwoInArray(self):
        gr = Grammar(nonterminals=[A, B])
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)

    def test_addThreeInArray(self):
        gr = Grammar(nonterminals=[A, B, C])
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_addThreeInTuple(self):
        gr = Grammar(nonterminals=(A, B, C))
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_addThreeOneDelete(self):
        gr = Grammar(nonterminals=(A, B, C))
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)
        gr.nonterminals.remove(B)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_addTerminal(self):
        with self.assertRaises(NotNonterminalException):
            gr = Grammar(nonterminals=[0])

    def test_addTerminalBetweenValid(self):
        with self.assertRaises(NotNonterminalException):
            gr = Grammar(nonterminals=[A, 0, B])


if __name__ == '__main__':
    main()
