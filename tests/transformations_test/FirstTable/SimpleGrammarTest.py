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
        self.assertEqual(len(first_table[S]), 2)
        self.assertEqual(len(first_table[A]), 2)
        self.assertEqual(len(first_table[B]), 1)
        self.assertIn((0,), first_table[S])
        self.assertIn((1,), first_table[S])
        self.assertIn((0,), first_table[A])
        self.assertIn(EPSILON, first_table[A])
        self.assertIn((1,), first_table[B])


if __name__ == '__main__':
    main()
