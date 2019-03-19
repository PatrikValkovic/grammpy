#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 17:58
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class TerminalHaveTest(TestCase):
    def test_onEmpty(self):
        gr = Grammar()
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)

    def test_haveOne(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        self.assertIn(A, gr.nonterminals)

    def test_haveMultiple(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_haveSome(self):
        gr = Grammar()
        gr.nonterminals.add(A, B)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)

    def test_haveOnEmptyAndInvalid(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            5 in gr.nonterminals

    def test_haveAndInvalid(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        with self.assertRaises(NotNonterminalException):
            5 in gr.nonterminals


if __name__ == '__main__':
    main()
