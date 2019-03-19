#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 22:18
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal, Rule
from grammpy.exceptions import RuleNotDefinedException, RuleSyntaxException, TerminalDoesNotExistsException, NonterminalDoesNotExistsException


class N(Nonterminal): pass
class X(Nonterminal): pass
class A(Rule): rule=([N], [0])
class B(Rule): rule=([N], [1])
class C(Rule): rule=([N], [2])
class D(Rule): rule=([0], [1])
class UndefinedRule(Rule): pass
class InvalidRule(Rule): rule=(N, [0, 1])
class NotInsideRule1(Rule): rule=([N], [3])
class NotInsideRule2(Rule): rule=([X], [0])


class AddWhenCreatingTest(TestCase):
    def test_onEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)

    def test_haveOne(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)

    def test_haveMultiple(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_haveSome(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)

    def test_haveOnEmptyAndUndefined(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleNotDefinedException):
            UndefinedRule in gr.rules

    def test_haveOnEmptyAndInvalid(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleSyntaxException):
            InvalidRule in gr.rules

    def test_haveOnEmptyAndNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertNotIn(NotInsideRule1, gr.rules)

    def test_haveOnEmptyAndNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertNotIn(NotInsideRule2, gr.rules)

    def test_haveOnFillAndUndefined(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleNotDefinedException):
            UndefinedRule in gr.rules

    def test_haveOnFillAndInvalid(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleSyntaxException):
            InvalidRule in gr.rules

    def test_haveOnFillAndNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertNotIn(NotInsideRule1, gr.rules)

    def test_haveOnFillAndNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertNotIn(NotInsideRule2, gr.rules)


if __name__ == '__main__':
    main()
