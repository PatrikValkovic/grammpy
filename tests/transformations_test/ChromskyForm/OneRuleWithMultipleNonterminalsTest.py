#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.08.2017 14:37
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rules(Rule):
    rules = [([S], [A, B, C])]


class OneRuleWithMultipleNonterminalsTest(TestCase):
    def test_transform(self):
        g = Grammar(nonterminals=[S, A, B, C],
                    rules=[Rules])
        com = ContextFree.transform_to_chomsky_normal_form(g)
        self.assertEqual(com.rules.size(), 2)
        self.assertEqual(len(com.rules), 2)
        from_s = list(filter(lambda r: r.fromSymbol == S, com.rules))[0]
        self.assertEqual(from_s.right[0], A)
        temp = from_s.right[1]
        temp_rule = list(filter(lambda r: r.right == [B, C], com.rules))[0]
        self.assertEqual(temp, temp_rule.fromSymbol)
        self.assertEqual(com.nonterminals.size(), 5)
        self.assertEqual(len(com.nonterminals), 5)

    def test_transformShouldNotChange(self):
        g = Grammar(nonterminals=[S, A, B, C],
                    rules=[Rules])
        ContextFree.transform_to_chomsky_normal_form(g)
        self.assertEqual(g.rules.size(), 1)
        self.assertEqual(len(g.rules), 1)
        self.assertIn(Rules, g.rules)

    def test_transformShouldChange(self):
        g = Grammar(nonterminals=[S, A, B, C],
                    rules=[Rules])
        ContextFree.transform_to_chomsky_normal_form(g, True)
        self.assertEqual(g.rules.size(), 2)
        self.assertEqual(len(g.rules), 2)
        from_s = list(filter(lambda r: r.fromSymbol == S, g.rules))[0]
        self.assertEqual(from_s.right[0], A)
        temp = from_s.right[1]
        from_temp = list(filter(lambda r: r.right == [B, C], g.rules))[0]
        self.assertEqual(temp, from_temp.fromSymbol)
        self.assertEqual(g.nonterminals.size(), 5)
        self.assertEqual(len(g.nonterminals), 5)


if __name__ == '__main__':
    main()
