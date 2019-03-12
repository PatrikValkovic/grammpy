#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:18
:Licence GPLv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class ClearWithNontermTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(nonterminals=[A, B, C],
                         start_symbol=A)

    def test_shouldDeleteStart(self):
        self.g.nonterminals.remove(A)
        self.assertIsNone(self.g.start)

    def test_shouldNotDeleteStart(self):
        self.g.nonterminals.remove(B)
        self.assertIsNotNone(self.g.start)
        self.assertIs(self.g.start, A)

    def test_shouldDeleteWhenMultiple(self):
        self.g.nonterminals.remove(B, A)
        self.assertIsNone(self.g.start)

    def test_shouldNotDeleteWhenMultiple(self):
        self.g.nonterminals.remove(B, C)
        self.assertIsNotNone(self.g.start)
        self.assertIs(self.g.start, A)


if __name__ == '__main__':
    main()
