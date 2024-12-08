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
        self.assertEqual(len(first_table[S]), 3)
        self.assertEqual(len(first_table[B]), 2)
        self.assertIn(('a', ), first_table[S])
        self.assertIn(('b', ), first_table[S])
        self.assertIn(('lambda', ), first_table[S])
        self.assertIn(('b', ), first_table[B])
        self.assertIn(('lambda', ), first_table[B])


if __name__ == '__main__':
    main()
