#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:12
:Licence GPLv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import Nonterminal, Grammar
from grammpy.exceptions import NonterminalDoesNotExistsException


class A(Nonterminal): pass
class B(Nonterminal): pass


class NonterminalNotInGrammarTest(TestCase):
    def test_shouldNotSetStartSymbol(self):
        g = Grammar(nonterminals=[A])
        self.assertIsNone(g.start)
        with self.assertRaises(NonterminalDoesNotExistsException):
            g.start = B
        self.assertIsNone(g.start)

    def test_shouldNotSetStartSymbolWhenCreate(self):
        with self.assertRaises(NonterminalDoesNotExistsException):
            g = Grammar(nonterminals=[B],
                        start_symbol=A)

    def test_oldStartSymbolShouldStaySame(self):
        g = Grammar(nonterminals=[A],
                    start_symbol=A)
        self.assertIsNotNone(g.start)
        with self.assertRaises(NonterminalDoesNotExistsException):
            g.start = B
        self.assertIsNotNone(g.start)
        self.assertIs(g.start, A)


if __name__ == '__main__':
    main()
