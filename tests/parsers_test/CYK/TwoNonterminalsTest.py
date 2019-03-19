#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 15:01
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import cyk


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class SAB(Rule): rule=([S], [A, B])
class A0(Rule): rule=([A], [0])
class B1(Rule): rule=([B], [1])



class TwoNonterminalsTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0, 1],
                         nonterminals=[S, A, B],
                         rules=[SAB, A0, B1],
                         start_symbol=S)

    def test_shouldParse(self):
        parsed = cyk(self.g, [0, 1])

    def test_shouldParseCorrectTypes(self):
        parsed = cyk(self.g, [0, 1])
        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, SAB)
        self.assertIsInstance(parsed.to_rule.to_symbols[0], A)
        self.assertIsInstance(parsed.to_rule.to_symbols[1], B)
        self.assertIsInstance(parsed.to_rule.to_symbols[0].to_rule, A0)
        self.assertIsInstance(parsed.to_rule.to_symbols[1].to_rule, B1)
        self.assertIsInstance(parsed.to_rule.to_symbols[0].to_rule.to_symbols[0], Terminal)
        self.assertIsInstance(parsed.to_rule.to_symbols[1].to_rule.to_symbols[0], Terminal)

    def test_shouldParseCorrectSymbols(self):
        parsed = cyk(self.g, [0, 1])
        self.assertEqual(parsed.to_rule.to_symbols[0].to_rule.to_symbols[0].s, 0)
        self.assertEqual(parsed.to_rule.to_symbols[1].to_rule.to_symbols[0].s, 1)


if __name__ == '__main__':
    main()
