#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 14.12.2024 14:21
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table, ll
from grammpy.transforms import *

# taken from: https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS21/html/LLParsing.html 10.2.5
class S(Nonterminal): pass
class B(Nonterminal): pass
class RuleSSpread(Rule):
    rule = ([S], ['a', S, 'c'])
class RuleSRewrite(Rule):
    rule = ([S], [B])
class RuleBRewrite(Rule):
    rule = ([B], ['b'])
class RuleBEps(Rule):
    rule = ([B], [EPSILON])
g = Grammar(terminals=['a', 'b', 'c'],
            nonterminals=[S, B],
            rules=[RuleSSpread, RuleSRewrite, RuleBRewrite, RuleBEps],
            start_symbol=S)

class OpenDsaTableTest(TestCase):
    def test_lookAhead1WithoutB(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        parsed = ll(g.start, ['a', 'a', 'a', 'c', 'c', 'c'], parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleSSpread
   |--(T)a
   |--(N)S
   |  `--(R)RuleSSpread
   |     |--(T)a
   |     |--(N)S
   |     |  `--(R)RuleSSpread
   |     |     |--(T)a
   |     |     |--(N)S
   |     |     |  `--(R)RuleSRewrite
   |     |     |     `--(N)B
   |     |     |        `--(R)RuleBEps
   |     |     |           `--(T)EPSILON
   |     |     `--(T)c
   |     `--(T)c
   `--(T)c
""".lstrip()
        )

    def test_lookAhead1WithB(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        parsed = ll(g.start, ['a', 'a', 'a', 'b', 'c', 'c', 'c'], parsing_table, 1)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleSSpread
   |--(T)a
   |--(N)S
   |  `--(R)RuleSSpread
   |     |--(T)a
   |     |--(N)S
   |     |  `--(R)RuleSSpread
   |     |     |--(T)a
   |     |     |--(N)S
   |     |     |  `--(R)RuleSRewrite
   |     |     |     `--(N)B
   |     |     |        `--(R)RuleBRewrite
   |     |     |           `--(T)b
   |     |     `--(T)c
   |     `--(T)c
   `--(T)c
""".lstrip()
        )

    def test_lookAhead3WithB(self):
        first_table = ContextFree.create_first_table(g, 3)
        follow_table = ContextFree.create_follow_table(g, first_table, 3)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 3)
        parsed = ll(g.start, ['a', 'a', 'a', 'b', 'c', 'c', 'c'], parsing_table, 3)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleSSpread
   |--(T)a
   |--(N)S
   |  `--(R)RuleSSpread
   |     |--(T)a
   |     |--(N)S
   |     |  `--(R)RuleSSpread
   |     |     |--(T)a
   |     |     |--(N)S
   |     |     |  `--(R)RuleSRewrite
   |     |     |     `--(N)B
   |     |     |        `--(R)RuleBRewrite
   |     |     |           `--(T)b
   |     |     `--(T)c
   |     `--(T)c
   `--(T)c
""".lstrip()
        )

if __name__ == '__main__':
    main()

