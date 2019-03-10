#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:00
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy import *
from grammpy.exceptions import NotNonterminalException


class InvalidNonterminalTest(TestCase):
    def test_oneInvalidNonterminal(self):
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[2])

    def test_threeInvalidNonterminal(self):
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[2, 'asdf', InvalidNonterminalTest])

    def test_oneInvalidNontermBetweenValidOnces(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[A, B, 5, C])
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[5, A, B, C])
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[A, B, C, 5])

    def test_moreInvalidNontermBetweenValidOnces(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[A, 2, B, 5, C])
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[5, A, 4, B, C])
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[A, 3, B, C, 5])
        with self.assertRaises(NotNonterminalException):
            Grammar(nonterminals=[3, A, B, C, 5])


if __name__ == '__main__':
    main()
