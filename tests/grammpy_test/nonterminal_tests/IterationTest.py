#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 18:02
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class IterationTest(TestCase):
    def test_One(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        for t in gr.nonterminals:
            self.assertEqual(t, A)

    def test_Three(self):
        gr = Grammar()
        gr.nonterminals.add(A, B)
        s = list(nonterm for nonterm in gr.nonterminals)
        for i in [A, B]:
            self.assertIn(i, s)


if __name__ == '__main__':
    main()
