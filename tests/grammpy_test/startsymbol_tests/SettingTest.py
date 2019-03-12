#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:06
:Licence GPLv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *


class A(Nonterminal): pass
class B(Nonterminal): pass


class SettingTest(TestCase):
    def test_setStartSymbol(self):
        g = Grammar(nonterminals=[A])
        self.assertIsNone(g.start)
        g.start = A
        self.assertIsNotNone(g.start)
        self.assertEqual(g.start, A)
        self.assertTrue(g.start is A)

    def test_setStartSymbolInInit(self):
        g = Grammar(nonterminals=[A],
                    start_symbol=A)
        self.assertIsNotNone(g.start)
        self.assertEqual(g.start, A)
        self.assertTrue(g.start is A)


if __name__ == '__main__':
    main()
