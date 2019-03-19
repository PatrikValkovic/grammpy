#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 15:07
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from grammpy.exceptions import NotParsedException, StartSymbolNotSetException
from grammpy.parsers import cyk


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass


class SAB(Rule): rule = ([S], [A, B])
class A0(Rule): rule = ([A], [0])
class BCD(Rule): rule = ([B], [C, D])
class C1(Rule): rule = ([C], [1])
class D2(Rule): rule = ([D], [2])


class FiveNonterminalsTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0, 1, 2],
                         nonterminals=[S, A, B, C, D],
                         rules=[SAB, A0, BCD, C1, D2],
                         start_symbol=S)

    def test_shouldntParse(self):
        with self.assertRaises(Exception):
            cyk(self.g, [1, 1, 2])

    def test_shouldRaiseNotParsed(self):
        with self.assertRaises(NotParsedException):
            cyk(self.g, [1, 1, 2])

    def test_shouldRaiseStartSymbolNotSet(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[S, A, B, C, D],
                    rules=[SAB, A0, BCD, C1, D2])
        with self.assertRaises(StartSymbolNotSetException):
            cyk(g, [0, 1, 2])


if __name__ == '__main__':
    main()
