#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:15
:Licence GPLv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *


class A(Nonterminal): pass
class B(Nonterminal): pass


class SettingTest(TestCase):
    def test_setStartSymbolToNone(self):
        g = Grammar(nonterminals=[A],
                    start_symbol=A)
        g.start = None
        self.assertIsNone(g.start)

    def test_shouldDeleteStart(self):
        g = Grammar(nonterminals=[A],
                    start_symbol=A)
        self.assertIsNotNone(g.start)
        self.assertIs(g.start, A)
        del g.start
        self.assertIsNone(g.start)
        g.start = A
        self.assertIsNotNone(g.start)
        self.assertIs(g.start, A)


if __name__ == '__main__':
    main()
