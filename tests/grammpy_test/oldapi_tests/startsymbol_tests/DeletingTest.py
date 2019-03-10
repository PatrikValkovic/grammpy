#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 23:00
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy.old_api import *


class A(Nonterminal): pass
class B(Nonterminal): pass


class SettingTest(TestCase):
    def test_setStartSymbolToNone(self):
        g = Grammar(nonterminals=[A], start_symbol=A)
        g.start_set(None)
        self.assertFalse(g.start_isSet())
        self.assertIsNone(g.start)

    def test_shouldDeleteStart(self):
        g = Grammar(nonterminals=[A], start_symbol=A)
        del g.start
        self.assertFalse(g.start_isSet())
        self.assertIsNone(g.start)


if __name__ == '__main__':
    main()
