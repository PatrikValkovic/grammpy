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


class ArithmeticGrammarTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_LL_parsing_table(g, first_table, follow_table, 1)

        self.assertEqual(2, len(parsing_table[E]))
        self.assertIn(('id',), parsing_table[E])
        self.assertEqual(1, len(parsing_table[E]['id',]))
        self.assertIn(RuleE, parsing_table[E]['id',])
        self.assertIn(('(',), parsing_table[E])
        self.assertEqual(1, len(parsing_table[E]['(',]))
        self.assertIn(RuleE, parsing_table[E]['(',])

        self.assertEqual(3, len(parsing_table[Ecap]))
        self.assertIn(('+',), parsing_table[Ecap])
        self.assertEqual(1, len(parsing_table[Ecap]['+',]))
        self.assertIn(RuleEcap, parsing_table[Ecap]['+',])
        self.assertIn((')',), parsing_table[Ecap])
        self.assertEqual(1, len(parsing_table[Ecap][')',]))
        self.assertIn(RuleEcapEps, parsing_table[Ecap][')',])
        self.assertIn((END_OF_INPUT,), parsing_table[Ecap])
        self.assertEqual(1, len(parsing_table[Ecap][END_OF_INPUT,]))
        self.assertIn(RuleEcapEps, parsing_table[Ecap][END_OF_INPUT,])

        self.assertEqual(2, len(parsing_table[T]))
        self.assertIn(('id',), parsing_table[T])
        self.assertEqual(1, len(parsing_table[T]['id',]))
        self.assertIn(RuleT, parsing_table[T]['id',])
        self.assertIn(('(',), parsing_table[T])
        self.assertEqual(1, len(parsing_table[T]['(',]))
        self.assertIn(RuleT, parsing_table[T]['(',])

        self.assertEqual(4, len(parsing_table[Tcap]))
        self.assertIn(('*',), parsing_table[Tcap])
        self.assertEqual(1, len(parsing_table[Tcap]['*',]))
        self.assertIn(RuleTcap, parsing_table[Tcap]['*',])
        self.assertIn(('+',), parsing_table[Tcap])
        self.assertEqual(1, len(parsing_table[Tcap]['+',]))
        self.assertIn(RuleTcapEps, parsing_table[Tcap]['+',])
        self.assertIn((')',), parsing_table[Tcap])
        self.assertEqual(1, len(parsing_table[Tcap][')',]))
        self.assertIn(RuleTcapEps, parsing_table[Tcap][')',])
        self.assertIn((END_OF_INPUT,), parsing_table[Tcap])
        self.assertEqual(1, len(parsing_table[Tcap][END_OF_INPUT,]))
        self.assertIn(RuleTcapEps, parsing_table[Tcap][END_OF_INPUT,])

        self.assertEqual(2, len(parsing_table[F]))
        self.assertIn(('id',), parsing_table[F])
        self.assertEqual(1, len(parsing_table[F]['id',]))
        self.assertIn(RuleNum, parsing_table[F]['id',])
        self.assertIn(('(',), parsing_table[F])
        self.assertEqual(1, len(parsing_table[F]['(',]))
        self.assertIn(RuleBrackets, parsing_table[F]['(',])

    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_LL_parsing_table(g, first_table, follow_table, 2)

        self.assertEqual(6, len(parsing_table[E]))
        E_tuples = [
            ('id', END_OF_INPUT),
            ('(', '('),
            ('(', 'id'),
            ('id', '+'),
            ('id', '*'),
            ('id', ')'),
        ]
        for t in E_tuples:
            self.assertIn(t, parsing_table[E])
            self.assertEqual(1, len(parsing_table[E][t]))
            self.assertIn(RuleE, parsing_table[E][t])

        self.assertEqual(7, len(parsing_table[Ecap]))
        Ecap_exp_tuples = [
            ('+', 'id'),
            ('+', '('),
        ]
        Ecap_eps_tuples = [
            (')', '+'),
            (')', '*'),
            (')', ')'),
            (')', END_OF_INPUT),
            (END_OF_INPUT, END_OF_INPUT),
        ]
        for t in Ecap_exp_tuples:
            self.assertIn(t, parsing_table[Ecap])
            self.assertEqual(1, len(parsing_table[Ecap][t]))
            self.assertIn(RuleEcap, parsing_table[Ecap][t])
        for t in Ecap_eps_tuples:
            self.assertIn(t, parsing_table[Ecap])
            self.assertEqual(1, len(parsing_table[Ecap][t]))
            self.assertIn(RuleEcapEps, parsing_table[Ecap][t])

        self.assertEqual(6, len(parsing_table[T]))
        T_tuples = [
            ('id', END_OF_INPUT),
            ('(', '('),
            ('(', 'id'),
            ('id', '+'),
            ('id', '*'),
            ('id', ')'),
        ]
        for t in T_tuples:
            self.assertIn(t, parsing_table[T])
            self.assertEqual(1, len(parsing_table[T][t]))
            self.assertIn(RuleT, parsing_table[T][t])

        self.assertEqual(9, len(parsing_table[Tcap]))
        Tcap_exp_tuples = [
            ('*', 'id'),
            ('*', '('),
        ]
        Tcap_eps_tuples = [
            ('+', 'id'),
            ('+', '('),
            (')', '+'),
            (')', '*'),
            (')', ')'),
            (')', END_OF_INPUT),
            (END_OF_INPUT, END_OF_INPUT),
        ]
        for t in Tcap_exp_tuples:
            self.assertIn(t, parsing_table[Tcap])
            self.assertEqual(1, len(parsing_table[Tcap][t]))
            self.assertIn(RuleTcap, parsing_table[Tcap][t])
        for t in Tcap_eps_tuples:
            self.assertIn(t, parsing_table[Tcap])
            self.assertEqual(1, len(parsing_table[Tcap][t]))
            self.assertIn(RuleTcapEps, parsing_table[Tcap][t])

        self.assertEqual(6, len(parsing_table[F]))
        F_id_tuples = [
            ('id', '+'),
            ('id', '*'),
            ('id', ')'),
            ('id', END_OF_INPUT),
        ]
        F_brackets_tuples = [
            ('(', 'id'),
            ('(', '('),
        ]
        for t in F_id_tuples:
            self.assertIn(t, parsing_table[F])
            self.assertEqual(1, len(parsing_table[F][t]))
            self.assertIn(RuleNum, parsing_table[F][t])
        for t in F_brackets_tuples:
            self.assertIn(t, parsing_table[F])
            self.assertEqual(1, len(parsing_table[F][t]))
            self.assertIn(RuleBrackets, parsing_table[F][t])


if __name__ == '__main__':
    main()
