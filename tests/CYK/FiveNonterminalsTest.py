#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 15:07
:Licence GNUv3
Part of pyparsers

"""

from unittest import main, TestCase
from grammpy import *
from pyparsers import cyk


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class SAB(Rule): rule=([S], [A, B])
class A0(Rule): rule=([A], [0])
class BCD(Rule): rule=([B], [C, D])
class C1(Rule): rule=([C], [1])
class D2(Rule): rule=([D], [2])



class FiveNonterminalsTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[S, A, B, C, D],
                    rules=[SAB, A0, BCD, C1, D2],
                    start_symbol=S)

    def test_shouldParse(self):
        parsed = cyk(self.g, [0, 1, 2])

    def test_shouldParseCorrectTypes(self):
        parsed = cyk(self.g, [0, 1, 2])
        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, SAB)
        self.assertIsInstance(parsed.to_rule.to_symbols[0], A)
        self.assertIsInstance(parsed.to_rule.to_symbols[1], B)
        a = parsed.to_rule.to_symbols[0]
        b = parsed.to_rule.to_symbols[1]
        self.assertIsInstance(a.to_rule, A0)
        self.assertIsInstance(a.to_rule.to_symbols[0], Terminal)
        self.assertIsInstance(b.to_rule, BCD)
        self.assertIsInstance(b.to_rule.to_symbols[0], C)
        self.assertIsInstance(b.to_rule.to_symbols[1], D)
        c = b.to_rule.to_symbols[0]
        d = b.to_rule.to_symbols[1]
        self.assertIsInstance(c.to_rule, C1)
        self.assertIsInstance(c.to_rule.to_symbols[0], Terminal)
        self.assertIsInstance(d.to_rule, D2)
        self.assertIsInstance(d.to_rule.to_symbols[0], Terminal)

    def test_shouldParseCorrectSymbols(self):
        parsed = cyk(self.g, [0, 1, 2])
        a = parsed.to_rule.to_symbols[0]
        b = parsed.to_rule.to_symbols[1]
        c = b.to_rule.to_symbols[0]
        d = b.to_rule.to_symbols[1]
        self.assertEqual(a.to_rule.to_symbols[0].s, 0)
        self.assertEqual(c.to_rule.to_symbols[0].s, 1)
        self.assertEqual(d.to_rule.to_symbols[0].s, 2)


if __name__ == '__main__':
    main()
