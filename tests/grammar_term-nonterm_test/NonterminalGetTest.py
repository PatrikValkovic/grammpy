#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import Grammar
from grammpy import Nonterminal


class TempClass(Nonterminal):
    pass


class Second(Nonterminal):
    pass


class Third(Nonterminal):
    pass


class TerminalGetTest(TestCase):
    def test_getNontermEmpty(self):
        gr = Grammar()
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(Second))
        self.assertIsNone(gr.get_nonterm(Third))

    def test_getNontermClass(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.get_nonterm(TempClass), TempClass)

    def test_getNontermArray(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        g = gr.get_term([Second, TempClass])
        for i in g:
            self.assertTrue(i in [TempClass, Second, Third])
        self.assertEqual(g[0], Second)
        self.assertEqual(g[1], TempClass)

    def test_dontGetNontermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, Second])
        g = gr.get_term([TempClass, Third])
        self.assertEqual(g[0], TempClass)
        self.assertIsNone(g[1])

    def test_getNontermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, Second, Third])
        g = gr.get_term((Third, TempClass))
        for i in g:
            self.assertTrue(i in [TempClass, Second, Third])
        self.assertEqual(g[0], Third)
        self.assertEqual(g[1], TempClass)

    def test_dontGetNontermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, Second])
        g = gr.get_term((TempClass, Third))
        self.assertEqual(g[0], TempClass)
        self.assertIsNone(g[1])


if __name__ == '__main__':
    main()
