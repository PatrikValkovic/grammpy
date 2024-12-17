#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 14.12.2024 13:34
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table, ll
from grammpy.transforms import *

# taken from: https://courses.cs.duke.edu/cps140/spring99/lects/sectllparseH.pdf
class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class RuleS(Rule):
    rule = ([S], [A, 3, B])
class RuleA1(Rule):
    rule = ([A], [1, A, 2])
class RuleA2(Rule):
    rule = ([A], [1, 2])
class RuleB1(Rule):
    rule = ([B], [1, B, 2])
class RuleB2(Rule):
    rule = ([B], [1, 3, 2])
g = Grammar(terminals=[1, 2, 3],
            nonterminals=[S, A, B],
            rules=[RuleS, RuleA1, RuleA2, RuleB1, RuleB2],
            start_symbol=S)

class DukeGrammarParsingTest(TestCase):
    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 2)
        parsed = ll(g.start, [1, 1, 2, 2, 3, 1, 3, 2], parsing_table, 2)
        ast_string = Traversing.print(parsed)
        self.assertEqual(
            ast_string,
"""
(N)S
`--(R)RuleS
   |--(N)A
   |  `--(R)RuleA1
   |     |--(T)1
   |     |--(N)A
   |     |  `--(R)RuleA2
   |     |     |--(T)1
   |     |     `--(T)2
   |     `--(T)2
   |--(T)3
   `--(N)B
      `--(R)RuleB2
         |--(T)1
         |--(T)3
         `--(T)2
""".lstrip()
        )

    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        with self.assertRaises(Exception) as caught:
            ll(g.start, [1, 1, 2, 2, 3, 1, 3, 2], parsing_table, 1)
        self.assertEqual(caught.exception.args[0], 'Ambiguity found for A with lookahead (1,)')

if __name__ == '__main__':
    main()

