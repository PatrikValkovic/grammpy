#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 14:54
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class SetOperationTest(TestCase):
    def test_intersection(self):
        gr = Grammar(nonterminals=[A, B, C])
        intersect = gr.nonterminals.intersection([B, C])
        self.assertEqual(intersect, {B, C})

    def test_intersectionOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        intersect = gr.nonterminals & {B, C}
        self.assertEqual(intersect, {B, C})

    def test_intersectionUpdate(self):
        gr = Grammar(nonterminals=[A, B, C])
        gr.nonterminals.intersection_update([B, C])
        self.assertEqual(gr.nonterminals, {B, C})

    def test_intersectionUpdateOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms &= {B, C}
        self.assertEqual(nonterms, {B, C})
        self.assertEqual(gr.nonterminals, {B, C})

    def test_difference(self):
        gr = Grammar(nonterminals=[A, B, C])
        difference = gr.nonterminals.difference([B, C])
        self.assertEqual(difference, {A})

    def test_differenceOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        difference = gr.nonterminals - {B, C}
        self.assertEqual(difference, {A})

    def test_differenceUpdate(self):
        gr = Grammar(nonterminals=[A, B, C])
        gr.nonterminals.difference_update([B, C])
        self.assertEqual(gr.nonterminals, {A})

    def test_differenceUpdateOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms -= {B, C}
        self.assertEqual(nonterms, {A})
        self.assertEqual(gr.nonterminals, {A})

    def test_union(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals.union([A, B])
        self.assertEqual(union, {A, B, C})

    def test_unionOperator(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals | {A, B}
        self.assertEqual(union, {A, B, C})

    def test_unionUpdate(self):
        gr = Grammar(nonterminals=[B, C])
        gr.nonterminals.update([A, B])
        self.assertEqual(gr.nonterminals, {A, B, C})

    def test_unionUpdateOperator(self):
        gr = Grammar(nonterminals=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms |= {A, B}
        self.assertEqual(nonterms, {A, B, C})
        self.assertEqual(gr.nonterminals, {A, B, C})

    def test_symDifference(self):
        gr = Grammar(nonterminals=[B, C])
        diff = gr.nonterminals.symmetric_difference([A, B])
        self.assertEqual(diff, {A, C})

    def test_symDifferenceOperator(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals ^ {A, B}
        self.assertEqual(union, {A, C})

    def test_symDifferenceUpdate(self):
        gr = Grammar(nonterminals=[B, C])
        gr.nonterminals.symmetric_difference_update([A, B])
        self.assertEqual(gr.nonterminals, {A, C})

    def test_symDifferenceUpdateOperator(self):
        gr = Grammar(nonterminals=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms ^= {A, B}
        self.assertEqual(nonterms, {A, C})
        self.assertEqual(gr.nonterminals, {A, C})


if __name__ == '__main__':
    main()
