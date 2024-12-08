#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 21:01
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *

# taken from: https://courses.cs.duke.edu/cps140/spring99/lects/sectllparseH.pdf
class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [A, 3, B]),
        ([A], [1, A, 2]),
        ([A], [1, 2]),
        ([B], [1, B, 2]),
        ([B], [1, 3, 2]),
    ]
g = Grammar(terminals=[1, 2, 3],
            nonterminals=[S, A, B],
            rules=[Rules],
            start_symbol=S)

class DukeGrammarTest(TestCase):
    def test_lookAhead2(self):
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        self.assertEqual(len(follow_table[S]), 1)
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[S])
        self.assertEqual(len(follow_table[A]), 3)
        self.assertIn((3, 1), follow_table[A])
        self.assertIn((2, 3), follow_table[A])
        self.assertIn((2, 2), follow_table[A])
        self.assertEqual(len(follow_table[B]), 3)
        self.assertIn((END_OF_INPUT, END_OF_INPUT), follow_table[B])
        self.assertIn((2, END_OF_INPUT), follow_table[B])
        self.assertIn((2, 2), follow_table[B])

if __name__ == '__main__':
    main()
