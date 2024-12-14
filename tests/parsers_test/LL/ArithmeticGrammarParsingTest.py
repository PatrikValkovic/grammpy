#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2024 21:09
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Nonterminal, Rule, EPSILON, Grammar, END_OF_INPUT, Terminal
from grammpy.parsers import create_ll_parsing_table, ll
from grammpy.transforms import ContextFree
from grammpy.transforms import Traversing

class ArithmeticGrammarParsingTest(TestCase):
    def test_plusMultiplyLookAhead1(self):
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
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        sequence = ['id', '+', 'id', '*', 'id']
        parsed = ll(g.start, sequence, parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)E
`--(R)RuleE
   |--(N)T
   |  `--(R)RuleT
   |     |--(N)F
   |     |  `--(R)RuleNum
   |     |     `--(T)id
   |     `--(N)Tcap
   |        `--(R)RuleTcapEps
   |           `--(T)EPSILON
   `--(N)Ecap
      `--(R)RuleEcap
         |--(T)+
         |--(N)T
         |  `--(R)RuleT
         |     |--(N)F
         |     |  `--(R)RuleNum
         |     |     `--(T)id
         |     `--(N)Tcap
         |        `--(R)RuleTcap
         |           |--(T)*
         |           |--(N)F
         |           |  `--(R)RuleNum
         |           |     `--(T)id
         |           `--(N)Tcap
         |              `--(R)RuleTcapEps
         |                 `--(T)EPSILON
         `--(N)Ecap
            `--(R)RuleEcapEps
               `--(T)EPSILON
""".lstrip()
        )

    def test_plusMultiplyWithInstancesLookAhead1(self):
        class Num(Terminal):
            def __init__(self, symbol):
                super().__init__(symbol)
            def __hash__(self):
                return hash(Num)
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
            rule = ([F], [Num])
        class RuleBrackets(Rule):
            rule = ([F], ['(', E, ')'])
        g = Grammar(terminals=[Num, '+', '*', '(', ')'],
                    nonterminals=[E, Ecap, T, Tcap, F],
                    rules=[RuleE, RuleEcap, RuleEcapEps, RuleT, RuleTcap, RuleTcapEps, RuleNum, RuleBrackets],
                    start_symbol=E)
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        sequence = [Num(5), '+', Num(4), '*', Num(0)]
        parsed = ll(g.start, sequence, parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)E
`--(R)RuleE
   |--(N)T
   |  `--(R)RuleT
   |     |--(N)F
   |     |  `--(R)RuleNum
   |     |     `--(T)5
   |     `--(N)Tcap
   |        `--(R)RuleTcapEps
   |           `--(T)EPSILON
   `--(N)Ecap
      `--(R)RuleEcap
         |--(T)+
         |--(N)T
         |  `--(R)RuleT
         |     |--(N)F
         |     |  `--(R)RuleNum
         |     |     `--(T)4
         |     `--(N)Tcap
         |        `--(R)RuleTcap
         |           |--(T)*
         |           |--(N)F
         |           |  `--(R)RuleNum
         |           |     `--(T)0
         |           `--(N)Tcap
         |              `--(R)RuleTcapEps
         |                 `--(T)EPSILON
         `--(N)Ecap
            `--(R)RuleEcapEps
               `--(T)EPSILON
""".lstrip()
        )

    def test_plusMultiplyLookAhead2(self):
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
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 2)
        sequence = ['id', '+', 'id', '*', 'id']
        parsed = ll(g.start, sequence, parsing_table, 2)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)E
`--(R)RuleE
   |--(N)T
   |  `--(R)RuleT
   |     |--(N)F
   |     |  `--(R)RuleNum
   |     |     `--(T)id
   |     `--(N)Tcap
   |        `--(R)RuleTcapEps
   |           `--(T)EPSILON
   `--(N)Ecap
      `--(R)RuleEcap
         |--(T)+
         |--(N)T
         |  `--(R)RuleT
         |     |--(N)F
         |     |  `--(R)RuleNum
         |     |     `--(T)id
         |     `--(N)Tcap
         |        `--(R)RuleTcap
         |           |--(T)*
         |           |--(N)F
         |           |  `--(R)RuleNum
         |           |     `--(T)id
         |           `--(N)Tcap
         |              `--(R)RuleTcapEps
         |                 `--(T)EPSILON
         `--(N)Ecap
            `--(R)RuleEcapEps
               `--(T)EPSILON
""".lstrip()
        )

    def test_plusMultiplyWithInstancesLookAhead2(self):
        class Num(Terminal):
            def __init__(self, symbol):
                super().__init__(symbol)
            def __hash__(self):
                return hash(Num)
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
            rule = ([F], [Num])
        class RuleBrackets(Rule):
            rule = ([F], ['(', E, ')'])
        g = Grammar(terminals=[Num, '+', '*', '(', ')'],
                    nonterminals=[E, Ecap, T, Tcap, F],
                    rules=[RuleE, RuleEcap, RuleEcapEps, RuleT, RuleTcap, RuleTcapEps, RuleNum, RuleBrackets],
                    start_symbol=E)
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 2)
        sequence = [Num(5), '+', Num(4), '*', Num(0)]
        parsed = ll(g.start, sequence, parsing_table, 2)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)E
`--(R)RuleE
   |--(N)T
   |  `--(R)RuleT
   |     |--(N)F
   |     |  `--(R)RuleNum
   |     |     `--(T)5
   |     `--(N)Tcap
   |        `--(R)RuleTcapEps
   |           `--(T)EPSILON
   `--(N)Ecap
      `--(R)RuleEcap
         |--(T)+
         |--(N)T
         |  `--(R)RuleT
         |     |--(N)F
         |     |  `--(R)RuleNum
         |     |     `--(T)4
         |     `--(N)Tcap
         |        `--(R)RuleTcap
         |           |--(T)*
         |           |--(N)F
         |           |  `--(R)RuleNum
         |           |     `--(T)0
         |           `--(N)Tcap
         |              `--(R)RuleTcapEps
         |                 `--(T)EPSILON
         `--(N)Ecap
            `--(R)RuleEcapEps
               `--(T)EPSILON
""".lstrip()
        )

if __name__ == '__main__':
    main()
