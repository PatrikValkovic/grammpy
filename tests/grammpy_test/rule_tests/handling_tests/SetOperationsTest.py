#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 21:09
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal, Rule


class N(Nonterminal): pass
class A(Rule): rule=([N], [0])
class B(Rule): rule=([N], [1])
class C(Rule): rule=([N], [2])


class SetOperationTest(TestCase):
    def test_intersection(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules.intersection([B, C])
        self.assertEqual(intersect, {B, C})

    def test_intersectionOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        intersect = gr.rules & {B, C}
        self.assertEqual(intersect, {B, C})

    def test_intersectionUpdate(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.intersection_update([B, C])
        self.assertEqual(gr.rules, {B, C})

    def test_intersectionUpdateOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules &= {B, C}
        self.assertEqual(rules, {B, C})
        self.assertEqual(gr.rules, {B, C})

    def test_difference(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules.difference([B, C])
        self.assertEqual(difference, {A})

    def test_differenceOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        difference = gr.rules - {B, C}
        self.assertEqual(difference, {A})

    def test_differenceUpdate(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        gr.rules.difference_update([B, C])
        self.assertEqual(gr.rules, {A})

    def test_differenceUpdateOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules -= {B, C}
        self.assertEqual(rules, {A})
        self.assertEqual(gr.rules, {A})

    def test_union(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules.union([A, B])
        self.assertEqual(union, {A, B, C})

    def test_unionOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules | {A, B}
        self.assertEqual(union, {A, B, C})

    def test_unionUpdate(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        gr.rules.update([A, B])
        self.assertEqual(gr.rules, {A, B, C})

    def test_unionUpdateOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules |= {A, B}
        self.assertEqual(rules, {A, B, C})
        self.assertEqual(gr.rules, {A, B, C})

    def test_symDifference(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        diff = gr.rules.symmetric_difference([A, B])
        self.assertEqual(diff, {A, C})

    def test_symDifferenceOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        union = gr.rules ^ {A, B}
        self.assertEqual(union, {A, C})

    def test_symDifferenceUpdate(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        gr.rules.symmetric_difference_update([A, B])
        self.assertEqual(gr.rules, {A, C})

    def test_symDifferenceUpdateOperator(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N],
                     rules=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        rules = gr.rules
        rules ^= {A, B}
        self.assertEqual(rules, {A, C})
        self.assertEqual(gr.rules, {A, C})


if __name__ == '__main__':
    main()
