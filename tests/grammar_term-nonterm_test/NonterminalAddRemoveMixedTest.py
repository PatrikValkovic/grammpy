#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar
from grammpy import Nonterminal


class TempClass(Nonterminal):
    pass


class Second(Nonterminal):
    pass


class Third(Nonterminal):
    pass


class NonterminalAddRemoveMixedTest(TestCase):
    def test_add_remove_add_one(self):
        gr = Grammar()
        self.assertEqual(gr.nonterms_count(), 0)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.nonterm(TempClass))
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        gr.remove_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 0)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.nonterm(TempClass))

    def test_addTwoRemoveOneAndAddThird(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        gr.add_nonterm(Second)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.get_nonterm(TempClass), TempClass)
        self.assertIsNotNone(gr.get_nonterm(Second))
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertEqual(gr.get_nonterm(Second), Second)
        gr.remove_nonterm(Second)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        self.assertIsNone(gr.get_nonterm(Second))
        gr.add_term(Third)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.get_nonterm(TempClass), TempClass)
        self.assertFalse(gr.have_nonterm(Second))
        self.assertIsNone(gr.nonterm(Second))
        self.assertIsNotNone(gr.get_nonterm(Third))
        self.assertIsNotNone(gr.nonterm(Third))
        self.assertEqual(gr.get_nonterm(Third), Third)

    def test_addThreeRemoveTwoInArray(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        self.assertIsNotNone(gr.get_nonterm(Second))
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertEqual(gr.nonterm(Second), Second)
        self.assertIsNotNone(gr.get_nonterm(Third))
        self.assertIsNotNone(gr.nonterm(Third))
        self.assertEqual(gr.nonterm(Third), Third)
        gr.remove_term([Third, TempClass])
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertTrue(gr.have_nonterm(Second))
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertFalse(gr.have_nonterm(Third))
        gr.add_nonterm(Third)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertEqual(gr.nonterm(Second), Second)
        self.assertIsNotNone(gr.get_nonterm(Second))
        self.assertIsNotNone(gr.nonterm(Third))
        self.assertEqual(gr.nonterm(Third), Third)
        self.assertIsNotNone(gr.get_nonterm(Third))


if __name__ == '__main__':
    main()
