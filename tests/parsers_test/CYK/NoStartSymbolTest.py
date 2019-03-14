#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:51
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from grammpy.exceptions import StartSymbolNotSetException
from grammpy.parsers import cyk


class S(Nonterminal): pass
class R(Rule): rule = ([S], [0])


class OneRuleTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0],
                         nonterminals=[S],
                         rules=[R],
                         start_symbol=None)

    def test_shouldntParse(self):
        with self.assertRaises(Exception):
            cyk(self.g, [0])

    def test_shouldRaiseStartSymbolNotSet(self):
        with self.assertRaises(StartSymbolNotSetException):
            cyk(self.g, [0])


if __name__ == '__main__':
    main()
