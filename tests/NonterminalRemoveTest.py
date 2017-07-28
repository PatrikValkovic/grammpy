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


class NonterminalRemoveTest(TestCase):
    def test_removeOne(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertTrue(gr.have_nonterm(Second))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(TempClass))

    def test_removeSecond(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm(Second)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertTrue(gr.have_nonterm(TempClass))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(Second))

    def test_removeTwo(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm(Second)
        self.assertEqual(gr.nonterms_count(), 2)
        self.assertTrue(gr.have_nonterm(TempClass))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(Second))
        gr.remove_nonterm(TempClass)
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(Second))

    def test_removeTwoInArray(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm([Second, TempClass])
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(Second))

    def test_removeTwoInTuple(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm((Second, TempClass))
        self.assertEqual(gr.nonterms_count(), 1)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertTrue(gr.have_nonterm(Third))
        self.assertFalse(gr.have_nonterm(Second))

    def test_removeAllWithoutParam(self):
        gr = Grammar()
        gr.add_term([TempClass, Second, Third])
        self.assertEqual(gr.nonterms_count(), 3)
        gr.remove_nonterm()
        self.assertEqual(gr.nonterms_count(), 0)
        self.assertFalse(gr.have_nonterm(TempClass))
        self.assertFalse(gr.have_nonterm(Second))
        self.assertFalse(gr.have_nonterm(Third))

    def test_removeEmptyGrammar(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        gr.remove_term()
        self.assertEqual(gr.terms_count(), 0)


if __name__ == '__main__':
    main()
