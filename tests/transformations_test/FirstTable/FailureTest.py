#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 21:30
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import *


class S(Nonterminal): pass
class Rules(Rule):
    rule = ([S], [0])
g = Grammar(terminals=[0],
            nonterminals=[S],
            rules=[Rules],
            start_symbol=S)


class LookAhead1Test(TestCase):
    def test_negative_lookahead(self):
        self.assertRaises(ValueError, lambda: ContextFree.create_first_table(g, -1))

    def test_zero_lookahead(self):
        self.assertRaises(ValueError, lambda: ContextFree.create_first_table(g, 0))

    def test_string_lookahead(self):
        self.assertRaises(TypeError, lambda: ContextFree.create_first_table(g, 'a'))


if __name__ == '__main__':
    main()
