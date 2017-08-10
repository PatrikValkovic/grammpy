#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
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


class NonterminalHaveTest(TestCase):
    def test_haveNontermEmpty(self):
        gr = Grammar()
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertFalse(gr.have_nonterm(Second))

    def test_haveNontermClass(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        self.assertTrue(gr.have_nonterm(TempClass))

    def test_haveNontermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, Second, Third])
        self.assertTrue(gr.have_term([Second, TempClass]))

    def test_dontHaveNontermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, Second])
        self.assertFalse(gr.have_term([TempClass, Third]))

    def test_haveNontermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, Second, Third])
        self.assertTrue(gr.have_term((Third, TempClass)))

    def test_dontHaveNontermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, Second])
        self.assertFalse(gr.have_term((TempClass, Third)))



if __name__ == '__main__':
    main()
