#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 14.12.2024 14:28
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table, ll
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

class SimpleTableTest(TestCase):
    def test_lookAhead1WithA(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        parsed = ll(g.start, [0, 1], parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleS
   |--(N)A
   |  `--(R)RuleAToZero
   |     `--(T)0
   `--(N)B
      `--(R)RuleB
         `--(T)1
""".lstrip()
        )

    def test_lookAhead1WithoutA(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        parsed = ll(g.start, [1], parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleS
   |--(N)A
   |  `--(R)RuleAToEpsilon
   |     `--(T)EPSILON
   `--(N)B
      `--(R)RuleB
         `--(T)1
""".lstrip()
        )

if __name__ == '__main__':
    main()
