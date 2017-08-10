#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 23:20
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *
from grammpy.exceptions import NonterminalDoesNotExistsException


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class NonterminalNotInGrammarTest(TestCase):
    def test_shouldNotSetStartSymbol(self):
        g = Grammar(nonterminals=[A])
        self.assertFalse(g.start_isSet())
        with self.assertRaises(NonterminalDoesNotExistsException):
            g.start_set(B)
        self.assertFalse(g.start_isSet())
        self.assertFalse(g.start_is(B))

    def test_shouldNotSetStartSymbolWhenCreate(self):
        with self.assertRaises(NonterminalDoesNotExistsException):
            g = Grammar(nonterminals=[B],
                        start_symbol=A)

    def test_oldStartSymbolShouldStaySame(self):
        g = Grammar(nonterminals=[A], start_symbol=A)
        self.assertTrue(g.start_isSet())
        with self.assertRaises(NonterminalDoesNotExistsException):
            g.start_set(B)
        self.assertTrue(g.start_isSet())
        self.assertTrue(g.start_is(A))
        self.assertEqual(g.start_get(), A)


if __name__ == '__main__':
    main()
