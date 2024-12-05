#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.12.2024 12:25
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
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        self.assertEqual(len(follow_table[S]), 1)
        self.assertEqual(len(follow_table[A]), 1)
        self.assertEqual(len(follow_table[B]), 1)
        self.assertIn(END_OF_INPUT, follow_table[S])
        self.assertIn((1,), follow_table[A])
        self.assertIn(END_OF_INPUT, follow_table[B])

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
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        self.assertEqual(len(follow_table[E]), 2)
        self.assertEqual(len(follow_table[Ecap]), 2)
        self.assertEqual(len(follow_table[T]), 3)
        self.assertEqual(len(follow_table[Tcap]), 3)
        self.assertEqual(len(follow_table[F]), 4)
        self.assertIn(END_OF_INPUT, follow_table[E])
        self.assertIn((')',), follow_table[E])
        self.assertIn(END_OF_INPUT, follow_table[Ecap])
        self.assertIn((')',), follow_table[Ecap])
        self.assertIn(END_OF_INPUT, follow_table[T])
        self.assertIn((')',), follow_table[T])
        self.assertIn(('+',), follow_table[T])
        self.assertIn(END_OF_INPUT, follow_table[Tcap])
        self.assertIn((')',), follow_table[Tcap])
        self.assertIn(('+',), follow_table[Tcap])
        self.assertIn(END_OF_INPUT, follow_table[F])
        self.assertIn((')',), follow_table[F])
        self.assertIn(('+',), follow_table[F])
        self.assertIn(('*',), follow_table[F])

    def test_opendsa(self):
        # taken from: https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS21/html/LLParsing.html
        class S(Nonterminal): pass
        class B(Nonterminal): pass
        class Rules(Rule):
            rules = [
                ([S], ['a', S, 'c']),
                ([S], [B]),
                ([B], ['b']),
                ([B], ['lambda'])
            ]
        g = Grammar(terminals=['a', 'b', 'c', 'lambda'],
                    nonterminals=[S, B],
                    rules=[Rules],
                    start_symbol=S)
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        self.assertEqual(len(follow_table[S]), 2)
        self.assertEqual(len(follow_table[B]), 2)
        self.assertIn(END_OF_INPUT, follow_table[S])
        self.assertIn(('c',), follow_table[S])
        self.assertIn(END_OF_INPUT, follow_table[B])
        self.assertIn(('c',), follow_table[B])

if __name__ == '__main__':
    main()
