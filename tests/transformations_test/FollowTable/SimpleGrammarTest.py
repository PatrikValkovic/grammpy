#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 08.12.2024 19:53
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
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
        self.assertEqual(len(follow_table[S]), 1)
        self.assertIn((END_OF_INPUT,), follow_table[S])
        self.assertEqual(len(follow_table[A]), 1)
        self.assertIn((1,), follow_table[A])
        self.assertEqual(len(follow_table[B]), 1)
        self.assertIn((END_OF_INPUT,), follow_table[B])


if __name__ == '__main__':
    main()
