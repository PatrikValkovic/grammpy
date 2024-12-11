#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 09.12.2024 21:42
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table
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

class OpenDsaTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)

        self.assertEqual(4, len(parsing_table[S]))
        self.assertIn(("a",), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S]["a",]))
        self.assertIn(RuleSSpread, parsing_table[S]["a",])
        self.assertIn(("c",), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S]["c",]))
        self.assertIn(RuleSRewrite, parsing_table[S]["c",])
        self.assertIn(("b", ), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S]["b",]))
        self.assertIn(RuleSRewrite, parsing_table[S]["b", ])
        self.assertIn((END_OF_INPUT,), parsing_table[S])
        self.assertEqual(1, len(parsing_table[S][END_OF_INPUT,]))
        self.assertIn(RuleSRewrite, parsing_table[S][END_OF_INPUT,])

        self.assertEqual(3, len(parsing_table[B]))
        self.assertIn(("b",), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B]["b", ]))
        self.assertIn(RuleBRewrite, parsing_table[B]["b", ])
        self.assertIn((END_OF_INPUT,), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B][END_OF_INPUT,]))
        self.assertIn(RuleBEps, parsing_table[B][END_OF_INPUT,])
        self.assertIn(("c",), parsing_table[B])
        self.assertEqual(1, len(parsing_table[B]["c", ]))
        self.assertIn(RuleBEps, parsing_table[B]["c", ])


if __name__ == '__main__':
    main()

