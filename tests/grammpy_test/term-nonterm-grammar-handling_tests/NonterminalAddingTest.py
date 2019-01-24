#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy.old_api import Grammar
from grammpy.old_api import Nonterminal


class TempClass(Nonterminal):
    pass


class Second(Nonterminal):
    pass


class Third(Nonterminal):
    pass


class NonterminalAddingTest(TestCase):
    def test_haveNontermEmpty(self):
        gr = Grammar()
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertEqual(gr.nonterms_count(), 0)

    def test_getNontermEmpty(self):
        gr = Grammar()
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.nonterm(TempClass))

    def test_correctAddOne(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.nonterm(TempClass))
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertTrue(issubclass(gr.nonterm(TempClass), TempClass))
        self.assertEqual(hash(gr.nonterm(TempClass)), hash(TempClass))

    def test_correctAddTwo(self):
        gr = Grammar()
        self.assertEqual(gr.nonterms_count(), 0)
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(Second))
        self.assertIsNone(gr.nonterm(Second))
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertTrue(issubclass(gr.nonterm(TempClass), Nonterminal))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        self.assertIsNone(gr.get_nonterm(Second))
        self.assertIsNone(gr.nonterm(Second))
        gr.add_nonterm(Second)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertTrue(issubclass(gr.nonterm(TempClass), Nonterminal))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertTrue(issubclass(gr.nonterm(Second), Nonterminal))
        self.assertEqual(gr.nonterm(Second), Second)

    def test_addInArray(self):
        gr = Grammar()
        gr.add_nonterm([Second, TempClass])
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        self.assertIsNotNone(gr.get_nonterm(Second))
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertEqual(gr.nonterm(Second), Second)
        self.assertIsNone(gr.get_nonterm(Third))
        self.assertIsNone(gr.nonterm(Third))

    def test_oneSeparateTwoTuple(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertEqual(gr.nonterm(TempClass), TempClass)
        gr.add_nonterm((Second, Third))
        self.assertEqual(gr.nonterms_count(), 3)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertIsNotNone(gr.get_nonterm(Second))
        self.assertIsNotNone(gr.nonterm(Second))
        self.assertIsNotNone(gr.get_nonterm(Third))
        self.assertIsNotNone(gr.nonterm(Third))

if __name__ == '__main__':
    main()
