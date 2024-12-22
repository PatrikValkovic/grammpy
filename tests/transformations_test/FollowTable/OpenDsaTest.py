#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 18:11
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *

# taken from: https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS21/html/LLParsing.html
class S(Nonterminal): pass
class B(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], ['a', S, 'c']),
        ([S], [B]),
        ([B], ['b']),
        ([B], ['lambda'])
    ]
g = Grammar(terminals=['a', 'b', 'c', 'lambda'],
            nonterminals=[S, B],
            rules=[Rules],
            start_symbol=S)

class OpenDsaTest(TestCase):
    def test_lookAhead1(self):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        self.assertEqual(len(follow_table[S]), 2)
        self.assertEqual(len(follow_table[B]), 2)
        self.assertIn((END_OF_INPUT,), follow_table[S])
        self.assertIn(('c',), follow_table[S])
        self.assertIn((END_OF_INPUT,), follow_table[B])
        self.assertIn(('c',), follow_table[B])


if __name__ == '__main__':
    main()
