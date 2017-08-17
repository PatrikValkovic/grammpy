#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 23:21
:Licence GNUv3
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
        self.g.remove_nonterm(A)
        self.assertFalse(self.g.start_isSet())

    def test_shouldNotDeleteStart(self):
        self.g.remove_nonterm(B)
        self.assertTrue(self.g.start_isSet())
        self.assertTrue(self.g.start_is(A))

    def test_shouldDeleteFromArray(self):
        self.g.remove_nonterm([B, A])
        self.assertFalse(self.g.start_isSet())

    def test_shouldNotDeleteFromArray(self):
        self.g.remove_nonterm([B, C])
        self.assertTrue(self.g.start_isSet())
        self.assertTrue(self.g.start_is(A))


if __name__ == '__main__':
    main()
