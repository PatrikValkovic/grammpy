#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 15:13
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class SetOperationsWithoutNonterminalTest(TestCase):
    def test_intersection(self):
        gr = Grammar(nonterminals=[A, B, C])
        intersect = gr.nonterminals.intersection([B, C, 0])
        self.assertEqual(intersect, {B, C})

    def test_intersectionOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        intersect = gr.nonterminals & {B, C, 0}
        self.assertEqual(intersect, {B, C})

    def test_intersectionUpdate(self):
        gr = Grammar(nonterminals=[A, B, C])
        gr.nonterminals.intersection_update([B, C, 0])
        self.assertEqual(gr.nonterminals, {B, C})

    def test_intersectionUpdateOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms &= {B, C, 0}
        self.assertEqual(nonterms, {B, C})
        self.assertEqual(gr.nonterminals, {B, C})

    def test_difference(self):
        gr = Grammar(nonterminals=[A, B, C])
        difference = gr.nonterminals.difference([B, C, 0])
        self.assertEqual(difference, {A})

    def test_differenceOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        difference = gr.nonterminals - {B, C, 0}
        self.assertEqual(difference, {A})

    def test_differenceUpdate(self):
        gr = Grammar(nonterminals=[A, B, C])
        gr.nonterminals.difference_update([B, C, 0])
        self.assertEqual(gr.nonterminals, {A})

    def test_differenceUpdateOperator(self):
        gr = Grammar(nonterminals=[A, B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        nonterms -= {B, C, 0}
        self.assertEqual(nonterms, {A})
        self.assertEqual(gr.nonterminals, {A})

    def test_union(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals.union([A, B, 0])
        self.assertEqual(union, {A, B, C, 0})

    def test_unionOperator(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals | {A, B, 0}
        self.assertEqual(union, {A, B, C, 0})

    def test_unionUpdate(self):
        gr = Grammar(nonterminals=[B, C])
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.update([A, B, 0])

    def test_unionUpdateOperator(self):
        gr = Grammar(nonterminals=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        with self.assertRaises(NotNonterminalException):
            nonterms |= {A, B, 0}

    def test_symDifference(self):
        gr = Grammar(nonterminals=[B, C])
        diff = gr.nonterminals.symmetric_difference([A, B, 0])
        self.assertEqual(diff, {A, C, 0})

    def test_symDifferenceOperator(self):
        gr = Grammar(nonterminals=[B, C])
        union = gr.nonterminals ^ {A, B, 0}
        self.assertEqual(union, {A, C, 0})

    def test_symDifferenceUpdate(self):
        gr = Grammar(nonterminals=[B, C])
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.symmetric_difference_update([A, B, 0])

    def test_symDifferenceUpdateOperator(self):
        gr = Grammar(nonterminals=[B, C])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        nonterms = gr.nonterminals
        with self.assertRaises(NotNonterminalException):
            nonterms ^= {A, B, 0}


if __name__ == '__main__':
    main()
