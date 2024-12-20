#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 09.12.2024 21:53
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table
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

class DukeGrammarTableTest(TestCase):
    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 2)

        self.assertEqual(2, len(parsing_table[S]))
        self.assertIn((1, 1), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S][1,1]))
        self.assertIn(RuleS, parsing_table[S][1,1])
        self.assertIn((1, 2), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S][1,2]))
        self.assertIn(RuleS, parsing_table[S][1,2])

        self.assertEqual(2, len(parsing_table[A]))
        self.assertIn((1, 1), parsing_table[A])
        self.assertEqual(1, len(parsing_table[A][1,1]))
        self.assertIn(RuleA1, parsing_table[A][1,1])
        self.assertIn((1, 2), parsing_table[A])
        self.assertEqual(1, len(parsing_table[A][1,2]))
        self.assertIn(RuleA2, parsing_table[A][1, 2])

        self.assertEqual(2, len(parsing_table[B]))
        self.assertIn((1, 1), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B][1, 1]))
        self.assertIn(RuleB1, parsing_table[B][1, 1])
        self.assertIn((1, 3), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B][1, 3]))
        self.assertIn(RuleB2, parsing_table[B][1, 3])


if __name__ == '__main__':
    main()

