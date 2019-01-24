#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 23:12
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy.old_api import Nonterminal, Grammar
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class NotNonterminalTest(TestCase):
    def test_shouldNotSetStartSymbol(self):
        g = Grammar(nonterminals=[A, B])
        self.assertFalse(g.start_isSet())
        with self.assertRaises(NotNonterminalException):
            g.start_set('asdf')
        self.assertFalse(g.start_isSet())
        self.assertFalse(g.start_is('asdf'))

    def test_shouldNotSetStartSymbolWhenCreate(self):
        with self.assertRaises(NotNonterminalException):
            g = Grammar(nonterminals=[A, B],
                        start_symbol='asdf')

    def test_oldStartSymbolShouldStaySame(self):
        g = Grammar(nonterminals=[A, B], start_symbol=A)
        self.assertTrue(g.start_isSet())
        with self.assertRaises(NotNonterminalException):
            g.start_set('asdf')
        self.assertTrue(g.start_isSet())
        self.assertTrue(g.start_is(A))
        self.assertEqual(g.start_get(), A)


if __name__ == '__main__':
    main()
