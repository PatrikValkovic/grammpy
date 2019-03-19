#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 21:45
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
class UndefinedRule(Rule): pass
class InvalidRule(Rule): rule=(N, [0, 1])
class NotInsideRule1(Rule): rule=([N], [3])
class NotInsideRule2(Rule): rule=([X], [0])


class AddingTest(TestCase):

    def test_haveEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)

    def test_correctAddOne(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertEqual(gr.rules.size(), 0)
        self.assertEqual(len(gr.rules), 0)
        self.assertNotIn(A, gr.rules)
        gr.rules.add(A)
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertIn(A, gr.rules)

    def test_correctAddTwo(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertEqual(gr.rules.size(), 0)
        self.assertEqual(len(gr.rules), 0)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        gr.rules.add(A)
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        gr.rules.add(B)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)

    def test_addThreeAsParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addThreeAsArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(*[A, B, C])
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_oneSeparateTwoTuple(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)
        gr.rules.add(*(B, C))
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addSameTwiceInParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, A, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addSameTwiceInSequence(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, C)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        gr.rules.add(A, B)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addUndefined(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.add(UndefinedRule)

    def test_addInvalid(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleSyntaxException):
            gr.rules.add(InvalidRule)

    def test_addNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.add(NotInsideRule1)

    def test_addNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.add(NotInsideRule2)

    def test_addUndefinedAsSecond(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.add(UndefinedRule)

    def test_addInvalidAsSecond(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(RuleSyntaxException):
            gr.rules.add(InvalidRule)

    def test_addNotInside1AsSecond(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.add(NotInsideRule1)

    def test_addNotInside2AsSecond(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.add(NotInsideRule2)

    def test_addUndefinedInParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.add(B, UndefinedRule)

    def test_addInvalidInParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(RuleSyntaxException):
            gr.rules.add(B, InvalidRule)

    def test_addNotInside1InParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.add(B, NotInsideRule1)

    def test_addNotInside2InParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A)
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.add(B, NotInsideRule2)


if __name__ == '__main__':
    main()
