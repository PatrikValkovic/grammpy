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


class NonterminalIterationTest(TestCase):
    def test_oneTerminalTerms(self):
        gr = Grammar()
        gr.add_term('a')
        for i in gr.terms():
            self.assertEqual(i.s, 'a')

    def test_oneTerminalGetTerm(self):
        gr = Grammar()
        gr.add_term('a')
        for i in gr.get_term():
            self.assertEqual(i.s, 'a')

    def test_ThreeTerminalTerms(self):
        gr = Grammar()
        gr.add_term([0, 'a', TempClass])
        s = set(term.s for term in gr.terms())
        for i in [0, 'a', TempClass]:
            self.assertTrue(i in s)

    def test_ThreeTerminalGetTerm(self):
        gr = Grammar()
        gr.add_term([0, 'a', TempClass])
        s = set(term.s for term in gr.get_term())
        for i in [0, 'a', TempClass]:
            self.assertTrue(i in s)


if __name__ == '__main__':
    main()
