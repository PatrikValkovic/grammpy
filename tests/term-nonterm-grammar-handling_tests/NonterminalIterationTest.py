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


class NonterminalIterationTest(TestCase):
    def test_oneNonterminalTerms(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        for i in gr.nonterms():
            self.assertEqual(i, TempClass)

    def test_oneNonterminalGetNonterm(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        for i in gr.get_nonterm():
            self.assertEqual(i, TempClass)

    def test_ThreeNonterminalNonterms(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        s = gr.nonterms()
        for i in [Third, Second, TempClass]:
            self.assertIn(i, s)

    def test_ThreeNonterminalGetNonterm(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        s = gr.get_nonterm()
        for i in [Second, Third, TempClass]:
            self.assertIn(i, s)


if __name__ == '__main__':
    main()
