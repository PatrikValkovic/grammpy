#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 23:31
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
class D(Rule): rule=([0], [2])
class UndefinedRule(Rule): pass
class InvalidRule(Rule): rule=(N, [0, 1])
class NotInsideRule1(Rule): rule=([N], [3])
class NotInsideRule2(Rule): rule=([X], [0])


class DiscardTest(TestCase):
    def test_removeOne(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(A)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertNotIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_removeTwo(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(A)
        gr.rules.discard(B)
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_removeTwoInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(*[A, B])
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_removeTwoInParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(*[A, B])
        self.assertEqual(gr.rules.size(), 1)
        self.assertEqual(len(gr.rules), 1)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_removeAll(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.clear()
        self.assertEqual(gr.rules.size(), 0)
        self.assertEqual(len(gr.rules), 0)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)
        self.assertNotIn(D, gr.rules)

    def test_removeEmptyGrammar(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertEqual(gr.rules.size(), 0)
        self.assertEqual(len(gr.rules), 0)
        gr.nonterminals.clear()
        self.assertEqual(gr.rules.size(), 0)
        self.assertEqual(len(gr.rules), 0)

    def test_removeSameElementMoreTimesInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(*[B, B])
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_removeSameElementMoreTimesAsParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(*[A, B, C])
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(B, B)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_removeSameElementMoreTimesSequentially(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(A)
        gr.rules.discard(A)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertNotIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_removeElementNotThere(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(D)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)

    def test_removeOneOfTheElementNotThere(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(gr.rules.size(), 3)
        self.assertEqual(len(gr.rules), 3)
        gr.rules.discard(B, D)
        self.assertEqual(gr.rules.size(), 2)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_removeUndefined(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.discard(UndefinedRule)

    def test_removeInvalid(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleSyntaxException):
            gr.rules.discard(InvalidRule)

    def test_removeNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule1)

    def test_removeNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule2)

    def test_removeUndefinedOnEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.discard(UndefinedRule)

    def test_removeInvalidOnEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(RuleSyntaxException):
            gr.rules.discard(InvalidRule)

    def test_removeNotInside1OnEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule1)

    def test_removeNotInside2OnEmpty(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule2)

    def test_removeUndefinedAsOneOfThem(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.discard(B, UndefinedRule)

    def test_removeInvalidAsOneOfThem(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleSyntaxException):
            gr.rules.discard(B, InvalidRule)

    def test_removeNotInside1AsOneOfThem(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.discard(B, NotInsideRule1)

    def test_removeNotInside2AsOneOfThem(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.discard(B, NotInsideRule2)

    def test_removeUndefinedMoreTimes(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.discard(UndefinedRule, UndefinedRule)

    def test_removeInvalidMoreTimes(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(RuleSyntaxException):
            gr.rules.discard(InvalidRule, InvalidRule)

    def test_removeNotInside1MoreTimes(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule1, NotInsideRule1)

    def test_removeNotInside2MoreTimes(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.discard(NotInsideRule2, NotInsideRule2)


if __name__ == '__main__':
    main()
