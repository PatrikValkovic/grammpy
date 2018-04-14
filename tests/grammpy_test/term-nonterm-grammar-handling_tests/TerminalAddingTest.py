#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Grammar
from grammpy import Terminal


class TempClass:
    pass


class TerminalAddingTest(TestCase):

    def test_haveTermEmpty(self):
        gr = Grammar()
        self.assertFalse(gr.have_term(TempClass))
        self.assertFalse(gr.have_term(1))
        self.assertFalse(gr.have_term('asdf'))

    def test_getTermEmpty(self):
        gr = Grammar()
        self.assertIsNone(gr.get_term(TempClass))
        self.assertIsNone(gr.get_term(1))
        self.assertIsNone(gr.get_term('asdf'))

    def test_correctAddOne(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        self.assertFalse(gr.have_term(0))
        self.assertIsNone(gr.get_term(0))
        self.assertIsNone(gr.term(0))
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).symbol(), 0)

    def test_correctAddTwo(self):
        gr = Grammar()
        self.assertEqual(gr.terms_count(), 0)
        self.assertIsNone(gr.get_term(0))
        self.assertIsNone(gr.term(0))
        self.assertIsNone(gr.get_term('asdf'))
        self.assertIsNone(gr.term('asdf'))
        gr.add_term(0)
        self.assertEqual(gr.terms_count(), 1)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNone(gr.get_term('asdf'))
        self.assertIsNone(gr.term('asdf'))
        gr.add_term('asdf')
        self.assertEqual(gr.terms_count(), 2)
        self.assertIsNotNone(gr.get_term(0))
        self.assertIsNotNone(gr.term(0))
        self.assertTrue(isinstance(gr.term(0), Terminal))
        self.assertEqual(gr.term(0).s, 0)
        self.assertIsNotNone(gr.get_term('asdf'))
        self.assertIsNotNone(gr.term('asdf'))
        self.assertTrue(isinstance(gr.term('asdf'), Terminal))
        self.assertEqual(gr.term('asdf').s, 'asdf')

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
        self.assertEqual(gr.terms_count(),1)
        self.assertEqual(gr.get_term(ins).s,ins)
        self.assertEqual(gr.term(ins).s,ins)
        self.assertEqual(gr.term(ins).s,gr.get_term(ins).s)


if __name__ == '__main__':
    main()