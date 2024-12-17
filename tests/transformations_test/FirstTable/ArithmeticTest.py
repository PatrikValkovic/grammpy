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

    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        self.assertEqual(len(first_table[E]), 5)
        self.assertIn(('id', ), first_table[E])
        self.assertIn(('id', '+'), first_table[E])
        self.assertIn(('id', '*'), first_table[E])
        self.assertIn(('(', '('), first_table[E])
        self.assertIn(('(', 'id'), first_table[E])
        self.assertEqual(len(first_table[Ecap]), 3)
        self.assertIn(('+', '('), first_table[Ecap])
        self.assertIn(('+','id'), first_table[Ecap])
        self.assertIn(EPSILON, first_table[Ecap])
        self.assertEqual(len(first_table[T]), 4)
        self.assertIn(('id',), first_table[T])
        self.assertIn(('(', 'id'), first_table[T])
        self.assertIn(('id', '*'), first_table[T])
        self.assertIn(('(', '('), first_table[T])
        self.assertEqual(len(first_table[Tcap]), 3)
        self.assertIn(('*', '('), first_table[Tcap])
        self.assertIn(('*', 'id'), first_table[Tcap])
        self.assertIn(EPSILON, first_table[Tcap])
        self.assertEqual(len(first_table[F]), 3)
        self.assertIn(('id',), first_table[F])
        self.assertIn(('(', 'id'), first_table[F])
        self.assertIn(('(', '('), first_table[F])


if __name__ == '__main__':
    main()
