#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 18:11
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *

class LookAhead1Test(TestCase):
    def test_simpleExample(self):
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
        first_table = ContextFree.create_first_table(g, 1)
        self.assertEqual(len(first_table[S]), 2)
        self.assertEqual(len(first_table[A]), 2)
        self.assertEqual(len(first_table[B]), 1)
        self.assertIn((0,), first_table[S])
        self.assertIn((1,), first_table[S])
        self.assertIn((0,), first_table[A])
        self.assertIn(EPSILON, first_table[A])
        self.assertIn((1,), first_table[B])

    def test_arithmetic(self):
        class E(Nonterminal): pass
        class Ecap(Nonterminal): pass
        class T(Nonterminal): pass
        class Tcap(Nonterminal): pass
        class F(Nonterminal): pass
        class Rules(Rule):
            rules = [
                ([E], [T, Ecap]),
                ([Ecap], ['+', T, Ecap]),
                ([Ecap], [EPSILON]),
                ([T], [F, Tcap]),
                ([Tcap], ['*', F, Tcap]),
                ([Tcap], [EPSILON]),
                ([F], ['(', E, ')']),
                ([F], ['id']),
            ]
        g = Grammar(terminals=['id', '+', '*', '(', ')'],
                    nonterminals=[E, Ecap, T, Tcap, F],
                    rules=[Rules],
                    start_symbol=E)
        first_table = ContextFree.create_first_table(g, 1)
        self.assertEqual(len(first_table[E]), 2)
        self.assertEqual(len(first_table[Ecap]), 2)
        self.assertEqual(len(first_table[T]), 2)
        self.assertEqual(len(first_table[Tcap]), 2)
        self.assertEqual(len(first_table[F]), 2)
        self.assertIn(('id', ), first_table[E])
        self.assertIn(('(', ), first_table[E])
        self.assertIn(('+', ), first_table[Ecap])
        self.assertIn(EPSILON, first_table[Ecap])
        self.assertIn(('id', ), first_table[T])
        self.assertIn(('(', ), first_table[T])
        self.assertIn(('*', ), first_table[Tcap])
        self.assertIn(EPSILON, first_table[Tcap])
        self.assertIn(('(', ), first_table[F])
        self.assertIn(('id', ), first_table[F])


if __name__ == '__main__':
    main()
