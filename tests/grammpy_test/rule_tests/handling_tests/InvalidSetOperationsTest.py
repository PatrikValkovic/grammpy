#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 21:16
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal, Rule
from grammpy.exceptions import NotRuleException, RuleNotDefinedException, RuleSyntaxException, TerminalDoesNotExistsException, NonterminalDoesNotExistsException


class N(Nonterminal): pass
class X(Nonterminal): pass
class A(Rule): rule=([N], [0])
class B(Rule): rule=([N], [1])
class C(Rule): rule=([N], [2])
class UndefinedRule(Rule): pass
class InvalidRule(Rule): rule=(N, [0, 1])
class NotInsideRule1(Rule): rule=([N], [3])
class NotInsideRule2(Rule): rule=([X], [0])


class SetOperationsWithoutNonterminalTest(TestCase):
    def test_intersectionWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules.intersection([B, C, 0])
        self.assertEqual(intersect, {B, C})

    def test_intersectionOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules & {B, C, 0}
        self.assertEqual(intersect, {B, C})

    def test_intersectionUpdateWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.intersection_update([B, C, 0])
        self.assertEqual(gr.rules, {B, C})

    def test_intersectionUpdateOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules &= {B, C, 0}
        self.assertEqual(rules, {B, C})
        self.assertEqual(gr.rules, {B, C})

    def test_intersectionWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules.intersection([B, C, InvalidRule])
        self.assertEqual(intersect, {B, C})

    def test_intersectionOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules & {B, C, InvalidRule}
        self.assertEqual(intersect, {B, C})

    def test_intersectionUpdateWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.intersection_update([B, C, InvalidRule])
        self.assertEqual(gr.rules, {B, C})

    def test_intersectionUpdateOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules &= {B, C, 0, InvalidRule}
        self.assertEqual(rules, {B, C})
        self.assertEqual(gr.rules, {B, C})

    def test_differenceWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules.difference([B, C, 0])
        self.assertEqual(difference, {A})

    def test_differenceOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules - {B, C, 0}
        self.assertEqual(difference, {A})

    def test_differenceUpdateWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.difference_update([B, C, 0])
        self.assertEqual(gr.rules, {A})

    def test_differenceUpdateOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules -= {B, C, 0}
        self.assertEqual(rules, {A})
        self.assertEqual(gr.rules, {A})

    def test_differenceWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules.difference([B, C, InvalidRule])
        self.assertEqual(difference, {A})

    def test_differenceOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules - {B, C, InvalidRule}
        self.assertEqual(difference, {A})

    def test_differenceUpdateWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.difference_update([B, C, InvalidRule])
        self.assertEqual(gr.rules, {A})

    def test_differenceUpdateOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules -= {B, C, InvalidRule}
        self.assertEqual(rules, {A})
        self.assertEqual(gr.rules, {A})

    def test_unionWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules.union([A, B, 0])
        self.assertEqual(union, {A, B, C, 0})

    def test_unionOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules | {A, B, 0}
        self.assertEqual(union, {A, B, C, 0})

    def test_unionUpdateWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(NotRuleException):
            gr.rules.update([A, B, 0])

    def test_unionUpdateOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(NotRuleException):
            rules |= {A, B, 0}

    def test_unionWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules.union([A, B, InvalidRule])
        self.assertEqual(union, {A, B, C, InvalidRule})

    def test_unionOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules | {A, B, InvalidRule}
        self.assertEqual(union, {A, B, C, InvalidRule})

    def test_unionUpdateWithUndefinedRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.update([A, B, UndefinedRule])

    def test_unionUpdateWithInvalidRule1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(RuleSyntaxException):
            gr.rules.update([A, B, InvalidRule])

    def test_unionUpdateWithNotInsideRule1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.update([A, B, NotInsideRule1])

    def test_unionUpdateWithNotInsideRule2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.update([A, B, NotInsideRule2])

    def test_unionUpdateOperatorWithUndefinedRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        rules = gr.rules
        with self.assertRaises(RuleNotDefinedException):
            rules |= {A, B, UndefinedRule}

    def test_unionUpdateOperatorWithInvalidRule1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        rules = gr.rules
        with self.assertRaises(RuleSyntaxException):
            rules |= {A, B, InvalidRule}

    def test_unionUpdateOperatorWithNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        rules = gr.rules
        with self.assertRaises(TerminalDoesNotExistsException):
            rules |= {A, B, NotInsideRule1}

    def test_unionUpdateOperatorWithNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        rules = gr.rules
        with self.assertRaises(NonterminalDoesNotExistsException):
            rules |= {A, B, NotInsideRule2}

    def test_symDifferenceWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        diff = gr.rules.symmetric_difference([A, B, 0])
        self.assertEqual(diff, {A, C, 0})

    def test_symDifferenceOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules ^ {A, B, 0}
        self.assertEqual(union, {A, C, 0})

    def test_symDifferenceUpdateWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(NotRuleException):
            gr.rules.symmetric_difference_update([A, B, 0])

    def test_symDifferenceUpdateOperatorWithTerm(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(NotRuleException):
            rules ^= {A, B, 0}

    def test_symDifferenceWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        diff = gr.rules.symmetric_difference([A, B, InvalidRule])
        self.assertEqual(diff, {A, C, InvalidRule})

    def test_symDifferenceOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules ^ {A, B, InvalidRule}
        self.assertEqual(union, {A, C, InvalidRule})

    def test_symDifferenceUpdateWithUndefinedRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(RuleNotDefinedException):
            gr.rules.symmetric_difference_update([A, B, UndefinedRule])

    def test_symDifferenceUpdateWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(RuleSyntaxException):
            gr.rules.symmetric_difference_update([A, B, InvalidRule])

    def test_symDifferenceUpdateWithNotInsideRule1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(TerminalDoesNotExistsException):
            gr.rules.symmetric_difference_update([A, B, NotInsideRule1])

    def test_symDifferenceUpdateWithNotInsideRule2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        with self.assertRaises(NonterminalDoesNotExistsException):
            gr.rules.symmetric_difference_update([A, B, NotInsideRule2])

    def test_symDifferenceUpdateOperatorWithUndefinedRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(RuleNotDefinedException):
            rules ^= {A, B, UndefinedRule}

    def test_symDifferenceUpdateOperatorWithInvalidRule(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(RuleSyntaxException):
            rules ^= {A, B, InvalidRule}

    def test_symDifferenceUpdateOperatorWithNotInside1(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(TerminalDoesNotExistsException):
            rules ^= {A, B, NotInsideRule1}

    def test_symDifferenceUpdateOperatorWithNotInside2(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        with self.assertRaises(NonterminalDoesNotExistsException):
            rules ^= {A, B, NotInsideRule2}


if __name__ == '__main__':
    main()
