#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2024 21:09
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Nonterminal, Rule, EPSILON, Grammar, END_OF_INPUT
from grammpy.parsers import create_LL_parsing_table
from grammpy.transforms import ContextFree

class E(Nonterminal): pass
class Ecap(Nonterminal): pass
class T(Nonterminal): pass
class Tcap(Nonterminal): pass
class F(Nonterminal): pass
class RuleE(Rule):
    rule = ([E], [T, Ecap])
class RuleEcap(Rule):
    rule = ([Ecap], ['+', T, Ecap])
class RuleEcapEps(Rule):
    rule = ([Ecap], [EPSILON])
class RuleT(Rule):
    rule = ([T], [F, Tcap])
class RuleTcap(Rule):
    rule = ([Tcap], ['*', F, Tcap])
class RuleTcapEps(Rule):
    rule = ([Tcap], [EPSILON])
class RuleNum(Rule):
    rule = ([F], ['id'])
class RuleBrackets(Rule):
    rule = ([F], ['(', E, ')'])
g = Grammar(terminals=['id', '+', '*', '(', ')'],
            nonterminals=[E, Ecap, T, Tcap, F],
            rules=[RuleE, RuleEcap, RuleEcapEps, RuleT, RuleTcap, RuleTcapEps, RuleNum, RuleBrackets],
            start_symbol=E)

class ArithmeticTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_LL_parsing_table(g, first_table, follow_table, 1)
        self.assertIn(RuleE, parsing_table[E]['id',])
        self.assertIn(RuleE, parsing_table[E]['(',])
        self.assertIn(RuleEcap, parsing_table[Ecap]['+',])
        self.assertIn(RuleEcapEps, parsing_table[Ecap][')',])
        self.assertIn(RuleEcapEps, parsing_table[Ecap][END_OF_INPUT,])
        self.assertIn(RuleT, parsing_table[T]['id',])
        self.assertIn(RuleT, parsing_table[T]['(',])
        self.assertIn(RuleTcap, parsing_table[Tcap]['*',])
        self.assertIn(RuleTcapEps, parsing_table[Tcap]['+',])
        self.assertIn(RuleTcapEps, parsing_table[Tcap][')',])
        self.assertIn(RuleTcapEps, parsing_table[Tcap][END_OF_INPUT,])
        self.assertIn(RuleNum, parsing_table[F]['id',])
        self.assertIn(RuleBrackets, parsing_table[F]['(',])
        self.assertNotIn(('+',), parsing_table[E])
        self.assertNotIn(('*',), parsing_table[E])
        self.assertNotIn((')',), parsing_table[E])
        self.assertNotIn((END_OF_INPUT,), parsing_table[E])
        self.assertNotIn(('*',), parsing_table[Ecap])
        self.assertNotIn(('(',), parsing_table[Ecap])
        self.assertNotIn(('id',), parsing_table[Ecap])
        self.assertNotIn(('+',), parsing_table[T])
        self.assertNotIn(('*',), parsing_table[T])
        self.assertNotIn((')',), parsing_table[T])
        self.assertNotIn((END_OF_INPUT,), parsing_table[T])
        self.assertNotIn(('(',), parsing_table[Tcap])
        self.assertNotIn(('id',), parsing_table[Tcap])
        self.assertNotIn(('+',), parsing_table[F])
        self.assertNotIn(('*',), parsing_table[F])
        self.assertNotIn((')',), parsing_table[F])
        self.assertNotIn((END_OF_INPUT,), parsing_table[F])

    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_LL_parsing_table(g, first_table, follow_table, 2)
        self.assertEqual(5, len(parsing_table[E]))
        self.assertIn(('id', END_OF_INPUT), parsing_table[E])
        self.assertIn(('(', '('), parsing_table[E])
        self.assertIn(('(', 'id'), parsing_table[E])
        self.assertIn(('id', '+'), parsing_table[E])
        self.assertIn(('id', '*'), parsing_table[E])
        self.assertEqual(7, len(parsing_table[Ecap]))
        self.assertIn(('+', 'id'), parsing_table[Ecap])
        self.assertIn(('+', '('), parsing_table[Ecap])
        self.assertIn((')', '+'), parsing_table[Ecap])
        self.assertIn((')', '*'), parsing_table[Ecap])
        self.assertIn((')', ')'), parsing_table[Ecap])
        self.assertIn((')', END_OF_INPUT), parsing_table[Ecap])
        self.assertIn((END_OF_INPUT, END_OF_INPUT), parsing_table[Ecap])
        self.assertEqual(6, len(parsing_table[T]))
        self.assertIn(('id', '+'), parsing_table[T])
        self.assertIn(('id', '*'), parsing_table[T])
        self.assertIn(('id', ')'), parsing_table[T])
        self.assertIn(('(', 'id'), parsing_table[T])
        self.assertIn(('(', '('), parsing_table[T])
        self.assertIn(('id', END_OF_INPUT), parsing_table[T])
        self.assertEqual(9, len(parsing_table[Tcap]))
        self.assertIn(('+', 'id'), parsing_table[Tcap])
        self.assertIn(('+', '('), parsing_table[Tcap])
        self.assertIn(('*', 'id'), parsing_table[Tcap])
        self.assertIn(('*', '('), parsing_table[Tcap])
        self.assertIn((')', '+'), parsing_table[Tcap])
        self.assertIn((')', '*'), parsing_table[Tcap])
        self.assertIn((')', ')'), parsing_table[Tcap])
        self.assertIn((')', END_OF_INPUT), parsing_table[Tcap])
        self.assertIn((END_OF_INPUT, END_OF_INPUT), parsing_table[Tcap])
        self.assertEqual(5, len(parsing_table[F]))
        self.assertIn(('id', '+'), parsing_table[F])
        self.assertIn(('id', '*'), parsing_table[F])
        self.assertIn(('id', ')'), parsing_table[F])
        self.assertIn(('(', 'id'), parsing_table[F])
        self.assertIn(('(', '('), parsing_table[F])

if __name__ == '__main__':
    main()
