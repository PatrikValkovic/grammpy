#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.12.2024 12:25
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *

class LookAhead2Test(TestCase):
    def test_duke(self):
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
        first_table = ContextFree.create_first_table(g, 2)
        follow_table = ContextFree.create_follow_table(g, first_table, 2)
        self.assertEqual(len(follow_table[S]), 1)
        self.assertEqual(len(follow_table[A]), 2)
        self.assertEqual(len(follow_table[B]), 2)
        self.assertIn(END_OF_INPUT, follow_table[S])
        self.assertIn((2,), follow_table[A])
        self.assertIn((3, 1), follow_table[A])
        self.assertIn(END_OF_INPUT, follow_table[B])
        self.assertIn((2,), follow_table[B])


if __name__ == '__main__':
    main()
