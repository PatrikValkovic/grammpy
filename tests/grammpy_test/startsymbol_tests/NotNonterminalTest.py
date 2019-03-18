#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:09
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import Nonterminal, Grammar
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass


class NotNonterminalTest(TestCase):
    def test_shouldNotSetStartSymbol(self):
        g = Grammar(nonterminals=[A, B])
        self.assertIsNone(g.start)
        with self.assertRaises(NotNonterminalException):
            g.start = 'asdf'
        self.assertIsNone(g.start)
        self.assertFalse(g.start == 'asdf')

    def test_shouldNotSetStartSymbolWhenCreate(self):
        with self.assertRaises(NotNonterminalException):
            g = Grammar(nonterminals=[A, B],
                        start_symbol='asdf')

    def test_oldStartSymbolShouldStaySame(self):
        g = Grammar(nonterminals=[A, B],
                    start_symbol=A)
        self.assertIsNotNone(g.start)
        self.assertIs(g.start, A)
        with self.assertRaises(NotNonterminalException):
            g.start = 'asdf'
        self.assertIsNotNone(g.start)
        self.assertIs(g.start, A)


if __name__ == '__main__':
    main()
