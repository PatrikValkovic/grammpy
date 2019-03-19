#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 22:08
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal, Rule


class N(Nonterminal): pass
class A(Rule): rule=([N], [0])
class B(Rule): rule=([N], [1])
class C(Rule): rule=([N], [2])
class D(Rule): rule=([0], [2])


class IterationTest(TestCase):
    def test_One(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        for t in gr.rules:
            self.assertEqual(t, A)

    def test_Three(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        s = list(rule for rule in gr.rules)
        for i in [A, B, C]:
            self.assertIn(i, s)


if __name__ == '__main__':
    main()
