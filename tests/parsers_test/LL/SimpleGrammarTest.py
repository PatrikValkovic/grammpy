#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 09.12.2024 22:02
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_LL_parsing_table
from grammpy.transforms import *

class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class RuleS(Rule):
    rule = ([S], [A, B])
class RuleB(Rule):
    rule = ([B], [1])
class RuleAToZero(Rule):
    rule = ([A], [0])
class RuleAToEpsilon(Rule):
    rule = ([A], [EPSILON])
g = Grammar(terminals=[0, 1],
            nonterminals=[S, A, B],
            rules=[RuleS, RuleB, RuleAToZero, RuleAToEpsilon],
            start_symbol=S)

class SimpleGrammarTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_LL_parsing_table(g, first_table, follow_table, 1)

        self.assertEqual(2, len(parsing_table[S]))
        self.assertIn((0,), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S][0,]))
        self.assertIn(RuleS, parsing_table[S][0,])
        self.assertIn((1,), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S][1,]))
        self.assertIn(RuleS, parsing_table[S][1,])

        self.assertEqual(1, len(parsing_table[B]))
        self.assertIn((1,), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B][1,]))
        self.assertIn(RuleB, parsing_table[B][1,])

        self.assertEqual(2, len(parsing_table[A]))
        self.assertIn((0,), parsing_table[A])
        self.assertEqual(1, len(parsing_table[A][0,]))
        self.assertIn(RuleAToZero, parsing_table[A][0,])
        self.assertIn((1,), parsing_table[A])
        self.assertEqual(1, len(parsing_table[A][1,]))
        self.assertIn(RuleAToEpsilon, parsing_table[A][1,])


if __name__ == '__main__':
    main()

