#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.03.2019 22:50
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Grammar


class TempClass:
    pass


class SetOperationTest(TestCase):
    def test_intersection(self):
        gr = Grammar(terminals=[0, 'asdf'])
        intersect = gr.terminals.intersection(['asdf', TempClass])
        self.assertEqual(intersect, {'asdf'})

    def test_intersectionOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        intersect = gr.terminals & {'asdf', TempClass}
        self.assertEqual(intersect, {'asdf'})

    def test_intersectionUpdate(self):
        gr = Grammar(terminals=[0, 'asdf'])
        gr.terminals.intersection_update(['asdf', TempClass])
        self.assertEqual(gr.terminals, {'asdf'})

    def test_intersectionUpdateOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        terms = gr.terminals
        terms &= {'asdf', TempClass}
        self.assertEqual(terms, {'asdf'})
        self.assertEqual(gr.terminals, {'asdf'})

    def test_difference(self):
        gr = Grammar(terminals=[0, 'asdf'])
        difference = gr.terminals.difference(['asdf', TempClass])
        self.assertEqual(difference, {0})

    def test_differenceOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        difference = gr.terminals - {'asdf', TempClass}
        self.assertEqual(difference, {0})

    def test_differenceUpdate(self):
        gr = Grammar(terminals=[0, 'asdf'])
        gr.terminals.difference_update(['asdf', TempClass])
        self.assertEqual(gr.terminals, {0})

    def test_differenceUpdateOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        terms = gr.terminals
        terms -= {'asdf', TempClass}
        self.assertEqual(terms, {0})
        self.assertEqual(gr.terminals, {0})

    def test_union(self):
        gr = Grammar(terminals=[0, 'asdf'])
        union = gr.terminals.union(['asdf', TempClass])
        self.assertEqual(union, {0, 'asdf', TempClass})

    def test_unionOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        union = gr.terminals | {'asdf', TempClass}
        self.assertEqual(union, {0, 'asdf', TempClass})

    def test_unionUpdate(self):
        gr = Grammar(terminals=[0, 'asdf'])
        gr.terminals.update(['asdf', TempClass])
        self.assertEqual(gr.terminals, {0, 'asdf', TempClass})

    def test_unionUpdateOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        terms = gr.terminals
        terms |= {'asdf', TempClass}
        self.assertEqual(terms, {0, 'asdf', TempClass})
        self.assertEqual(gr.terminals, {0, 'asdf', TempClass})

    def test_symDifference(self):
        gr = Grammar(terminals=[0, 'asdf'])
        diff = gr.terminals.symmetric_difference(['asdf', TempClass])
        self.assertEqual(diff, {0, TempClass})

    def test_symDifferenceOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        union = gr.terminals ^ {'asdf', TempClass}
        self.assertEqual(union, {0, TempClass})

    def test_symDifferenceUpdate(self):
        gr = Grammar(terminals=[0, 'asdf'])
        gr.terminals.symmetric_difference_update(['asdf', TempClass])
        self.assertEqual(gr.terminals, {0, TempClass})

    def test_symDifferenceUpdateOperator(self):
        gr = Grammar(terminals=[0, 'asdf'])
        # Because Python is PIECE OF SHIT that can't handle FUCKING OPERATOR on property
        # if there isn't FUCKING SETTER. Storing the property in variable na CALLING FUCKING
        # OPERATOR on that variable works and MODIFY FUCKING PROPERTY ITSELF.
        # Burn in FUCKING HELL!!!!
        terms = gr.terminals
        terms ^= {'asdf', TempClass}
        self.assertEqual(terms, {0, TempClass})
        self.assertEqual(gr.terminals, {0, TempClass})


if __name__ == '__main__':
    main()
