#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:51
:Licence GNUv3
Part of pyparsers

"""

from unittest import main, TestCase
from grammpy import *
from pyparsers import cyk


class S(Nonterminal): pass
class R(Rule): rule=([S], [0, 1])


class OneRuleTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0,1],
                    nonterminals=[S],
                    rules=[R],
                    start_symbol=S)

    def test_shouldParse(self):
        parsed = cyk(self.g, [0, 1])

    def test_shouldParseCorrectTypes(self):
        parsed = cyk(self.g, [0, 1])
        self.assertIsInstance(parsed, Nonterminal)
        self.assertIsInstance(parsed.to_rule, R)
        self.assertIsInstance(parsed.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(parsed.to_rule.to_nonterms[1], Terminal)

    def test_shouldParseCorrectSymbols(self):
        parsed = cyk(self.g, [0, 1])
        self.assertEqual(parsed.to_rule.to_nonterms[0].s, 0)
        self.assertEqual(parsed.to_rule.to_nonterms[1].s, 1)



if __name__ == '__main__':
    main()
