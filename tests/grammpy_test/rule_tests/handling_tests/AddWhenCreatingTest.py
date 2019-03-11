#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 22:03
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
    def test_addOneInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A])
        self.assertIn(A, gr.rules)

    def test_addTwoInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B])
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)

    def test_addThreeInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_addThreeInTuple(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=(A, B, C))
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_addThreeOneDelete(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=(A, B, C))
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)
        gr.rules.remove(B)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_addUndefined(self):
        with self.assertRaises(RuleNotDefinedException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[UndefinedRule])

    def test_addInvalid(self):
        with self.assertRaises(RuleSyntaxException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[InvalidRule])

    def test_addNotInside1(self):
        with self.assertRaises(TerminalDoesNotExistsException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[NotInsideRule1])

    def test_addNotInside2(self):
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[NotInsideRule2])

    def test_addUndefinedBetweenValid(self):
        with self.assertRaises(RuleNotDefinedException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[A, UndefinedRule, B])

    def test_addInvalidBetweenValid(self):
        with self.assertRaises(RuleSyntaxException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[A, InvalidRule, B])

    def test_addNotInside1BetweenValid(self):
        with self.assertRaises(TerminalDoesNotExistsException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[A, NotInsideRule1, B])

    def test_addNotInside2BetweenValid(self):
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr = Grammar(terminals=[0, 1, 2],
                         nonterminals=[N],
                         rules=[A, NotInsideRule2, B])


if __name__ == '__main__':
    main()
