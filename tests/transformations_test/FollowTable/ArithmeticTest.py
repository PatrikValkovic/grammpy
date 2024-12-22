#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 08.12.2024 19:52
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *

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

class ArithmeticTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        self.assertEqual(len(follow_table[E]), 2)
        self.assertEqual(len(follow_table[Ecap]), 2)
        self.assertEqual(len(follow_table[T]), 3)
        self.assertEqual(len(follow_table[Tcap]), 3)
        self.assertEqual(len(follow_table[F]), 4)
        self.assertIn((END_OF_INPUT,), follow_table[E])
        self.assertIn((')',), follow_table[E])
        self.assertIn((END_OF_INPUT,), follow_table[Ecap])
        self.assertIn((')',), follow_table[Ecap])
        self.assertIn((END_OF_INPUT,), follow_table[T])
        self.assertIn((')',), follow_table[T])
        self.assertIn(('+',), follow_table[T])
        self.assertIn((END_OF_INPUT,), follow_table[Tcap])
        self.assertIn((')',), follow_table[Tcap])
        self.assertIn(('+',), follow_table[Tcap])
        self.assertIn((END_OF_INPUT,), follow_table[F])
        self.assertIn((')',), follow_table[F])
        self.assertIn(('+',), follow_table[F])
        self.assertIn(('*',), follow_table[F])

    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        self.assertEqual(len(follow_table[E]), 5)
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[E])
        self.assertIn((')', ')'), follow_table[E])
        self.assertIn((')', '+'), follow_table[E])
        self.assertIn((')', '*'), follow_table[E])
        self.assertIn((')', END_OF_INPUT), follow_table[E])
        self.assertEqual(len(follow_table[Ecap]), 5)
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[Ecap])
        self.assertIn((')', '*'), follow_table[Ecap])
        self.assertIn((')', '+'), follow_table[Ecap])
        self.assertIn((')', ')'), follow_table[Ecap])
        self.assertIn((')', END_OF_INPUT), follow_table[Ecap])
        self.assertEqual(len(follow_table[T]), 7)
        self.assertIn(('+', '('), follow_table[T])
        self.assertIn(('+', 'id'), follow_table[T])
        self.assertIn((')', '*'), follow_table[T])
        self.assertIn((')', '+'), follow_table[T])
        self.assertIn((')', END_OF_INPUT), follow_table[T])
        self.assertIn((')', ')'), follow_table[T])
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[T])
        self.assertEqual(len(follow_table[Tcap]), 7)
        self.assertIn(('+', '('), follow_table[Tcap])
        self.assertIn(('+', 'id'), follow_table[Tcap])
        self.assertIn((')', '*'), follow_table[Tcap])
        self.assertIn((')', '+'), follow_table[Tcap])
        self.assertIn((')', ')'), follow_table[Tcap])
        self.assertIn((')', END_OF_INPUT), follow_table[Tcap])
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[Tcap])
        self.assertEqual(len(follow_table[F]), 9)
        self.assertIn(('*', '('), follow_table[F])
        self.assertIn(('*', 'id'), follow_table[F])
        self.assertIn(('+', '('), follow_table[F])
        self.assertIn(('+', 'id'), follow_table[F])
        self.assertIn((')', '*'), follow_table[F])
        self.assertIn((')', '+'), follow_table[F])
        self.assertIn((')', ')'), follow_table[F])
        self.assertIn((')', END_OF_INPUT), follow_table[F])
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[F])


if __name__ == '__main__':
    main()
