#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 15:16
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
class SAB(Rule): rule=([S], [A, B])
class AAC(Rule): rule=([A], [A, C])
class B1(Rule): rule=([B], [1])
class C0(Rule): rule=([C], [0])
class A2(Rule): rule=([A], [2])




class TwoNonterminalsTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = None

    def setUp(self):
        self.g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[S, A, B, C],
                    rules=[SAB, AAC, B1, C0, A2],
                    start_symbol=S)

    def test_shouldParse(self):
        parsed = cyk(self.g, [2, 1])

    def test_shouldParseCorrectTypesForNoLoop(self):
        parsed = cyk(self.g, [2, 1])
        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, SAB)
        self.assertIsInstance(parsed.to_rule.to_nonterms[0], A)
        self.assertIsInstance(parsed.to_rule.to_nonterms[1], B)
        a = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        self.assertIsInstance(a.to_rule, A2)
        self.assertIsInstance(a.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(b.to_rule, B1)
        self.assertIsInstance(b.to_rule.to_nonterms[0], Terminal)

    def test_shouldParseCorrectSymbolsNoLoop(self):
        parsed = cyk(self.g, [2, 1])
        a = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        self.assertEqual(a.to_rule.to_nonterms[0].s, 2)
        self.assertEqual(b.to_rule.to_nonterms[0].s, 1)

    def test_shouldParseCorrectTypesForOneLoop(self):
        parsed = cyk(self.g, [2, 0, 1])
        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, SAB)
        self.assertIsInstance(parsed.to_rule.to_nonterms[0], A)
        self.assertIsInstance(parsed.to_rule.to_nonterms[1], B)
        a = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        self.assertIsInstance(b.to_rule, B1)
        self.assertIsInstance(b.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(a.to_rule, AAC)
        self.assertIsInstance(a.to_rule.to_nonterms[0], A)
        self.assertIsInstance(a.to_rule.to_nonterms[1], C)
        a = a.to_rule.to_nonterms[0]
        c = a.to_rule.to_nonterms[1]
        self.assertIsInstance(a.to_rule, A2)
        self.assertIsInstance(a.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(c.to_rule, C0)
        self.assertIsInstance(c.to_rule.to_nonterms[0], Terminal)

    def test_shouldParseCorrectSymbolsOneLoop(self):
        parsed = cyk(self.g, [2, 0, 1])
        a = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        a = a.to_rule.to_nonterms[0]
        c = a.to_rule.to_nonterms[1]
        self.assertEqual(a.to_rule.to_nonterms[0].s, 2)
        self.assertEqual(b.to_rule.to_nonterms[0].s, 1)
        self.assertEqual(c.to_rule.to_nonterms[0].s, 0)

    def test_shouldParseCorrectTypesForThreeLoops(self):
        parsed = cyk(self.g, [2, 0, 0, 0, 1])
        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, SAB)
        self.assertIsInstance(parsed.to_rule.to_nonterms[0], A)
        self.assertIsInstance(parsed.to_rule.to_nonterms[1], B)
        a1 = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        self.assertIsInstance(b.to_rule, B1)
        self.assertIsInstance(b.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(a1.to_rule, AAC)
        self.assertIsInstance(a1.to_rule.to_nonterms[0], A)
        self.assertIsInstance(a1.to_rule.to_nonterms[1], C)
        a2 = a1.to_rule.to_nonterms[0]
        c1 = a1.to_rule.to_nonterms[1]
        self.assertIsInstance(c1.to_rule, C0)
        self.assertIsInstance(c1.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(a2.to_rule, AAC)
        self.assertIsInstance(a2.to_rule.to_nonterms[0], A)
        self.assertIsInstance(a2.to_rule.to_nonterms[1], C)
        a3 = a2.to_rule.to_nonterms[0]
        c2 = a2.to_rule.to_nonterms[1]
        self.assertIsInstance(c2.to_rule, C0)
        self.assertIsInstance(c2.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(a3.to_rule, AAC)
        self.assertIsInstance(a3.to_rule.to_nonterms[0], A)
        self.assertIsInstance(a3.to_rule.to_nonterms[1], C)
        a4 = a1.to_rule.to_nonterms[0]
        c3 = a3.to_rule.to_nonterms[1]
        self.assertIsInstance(c3.to_rule, C0)
        self.assertIsInstance(c3.to_rule.to_nonterms[0], Terminal)
        self.assertIsInstance(a4.to_rule, A2)
        self.assertIsInstance(a4.to_rule.to_nonterms[0], Terminal)

    def test_shouldParseCorrectSymbolsThreeLoops(self):
        parsed = cyk(self.g, [2, 0, 1])
        a1 = parsed.to_rule.to_nonterms[0]
        b = parsed.to_rule.to_nonterms[1]
        a2 = a1.to_rule.to_nonterms[0]
        c1 = a1.to_rule.to_nonterms[1]
        a3 = a2.to_rule.to_nonterms[0]
        c2 = a2.to_rule.to_nonterms[1]
        a4 = a1.to_rule.to_nonterms[0]
        c3 = a3.to_rule.to_nonterms[1]
        self.assertEqual(a4.to_rule.to_nonterms[0].s, 2)
        self.assertEqual(c3.to_rule.to_nonterms[0].s, 0)
        self.assertEqual(c2.to_rule.to_nonterms[0].s, 0)
        self.assertEqual(c1.to_rule.to_nonterms[0].s, 0)
        self.assertEqual(b.to_rule.to_nonterms[0].s, 1)







if __name__ == '__main__':
    main()
