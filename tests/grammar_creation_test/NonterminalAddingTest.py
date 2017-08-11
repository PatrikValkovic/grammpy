#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:03
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class C(Nonterminal):
    pass


class D(Nonterminal):
    pass


class NonterminalAddingTest(TestCase):
    def test_shouldAddOneNonterminal(self):
        g = Grammar(nonterminals=[A])
        self.assertTrue(g.have_nonterm(A))
        self.assertFalse(g.have_nonterm(B))
        self.assertFalse(g.have_nonterm([A, B]))

    def test_shouldAddMoreNonterminals(self):
        g = Grammar(nonterminals=[A, B, C])
        self.assertTrue(g.have_nonterm(A))
        self.assertTrue(g.have_nonterm([A, B, C]))
        self.assertFalse(g.have_nonterm(D))

    def test_shouldNotAddInvalidNonterminal(self):
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[0])

    def test_shouldNotAddOneInvalidNonterminal(self):
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[A, B, 1])


if __name__ == '__main__':
    main()
