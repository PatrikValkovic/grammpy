#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar
from grammpy.Terminal import Terminal
from grammpy import Nonterminal


class TempClass(Nonterminal):
    pass


class Second(Nonterminal):
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
        gr.add_nonterm(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_nonterm(TempClass))
        self.assertIsNotNone(gr.nonterm(TempClass))
        self.assertTrue(issubclass(gr.nonterm(TempClass), Terminal))
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

    # TODO write
    def test_addInArray(self):
        gr = Grammar()
        gr.add_term([0, 'asdf', TempClass])
        self.assertEqual(gr.terms_count(), 3)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').s, 'asdf')
        self.assertIsNotNone(gr.get_term(TempClass))
        self.assertIsNotNone(gr.term(TempClass))
        self.assertTrue(isinstance(gr.term(TempClass), Terminal))
        self.assertEqual(gr.term(TempClass).s, TempClass)

    def test_oneSeparateTwoTuple(self):
        gr = Grammar()
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        gr.add_term(('asdf', TempClass))
        self.assertEqual(gr.terms_count(), 3)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').s, 'asdf')
        self.assertIsNotNone(gr.get_term(TempClass))
        self.assertIsNotNone(gr.term(TempClass))
        self.assertTrue(isinstance(gr.term(TempClass), Terminal))
        self.assertEqual(gr.term(TempClass).s, TempClass)

    def test_equalGetTermAndTermMethods(self):
        gr = Grammar()
        ins = TempClass()
        gr.add_term(ins)
        self.assertEqual(gr.terms_count(), 1)
        self.assertEqual(gr.get_term(ins).s, ins)
        self.assertEqual(gr.term(ins).s, ins)
        self.assertEqual(gr.term(ins).s, gr.get_term(ins).s)


if __name__ == '__main__':
    main()
