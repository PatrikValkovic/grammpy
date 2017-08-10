#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 23:00
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class SettingTest(TestCase):
    def test_setStartSymbol(self):
        g = Grammar(nonterminals=[A])
        self.assertFalse(g.start_isSet())
        g.start_set(A)
        self.assertTrue(g.start_isSet())
        self.assertEqual(g.start_get(), A)
        self.assertTrue(g.start_is(A))

    def test_setStartSymbolInInit(self):
        g = Grammar(nonterminals=[A], start_symbol=A)
        self.assertTrue(g.start_isSet())
        self.assertEqual(g.start_get(), A)
        self.assertTrue(g.start_is(A))


if __name__ == '__main__':
    main()
