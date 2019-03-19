#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.03.2019 16:53
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.exceptions import StartSymbolNotSetException
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass


class SimpleTest(TestCase):
    def test_startNotSet(self):
        class Rules(Rule):
            rules = [
                ([A], [0, B]),
                ([B], [1, C]),
                ([C], [0])
            ]
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D],
                    rules=[Rules])
        self.assertIsNone(g.start)
        with self.assertRaises(StartSymbolNotSetException):
            ContextFree.remove_unreachable_symbols(g)


if __name__ == '__main__':
    main()
