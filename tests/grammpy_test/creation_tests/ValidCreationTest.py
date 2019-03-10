#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:00
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy import *


class ValidCreationTest(TestCase):
    def test_createEmptyGrammar(self):
        grammar = Grammar()

    def test_createWithTerminals(self):
        grammar = Grammar(terminals=[0, 1, 2, 'asdf', ValidCreationTest])
        self.assertEqual(len(grammar.terminals), 5)
        self.assertIn(0, grammar.terminals)
        self.assertIn(1, grammar.terminals)
        self.assertIn(2, grammar.terminals)
        self.assertIn('asdf', grammar.terminals)
        self.assertIn(ValidCreationTest, grammar.terminals)

    def test_createWithTerminalMultipleTimes(self):
        grammar = Grammar(terminals=[0, 1, 2, 'asdf', 2, ValidCreationTest])
        self.assertEqual(len(grammar.terminals), 5)
        self.assertIn(0, grammar.terminals)
        self.assertIn(1, grammar.terminals)
        self.assertIn(2, grammar.terminals)
        self.assertIn('asdf', grammar.terminals)
        self.assertIn(ValidCreationTest, grammar.terminals)

    def test_createWithNonterminals(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        grammar = Grammar(nonterminals=[A, B, C])
        self.assertEqual(len(grammar.nonterminals), 3)
        self.assertIn(A, grammar.nonterminals)
        self.assertIn(B, grammar.nonterminals)
        self.assertIn(C, grammar.nonterminals)

    def test_createWithSomeNonterminalMultipleTimes(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        grammar = Grammar(nonterminals=[B, A, B, C])
        self.assertEqual(len(grammar.nonterminals), 3)
        self.assertIn(A, grammar.nonterminals)
        self.assertIn(B, grammar.nonterminals)
        self.assertIn(C, grammar.nonterminals)

    def test_createWithTerminalsAndNonterminals(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        grammar = Grammar(terminals=[0, 1, 2, 'asdf', ValidCreationTest],
                          nonterminals=[A, B, C])
        self.assertEqual(len(grammar.terminals), 5)
        self.assertIn(0, grammar.terminals)
        self.assertIn(1, grammar.terminals)
        self.assertIn(2, grammar.terminals)
        self.assertIn('asdf', grammar.terminals)
        self.assertIn(ValidCreationTest, grammar.terminals)
        self.assertEqual(len(grammar.nonterminals), 3)
        self.assertIn(A, grammar.nonterminals)
        self.assertIn(B, grammar.nonterminals)
        self.assertIn(C, grammar.nonterminals)

    def test_createWithOneRule(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        class R(Rule): rule=([A], [2, B])
        grammar = Grammar(terminals=[0, 1, 2],
                          nonterminals=[A, B, C],
                          rules=[R])
        self.assertEqual(len(grammar.rules), 1)
        self.assertIn(R, grammar.rules)
        class R2(Rule): rule = ([A], [2, B])
        self.assertIn(R2, grammar.rules)

    def test_createWithThreeRule(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        class R1(Rule): rule=([A], [2, B])
        class R2(Rule): rule=([B], [1, A])
        class R3(Rule): rule=([C], [0, C])
        grammar = Grammar(terminals=[0, 1, 2],
                          nonterminals=[A, B, C],
                          rules=[R1, R2, R3])
        self.assertEqual(len(grammar.rules), 3)
        self.assertIn(R1, grammar.rules)
        self.assertIn(R2, grammar.rules)
        self.assertIn(R3, grammar.rules)
        class R1_(Rule): rule=([A], [2, B])
        class R2_(Rule): rule=([B], [1, A])
        class R3_(Rule): rule=([C], [0, C])
        self.assertIn(R1_, grammar.rules)
        self.assertIn(R2_, grammar.rules)
        self.assertIn(R3_, grammar.rules)

    def test_createWithOneRuleIncludingThree(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        class R(Rule): rules=[
            ([A], [2, B]),
            ([B], [1, A]),
            ([C], [0, C])
        ]
        grammar = Grammar(terminals=[0, 1, 2],
                          nonterminals=[A, B, C],
                          rules=[R])
        self.assertEqual(len(grammar.rules), 3)
        self.assertIn(R, grammar.rules)
        class R1_(Rule): rule=([A], [2, B])
        class R2_(Rule): rule=([B], [1, A])
        class R3_(Rule): rule=([C], [0, C])
        self.assertIn(R1_, grammar.rules)
        self.assertIn(R2_, grammar.rules)
        self.assertIn(R3_, grammar.rules)


if __name__ == '__main__':
    main()
